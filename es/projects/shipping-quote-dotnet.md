---
title: Shipping Quote — .NET
description: "El mismo cotizador de envíos, portado a ASP.NET Core sobre los mismos puertos y casos de uso. El port encontró dos bugs que el original nunca había mostrado."
permalink: /es/projects/shipping-quote-dotnet/
---

<p class="crumbs"><a href="{{ '/es/projects/' | relative_url }}">← Volver a proyectos</a></p>

<section class="hero">
  <h1>Shipping Quote — .NET <span class="tag active">activo</span></h1>
  <p class="lead">El mismo cotizador de envíos con <strong>arquitectura hexagonal</strong> que existe en Python, portado a <strong>ASP.NET Core</strong>. El port <strong>encontró dos bugs</strong> que el original nunca había mostrado.</p>
  <div class="chip-row">
    <span class="tag">C#</span><span class="tag">.NET 8</span><span class="tag">ASP.NET Core</span>
    <span class="tag">EF Core</span><span class="tag">MySQL</span><span class="tag">Testcontainers</span>
    <span class="tag">xUnit</span><span class="tag">Docker</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/shipping-quote-dotnet" target="_blank" rel="noopener">Repo ↗</a>
    <a href="{{ '/es/projects/shipping-quote/' | relative_url }}">La versión en Python →</a>
    <a href="{{ '/es/projects/nexo/' | relative_url }}">El proyecto .NET más completo →</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">La decisión de diseño</p>
  <p>Al portar el sistema a otro stack se ve qué partes eran arquitectura y cuáles eran costumbre. Los puertos, el pipeline y la política de precio pasaron intactos al nuevo lenguaje. Lo que hubo que rehacer fueron decisiones que en Python parecían neutrales y en .NET no lo eran.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">63</span><span class="lbl">tests en CI</span></div>
  <div class="stat"><span class="num">306<small>ms</small></span><span class="lbl">3 carriers de 300ms c/u</span></div>
  <div class="stat"><span class="num">2</span><span class="lbl">bugs que encontró el port</span></div>
</div>

## Concurrencia medida con un test

Los tres transportistas se consultan en paralelo con `Task.WhenAll`, así que el request
tarda lo que tarda el más lento. Es fácil romperlo sin darse cuenta: un `await` dentro de
un `foreach` compila, pasa los tests y triplica en silencio la latencia del servicio.

Por eso hay un test que lo **mide**:

```
3 transportistas × 300ms   →  306 ms      en fila serían 900
latencias 50 / 150 / 400   →  399 ms      la suma sería 600
```

El test falla si pasa de 700ms. Lo que controla es el tiempo de reloj del request.

Para que eso se cumpla en todo el servicio:

- **`async`/`await` de punta a punta.** Ni un `.Result` ni un `.Wait()` en todo el repo:
  nada bloquea un hilo del pool esperando I/O.
- **`Task.Delay`, nunca `Thread.Sleep`.** La espera no ocupa un hilo, y con mil requests
  concurrentes eso decide si el pool alcanza o se agota.
- **`CancellationToken` enhebrado hasta el adaptador.** Si el cliente corta, se cortan las
  llamadas en vuelo. Hay un test con un transportista de 30 segundos que corta en 67ms.
- **`CreateLinkedTokenSource` para el timeout del contrato.** Así el timeout no pisa la
  cancelación del request entrante y se respetan las dos.
- **Cada request con su propio `TraceRecorder`.** Un test lanza 40 requests concurrentes y
  verifica que ninguna traza se mezcle con otra. Si hubiera estado mutable compartido, ese
  test lo detectaría.

## Primer bug: SQLite y las escrituras concurrentes

El port arrancó con SQLite, igual que el original. El test de veinte cotizaciones
concurrentes falló:

```
SqliteException : SQLite Error 5: 'database is locked'
```

SQLite **serializa las escrituras**, y el servicio se trababa en el único punto donde
escribe. El primer arreglo fue un `busy_timeout`: la segunda escritura espera en vez de
fallar, lo que sólo cambia el error por latencia.

La base pasó a **MySQL**:

| Con SQLite | Con MySQL |
|---|---|
| plata guardada como `TEXT` | `decimal(12,2)` nativo |
| fecha como entero de ticks | `datetime(6)`, microsegundos |
| `busy_timeout` para no fallar | escrituras concurrentes reales |
| `EnsureCreated` | migraciones de EF Core |
| — | `EnableRetryOnFailure` ante deadlocks |

Sin `datetime(6)`, MySQL trunca a segundos y dos cotizaciones del mismo segundo ya no se
pueden ordenar entre sí.

## Segundo bug: sólo aparece contra el motor real

La primera versión guardaba el historial en SQLite, y los tests de integración corrían
contra ese motor real en lugar de un doble en memoria. La primera corrida tiró:

```
SQLite does not support expressions of type 'DateTimeOffset' in ORDER BY clauses
```

El endpoint de historial ordenaba por fecha, y SQLite no puede ordenar un `DateTimeOffset`
del lado del servidor. El error es de **runtime**: el código compilaba y se habría caído en
producción con el primer request al historial. Desde entonces el adaptador guarda la fecha
en UTC y la convierte a `DateTimeOffset` al leer, así el dominio sigue hablando en instantes
con offset y la base solo ve un `datetime`.

Un doble en memoria lo habría tapado. Los dos bugs de esta página aparecieron corriendo
contra un motor real, y por eso los tests de integración de hoy levantan un **MySQL 8.0
real** en un contenedor efímero que vive lo que dura la corrida.

## La regla de negocio no sabe que existe HTTP

Que un bulto de más de 30 kg no se cotice es una regla de negocio. Que eso se comunique
como un `422` es una decisión de transporte. Por eso viven en lugares distintos: el
dominio tira su excepción y un **middleware** la traduce a HTTP.

```csharp
catch (Exception exc) when (exc is PackageTooHeavyException or InvalidPostalCodeException)
```

El controller no tiene ningún `try/catch`, y un controller nuevo hereda el mapeo sin
escribir nada. El patrón es Chain of Responsibility, el mismo que usa por dentro el pipeline
de ASP.NET Core: cada middleware decide si maneja el request o se lo pasa al siguiente.

## El hexágono, igual que en Python

La arquitectura hexagonal pasó entera al nuevo lenguaje. Son cuatro proyectos con las
dependencias apuntando siempre hacia adentro, y el compilador hace cumplir los límites: el
dominio no puede importar ASP.NET porque no lo referencia.

```
ShippingQuote.Domain           sin dependencias
      ▲
ShippingQuote.Application      puertos y casos de uso
      ▲
ShippingQuote.Infrastructure   adaptadores — HTTP, EF Core
      ▲
ShippingQuote.Api              controllers, middleware, DI
```

El caso de uso recibe un `IEnumerable<ICarrierPort>` y no sabe cuántos transportistas hay,
quiénes son, ni que hablan HTTP. Sumar un cuarto es una entrada en el catálogo y una línea
en el composition root.

Los tres transportistas son tres **instancias** de la misma clase. Cada uno aporta sólo
datos: su endpoint y dos funciones de traducción. El timeout, el manejo de errores y la
traza están escritos una sola vez. Con composición en vez de herencia se evitan tres clases
casi idénticas.

## Alcance

Los tres transportistas son **simulados**, igual que en la versión Python. Acá se montan
como un `HttpMessageHandler` propio: el `HttpClient` hace un POST real, con serialización,
status codes y deserialización reales, pero la llamada nunca sale a la red. El adaptador
que se testea es el mismo binario que correría en producción, y lo único que habría que
cambiar es ese último eslabón.

El mismo dominio produce tres resultados distintos sin saber que hay tres transportistas, y
si uno se cae, la respuesta sale igual.
