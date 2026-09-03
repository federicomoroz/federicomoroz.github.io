---
title: Shipping Quote — .NET
description: "El mismo cotizador de envíos, portado a ASP.NET Core. Lo interesante no fue reescribirlo: fue lo que el port dejó a la vista."
permalink: /es/projects/shipping-quote-dotnet/
---

<p class="crumbs"><a href="{{ '/es/projects/' | relative_url }}">← Volver a proyectos</a></p>

<section class="hero">
  <h1>Shipping Quote — .NET <span class="tag active">activo</span></h1>
  <p class="lead">El mismo cotizador de envíos que existe en Python, portado a <strong>ASP.NET Core</strong>. Lo interesante no fue reescribirlo: fue que el port <strong>encontró dos bugs</strong> que el original nunca había mostrado.</p>
  <div class="chip-row">
    <span class="tag">C#</span><span class="tag">.NET 8</span><span class="tag">ASP.NET Core</span>
    <span class="tag">EF Core</span><span class="tag">MySQL</span><span class="tag">Testcontainers</span>
    <span class="tag">xUnit</span><span class="tag">Docker</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/shipping-quote-dotnet" target="_blank" rel="noopener">Repo ↗</a>
    <a href="{{ '/es/projects/shipping-quote/' | relative_url }}">La versión en Python →</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">La decisión de diseño</p>
  <p>Portar un sistema a otro stack es la forma más barata de descubrir qué partes eran arquitectura y qué partes eran costumbre. Lo que sobrevivió al cambio de lenguaje —los puertos, el pipeline, la política de precio— era diseño. Lo que hubo que rehacer eran decisiones que en Python parecían neutrales y en .NET no lo eran.</p>
</div>

<div class="statline">
  <div class="stat"><span class="num">63</span><span class="lbl">tests en CI</span></div>
  <div class="stat"><span class="num">306<small>ms</small></span><span class="lbl">3 carriers de 300ms c/u</span></div>
  <div class="stat"><span class="num">2</span><span class="lbl">bugs que encontró el port</span></div>
</div>

## Concurrencia, medida y no afirmada

Los tres transportistas se consultan en paralelo con `Task.WhenAll`: el request tarda lo
que el más lento, no la suma de los tres. Eso es fácil de escribir y fácil de romper sin
darse cuenta —alguien mete un `await` dentro de un `foreach` y sigue compilando, sigue
pasando los tests, y el servicio triplica su latencia en silencio—.

Por eso hay un test que lo **mide**:

```
3 transportistas × 300ms   →  306 ms      en fila serían 900
latencias 50 / 150 / 400   →  399 ms      la suma sería 600
```

El test falla si pasa de 700ms. No verifica que el código diga `Task.WhenAll`: verifica
que el reloj se comporte como si lo dijera.

Alrededor de eso, lo que hace que sea verdad y no casualidad:

- **`async`/`await` de punta a punta.** Ni un `.Result` ni un `.Wait()` en todo el repo:
  nada bloquea un hilo del pool esperando I/O.
- **`Task.Delay`, nunca `Thread.Sleep`.** Esperar sin ocupar un hilo es la diferencia
  entre aguantar mil requests concurrentes y quedarse sin pool.
- **`CancellationToken` enhebrado hasta el adaptador.** Si el cliente corta, se cortan las
  llamadas en vuelo. Hay un test con un transportista de 30 segundos que corta en 67ms.
- **`CreateLinkedTokenSource` para el timeout del contrato**, que así no pisa la
  cancelación del request entrante: respeta las dos.
- **Cada request con su propio `TraceRecorder`.** Un test lanza 40 requests concurrentes y
  verifica que ninguna traza se mezcle con otra. Es el que probaría que hay estado mutable
  compartido, si lo hubiera.

## El primer bug: la base de datos equivocada

El port arrancó con SQLite, igual que el original. El test de veinte cotizaciones
concurrentes falló:

```
SqliteException : SQLite Error 5: 'database is locked'
```

SQLite **serializa las escrituras**. Es decir: un servicio construido para mostrar trabajo
concurrente se trababa justo en el único punto donde escribe. El primer arreglo fue un
`busy_timeout`, que hace que la segunda escritura espere en vez de fallar —y que es
convertir un error en latencia, no resolver nada—.

La base pasó a **MySQL**, y ahí lo que antes era un parche se volvió diseño:

| Con SQLite | Con MySQL |
|---|---|
| plata guardada como `TEXT` | `decimal(12,2)` nativo |
| fecha como entero de ticks | `datetime(6)`, microsegundos |
| `busy_timeout` para no fallar | escrituras concurrentes reales |
| `EnsureCreated` | migraciones de EF Core |
| — | `EnableRetryOnFailure` ante deadlocks |

El `datetime(6)` no es exquisitez: sin los microsegundos, MySQL trunca a segundos y dos
cotizaciones del mismo segundo dejan de poder ordenarse entre sí.

## El segundo bug: uno que sólo se ve con la base real

Los tests de integración levantan un **MySQL 8.0 de verdad**, efímero, en un contenedor
que vive lo que dura la corrida. No una base falsa en memoria.

Esa decisión se pagó sola. La primera corrida contra el motor real tiró:

```
SQLite does not support expressions of type 'DateTimeOffset' in ORDER BY clauses
```

El endpoint de historial ordenaba por fecha, y el tipo `DateTimeOffset` no se puede
ordenar del lado del servidor. Es un error de **runtime**, no de compilación: el código
compilaba perfecto y se hubiera caído en producción, en el primer request al historial.

Un doble en memoria lo habría tapado. Los dos bugs más caros del proyecto aparecieron
porque del otro lado había un motor de verdad.

## La regla de negocio no sabe que existe HTTP

Que un bulto de más de 30 kg no se cotice es una regla de negocio. Que eso se comunique
como un `422` es una decisión de transporte. Son dos cosas distintas y viven en dos
lugares distintos: el dominio tira su excepción, y un **middleware** la traduce a HTTP.

```csharp
catch (Exception exc) when (exc is PackageTooHeavyException or InvalidPostalCodeException)
```

El controller no tiene un solo `try/catch`. Uno nuevo hereda el mapeo sin escribir nada.
Es Chain of Responsibility, que es exactamente lo que el pipeline de ASP.NET Core es por
dentro: cada middleware decide si maneja el request o se lo pasa al siguiente.

## Lo que no cambió

Cuatro proyectos, con las dependencias apuntando siempre hacia adentro:

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

Y los tres transportistas son tres **instancias** de la misma clase, no tres subclases:
cada uno aporta sólo datos —su endpoint y dos funciones de traducción—, mientras el
timeout, el manejo de errores y la traza viven una sola vez. Composición sobre herencia,
que es lo único que evita tres clases casi idénticas.

## Honestidad sobre el alcance

Los tres transportistas son **simulados**, igual que en la versión Python. Acá se montan
como un `HttpMessageHandler` propio: el `HttpClient` hace un POST real, con serialización,
status codes y deserialización reales, pero nunca sale a la red. El adaptador que se
testea es el mismo binario que correría en producción; lo único que se cambiaría es ese
último eslabón.

El valor no está en haber integrado a un transportista real. Está en que el mismo dominio
produzca tres resultados distintos sin enterarse de que existen tres, y en que uno de
ellos pueda caerse sin llevarse la respuesta puesta.
