---
title: handoff
description: "Un cliente reclama que su pedido llegó roto. Contestarle bien exige revisar cuatro cosas en un sistema viejo. handoff las revisa y propone la respuesta, con once reglas que le impiden mover plata cuando los datos no alcanzan."
permalink: /es/projects/handoff/
---

<p class="crumbs"><a href="{{ '/es/projects/' | relative_url }}">← Volver a proyectos</a></p>

<section class="hero">
  <h1>handoff <span class="tag active">activo</span></h1>
  <p class="lead">Un cliente escribe: <strong>«me llegó roto»</strong>. Para contestarle hay que mirar el pedido, el envío, cuántas veces reclamó antes y qué anotó el depósito — cuatro consultas a un sistema viejo — y recién ahí decidir si se le manda otro, se le devuelve la plata, se le pide una foto, o el caso lo mira una persona. <strong>handoff hace esas cuatro consultas y propone la decisión.</strong></p>
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
  <p>Una operación de e-commerce recibe reclamos todo el día. El trabajo no es difícil: es repetitivo, está desparramado en cuatro pantallas y equivocarse cuesta plata. Lo que hace falta no es sólo que alguien lo haga más rápido, sino que <strong>no devuelva plata cuando los datos no alcanzan para justificarlo</strong>. Esa segunda mitad es la que ocupa la mayor parte de este proyecto.</p>
</div>

{% include handoff-circuito.html lang="es" %}

## Lo que decide, y con qué

Un reclamo entra con tres datos: el número de pedido, qué pasó —llegó roto, llegó tarde, no llegó— y lo que escribió el cliente. Con eso el agente busca cuatro cosas en el sistema de la empresa:

- **el pedido** — cuánto salió, de qué tipo es, quién lo compró;
- **el envío** — en qué estado está y cuándo fue la última novedad;
- **el historial del cliente** — cuántos reclamos hizo en los últimos 90 días;
- **las notas internas** — lo que alguien del depósito haya anotado.

Y elige una de cuatro salidas: **mandar otro**, **devolver la plata**, **pedirle una foto al cliente**, o **pasárselo a una persona**.

Las dos primeras mueven plata o mercadería y no se pueden deshacer. Las dos últimas no cuestan nada. Esa diferencia es la que ordena todo el resto.

## Las reglas no confían en el modelo

El modelo elige qué hacer. Once reglas revisan esa elección antes de que ocurra, y cualquiera de ellas la frena: el monto es alto, el cliente ya reclamó tres veces, el envío todavía se está moviendo, la última novedad tiene más de tres días, o falta alguno de los cuatro datos.

Esa última importa más de lo que parece. Si el sistema de la empresa no contesta cuando le preguntan por el historial de un cliente, **la ausencia de reclamos previos no se lee como un cliente sin reclamos**. Un dato que no se pudo leer no vale como un dato que dice que no.

{% include handoff-freno.html lang="es" %}

Y las reglas estrictas se aplican sólo a lo irreversible. Exigirle certeza al agente para *preguntarle algo al cliente* lo dejaba con una sola jugada legal cuando dudaba: despertar a una persona. Preguntar es justamente lo que se hace cuando no se está seguro.

## Cómo se sabe que funciona

El agente corre contra 36 situaciones de prueba escritas a mano: 16 que tienen que terminar en una persona y 20 que debería resolver solo. Cada una dice qué pasó, no qué debería contestar — la respuesta correcta vive en un archivo aparte, al que el agente no tiene forma de llegar.

Varias están puestas justo al borde de cada límite: un pedido de 149.900 contra un tope de 150.000, un envío con 71 horas sin novedades contra un límite de 72, un cliente con dos reclamos contra una regla que salta en tres. El borde es donde está el criterio.

<div class="statline">
  <div class="stat"><span class="num">83<small>%</small></span><span class="lbl">de los casos resueltos como correspondía</span></div>
  <div class="stat"><span class="num">19</span><span class="lbl">intentos de mover plata sin respaldo</span></div>
  <div class="stat"><span class="num">0</span><span class="lbl">que llegaron a ejecutarse</span></div>
</div>

Hay un número que el proyecto publica y no favorece: **el modelo por su cuenta acierta el 67%**, y contestar «que lo mire una persona» a todo acierta el 46%. La distancia entre ese 67% y el 83% del sistema completo son las reglas trabajando. Es a propósito que las dos cifras estén publicadas por separado: un agente que sólo acierta porque lo frenan está a un agujero de distancia de equivocarse en producción, y una sola cifra combinada esconde exactamente eso.

## Contra un sistema que contesta mal

El ERP contra el que corre está simulado, y el repositorio lo dice. Está construido para portarse mal de diez maneras concretas, todas sacadas de integraciones reales: contesta XML en un endpoint y JSON en el resto, vence la sesión a mitad de un lote, corta una respuesta al 60% y la devuelve igual como exitosa, escribe «sin dato» de cinco formas distintas, y tiene un código de estado cuyo significado depende de un campo que vive en otra consulta.

Todo eso se resuelve antes de que el modelo vea nada. Lo que tiene una única respuesta correcta —convertir un monto, resolver un código, entender una fecha— lo hace el código; al modelo le llega sólo el criterio. Dejarle el desorden crudo volvería impredecible algo que tiene una sola respuesta, y haría que las pruebas midieran parseo en lugar de decisiones.

Cuando el sistema realmente no contesta, el agente lo dice: el dato queda marcado como faltante y las reglas lo tratan como lo que es, un hueco.

## Cada cambio se vuelve a medir

Las respuestas del modelo están grabadas, y cada grabación se archiva bajo una huella de todo lo que se le mandó. Un cambio que no puede afectar la decisión —renombrar algo, reordenar código— reproduce las grabaciones y no cuesta nada. Un cambio que sí puede —una palabra del texto que se le manda al modelo— invalida las grabaciones y obliga a volver a medir antes de que el cambio se pueda integrar.

Se verificó en las dos direcciones: agregar una sola línea al texto invalidó las 96 grabaciones y frenó la integración; sacarla las devolvió a verde.

<div class="callout">
  <p class="callout-title">Lo que todavía no hace bien</p>
  <p>Tres situaciones de prueba fallan siempre, y dos comparten el mismo error: el envío figura como perdido y el agente le pide al cliente una foto de un paquete que no existe. Es criterio, no cuentas, y ahí el límite es el tamaño del modelo — corre local, en una placa de video común, sin costo de API. La pieza que lo reemplazaría es un parámetro.</p>
</div>
