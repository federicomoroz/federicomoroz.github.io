---
title: Comanda
description: "Restaurant management: orders on a tablet, a kitchen screen and printer per station, a register with electronic invoicing, stock by recipe and owner alerts. It runs on a computer at the restaurant and keeps working without internet."
permalink: /en/projects/comanda/
---

<p class="crumbs"><a href="{{ '/en/projects/' | relative_url }}">← Back to projects</a></p>

<section class="hero">
  <h1>Comanda <span class="tag active">active</span></h1>
  <p class="lead">Waiters take orders on a tablet, every kitchen station gets its own items on screen and on paper, and the register charges and invoices. It all runs on a computer at the restaurant, so <strong>if the internet goes down, the floor keeps working</strong>.</p>
  <div class="chip-row">
    <span class="tag">C#</span><span class="tag">.NET 8</span><span class="tag">ASP.NET Core MVC</span>
    <span class="tag">SignalR</span><span class="tag">EF Core</span><span class="tag">React</span>
    <span class="tag">TypeScript</span><span class="tag">PostgreSQL</span><span class="tag">Docker</span>
    <span class="tag">xUnit</span><span class="tag">Testcontainers</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/comanda-docs/blob/main/README.en.md" target="_blank" rel="noopener">Docs ↗</a>
    <a href="https://github.com/federicomoroz/comanda-docs/blob/main/docs/adr/0001-facturacion-como-servicio-aparte.md" target="_blank" rel="noopener">Why invoicing runs apart (in Spanish) ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">About the data</p>
  <p>It is an MVP to present to a restaurant. The starting menu comes from the public online menu of a real grill; everything else (drinks, tables, staff, ingredients, costs and tax data) is simulated, and invoicing runs against a simulated ARCA, the Argentine tax authority, so invoices print as "not valid for tax purposes". The app is in Spanish. The code is private; the docs, screenshots and diagrams are public.</p>
</div>

<figure class="shot">
  <video controls muted playsinline preload="metadata" poster="{{ '/assets/img/comanda-video-poster-en.jpg' | relative_url }}" width="1566" height="936">
    <source src="{{ '/assets/video/comanda-en.mp4' | relative_url }}" type="video/mp4">
  </video>
  <figcaption>An order end to end, in one take with the application running. On the left, the waiter's tablet; on the right, the kitchen and then the register. The ticket reaches the kitchen the moment it is sent, and the invoice comes back authorized on its own.</figcaption>
</figure>

<div class="statline">
  <div class="stat"><span class="num">173</span><span class="lbl">tests, both services on real databases</span></div>
  <div class="stat"><span class="num">14<small>s</small></span><span class="lbl">for a waiting invoice to go out on its own once billing is back</span></div>
  <div class="stat"><span class="num">0</span><span class="lbl">invoices lost with billing or ARCA down</span></div>
</div>

## A shift, from every post

**The waiter** sees the whole floor: which tables are free, each one's total, who serves it, whether it has dishes ready to serve or has asked for the bill. They enter the order with its options (doneness, salad toppings, soda flavour) and send it. **The kitchen** has one screen per station with the day's numbered tickets. Each turns amber at 12 minutes and red at 20; both numbers change from the admin.

<div class="shot-pair">
  <figure class="shot">
    <img src="{{ '/assets/img/comanda-salon.jpg' | relative_url }}" alt="The floor on the waiter's tablet: free tables in white and busy ones with their total, waiter and flags such as «5 listos» (5 ready), «Cuenta» (bill) or «1 sin enviar» (1 not sent)." loading="lazy" width="834" height="1112">
    <figcaption>The floor, on the tablet.</figcaption>
  </figure>
  <figure class="shot">
    <img src="{{ '/assets/img/comanda-cocina.jpg' | relative_url }}" alt="The kitchen screen with every station: tickets in green, amber and red by how late they are, with doneness and notes highlighted, and a voided order of fries crossed out." loading="lazy" width="1440" height="1150">
    <figcaption>The kitchen, every station. Voided items stay crossed out and, if the station has a printer, a void notice prints too.</figcaption>
  </figure>
</div>

**The register** splits payments across methods, with tips and change, and issues invoices A, B or C without making anyone wait. It lists what was charged but not invoiced yet, and closes the shift with a cash count: what should be there against what was counted.

<figure class="shot">
  <img src="{{ '/assets/img/comanda-factura.jpg' | relative_url }}" alt="The register with an authorized invoice B: issuer data, items, VAT included, CAE and ARCA's QR, marked as a simulated invoice." loading="lazy" width="1440" height="900">
  <figcaption>Invoice B with CAE and a QR in ARCA's format. In this version the CAE comes from a simulator, and the invoice says so twice.</figcaption>
</figure>

**The owner** configures everything on screen, with no code: the menu, prices, each dish's options, stations, tables, staff and their permissions, payment methods and tax data. Every dish has a recipe: charging a tab deducts the ingredients, and the admin shows what each dish earns and which ones fell below the target margin. By Telegram, email or Slack they hear about an ingredient reaching its minimum, a shift closing short or a large void.

<figure class="shot">
  <img src="{{ '/assets/img/comanda-margenes.jpg' | relative_url }}" alt="Admin, recipes and margins, filtered to dishes below the 65% target: price, price before VAT, recipe cost and margin in red." loading="lazy" width="1440" height="610">
  <figcaption>The dishes below the target margin, with their recipe cost.</figcaption>
</figure>

## From the table to the invoice

<figure class="shot">
  <a href="{{ '/diagramas/comanda/circuito_en.html' | relative_url }}"><img src="{{ '/assets/img/comanda-circuito-en.gif' | relative_url }}" alt="Six-step animation: the waiter sends the order; Comanda makes one ticket per station; the kitchen marks it ready and the waiter's tablet knows; the register takes payment; billing asks ARCA for the CAE; the invoice comes back authorized with its QR." loading="lazy" width="1200" height="750"></a>
  <figcaption>An order's whole path. Floor, kitchen and register share one database and one transaction; invoicing runs apart.</figcaption>
</figure>

Charging a tab deducts stock, closes the table and adds to the shift. **Either all of it happens or none of it does**, which is why those parts live together, in one service with one database. Invoicing runs in a separate service, with its own database and queue, because it depends on ARCA, which does not always answer, and because with real ARCA it holds the restaurant's digital certificate.

## If something goes down, nothing is lost

<figure class="shot">
  <a href="{{ '/diagramas/comanda/facturacion_en.html' | relative_url }}"><img src="{{ '/assets/img/comanda-facturacion-en.gif' | relative_url }}" alt="Six-step animation: the invoice request is saved in the outbox together with the tab; billing does not answer and the request waits; billing comes back and the request goes out; ARCA does not answer and the invoice waits in the queue; ARCA is back with the CAE; the status returns to Comanda with its version number." loading="lazy" width="1200" height="750"></a>
  <figcaption>Each service keeps what it owes the other in its outbox, in the same transaction as the change, and retries until it arrives.</figcaption>
</figure>

- **If billing does not answer**, the register shows "waiting for billing" and the reason, and the cashier moves on to the next table. The request stays saved and goes out on its own. Measured with the production images: it went out 14 seconds after the service came back.
- **If ARCA does not answer**, the invoice waits in billing's queue, in order, so numbering stays consecutive. Each retry comes further apart, from 10 seconds to 5 minutes, and the owner gets an alert when it goes down and another when it is back.
- **If something is sent twice**, nothing is duplicated. Every request carries an id, so the same request twice is one invoice, and every status a version number, so an old one arriving late never overwrites a newer one.
- **If billing refuses the request** (a mistyped ID number, say), the cashier sees it at once, with the reason, and can invoice the tab again.

## Works without internet

<figure class="shot">
  <a href="{{ '/diagramas/comanda/instalacion_en.html' | relative_url }}"><img src="{{ '/assets/img/comanda-instalacion-en.gif' | relative_url }}" alt="Five-step animation: tablets, kitchen screens, the register and printers talk to the restaurant's computer; the internet goes down and the floor carries on; invoices and alerts wait in a queue; the internet is back and everything goes out; both databases are backed up." loading="lazy" width="1200" height="750"></a>
  <figcaption>The internet is only needed to invoice and to alert the owner, and both wait in a queue.</figcaption>
</figure>

The whole system installs with Docker Compose on a computer at the restaurant, and tablets, screens and printers connect over the local Wi‑Fi. Both databases back themselves up: on start if the last backup is over a day old, then once a day, to an external disk or a cloud-synced folder. Restoring takes one command, and it backs up the current state first in case the wrong folder was picked.

## For engineers

<figure class="shot">
  <a href="{{ '/diagramas/comanda/arquitectura_en.html' | relative_url }}"><img src="{{ '/assets/img/comanda-arquitectura-en.png' | relative_url }}" alt="Architecture map: on the floor, tablets, kitchen screens, the register and printers; on the restaurant's computer, the server (Comanda.Api, Application, Domain, Infrastructure), the billing service with its queue and outbox, PostgreSQL with two databases, the print agent, notify-router and backups; over the internet, ARCA, the owner's channels and the backup disk. Every connection with its protocol and key." loading="lazy" width="1600" height="1010"></a>
  <figcaption>The whole map: what runs where, how the pieces talk and what each one keeps. The interactive version animates the connections by kind.</figcaption>
</figure>

<div class="cards">
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/comanda/arquitectura_en.html' | relative_url }}">The whole map ↗</a></div>
    <div class="card-desc"><p>The containers, each service's projects, every connection's protocol and key, and each database's tables.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/comanda/circuito_en.html' | relative_url }}">From the table to the invoice ↗</a></div>
    <div class="card-desc"><p>The six steps of an order, from the tablet to the authorized invoice.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/comanda/facturacion_en.html' | relative_url }}">If billing goes down ↗</a></div>
    <div class="card-desc"><p>The outbox both ways, the queue to ARCA and the versioned statuses.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/comanda/instalacion_en.html' | relative_url }}">Works without internet ↗</a></div>
    <div class="card-desc"><p>The installation at the restaurant: what needs the internet, what does not, and the backups.</p></div>
  </article>
</div>

| Service | Why it runs apart |
|---|---|
| **server** (`Comanda.Api`) | Floor, register, kitchen and stock. They stay together because charging a tab touches all of them and has to land whole or not at all, in one transaction. |
| **billing** (`Comanda.Billing`) | Depends on ARCA and, with real ARCA, holds the restaurant's certificate. Own database, queue and outbox; publishes no ports. |
| **print-agent** | Has to run near the printers. Asks over HTTP what to print and sends it as ESC/POS over TCP 9100. |
| **notify-router** | Another language (Python) and release cycle. If it goes down, the floor never notices. |
| **backup** | `pg_dump` of both databases, with retention and restore. |

The decisions the rest stands on:

- **Transactional outbox both ways, with one queue per destination.** notify-router being down does not hold back invoice requests, and a new request never jumps ahead of an older message for the same destination, so numbering stays in order. 2xx is delivered; 5xx, 408 and 429 are retried; any other 4xx is parked with the error shown to the admin.
- **The request is saved first and sent at once.** The cashier sees a refusal right away, and if billing does not answer, the request waits in the queue without anyone re-entering it.
- **The database draws the lines.** Partial unique indexes prevent two open tabs on one table, two open shifts, two live invoices for one tab and two tickets with the same number. Ticket numbers come from an atomic per-day counter. Tabs, shifts and invoices carry a concurrency token.
- **Copies, not references.** Each item keeps the name, price, VAT and station it had when ordered: editing the menu never changes open tabs or history.
- **Sessions checked on every request.** PIN login with lockout, a session cookie and roles; deactivating someone cuts their access at once.
- **A data move without gaps.** Invoices the server issued before billing existed moved to the new service with a migration that, in one transaction, turns every row into an outbox message and drops the old tables. Billing imports them with their original number and CAE. The migration has a test that runs it on a database with data.

The 173 tests run against real PostgreSQL with Testcontainers, and Comanda's also start the billing service in memory, with its own database, talking over HTTP. The whole system was also tested end to end with the production images: billing down, ARCA down, the server down while billing authorizes, the server starting without billing, a full restart and a backup restore.

## What it does not do

- **It does not invoice against real ARCA yet.** That needs the restaurant's digital certificate. It goes behind a single interface (WSAA + WSFEv1) and is tested against ARCA's test environment; invoice types, VAT per rate, numbering, the queue, CAE and QR are already in place.
- **It does not handle several restaurants on one installation.** Each restaurant has its own server and database. A cloud service for many restaurants is a product decision, with data split per restaurant and a syncing agent so it does not depend on the internet.
- **It has not been tested with a restaurant's hardware.** Printing was tested against a simulated TCP printer; it still needs a run with real tablets, screens and a thermal printer.
