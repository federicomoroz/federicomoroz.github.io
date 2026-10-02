---
title: Shipping Quote — .NET
description: "The same shipping quoter, ported to ASP.NET Core over the same ports and use cases. The port found two bugs the original had never shown."
permalink: /en/projects/shipping-quote-dotnet/
---

<p class="crumbs"><a href="{{ '/en/tools/' | relative_url }}">{{ site.data.i18n[page.lang].services.back }}</a></p>

<section class="hero">
  <h1>Shipping Quote — .NET <span class="tag active">active</span></h1>
  <p class="lead">The same <strong>hexagonal architecture</strong> shipping quoter that exists in Python, ported to <strong>ASP.NET Core</strong>. The port <strong>found two bugs</strong> the original had never surfaced.</p>
  <div class="chip-row">
    <span class="tag">C#</span><span class="tag">.NET 8</span><span class="tag">ASP.NET Core</span>
    <span class="tag">EF Core</span><span class="tag">MySQL</span><span class="tag">Testcontainers</span>
    <span class="tag">xUnit</span><span class="tag">Docker</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/shipping-quote-dotnet" target="_blank" rel="noopener">Repo ↗</a>
    <a href="{{ '/en/projects/shipping-quote/' | relative_url }}">The Python version →</a>
    <a href="{{ '/en/projects/nexo/' | relative_url }}">The fuller .NET project &rarr;</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">The design decision</p>
  <p>Porting the system to another stack shows which parts were architecture and which were habit. The ports, the pipeline and the pricing policy carried over to the new language intact. What had to be redone were decisions that looked neutral in Python and turned out not to be in .NET.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">63</span><span class="lbl">tests in CI</span></div>
  <div class="stat"><span class="num">306<small>ms</small></span><span class="lbl">3 carriers at 300ms each</span></div>
  <div class="stat"><span class="num">2</span><span class="lbl">bugs the port found</span></div>
</div>

## Concurrency, measured by a test

The three carriers are queried in parallel with `Task.WhenAll`, so a request takes as long
as the slowest one. That is easy to break without noticing: an `await` inside a `foreach`
compiles, passes the tests and silently triples the service's latency.

So there is a test that **measures** it:

```
3 carriers × 300ms          →  306 ms      sequential would be 900
latencies 50 / 150 / 400    →  399 ms      the sum would be 600
```

The test fails past 700ms. What it checks is the request's wall-clock time.

What keeps that true across the service:

- **`async`/`await` end to end.** Not a single `.Result` or `.Wait()` in the repo: nothing
  blocks a pool thread waiting on I/O.
- **`Task.Delay`, never `Thread.Sleep`.** Waiting doesn't occupy a thread, and with a
  thousand concurrent requests that decides whether the pool holds up or runs out.
- **`CancellationToken` threaded down to the adapter.** If the client hangs up, in-flight
  calls are cut. A test with a 30-second carrier returns in 67ms.
- **`CreateLinkedTokenSource` for the contract timeout.** The timeout doesn't override the
  incoming request's cancellation, and both are honoured.
- **Every request gets its own `TraceRecorder`.** One test fires 40 concurrent requests and
  verifies no trace bleeds into another. If there were shared mutable state, that test
  would catch it.

## First bug: SQLite and concurrent writes

The port started on SQLite, like the original. The twenty-concurrent-quotes test failed:

```
SqliteException : SQLite Error 5: 'database is locked'
```

SQLite **serializes writes**, and the service was stalling at the one point where it
writes. The first fix was a `busy_timeout`: the second write waits instead of failing,
which only trades the error for latency.

The database moved to **MySQL**:

| On SQLite | On MySQL |
|---|---|
| money stored as `TEXT` | native `decimal(12,2)` |
| timestamp as an integer of ticks | `datetime(6)`, microsecond precision |
| `busy_timeout` to avoid failing | real concurrent writes |
| `EnsureCreated` | EF Core migrations |
| — | `EnableRetryOnFailure` on deadlocks |

Without `datetime(6)`, MySQL truncates to whole seconds and two quotes from the same second
can no longer be ordered against each other.

## Second bug: it only shows up against the real engine

The first version stored the history in SQLite, and the integration tests ran against that
real engine instead of an in-memory double. The first run threw:

```
SQLite does not support expressions of type 'DateTimeOffset' in ORDER BY clauses
```

The history endpoint ordered by date, and SQLite can't order a `DateTimeOffset`
server-side. The error happens at **runtime**: the code compiled cleanly and would have
crashed in production on the first request to the history endpoint. Since then the adapter
stores the date in UTC and converts it back to `DateTimeOffset` on read, so the domain keeps
speaking in instants with an offset and the database only sees a `datetime`.

An in-memory double would have hidden it. Both bugs on this page showed up when running
against a real engine, which is why today's integration tests spin up a **real MySQL 8.0**
in an ephemeral container that lives for the length of the run.

## The business rule doesn't know HTTP exists

That a parcel over 30 kg can't be quoted is a business rule. That this is communicated as a
`422` is a transport decision. So they live in different places: the domain throws its
exception and a **middleware** translates it to HTTP.

```csharp
catch (Exception exc) when (exc is PackageTooHeavyException or InvalidPostalCodeException)
```

The controller has no `try/catch` at all, and a new controller inherits the mapping without
writing anything. The pattern is Chain of Responsibility, the same one the ASP.NET Core
pipeline uses underneath: each middleware decides whether it handles the request or passes
it on.

## The hexagon, same as in Python

The hexagonal architecture carried over to the new language intact. There are four
projects with dependencies always pointing inward, and the compiler enforces the
boundaries: the domain cannot import ASP.NET because it doesn't reference it.

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

The three carriers are three **instances** of the same class. Each one contributes only
data: its endpoint and two translation functions. The timeout, error handling and tracing
are written once. Using composition instead of inheritance avoids three nearly identical
classes.

## Scope

The three carriers are **simulated**, same as in the Python version. Here they're mounted
as a custom `HttpMessageHandler`: the `HttpClient` makes a real POST, with real
serialization, status codes and deserialization, but the call never leaves the machine. The
adapter under test is the same binary that would run in production, and the only thing to
swap would be that last link.

The same domain produces three different results without knowing there are three carriers,
and if one goes down the response still goes out.
