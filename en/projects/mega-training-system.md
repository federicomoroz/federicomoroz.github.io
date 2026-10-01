---
title: Mega Training System
description: "Training plan generator on the Claude API, used by a major gym chain in Argentina and by individual users. Plugin architecture and cost control."
permalink: /en/projects/mega-training-system/
---

<p class="crumbs"><a href="{{ '/en/projects/' | relative_url }}">← Back to projects</a></p>

<section class="hero">
  <h1>Mega Training System <span class="tag active">active</span></h1>
  <p class="lead">Training plan generator built on the <strong>Claude API</strong>. It started as a tool for one indoor cycling instructor and is now used by <strong>a major gym chain in Argentina and individual users</strong>.</p>
  <div class="chip-row">
    <span class="tag">Python</span><span class="tag">Flask</span><span class="tag">Claude</span>
    <span class="tag">SSE</span><span class="tag">PostgreSQL</span><span class="tag">Docker</span><span class="tag">pytest</span>
  </div>
  <p class="row-links">
    <span class="muted">Private repo</span>
  </p>
</section>

<div class="callout">
  <p class="callout-title">The design decision</p>
  <p>The architecture rules are checked by tests. Around 670 of them read the code's <strong>AST</strong> and fail if a layer imports one it has no business importing, if a route talks straight to the database, or if a service bypasses its port. A refactor that breaks layer separation never gets merged.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">1,671</span><span class="lbl">tests in CI</span></div>
  <div class="stat"><span class="num">87%</span><span class="lbl">coverage</span></div>
  <div class="stat"><span class="num">~670</span><span class="lbl">architecture tests</span></div>
</div>

## The problem

Putting together an indoor cycling class in the chain's format is repetitive work with hard
rules: five phases, exactly 3360 seconds, cadence between 60 and 110 RPM, BPM at twice the
cadence. An LLM drafts that well, but putting one in the middle introduces two problems that
did not exist before: **the model returns structures that don't always respect the rules**,
and **every generation costs money**.

The system is built around those two problems.

Then came a third. When the chain adopted it, a second discipline was needed, strength
training, with its own methodology, catalogue and output format. That is where the plugin
architecture comes from: adding strength training shouldn't force a rewrite of indoor
cycling.

## The music editor

Every class carries **the music on top of its structure**. That is the job of an audio editor
in the browser, a small DAW with a timeline by phase, tracks you drag onto each block,
crossfades, and a final render to a single file.

<figure class="shot">
  <img src="{{ '/assets/img/mts-musicalizador.jpg' | relative_url }}" alt="Audio editor: timeline with the class phases, the music lane with its waveform, the fade controls, and the track library with BPM and intensity." loading="lazy" width="1600" height="1000">
  <figcaption>A finished class: 56 minutes with its structure on top and the music underneath, every block with its track, its waveform and its crossfade. The percentage on each one is how well the track fits the phase; the library below carries BPM and intensity, which is what decides where it can go.</figcaption>
</figure>

## The training plan

The other discipline generates strength training plans. It runs on the same core as indoor
cycling, with a different agent and a different output format.

<figure class="shot">
  <img src="{{ '/assets/img/mts-plan.jpg' | relative_url }}" alt="A twelve-week hypertrophy plan: three mesocycles, four days a week, and the exercises with sets, reps, rest and RPE." loading="lazy" width="1600" height="1150">
  <figcaption>Twelve weeks across three mesocycles (accumulation, intensification, and peak with deload), with every exercise and its sets, reps, rest and target RPE.</figcaption>
</figure>

The capture shows something the diagrams don't: **the member's restriction reaches the
exercise**. An injury declared in the profile travels down into the plan and decides which
movements are avoided and what replaces them, exercise by exercise.

## Architecture

Four layers, with the discipline registry cutting across them:

- **Presentation (HTTP / SSE):** one blueprint per domain, auth hook and rate limiting.
- **Application:** generation orchestrator, idempotency and result store. The orchestrator
  does not import Flask, so it can be exercised without starting the server.
- **Services:** the logic of each discipline. The strength-training service receives a
  two-method port and never sees the rest of the repository.
- **Infrastructure:** the Claude client behind the circuit breaker, repositories, filesystem
  and knowledge base.

Adapters come in through ports (`ClassStoragePort`, `KnowledgeBasePort`, `UserRepoPort`), so
the services are tested with no filesystem and no database.

## The diagrams

The full architecture is documented as a single self-contained HTML page with nine generated
diagrams: the overview, the modules, the domain models, the SSE and threading flow, the
SQLite schema, the discipline system, the API routes, resilience and startup, and an
architecture assessment.

<div class="cards">
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/mega-training-system/arquitectura_en.html' | relative_url }}">Full architecture ↗</a></div>
    <div class="card-desc"><p>Seven sections, from the bird's-eye view down to the table schema: each discipline's secondary ports, the domain invariants, how streaming is solved with threading inside a synchronous Flask, and what the API exposes.</p></div>
  </article>
</div>

## Decisions that mattered

**LLM calls go through a circuit breaker.** It has all three states (`CLOSED` / `OPEN` /
`HALF_OPEN`). In `HALF_OPEN`, an in-flight probe flag serializes the retry: when the circuit
opens, a single request checks whether the service came back instead of N simultaneous ones.

**Four independent mechanisms keep cost down.** The system prompt is sent as a cached block,
so reads cost a fraction of the price. Work that doesn't need an immediate answer goes
through the Batch API. An `Idempotency-Key` carrying a hash of the profile avoids
regenerating the same thing inside the window. And the model is picked by request
complexity, instead of always reaching for the most expensive one.

**The model always answers with a tool call.** Generation uses `tool_choice="any"`, so the
output arrives structured and there is no free text to parse. The domain invariants live in
Pydantic v2 validators. When the model returns durations that don't add up, a repair routine
adjusts them and the generation is still used.

**A new discipline doesn't touch the core.** The registry discovers plugins through
`pkgutil`. Adding a discipline is a `plugin.py` plus its agent, without opening `app.py`.

**Streaming with SSE and threading, no asyncio.** Flask is synchronous. Generation returns a
`task_id`, the client attaches to a stream, and each task has its own `threading.Event`, so
there is no polling.