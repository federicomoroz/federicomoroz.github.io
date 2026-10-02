---
title: Nexo
description: "A wholesaler was sending its catalogue over FTP once a day. Here the ERP publishes and the network listens. Persistence sits behind ports, and one suite runs the same cases against four engines."
permalink: /en/projects/nexo/
---

<p class="crumbs"><a href="{{ '/en/tools/' | relative_url }}">{{ site.data.i18n[page.lang].services.back }}</a></p>

<section class="hero">
  <h1>Nexo <span class="tag active">active</span></h1>
  <p class="lead">A wholesale distributor was emailing spreadsheets over FTP to 40 resellers, once a day, and <strong>morning stock was useless by the afternoon</strong>. With Nexo, the ERP publishes changes and resellers pull the catalogue over a WebSocket. They then stay on that same connection and receive each change as it is published.</p>
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
  <p>The data in the repository is placeholder, so the system can be published without exposing the client. The documentation is the project's internal set, including the ADRs, the runbook and the ERP integration contract. The code, the measurements and the 356 tests are real and reproduce with the commands in the README.</p>
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
    circuit_foot="A stock change published at 14:03 reaches connected resellers before 14:03:01."

    bp_head="The server does not send the next batch until the previous one is acknowledged."
    bp_alt="Animated backpressure diagram: the server sends a batch of 500 items, waits, and only sends the next one once the reseller's ack arrives."
    bp_server="server"
    bp_client="reseller"
    bp_batch_tag="batch"
    bp_batch="500 items"
    bp_ack_tag="acknowledgement"
    bp_held="holding · nothing goes out"
    bp_foot="A WebSocket write buffer accepts far more than the network on the other side can swallow. Without this pause the server piles up megabytes in memory for every reseller on a slow link while it keeps reading the database at full speed. On the client side the rule is to acknowledge a batch <b>after</b> persisting it."

    eng_head="The application layer references only the domain: zero packages, not one mention of Entity Framework."
    eng_alt="Animated diagram: the same ports on top and four database engines below taking turns, each stamped with 27 of 27 contract cases passed."
    eng_ports="Ports"
    eng_prod="production"
    eng_demo="the demo"
    eng_pre="pre-production"
    eng_mem="In-memory"
    eng_dev="development"
    eng_foot="The same 27 cases run against all four, with no per-provider <code>if</code>. MySQL and PostgreSQL in real containers in CI; without Docker those cases report as skipped. The in-memory provider is written without EF Core, so if the ports leaked anything from EF it would not compile."
%}

<div class="statline">
  <div class="stat"><span class="num">356</span><span class="lbl">tests in CI</span></div>
  <div class="stat"><span class="num">27<small>×4</small></span><span class="lbl">contract cases × engines</span></div>
  <div class="stat"><span class="num">68<small>ms</small></span><span class="lbl">from an ERP change to 40 resellers</span></div>
</div>

## Switching databases is a one-line change

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

The in-memory provider is written without EF, so if the ports leaked anything
from EF, that project would not compile. That is what makes the abstraction
checkable.

On top of that, `tests/Nexo.Persistence.ContractTests` runs **the same 27 cases
against all four providers**, with no per-provider branching. The per-engine
classes are four lines each and define no cases of their own. MySQL and
PostgreSQL run in real containers in CI, with the versioned migrations applied.
Without Docker, those cases report as **skipped**, so a test that did not run
never shows up green.

PostgreSQL was added once everything else was already written. It took two
provider files, its migrations, a fixture and a four-line class. All the
contract cases passed on the first run, without touching any use case,
controller or the WebSocket handler.

## Backpressure: the server waits

A WebSocket's write buffer accepts far more data than the network on the other
side can swallow. Without an acknowledgement per batch, the server piles up
megabytes in memory for every reseller on a slow link while it keeps reading the
database at full speed.

So the server does not send the next batch until the previous `ack` comes back.
The client has to acknowledge only **after** persisting the batch. The protocol
documentation asks for this explicitly, because acknowledging on receipt is the
most likely mistake in an integration.

To join the snapshot and the live stream without losing anything, the
change-log watermark is taken **before** reading the first batch and travels in
the header. If the catalogue changes during the download, those changes still
arrive through the journal afterwards. If the watermark were taken at the end,
they would be lost.

## The access policy and the order of the checks

Every request goes through seven checks, in this order:

```
format → key → validity → allowlist → account → scope → quota
```

Two of those positions have their own tests pinning them down:

- **The IP allowlist is evaluated after verifying the secret.** The other way
  round, someone who knows only the prefix (it is public and appears in logs)
  could probe from different networks and map another account's permitted
  ranges, without holding any valid credential.
- **Quota is consumed last.** It is the only step with a side effect. If it were
  spent before authentication, anyone could deny service to another account by
  sending junk with the victim's prefix.

The WebSocket handshake runs **exactly the same pipeline** as the MVC filter, so
the policy is implemented once for both transports.

## The view: an operations console

The application is MVC (`AddControllersWithViews`, five controllers, Razor
views), but four of the five controllers serve JSON, because the API's
consumers are integrations. The view is a single screen.

<figure class="shot">
  <img src="{{ '/assets/img/nexo-panel.jpg' | relative_url }}" alt="Nexo operations console: four indicators across the top —one active connection, 59 requests per minute, 7 rejections per minute and 4 milliseconds p95 latency—; below, per-reseller activity with each account's requests and rejections, rejections grouped by reason (BadSecret, UnknownKey, ScopeNotGranted), and the live feed showing a stream opening and the rejected credentials." loading="lazy" width="1500" height="823">
  <figcaption>The view, running. The numbers come from real traffic against the local instance: successful queries, invalid credentials being rejected, and a snapshot in flight. The panel reads from the event bus.</figcaption>
</figure>

The panel shows live active connections, per-reseller activity, rejections by
reason and p95 latency. It feeds off the same event bus the authorization
pipeline emits to, **without querying the business database**. If the panel
goes down the API never notices, and there is a test for that.

The data arrives over Server-Sent Events. SignalR was the natural candidate, but
the panel lives behind the VPN, with no internet access to fetch a client from a
CDN, and the repo has no front-end build. `EventSource` ships with the browser
and reconnects on its own. For one-way traffic, that is enough.

## Per-key quota, shared across instances

Every credential carries its own per-minute quota, and the step that spends it is
the last in the pipeline. The count lives in Redis, as a sliding window over a
sorted set. The four operations (drop what expired, count, add and renew the
TTL) go in **a single Lua script**. Split across four round trips, two instances
could both read 119 at the same time and both let the request through.

If Redis does not answer, the operator chooses what happens. `PerProcess` keeps
serving against each process's own counter. It is the default, because the
quota exists to protect the distributor's database and a Redis outage should not
become a service outage. `Reject` returns 429 until Redis comes back. Which one
applies depends on whether the quota is a protection or an obligation.

## Who gets into the panel

With an identity provider configured, the panel requires sign-in over **OpenID
Connect** (code flow with PKCE, an eight-hour session cookie and an enforceable
group in configuration), and the shared token stops working. If the two
coexisted, the token would let anyone skip the identity check.

The name of the claim carrying the groups is configuration, because it differs
per provider: Entra ID sends `roles`, Okta usually sends `groups`. The suite
runs the whole flow against a Keycloak in a container: discovery, PKCE, login,
code exchange, claims and cookie.

## How it is operated

So that someone else can run and maintain it, the repo includes:

- **Separate `/health/live` and `/health/ready`**, and the liveness one does not
  depend on the database on purpose: if it did, a MySQL outage would have the
  orchestrator killing and restarting healthy containers in a loop.
- **A runbook organised by business symptom**, such as "a reseller is not
  getting changes", "everyone fails at once" or "the ERP is not publishing".
  Each with the actual `curl` calls and queries.
- **The wire protocol spec and one integration guide per type of consumer** (the
  ERP that writes and the reseller that reads), with the error contract and
  recommended batch sizes.
- **Eleven ADRs** recording what was rejected and why, for when someone, six
  months later, proposes one of those alternatives again.

## Log

What changed along the way, and why. The detail for each point is in its ADR.

| What happened | What came out of it |
|---|---|
| The benchmark I wrote to back an ADR **refuted both of its claims**. | The ADR was corrected with the measured table and is still published. The decision now rests on 1 authorization against 96. Speed is no longer part of the argument. ([ADR 0001](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0001-websocket-para-la-sincronizacion-completa.md)) |
| The same search returned different results per engine, and dates shifted by three hours. | Normalisation in the domain, in indexable columns. Neither shows up when you test against a single engine. ([ADR 0008](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0008-columnas-normalizadas-para-busqueda.md)) |
| A test showed that the `X-Forwarded-For` setup found in the samples trusts the header from anyone. | With no proxies declared, header processing is turned off entirely. A rule came out of it too: a comment along the lines of "this is safe because X" is treated as a hypothesis. ([ADR 0009](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0009-forwarded-headers-cierra-por-defecto.md)) |
| The "single writer" assumption was enforced by nothing: two overlapping batches hid a change from the reader. | Writers are serialised with a row lock, and there is a contract case with two writers and a reader. ([ADR 0004](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0004-un-solo-escritor-en-el-diario-de-cambios.md)) |
| Testing OIDC against a real provider found that `ForbidAsync` redirected instead of returning 403, and that the role was never matched. | The whole flow is verified now, and the claim name became configuration. ([ADR 0011](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0011-identidad-del-panel-interno.md)) |
| The first load test gave 0 of 40 connections. | The server never completed the close handshake when the client closed first. Two of the repo's clients were masking it with a `try/catch`. |
| The propagation measurement reported 227 ms, and that number was read as "the cost of dispatching to forty". | With the full curve (1, 5, 10, 20 and 40 connections), the latency does not move: the cost is in the write path and the fan-out is nearly free. A single point cannot separate fixed cost from what scales. |
