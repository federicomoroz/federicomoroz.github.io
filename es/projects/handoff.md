---
title: handoff
description: "Un cliente reclama que su pedido llegó roto. handoff hace las cuatro consultas que hacen falta para contestarle y decide en dos segundos: resuelve el caso, o se lo pasa a una persona con todo ya reunido."
permalink: /es/projects/handoff/
---

<p class="crumbs"><a href="{{ '/es/projects/' | relative_url }}">← Volver a proyectos</a></p>

<section class="hero">
  <h1>handoff <span class="tag active">activo</span></h1>
  <p class="lead">Un cliente escribe: <strong>«me llegó roto»</strong>. Para contestarle hay que mirar el pedido, el envío, cuántas veces reclamó antes y qué anotó el depósito — cuatro consultas a un sistema viejo — y recién ahí decidir. <strong>handoff hace esas cuatro consultas y decide, en dos segundos.</strong> Le manda otro, le devuelve la plata, le pide una foto, o se lo pasa a una persona con las cuatro consultas ya hechas y la razón por la que se frenó.</p>
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
  <p>Una operación de e-commerce recibe reclamos todo el día. El trabajo no es difícil: es repetitivo, está desparramado en cuatro pantallas, y cada caso tarda lo que tarda abrirlas. handoff los toma por HTTP y devuelve la decisión con los hechos que la justifican. <strong>En ocho de cada diez la decisión es la que correspondía</strong> — incluida la de no decidir: cuando los datos no alcanzan, el caso llega a una persona ya armado, no en blanco.</p>
</div>

{% include handoff-circuito.html lang="es" %}

## Un servicio que se llama y contesta

Corre como servicio HTTP. Le entra un reclamo por `POST /api/triage` con tres datos —el número de pedido, qué pasó (llegó roto, llegó tarde, no llegó) y lo que escribió el cliente— y devuelve la decisión, los hechos con los que la tomó, y la traza de todo lo que consultó.

Con esos tres datos busca cuatro cosas en el sistema de la empresa:

- **el pedido** — cuánto salió, de qué tipo es, quién lo compró;
- **el envío** — en qué estado está y cuándo fue la última novedad;
- **el historial del cliente** — cuántos reclamos hizo en los últimos 90 días;
- **las notas internas** — lo que alguien del depósito haya anotado.

Y elige una de cuatro salidas: **mandar otro**, **devolver la plata**, **pedirle una foto al cliente**, o **pasárselo a una persona**.

Las dos primeras mueven plata o mercadería y no se pueden deshacer. Las dos últimas no cuestan nada. Esa diferencia es la que ordena todo el resto.

## Lo que resuelve, y en cuánto

<div class="statline">
  <div class="stat"><span class="num">83<small>%</small></span><span class="lbl">de los casos, la decisión que correspondía</span></div>
  <div class="stat"><span class="num">2<small>s</small></span><span class="lbl">en hacer las cuatro consultas y decidir</span></div>
  <div class="stat"><span class="num">0</span><span class="lbl">devoluciones sin respaldo suficiente</span></div>
</div>

Los dos segundos son el percentil 95: diecinueve de cada veinte reclamos salen resueltos más rápido que eso, con el modelo corriendo local en una placa de video común.

El cero es el que hace que los otros dos sirvan. **Nunca devolvió plata en un caso que necesitaba una persona.** No porque el modelo no lo haya intentado —lo intentó diecinueve veces sobre noventa y seis— sino porque hay once reglas entre la propuesta y la ejecución, y cualquiera de ellas la frena.

{% include handoff-freno.html lang="es" %}

## Las reglas no confían en el modelo

El modelo elige qué hacer. Once reglas revisan esa elección antes de que ocurra: el monto es alto, el cliente ya reclamó tres veces, el envío todavía se está moviendo, la última novedad tiene más de tres días, o falta alguno de los cuatro datos.

Esa última importa más de lo que parece. Si el sistema de la empresa no contesta cuando le preguntan por el historial de un cliente, **la ausencia de reclamos previos no se lee como un cliente sin reclamos**. Un dato que no se pudo leer no vale como un dato que dice que no.

Y las reglas estrictas se aplican sólo a lo irreversible. Exigirle certeza al agente para *preguntarle algo al cliente* lo dejaba con una sola jugada legal cuando dudaba: despertar a una persona. Preguntar es justamente lo que se hace cuando no se está seguro.

## Contra un sistema que contesta mal

El ERP contra el que corre está simulado, y está construido para portarse mal de diez maneras concretas, todas sacadas de integraciones reales: contesta XML en un endpoint y JSON en el resto, vence la sesión a mitad de un lote, corta una respuesta al 60% y la devuelve igual como exitosa, escribe «sin dato» de cinco formas distintas, y tiene un código de estado cuyo significado depende de un campo que vive en otra consulta.

handoff resuelve las diez antes de que el modelo vea nada. Lo que tiene una única respuesta correcta —convertir un monto, resolver un código, entender una fecha— lo hace el código; al modelo le llega sólo el criterio. Cuando el sistema realmente no contesta, el dato queda marcado como faltante y las reglas lo tratan como lo que es, un hueco.

## Cómo se sostiene

El agente corre contra 36 situaciones escritas a mano: 16 que tienen que terminar en una persona y 20 que debería resolver solo. Cada una dice qué pasó, no qué debería contestar — la respuesta correcta vive en un archivo aparte, al que el agente no tiene forma de llegar. Varias están puestas justo al borde de cada límite: un pedido de 149.900 contra un tope de 150.000, un envío con 71 horas sin novedades contra un límite de 72, un cliente con dos reclamos contra una regla que salta en tres. El borde es donde está el criterio.

Las respuestas del modelo están grabadas, y cada grabación se archiva bajo una huella de todo lo que se le mandó. Un cambio que no puede afectar la decisión —renombrar algo, reordenar código— reproduce las grabaciones y no cuesta nada. Un cambio que sí puede —una palabra del texto que se le manda al modelo— invalida las grabaciones y obliga a volver a medir antes de que el cambio se pueda integrar. Se verificó en las dos direcciones: agregar una sola línea al texto invalidó las 96 grabaciones y frenó la integración; sacarla las devolvió a verde.

Las dos cifras que importan van publicadas por separado: **83% el sistema completo, 67% el modelo antes de las reglas.** La distancia entre las dos es lo que aportan las reglas, y una sola cifra combinada la escondería.
