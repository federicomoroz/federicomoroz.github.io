---
title: Shipping Quote
description: "Cotizador de envíos con arquitectura hexagonal que consulta a tres transportistas en paralelo y devuelve la traza de cada request, salto por salto."
permalink: /es/projects/shipping-quote/
---

<p class="crumbs"><a href="{{ '/es/projects/' | relative_url }}">← Volver a proyectos</a></p>

<section class="hero">
  <h1>Shipping Quote <span class="tag active">activo</span></h1>
  <p class="lead">Cotizador de envíos armado como un <strong>circuito hexagonal</strong>. Cada request queda trazado hop por hop, desde que entra por HTTP hasta que los tres adaptadores de transportista devuelven cada uno su cotización.</p>
  <div class="chip-row">
    <span class="tag">Python</span><span class="tag">FastAPI</span><span class="tag">SQLAlchemy</span>
    <span class="tag">Alembic</span><span class="tag">httpx</span><span class="tag">pytest</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/shipping-quote" target="_blank" rel="noopener">Repo ↗</a>
    <a href="https://shipping-quote.onrender.com" target="_blank" rel="noopener">Demo en vivo ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">La decisión de diseño</p>
  <p>Cada request arma su propia traza ordenada (entrada, adaptador, puerto, caso de uso, dominio, puerto, adaptador, salida) y la devuelve en la respuesta. El diagrama del hexágono sale de esa traza, así que se puede comparar con lo que el código hizo en ese request.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">31</span><span class="lbl">tests en CI</span></div>
  <div class="stat"><span class="num">3</span><span class="lbl">adaptadores de carrier</span></div>
  <div class="stat"><span class="num">~15</span><span class="lbl">líneas para sumar un cuarto</span></div>
</div>

## Qué hace

Hay un solo caso de uso, cotizar un paquete, y corre contra tres adaptadores en el mismo
request. **En la versión publicada los tres transportistas son stubs**: un sub-app de FastAPI
aparte que imita sus APIs, conectado por `ASGITransport` sin abrir un socket. El mismo
dominio produce tres cotizaciones distintas sin saber que hay tres transportistas. La
persistencia y el manejo de errores son reales.

<figure class="shot">
  <img src="{{ '/assets/img/shipping-quote-circuito.gif' | relative_url }}" alt="Animación del circuito hexagonal: un request entra por HTTP, atraviesa el adaptador primario, el puerto, el caso de uso y el dominio, sale por el puerto secundario hacia los tres adaptadores de transportista y vuelve con las cotizaciones." loading="lazy" width="1168" height="715">
  <figcaption>El circuito que recorre un request real, hop por hop. La secuencia está tomada de la traza que devuelve la respuesta.</figcaption>
</figure>

## El circuito

```
entrada -> adaptador -> puerto -> caso de uso -> dominio -> puerto -> adaptador -> salida
 (POST)   quote_       Shipping   QuoteShipping  pipeline   Carrier   *Adapter   API del
          controller   QuotePort  UseCase        steps      Port                 carrier
```

El `main.py` es el composition root: arma todo en el lifespan. El dominio (`Package`, zonas,
`FeePolicy`, `Tracer`) no importa nada de afuera.

**La traza vuelve dentro de la respuesta.** Un paquete de 2,5 kg a CP 1425 devuelve
dieciocho pasos con el tiempo de cada uno: entrada, adaptador, puerto, los pasos de dominio,
los tres adaptadores de carrier y salida. En el mismo JSON aparece la regla de peso
volumétrico aplicada: 2,5 kg reales contra 4,8 kg efectivos.

## Decisiones de diseño

**La plata va en `Decimal`, nunca en `float`.** La comisión se calcula en `Decimal` y se
redondea con `ROUND_HALF_UP` explícito. El `round()` nativo de Python usa banker's rounding,
y con montos de dinero eso da resultados inesperados. El test
`test_apply_service_fee_rounds_half_up_not_banker` fija esa diferencia. El redondeo
explícito entró como pago de deuda técnica.

**Una sola clase para los tres transportistas.** `HttpCarrierAdapter` se configura por
composición, con un endpoint y dos funciones de mapeo, y el try/except/timeout está escrito
una sola vez. Sumar un cuarto transportista es un archivo de unas quince líneas.

**Un transportista falla a propósito.** El mock de Correo Argentino devuelve error cerca del
15% de las veces. El caso de uso corre los tres con `asyncio.gather`, y cuando uno falla
responde igual con las otras dos cotizaciones.

**La traza pasa por un `Tracer`.** Una traza tiene un solo consumidor y un orden estricto,
así que el `Tracer` se pasa por referencia a través de las capas. Un bus de eventos pub/sub,
con un solo consumidor, sólo agregaría indirección.

**Un puerto primario para una sola implementación.** Según YAGNI, `ShippingQuotePort` sobra.
Está igual, porque sin ese puerto el lado de entrada del hexágono queda implícito y el
circuito ya no se puede trazar de punta a punta. El docstring del ABC lo aclara para que no
se lea como un descuido.

**El peso efectivo es `max(peso real, largo × ancho × alto / 5000)`**, la fórmula estándar de
peso volumétrico.

## Fuera de alcance

No tiene autenticación ni rate limiting, y el transportista no se elige: siempre se cotizan
los tres.

Las migraciones con Alembic están deliberadamente separadas del `create_all()` del arranque:
engancharlas al lifespan habría hecho que los tests migraran la base real en vez de la de
memoria, porque los tests parchean el engine y no la URL.
