---
title: handoff
description: "A customer says their order arrived broken. Answering properly means checking four things in an old system. handoff checks them and proposes the answer, with eleven rules that stop it moving money when the facts fall short."
permalink: /en/projects/handoff/
---

<p class="crumbs"><a href="{{ '/en/projects/' | relative_url }}">← Back to projects</a></p>

<section class="hero">
  <h1>handoff <span class="tag active">active</span></h1>
  <p class="lead">A customer writes in: <strong>"it arrived broken"</strong>. To answer them, someone has to look at the order, the shipment, how many times that customer has claimed before, and whatever the warehouse wrote down — four reads against an old system — and only then decide whether to send a replacement, refund, ask for a photo, or hand the case to a person. <strong>handoff does those four reads and proposes the decision.</strong></p>
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
  <p>An e-commerce operation takes claims all day. The work is not hard: it is repetitive, spread across four screens, and getting it wrong costs money. What is needed is not only somebody doing it faster, but <strong>never refunding when the facts do not support it</strong>. That second half is where most of this project went.</p>
</div>

{% include handoff-circuito.html lang="en" %}

## What it decides, and on what

A claim arrives with three things: an order number, what happened —arrived broken, arrived late, never arrived— and what the customer wrote. From there the agent looks up four things in the company's system:

- **the order** — what it cost, what type it is, who bought it;
- **the shipment** — what state it is in and when it last moved;
- **the customer's history** — how many claims they filed in the last 90 days;
- **the internal notes** — anything the warehouse wrote down.

And it picks one of four exits: **send a replacement**, **refund**, **ask the customer for a photo**, or **hand it to a person**.

The first two move money or goods and cannot be taken back. The last two cost nothing. That difference is what organises everything else.

## The rules do not trust the model

The model picks what to do. Eleven rules review that pick before it happens, and any one of them stops it: the amount is high, the customer has already claimed three times, the shipment is still moving, the last update is more than three days old, or one of the four facts is missing.

That last one matters more than it looks. If the company's system does not answer when asked for a customer's history, **the absence of previous claims is not read as a customer with no claims**. A fact that could not be read does not count as a fact that says no.

{% include handoff-freno.html lang="en" %}

And the strict rules apply only to what is irreversible. Demanding certainty before the agent was allowed to *ask the customer a question* left it one legal move when it was unsure: wake a person. Asking is exactly what you do when you are not sure.

## How it is known to work

The agent runs against 36 hand-written situations: 16 that must end with a person and 20 it should resolve on its own. Each one states what happened, not what the answer should be — the correct answer lives in a separate file the agent has no way of reaching.

Several sit right at the edge of a limit: an order of 149,900 against a ceiling of 150,000; a shipment 71 hours without news against a limit of 72; a customer with two claims against a rule that fires at three. The edge is where the judgement is.

<div class="statline">
  <div class="stat"><span class="num">83<small>%</small></span><span class="lbl">of cases handled as they should be</span></div>
  <div class="stat"><span class="num">19</span><span class="lbl">attempts to move money without backing</span></div>
  <div class="stat"><span class="num">0</span><span class="lbl">that ever executed</span></div>
</div>

There is a number the project publishes that does not flatter it: **the model on its own is right 67% of the time**, and answering "let a person look at it" to everything is right 46% of the time. The distance between that 67% and the system's 83% is the rules working. The two figures are published separately on purpose: an agent that is only ever right because it gets stopped is one gap away from being wrong in production, and a single blended number hides exactly that.

## Against a system that answers badly

The ERP it runs against is simulated, and the repository says so. It is built to misbehave in ten specific ways, all taken from real integrations: it answers XML on one endpoint and JSON on the rest, expires the session halfway through a batch, cuts a response off at 60% and still reports it as successful, writes "no value" in five different ways, and has a status code whose meaning depends on a field that lives in a different call.

All of it is resolved before the model sees anything. Whatever has exactly one correct answer —converting an amount, resolving a code, reading a date— is done in code, and only the judgement reaches the model. Handing it the raw mess would make something with a single right answer unpredictable, and would make the tests measure parsing instead of decisions.

When the system genuinely does not answer, the agent says so: the fact is marked missing and the rules treat it as what it is, a hole.

## Every change is measured again

The model's answers are recorded, and each recording is filed under a fingerprint of everything that was sent to it. A change that cannot affect the decision —a rename, a reordering— replays the recordings and costs nothing. A change that can —one word of the text sent to the model— invalidates them and forces a fresh measurement before the change can be merged.

Verified both ways: adding a single line to that text invalidated all 96 recordings and blocked the merge; removing it turned them green again.

<div class="callout">
  <p class="callout-title">What it still does not do well</p>
  <p>Three test situations fail every time, and two share the same mistake: the shipment is marked lost and the agent asks the customer to photograph a package that does not exist. That is judgement, not arithmetic, and the limit there is the size of the model — it runs locally, on an ordinary graphics card, with no API cost. The piece that would replace it is one parameter.</p>
</div>
