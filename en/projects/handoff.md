---
title: handoff
description: "A customer says their order arrived broken. handoff makes the four reads it takes to answer them and decides in two seconds: it resolves the case, or hands it to a person with everything already gathered."
permalink: /en/projects/handoff/
---

<p class="crumbs"><a href="{{ '/en/tools/' | relative_url }}">{{ site.data.i18n[page.lang].services.back }}</a></p>

<section class="hero">
  <h1>handoff <span class="tag active">active</span></h1>
  <p class="lead">A customer writes in: <strong>"it arrived broken"</strong>. To answer them, someone has to look at the order, the shipment, how many times that customer has claimed before, and whatever the warehouse wrote down (four reads against an old system), and only then decide. <strong>handoff makes those four reads and decides, in two seconds.</strong> It sends a replacement, refunds, asks for a photo, or hands the case to a person with the four reads already done and the reason it stopped.</p>
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
  <p>An e-commerce operation takes claims all day. The work is repetitive: each claim means looking at four screens, and takes as long as opening them does. handoff takes the claims over HTTP and returns the decision together with the facts behind it. <strong>In eight out of ten the decision is the right one</strong>, counting the cases where the right call was not to decide. When the facts fall short, the case reaches a person with everything already gathered.</p>
</div>

{% include handoff-circuito.html lang="en" %}

## How it's used

It runs as an HTTP service. A claim comes in through `POST /api/triage` with three things: an order number, what happened (arrived broken, arrived late, never arrived) and what the customer wrote. It returns the decision, the facts it used and a trace of everything it read.

From those three it looks up four things in the company's system:

- **The order**: what it cost, what type it is, who bought it.
- **The shipment**: what state it is in and when it last moved.
- **The customer's history**: how many claims they filed in the last 90 days.
- **The internal notes**: anything the warehouse wrote down.

Then it picks one of four exits: **send a replacement**, **refund**, **ask the customer for a photo** or **hand it to a person**.

The first two move money or goods and cannot be taken back. The last two cost nothing. The rules further down are built on that difference.

## Results

<div class="statline">
  <div class="stat"><span class="num">83<small>%</small></span><span class="lbl">of cases, the right decision</span></div>
  <div class="stat"><span class="num">2<small>s</small></span><span class="lbl">to make the four reads and decide</span></div>
  <div class="stat"><span class="num">0</span><span class="lbl">refunds without enough backing</span></div>
</div>

The two seconds are the 95th percentile: nineteen out of twenty claims come back resolved faster than that, with the model running locally on an ordinary graphics card.

The zero means that **money was never refunded on a case that needed a person.** There are eleven rules between the model's proposal and its execution, and any one of them is enough to stop it. The rules stopped all nineteen times, out of ninety-six, that the model proposed a refund on one of those cases.

{% include handoff-freno.html lang="en" %}

## The rules that check the model

The model picks what to do. Eleven rules review that pick before it is executed. They check whether the amount is high, whether the customer has already claimed three times, whether the shipment is still moving, whether the last update is more than three days old, and whether any of the four facts is missing.

If the company's system does not answer when asked for a customer's history, handoff marks that fact as missing and the rule stops the decision. **A history that could not be read counts as a missing fact**, never as a customer with no previous claims.

The strict rules apply only to what is irreversible. The agent needs no certainty to *ask the customer a question*, so when it is unsure it can ask for a photo without handing the case to a person.

## An ERP that answers badly

The ERP it runs against is simulated, and it is built to misbehave in ten specific ways, all taken from real integrations: it answers XML on one endpoint and JSON on the rest, expires the session halfway through a batch, cuts a response off at 60% and still reports it as successful, writes "no value" in five different ways, and has a status code whose meaning depends on a field that lives in a different call.

handoff resolves all ten before the model sees anything. Code handles whatever has exactly one correct answer, such as converting an amount, resolving a code or reading a date. Only what takes judgement reaches the model. When the system genuinely does not answer, the fact is marked missing and the rules treat it as a hole.

## How it's measured

The agent runs against 36 hand-written situations: 16 that must end with a person and 20 it should resolve on its own. Each one describes what happened. The correct answer lives in a separate file the agent has no way of reaching. Several sit right at the edge of a limit: an order of 149,900 against a ceiling of 150,000, a shipment 71 hours without news against a limit of 72, a customer with two claims against a rule that fires at three.

The model's answers are recorded, and each recording is filed under a fingerprint of everything that was sent to it. A change that cannot affect the decision (a rename, a reordering) replays the recordings and costs nothing. A change that can affect it, even one word of the text sent to the model, invalidates them and forces a fresh measurement before it can be merged. This was verified both ways. Adding a single line to that text invalidated all 96 recordings and blocked the merge, and removing it turned them green again.

The two figures are published separately: **83% for the whole system, 67% for the model before the rules.** The difference between them is what the rules contribute.
