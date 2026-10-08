---
layout: article
article: indexing-dates
title: "Fechas en la base de datos: 59 ms o 1 ms según cómo escribís la consulta"
description: "Cuatro formas de indexar y consultar fechas, medidas en PostgreSQL 17 con 2.000.000 de pedidos: qué índice conviene, qué consulta lo deja usar, cuándo conviene BRIN y cuánto cuesta cada índice al insertar."
permalink: /es/articles/indexing-dates/
image: /assets/img/articles/indexing-dates/share.png
---

Casi todo backend filtra por fecha: los pedidos de hoy, el reporte del mes, los últimos movimientos. Indexar la fecha de creación ayuda, pero que la base use el índice depende de cómo está escrita la consulta. Lo medí en PostgreSQL 17 con una tabla de 2.000.000 de pedidos y lo resumo en cuatro comparaciones, cada una con las dos formas lado a lado.

<div class="statline">
  <div class="stat"><span class="num">31×</span><span class="lbl">más rápido el reporte de un día con un índice en la fecha</span></div>
  <div class="stat"><span class="num">56×</span><span class="lbl">entre filtrar con DATE(created_at) y con un rango, con el mismo índice</span></div>
  <div class="stat"><span class="num">21</span><span class="lbl">pedidos al año que un reporte hasta las 23:59:59 nunca cuenta</span></div>
</div>

## El banco de pruebas

Una tabla de pedidos con un año de datos, del 1 de octubre de 2025 al 1 de octubre de 2026: uno cada 15,8 segundos en promedio, entre 10.000 clientes, insertados en el orden en que ocurren y con microsegundos en `created_at`. Son 2.000.000 de filas y ocupan 130 MB. Cada consulta corrió tres veces con `EXPLAIN ANALYZE` y los datos ya en memoria, y los números de abajo son la mediana.

```sql
CREATE TABLE pedidos (
    id         bigserial PRIMARY KEY,
    cliente_id int NOT NULL,
    total      numeric(12, 2) NOT NULL,
    estado     text NOT NULL,
    created_at timestamptz NOT NULL
);
```

## 1. Indexar la fecha

<figure class="shot">
  <img src="{{ '/assets/img/articles/indexing-dates/1-es.webp' | relative_url }}" alt="Dos columnas. Sin índice, la consulta de un día lee las 2.000.000 de filas de la tabla y tarda 33 ms. Con un índice B-tree en created_at va directo al 29 de abril, lee 5.480 filas y tarda 1,1 ms." loading="lazy" width="1960" height="1162">
  <figcaption>Los pedidos del 29 de abril: sin índice se recorre el año entero; con el índice, solo ese día.</figcaption>
</figure>

Sin índice, encontrar los pedidos de un día obliga a recorrer la tabla entera: PostgreSQL lee las 2.000.000 de filas y se queda con 5.480. Con un B-tree en `created_at` baja directo al día y lee solo esas 5.480. El reporte pasa de 33 ms a 1,1 ms.

```sql
CREATE INDEX ON pedidos (created_at);

SELECT count(*), sum(total) FROM pedidos
WHERE created_at >= '2026-04-29' AND created_at < '2026-04-30';
```

El índice además ya está ordenado. Los últimos 20 pedidos, `ORDER BY created_at DESC LIMIT 20`, salen leyéndolo desde el final: 0,04 ms, contra 137 ms de recorrer y ordenar la tabla entera. Y como la fecha de creación siempre crece, cada pedido nuevo se agrega al final del índice.

## 2. Que la consulta deje usar el índice

<figure class="shot">
  <img src="{{ '/assets/img/articles/indexing-dates/2-es.webp' | relative_url }}" alt="Dos columnas con el mismo índice puesto. Con DATE(created_at) = '2026-04-29' el índice no se usa: se leen 2.000.000 de filas en 59 ms. Con el rango created_at >= '2026-04-29' AND created_at < '2026-04-30' se leen 5.480 filas en 1,1 ms." loading="lazy" width="1960" height="1162">
  <figcaption>La misma pregunta, el mismo índice: lo que cambia es si la columna queda sola en la condición.</figcaption>
</figure>

Con el índice puesto, `WHERE DATE(created_at) = '2026-04-29'` no lo usa. El índice guarda `created_at`, no `DATE(created_at)`, así que PostgreSQL tiene que calcular la función en cada una de las 2.000.000 de filas. Tarda 59 ms, más que la tabla sin índice. La misma pregunta escrita como rango sí lo usa y tarda 1,1 ms.

```sql
-- No usa el índice: calcula DATE() en cada fila.
WHERE DATE(created_at) = '2026-04-29'

-- Usa el índice: la columna queda sola.
WHERE created_at >= '2026-04-29' AND created_at < '2026-04-30'
```

Pasa con cualquier función o cálculo aplicado a la columna. La salida es dejar la columna sola y llevar el cálculo al otro lado de la comparación, como en el rango.

Y el rango conviene semiabierto, mayor o igual que el día y menor que el siguiente, por otra razón. `BETWEEN '2026-04-29 00:00:00' AND '2026-04-29 23:59:59'` deja afuera lo que pase entre las 23:59:59 y la medianoche, y PostgreSQL guarda `timestamptz` con microsegundos. En la tabla de prueba hay 21 pedidos en el último segundo de su día: un reporte diario escrito así no los cuenta nunca.

## 3. Igualdad primero, rango después

<figure class="shot">
  <img src="{{ '/assets/img/articles/indexing-dates/3-es.webp' | relative_url }}" alt="Dos columnas. Con un índice en created_at, los pedidos del cliente 4242 en abril obligan a leer los 164.384 pedidos del mes y tardan 9,8 ms. Con un índice en (cliente_id, created_at) se leen los 7 pedidos del cliente en 0,08 ms." loading="lazy" width="1960" height="1162">
  <figcaption>Con el cliente adelante, sus pedidos quedan juntos y ordenados por fecha dentro del índice.</figcaption>
</figure>

Para los pedidos de un cliente en un mes, el índice en `created_at` ayuda a medias. Encuentra abril, pero tiene que leer los 164.384 pedidos del mes y descartar los de los otros 9.999 clientes: 9,8 ms. Un índice compuesto con el cliente adelante va directo a los 7 pedidos de ese cliente en abril: 0,08 ms.

```sql
CREATE INDEX ON pedidos (cliente_id, created_at);

SELECT count(*), sum(total) FROM pedidos
WHERE cliente_id = 4242
  AND created_at >= '2026-04-01' AND created_at < '2026-05-01';
```

El orden de las columnas importa. Con `(cliente_id, created_at)` las entradas de cada cliente quedan juntas y ordenadas por fecha, así que la igualdad elige el grupo y el rango recorre un tramo de ese grupo. Con la fecha adelante, el rango se lleva todo el mes y el cliente se vuelve a filtrar entrada por entrada.

## 4. BRIN para tablas que solo crecen

<figure class="shot">
  <img src="{{ '/assets/img/articles/indexing-dates/4-es.webp' | relative_url }}" alt="Dos columnas. El índice B-tree guarda una entrada por fila: ocupa 43 MB, lee un día en 1,1 ms y suma un 20 % al costo de insertar. BRIN guarda un mínimo y un máximo por tramo: ocupa 24 kB, lee un día en 2,4 ms y suma un 7 % al insertar." loading="lazy" width="1960" height="1144">
  <figcaption>BRIN resume cada tramo de la tabla en su fecha mínima y máxima: el tramo de abril y mayo es el único que puede tener el 29 de abril.</figcaption>
</figure>

Un B-tree guarda una entrada por fila: con 2.000.000 de pedidos ocupa 43 MB, un tercio de la tabla. BRIN guarda solo el mínimo y el máximo de `created_at` de cada tramo de 128 páginas, y ocupa 24 kB. Para leer un día, PostgreSQL descarta los tramos cuyo rango no lo incluye y revisa los que quedan. Tarda 2,4 ms, contra 1,1 del B-tree, porque lee 256 bloques enteros y descarta 25.240 filas que no son del día.

```sql
CREATE INDEX ON pedidos USING brin (created_at);
```

Funciona porque las filas llegan en orden de fecha y cada tramo cubre pocos días. Si las fechas llegan desordenadas, por ejemplo porque se cargan pedidos viejos más tarde, los tramos se superponen y BRIN deja de descartar.

## Lo que cuesta un índice

Cada índice se actualiza en cada `INSERT`. Inserté 100.000 pedidos de a uno en tres copias de la tabla que solo difieren en ese índice, cinco veces cada una. Sin índice en la fecha tardó 934 ms (la mediana), con el B-tree 1.126 ms, alrededor de un 20 % más, y con BRIN 999 ms, un 7 % más.

Por eso un índice se agrega cuando hay una consulta que lo necesita, y se comprueba con `EXPLAIN ANALYZE` que esa consulta lo usa. Un índice que ninguna consulta usa solo cuesta.

## Los números

| Consulta | Forma A | Forma B |
|---|---|---|
| Pedidos de un día | sin índice: 33 ms | B-tree: 1,1 ms |
| El mismo día, con el índice puesto | `DATE(created_at)`: 59 ms | rango: 1,1 ms |
| Últimos 20 pedidos | sin índice: 137 ms | B-tree: 0,04 ms |
| Pedidos de un cliente en un mes | `(created_at)`: 9,8 ms | `(cliente_id, created_at)`: 0,08 ms |
| Pedidos de un día | B-tree de 43 MB: 1,1 ms | BRIN de 24 kB: 2,4 ms |

## Reproducirlo

El script crea la misma tabla con los mismos datos: la semilla hace que los números al azar sean siempre los mismos. Las mediciones corrieron en la imagen `postgres:17-alpine` de Docker.

```sql
SET TIME ZONE 'America/Argentina/Buenos_Aires';
SELECT setseed(0.42);

CREATE TABLE pedidos (
    id         bigserial PRIMARY KEY,
    cliente_id int NOT NULL,
    total      numeric(12, 2) NOT NULL,
    estado     text NOT NULL,
    created_at timestamptz NOT NULL
);

INSERT INTO pedidos (cliente_id, total, estado, created_at)
SELECT 1 + (random() * 9999)::int,
       round((random() * 100000)::numeric, 2),
       'entregado',
       timestamptz '2025-10-01 00:00:00-03' + n * interval '15.768 seconds'
           + random() * interval '10 seconds'
FROM generate_series(1, 2000000) n;

VACUUM ANALYZE pedidos;

EXPLAIN ANALYZE SELECT count(*), sum(total) FROM pedidos
WHERE created_at >= '2026-04-29' AND created_at < '2026-04-30';
```

Después se crea el índice, se repite el `EXPLAIN ANALYZE` y se prueban las otras formas: `DATE(created_at)`, el índice `(cliente_id, created_at)` y `USING brin`. Los tiempos cambian con la máquina. Lo que lee cada consulta, no.
