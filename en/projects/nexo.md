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
    <a href="https://github.com/federicomoroz/nexo/tree/main/docs/adr" target="_blank" rel="noopener">The eleven ADRs ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">About the scenario</p>
  <p>The data in the repository is placeholder: the system is published without exposing the client. What is here is the project's internal documentation —ADRs, runbook and the ERP integration contract included— and the code, the measurements and the 356 tests are real, and they reproduce with the commands in the README.</p>
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
    eng_alt="Animated diagram: the same ports on top and four database engines below taking turns, each stamped with 27 of 27 contract cases passed."
    eng_ports="Ports"
    eng_prod="production"
    eng_demo="the demo"
    eng_pre="pre-production"
    eng_mem="In-memory"
    eng_dev="development"
    eng_foot="The same 27 cases run against all four, with no per-provider <code>if</code>. MySQL and PostgreSQL in real containers in CI; without Docker those cases report as skipped, never green. The in-memory provider uses no EF Core at all: it is the one that proves the ports leak nothing."
%}

<div class="statline">
  <div class="stat"><span class="num">356</span><span class="lbl">tests in CI</span></div>
  <div class="stat"><span class="num">27<small>×4</small></span><span class="lbl">contract cases × engines</span></div>
  <div class="stat"><span class="num">68<small>ms</small></span><span class="lbl">from an ERP change to 40 resellers</span></div>
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
| PostgreSQL | the deployment configuration | EF Core, its own migrations |
| SQLite | pre-production | EF Core, its own migrations |
| In-memory | development and tests | by hand, **not a line of EF** |

The fourth is what makes the abstraction verifiable rather than declarative: if
the ports leaked anything from EF, that project would not compile.

On top of that, `tests/Nexo.Persistence.ContractTests` runs **the same 27 cases
against all four providers**, with no per-provider branching. The per-engine
classes are four lines each and define no cases of their own. MySQL and
PostgreSQL run in real containers in CI, with the versioned migrations applied;
without Docker those cases report as **skipped, never green** — a test that
passes without running is worse than no test.

**The proof arrived on its own.** PostgreSQL was added once everything else was
already written: two provider files, its migrations, a fixture and a four-line
class. All the contract cases passed on the first run, and not one use case, controller or
WebSocket handler was touched.

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

## Per-key quota, shared across instances

Every credential carries its own per-minute quota, and the step that spends it is
the last in the pipeline. The count lives in Redis, as a sliding window over a
sorted set, and the four operations — drop what expired, count, add, renew the
TTL — go in **a single Lua script**. Split across four round trips, two instances
both read 119 at the same time and both let the request through.

What happens when Redis does not answer is an operator's choice, not a decision
made in this code: `PerProcess` keeps serving against each process's own counter
— the default, because the quota exists to protect the distributor's database and
a Redis outage should not become a service outage — and `Reject` returns 429
until it comes back. Which one applies depends on whether the quota is a
protection or an obligation.

## Who gets into the panel

With an identity provider configured, the panel requires sign-in over **OpenID
Connect** — code flow with PKCE, an eight-hour session cookie, and an enforceable
group in configuration — and the shared token stops working. If the two
coexisted, the token would be a back door around the identity check.

The name of the claim carrying the groups is configuration, because it differs
per provider: Entra ID sends `roles`, Okta usually sends `groups`. The whole flow
— discovery, PKCE, login, code exchange, claims and cookie — runs in the suite
against a Keycloak in a container.

## How it is operated

A service someone else will maintain needs more than endpoints:

- **Separate `/health/live` and `/health/ready`**, and the liveness one does not
  depend on the database on purpose: if it did, a MySQL outage would have the
  orchestrator killing and restarting healthy containers in a loop.
- **A runbook organised by business symptom**, not by component: "a reseller is
  not getting changes", "everyone fails at once", "the ERP is not publishing".
  Each with the actual `curl` calls and queries.
- **The wire protocol spec and one integration guide per type of consumer** — the
  ERP that writes and the reseller that reads — with the error contract and
  recommended batch sizes.
- **Eleven ADRs** recording what was rejected and why, which is the useful part
  six months later, when someone proposes exactly what was already rejected.

## Log

What changed, and why. It is here because the progression says more than a final
snapshot, and it is short because the detail lives in the ADRs.

| What happened | What came out of it |
|---|---|
| The benchmark I wrote to back an ADR **refuted both of its claims**. | The ADR was corrected with the measured table, not deleted. The real argument is 1 authorization against 96, not speed. ([ADR 0001](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0001-websocket-para-la-sincronizacion-completa.md)) |
| The same search returned different results per engine, and dates shifted by three hours. | Normalisation in the domain, in indexable columns. Neither shows up when you test against a single engine. ([ADR 0008](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0008-columnas-normalizadas-para-busqueda.md)) |
| A test showed that the `X-Forwarded-For` setup every sample copies trusts the header from anyone. | With no proxies declared, header processing is turned off entirely. And a rule: a comment saying "this is safe because X" is a hypothesis. ([ADR 0009](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0009-forwarded-headers-cierra-por-defecto.md)) |
| The "single writer" assumption was enforced by nothing: two overlapping batches hid a change from the reader. | Writers are serialised with a row lock, and there is a contract case with two writers and a reader. ([ADR 0004](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0004-un-solo-escritor-en-el-diario-de-cambios.md)) |
| Testing OIDC against a real provider found that `ForbidAsync` redirected instead of returning 403, and that the role was never matched. | The whole flow is verified now, and the claim name became configuration. ([ADR 0011](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0011-identidad-del-panel-interno.md)) |
| The first load test gave 0 of 40 connections. | The server never completed the close handshake when the client closed first. Two of the repo's clients were masking it with a `try/catch`. |
| The propagation measurement reported 227 ms and I quoted it as "the cost of dispatching to forty". | With the full curve — 1, 5, 10, 20 and 40 connections — the latency does not move: the cost is in the write path and the fan-out is nearly free. A single point cannot separate fixed cost from what scales. |

## What it does not do

- **It is not integrated with a real provider of the distributor's.** There is
  OIDC verified against Keycloak; there is no tenant registered.
- **The measurements are from localhost.** What holds outside is the shape of the
  curve, not the milliseconds.
- **There is no deployed demo.** There is a deployment descriptor and nothing
  running.
- **It runs as a single instance.** The quota is shared now, but the journal and
  the change signal are per process: with two instances, a change published on
  one does not wake the connections on the other.

Each one is in the ADRs with its rejected alternative beside it. An ADR with no
downsides was not thought through.
