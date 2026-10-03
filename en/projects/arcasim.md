---
title: ArcaSim
description: "ARCA's web services, for developing and testing without ARCA: 52 of the 53 current ones, with their WSDL files, their errors with the real texts and their rules, and failures on demand. Going to production changes two addresses and the certificate."
permalink: /en/projects/arcasim/
---

<p class="crumbs"><a href="{{ '/en/tools/' | relative_url }}">{{ site.data.i18n[page.lang].services.back }}</a></p>

<section class="hero">
  <h1>ArcaSim <span class="tag active">active</span></h1>
  <p class="lead"><strong>ARCA's web services, for developing and testing without ARCA,</strong> Argentina's tax authority. An application that invoices uses its real ARCA client against ArcaSim during development, in its tests and in demos. Going to production <strong>changes two addresses and the certificate, not the code</strong>.</p>
  <div class="chip-row">
    <span class="tag">C#</span><span class="tag">.NET 8</span><span class="tag">ASP.NET Core</span>
    <span class="tag">SOAP</span><span class="tag">PostgreSQL</span><span class="tag">Docker</span>
    <span class="tag">xUnit</span><span class="tag">Testcontainers</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/arcasim" target="_blank" rel="noopener">Repo ↗</a>
    <a href="https://github.com/federicomoroz/arcasim/blob/main/docs/api.en.md" target="_blank" rel="noopener">API reference ↗</a>
    <a href="https://github.com/federicomoroz/arcasim/tree/main/docs/arca" target="_blank" rel="noopener">The study of ARCA's API (Spanish) ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">About ARCA</p>
  <p>ArcaSim is not related to ARCA. The taxpayers are fictitious, the CAEs it grants have no tax validity and its access tickets only work against ArcaSim. What does come from ARCA are the WSDL files, the error codes and the texts, taken from its public documentation and from real responses. The panel is in Spanish.</p>
</div>

<figure class="shot">
  <img src="{{ '/assets/img/arcasim-panel.jpg' | relative_url }}" alt="ArcaSim's panel: environment, manual version and clock; fictitious taxpayers with their points of sale; certificates and authorizations; failures on demand; exchange rates, and the table of issued vouchers with their CAE." loading="lazy" width="1425" height="1443">
  <figcaption>The panel. What WSASS does at ARCA (certificates and authorizations), ArcaSim does here, and it also moves the clock and causes failures.</figcaption>
</figure>

<div class="statline">
  <div class="stat"><span class="num">52</span><span class="lbl">of ARCA's 53 current web services, with their official WSDL files</span></div>
  <div class="stat"><span class="num">byte for byte</span><span class="lbl">the same as a real ARCA response, except the CAE number</span></div>
  <div class="stat"><span class="num">499</span><span class="lbl">tests, with the client generated from the official WSDL, every service against its WSDL and real PostgreSQL</span></div>
</div>

## What it is for

Invoicing in Argentina goes through ARCA: every invoice needs its authorization code (CAE), and to get it an application signs a request with a digital certificate, gets an access ticket and only then calls the electronic invoicing service. Testing that against ARCA takes a test certificate obtained with the company's tax credentials, and even then the things most worth testing cannot be caused: ARCA not answering, rejecting with a specific code, or the answer getting lost after the CAE was granted.

The usual way out is a simulator written inside each application, which returns a made-up CAE and never quite matches the real protocol. ArcaSim does the opposite: **the application uses, from day one, the same client it will invoice with in production**, and on the other side answers a service that speaks exactly like ARCA.

## Endpoints only

ArcaSim is used the way ARCA is: two URLs and a certificate. Nothing has to be loaded first. It accepts any certificate with a CUIT in its DN, whether the one WSASS issued for homologación or a self-signed one made with openssl, and the taxpayer and the point of sale are created the first time they are used. That is why it works from any language and with any ARCA client: the repository has an example that gets a CAE with openssl and curl alone, and a full [reference](https://github.com/federicomoroz/arcasim/blob/main/docs/api.en.md) of the operations, the errors and the test scenarios.

```bash
docker run -d -p 7080:8080 -v arcasim-data:/data ghcr.io/federicomoroz/arcasim
```

Whoever needs to reproduce ARCA's registration errors (an unauthorized certificate, a point of sale that is not for web services) switches it to strict mode.

## Swapping ArcaSim for ARCA

<figure class="shot">
  <a href="{{ '/diagramas/arcasim/modulo_en.html' | relative_url }}"><img src="{{ '/assets/img/arcasim-modulo-en.gif' | relative_url }}" alt="Five-step animation: the application signs the request and gets its access ticket from ArcaSim; it asks for the CAE of an invoice B; the panel causes failures; the clock expires the ticket or crosses 01/12/2026; for production, the same calls go to ARCA by changing two addresses and the certificate." loading="lazy" width="1200" height="750"></a>
  <figcaption>Nothing changes on the application's side: the client, the calls and the error handling are the same against ArcaSim and against ARCA.</figcaption>
</figure>

To invoice, an application needs two services:

- **WSAA**, which hands out the access ticket. It checks the signed request in ARCA's order, returns the ticket in its exact format with a 12-hour life, and answers with the same errors, including the window that refuses a new ticket while the previous one is still valid.
- **WSFEv1**, electronic invoicing, with its 22 operations: the CAE for one voucher or a batch, the last number authorized, looking up an issued voucher, the parameter tables and the CAEA contingency regime. The manual's validations answer with the code and the text ARCA answers with, missing accents and double spaces included.

The repository also ships **Arca.Client**, the client applications use. It knows nothing about ArcaSim: it signs the request, keeps the ticket until it expires, builds the vouchers and tells a rejection, which gets fixed and sent again, from a failure worth retrying.

## Not just electronic invoicing

ARCA has more than fifty web services, and a company rarely uses WSFEv1 alone: an exporter asks for its CAEs through WSFEXv1, a grain elevator issues waybills through WSCPE and settles through WSLPG, a bank checks debts through SUD, a bonded warehouse reports its movements to customs. **ArcaSim answers 52 of the 53 current services**; the missing one has no published contract.

Each one on its path, with its official WSDL and in its server's dialect: .NET ASMX, Apache Axis2, CXF, JAX-WS or Spring-WS. They refuse a ticket with their own codes and texts, and they do not return sample data: they apply their manual's rules over what ArcaSim keeps.

- **Invoicing**: invoices with items, export invoices, fiscal bonds, tourism and surety insurance, with their numbering, their CAE or CAEA and their validations. What any of them authorizes can be verified through WSCDC, as at ARCA.
- **MiPyME e-credit invoices**: the account between issuer and receiver (accept, reject, cancel, adjust) and, on top of it, the collective deposit agents and the open circulation system.
- **Agriculture**: the waybill end to end (authorize, arrival, unloading, diversion, cancellation), the settlements for grain, livestock, milk, tobacco and sugar cane, the tobacco regime and the delivery notes for flour, meat and sugar.
- **Government agencies**: the Ventanilla Electrónica inbox, supplier debts, fake invoices, gambling, withholding certificates, tax returns, car transfers and VEP payments, the only REST one.
- **Customs**: ten DIA services, from seals and bonded warehouses to duty-free shops.

The registries ARCA fills outside its web services, such as debts, fake invoices or customs declarations, start with fictitious data, and are replaced through the admin API before a test.

## The answer that gets lost

<figure class="shot">
  <a href="{{ '/diagramas/arcasim/recuperacion_en.html' | relative_url }}"><img src="{{ '/assets/img/arcasim-recuperacion-en.gif' | relative_url }}" alt="Six-step animation: the client asks for the last number and requests the CAE of 42; ARCA grants and stores it but the connection drops; a blind resend would get 10016; the client looks up 42 with FECompConsultar and recovers the CAE without duplicating anything." loading="lazy" width="1200" height="750"></a>
  <figcaption>The procedure ARCA's manual prescribes for communication errors, caused on demand from the panel.</figcaption>
</figure>

ARCA is not idempotent: if the answer to a CAE request gets lost and the application sends the same voucher again, ARCA rejects it because that number is already issued. Against the real ARCA this is almost impossible to cause. **ArcaSim causes it on demand**: it grants the CAE, stores it and drops the connection before answering. Arca.Client handles it as the manual says, looking the voucher up before retrying.

The panel also takes the service down, adds a delay, rejects the next voucher with a chosen code and moves the clock: expire the ticket, leave the allowed date range or cross 01/12/2026, when the receiver's VAT condition becomes mandatory.

## Saturation and bottlenecks

<figure class="shot">
  <img src="{{ '/assets/img/arcasim-trafico.jpg' | relative_url }}" alt="The panel's traffic section: two saturation meters, one per service. WSFEv1's reads 58.3 %: of 12 requests in the last minute, 7 refused, 805 ms on average and 1,281 ms at p95, with two served at once, 400 ms each and three places in the queue." loading="lazy" width="1245" height="384">
  <figcaption>Twelve requests at once, with two served at a time and three places in the queue: five go through, seven get a 503, and the meter shows it. The panel is in Spanish.</figcaption>
</figure>

A saturated service slows down or stops answering. ArcaSim reproduces that on its same URLs, with a requests-per-minute limit, a capacity (how many it serves at once and how long each takes) and a queue. What does not fit gets HTTP 503, like a saturated load balancer, and the client has to retry. The meter, ported from [Rate Guardian]({{ '/en/tools/#rate-guardian' | relative_url }})'s, shows which share of the last minute's requests was turned away, and a live log shows every ticket, every CAE and every rejection.

## The same as ARCA, checked

| Level | What matches | How it is checked |
|---|---|---|
| Contract | Paths, ARCA's WSDL files, operations, namespaces, SOAP 1.1 and 1.2 | The client `dotnet-svcutil` generates from ARCA's WSDL, untouched, asks ArcaSim for a CAE over SOAP 1.1 and 1.2 |
| Bytes | One line with the `FEHeaderInfo` header, an empty `<CAE />`, amounts without trailing zeros, the literal `NULL` for empty dates; Apache Axis faults in WSAA | An approved CAE and a rejected resend match recorded ARCA responses byte for byte, except the CAE number |
| Errors | The manual's codes, and the real texts where they are known | A coverage table generated from the code |
| Behavior | Numbering per CUIT, point of sale and type; a batch stops at the first rejection; 12-hour ticket | Scenario tests |
| The other services | Every answer valid against ARCA's WSDL; the refused ticket with each service's codes and texts | A test per operation of every service, plus each one's main flows |

## Used by

<div class="cards">
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/en/projects/comanda/' | relative_url }}">Comanda</a></div>
    <div class="card-desc"><p>Comanda's billing service gets its CAEs with Arca.Client. In homologación mode it talks to ArcaSim, and its tests walk the real path: CAE granted, a rejection by ARCA with its reason at the register, and ARCA down with the invoice waiting in the queue.</p></div>
    <p class="row-links"><a href="{{ '/en/projects/comanda/' | relative_url }}">Case study</a></p>
  </article>
</div>

## For engineers

- **Its own SOAP layer instead of CoreWCF.** ARCA's services run on six different servers: .NET ASMX, Apache Axis and Axis2, CXF, JAX-WS and Spring-WS, each with its quirks, and a generic framework would smooth them out. WSFEv1 reads and writes through `XmlSerializer`, the serializer ASMX itself uses: it accepts elements in any order, ignores unknown ones and answers in the same format.
- **An engine that reads ARCA's WSDL files.** Beyond WSAA and WSFEv1, no service has a hand-written contract: the engine reads the official WSDL and XSD files, checks the ticket and answers in the service's dialect. A catalog says how each one refuses a ticket and which fixed values it sends; a service's rules are a class that registers itself, and its state goes to a document store, in memory or in PostgreSQL.
- **Rules as data.** Each validation is a rule carrying its code when asking for a CAE and its code when reporting a contingency voucher, where many observe instead of rejecting. Whether it rejects or observes, and its text, come from the manual's table, extracted from the study into a data file.
- **Profiles.** The environment (homologación or production) changes the header texts and the ticket window; the manual version (4.7 or 4.8) follows ArcaSim's clock by default.
- **An event bus between the parts.** The traffic gate, WSAA and WSFEv1 publish what happens: request served or refused, ticket issued, voucher authorized or rejected. The meter and the live log only listen; nobody knows they exist. The admin API is MVC controllers, one per resource.
- **Storage behind ports.** In memory for an application's tests, starting in milliseconds, or PostgreSQL for a team or a CI. The same contract suite runs against both.
- **Keys that survive a restart.** ArcaSim's own certification authority and the ticket-signing key live on disk: an application keeps its ticket for 12 hours and has no reason to lose it when ArcaSim restarts.

Before any code, the whole public ARCA API was studied: WSAA, WSFEv1 and its 496 validations, every other service with its codes, the catalog and the regulations in force, with the official WSDL files and real responses. It is in the repository, in [`docs/arca/`](https://github.com/federicomoroz/arcasim/tree/main/docs/arca) (Spanish).

```bash
docker run -d -p 7080:8080 ghcr.io/federicomoroz/arcasim   # the published image, in memory
docker compose up -d                                       # from the repository, with PostgreSQL
dotnet test
```
