---
layout: article
article: indexing-dates
title: "Dates in the database: 59 ms or 1 ms depending on how you write the query"
description: "Four ways to index and query dates, measured in PostgreSQL 17 with 2,000,000 orders: which index pays off, which query lets it work, when BRIN wins and what each index costs on insert."
permalink: /en/articles/indexing-dates/
image: /assets/img/articles/indexing-dates/share.png
---

Almost every backend filters by date: today's orders, the monthly report, the latest transactions. Indexing the creation date helps, but whether the database uses the index depends on how the query is written. I measured it in PostgreSQL 17 on a table of 2,000,000 orders, and it comes down to four comparisons, each with the two ways side by side.

<div class="statline">
  <div class="stat"><span class="num">31×</span><span class="lbl">faster one-day report with an index on the date</span></div>
  <div class="stat"><span class="num">56×</span><span class="lbl">between filtering with DATE(created_at) and with a range, on the same index</span></div>
  <div class="stat"><span class="num">21</span><span class="lbl">orders a year that a report up to 23:59:59 never counts</span></div>
</div>

## The test bench

A table of orders holding one year of data, from October 1, 2025 to October 1, 2026: one order every 15.8 seconds on average, among 10,000 customers, inserted in the order they happen and with microseconds in `created_at`. That is 2,000,000 rows in 130 MB. Each query ran three times with `EXPLAIN ANALYZE` and the data already in memory, and the numbers below are the median.

```sql
CREATE TABLE orders (
    id          bigserial PRIMARY KEY,
    customer_id int NOT NULL,
    total       numeric(12, 2) NOT NULL,
    status      text NOT NULL,
    created_at  timestamptz NOT NULL
);
```

## 1. Index the date

<figure class="shot">
  <img src="{{ '/assets/img/articles/indexing-dates/1-en.webp' | relative_url }}" alt="Two columns. Without an index, the one-day query reads all 2,000,000 rows of the table and takes 33 ms. With a B-tree index on created_at it goes straight to April 29, reads 5,480 rows and takes 1.1 ms." loading="lazy" width="1960" height="1162">
  <figcaption>The orders of April 29: without an index the whole year is read; with it, only that day.</figcaption>
</figure>

Without an index, finding one day's orders means scanning the whole table: PostgreSQL reads all 2,000,000 rows and keeps 5,480. With a B-tree on `created_at` it goes straight to the day and reads only those 5,480. The report drops from 33 ms to 1.1 ms.

```sql
CREATE INDEX ON orders (created_at);

SELECT count(*), sum(total) FROM orders
WHERE created_at >= '2026-04-29' AND created_at < '2026-04-30';
```

The index is also already sorted. The latest 20 orders, `ORDER BY created_at DESC LIMIT 20`, come out by reading it from the end: 0.04 ms, against 137 ms for scanning and sorting the whole table. And since the creation date only grows, every new order is added at the end of the index.

## 2. Let the query use the index

<figure class="shot">
  <img src="{{ '/assets/img/articles/indexing-dates/2-en.webp' | relative_url }}" alt="Two columns with the same index in place. With DATE(created_at) = '2026-04-29' the index goes unused: 2,000,000 rows are read in 59 ms. With the range created_at >= '2026-04-29' AND created_at < '2026-04-30', 5,480 rows are read in 1.1 ms." loading="lazy" width="1960" height="1162">
  <figcaption>The same question, the same index: what changes is whether the column stands alone in the condition.</figcaption>
</figure>

With the index in place, `WHERE DATE(created_at) = '2026-04-29'` does not use it. The index stores `created_at`, not `DATE(created_at)`, so PostgreSQL has to compute the function on each of the 2,000,000 rows. It takes 59 ms, more than the table without an index. The same question written as a range does use it and takes 1.1 ms.

```sql
-- Does not use the index: computes DATE() on every row.
WHERE DATE(created_at) = '2026-04-29'

-- Uses the index: the column stands alone.
WHERE created_at >= '2026-04-29' AND created_at < '2026-04-30'
```

The same happens with any function or calculation applied to the column. The way out is to leave the column alone and move the calculation to the other side of the comparison, as the range does.

And the range is better half-open, greater than or equal to the day and less than the next one, for another reason. `BETWEEN '2026-04-29 00:00:00' AND '2026-04-29 23:59:59'` leaves out whatever happens between 23:59:59 and midnight, and PostgreSQL stores `timestamptz` with microseconds. The test table has 21 orders in the last second of their day: a daily report written that way never counts them.

## 3. Equality first, range second

<figure class="shot">
  <img src="{{ '/assets/img/articles/indexing-dates/3-en.webp' | relative_url }}" alt="Two columns. With an index on created_at, customer 4242's orders in April require reading the month's 164,384 orders and take 9.8 ms. With an index on (customer_id, created_at), the customer's 7 orders are read in 0.08 ms." loading="lazy" width="1960" height="1162">
  <figcaption>With the customer first, their orders sit together inside the index, sorted by date.</figcaption>
</figure>

For one customer's orders in one month, the index on `created_at` only half helps. It finds April, but it has to read the month's 164,384 orders and discard those of the other 9,999 customers: 9.8 ms. A composite index with the customer first goes straight to that customer's 7 orders in April: 0.08 ms.

```sql
CREATE INDEX ON orders (customer_id, created_at);

SELECT count(*), sum(total) FROM orders
WHERE customer_id = 4242
  AND created_at >= '2026-04-01' AND created_at < '2026-05-01';
```

The order of the columns matters. With `(customer_id, created_at)` each customer's entries sit together, sorted by date, so the equality picks the group and the range walks a stretch of it. With the date first, the range takes the whole month and the customer is filtered again entry by entry.

## 4. BRIN for tables that only grow

<figure class="shot">
  <img src="{{ '/assets/img/articles/indexing-dates/4-en.webp' | relative_url }}" alt="Two columns. The B-tree index stores one entry per row: it takes 43 MB, reads one day in 1.1 ms and adds 20% to the cost of an insert. BRIN stores one minimum and one maximum per range: it takes 24 kB, reads one day in 2.4 ms and adds 7% to an insert." loading="lazy" width="1960" height="1144">
  <figcaption>BRIN sums up each range of the table in its earliest and latest date: the April to May range is the only one that can hold April 29.</figcaption>
</figure>

A B-tree stores one entry per row: with 2,000,000 orders it takes 43 MB, a third of the table. BRIN stores only the minimum and maximum `created_at` of each range of 128 pages, and takes 24 kB. To read one day, PostgreSQL discards the ranges that cannot contain it and checks the rest. It takes 2.4 ms, against 1.1 for the B-tree, because it reads 256 whole blocks and discards 25,240 rows from other days.

```sql
CREATE INDEX ON orders USING brin (created_at);
```

It works because the rows arrive in date order and each range covers a few days. If dates arrive out of order, for instance because old orders are loaded later, the ranges overlap and BRIN stops discarding.

## What an index costs

Every index is updated on every `INSERT`. I inserted 100,000 orders one at a time into three copies of the table that differ only in that index, five times each. Without an index on the date it took 934 ms (the median), with the B-tree 1,126 ms, about 20% more, and with BRIN 999 ms, 7% more.

So an index is added when a query needs it, and `EXPLAIN ANALYZE` confirms that the query uses it. An index no query uses only costs.

## The numbers

| Query | Way A | Way B |
|---|---|---|
| One day's orders | no index: 33 ms | B-tree: 1.1 ms |
| The same day, with the index in place | `DATE(created_at)`: 59 ms | range: 1.1 ms |
| Latest 20 orders | no index: 137 ms | B-tree: 0.04 ms |
| One customer's orders in a month | `(created_at)`: 9.8 ms | `(customer_id, created_at)`: 0.08 ms |
| One day's orders | 43 MB B-tree: 1.1 ms | 24 kB BRIN: 2.4 ms |

## Reproduce it

The script creates the same table with the same data: the seed makes the random numbers the same every time. The measurements ran on Docker's `postgres:17-alpine` image.

```sql
SET TIME ZONE 'America/Argentina/Buenos_Aires';
SELECT setseed(0.42);

CREATE TABLE orders (
    id          bigserial PRIMARY KEY,
    customer_id int NOT NULL,
    total       numeric(12, 2) NOT NULL,
    status      text NOT NULL,
    created_at  timestamptz NOT NULL
);

INSERT INTO orders (customer_id, total, status, created_at)
SELECT 1 + (random() * 9999)::int,
       round((random() * 100000)::numeric, 2),
       'delivered',
       timestamptz '2025-10-01 00:00:00-03' + n * interval '15.768 seconds'
           + random() * interval '10 seconds'
FROM generate_series(1, 2000000) n;

VACUUM ANALYZE orders;

EXPLAIN ANALYZE SELECT count(*), sum(total) FROM orders
WHERE created_at >= '2026-04-29' AND created_at < '2026-04-30';
```

Then create the index, repeat the `EXPLAIN ANALYZE` and try the other ways: `DATE(created_at)`, the `(customer_id, created_at)` index and `USING brin`. The times change with the machine. What each query reads does not.
