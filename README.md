# Federico Moroz

**Backend Developer · API Integrations · Distributed Systems**

Buenos Aires, Argentina &nbsp;·&nbsp; Open to remote

---

## Background

I build backend systems that are correct by design: layered architecture, explicit contracts between components, and tests that verify behavior rather than implementation.                                                                                                                          My recent work spans distributed task queues, API gateways with circuit breakers, multi-channel notification engines, and an AI-powered platform using the Claude API with real-time SSE streaming — all deployed and   tested.                                                  
I also have hands-on experience integrating external APIs at scale: one system I built processes ~2,100 transactions/month and cut per-transaction time from ~10 minutes to ~5 seconds.
If your system needs to keep running when something breaks, I'm the person you bring in.

---

## Projects

### [Task Queue](https://github.com/federicomoroz/task-queue) &nbsp;·&nbsp; [Live demo](https://task-queue-tpdz.onrender.com)
Distributed task queue with a FastAPI API server, Redis broker (LPUSH/BRPOP), SQLite persistence, and horizontally scalable workers. Multi-container Docker architecture — workers scale with `--scale worker=N` without touching any code.

`Python` `FastAPI` `Redis` `SQLAlchemy 2.0` `Docker` `APScheduler` · **37 tests**

---

### [Rate Guardian](https://github.com/federicomoroz/rate-guardian)
API gateway with sliding-window rate limiting (Redis sorted sets), Redis-backed circuit breaker, transparent HTTP proxy, and a real-time terminal dashboard. Event-driven logging via pub/sub bus — the gateway never imports the logger directly. Full Docker Compose setup with PostgreSQL + Redis.

`Python` `FastAPI` `Redis` `PostgreSQL` `Docker` `httpx` · **202 tests**

---

### [Notify Router](https://github.com/federicomoroz/notify-router)
Multi-channel notification routing engine. A single inbound event is evaluated against routing rules and dispatched to any combination of channels — email (SendGrid), Telegram Bot, Slack, or generic webhook. Pipeline + Strategy + EventManager architecture. Full browser SPA to manage channels, rules, and events without touching the terminal.

`Python` `FastAPI` `SQLite` `SendGrid` `httpx` `APScheduler`

---

### [Webhook Logger](https://github.com/federicomoroz/webhook-logger) &nbsp;·&nbsp; [Live demo](https://webhook-logger-9paz.onrender.com)
Backend service that receives, stores, and exposes webhook events from any source. Includes a built-in HTTP tester to fire outbound requests from the browser. MVC + Repository, strict layer separation.

`Python` `FastAPI` `SQLAlchemy` `SQLite` `Pydantic v2`

---

### [Dollar Tracker](https://github.com/federicomoroz/dollar-tracker)
Scheduled service that fetches unofficial USD/ARS exchange rates, persists history, fires email alerts on threshold breaches, and sends periodic reports. Fully configurable via env vars.

`Python` `FastAPI` `SQLAlchemy` `APScheduler` `SendGrid`

---

### [envcheck](https://github.com/federicomoroz/envcheck)
Zero-dependency CLI tool that validates `.env` against `.env.example`. Catches missing and empty variables before they reach production. Exit code 1 makes it a drop-in CI pre-deploy gate.

`Python` `CLI` · **29 tests** · No external dependencies

---

### [RPG Turn-Based Battler](https://github.com/federicomoroz/RPG-Turn-Based-Battler)
Turn-based combat engine for a 2D RPG. ScriptableObject data layer with runtime cloning (Flyweight), 4-phase skill execution skeleton (Template Method), pluggable movement strategies (Strategy), generic object pool auto-discovered via reflection, and a damage modifier pipeline (Chain of Responsibility).

`Unity` `C#`

---

## Tech

**Languages:** Python · JavaScript · C# · SQL · PHP

**Backend:** FastAPI · Django · Flask · Node.js · Laravel · SQLAlchemy · Pydantic

**Infrastructure:** Redis · PostgreSQL · SQLite · Docker · APScheduler

**Integrations:** REST APIs · Webhooks · SendGrid · Telegram Bot API · n8n · Airtable · BigQuery

---

📫 fedegfs@gmail.com &nbsp;·&nbsp; [LinkedIn](https://linkedin.com/in/federico-moroz-1760a2241/)
