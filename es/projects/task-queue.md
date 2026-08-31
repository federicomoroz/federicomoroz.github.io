---
title: Task Queue
description: "Cola de tareas distribuida con API en FastAPI, broker Redis y workers escalables horizontalmente."
permalink: /es/projects/task-queue/
---

<!--
  PLANTILLA DE CASE STUDY. Esta pagina es el ejemplo de referencia: copiala
  para cada proyecto nuevo (es/ + en/, mismo id, permalink por idioma).

  Estructura que funciona:
    1. crumbs        -> volver al listado
    2. hero          -> titulo, una linea de que es, chips de stack
    3. callout       -> el gancho: la decision de diseno interesante
    4. statline      -> numeros REALES y medidos. Si no hay, se borra el bloque.
    5. secciones md  -> problema, decisiones, resultado, que aprendi

  REGLA: no inventar metricas. Si no hay numero medido, describir cualitativamente.
  Los TODO marcan lo que falta completar.
-->

<p class="crumbs"><a href="{{ '/es/projects/' | relative_url }}">← Volver a proyectos</a></p>

<section class="hero">
  <h1>Task Queue <span class="tag active">activo</span></h1>
  <p class="lead">Cola de tareas distribuida: API en <strong>FastAPI</strong>, broker <strong>Redis</strong> (LPUSH/BRPOP), persistencia en SQLite y <strong>workers que escalan horizontalmente</strong> sin tocar una línea de código.</p>
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
  <p>El worker no sabe que existe la API y la API no sabe que existen los workers: lo único compartido es la cola en Redis. Eso es lo que permite <code>--scale worker=N</code> en Docker Compose sin cambiar código ni configuración.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">37</span><span class="lbl">tests</span></div>
  <div class="stat"><span class="num">N</span><span class="lbl">workers en paralelo</span></div>
  <div class="stat"><span class="num">TODO</span><span class="lbl">completar con un número real</span></div>
</div>

## El problema

TODO(Federico): qué necesitabas resolver y por qué las alternativas existentes
(Celery, RQ, un cron) no encajaban — o, si fue un ejercicio deliberado para
entender el mecanismo por dentro, decilo así, sin adornarlo.

## Arquitectura

TODO(Federico): las capas y cómo se hablan. Un diagrama en texto o una lista
alcanza; lo que importa es que se entienda quién depende de quién.

- **API (FastAPI)** — recibe la tarea, la encola con `LPUSH`, responde el id.
- **Broker (Redis)** — la cola. Único punto de contacto entre API y workers.
- **Worker** — bloquea en `BRPOP`, ejecuta, persiste el resultado.
- **Persistencia (SQLAlchemy 2.0 + SQLite)** — estado e historial de cada tarea.
- **Scheduler (APScheduler)** — TODO: qué corre agendado.

## Decisiones que importaron

TODO(Federico): 2 o 3 decisiones concretas, cada una con el *por qué*. Ejemplos
del tipo de cosa que va acá: por qué `BRPOP` y no polling; qué pasa si un worker
muere a mitad de una tarea; cómo se evita procesar dos veces.

## Resultado

TODO(Federico): qué quedó funcionando y qué no. Si hay algo que todavía no
resolviste, decilo — un límite conocido suma más credibilidad que una lista de
features sin fisuras.
