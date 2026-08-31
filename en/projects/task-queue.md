---
title: Task Queue
description: "Distributed task queue with a FastAPI API server, a Redis broker and horizontally scalable workers."
permalink: /en/projects/task-queue/
---

<!--
  CASE STUDY TEMPLATE. This page is the reference example: copy it for every new
  project (es/ + en/, same id, one permalink per language).

  Structure that works:
    1. crumbs      -> back to the listing
    2. hero        -> title, one line on what it is, stack chips
    3. callout     -> the hook: the interesting design decision
    4. statline    -> REAL, measured numbers. No numbers? Delete the block.
    5. md sections -> problem, decisions, outcome, what you learned

  RULE: never invent metrics. With no measured number, describe qualitatively.
  TODO markers flag what's still missing.
-->

<p class="crumbs"><a href="{{ '/en/projects/' | relative_url }}">← Back to projects</a></p>

<section class="hero">
  <h1>Task Queue <span class="tag active">active</span></h1>
  <p class="lead">Distributed task queue: a <strong>FastAPI</strong> API server, a <strong>Redis</strong> broker (LPUSH/BRPOP), SQLite persistence and <strong>workers that scale horizontally</strong> without touching a line of code.</p>
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
  <p>The worker doesn't know the API exists, and the API doesn't know the workers exist: the only shared thing is the Redis queue. That's what makes <code>--scale worker=N</code> work in Docker Compose with no code or config changes.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">37</span><span class="lbl">tests</span></div>
  <div class="stat"><span class="num">N</span><span class="lbl">parallel workers</span></div>
  <div class="stat"><span class="num">TODO</span><span class="lbl">fill in with a real number</span></div>
</div>

## The problem

TODO(Federico): what you needed to solve, and why the existing options (Celery,
RQ, a cron job) didn't fit — or, if it was a deliberate exercise to understand
the mechanism from the inside, say exactly that, without dressing it up.

## Architecture

TODO(Federico): the layers and how they talk. A text diagram or a list is
enough; what matters is that the reader can tell who depends on whom.

- **API (FastAPI)** — takes the task, enqueues it with `LPUSH`, returns the id.
- **Broker (Redis)** — the queue. The only contact point between API and workers.
- **Worker** — blocks on `BRPOP`, runs the task, persists the result.
- **Persistence (SQLAlchemy 2.0 + SQLite)** — per-task state and history.
- **Scheduler (APScheduler)** — TODO: what runs on a schedule.

## Decisions that mattered

TODO(Federico): 2 or 3 concrete decisions, each with the *why*. The kind of
thing that belongs here: why `BRPOP` instead of polling; what happens when a
worker dies mid-task; how double processing is avoided.

## Outcome

TODO(Federico): what ended up working and what didn't. If something is still
unsolved, say so — a known limitation buys more credibility than a feature list
with no cracks in it.
