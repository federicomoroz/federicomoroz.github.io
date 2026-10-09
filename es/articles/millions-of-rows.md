---
layout: article
article: millions-of-rows
title: "Tu BD funciona, hasta que llegan millones de datos"
description: "Con cien filas cualquier consulta es rápida, y por eso la base de desarrollo no avisa nada. Cómo llenarla con millones de registros parecidos a los reales y usarlos para decidir índices, claves foráneas, ordenamientos e índices compuestos antes de que el sistema crezca."
permalink: /es/articles/millions-of-rows/
image: /assets/img/articles/millions-of-rows/share.png
---

En desarrollo, la tabla de ventas tiene cien filas y todo responde al instante. Ninguna consulta parece lenta, porque ninguna tiene mucho para leer. Meses después, en producción, esa tabla pasó los diez millones de filas y la pantalla que más se usa empieza a tardar. El código es el mismo. Lo que cambió es cuántas filas tiene que mirar la base para contestar.

Eso se puede ver venir antes de que pase: llenando la base de desarrollo con millones de registros y mirando ahí cómo se resuelve cada consulta importante. Con un asistente de IA, el script que genera esos datos se escribe en minutos.

## Por qué con pocos datos todo anda

Sin un índice que le sirva, la base resuelve una consulta recorriendo la tabla entera y quedándose con las filas que cumplen la condición. Con cien filas, recorrerlas no cuesta nada: la consulta mal resuelta tarda lo mismo que la bien resuelta. Con diez millones, recorrerlas es justamente lo que tarda.

Un índice cambia eso. La base va directo a las filas que necesita, como en un libro se va del índice a la página. Pero en desarrollo la diferencia no se ve, así que nadie se entera de qué consultas lo necesitan hasta que la tabla crece. En [el artículo sobre fechas]({{ '/es/articles/indexing-dates/' | relative_url }}) lo medí con 2.000.000 de pedidos: el reporte de un día pasaba de 33 ms a 1,1 ms con un índice en la fecha.

## 1. Encontrá el núcleo del sistema

No hace falta optimizar todo. Cada sistema tiene una parte que no puede fallar: la que hace aquello para lo que el sistema existe. En un sistema de ventas es donde se hace la venta, no donde se sacan los reportes de ventas. En uno de venta de entradas, es la compra.

Ese recorrido son pocas consultas, y se ejecutan miles de veces con una persona esperando del otro lado:

- ver cuántas entradas quedan en cada sector del evento;
- elegir butacas libres en un sector;
- confirmar la compra;
- ver "mis entradas".

El reporte de ventas del mes, en cambio, corre una vez por día y puede tardar unos segundos sin que nadie lo sufra. Eso define dónde poner el esfuerzo, y también dónde no: cada índice se actualiza en cada compra, así que indexar para el reporte hace más lenta la compra.

## 2. Llená la base de desarrollo con millones de registros

La de desarrollo, nunca la de producción. El llenado puede vivir en un procedimiento almacenado, pero conviene que adentro haya una sola sentencia por tabla que genere todas las filas con `generate_series`, y no un bucle que inserte de a una: la base hace el trabajo de una vez, sin ir y volver por cada fila.

Para un sistema de entradas, este es el esquema:

```sql
CREATE TABLE users (
    id    bigserial PRIMARY KEY,
    email text NOT NULL
);

CREATE TABLE events (
    id                bigserial PRIMARY KEY,
    name              text NOT NULL,
    starts_at         timestamptz NOT NULL,
    sections          int NOT NULL,
    seats_per_section int NOT NULL
);

CREATE TABLE tickets (
    id       bigserial PRIMARY KEY,
    event_id bigint NOT NULL REFERENCES events (id),
    section  int NOT NULL,
    seat     int NOT NULL,
    price    numeric(10, 2) NOT NULL,
    status   text NOT NULL,
    user_id  bigint REFERENCES users (id),
    sold_at  timestamptz
);
```

Y este, el llenado: un millón de usuarios y 16.310 eventos repartidos en dos años, de cuatro tamaños. Diez estadios de 60.000 butacas, 300 estadios cubiertos de 10.000, 4.000 teatros de 1.000 y 12.000 bares de 200. Cada butaca es una entrada, así que son diez millones. Los eventos que ya pasaron vendieron el 95 % de sus butacas; los que vienen, entre el 20 % y el 80 %.

```sql
SELECT setseed(0.42);

INSERT INTO users (email)
SELECT 'user' || n || '@example.com'
FROM generate_series(1, 1000000) n;

INSERT INTO events (name, starts_at, sections, seats_per_section)
SELECT 'Event ' || row_number() OVER (), starts_at, sections, seats
FROM (
    SELECT timestamptz '2025-10-01 21:00' + (random() * 730)::int * interval '1 day' AS starts_at,
           sections, seats
    FROM (VALUES (10, 30, 2000), (300, 10, 1000), (4000, 4, 250), (12000, 1, 200))
             AS venue (events, sections, seats),
         generate_series(1, venue.events)
    ORDER BY random()
) e;

INSERT INTO tickets (event_id, section, seat, price, status, user_id, sold_at)
WITH e AS MATERIALIZED (
    SELECT id, starts_at, sections, seats_per_section,
           CASE WHEN starts_at < now() THEN 0.95 ELSE 0.2 + random() * 0.6 END AS sold_ratio
    FROM events
)
SELECT event_id, section, seat, price,
       CASE WHEN sold THEN 'sold' ELSE 'available' END,
       CASE WHEN sold THEN 1 + (random() * 999999)::bigint END,
       CASE WHEN sold THEN least(starts_at, now()) - random() * interval '60 days' END
FROM (
    SELECT e.id AS event_id, s AS section, seat, 10000 + 2500 * (s % 8) AS price, e.starts_at,
           random() < e.sold_ratio AS sold
    FROM e, generate_series(1, e.sections) s, generate_series(1, e.seats_per_section) seat
    ORDER BY e.id, s, seat
) t;

VACUUM ANALYZE;
```

`setseed` hace que los números al azar salgan iguales en cada corrida, así una medición se puede repetir. `MATERIALIZED` hace que el porcentaje vendido se sortee una vez por evento y no una vez por entrada. Y el `ORDER BY` final guarda las entradas en el orden en que se crean en la realidad: todas juntas, cuando se publica el evento. `VACUUM ANALYZE` deja las estadísticas al día para que la base elija bien cómo resolver cada consulta.

### Que se parezcan a los datos reales

Diez millones de filas iguales no alcanzan. Lo que hace útil la prueba es que los datos tengan la forma de los de producción:

- **Cuántas filas tiene cada tabla.** La proporción entre tablas importa tanto como el total: un millón de usuarios, dieciséis mil eventos, diez millones de entradas.
- **Cómo se reparten.** Un estadio tiene 60.000 butacas y un bar, 200. Si el script genera todos los eventos del mismo tamaño, la prueba con un evento cualquiera sale bien, y el problema del estadio, que es el que más vende el día que sale a la venta, no aparece.
- **Qué valores se repiten.** La columna `status` tiene dos valores; `user_id`, un millón. La base decide distinto según cuántas filas devuelve cada valor.
- **En qué orden llegan.** Las entradas de un evento se crean juntas y las fechas de venta crecen. El orden en que quedan guardadas cambia cuánto lee la base para encontrarlas.

<div class="callout">
  <p class="callout-title">Pedíselo a la IA con los números</p>
  <p>"Escribí un script de PostgreSQL para la base de desarrollo que llene estas tablas con una sola sentencia INSERT … SELECT por tabla, usando generate_series. Un millón de usuarios y 16.310 eventos repartidos en dos años: 10 de 60.000 butacas, 300 de 10.000, 4.000 de 1.000 y 12.000 de 200. Cada butaca es una entrada. Los eventos pasados vendieron el 95 %; los futuros, entre el 20 % y el 80 %. Fijá la semilla con setseed." Y abajo, el esquema. Sin esos números, el script sale con datos parejos y la prueba no muestra nada.</p>
</div>

## 3. Medí las consultas del núcleo

Con los datos cargados, cada consulta del núcleo pasa por `EXPLAIN ANALYZE`, que la ejecuta y muestra cómo la resolvió la base y cuánto tardó:

```sql
EXPLAIN ANALYZE
SELECT id, seat FROM tickets
WHERE event_id = 42 AND section = 12 AND status = 'available'
ORDER BY seat
LIMIT 4;
```

Lo que conviene mirar en la salida:

- **`Seq Scan on tickets`**: recorrió la tabla entera. En una tabla de millones y en una consulta del núcleo, es la primera señal.
- **`Rows Removed by Filter`**: cuántas filas leyó y descartó. Si leyó decenas de miles para devolver cuatro, le falta un índice que la lleve directo.
- **`Sort`**: tuvo que ordenar antes de devolver las primeras filas.
- **`Execution Time`**: el tiempo total, para comparar antes y después de cada cambio con los mismos datos.

Y la prueba se hace con el caso grande, no con el promedio: el evento con más butacas que esté a la venta, el usuario con más compras.

## 4. Lo que vas a decidir con los datos cargados

### Dónde poner índices

En las columnas que usan los `WHERE` y los `JOIN` de las consultas del núcleo que leen mucho más de lo que devuelven. No en todas las columnas: cada índice ocupa espacio y se actualiza en cada escritura.

### Claves foráneas

En PostgreSQL, declarar `REFERENCES` no crea un índice en la columna que referencia: solo tiene índice la clave primaria del otro lado. MySQL con InnoDB sí lo crea solo, y por eso es fácil darlo por sentado.

Sin un índice en `tickets.user_id`, "mis entradas" recorre las diez millones de entradas para encontrar las de una persona. Y hay un costo que se ve menos: para borrar un evento, la base tiene que comprobar que ninguna entrada lo referencia, y sin un índice en `tickets.event_id` esa comprobación recorre la tabla entera.

```sql
CREATE INDEX ON tickets (user_id);
```

### Índices compuestos

Elegir butacas filtra por tres columnas a la vez, evento, estado y sector, y ordena por butaca. Un índice solo en `event_id` encuentra el evento, pero después revisa sus entradas una por una: en un bar son 200; en un estadio, 60.000. Un índice con las cuatro columnas va directo a las butacas libres de ese sector, y ya ordenadas:

```sql
CREATE INDEX ON tickets (event_id, status, section, seat);
```

El orden de las columnas importa. Primero van las que se comparan por igualdad, y al final la que se usa para ordenar o para un rango. Así, las entradas que busca la consulta quedan juntas dentro del índice. El mismo índice sirve para contar cuántas quedan por sector, que filtra por evento y estado y agrupa por sector. Y como empieza por `event_id`, también cubre la clave foránea del evento: no hace falta otro índice solo para esa columna.

En el artículo sobre fechas, un índice compuesto con el cliente adelante llevó los pedidos de un cliente en un mes de 9,8 ms a 0,08 ms.

### Si vale la pena ordenar

Un `ORDER BY` sin un índice que ya tenga ese orden obliga a la base a leer todas las filas candidatas para saber cuáles van primero. Para las pocas entradas de una persona no importa: ordenarlas no cuesta nada. Para un listado sobre una tabla grande, sí. Si el índice ya tiene el orden, la base lee las primeras filas y se detiene. Es lo que hace `seat` al final del índice compuesto, y en el artículo sobre fechas fue la diferencia entre 137 ms y 0,04 ms para los últimos 20 pedidos.

Si el listado además se pagina, `OFFSET` lee y descarta todas las filas de las páginas anteriores. Para páginas profundas conviene seguir desde la última fila vista, con una condición como `WHERE sold_at < <la última fecha mostrada>`.

### Cuándo hacer cada consulta

El reporte de ventas del mes necesita la mayoría de las filas, así que la base lo resuelve recorriendo la tabla con índice o sin él. Indexar para el reporte casi no lo acelera y encarece cada compra. Lo que sí se decide es cuándo y dónde corre: de noche, sobre una réplica de lectura o sobre una tabla de resumen que se actualiza una vez por día. Así no compite con las compras.

## Lo que cuesta cada índice

Cada `INSERT` escribe también en todos los índices de la tabla. Y una compra cambia `status`, `user_id` y `sold_at`, columnas indexadas, así que PostgreSQL agrega una entrada nueva en cada índice de la tabla, no solo en los de esas columnas. En el artículo sobre fechas, un solo índice B-tree sumó alrededor de un 20 % al costo de insertar.

Por eso el orden es medir, agregar el índice que una consulta del núcleo necesita y volver a medir para comprobar que la consulta lo usa. Un índice que ninguna consulta usa solo cuesta.

## El recorrido completo

1. Elegí las consultas del núcleo: las que corren más veces con alguien esperando.
2. Llená la base de desarrollo con millones de filas que tengan la forma de las reales: cantidades, reparto, valores repetidos y orden.
3. Pasá cada consulta del núcleo por `EXPLAIN ANALYZE`, con el caso grande y no con el promedio.
4. Donde lea mucho más de lo que devuelve, agregá el índice que la lleve directo: el de la clave foránea, el compuesto, el que ya trae el orden.
5. Volvé a medir. Si el índice no se usa, sacalo.

La IA escribe el script en minutos y puede sugerir índices. Lo que no puede adivinar es cómo son tus datos y qué parte del sistema no puede fallar: eso se lo das vos.
