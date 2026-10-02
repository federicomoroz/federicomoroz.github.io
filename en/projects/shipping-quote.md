---
title: Shipping Quote
description: "Shipping rate quoter with a hexagonal architecture that queries three carriers in parallel and returns the trace of each request, hop by hop."
permalink: /en/projects/shipping-quote/
---

<p class="crumbs"><a href="{{ '/en/tools/' | relative_url }}">{{ site.data.i18n[page.lang].services.back }}</a></p>

<section class="hero">
  <h1>Shipping Quote <span class="tag active">active</span></h1>
  <p class="lead">Shipping rate quoter built as a <strong>hexagonal circuit</strong>. Every request is traced hop by hop, from the moment it arrives over HTTP until each of the three carrier adapters returns its quote.</p>
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
  <p>Every request builds its own ordered trace (entry, adapter, port, use case, domain, port, adapter, exit) and returns it in the response. The hexagon diagram is drawn from that trace, so you can check it against what the code actually did on that request.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">31</span><span class="lbl">tests in CI</span></div>
  <div class="stat"><span class="num">3</span><span class="lbl">carrier adapters</span></div>
  <div class="stat"><span class="num">~15</span><span class="lbl">lines to add a fourth</span></div>
</div>

## What it does

There is a single use case, quoting a package, and it runs against three adapters inside the
same request. **In the published version the three carriers are stubs**: a separate FastAPI
sub-app that mimics their APIs, wired through `ASGITransport` without opening a socket. The
same domain produces three different quotes without knowing there are three carriers.
Persistence and error handling are real.

<figure class="shot">
  <img src="{{ '/assets/img/shipping-quote-circuito.gif' | relative_url }}" alt="Animation of the hexagonal circuit: a request comes in over HTTP, crosses the primary adapter, the port, the use case and the domain, exits through the secondary port into the three carrier adapters and returns with the quotes." loading="lazy" width="1168" height="715">
  <figcaption>The circuit as travelled by a real request, hop by hop. The sequence is taken from the trace the response returns.</figcaption>
</figure>

## The circuit

```
entry -> adapter -> port -> use case -> domain -> port -> adapter -> exit
(POST)   quote_     Shipping  QuoteShipping  pipeline  Carrier  *Adapter  carrier
         controller QuotePort UseCase        steps     Port               API
```

`main.py` is the composition root: it wires everything in the lifespan. The domain
(`Package`, zones, `FeePolicy`, `Tracer`) imports nothing from the outside.

**The trace comes back inside the response.** A 2.5 kg package to postal code 1425 returns
eighteen steps, each with its own timing: entry, adapter, port, the domain steps, the three
carrier adapters and exit. The same JSON shows the volumetric weight rule being applied:
2.5 kg actual against 4.8 kg effective.

## Design decisions

**Money is kept in `Decimal`, never in `float`.** The service fee is calculated in `Decimal`
and rounded with an explicit `ROUND_HALF_UP`. Python's built-in `round()` uses banker's
rounding, which gives unexpected results on money amounts. The test
`test_apply_service_fee_rounds_half_up_not_banker` pins that difference. The explicit
rounding came in as a technical debt payoff.

**One class for all three carriers.** `HttpCarrierAdapter` is configured by composition,
with an endpoint and two mapping functions, and the try/except/timeout is written once.
Adding a fourth carrier is a file of about fifteen lines.

**One carrier fails on purpose.** The Correo Argentino mock returns an error roughly 15% of
the time. The use case runs all three through `asyncio.gather`, and when one fails it still
answers with the other two quotes.

**Tracing goes through a `Tracer`.** A trace has a single consumer and a strict order, so the
`Tracer` is passed by reference through the layers. A pub/sub event bus with a single
consumer would only add indirection.

**A primary port for a single implementation.** By YAGNI, `ShippingQuotePort` is
unnecessary. It stays because without it the driving side of the hexagon is implicit and the
circuit can no longer be traced end to end. The ABC's docstring says so, so nobody reads it
as an oversight.

**Effective weight is `max(actual weight, length × width × height / 5000)`**, the standard
volumetric weight formula.

## Out of scope

There is no authentication and no rate limiting, and the carrier can't be chosen: all three
are always quoted.

The Alembic migrations are deliberately kept apart from the `create_all()` at startup:
hooking them into the lifespan would have made the tests migrate the real database instead
of the in-memory one, because the tests patch the engine rather than the URL.
