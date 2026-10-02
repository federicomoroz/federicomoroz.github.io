---
title: Task Queue
description: "Cola de tareas en FastAPI y Redis: la API acepta el trabajo y responde al instante, y los workers lo ejecutan en segundo plano, con reintentos, y escalan con un solo flag."
permalink: /es/projects/task-queue/
---

<p class="crumbs"><a href="{{ '/es/tools/' | relative_url }}">{{ site.data.i18n[page.lang].services.back }}</a></p>

<section class="hero">
  <h1>Task Queue <span class="tag active">activo</span></h1>
  <p class="lead">Cola de tareas distribuida: API en <strong>FastAPI</strong>, broker <strong>Redis</strong> (LPUSH/BRPOP), persistencia en SQLite y <strong>workers que escalan horizontalmente</strong> sin cambios de código.</p>
  <div class="chip-row">
    <span class="tag">Python</span><span class="tag">FastAPI</span><span class="tag">Redis</span>
    <span class="tag">SQLAlchemy 2.0</span><span class="tag">Docker</span><span class="tag">APScheduler</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/task-queue" target="_blank" rel="noopener">Repo ↗</a>
    <a href="https://task-queue-tpdz.onrender.com" target="_blank" rel="noopener">Demo en vivo ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">La decisión de diseño</p>
  <p>Los workers no le hablan a la API. Cada uno se bloquea en <code>BRPOP</code> sobre las mismas listas de Redis, y Redis le entrega cada id a un solo worker. Por eso <code>--scale worker=N</code> en Docker Compose suma workers sin cambiar código ni configuración.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">37</span><span class="lbl">tests, sin Docker</span></div>
  <div class="stat"><span class="num">3</span><span class="lbl">colas en Redis</span></div>
  <div class="stat"><span class="num">5</span><span class="lbl">estados por tarea</span></div>
</div>

## El problema

Una API sincrónica tiene que terminar el trabajo antes de responder. Si la tarea tarda, como
mandar un mail, llamar a una API de terceros lenta o generar un reporte, el cliente queda
bloqueado y los timeouts se acumulan cuando sube la carga.

La cola separa aceptar el trabajo de ejecutarlo. `POST /tasks` valida el pedido, lo guarda y
responde `202` con el id. Un worker en otro proceso lo ejecuta después, y el cliente consulta
el estado con `GET /tasks/{id}`. Hay dos tipos de tarea: `echo`, que loguea un mensaje y espera
un segundo, y `http_request`, que hace una llamada HTTP saliente real.

## Arquitectura

En local son tres contenedores en Docker Compose, que arrancan en orden de dependencia con
health checks.

- **API (FastAPI):** corre un pipeline de dos pasos. `ValidateStep` rechaza los tipos desconocidos con `422` antes de escribir nada. `EnqueueStep` inserta la fila en SQLite como `pending`, hace `LPUSH` del id y emite el evento `TASK_ENQUEUED`.
- **Broker (Redis 7):** una lista por cola (`tq:queue:high`, `tq:queue:default`, `tq:queue:low`). Por Redis viaja solo el id; el payload queda en la base.
- **Worker (×N):** se bloquea en `BRPOP`, carga la tarea, la marca `processing`, busca el handler por tipo en un registro y guarda el resultado.
- **Persistencia (SQLAlchemy 2.0 + SQLite):** estado, contador de reintentos, último error y timestamps de cada tarea. La API y los workers montan el mismo volumen con el archivo de la base.
- **Scheduler (APScheduler):** cada hora borra las tareas completadas hace más de 24 horas. El plazo se configura con `PURGE_COMPLETED_AFTER_HOURS`.

```
POST /tasks -> pending -> processing -> completed
                                     -> retrying -> vuelve a la cola -> processing
                                     -> failed      (sin reintentos disponibles)
```

Los efectos secundarios pasan por un `EventManager` sincrónico. El worker emite
`TASK_COMPLETED` y `TASK_FAILED`, y `LogListener` se suscribe a los tres eventos. Para sumar
una alerta alcanza con otra clase suscripta al arranque, sin tocar el worker.

## Decisiones que importaron

**`BRPOP` en lugar de consultar la base en un loop.** El worker queda bloqueado en Redis hasta
que llega un id o vence el timeout de 5 segundos, y no hace consultas en vacío. `LPUSH` mete por
la izquierda y `BRPOP` saca por la derecha, así que cada cola es FIFO. Cuando se le pasan varias
listas, Redis las revisa en el orden de `WORKER_QUEUES` y toma de la primera que tenga algo. La
prioridad entre colas sale de ese orden.

**Primero la base, después Redis.** La fila se escribe antes del `LPUSH`. Si Redis no responde
al encolar, la API contesta igual y la tarea queda `pending` en SQLite con el registro completo.
`GET /queues` informa profundidad 0 en lugar de devolver un error.

**Reintentos con tope por tarea.** Cada tarea trae su `max_retries`, entre 0 y 10, con 3 por
defecto. Si el handler lanza una excepción y quedan intentos, la tarea pasa a `retrying`, suma
uno al contador y su id vuelve al final de su cola. Al agotarlos queda `failed` con el último
error guardado. `HttpHandler` lanza ante cualquier respuesta fuera de 2xx, así que un endpoint
caído entra por el mismo camino. Con `max_retries: 0` la tarea falla en el primer error.

**Tests sin infraestructura.** Los 37 tests corren sin Docker. `fakeredis` reemplaza a Redis, y
el SQLite en memoria usa `StaticPool` para que todas las sesiones vean las tablas que crea el
fixture. El código importa módulos (`import app.core.database as _db_mod`) en lugar de
funciones sueltas, y así el fixture parchea `SessionLocal` y `get_redis` en un solo lugar.

## Resultado

`docker compose up --build` levanta Redis, la API y un worker. Con `--scale worker=3` tres
workers compiten por las mismas colas, y en los logs se ven los ids repartidos entre
contenedores. La interfaz en `/` tiene cuatro pestañas (dashboard, encolar, tareas y colas),
está hecha en JavaScript sin build, trae cuatro escenarios de demo y se refresca cada 2
segundos.

La demo publicada corre en el plan gratuito de Render, en un solo contenedor. La API levanta
el loop de `BRPOP` en un hilo contra un Redis en Upstash, y un poller cada 3 segundos procesa
las tareas que quedaron `pending` en la base. La instancia se duerme después de 15 minutos sin
uso, la primera carga puede tardar unos 30 segundos y la base de la demo es efímera.

Si un worker muere a mitad de una tarea, el id ya salió de Redis y la
fila queda en `processing`; no hay un proceso que la detecte y la vuelva a encolar. Los
reintentos son inmediatos, sin espera creciente entre intentos.
