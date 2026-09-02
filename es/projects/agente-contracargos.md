---
title: Agente de investigación de contracargos
description: "Agente que investiga contracargos: reúne el caso completo, propone una resolución justificada, se autoevalúa y frena en los casos de riesgo alto. n8n + FastAPI + RAG."
permalink: /es/projects/agente-contracargos/
---

<p class="crumbs"><a href="{{ '/es/projects/' | relative_url }}">← Volver a proyectos</a></p>

<section class="hero">
  <h1>Agente de investigación de contracargos <span class="tag active">activo</span></h1>
  <p class="lead">Ante un contracargo, el agente reúne todo lo que se sabe del caso —la transacción, sus logs, las políticas que aplican, qué se resolvió en casos parecidos, el riesgo del comercio y el historial del cliente—, <strong>propone una resolución justificada y se autoevalúa</strong>. Los casos de riesgo alto frenan y esperan a un analista.</p>
  <div class="chip-row">
    <span class="tag">Python 3.11</span><span class="tag">FastAPI</span><span class="tag">n8n</span>
    <span class="tag">Claude (Haiku + Sonnet)</span><span class="tag">Qdrant</span><span class="tag">RAG</span>
    <span class="tag">Docker</span><span class="tag">pytest</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/ciri-api-aux-sourcecode" target="_blank" rel="noopener">Repo ↗</a>
    <a href="https://ciri-chargeback-agent.onrender.com/panel" target="_blank" rel="noopener">Panel en vivo ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">La decisión que define el sistema</p>
  <p>El panel puede ejecutar el pipeline directo o a través de tu instancia de n8n. Si tu n8n deja de responder a mitad de camino, el modo se apaga y vuelve a directo — <strong>pero nunca por lo bajo</strong>. Un informe idéntico al real haciéndose pasar por una ejecución de la orquestación sería peor que un error.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">1232</span><span class="lbl">tests en CI</span></div>
  <div class="stat"><span class="num">36</span><span class="lbl">pasos del circuito</span></div>
  <div class="stat"><span class="num">32</span><span class="lbl">endpoints</span></div>
  <div class="stat"><span class="num">46</span><span class="lbl">nodos de n8n</span></div>
</div>

## Qué resuelve

Un contracargo es una disputa: el cliente desconoce un cargo y alguien tiene que decidir si
se devuelve la plata. La decisión depende de piezas que viven en lugares distintos —la
transacción y sus logs, el reglamento que aplica, cómo se resolvieron casos parecidos, qué
tan riesgoso es el comercio, qué historial tiene el cliente— y de un criterio que no está
escrito en ninguna tabla.

El agente arma ese expediente completo, propone una resolución **con su justificación**, y
después se pone una nota a sí mismo. Lo que no hace es decidir solo cuando no debe: los
casos de riesgo alto se detienen y quedan esperando a un analista humano.

## Lo que produce

El panel de pruebas deja correr el circuito sobre cualquier transacción del dataset y ver el
resultado sin instalar nada. Los tres escenarios de arriba cubren los dos desenlaces del
enrutador: rechazo automático y revisión humana.

<figure class="shot">
  <img src="{{ '/assets/img/ciri-panel.jpg' | relative_url }}" alt="Panel de pruebas: estado de FastAPI, SQLite, Qdrant y Langfuse, y tres escenarios de prueba con su desenlace esperado." loading="lazy" width="1000" height="1071">
  <figcaption>El panel chequea sus propias dependencias antes de dejarte correr nada: si Qdrant no responde, se ve ahí y no en un error a mitad del pipeline.</figcaption>
</figure>

Cada corrida termina en un informe: la transacción, el perfil del cliente y el del comercio con
sus flags, las políticas que aplican, los precedentes y la resolución propuesta con su
justificación.

<figure class="shot">
  <img src="{{ '/assets/img/ciri-informe.jpg' | relative_url }}" alt="Informe de contracargo: datos de la transacción, nivel de riesgo, perfil del cliente y perfil de riesgo del comercio con flags de anomalía." loading="lazy" width="1600" height="1143">
  <figcaption>Un caso de riesgo alto. El score antifraude, la anomalía geográfica y el comercio suspendido son lo que lleva al circuito a frenar y esperar a un analista.</figcaption>
</figure>

Estos tres son los que viajan en el paquete de entrega, y no están elegidos por su puntaje sino
por cubrir situaciones de política distintas: un bloqueante por criptomonedas, un cliente VIP con
score de fraude, y un SLA extendido fuera de LATAM.

<div class="cards">
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/informe-bloqueante.html' | relative_url }}">Rechazo automático ↗</a></div>
    <div class="card-desc"><p>Una política bloqueante corta el caso antes de que el modelo opine. El código decide; el informe explica cuál fue la regla y por qué no había nada que deliberar.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/informe-riesgo-alto.html' | relative_url }}">Revisión humana ↗</a></div>
    <div class="card-desc"><p>Riesgo alto: el agente reúne el caso y propone, pero no resuelve. Queda esperando a un analista, con todo lo que necesita para decidir en una sola pantalla.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/informe-sla.html' | relative_url }}">Alerta de SLA ↗</a></div>
    <div class="card-desc"><p>Un cargo duplicado fuera de LATAM, donde el plazo de respuesta es otro. El caso más sutil de los tres: la política correcta depende de dónde ocurrió.</p></div>
  </article>
</div>

## El circuito

Cinco diagramas interactivos, autocontenidos: se abren en cualquier navegador, sin conexión
ni instalar nada. Están en orden de lectura — primero **qué** hace el circuito, después
**cómo** se hablan las piezas.

<figure class="shot">
  <a href="{{ '/diagramas/contracargos/n8n_workflow_analysis.html' | relative_url }}"><img src="{{ '/assets/img/ciri-diagrama-circuito.jpg' | relative_url }}" alt="Diagrama del circuito completo: los 36 pasos con su leyenda de tipos de nodo, de la entrada del webhook a la salida del informe." loading="lazy" width="1600" height="1000"></a>
  <figcaption>Los 36 pasos en el orden en que corren, con el tipo de cada nodo: llamada a la API, búsqueda semántica, modelo, bifurcación, espera humana o salida de error. Se genera del propio JSON del workflow, así que no puede quedar desfasado. <strong>Tocá cualquier nodo para abrirlo.</strong></figcaption>
</figure>

<figure class="shot">
  <a href="{{ '/diagramas/contracargos/pipeline_n8n_api.html' | relative_url }}"><img src="{{ '/assets/img/ciri-diagrama-n8n.jpg' | relative_url }}" alt="Diagrama de n8n y la API: las llamadas en orden, con su endpoint y qué toca cada una." loading="lazy" width="1600" height="1000"></a>
  <figcaption>Quién le pide qué a quién. Cada paso del razonamiento es un nodo visible y cada dato que necesita es una llamada con nombre: n8n decide el orden, la API ejecuta y es la única que toca el mundo exterior.</figcaption>
</figure>

<div class="cards">
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/n8n_workflow_analysis.html' | relative_url }}">El circuito completo ↗</a></div>
    <div class="card-desc"><p>Los 36 pasos en orden de ejecución más las 4 salidas de error, con el endpoint de cada uno. Se genera del propio JSON del workflow, así que no puede quedar desfasado del flujo real.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/pipeline_n8n_api.html' | relative_url }}">n8n y la API ↗</a></div>
    <div class="card-desc"><p>Quién le pide qué a quién. Las quince llamadas en orden, qué toca cada una —SQLite, Qdrant, el modelo— y las dos veces que la conversación va al revés. Se lee en un minuto.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/api.html' | relative_url }}">La API por dentro ↗</a></div>
    <div class="card-desc"><p>Los 32 endpoints como un circuito. Además de qué hace cada pieza, explica por qué está separada así: qué principio SOLID sostiene cada corte y qué patrones usa. Es la única que habla de decisiones y no de flujo.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/rag.html' | relative_url }}">El RAG ↗</a></div>
    <div class="card-desc"><p>La cadena entera de recuperación, seguida con un caso real: qué se indexa y qué no, cómo se arma la consulta, por qué las dos colecciones se buscan con criterios opuestos y por dónde el índice se escribe solo.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/contracargos/tests.html' | relative_url }}">Los tests ↗</a></div>
    <div class="card-desc"><p>Qué defecto concreto no puede volver. Las tres capas, la cobertura por paquete y los dieciséis errores reales que hoy tienen un test que los fija. Ninguno de los dieciséis rompía un import.</p></div>
  </article>
</div>

## Cómo está armado

- **Orquestación en n8n** — 46 nodos, 40 ejecutables. Es la pieza que coordina; los nodos
  llaman a la API, no reimplementan nada. Hay un segundo workflow con un formulario como vía
  de entrada alternativa, y un tercero que recibe los fallos de los otros dos y los registra.
- **API en FastAPI** — 32 endpoints, separados por capas: dominio, análisis, RAG, LLM,
  reportes, observabilidad. Todo lo que hace el workflow está disponible como endpoint.
- **RAG sobre Qdrant** — dos colecciones, políticas y precedentes, que se buscan con
  criterios opuestos a propósito.
- **Dos modelos con roles distintos** — Haiku evalúa las políticas, Sonnet sintetiza y
  después juzga el resultado.
- **Guardrails, rate limiting y trazas** — cada corrida deja registro de qué consultó, qué
  recuperó y cuánto costó.

## Lo que más me gusta de este proyecto

No es la arquitectura: es **cómo trata sus propios números**.

El repo muestra un puntaje de 9.1/10 del juez, y a continuación explica en detalle que ese
número salió de corridas de desarrollo que hoy no son reproducibles sin saldo de API, que
los tres informes que viajan en el paquete promedian 8.67, y que las dos corridas
posteriores —hechas con modelos gratuitos— dan 8.97 y 8.4 pero **no deberían mover el
badge**, porque cada modelo se puntúa a sí mismo con su propia vara y los casos compartidos
entre ambas corridas se llevan hasta ±1.8 entre sí.

Después deja el instrumento para volver a medir: un script que corre la muestra, escribe el
detalle caso por caso y reporta el costo.

Un informe generado por el sistema siempre declara cómo se produjo —si corrió de verdad o si
es un resultado guardado, con qué modelo, y cuánto se puede desviar la nota—, y eso viaja en
la cabecera HTTP, en el cuerpo y en un warning del log.

Es más fácil publicar el 9.1 solo. Documentar por qué no hay que creerle del todo es la parte
que cuesta, y es la que distingue a alguien que mide de alguien que reporta.

## Probarlo

El [panel en vivo](https://ciri-chargeback-agent.onrender.com/panel) corre el pipeline
completo sin instalar nada ni cargar ninguna clave: arranca en modo demo, que cae a un modelo
con free tier y **ejecuta de verdad** en vez de recitar un resultado guardado.

Está en el free tier de Render y duerme tras 15 minutos sin uso: la primera llamada puede
tardar cerca de un minuto en despertarlo.
