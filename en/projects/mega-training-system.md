---
title: Mega Training System
description: "Training plan generator on the Claude API, in production at a client. Plugin architecture and cost control by design."
permalink: /en/projects/mega-training-system/
---

<p class="crumbs"><a href="{{ '/en/projects/' | relative_url }}">← Back to projects</a></p>

<section class="hero">
  <h1>Mega Training System <span class="tag active">active</span></h1>
  <p class="lead">Training plan generator built on the <strong>Claude API</strong>. It started as a tool for one indoor cycling instructor and is now used by <strong>a client</strong> in daily operation.</p>
  <div class="chip-row">
    <span class="tag">Python</span><span class="tag">Flask</span><span class="tag">Claude</span>
    <span class="tag">SSE</span><span class="tag">PostgreSQL</span><span class="tag">Docker</span><span class="tag">pytest</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/MegaTrainingSystem" target="_blank" rel="noopener">Repo ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">The design decision</p>
  <p>The architecture is not held up by convention — it is verified. Around 670 tests read the code's <strong>AST</strong> and fail if a layer imports one it has no business importing, if a route talks straight to the database, or if a service bypasses its port. A refactor that breaks layer separation never gets merged.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">1,671</span><span class="lbl">tests in CI</span></div>
  <div class="stat"><span class="num">87%</span><span class="lbl">coverage</span></div>
  <div class="stat"><span class="num">~670</span><span class="lbl">architecture tests</span></div>
</div>

## The problem

Putting together an indoor cycling class in the client's format is repetitive work with hard
rules: five phases, exactly 3360 seconds, cadence between 60 and 110 RPM, BPM at twice the
cadence. An LLM drafts that well, but putting one in the middle introduces two problems that
did not exist before: **the model returns structures that don't always respect the rules**,
and **every generation costs money**.

The system is built around those two problems, not around the prompt.

Then came a third. When the client adopted it, a second discipline was needed —strength
training— with its own methodology, its own catalogue and its own output format. That is
where the plugin architecture comes from: the second discipline could not cost a rewrite of
the first.

## The music editor

A class is not just its structure: it is the structure **with the music on top**. The audio
editor is a small DAW in the browser — a timeline by phase, tracks dragged onto each block,
crossfades, and a final render to a single file.

<figure class="shot">
  <img src="{{ '/assets/img/mts-musicalizador.jpg' | relative_url }}" alt="Audio editor: timeline with the class phases, the music lane with its waveform, the fade controls, and the track library with BPM and intensity." loading="lazy" width="1600" height="1000">
  <figcaption>The 56 minutes of a class, structure on top and music underneath. Every track in the library carries its BPM and its intensity, which is what decides the phase it can go into.</figcaption>
</figure>

## Architecture

Four layers, with the discipline registry cutting across them:

- **Presentation (HTTP / SSE)** — one blueprint per domain, auth hook and rate limiting.
- **Application** — generation orchestrator, idempotency and result store. The orchestrator
  does not import Flask, so it can be exercised without starting the server.
- **Services** — the logic of each discipline. The strength-training service receives a
  two-method port, not the whole repository.
- **Infrastructure** — the Claude client behind the circuit breaker, repositories, filesystem
  and knowledge base.

Adapters come in through ports (`ClassStoragePort`, `KnowledgeBasePort`, `UserRepoPort`), so
the services are tested with no filesystem and no database.

## The diagrams

The full architecture is documented as a single self-contained HTML page with nine generated
diagrams: the overview, the modules, the domain models, the SSE and threading flow, the
SQLite schema, the discipline system and the API routes.

<div class="cards">
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/mega-training-system/arquitectura_en.html' | relative_url }}">Full architecture ↗</a></div>
    <div class="card-desc"><p>Seven sections, from the bird's-eye view down to the table schema: each discipline's secondary ports, the domain invariants, how streaming is solved with threading inside a synchronous Flask, and what the API exposes.</p></div>
  </article>
</div>

## Decisions that mattered

**The LLM is treated as a dependency that fails.** Calls go through a circuit breaker with
all three states (`CLOSED` / `OPEN` / `HALF_OPEN`). The detail that matters is in
`HALF_OPEN`: an in-flight probe flag serializes the retry, so that when the circuit opens it
doesn't send N simultaneous requests to check whether the service came back.

**Cost is a design dimension, not a side effect.** Four independent mechanisms attack the
same thing: the system prompt is sent as a cached block, so reads cost a fraction of the
price; work that doesn't need an immediate answer goes through the Batch API; an
`Idempotency-Key` carrying a hash of the profile avoids regenerating the same thing inside
the window; and the model is picked by request complexity instead of always reaching for the
most expensive one.

**Structured output is not requested, it is enforced.** Generation uses `tool_choice="any"`:
the model returns a tool call, never free text that has to be parsed afterwards. On top of
that, the domain invariants live in Pydantic v2 validators, and when the model returns
durations that don't add up, a repair routine adjusts them instead of throwing the whole
generation away.

**A new discipline doesn't touch the core.** The registry discovers plugins through
`pkgutil`; adding a discipline is a `plugin.py` plus its agent, without opening `app.py`.

**SSE and threading, not asyncio.** Flask is synchronous. Generation returns a `task_id` and
the client attaches to a stream, with one `threading.Event` per task instead of polling.

<!--
  TODO(Federico): same two items as the Spanish page — how it reached the client, and a real
  production incident with its root cause. Both would add more than the pattern list above,
  and neither can be written without you.
-->
