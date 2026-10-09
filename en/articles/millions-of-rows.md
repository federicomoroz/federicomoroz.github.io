---
layout: article
article: millions-of-rows
title: "Your database works, until millions of rows show up"
description: "With a hundred rows every query is fast, which is why the development database never warns you. How to fill it with millions of records shaped like the real ones and use them to decide indexes, foreign keys, sorting and composite indexes before the system grows."
permalink: /en/articles/millions-of-rows/
image: /assets/img/articles/millions-of-rows/share.png
---

In development, the sales table has a hundred rows and everything answers instantly. No query looks slow, because none of them has much to read. Months later, in production, that table is past ten million rows and the most used screen starts to lag. The code is the same. What changed is how many rows the database has to look at to answer.

You can see it coming before it happens: fill the development database with millions of records and watch how each important query gets resolved there. With an AI assistant, the script that generates that data takes minutes to write.

## Why everything works with little data

Without an index it can use, the database answers a query by walking the whole table and keeping the rows that match. With a hundred rows, walking them costs nothing: the badly resolved query takes as long as the well resolved one. With ten million, walking them is exactly what takes the time.

An index changes that. The database goes straight to the rows it needs, the way you go from a book's index to the page. But in development the difference doesn't show, so nobody finds out which queries need one until the table grows. In [the article on dates]({{ '/en/articles/indexing-dates/' | relative_url }}) I measured it with 2,000,000 orders: the one-day report went from 33 ms to 1.1 ms with an index on the date.

## 1. Find the core of the system

You don't need to optimize everything. Every system has a part that can't fail: the one that does what the system exists to do. In a sales system it's where the sale happens, not where the sales reports come from. In a ticketing system, it's the purchase.

That path is a handful of queries, and they run thousands of times with a person waiting on the other end:

- see how many tickets are left in each section of the event;
- pick free seats in a section;
- confirm the purchase;
- see "my tickets".

The monthly sales report, on the other hand, runs once a day and can take a few seconds without anyone suffering it. That tells you where to put the effort, and also where not to: every index is updated on every purchase, so indexing for the report makes the purchase slower.

## 2. Fill the development database with millions of records

The development one, never production. The fill can live in a stored procedure, but inside it there should be one statement per table that generates every row with `generate_series`, not a loop that inserts them one at a time: the database does the work in one go, without a round trip per row.

For a ticketing system, this is the schema:

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

And this is the fill: a million users and 16,310 events spread over two years, in four sizes. Ten stadiums of 60,000 seats, 300 arenas of 10,000, 4,000 theaters of 1,000 and 12,000 clubs of 200. Every seat is a ticket, so that's ten million. Past events sold 95% of their seats; upcoming ones, between 20% and 80%.

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

`setseed` makes the random numbers come out the same on every run, so a measurement can be repeated. `MATERIALIZED` makes the sold share be drawn once per event and not once per ticket. And the final `ORDER BY` stores the tickets in the order they're created in real life: all together, when the event is published. `VACUUM ANALYZE` brings the statistics up to date so the database picks well how to resolve each query.

### Shaped like the real data

Ten million identical rows are not enough. What makes the test useful is data with the shape of production's:

- **How many rows each table has.** The ratio between tables matters as much as the total: a million users, sixteen thousand events, ten million tickets.
- **How they're spread.** A stadium has 60,000 seats and a club, 200. If the script makes every event the same size, the test with any event passes, and the stadium's problem, the one that sells the most on the day it goes on sale, never shows up.
- **Which values repeat.** The `status` column has two values; `user_id`, a million. The database decides differently depending on how many rows each value returns.
- **In which order they arrive.** An event's tickets are created together and sale dates keep growing. The order they're stored in changes how much the database reads to find them.

<div class="callout">
  <p class="callout-title">Ask the AI with the numbers</p>
  <p>"Write a PostgreSQL script for the development database that fills these tables with a single INSERT … SELECT per table, using generate_series. A million users and 16,310 events spread over two years: 10 with 60,000 seats, 300 with 10,000, 4,000 with 1,000 and 12,000 with 200. Every seat is a ticket. Past events sold 95%; future ones, between 20% and 80%. Fix the seed with setseed." And the schema below it. Without those numbers, the script comes out with even data and the test shows nothing.</p>
</div>

## 3. Measure the core queries

With the data loaded, every core query goes through `EXPLAIN ANALYZE`, which runs it and shows how the database resolved it and how long it took:

```sql
EXPLAIN ANALYZE
SELECT id, seat FROM tickets
WHERE event_id = 42 AND section = 12 AND status = 'available'
ORDER BY seat
LIMIT 4;
```

What to look at in the output:

- **`Seq Scan on tickets`**: it walked the whole table. On a table of millions and in a core query, that's the first sign.
- **`Rows Removed by Filter`**: how many rows it read and threw away. If it read tens of thousands to return four, it's missing an index that takes it straight there.
- **`Sort`**: it had to sort before returning the first rows.
- **`Execution Time`**: the total time, to compare before and after each change on the same data.

And the test uses the big case, not the average one: the event with the most seats that's on sale, the user with the most purchases.

## 4. What you'll decide with the data loaded

### Where to put indexes

On the columns used by the `WHERE` and `JOIN` clauses of the core queries that read far more than they return. Not on every column: every index takes space and is updated on every write.

### Foreign keys

In PostgreSQL, declaring `REFERENCES` doesn't create an index on the referencing column: only the primary key on the other side has one. MySQL with InnoDB does create it on its own, which is why it's easy to take for granted.

Without an index on `tickets.user_id`, "my tickets" walks all ten million tickets to find one person's. And there's a cost that's harder to see: to delete an event, the database has to check that no ticket references it, and without an index on `tickets.event_id` that check walks the whole table.

```sql
CREATE INDEX ON tickets (user_id);
```

### Composite indexes

Picking seats filters on three columns at once, event, status and section, and sorts by seat. An index on `event_id` alone finds the event, but then goes through its tickets one by one: 200 in a club; 60,000 in a stadium. An index with the four columns goes straight to the free seats of that section, already sorted:

```sql
CREATE INDEX ON tickets (event_id, status, section, seat);
```

Column order matters. First the ones compared by equality, and last the one used to sort or for a range. That way, the tickets the query is after sit together inside the index. The same index serves counting how many are left per section, which filters by event and status and groups by section. And since it starts with `event_id`, it also covers the event's foreign key: there's no need for another index on that column alone.

In the article on dates, a composite index with the customer first took one customer's orders in a month from 9.8 ms to 0.08 ms.

### Whether sorting is worth it

An `ORDER BY` without an index that already holds that order forces the database to read every candidate row to know which ones come first. For one person's few tickets it doesn't matter: sorting them costs nothing. For a listing over a big table, it does. If the index already has the order, the database reads the first rows and stops. That's what `seat` at the end of the composite index does, and in the article on dates it was the difference between 137 ms and 0.04 ms for the latest 20 orders.

If the listing is also paginated, `OFFSET` reads and throws away every row of the previous pages. For deep pages it's better to continue from the last row seen, with a condition like `WHERE sold_at < <the last date shown>`.

### When to run each query

The monthly sales report needs most of the rows, so the database resolves it by walking the table, index or no index. Indexing for the report barely speeds it up and makes every purchase more expensive. What you do decide is when and where it runs: at night, on a read replica or on a summary table updated once a day. That way it doesn't compete with purchases.

## What each index costs

Every `INSERT` also writes to every index on the table. And a purchase changes `status`, `user_id` and `sold_at`, which are indexed columns, so PostgreSQL adds a new entry to every index on the table, not only the ones on those columns. In the article on dates, a single B-tree index added around 20% to the cost of inserting.

That's why the order is: measure, add the index a core query needs, and measure again to check the query uses it. An index no query uses only costs.

## The whole path

1. Pick the core queries: the ones that run most often with someone waiting.
2. Fill the development database with millions of rows shaped like the real ones: counts, spread, repeated values and order.
3. Run every core query through `EXPLAIN ANALYZE`, with the big case and not the average one.
4. Where it reads far more than it returns, add the index that takes it straight there: the foreign key's, the composite one, the one that already holds the order.
5. Measure again. If the index isn't used, drop it.

AI writes the script in minutes and can suggest indexes. What it can't guess is what your data looks like and which part of the system can't fail: that part comes from you.
