---
title: Shipping Quote
description: "Cotizador de envíos construido para mostrar un circuito de arquitectura hexagonal funcionando, con la traza de cada request visible hop por hop."
permalink: /es/projects/shipping-quote/
---

<p class="crumbs"><a href="{{ '/es/projects/' | relative_url }}">← Volver a proyectos</a></p>

<section class="hero">
  <h1>Shipping Quote <span class="tag active">activo</span></h1>
  <p class="lead">Cotizador de envíos que existe para mostrar un <strong>circuito hexagonal funcionando</strong>, no dibujado: cada request queda trazado hop por hop, desde que entra por HTTP hasta que tres adaptadores de transportista devuelven su propia cotización.</p>
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
  <p>La arquitectura hexagonal casi siempre se explica con un diagrama y se afirma que el código lo respeta. Acá se puede mirar: cada request emite su propia traza ordenada —entrada, adaptador, puerto, caso de uso, dominio, puerto, adaptador, salida— y esa traza vuelve en la respuesta. El diagrama no es documentación al lado del código: es la salida del código.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">31</span><span class="lbl">tests en CI</span></div>
  <div class="stat"><span class="num">3</span><span class="lbl">adaptadores de carrier</span></div>
  <div class="stat"><span class="num">~15</span><span class="lbl">líneas para sumar un cuarto</span></div>
</div>

## Por qué existe

Es un artefacto didáctico y conviene decirlo de entrada: no es un producto, es un caso de
uso —cotizar un paquete— corriendo contra tres adaptadores en el mismo request. Los tres
transportistas son **simulaciones**, no integraciones reales: un sub-app de FastAPI aparte
que imita las APIs, conectado por `ASGITransport` sin abrir un socket. El valor no está en
haber integrado a Correo Argentino: está en que el mismo dominio produzca tres resultados
distintos sin enterarse de que existen tres.

Eso permite algo que un ejemplo de juguete no da: el circuito completo, con persistencia
real, manejo de errores real y una traza que se puede leer.

## El circuito

```
entrada -> adaptador -> puerto -> caso de uso -> dominio -> puerto -> adaptador -> salida
 (POST)   quote_       Shipping   QuoteShipping  pipeline   Carrier   *Adapter   API del
          controller   QuotePort  UseCase        steps      Port                 carrier
```

El `main.py` es el composition root: arma todo en el lifespan. El dominio (`Package`, zonas,
`FeePolicy`, `Tracer`) no importa nada de afuera.

Esto no hay que creerlo: **la traza vuelve dentro de la respuesta**. Un paquete de 2,5 kg a
CP 1425 devuelve dieciocho pasos — entrada, adaptador, puerto, los pasos de dominio, los tres
adaptadores de carrier y la salida— con el tiempo de cada uno. En el mismo JSON se ve la
regla de peso volumétrico decidiendo: 2,5 kg reales contra 4,8 kg efectivos.

## Decisiones que importaron

**Plata en `Decimal`, no en `float`.** El cálculo de la comisión opera en `Decimal` y
redondea con `ROUND_HALF_UP` explícito, porque el `round()` nativo de Python usa banker's
rounding y para dinero da resultados que sorprenden. Hay un test que fija exactamente esa
diferencia: `test_apply_service_fee_rounds_half_up_not_banker`. Fue deuda técnica saldada,
no algo que estuvo bien desde el principio.

**Los tres transportistas son una clase, no tres.** `HttpCarrierAdapter` se configura por
composición —endpoint más dos funciones de mapeo— en vez de repetir el mismo
try/except/timeout tres veces. Por eso sumar un cuarto transportista es un archivo de unas
quince líneas y no una clase entera.

**Un transportista falla a propósito.** El mock de Correo Argentino devuelve error cerca del
15% de las veces. El caso de uso corre los tres con `asyncio.gather` y responde con dos
cotizaciones de tres sin romperse. Es la diferencia entre demostrar que se llama a tres
servicios y demostrar qué pasa cuando uno se cae.

**Traza con `Tracer`, no con un bus de eventos.** Una traza tiene un solo consumidor y un
orden estricto, así que se pasa por referencia a través de las capas. Un pub/sub habría sido
usar el patrón porque sí: acá no aporta nada y agrega indirección.

**Un puerto primario para una sola implementación.** `ShippingQuotePort` es over-engineering
según YAGNI, y está a propósito: el proyecto existe para mostrar el circuito completo, y sin
ese puerto el lado de entrada del hexágono no se ve. Está anotado en el docstring del ABC
para que nadie lo lea como un descuido.

**El peso efectivo es `max(peso real, largo × ancho × alto / 5000)`**, la fórmula estándar de
peso volumétrico. El dominio tiene una regla de negocio de verdad, no un `if` de adorno.

## Fuera de alcance, a propósito

Sin autenticación, sin rate limiting y sin elegir transportista a mano: siempre se cotizan
los tres. El objetivo es la arquitectura, no un producto completo.

Las migraciones con Alembic están deliberadamente separadas del `create_all()` del arranque:
engancharlas al lifespan habría hecho que los tests migraran la base real en vez de la de
memoria, porque los tests parchean el engine y no la URL.
