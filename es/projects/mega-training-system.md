---
title: Mega Training System
description: "Generador de planes de entrenamiento sobre la API de Claude, en producción en un cliente. Arquitectura de plugins y control de costo por diseño."
permalink: /es/projects/mega-training-system/
---

<p class="crumbs"><a href="{{ '/es/projects/' | relative_url }}">← Volver a proyectos</a></p>

<section class="hero">
  <h1>Mega Training System <span class="tag active">activo</span></h1>
  <p class="lead">Generador de planes de entrenamiento sobre la <strong>API de Claude</strong>. Nació como herramienta para un instructor de indoor cycling y hoy lo usa <strong>un cliente</strong> en su operación diaria.</p>
  <div class="chip-row">
    <span class="tag">Python</span><span class="tag">Flask</span><span class="tag">Claude</span>
    <span class="tag">SSE</span><span class="tag">PostgreSQL</span><span class="tag">Docker</span><span class="tag">pytest</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/MegaTrainingSystem" target="_blank" rel="noopener">Repo ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">La decisión de diseño</p>
  <p>La arquitectura no se sostiene por convención: se verifica. Alrededor de 670 tests leen el <strong>AST</strong> del código y fallan si una capa importa a otra que no le corresponde, si una ruta habla directo con la base o si un servicio se salta su puerto. Un refactor que rompe la separación de capas no llega a mergear.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">1.671</span><span class="lbl">tests en CI</span></div>
  <div class="stat"><span class="num">87%</span><span class="lbl">cobertura</span></div>
  <div class="stat"><span class="num">~670</span><span class="lbl">tests de arquitectura</span></div>
</div>

## El problema

Armar una clase de indoor cycling en el formato del cliente es trabajo repetitivo con reglas
duras: cinco fases, 3360 segundos exactos, cadencia entre 60 y 110 RPM, BPM igual al doble
de la cadencia. Un LLM resuelve bien el borrador, pero al meterlo en el medio aparecen dos
problemas que antes no existían: **el modelo devuelve estructuras que no siempre respetan
las reglas**, y **cada generación cuesta plata**.

El sistema está construido alrededor de esos dos problemas, no alrededor del prompt.

Después llegó un tercero: cuando el cliente lo adoptó, hizo falta una segunda disciplina
—musculación— con su propia metodología, su propio catálogo y su propio formato de salida.
De ahí sale la arquitectura de plugins: la segunda disciplina no podía costar reescribir la
primera.

## El musicalizador

Una clase no es solo la estructura: es la estructura **con la música encima**. El editor de
audio es un mini DAW en el navegador — timeline por fases, tracks arrastrables sobre cada
bloque, crossfades y render final a un solo archivo.

<figure class="shot">
  <img src="{{ '/assets/img/mts-musicalizador.jpg' | relative_url }}" alt="Editor de audio: timeline con las fases de la clase, la pista de musicalización con su forma de onda, los controles de fade y la librería de tracks con BPM e intensidad." loading="lazy" width="1600" height="1000">
  <figcaption>Los 56 minutos de una clase con su estructura arriba y la musicalización abajo. Cada track de la librería lleva su BPM y su intensidad, que es lo que decide en qué fase puede entrar.</figcaption>
</figure>

## Arquitectura

Cuatro capas, con el registro de disciplinas cruzándolas por arriba:

- **Presentación (HTTP / SSE)** — blueprints por dominio, hook de auth y rate limiting.
- **Aplicación** — orquestador de generación, idempotencia y store de resultados. El
  orquestador no importa Flask: se puede ejercitar sin levantar el servidor.
- **Servicios** — la lógica de cada disciplina. El servicio de musculación recibe un puerto
  de dos métodos, no el repositorio entero.
- **Infraestructura** — cliente de Claude detrás del circuit breaker, repositorios,
  filesystem y base de conocimiento.

Los adaptadores entran por puertos (`ClassStoragePort`, `KnowledgeBasePort`, `UserRepoPort`),
así que los servicios se testean sin filesystem ni base de datos.

## Los diagramas

La arquitectura completa está documentada como un solo HTML autocontenido con nueve
diagramas generados: la visión general, los módulos, los modelos de dominio, el flujo de
SSE y threading, el schema de SQLite, el sistema de disciplinas y las rutas de la API.

<div class="cards">
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/mega-training-system/arquitectura.html' | relative_url }}">Arquitectura completa ↗</a></div>
    <div class="card-desc"><p>Siete secciones, de la vista de pájaro al schema de tablas: los puertos secundarios de cada disciplina, las invariantes de dominio, cómo se resuelve el streaming con threading en un Flask sincrónico y qué rutas expone la API.</p></div>
  </article>
</div>

## Decisiones que importaron

**El LLM se trata como una dependencia que falla.** Las llamadas pasan por un circuit
breaker con los tres estados (`CLOSED` / `OPEN` / `HALF_OPEN`). El detalle que importa está
en `HALF_OPEN`: una bandera de sonda en vuelo serializa el reintento, para que al abrirse el
circuito no salgan N pedidos simultáneos a probar si el servicio volvió.

**El costo es una dimensión de diseño, no un efecto secundario.** Cuatro mecanismos
independientes atacan lo mismo: el system prompt va como bloque cacheado, así las lecturas
salen una fracción del precio; el trabajo que no necesita respuesta inmediata va por la
Batch API; una `Idempotency-Key` con el hash del perfil evita volver a generar lo mismo
dentro de la ventana; y el modelo se elige según la complejidad del pedido en vez de usar
siempre el más caro.

**La salida estructurada no se pide, se fuerza.** La generación usa `tool_choice="any"`: el
modelo devuelve una herramienta, nunca texto libre que después haya que parsear. Encima de
eso, las invariantes del dominio viven en validadores Pydantic v2, y cuando el modelo
devuelve duraciones que no cierran hay una rutina de reparación que las ajusta en vez de
tirar la generación entera a la basura.

**Una disciplina nueva no toca el core.** El registro descubre los plugins con `pkgutil`;
sumar una disciplina es un `plugin.py` y su agent, sin abrir `app.py`.

**SSE y threading, no asyncio.** Flask es sincrónico. La generación devuelve un `task_id` y
el cliente se engancha a un stream, con un `threading.Event` por tarea en vez de polling.

<!--
  TODO(Federico): dos cosas que solo podés contar vos y que le agregarían mucho a esta
  página. No las escribo yo porque serían inventadas.

  1. Cómo llegó al cliente: si fue freelance, un favor que escaló, o parte de un trabajo.
     Eso decide si esto se cuenta como experiencia laboral o como proyecto.
  2. Qué se rompió en producción y cómo lo arreglaste. Un incidente real con su causa raíz
     vale más que toda la lista de patterns de arriba.
-->
