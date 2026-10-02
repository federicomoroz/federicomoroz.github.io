---
title: Order Outbox Service
description: "Dos microservicios en Java y Spring Boot que garantizan que ningún evento se pierda cuando el broker de mensajería se cae."
permalink: /es/projects/order-outbox-service/
---

<p class="crumbs"><a href="{{ '/es/tools/' | relative_url }}">{{ site.data.i18n[page.lang].services.back }}</a></p>

<section class="hero">
  <h1>Order Outbox Service <span class="tag active">activo</span></h1>
  <p class="lead">Dos microservicios en Java y Spring Boot. Cuando el broker de mensajería se cae, <strong>los eventos esperan en la base y no se pierde ninguno</strong>. Cuando el broker vuelve, el sistema se recupera solo.</p>
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
  <p class="callout-title">El problema en una línea</p>
  <p>Guardás el pedido en la base y publicás el evento en la cola. Son dos operaciones separadas, y no hay forma de hacerlas atómicas: si la segunda falla, el pedido existe y nadie se entera. Es el problema del <em>dual write</em>, y aparece en casi cualquier sistema de microservicios.</p>
</div>

<figure class="shot">
  <img src="{{ '/assets/img/order-outbox-circuito.gif' | relative_url }}" alt="Animación en cinco pasos: el pedido y su evento se escriben en un solo commit de Postgres; Kafka se cae y la API sigue respondiendo 201; el relay reintenta con intervalos crecientes de 2 a 64 segundos; Kafka vuelve y el evento se publica solo; el consumidor deduplica y queda exactamente una notificación." loading="lazy" width="1200" height="750">
  <figcaption>El circuito completo, con una caída real del broker. Los tiempos que se ven (el backoff de 2 a 64 segundos, la recuperación a las 06:22:20) salen de una corrida medida contra el sistema funcionando.</figcaption>
</figure>

<div class="statline">
  <div class="stat"><span class="num">86</span><span class="lbl">tests en CI</span></div>
  <div class="stat"><span class="num">10</span><span class="lbl">reglas de arquitectura ejecutables</span></div>
  <div class="stat"><span class="num">0</span><span class="lbl">eventos perdidos con el broker caído</span></div>
</div>

## Cómo se resuelve

El patrón es el **transactional outbox**, y se arma en tres piezas:

1. **Un solo commit.** El pedido y su evento se escriben en la misma transacción de Postgres, en dos tablas. Kafka no participa del request HTTP. Si el commit sale, existen los dos. Si falla, no existe ninguno.
2. **Un relay aparte.** Un proceso agendado lee los eventos pendientes y los publica. Si el broker no responde, reintenta más tarde, espaciando cada vez más para no castigar a un servicio que ya está en problemas.
3. **Un consumidor idempotente.** Con entrega *at-least-once*, los reintentos van a duplicar mensajes. Por eso el servicio que consume tiene una tabla de deduplicación con clave única, y el segundo mensaje idéntico se descarta antes de tener efecto.

Sin esa tabla, cada reintento le llegaría al cliente como una notificación repetida.

## Lo que se ve en la animación

Con el broker apagado a propósito, la API sigue aceptando pedidos y respondiendo `201`, porque nunca necesitó a Kafka para eso. El evento queda esperando en su tabla mientras el relay reintenta a los 2, 4, 8, 16, 32 y 64 segundos. Al agotar los reintentos rápidos, la fila queda marcada como degradada y **el relay la sigue tomando indefinidamente**.

Cuando el broker vuelve, el evento se publica solo, sin scripts de reparación ni reprocesos a mano. Esa corrida terminó con 15 notificaciones para 15 pedidos, sin duplicados ni pérdidas.

## El servicio no arranca con plazos desincronizados

En la verificación manual aparecieron filas marcadas como fallidas cuyo evento **sí** había llegado. El código esperaba 5 segundos por la confirmación, mientras el cliente de Kafka seguía reintentando por debajo durante 120 segundos, su valor por defecto, que no estaba configurado.

Además de alinear los dos valores, el servicio ahora **se niega a arrancar** si esos plazos quedan desincronizados, y muestra un mensaje que explica por qué. Así el desajuste no puede volver a entrar por descuido.

## Reglas de arquitectura en ArchUnit

El dominio y la capa de aplicación no importan nada de Spring, JPA ni Hibernate. Lo hacen cumplir diez reglas de **ArchUnit** (cinco por servicio), que rompen el build si el código las cruza.

## El panel

El repositorio incluye un panel en React que muestra el circuito en vivo: los pedidos entrando, su evento pasando de pendiente a publicado, y la notificación apareciendo en la base del otro servicio. Se levanta todo con un comando (`docker compose up`), sin configurar nada.

<figure class="shot">
  <img src="{{ '/assets/img/order-outbox-panel.jpg' | relative_url }}" alt="Panel del sistema en tres columnas: las órdenes entrando, sus eventos en el outbox marcados como publicados con el tiempo que tardó cada uno, y las notificaciones generadas en la base del otro servicio. Arriba, contadores de órdenes, eventos por estado y latencia del relay." loading="lazy" width="1600" height="1000">
  <figcaption>El mismo identificador aparece en las tres columnas: es el evento cruzando de un servicio al otro. Las filas con "6 intentos" y "+176,45 s" son las que quedaron esperando durante una caída de Kafka y se publicaron solas cuando volvió.</figcaption>
</figure>

## Fuera de alcance

El sistema no tiene autenticación ni envío real de notificaciones. Tampoco hay deploy público: el stack son dos bases de datos, Kafka y dos servicios, y no entra cómodo en un plan gratuito. El alcance se limitó a la garantía de entrega.
