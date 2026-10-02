---
title: handoff
description: "Un cliente reclama que su pedido llegó roto. handoff hace las cuatro consultas que hacen falta para contestarle y decide en dos segundos: resuelve el caso, o se lo pasa a una persona con todo ya reunido."
permalink: /es/projects/handoff/
---

<p class="crumbs"><a href="{{ '/es/tools/' | relative_url }}">{{ site.data.i18n[page.lang].services.back }}</a></p>

<section class="hero">
  <h1>handoff <span class="tag active">activo</span></h1>
  <p class="lead">Un cliente escribe: <strong>«me llegó roto»</strong>. Para contestarle hay que mirar el pedido, el envío, cuántas veces reclamó antes y qué anotó el depósito (cuatro consultas a un sistema viejo), y recién ahí decidir. <strong>handoff hace esas cuatro consultas y decide, en dos segundos.</strong> Le manda otro, le devuelve la plata, le pide una foto, o se lo pasa a una persona con las cuatro consultas ya hechas y la razón por la que se frenó.</p>
  <div class="chip-row">
    <span class="tag">TypeScript</span><span class="tag">Node</span><span class="tag">Hono</span>
    <span class="tag">Zod</span><span class="tag">Ollama</span><span class="tag">vitest</span>
    <span class="tag">GitHub Actions</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/handoff" target="_blank" rel="noopener">Repo ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">Para qué sirve</p>
  <p>Una operación de e-commerce recibe reclamos todo el día. Es trabajo repetitivo: cada reclamo se resuelve mirando cuatro pantallas y tarda lo que tarda abrirlas. handoff toma los reclamos por HTTP y devuelve la decisión con los hechos que la justifican. <strong>En ocho de cada diez la decisión es la que correspondía</strong>, contando los casos en que lo correcto era no decidir. Cuando los datos no alcanzan, el caso le llega a una persona con todo ya reunido.</p>
</div>

{% include handoff-circuito.html lang="es" %}

## Cómo se usa

Corre como servicio HTTP. Le entra un reclamo por `POST /api/triage` con tres datos: el número de pedido, qué pasó (llegó roto, llegó tarde, no llegó) y lo que escribió el cliente. Devuelve la decisión, los hechos con los que la tomó y la traza de todo lo que consultó.

Con esos tres datos busca cuatro cosas en el sistema de la empresa:

- **El pedido**: cuánto salió, de qué tipo es, quién lo compró.
- **El envío**: en qué estado está y cuándo fue la última novedad.
- **El historial del cliente**: cuántos reclamos hizo en los últimos 90 días.
- **Las notas internas**: lo que alguien del depósito haya anotado.

Después elige una de cuatro salidas: **mandar otro**, **devolver la plata**, **pedirle una foto al cliente** o **pasárselo a una persona**.

Las dos primeras mueven plata o mercadería y no se pueden deshacer. Las dos últimas no cuestan nada. Las reglas de más abajo se apoyan en esa diferencia.

## Resultados

<div class="statline">
  <div class="stat"><span class="num">83<small>%</small></span><span class="lbl">de los casos, la decisión que correspondía</span></div>
  <div class="stat"><span class="num">2<small>s</small></span><span class="lbl">en hacer las cuatro consultas y decidir</span></div>
  <div class="stat"><span class="num">0</span><span class="lbl">devoluciones sin respaldo suficiente</span></div>
</div>

Los dos segundos son el percentil 95: diecinueve de cada veinte reclamos salen resueltos más rápido que eso, con el modelo corriendo local en una placa de video común.

El cero significa que **nunca se devolvió plata en un caso que necesitaba una persona.** Entre la propuesta del modelo y la ejecución hay once reglas, y cualquiera de ellas alcanza para frenarla. Las reglas frenaron las diecinueve veces, sobre noventa y seis, en que el modelo propuso devolver plata en uno de esos casos.

{% include handoff-freno.html lang="es" %}

## Las reglas que revisan al modelo

El modelo elige qué hacer. Once reglas revisan esa elección antes de que se ejecute. Miran si el monto es alto, si el cliente ya reclamó tres veces, si el envío todavía se está moviendo, si la última novedad tiene más de tres días o si falta alguno de los cuatro datos.

Si el sistema de la empresa no contesta cuando le preguntan por el historial de un cliente, handoff marca ese dato como faltante y la regla frena. **Un historial que no se pudo leer cuenta como dato faltante**, y nunca como un cliente sin reclamos previos.

Las reglas estrictas se aplican sólo a lo irreversible. Para *preguntarle algo al cliente* el agente no necesita certeza, así que cuando duda puede pedir una foto sin tener que pasarle el caso a una persona.

## Un ERP que contesta mal

El ERP contra el que corre está simulado, y está construido para portarse mal de diez maneras concretas, todas sacadas de integraciones reales: contesta XML en un endpoint y JSON en el resto, vence la sesión a mitad de un lote, corta una respuesta al 60% y la devuelve igual como exitosa, escribe «sin dato» de cinco formas distintas, y tiene un código de estado cuyo significado depende de un campo que vive en otra consulta.

handoff resuelve las diez antes de que el modelo vea nada. El código se encarga de lo que tiene una única respuesta correcta, como convertir un monto, resolver un código o entender una fecha. Al modelo le llega sólo lo que pide criterio. Cuando el sistema realmente no contesta, el dato queda marcado como faltante y las reglas lo tratan como un hueco.

## Cómo se mide

El agente corre contra 36 situaciones escritas a mano: 16 que tienen que terminar en una persona y 20 que debería resolver solo. Cada una describe qué pasó. La respuesta correcta está en un archivo aparte, al que el agente no tiene forma de llegar. Varias están puestas justo al borde de un límite: un pedido de 149.900 contra un tope de 150.000, un envío con 71 horas sin novedades contra un límite de 72, un cliente con dos reclamos contra una regla que salta en tres.

Las respuestas del modelo están grabadas, y cada grabación se archiva bajo una huella de todo lo que se le mandó. Un cambio que no puede afectar la decisión (renombrar algo, reordenar código) reproduce las grabaciones y no cuesta nada. Un cambio que sí puede afectarla, aunque sea una palabra del texto que se le manda al modelo, invalida las grabaciones y obliga a volver a medir antes de integrarlo. Se verificó en las dos direcciones. Agregar una sola línea al texto invalidó las 96 grabaciones y frenó la integración, y sacarla las devolvió a verde.

Las dos cifras van publicadas por separado: **83% el sistema completo, 67% el modelo antes de las reglas.** La diferencia entre las dos es lo que aportan las reglas.
