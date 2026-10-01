---
title: Mega Training System
description: "Generador de planes de entrenamiento con la API de Claude, usado por una cadena importante de gimnasios en Argentina y por usuarios particulares. Arquitectura de plugins y control de costo."
permalink: /es/projects/mega-training-system/
---

<p class="crumbs"><a href="{{ '/es/projects/' | relative_url }}">← Volver a proyectos</a></p>

<section class="hero">
  <h1>Mega Training System <span class="tag active">activo</span></h1>
  <p class="lead">Generador de planes de entrenamiento sobre la <strong>API de Claude</strong>. Nació como herramienta para un instructor de indoor cycling y hoy lo usan <strong>una cadena importante de gimnasios en Argentina y usuarios particulares</strong>.</p>
  <div class="chip-row">
    <span class="tag">Python</span><span class="tag">Flask</span><span class="tag">Claude</span>
    <span class="tag">SSE</span><span class="tag">PostgreSQL</span><span class="tag">Docker</span><span class="tag">pytest</span>
  </div>
  <p class="row-links">
    <span class="muted">Repo privado</span>
  </p>
</section>

<div class="callout">
  <p class="callout-title">La decisión de diseño</p>
  <p>Las reglas de arquitectura se verifican con tests. Alrededor de 670 leen el <strong>AST</strong> del código y fallan si una capa importa a otra que no le corresponde, si una ruta habla directo con la base o si un servicio se salta su puerto. Un refactor que rompe la separación de capas no llega a mergear.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">1.671</span><span class="lbl">tests en CI</span></div>
  <div class="stat"><span class="num">87%</span><span class="lbl">cobertura</span></div>
  <div class="stat"><span class="num">~670</span><span class="lbl">tests de arquitectura</span></div>
</div>

## El problema

Armar una clase de indoor cycling en el formato de la cadena es trabajo repetitivo con reglas
duras: cinco fases, 3360 segundos exactos, cadencia entre 60 y 110 RPM, BPM igual al doble
de la cadencia. Un LLM arma bien el borrador, pero al ponerlo en el medio aparecen dos
problemas que antes no existían: **el modelo devuelve estructuras que no siempre respetan
las reglas**, y **cada generación cuesta plata**.

El sistema está construido alrededor de esos dos problemas.

Después llegó un tercero. Cuando la cadena lo adoptó hizo falta una segunda disciplina,
musculación, con metodología, catálogo y formato de salida propios. De ahí sale la
arquitectura de plugins: sumar musculación no tenía que obligar a reescribir indoor cycling.

## El musicalizador

Cada clase lleva **la música encima de la estructura**. Para eso hay un editor de audio en el
navegador, un mini DAW con timeline por fases, tracks que se arrastran sobre cada bloque,
crossfades y un render final a un solo archivo.

<figure class="shot">
  <img src="{{ '/assets/img/mts-musicalizador.jpg' | relative_url }}" alt="Editor de audio: timeline con las fases de la clase, la pista de musicalización con su forma de onda, los controles de fade y la librería de tracks con BPM e intensidad." loading="lazy" width="1600" height="1000">
  <figcaption>Una clase terminada: los 56 minutos con su estructura arriba y la musicalización abajo, cada bloque con su track, su forma de onda y su crossfade. El porcentaje sobre cada uno es qué tan bien encaja el track con la fase; la librería de abajo lleva BPM e intensidad, que es lo que decide dónde puede entrar.</figcaption>
</figure>

## El plan de entrenamiento

La otra disciplina genera planes de musculación. Corre sobre el mismo core que indoor
cycling, con otro agent y otro formato de salida.

<figure class="shot">
  <img src="{{ '/assets/img/mts-plan.jpg' | relative_url }}" alt="Plan de hipertrofia de doce semanas: tres mesociclos, cuatro días por semana y los ejercicios con series, repeticiones, descanso y RPE." loading="lazy" width="1600" height="1150">
  <figcaption>Doce semanas en tres mesociclos (acumulación, intensificación, pico y deload), con cada ejercicio y sus series, repeticiones, descanso y RPE objetivo.</figcaption>
</figure>

En la captura se ve algo que los diagramas no muestran: **la restricción del socio llega
hasta el ejercicio**. Una lesión declarada en el perfil baja al plan y decide qué movimientos
se evitan y con qué se reemplazan, ejercicio por ejercicio.

## Arquitectura

Cuatro capas, con el registro de disciplinas cruzándolas por arriba:

- **Presentación (HTTP / SSE):** blueprints por dominio, hook de auth y rate limiting.
- **Aplicación:** orquestador de generación, idempotencia y store de resultados. El
  orquestador no importa Flask, así que se puede ejercitar sin levantar el servidor.
- **Servicios:** la lógica de cada disciplina. El servicio de musculación recibe un puerto
  de dos métodos y no ve el resto del repositorio.
- **Infraestructura:** cliente de Claude detrás del circuit breaker, repositorios,
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

**Las llamadas al LLM pasan por un circuit breaker.** Tiene los tres estados (`CLOSED` /
`OPEN` / `HALF_OPEN`). En `HALF_OPEN`, una bandera de sonda en vuelo serializa el reintento:
cuando el circuito se abre, sale un solo pedido a probar si el servicio volvió, en lugar de
N simultáneos.

**Cuatro mecanismos independientes bajan el costo.** El system prompt va como bloque
cacheado, así las lecturas salen una fracción del precio. El trabajo que no necesita
respuesta inmediata va por la Batch API. Una `Idempotency-Key` con el hash del perfil evita
volver a generar lo mismo dentro de la ventana. Y el modelo se elige según la complejidad
del pedido, en vez de usar siempre el más caro.

**El modelo responde siempre con una llamada a herramienta.** La generación usa
`tool_choice="any"`, así que la salida llega estructurada y no hay texto libre que parsear.
Las invariantes del dominio viven en validadores Pydantic v2. Cuando el modelo devuelve
duraciones que no cierran, una rutina de reparación las ajusta y la generación se aprovecha
igual.

**Una disciplina nueva no toca el core.** El registro descubre los plugins con `pkgutil`.
Sumar una disciplina es un `plugin.py` y su agent, sin abrir `app.py`.

**Streaming con SSE y threading, sin asyncio.** Flask es sincrónico. La generación devuelve
un `task_id`, el cliente se engancha a un stream y cada tarea tiene su `threading.Event`, así
que no hace falta polling.

<!--
  TODO(Federico): dos cosas que solo podés contar vos y que le agregarían mucho a esta
  página. No las escribo yo porque serían inventadas.

  1. Cómo llegó al cliente: si fue freelance, un favor que escaló, o parte de un trabajo.
     Eso decide si esto se cuenta como experiencia laboral o como proyecto.
  2. Qué se rompió en producción y cómo lo arreglaste. Un incidente real con su causa raíz
     vale más que toda la lista de patterns de arriba.
-->
