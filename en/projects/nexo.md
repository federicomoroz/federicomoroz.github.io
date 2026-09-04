---
title: Nexo
description: "A wholesaler was sending its catalogue over FTP once a day. Here the ERP publishes and the network listens. Persistence sits behind ports, and one suite runs the same cases against four engines."
permalink: /en/projects/nexo/
---

<p class="crumbs"><a href="{{ '/en/projects/' | relative_url }}">← Back to projects</a></p>

<section class="hero">
  <h1>Nexo <span class="tag active">active</span></h1>
  <p class="lead">A wholesale distributor was emailing spreadsheets over FTP to 40 resellers, once a day, and <strong>morning stock was useless by the afternoon</strong>. Here the ERP publishes, resellers pull the catalogue over a WebSocket, and they stay on that same connection receiving changes.</p>
  <div class="chip-row">
    <span class="tag">C#</span><span class="tag">.NET 8</span><span class="tag">ASP.NET Core MVC</span>
    <span class="tag">WebSocket</span><span class="tag">SSE</span><span class="tag">EF Core</span>
    <span class="tag">MySQL</span><span class="tag">PostgreSQL</span><span class="tag">Testcontainers</span>
    <span class="tag">xUnit</span><span class="tag">Docker</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/nexo" target="_blank" rel="noopener">Repo ↗</a>
    <a href="https://federicomoroz.github.io/nexo/" target="_blank" rel="noopener">Project page ↗</a>
    <a href="https://github.com/federicomoroz/nexo/tree/main/docs/adr" target="_blank" rel="noopener">The nine ADRs ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">About the scenario</p>
  <p>The distributor and its reseller network are a constructed scenario, and the repo says so. I wrote it the way that project's internal documentation would be written —ADRs, runbook and the ERP integration contract included— because that was the exercise: to see whether I could hold up a whole system rather than a demo endpoint. The code, the measurements and the 306 tests are real, and they reproduce with the commands in the README.</p>
</div>

{% include nexo-diagramas.html
    circuit_head="The ERP publishes; the network queries and listens. The change journal carries a sequential number, and each reseller stores how far it has read."
    circuit_alt="Animated diagram of the circuit: the ERP writes into Nexo, resellers query it, and Nexo pushes changes back to them. Below, the change journal watermark."
    erp_sub="catalogue · prices<br>stock levels"
    pipe_write="the ERP writes"
    pipe_read="the network queries"
    pipe_push="Nexo pushes changes"
    peer_1="Sanitarios Sur"
    peer_2="Ferretera Norte"
    peer_3="Casa Grande"
    peer_more="+ 37 resellers"
    watermark_label="journal watermark"
    circuit_foot="A stock change published at 14:03 reaches connected resellers before 14:03:01. That is what the morning FTP file could not do."

    bp_head="The server does not send the next batch until the previous one is acknowledged."
    bp_alt="Animated backpressure diagram: the server sends a batch of 500 items, waits, and only sends the next one once the reseller's ack arrives."
    bp_server="server"
    bp_client="reseller"
    bp_batch_tag="batch"
    bp_batch="500 items"
    bp_ack_tag="acknowledgement"
    bp_held="holding · nothing goes out"
    bp_foot="A WebSocket write buffer accepts far more than the network on the other side can swallow. Without this pause the server piles up megabytes in memory for every reseller on a slow link while it keeps reading the database at full speed. On the client side the rule is to acknowledge <b>after</b> persisting the batch, not on receipt."

    eng_head="The application layer references only the domain: zero packages, not one mention of Entity Framework."
    eng_alt="Animated diagram: the same ports on top and four database engines below taking turns, each stamped with 24 of 24 contract cases passed."
    eng_ports="Ports"
    eng_prod="production"
    eng_demo="the demo"
    eng_pre="pre-production"
    eng_mem="In-memory"
    eng_dev="development"
    eng_foot="The same 24 cases run against all four, with no per-provider <code>if</code>. MySQL and PostgreSQL in real containers in CI; without Docker those cases report as skipped, never green. The in-memory provider uses no EF Core at all: it is the one that proves the ports leak nothing."
%}

<div class="statline">
  <div class="stat"><span class="num">306</span><span class="lbl">tests in CI</span></div>
  <div class="stat"><span class="num">24<small>×4</small></span><span class="lbl">contract cases × engines</span></div>
  <div class="stat"><span class="num">4</span><span class="lbl">bugs the tests found</span></div>
</div>

## Switching databases is a one-line change

Here that sentence is backed by a suite, not by a diagram.

All persistence goes through ports declared in the application layer, which
**references only the domain: zero packages, not one mention of Entity
Framework**. There are four implementations, chosen by configuration:

```json
"Nexo": { "Persistence": { "Provider": "MySql" } }
```

| Provider | Where it runs | How it is built |
|---|---|---|
| MySQL | production | EF Core, its own migrations |
| PostgreSQL | the deployed demo | EF Core, its own migrations |
| SQLite | pre-production | EF Core, its own migrations |
| In-memory | development and tests | by hand, **not a line of EF** |

The fourth is what makes the abstraction verifiable rather than declarative: if
the ports leaked anything from EF, that project would not compile.

On top of that, `tests/Nexo.Persistence.ContractTests` runs **the same 24 cases
against all four providers**, with no per-provider branching. The per-engine
classes are four lines each and define no cases of their own. MySQL and
PostgreSQL run in real containers in CI, with the versioned migrations applied;
without Docker those cases report as **skipped, never green** — a test that
passes without running is worse than no test.

**The proof arrived on its own.** PostgreSQL was added once everything else was
already written: two provider files, its migrations, a fixture and a four-line
class. All 24 cases passed on the first run, and not one use case, controller or
WebSocket handler was touched.

## What the suite caught before production

Not a decorative list. These were bugs in the code.

**Search returned different results depending on the engine.**
`string.Contains` translates to `instr()` in SQLite, which is case-sensitive;
MySQL with its default collation is not. In production that shows up as "it
sometimes can't find the item", and differently per environment, which is one of
the hardest reports to chase. The fix was not a patch: normalisation lives in the
domain and is stored in its own columns, which are also indexable —
`UPPER(name) LIKE ...` is not.

**Timestamps shifted by three hours.** MySQL has no timezone-aware type and the
driver flattens it silently. The same value read on an Argentine machine and in a
UTC container produced two different instants.

Neither would have been found testing against a single engine.

## The benchmark refuted my own ADR

I wrote an architecture decision record justifying why the catalogue download
goes over a WebSocket instead of paginated HTTP. I claimed it saved about a
hundred network round trips and half the payload.

Then I wrote the tool that measures it. Over 48,000 items, against MySQL:

| Method | Round trips | Authentications | Bytes | Time |
|---|---|---|---|---|
| Paginated HTTP | 96 | **96** | 9.9 MB | 1.02 s |
| WebSocket | **97** | **1** | 10.0 MB | 0.79 s |

Both claims were wrong. The WebSocket makes **one more** round trip, not a
hundred fewer — because my own design waits for an acknowledgement per batch, so
there is one exchange per batch just as in pagination. And the payload is the
same.

I did not delete the ADR. I added a correction section saying the original
reasoning was wrong, put the measured table in, and rewrote the argument around
the only thing the measurement supports: **96 authentications versus one**,
because every HTTP request pays the whole pipeline and the WebSocket pays it once
at the handshake. And the real reason, which appears in no speed table: once the
snapshot ends, that same connection carries the live changes.

The timings are measured on localhost and the document says so in those words.
They do not extrapolate to a reseller on the other side of the country.

## Backpressure: the server waits

A WebSocket's write buffer will happily accept far more than the network on the
other side can swallow. Without an acknowledgement per batch, the server piles up
megabytes in memory for every reseller on a slow link while it keeps reading the
database at full speed.

So the next batch does not go out until the previous `ack` comes back. On the
client side that means acknowledging **after** persisting the batch, not on
receipt, and that is spelled out in the protocol documentation because it is the
mistake the first integrator will make.

The join between the snapshot and the live stream is what keeps anything from
being lost: the change-log watermark is taken **before** reading the first batch
and travels in the header. If the catalogue changes during the download, those
changes still arrive through the journal afterwards. Taking it at the end would
be the bug.

## The access policy, and why order matters

Seven checks, in an order that is not incidental:

```
format → key → validity → allowlist → account → scope → quota
```

Two positions are non-negotiable and have their own tests:

- **The IP allowlist is evaluated after verifying the secret.** The other way
  round, someone who knows only the prefix —which is public and appears in logs—
  can probe from different networks and map another account's permitted ranges,
  without holding any valid credential.
- **Quota is consumed last.** It is the only step with a side effect: before
  authentication, anyone could deny service to anyone by sending junk with the
  victim's prefix.

The WebSocket handshake runs **exactly the same pipeline** as the MVC filter. One
implementation of the policy, two transports.

### The hole a test found

The IP allowlist depends on knowing the real client IP behind the proxy, which
arrives in `X-Forwarded-For`. I had left the known-proxy lists empty by default,
with a comment saying: "with the list empty the header is ignored, which is the
safe behaviour."

I wrote the test that sends a forged `X-Forwarded-For` with no proxies configured
and expects a 403. It returned 200.

`ForwardedHeadersMiddleware` **only validates the header's origin if there is
something** in `KnownProxies` or `KnownNetworks`. With both lists empty — the
default — it trusts anyone. So in the default configuration, anyone with a valid
credential could bypass the allowlist with a forged header.

Now, with no proxies declared, header processing is switched off entirely. The
resulting failure mode is deliberately loud: misconfigured behind a proxy, the
whole network is locked out at once, which is impossible to miss.

What I took from it is not "test everything". It is that **a comment saying "this
is safe because X" is a hypothesis**, and this one was wrong for days without
bothering anyone.

## The view: an operations console

It is genuine MVC — `AddControllersWithViews`, five controllers, Razor views —
though to be precise: four of the five serve JSON, because integrations sit on
the other side, not browsers. The view is a single screen, and that is the right
call.

<figure class="shot">
  <img src="{{ '/assets/img/nexo-panel.jpg' | relative_url }}" alt="Nexo operations console: four indicators across the top —one active connection, 59 requests per minute, 7 rejections per minute and 4 milliseconds p95 latency—; below, per-reseller activity with each account's requests and rejections, rejections grouped by reason (BadSecret, UnknownKey, ScopeNotGranted), and the live feed showing a stream opening and the rejected credentials." loading="lazy" width="1500" height="823">
  <figcaption>The view, running. The numbers come from real traffic against the local instance: successful queries, invalid credentials being rejected, and a snapshot in flight. The panel feeds off the event bus, not the business database.</figcaption>
</figure>

The panel shows active connections, per-reseller activity, rejections by reason
and p95 latency, live. It **does not query the business database**: it feeds off
the same event bus the authorization pipeline emits to. If the panel goes down
the API never notices, and there is a test for that.

It runs on Server-Sent Events rather than SignalR, which was the natural
candidate. The reason is deployment, not technology: the panel lives behind the
VPN, with no internet access to fetch a client from a CDN, and there is no
front-end build in the repo. `EventSource` ships with the browser, reconnects on
its own, and for one-way traffic that is enough.

## What is not solved

Written in the repo, not here to look good:

- **Quota is per process.** With two instances behind a load balancer each
  enforces its own. The way out is implementing the same port against Redis; not
  done, because it is not needed yet.
- **There is no load test.** The design avoids the obvious problem —
  backpressure, bounded queues, `async` end to end — but that is design, not
  measurement, and I will not present one as the other.
- **The panel is protected by a shared token.** Enough behind the VPN; if it goes
  public it needs the corporate SSO.
- **Search does not strip accents.** "Válvula" and "Valvula" are different.

All four are in the ADRs with the way out noted. An ADR with no downsides was not
thought through.
