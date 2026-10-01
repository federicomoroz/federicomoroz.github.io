---
title: Chargeback investigation agent
description: "An agent that investigates chargebacks: assembles the full case, proposes a justified resolution, grades itself, and stops on high-risk cases. n8n + FastAPI + RAG."
permalink: /en/projects/agente-contracargos/
---

<p class="crumbs"><a href="{{ '/en/projects/' | relative_url }}">← Back to projects</a></p>

<section class="hero">
  <h1>Chargeback investigation agent <span class="tag active">active</span></h1>
  <p class="lead">Given a chargeback, the agent gathers what is known about the case: the transaction and its logs, the policies that apply, how similar cases were resolved, the merchant's risk and the customer's history. From that it <strong>proposes a justified resolution and grades itself</strong>. High-risk cases stop and wait for a human analyst.</p>
  <div class="chip-row">
    <span class="tag">Python 3.11</span><span class="tag">FastAPI</span><span class="tag">n8n</span>
    <span class="tag">Claude (Haiku + Sonnet)</span><span class="tag">Qdrant</span><span class="tag">RAG</span>
    <span class="tag">Docker</span><span class="tag">pytest</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/ciri-api-aux-sourcecode" target="_blank" rel="noopener">Repo ↗</a>
    <a href="https://ciri-chargeback-agent.onrender.com/panel" target="_blank" rel="noopener">Live panel ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">Direct mode and n8n mode</p>
  <p>The panel can run the pipeline directly or through your own n8n instance. If your n8n stops responding mid-run, the panel switches back to direct mode <strong>and says so</strong>. I'd rather show an error than a report claiming it went through the orchestration when it didn't.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">1232</span><span class="lbl">tests in CI</span></div>
  <div class="stat"><span class="num">36</span><span class="lbl">steps in the circuit</span></div>
  <div class="stat"><span class="num">32</span><span class="lbl">endpoints</span></div>
  <div class="stat"><span class="num">46</span><span class="lbl">n8n nodes</span></div>
</div>

## What it solves

A chargeback is a dispute: the customer doesn't recognize a charge and someone has to decide
whether the money goes back. Deciding means pulling together data that lives in different
places: the transaction and its logs, the policy that applies, how similar cases were
resolved, how risky the merchant is and what history the customer has. It also takes
judgement that isn't written down in any table.

The agent assembles that case file, proposes a resolution **with its reasoning** and then
grades itself. On high-risk cases it stops and leaves the file waiting for a human analyst.

## What it produces

The testing panel runs the circuit over any transaction in the dataset and shows the result
without installing anything. The three scenarios cover both of the router's outcomes: automatic
rejection and human review.

<figure class="shot">
  <img src="{{ '/assets/img/ciri-panel.jpg' | relative_url }}" alt="Testing panel: health of FastAPI, SQLite, Qdrant and Langfuse, plus three test scenarios with their expected outcome." loading="lazy" width="1000" height="1071">
  <figcaption>The panel checks its own dependencies before letting you run anything: if Qdrant is down you see it there, before the pipeline starts.</figcaption>
</figure>

Every run ends in a report: the transaction, the customer and merchant profiles with their flags,
the policies that apply, the precedents, and the proposed resolution with its reasoning.

<figure class="shot">
  <img src="{{ '/assets/img/ciri-informe.jpg' | relative_url }}" alt="Chargeback report: transaction data, risk level, customer profile and merchant risk profile with anomaly flags." loading="lazy" width="1600" height="1143">
  <figcaption>A high-risk case. The antifraud score, the geographic anomaly and the suspended merchant are what make the circuit stop and wait for an analyst.</figcaption>
</figure>

These three reports ship with the delivery package. I picked them for the policy situation each
one covers, without looking at the score: a crypto blocker, a VIP customer with a fraud score and
an extended SLA outside LATAM.

*The reports are in Spanish because that is what the system wrote. A translation would show
output it never produced.*

<div class="cards">
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/informe-bloqueante.html' | relative_url }}">Automatic rejection ↗</a></div>
    <div class="card-desc"><p>A blocking policy stops the case before the model gets an opinion. The code decides, and the report explains which rule applied and why there was nothing to deliberate.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/informe-riesgo-alto.html' | relative_url }}">Human review ↗</a></div>
    <div class="card-desc"><p>High risk. The agent assembles the case and proposes a resolution, and the case waits for an analyst with everything needed to decide on a single screen.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/informe-sla.html' | relative_url }}">SLA alert ↗</a></div>
    <div class="card-desc"><p>A duplicate charge outside LATAM, where the response window is different. Here the right policy depends on where the charge happened.</p></div>
  </article>
</div>

## The circuit

These are five interactive, self-contained diagrams that open in any browser, offline, with
nothing to install. They're in reading order: first **what** the circuit does, then **how**
the pieces talk to each other.

*The sample strings inside them (the indexed policy, the case document, the assembled query)
stay in Spanish because they are what the system actually sends.*

{% include diagrama-circuito.html lang="en" %}

<div class="cards">
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/n8n_workflow_analysis_en.html' | relative_url }}">The full circuit ↗</a></div>
    <div class="card-desc"><p>All 36 steps in execution order plus the 4 error exits, each with its endpoint. Generated from the workflow's own JSON, so it can't drift from the real flow.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/pipeline_n8n_api_en.html' | relative_url }}">n8n and the API ↗</a></div>
    <div class="card-desc"><p>The fifteen calls in order, what each one touches (SQLite, Qdrant or the model) and the two times the conversation runs the other way. A one-minute read.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/api_en.html' | relative_url }}">Inside the API ↗</a></div>
    <div class="card-desc"><p>The 32 endpoints drawn as a circuit. For each piece it explains what it does and why it's split that way: which SOLID principle backs each seam and which patterns are used. The other diagrams show the flow, and this one shows the design decisions.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/rag_en.html' | relative_url }}">The RAG ↗</a></div>
    <div class="card-desc"><p>The whole retrieval chain, followed through a real case: what gets indexed and what doesn't, how the query is built, why the two collections are searched by opposite criteria, and where the index writes itself.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/tests_en.html' | relative_url }}">The tests ↗</a></div>
    <div class="card-desc"><p>The three layers, coverage per package, and the sixteen regression tests that pin real bugs so they can't come back. None of those sixteen bugs broke an import.</p></div>
  </article>
</div>

## The RAG

The RAG is a chain of transformations over text, and a model decides none of them.

{% include diagrama-rag.html lang="en" %}

The RAG diagram further down has the full detail: what text gets embedded, how the query is
built and why the two collections are searched by different criteria.

## How it's built

- **Orchestration in n8n**: 46 nodes, 40 executable. n8n coordinates, and the nodes only call
  the API. A second workflow adds a form as an alternative entry point, and a third receives
  failures from the other two and logs them.
- **FastAPI service**: 32 endpoints, split by layer (domain, analysis, RAG, LLM, reports,
  observability). Everything the workflow does is available as an endpoint.
- **RAG over Qdrant**: two collections, policies and precedents, deliberately searched by
  opposite criteria.
- **Two models with different jobs**: Haiku evaluates the policies, and Sonnet synthesizes
  and then judges the result.
- **Guardrails, rate limiting and traces**: every run records what it queried, what it
  retrieved and what it cost.

## The judge's numbers

What I like most about this project is **how it treats its own numbers**.

The repo shows a 9.1/10 judge score and then explains where it comes from. That number came
from development runs that can't be reproduced today without API credit. The three reports
shipped in the package average 8.67. The two later runs, done with free-tier models, score
8.97 and 8.4, but **shouldn't move the badge**: each model grades itself by its own yardstick,
and on the cases both runs share the score swings by up to ±1.8 between them.

It also leaves a script to measure again, which runs the sample, writes the case-by-case
detail and reports the cost.

Every report the system generates states how it was produced: whether it really ran or is a
stored result, with which model, and how far the score can drift. That travels in the HTTP
header, in the body and in a log warning.

## Trying it

The [live panel](https://ciri-chargeback-agent.onrender.com/panel) runs the full pipeline
with nothing to install and no key to provide. It starts in demo mode, which falls back to a
free-tier model and **actually runs the pipeline** rather than replaying a stored result.

It's on Render's free tier and sleeps after 15 minutes idle, so the first call can take about
a minute to wake it up.
