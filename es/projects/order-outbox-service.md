---
title: Order Outbox Service
description: "Dos microservicios en Java y Spring Boot que garantizan que ningún evento se pierda cuando el broker de mensajería se cae."
permalink: /es/projects/order-outbox-service/
---

<p class="crumbs"><a href="{{ '/es/projects/' | relative_url }}">← Volver a proyectos</a></p>

<section class="hero">
  <h1>Order Outbox Service <span class="tag active">activo</span></h1>
  <p class="lead">Dos microservicios en Java y Spring Boot que resuelven un problema concreto: <strong>qué pasa con tus eventos cuando el broker de mensajería se cae</strong>. La respuesta acá es que no se pierde ninguno, y que el sistema se recupera solo cuando el broker vuelve.</p>
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
  <p>Guardás el pedido en la base y publicás el evento en la cola. Son dos operaciones separadas, y no hay forma de hacerlas atómicas: si la segunda falla, el pedido existe y nadie se entera. Se llama <em>dual write</em>, y aparece en casi cualquier sistema de microservicios.</p>
</div>

<figure class="shot">
  <img src="{{ '/assets/img/order-outbox-circuito.gif' | relative_url }}" alt="Animación en cinco pasos: el pedido y su evento se escriben en un solo commit de Postgres; Kafka se cae y la API sigue respondiendo 201; el relay reintenta con intervalos crecientes de 2 a 64 segundos; Kafka vuelve y el evento se publica solo; el consumidor deduplica y queda exactamente una notificación." loading="lazy" width="1200" height="750">
  <figcaption>El circuito completo bajo falla real. Los tiempos que se ven —el backoff de 2 a 64 segundos, la recuperación a las 06:22:20— salen de una corrida medida contra el sistema andando, no de una simulación.</figcaption>
</figure>

<div class="statline">
  <div class="stat"><span class="num">86</span><span class="lbl">tests en CI</span></div>
  <div class="stat"><span class="num">10</span><span class="lbl">reglas de arquitectura ejecutables</span></div>
  <div class="stat"><span class="num">0</span><span class="lbl">eventos perdidos con el broker caído</span></div>
</div>

## Cómo se resuelve

El patrón se llama **transactional outbox** y tiene tres piezas:

1. **Un solo commit.** El pedido y su evento se escriben en la misma transacción de Postgres, en dos tablas. Kafka no participa del request HTTP. Si el commit sale, ambos existen; si falla, ninguno.
2. **Un relay aparte.** Un proceso agendado lee los eventos pendientes y los publica. Si el broker no responde, reintenta más tarde, espaciando cada vez más para no castigar a un servicio que ya está en problemas.
3. **Un consumidor idempotente.** Los reintentos van a duplicar mensajes —es inevitable con entrega *at-least-once*— así que del otro lado hay una tabla de deduplicación con clave única. El segundo mensaje idéntico se descarta antes de tener efecto.

La tercera pieza es la que más se olvida. Sin ella, cada reintento es una notificación repetida al cliente.

## Lo que se ve en la animación

Con el broker apagado a propósito, la API sigue aceptando pedidos y respondiendo `201`, porque nunca necesitó a Kafka para eso. El evento queda esperando en su tabla mientras el relay reintenta a los 2, 4, 8, 16, 32 y 64 segundos. Al agotar los reintentos rápidos la fila queda marcada como degradada —pero **no abandonada**: el relay la sigue tomando indefinidamente.

Cuando el broker vuelve, el evento se publica solo. Sin scripts de reparación, sin reprocesar a mano, sin un ticket. El resultado final de esa corrida fueron 15 notificaciones para 15 pedidos: ningún duplicado y ninguna pérdida.

## Un bug real, y cómo se cerró

Durante la verificación manual apareció algo que no estaba previsto: filas marcadas como fallidas cuyo evento **sí** había llegado. La causa eran dos plazos que se contradecían — el código esperaba 5 segundos por la confirmación, mientras el cliente de Kafka seguía reintentando 120 segundos por debajo, un valor por defecto que nadie había configurado.

El arreglo no fue sólo corregir los números. El servicio ahora **se niega a arrancar** si esos dos plazos quedan desincronizados, con un mensaje que explica por qué. El bug no se puede reintroducir por descuido.

## Las reglas de arquitectura son tests

El dominio y la capa de aplicación no importan nada de Spring, JPA ni Hibernate. Eso no queda como acuerdo de equipo ni como comentario en el README: son diez reglas de **ArchUnit** —cinco por servicio— que revientan el build si alguien las cruza. La misma idea que un linter, aplicada a la forma del sistema.

## El panel

El repositorio incluye un panel en React que muestra el circuito en vivo: los pedidos entrando, su evento pasando de pendiente a publicado, y la notificación apareciendo en la base del otro servicio. Se levanta todo con un comando (`docker compose up`), sin configurar nada.

<figure class="shot">
  <img src="{{ '/assets/img/order-outbox-panel.jpg' | relative_url }}" alt="Panel del sistema en tres columnas: las órdenes entrando, sus eventos en el outbox marcados como publicados con el tiempo que tardó cada uno, y las notificaciones generadas en la base del otro servicio. Arriba, contadores de órdenes, eventos por estado y latencia del relay." loading="lazy" width="1600" height="1000">
  <figcaption>El mismo identificador aparece en las tres columnas: es el evento cruzando de un servicio al otro. Las filas con "6 intentos" y "+176,45 s" son las que quedaron esperando durante una caída de Kafka y se publicaron solas cuando volvió.</figcaption>
</figure>

## Fuera de alcance, a propósito

No hay autenticación, no hay envío real de notificaciones y no hay deploy público —el stack son dos bases de datos, Kafka y dos servicios, que no entran cómodos en un plan gratuito—. El objetivo era la garantía de entrega, no un producto terminado.
