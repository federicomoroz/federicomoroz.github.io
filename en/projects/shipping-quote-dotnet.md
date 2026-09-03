---
title: Shipping Quote — .NET
description: "The same shipping quoter, ported to ASP.NET Core. The interesting part wasn't rewriting it: it was what the port exposed."
permalink: /en/projects/shipping-quote-dotnet/
---

<p class="crumbs"><a href="{{ '/en/projects/' | relative_url }}">← Back to projects</a></p>

<section class="hero">
  <h1>Shipping Quote — .NET <span class="tag active">active</span></h1>
  <p class="lead">The same shipping quoter that exists in Python, ported to <strong>ASP.NET Core</strong>. The interesting part wasn't rewriting it: it was that the port <strong>found two bugs</strong> the original had never surfaced.</p>
  <div class="chip-row">
    <span class="tag">C#</span><span class="tag">.NET 8</span><span class="tag">ASP.NET Core</span>
    <span class="tag">EF Core</span><span class="tag">MySQL</span><span class="tag">Testcontainers</span>
    <span class="tag">xUnit</span><span class="tag">Docker</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/shipping-quote-dotnet" target="_blank" rel="noopener">Repo ↗</a>
    <a href="{{ '/en/projects/shipping-quote/' | relative_url }}">The Python version →</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">The design decision</p>
  <p>Porting a system to another stack is the cheapest way to find out which parts were architecture and which were habit. What survived the language change —the ports, the pipeline, the pricing policy— was design. What had to be redone were decisions that looked neutral in Python and turned out not to be in .NET.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">63</span><span class="lbl">tests in CI</span></div>
  <div class="stat"><span class="num">306<small>ms</small></span><span class="lbl">3 carriers at 300ms each</span></div>
  <div class="stat"><span class="num">2</span><span class="lbl">bugs the port found</span></div>
</div>

## Concurrency, measured rather than claimed

The three carriers are queried in parallel with `Task.WhenAll`: a request takes as long as
the slowest one, not the sum of the three. That is easy to write and easy to break without
noticing — someone puts an `await` inside a `foreach`, it still compiles, the tests still
pass, and the service silently triples its latency.

So there is a test that **measures** it:

```
3 carriers × 300ms          →  306 ms      sequential would be 900
latencies 50 / 150 / 400    →  399 ms      the sum would be 600
```

The test fails past 700ms. It doesn't verify that the code says `Task.WhenAll`; it verifies
that the clock behaves as if it did.

Around that, what makes it true rather than accidental:

- **`async`/`await` end to end.** Not a single `.Result` or `.Wait()` in the repo: nothing
  blocks a pool thread waiting on I/O.
- **`Task.Delay`, never `Thread.Sleep`.** Waiting without occupying a thread is the
  difference between handling a thousand concurrent requests and running out of pool.
- **`CancellationToken` threaded down to the adapter.** If the client hangs up, in-flight
  calls are cut. A test with a 30-second carrier returns in 67ms.
- **`CreateLinkedTokenSource` for the contract timeout**, so it doesn't override the
  incoming request's cancellation: it honours both.
- **Every request gets its own `TraceRecorder`.** One test fires 40 concurrent requests and
  verifies no trace bleeds into another. That's the test that would expose shared mutable
  state, if there were any.

## The first bug: the wrong database

The port started on SQLite, like the original. The twenty-concurrent-quotes test failed:

```
SqliteException : SQLite Error 5: 'database is locked'
```

SQLite **serializes writes**. Which means a service built to demonstrate concurrent work
was stalling at the one point where it writes. The first fix was a `busy_timeout`, which
makes the second write wait instead of failing — turning an error into latency rather than
solving anything.

The database moved to **MySQL**, and what had been a patch became design:

| On SQLite | On MySQL |
|---|---|
| money stored as `TEXT` | native `decimal(12,2)` |
| timestamp as an integer of ticks | `datetime(6)`, microsecond precision |
| `busy_timeout` to avoid failing | real concurrent writes |
| `EnsureCreated` | EF Core migrations |
| — | `EnableRetryOnFailure` on deadlocks |

The `datetime(6)` isn't fussiness: without microseconds, MySQL truncates to whole seconds
and two quotes from the same second can no longer be ordered against each other.

## The second bug: one only a real database shows

The integration tests spin up a **real MySQL 8.0**, ephemeral, in a container that lives
for the length of the run. Not an in-memory fake.

That decision paid for itself immediately. The first run against the real engine threw:

```
SQLite does not support expressions of type 'DateTimeOffset' in ORDER BY clauses
```

The history endpoint ordered by date, and `DateTimeOffset` can't be ordered server-side.
It's a **runtime** error, not a compile-time one: the code compiled cleanly and would have
crashed in production on the first request to the history endpoint.

An in-memory double would have hidden it. The two most expensive bugs in this project
surfaced because there was a real engine on the other side.

## The business rule doesn't know HTTP exists

That a parcel over 30 kg can't be quoted is a business rule. That this is communicated as a
`422` is a transport decision. Two different things, living in two different places: the
domain throws its exception, and a **middleware** translates it to HTTP.

```csharp
catch (Exception exc) when (exc is PackageTooHeavyException or InvalidPostalCodeException)
```

The controller has no `try/catch` at all. A new one inherits the mapping without writing
anything. It's Chain of Responsibility — which is exactly what the ASP.NET Core pipeline
is underneath: each middleware decides whether it handles the request or passes it on.

## What didn't change

Four projects, with dependencies always pointing inward:

```
ShippingQuote.Domain           no dependencies
      ▲
ShippingQuote.Application      ports and use cases
      ▲
ShippingQuote.Infrastructure   adapters — HTTP, EF Core
      ▲
ShippingQuote.Api              controllers, middleware, DI
```

The use case takes an `IEnumerable<ICarrierPort>` and doesn't know how many carriers there
are, who they are, or that they speak HTTP. Adding a fourth is one entry in the catalogue
and one line in the composition root.

And the three carriers are three **instances** of the same class, not three subclasses:
each contributes only data — its endpoint and two translation functions — while the
timeout, error handling and tracing live in exactly one place. Composition over
inheritance, which is the only thing that prevents three nearly identical classes.

## Honesty about scope

The three carriers are **simulated**, same as in the Python version. Here they're mounted
as a custom `HttpMessageHandler`: the `HttpClient` makes a real POST, with real
serialization, status codes and deserialization, but never leaves the machine. The adapter
under test is the same binary that would run in production; the only thing swapped is that
last link.

The value isn't in having integrated a real carrier. It's that the same domain produces
three different results without knowing there are three, and that one of them can fail
without taking the response down with it.
