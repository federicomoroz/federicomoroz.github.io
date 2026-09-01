---
title: Shipping Quote
description: "Shipping rate quoter built to show a hexagonal architecture circuit running, with every request traced hop by hop."
permalink: /en/projects/shipping-quote/
---

<p class="crumbs"><a href="{{ '/en/projects/' | relative_url }}">← Back to projects</a></p>

<section class="hero">
  <h1>Shipping Quote <span class="tag active">active</span></h1>
  <p class="lead">Shipping rate quoter that exists to show a <strong>hexagonal circuit running</strong> rather than drawn: every request is traced hop by hop, from the moment it arrives over HTTP until three carrier adapters return their own quote.</p>
  <div class="chip-row">
    <span class="tag">Python</span><span class="tag">FastAPI</span><span class="tag">SQLAlchemy</span>
    <span class="tag">Alembic</span><span class="tag">httpx</span><span class="tag">pytest</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/shipping-quote" target="_blank" rel="noopener">Repo ↗</a>
    <a href="https://shipping-quote.onrender.com" target="_blank" rel="noopener">Live demo ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">The design decision</p>
  <p>Hexagonal architecture is almost always explained with a diagram, and the claim that the code respects it is taken on faith. Here you can watch it: every request emits its own ordered trace —entry, adapter, port, use case, domain, port, adapter, exit— and that trace comes back in the response. The diagram isn't documentation sitting next to the code; it's the code's output.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">31</span><span class="lbl">tests in CI</span></div>
  <div class="stat"><span class="num">3</span><span class="lbl">carrier adapters</span></div>
  <div class="stat"><span class="num">~15</span><span class="lbl">lines to add a fourth</span></div>
</div>

## Why it exists

It is a teaching artifact, and that is worth saying up front: not a product, but one use
case —quoting a package— running against three adapters inside the same request. The three
carriers are **simulations**, not real integrations: a separate FastAPI sub-app mimicking
the APIs, wired through `ASGITransport` without opening a socket. The value isn't in having
integrated a real carrier; it's that the same domain produces three different results
without ever learning that three of them exist.

That buys something a toy example doesn't: the whole circuit, with real persistence, real
error handling and a trace you can read.

## The circuit

```
entry -> adapter -> port -> use case -> domain -> port -> adapter -> exit
(POST)   quote_     Shipping  QuoteShipping  pipeline  Carrier  *Adapter  carrier
         controller QuotePort UseCase        steps     Port               API
```

`main.py` is the composition root: it wires everything in the lifespan. The domain
(`Package`, zones, `FeePolicy`, `Tracer`) imports nothing from the outside.

None of this has to be taken on faith: **the trace comes back inside the response**. A 2.5 kg
package to postal code 1425 returns eighteen steps —entry, adapter, port, the domain steps,
the three carrier adapters and the exit— each with its own timing. The same JSON shows the
volumetric weight rule deciding: 2.5 kg actual against 4.8 kg effective.

## Decisions that mattered

**Money in `Decimal`, not `float`.** The service fee calculation works in `Decimal` and
rounds with an explicit `ROUND_HALF_UP`, because Python's built-in `round()` uses banker's
rounding, which for money produces results that surprise people. One test pins exactly that
difference: `test_apply_service_fee_rounds_half_up_not_banker`. It was technical debt paid
off, not something that was right from the start.

**The three carriers are one class, not three.** `HttpCarrierAdapter` is configured by
composition —an endpoint plus two mapping functions— instead of repeating the same
try/except/timeout three times. That is why adding a fourth carrier is a file of about
fifteen lines rather than a whole class.

**One carrier fails on purpose.** The Correo Argentino mock returns an error roughly 15% of
the time. The use case runs all three through `asyncio.gather` and answers with two quotes
out of three without falling over. That is the difference between demonstrating that you
call three services and demonstrating what happens when one of them goes down.

**Tracing through `Tracer`, not an event bus.** A trace has a single consumer and a strict
order, so it is passed by reference through the layers. A pub/sub bus would have been using
the pattern for its own sake: here it adds indirection and buys nothing.

**A primary port for a single implementation.** `ShippingQuotePort` is over-engineering by
YAGNI, and it is deliberate: the project exists to show the full circuit, and without that
port the driving side of the hexagon is invisible. It is written down in the ABC's docstring
so nobody reads it as an oversight.

**Effective weight is `max(actual weight, length × width × height / 5000)`**, the standard
volumetric weight formula. The domain carries a real business rule, not a decorative `if`.

## Deliberately out of scope

No authentication, no rate limiting, no manual carrier selection — all three are always
quoted. The goal is the architecture, not a finished product.

The Alembic migrations are deliberately kept apart from the `create_all()` at startup:
hooking them into the lifespan would have made the tests migrate the real database instead
of the in-memory one, because the tests patch the engine rather than the URL.
