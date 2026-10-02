---
title: Task Queue
description: "Task queue built on FastAPI and Redis: the API accepts the work and answers right away, and workers run it in the background, with retries, and scale with a single flag."
permalink: /en/projects/task-queue/
---

<p class="crumbs"><a href="{{ '/en/tools/' | relative_url }}">{{ site.data.i18n[page.lang].services.back }}</a></p>

<section class="hero">
  <h1>Task Queue <span class="tag active">active</span></h1>
  <p class="lead">Distributed task queue: a <strong>FastAPI</strong> API server, a <strong>Redis</strong> broker (LPUSH/BRPOP), SQLite persistence and <strong>workers that scale horizontally</strong> with no code changes.</p>
  <div class="chip-row">
    <span class="tag">Python</span><span class="tag">FastAPI</span><span class="tag">Redis</span>
    <span class="tag">SQLAlchemy 2.0</span><span class="tag">Docker</span><span class="tag">APScheduler</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/task-queue" target="_blank" rel="noopener">Repo ↗</a>
    <a href="https://task-queue-tpdz.onrender.com" target="_blank" rel="noopener">Live demo ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">The design decision</p>
  <p>Workers never talk to the API. Each one blocks on <code>BRPOP</code> over the same Redis lists, and Redis hands each id to a single worker. That is why <code>--scale worker=N</code> in Docker Compose adds workers with no code or config changes.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">37</span><span class="lbl">tests, no Docker needed</span></div>
  <div class="stat"><span class="num">3</span><span class="lbl">Redis queues</span></div>
  <div class="stat"><span class="num">5</span><span class="lbl">states per task</span></div>
</div>

## The problem

A synchronous API has to finish the work before it can respond. When a task takes a while,
like sending an email, calling a slow third-party API or generating a report, the client is
left waiting and timeouts pile up as load grows.

A queue separates accepting the work from running it. `POST /tasks` validates the request,
stores it and returns `202` with the id. A worker in another process runs it later, and the
client checks the status with `GET /tasks/{id}`. There are two task types: `echo`, which logs a
message and waits one second, and `http_request`, which makes a real outbound HTTP call.

## Architecture

Locally it runs as three Docker Compose containers, started in dependency order with health
checks.

- **API (FastAPI):** runs a two-step pipeline. `ValidateStep` rejects unknown types with a `422` before anything is written. `EnqueueStep` inserts the row into SQLite as `pending`, runs `LPUSH` with the id and emits the `TASK_ENQUEUED` event.
- **Broker (Redis 7):** one list per queue (`tq:queue:high`, `tq:queue:default`, `tq:queue:low`). Only the id travels through Redis; the payload stays in the database.
- **Worker (×N):** blocks on `BRPOP`, loads the task, marks it `processing`, looks up the handler for its type in a registry and stores the result.
- **Persistence (SQLAlchemy 2.0 + SQLite):** status, retry counter, last error and timestamps for every task. The API and the workers mount the same volume holding the database file.
- **Scheduler (APScheduler):** every hour it deletes tasks completed more than 24 hours earlier. The window is set with `PURGE_COMPLETED_AFTER_HOURS`.

```
POST /tasks -> pending -> processing -> completed
                                     -> retrying -> back to the queue -> processing
                                     -> failed      (no retries left)
```

Side effects go through a synchronous `EventManager`. The worker emits `TASK_COMPLETED` and
`TASK_FAILED`, and `LogListener` subscribes to all three events. Adding an alert takes one more
class subscribed at startup, with no change to the worker.

## Decisions that mattered

**`BRPOP` instead of querying the database in a loop.** The worker stays blocked on Redis until
an id arrives or the 5-second timeout expires, so it never runs empty queries. `LPUSH` inserts
on the left and `BRPOP` takes from the right, which makes each queue FIFO. Given several lists,
Redis checks them in `WORKER_QUEUES` order and pops from the first one that has an item.
Priority between queues comes from that order.

**Database first, Redis second.** The row is written before the `LPUSH`. If Redis is
unreachable at enqueue time, the API still responds and the task stays `pending` in SQLite with
its full record. `GET /queues` reports a depth of 0 instead of returning an error.

**Retries with a per-task cap.** Every task carries its own `max_retries`, from 0 to 10, with a
default of 3. If the handler raises and attempts remain, the task moves to `retrying`, the
counter goes up by one and its id goes back to the end of its queue. Once attempts run out it
ends as `failed` with the last error saved. `HttpHandler` raises on any non-2xx response, so a
failing endpoint takes the same path. With `max_retries: 0` the task fails on the first error.

**Tests without infrastructure.** All 37 tests run without Docker. `fakeredis` stands in for
Redis, and the in-memory SQLite uses `StaticPool` so every session sees the tables the fixture
creates. The code imports modules (`import app.core.database as _db_mod`) rather than bare
functions, which lets the fixture patch `SessionLocal` and `get_redis` in one place.

## Outcome

`docker compose up --build` starts Redis, the API and one worker. With `--scale worker=3`, three
workers compete for the same queues, and the logs show the ids spread across containers. The UI
at `/` has four tabs (dashboard, enqueue, tasks and queues), is plain JavaScript with no build
step, ships four demo scenarios and refreshes every 2 seconds.

The live demo runs on Render's free plan in a single container. The API starts the `BRPOP` loop
in a thread against an Upstash Redis instance, and a poller running every 3 seconds processes
any tasks left `pending` in the database. The instance sleeps after 15 minutes without traffic,
the first load can take around 30 seconds, and the demo database is ephemeral.

If a worker dies mid-task, the id has already left Redis and the row
stays in `processing`; no process detects it and puts it back in the queue. Retries are
immediate, with no growing delay between attempts.
