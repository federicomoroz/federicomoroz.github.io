---
title: Order Outbox Service
description: "Two Java and Spring Boot microservices that guarantee no event is lost when the message broker goes down."
permalink: /en/projects/order-outbox-service/
---

<p class="crumbs"><a href="{{ '/en/projects/' | relative_url }}">← Back to projects</a></p>

<section class="hero">
  <h1>Order Outbox Service <span class="tag active">active</span></h1>
  <p class="lead">Two Java and Spring Boot microservices. When the message broker goes down, <strong>events wait in the database and none are lost</strong>. When the broker returns, the system recovers on its own.</p>
  <div class="chip-row">
    <span class="tag">Java 21</span><span class="tag">Spring Boot</span><span class="tag">Kafka</span>
    <span class="tag">PostgreSQL</span><span class="tag">Testcontainers</span><span class="tag">ArchUnit</span>
    <span class="tag">React</span><span class="tag">Docker</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/order-outbox-service" target="_blank" rel="noopener">Repo ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">The problem in one line</p>
  <p>You save the order to the database and publish the event to the queue. Two separate operations, and there is no way to make them atomic: if the second one fails, the order exists and nobody finds out. It is called the <em>dual write</em> problem, and it shows up in almost any microservice system.</p>
</div>

<figure class="shot">
  <img src="{{ '/assets/img/order-outbox-circuito.gif' | relative_url }}" alt="Five-step animation: the order and its event are written in a single Postgres commit; Kafka goes down and the API still returns 201; the relay retries with growing intervals from 2 to 64 seconds; Kafka comes back and the event publishes itself; the consumer dedupes and exactly one notification remains." loading="lazy" width="1200" height="750">
  <figcaption>The full circuit, with a real broker outage. The timings shown (the 2-to-64-second backoff, the recovery at 06:22:20) come from a run measured against the live system.</figcaption>
</figure>

<div class="statline">
  <div class="stat"><span class="num">86</span><span class="lbl">tests in CI</span></div>
  <div class="stat"><span class="num">10</span><span class="lbl">executable architecture rules</span></div>
  <div class="stat"><span class="num">0</span><span class="lbl">events lost with the broker down</span></div>
</div>

## How it is solved

The pattern is the **transactional outbox**, built from three parts:

1. **A single commit.** The order and its event are written in the same Postgres transaction, across two tables. Kafka takes no part in the HTTP request. If the commit succeeds, both exist. If it fails, neither does.
2. **A separate relay.** A scheduled process reads pending events and publishes them. If the broker does not answer, it retries later, spacing attempts further apart so it does not hammer a service that is already struggling.
3. **An idempotent consumer.** With *at-least-once* delivery, retries will duplicate messages. So the consuming service keeps a deduplication table with a unique key, and a second identical message is discarded before it has any effect.

Without that table, every retry would reach the customer as a repeated notification.

## What the animation shows

With the broker deliberately switched off, the API keeps accepting orders and returning `201`, because it never needed Kafka for that. The event waits in its table while the relay retries at 2, 4, 8, 16, 32 and 64 seconds. Once the fast retries are exhausted, the row is flagged as degraded and **the relay keeps picking it up indefinitely**.

When the broker returns, the event publishes itself, with no repair scripts or manual reprocessing. That run ended with 15 notifications for 15 orders, with no duplicates and no losses.

## The service will not start with mismatched deadlines

Manual verification turned up rows marked as failed whose event **had** in fact been delivered. The code waited 5 seconds for confirmation, while the Kafka client kept retrying underneath for 120 seconds, its default value, which had not been configured.

Besides aligning the two values, the service now **refuses to start** if those deadlines drift apart, and prints a message explaining why. That keeps the mismatch from coming back by accident.

## Architecture rules in ArchUnit

The domain and application layers import nothing from Spring, JPA or Hibernate. Ten **ArchUnit** rules (five per service) enforce this and break the build if the code crosses them.

## The dashboard

The repository includes a React panel showing the circuit live: orders coming in, their event moving from pending to published, and the notification appearing in the other service's database. The whole thing comes up with one command (`docker compose up`), with nothing to configure.

<figure class="shot">
  <img src="{{ '/assets/img/order-outbox-panel.jpg' | relative_url }}" alt="Three-column system dashboard: orders coming in, their outbox events marked as published with the time each one took, and the notifications created in the other service's database. Along the top, counters for orders, events by status and relay latency." loading="lazy" width="1600" height="1000">
  <figcaption>The same identifier shows up in all three columns: that is the event crossing from one service to the other. The rows reading "6 intentos" and "+176,45 s" are the ones that waited out a Kafka outage and published themselves once it came back.</figcaption>
</figure>

## Out of scope

The system has no authentication and no real notification delivery. There is no public deployment either: the stack is two databases, Kafka and two services, and it does not fit comfortably in a free tier. The scope was limited to the delivery guarantee.
