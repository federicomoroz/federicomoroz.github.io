---
title: handoff
description: "A customer says their order arrived broken. handoff makes the four reads it takes to answer them and decides in two seconds: it resolves the case, or hands it to a person with everything already gathered."
permalink: /en/projects/handoff/
---

<p class="crumbs"><a href="{{ '/en/projects/' | relative_url }}">← Back to projects</a></p>

<section class="hero">
  <h1>handoff <span class="tag active">active</span></h1>
  <p class="lead">A customer writes in: <strong>"it arrived broken"</strong>. To answer them, someone has to look at the order, the shipment, how many times that customer has claimed before, and whatever the warehouse wrote down — four reads against an old system — and only then decide. <strong>handoff makes those four reads and decides, in two seconds.</strong> It sends a replacement, refunds, asks for a photo, or hands the case to a person with the four reads already done and the reason it stopped.</p>
  <div class="chip-row">
    <span class="tag">TypeScript</span><span class="tag">Node</span><span class="tag">Hono</span>
    <span class="tag">Zod</span><span class="tag">Ollama</span><span class="tag">vitest</span>
    <span class="tag">GitHub Actions</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/handoff" target="_blank" rel="noopener">Repo ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">What it is for</p>
  <p>An e-commerce operation takes claims all day. The work is not hard: it is repetitive, spread across four screens, and every case costs whatever it costs to open them. handoff takes the claims over HTTP and returns the decision together with the facts behind it. <strong>In eight out of ten the decision is the right one</strong> — including the decision not to decide: when the facts fall short, the case reaches a person already assembled, not blank.</p>
</div>

{% include handoff-circuito.html lang="en" %}

## A service you call, and it answers

It runs as an HTTP service. A claim comes in through `POST /api/triage` with three things —an order number, what happened (arrived broken, arrived late, never arrived) and what the customer wrote— and it returns the decision, the facts it used, and a trace of everything it read.

From those three it looks up four things in the company's system:

- **the order** — what it cost, what type it is, who bought it;
- **the shipment** — what state it is in and when it last moved;
- **the customer's history** — how many claims they filed in the last 90 days;
- **the internal notes** — anything the warehouse wrote down.

And it picks one of four exits: **send a replacement**, **refund**, **ask the customer for a photo**, or **hand it to a person**.

The first two move money or goods and cannot be taken back. The last two cost nothing. That difference is what organises everything else.

## What it resolves, and how fast

<div class="statline">
  <div class="stat"><span class="num">83<small>%</small></span><span class="lbl">of cases, the right decision</span></div>
  <div class="stat"><span class="num">2<small>s</small></span><span class="lbl">to make the four reads and decide</span></div>
  <div class="stat"><span class="num">0</span><span class="lbl">refunds without enough backing</span></div>
</div>

The two seconds are the 95th percentile: nineteen out of twenty claims come back resolved faster than that, with the model running locally on an ordinary graphics card.

The zero is what makes the other two worth anything. **It never refunded on a case that needed a person.** Not because the model never tried — it tried nineteen times out of ninety-six — but because there are eleven rules between the proposal and the execution, and any one of them stops it.

{% include handoff-freno.html lang="en" %}

## The rules do not trust the model

The model picks what to do. Eleven rules review that pick before it happens: the amount is high, the customer has already claimed three times, the shipment is still moving, the last update is more than three days old, or one of the four facts is missing.

That last one matters more than it looks. If the company's system does not answer when asked for a customer's history, **the absence of previous claims is not read as a customer with no claims**. A fact that could not be read does not count as a fact that says no.

And the strict rules apply only to what is irreversible. Demanding certainty before the agent was allowed to *ask the customer a question* left it one legal move when it was unsure: wake a person. Asking is exactly what you do when you are not sure.

## Against a system that answers badly

The ERP it runs against is simulated, and it is built to misbehave in ten specific ways, all taken from real integrations: it answers XML on one endpoint and JSON on the rest, expires the session halfway through a batch, cuts a response off at 60% and still reports it as successful, writes "no value" in five different ways, and has a status code whose meaning depends on a field that lives in a different call.

handoff resolves all ten before the model sees anything. Whatever has exactly one correct answer —converting an amount, resolving a code, reading a date— is done in code, and only the judgement reaches the model. When the system genuinely does not answer, the fact is marked missing and the rules treat it as what it is, a hole.

## How it holds up

The agent runs against 36 hand-written situations: 16 that must end with a person and 20 it should resolve on its own. Each one states what happened, not what the answer should be — the correct answer lives in a separate file the agent has no way of reaching. Several sit right at the edge of a limit: an order of 149,900 against a ceiling of 150,000; a shipment 71 hours without news against a limit of 72; a customer with two claims against a rule that fires at three. The edge is where the judgement is.

The model's answers are recorded, and each recording is filed under a fingerprint of everything that was sent to it. A change that cannot affect the decision —a rename, a reordering— replays the recordings and costs nothing. A change that can —one word of the text sent to the model— invalidates them and forces a fresh measurement before the change can be merged. Verified both ways: adding a single line to that text invalidated all 96 recordings and blocked the merge; removing it turned them green again.

The two figures that matter are published separately: **83% for the whole system, 67% for the model before the rules.** The distance between them is what the rules contribute, and a single blended number would hide it.
