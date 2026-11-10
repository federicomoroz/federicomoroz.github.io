---
layout: manual
manual: costos-y-reportes
title: "Costs and reports · Fornu manual"
description: "What to review in prices and recipes, the cost sheet of each product and stock item, the margin on each channel and how it is worked out, menu statistics, the sales summary and profitability."
permalink: /en/projects/fornu/manual/costos-y-reportes/
---

Costs and Reports are two account modules, each with its own group. **Costos** (costs) looks at the menu: what each product costs and what it leaves on each channel, whether it sells or not. **Reportes** (reports) looks at what happened: how much was sold and how much was left. On a phone, Costos sits under **Más** (more) and Reportes is in the bottom bar. If the account does not have a module switched on, its group does not appear.

## To review {#revisar}

This is the list of what deserves a look in costs and prices: an ingredient with no price, a product that loses money on Rappi, a price nobody has touched in months. What is wrong comes first, then what is worth checking. It is the place to start whenever suppliers change their prices.

<p class="perm"><span>Who can:</span> <span class="tag">Costos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/costos-revisar.jpg' | relative_url }}" alt="Para revisar with zero problems, zero warnings and zero reminders, and the message that there is nothing to review" loading="lazy" width="1440" height="400">
  <ol class="marks">
    <li><b>Problemas</b> (problems): numbers that are wrong or missing.</li>
    <li><b>Avisos</b> (warnings): numbers that are fine but worth a look.</li>
    <li><b>Recordatorios</b> (reminders): old prices and notes.</li>
    <li>The list. Here it is empty: «Nada para revisar: todos los insumos tienen precio y todos los productos dejan lo que tienen que dejar.» (nothing to review: every item has a price and every product leaves what it should).</li>
  </ol>
  <figcaption>The demo with its menu up to date.</figcaption>
</figure>

The screen's title is **Para revisar** (to review). Tapping a figure filters the list. At the top you also have **Todo** / **Problemas** / **Avisos** / **Recordatorios** and the search box **Buscar producto o insumo…** (search product or item).

Each row shows the name and, below it, the business unit or what kind of item it is (**Ingrediente**, **Elaboración** for prepared items, **Inventario** for supplies, or **Unidad de negocio**). Next to it, what is going on, and two buttons: **Ficha** (cost sheet), which opens the [cost sheet](#ficha), and **Corregir** (fix), which opens exactly the form that fixes it: the product's recipe or prices in Carta, the item in Insumos, or the unit's extras in Unidades de negocio.

| Level | What it says | What is going on |
|---|---|---|
| Problem | «Falta el precio» (price missing) | A bought item has no price. |
| Problem | «Sin receta» (no recipe) | A prepared item, or an active product, has no recipe. |
| Problem | «Harina no tiene precio» (flour has no price) | A prepared item uses an item with no price. |
| Problem | «Sin precio» (no price) | A product on the menu is priced at 0. |
| Problem | «Pierde $X por unidad en Rappi» (loses $X per unit on Rappi) | The margin on that channel is negative. |
| Warning | «$X debajo del sugerido en Rappi» ($X below the suggested price) | It makes money, but less than it should. |
| Warning | «Lleva Cheddar, que está desactivado» (uses Cheddar, which is switched off) | It uses a switched-off item, in its recipe or its extras. |
| Reminder | «Precio de hace N días» (price from N days ago) or «Precio sin fecha» (undated price) | The price is older than Ajustes › Configuración, **Un precio es viejo a los (días)** (a price is old after N days). |
| Reminder | «Tiene una nota» (has a note) | The item has a note. |

When it happens on several channels, it goes on one line: «Pierde $ 620 por unidad en Rappi, $ 410 en PedidosYa».

### Fixing a problem

1. Tap the **Problemas** figure.
2. On the row, tap **Corregir**. The right form opens.
3. Enter what is missing and save. Once the number is right, the row drops off the list.
{: .steps}

Two more places flag it: at the top, Costos shows a number with the problems to review, and on the home page, **Para atender** (needs attention) says «N problemas de precios o recetas para revisar». Both count problems only, not warnings or reminders.

## Cost sheet {#ficha}

Everything about one product or one stock item on one screen: what it costs, what it leaves on each channel, what it is made of and where it is used. Use it to understand a number before you change a price.

<p class="perm"><span>Who can:</span> <span class="tag">Costos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/costos-ficha.jpg' | relative_url }}" alt="Cost sheet of the Doble cheddar from Doble Smash: recipe cost 3,177.35 pesos, 35% markup on cost, lowest margin 45.9% on Rappi, the prices per channel table and one bar per channel" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li><b>Producto</b> / <b>Insumo</b> (product / stock item), and which one to see.</li>
    <li>The name, unit and category, and anything to review. Here, «Sin nada para revisar» (nothing to review).</li>
    <li><b>Editar producto</b> (edit product) and <b>Receta</b> (recipe): change it without going to look for it.</li>
    <li>The figures: cost, markup on cost, the lowest margin and on how many channels it sits below the suggested price.</li>
    <li><b>Precios por canal</b> (prices per channel): price, what the channel keeps, extras, margin and suggested price.</li>
    <li>How the price splits on each channel.</li>
  </ol>
  <figcaption>A demo product's cost sheet.</figcaption>
</figure>

The tab says **Ficha**.

### A product's sheet

- **Costo de la receta** (recipe cost), or «Sin receta» if it has none.
- **Ganancia sobre el costo** (markup on cost): the product's own, or «la de la cuenta» (the account's).
- **Margen más bajo** (lowest margin), with the channel where it happens.
- **Debajo del sugerido** (below suggested): on how many channels.
- **Precios por canal**: one row per channel with **Precio**, **Se queda el canal** (what the channel keeps), **Adicionales** (extras), **Margen** ($ and %) and **Sugerido** (suggested). Below, one bar per channel split into **Receta**, **Adicionales**, **Se queda el canal**, VAT (on a registered VAT payer account) and **Margen** or **Pérdida** (loss).
- **Receta**: each item with its quantity, its cost and its share of the cost. Tap one to open its sheet.
- **Adicionales**: what goes with the product besides the recipe (the box, the bag), per channel, and whether it goes with each unit, once per order, or belongs to the product.

The picker lists the products sold on their own, grouped by business unit. Stock items are grouped by category.

### A stock item's sheet

- At the top, its group, category and supplier, its note and anything to review, with **Editar insumo** (edit item).
- If it is bought: **Precio por** (price per) the unit it is bought in (exempt, with 21% VAT or without 21% VAT), **Costo utilizable** (usable cost: what the part you actually use costs, with its yield), **Precio desde** (price since: today or N days ago) and **Último cambio** (last change).
- If it is prepared: **Costo de la tanda** (batch cost), **Costo utilizable**, **Se usa en** (used in: how many places) and the **Receta de la tanda** (batch recipe).
- **Se usa en**: every product, prepared item or extra that uses it, with the quantity, the cost and its share of that recipe.
- **Historial de precios** (price history, for bought items): the last 60 changes with date, price, VAT, how much it changed, where it came from (**Alta** created, **Editado** edited, **Compra** purchase, **Compra en Stock** purchase from stock, **Cambio masivo** bulk change, **Compra anulada** voided purchase) and who did it.

<div class="callout tip"><p class="callout-title">Tip</p><p>When a supplier raises a price, open the item's sheet and look at <b>Se usa en</b>: that is every product whose margin just moved. You can also get there from Carta: each product's margin links to its sheet.</p></div>

## Margins per channel {#margenes}

This is a business unit's whole menu with what each product leaves on each channel. At a glance you see what is too cheap on Rappi, what fell below the suggested price and what has no recipe.

The tab says **Márgenes** and the title **Márgenes por canal** (margins per channel).

<p class="perm"><span>Who can:</span> <span class="tag">Costos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/costos-margenes.jpg' | relative_url }}" alt="Doble Smash margins: one column per channel with its commission, and for each product the price, the margin in pesos and percent, and the extras" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li>One tab per business unit.</li>
    <li><b>¿Cómo se calcula?</b> (how is it worked out?): the formula, explained.</li>
    <li>Each channel with what it keeps: «comisión 25%».</li>
    <li>One cell: price, margin in pesos and percent, and extras. Tap it to see the sum.</li>
  </ol>
  <figcaption>Doble Smash's margins in the demo.</figcaption>
</figure>

The table has **Producto**, **Costo** («Sin receta» if missing) and one column per channel the unit sells on. Each channel shows what it keeps: «comisión X%», plus «$Y por unidad» if it charges a fixed fee per unit. Products are grouped by category, and inactive ones are dimmed.

Each cell shows the price, the margin («$ 5.279,65 · 45,9%»), «adicionales $X» and, if the price is under the suggested one, «sugerido $X» in orange. Tapping a cell (or hovering over it) opens the full sum, titled «Doble cheddar en Rappi»:

| Line | Example: Doble cheddar on Rappi |
|---|---|
| **Precio** | $ 11.500 |
| **Se queda el canal** | −$ 2.875 (25% of $ 11.500) |
| **Receta** | −$ 3.177,35 |
| **Adicionales** | −$ 168 |
| **Margen** | $ 5.279,65 (45,9%) |
| **Sugerido** | $ 5.943,24, con 35% sobre el costo (with 35% on cost) |

The demo account is a monotributo. On a registered VAT payer account there is also a **Sin IVA** (before VAT) line under the price. On a phone each cell shows only the price and the percentage, and the rest is a tap away.

### How the margin is worked out

**¿Cómo se calcula?** sums it up: «Precio sin IVA (21%), menos lo que se queda el canal, el costo de la receta y los adicionales: lo que lleva cada unidad, más su parte de lo que lleva cada pedido. En naranja, los precios por debajo del sugerido. Tocá un margen para ver la cuenta.» (price before 21% VAT, minus what the channel keeps, the recipe cost and the extras: what goes with each unit plus its share of what goes with each order. In orange, prices below the suggested one. Tap a margin to see the sum). On a monotributo account it starts with «Precio completo (sin IVA de venta, como monotributo)» (full price, no sales VAT, as a monotributo).

- **Margin** = price before VAT − what the channel keeps − recipe − extras.
- **What the channel keeps** is its commission on the full price, the one the customer pays with VAT, plus its fixed fee per unit if it has one. Each channel's commission and fee are set in Ajustes › Unidades de negocio.
- **Extras** are what goes with each unit (the burger box) plus a share of what goes with each order (the bag, the sticker), spread across the products of an average order on that channel.
- The margin **%** is over the price before VAT.

On a registered VAT payer account, the same Doble cheddar at $ 11.500 on Rappi would work out like this: before VAT it is $ 9.504,13, the channel keeps $ 2.875 (25% of the price with VAT), and the margin is $ 9.504,13 − $ 2.875 − $ 3.177,35 − $ 168 = $ 3.283,78, or 34,6%.

### How the suggested price is worked out

The suggested price is the one that leaves the markup you want after paying for everything. It is built like this: the recipe cost plus the **Ganancia sobre el costo**, plus extras and the channel's fixed fee, turned into a price that, after VAT and commission, leaves exactly that amount.

For the Doble cheddar on Rappi: $ 3.177,35 plus 35% is $ 4.289,42. With $ 168 of extras, $ 4.457,42. Since Rappi keeps 25%, the price has to be $ 4.457,42 ÷ 0,75 = $ 5.943,24. On own orders, with no commission, the suggested price is $ 4.457,43.

The markup is the product's own if it has one, or the one in Ajustes › Configuración, **Ganancia sobre el costo (%)**: «Lo que el precio sugerido le suma al costo de cada producto, si no tiene una propia.» (what the suggested price adds to each product's cost, if it has none of its own).

## Statistics {#estadisticas}

What the margins of the whole menu say together: how much they leave on average, which products leave the most and the least, how each price splits, and how stock item prices moved. Use it to review the whole menu at once, before a price update for example.

The tab says **Estadísticas**.

<p class="perm"><span>Who can:</span> <span class="tag">Costos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/costos-estadisticas.jpg' | relative_url }}" alt="Statistics for the whole menu: 52.9% average margin, 33 readable prices, none below the suggested price, the margin per product chart, the donut of how prices stand and the bars of how the price splits per channel" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li>What to look at: all units or one, all channels or one.</li>
    <li>The menu's figures.</li>
    <li><b>Margen por producto</b> (margin per product), from highest to lowest.</li>
    <li><b>Cómo están los precios</b> (how prices stand): fine, below suggested, losing money, or missing a price or recipe.</li>
    <li><b>Cómo se reparte el precio</b> (how the price splits), on average, on each channel.</li>
  </ol>
  <figcaption>Statistics for the demo's four brands together.</figcaption>
</figure>

**Figures**: **Margen promedio** (average margin), **Deja por unidad** (left per unit, on average), **Precios para leer** (readable prices: how many have everything needed to work out, out of how many), **Debajo del sugerido**, **Pierden plata** (losing money) and **Sin precio o receta** (no price or recipe).

**Charts**:

- **Margen por producto**.
- **Cómo están los precios**: **Bien** (fine), **Debajo del sugerido**, **Pierden plata** and **Sin precio o receta**.
- **Cómo se reparte el precio**: average per channel.
- **Contra el precio sugerido** (against the suggested price): how far above or below the suggested price each one is.
- **Margen por categoría** (margin per category).
- **Precios de los insumos, mes a mes** (stock item prices, month by month): the average change of the items whose price changed, over the last 12 months.

**Top-five lists**, where tapping a row opens its sheet: **Los que más dejan** (leave the most), **Los que menos dejan** (leave the least), **Más debajo del sugerido** (furthest below suggested), **Insumos que más subieron** (items that rose the most) and **Insumos que más se usan** (most used items).

<div class="callout"><p class="callout-title">Good to know</p><p>The averages are plain averages: each product on each channel counts the same, whether it sold a lot or a little. Only active units and products on the menu are included. For what was actually sold and what it left, see <a href="#rentabilidad">Profitability</a>.</p></div>

## Sales summary {#resumen}

How a period went compared with the previous one of the same length: how much was sold, on which days and at what time, through which channels and brands, and what sells best.

The tab says **Resumen** and the title **Resumen de ventas** (sales summary).

<p class="perm"><span>Who can:</span> <span class="tag">Reportes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/reportes-resumen.jpg' | relative_url }}" alt="Sales summary for last week against the week before: 2,911,600 pesos, 165 orders, average ticket, sales per day and cancellations, each with its change, and the chart of sales and orders per day" loading="lazy" width="1440" height="808">
  <ol class="marks">
    <li>The period. It starts on <b>Últimos 7 días</b> (last 7 days).</li>
    <li>What it is compared with: «Se compara con…», the same number of days just before.</li>
    <li>The figures, each with its change.</li>
    <li><b>Evolución de las ventas</b> (sales over time): the bars are each day's sales and the line is the number of orders.</li>
  </ol>
  <figcaption>A demo week against the one before.</figcaption>
</figure>

**Figures**: **Ventas** (sales), **Pedidos** (orders), **Ticket promedio** (average ticket), **Venta por día** (sales per day: the total divided by the days in the period) and **Cancelados** (how many, and for how much). Each says how much it changed: «↑ +3,1 % vs. período anterior» (vs. the previous period). Green is good news and red is bad. For **Cancelados**, going down is good, so −30% shows in green. If there was nothing before, it says «Sin datos del período anterior» (no data for the previous period).

Further down, the charts:

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/reportes-resumen-graficos.jpg' | relative_url }}" alt="Summary charts: sales by weekday, sales by hour with a midday and an evening peak, channels, business units and the ten best-selling products" loading="lazy" width="1440" height="1000">
  <figcaption>Which days, what time, through where and what sells best.</figcaption>
</figure>

- **Por día de la semana** (by weekday): which days sell the most.
- **Por hora** (by hour): when orders come in, by the kitchen's clock.
- **Canales** (channels): how much came in through each channel, with its share and its orders.
- **Unidades de negocio**: what each brand sold.
- **Lo más vendido** (best sellers): the ten products with the most units, with how many and for how much.

A sale here is any confirmed order that was not cancelled, including those still being prepared. Sales include VAT. The period can span up to a year.

## Profitability {#rentabilidad}

What was really left: sales before VAT, minus what the channels kept and the stock items at each day's cost, and then each unit's own expenses and its share of the shared ones. Use it to know which brand and which channel make money, and how much.

The tab and title say **Rentabilidad** (profitability).

<p class="perm"><span>Who can:</span> <span class="tag">Reportes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/reportes-rentabilidad.jpg' | relative_url }}" alt="Profitability for this month: sales before VAT, stock cost, commissions, expenses and result, the notice that the result does not include wages, the chart of where each peso sold goes and the table per business unit" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li><b>Exportar</b>: the table to a spreadsheet.</li>
    <li>The period's figures.</li>
    <li>The wages notice.</li>
    <li><b>A dónde va cada peso vendido</b> (where each peso sold goes), for the whole kitchen and for each unit.</li>
    <li>The table per business unit. Tap one to see its detail.</li>
  </ol>
  <figcaption>The month's profitability in the demo, with a single sale.</figcaption>
</figure>

The period starts on **Este mes** (this month).

**Figures**: **Ventas sin IVA** (sales before VAT, with how many orders), **Costo de insumos** (stock cost, in % and pesos, including what was lost in cancelled orders), **Comisiones** (commissions), **Gastos** (expenses) and **Resultado** (result), or **Pérdida** (loss) if it came out negative.

### Wages

If the period has no wages at all, the screen warns: «Este resultado no incluye sueldos: en el período no hay ninguno pagado ni cargado como gasto. Se pagan en Personal › Liquidación, o se cargan en Gastos con la categoría de sueldos.» (this result does not include wages: none were paid or entered as an expense in the period. They are paid in Personal › Liquidación, or entered in Gastos under the wages category).

This happens when wages are paid outside Fornu: a bank transfer, cash out of the owner's pocket. The result then looks better than it is. There are two ways to bring them in:

- Pay them from [Staff]({{ '/en/projects/fornu/manual/personal/' | relative_url }}#liquidacion), in **Liquidación** (payroll).
- Enter them in [Gastos]({{ '/en/projects/fornu/manual/compras-y-gastos/' | relative_url }}#gastos) under a wages category. Fornu recognizes the category if its name has the word sueldo (wage) in it, like Sueldos or Sueldos de cocina.

### The chart and the table

**A dónde va cada peso vendido** has one row for **Toda la cocina** (the whole kitchen) and one per unit, split into **Insumos** (stock), **Comisiones**, **Gastos** and **Resultado**. Tap a row to see each amount.

The table has one row per unit and the **Total** at the bottom:

| Column | What it is |
|---|---|
| **Pedidos** (orders) | How many, and how many were cancelled. |
| **Ventas** / **Sin IVA** | Sales, with and without VAT. |
| **Comisiones** | What the channels kept. |
| **Insumos** | What the stock used cost, plus what was lost in cancellations. |
| **Contribución** (contribution) | What is left before expenses. |
| **Gastos propios** (own expenses) | Expenses charged to that unit. |
| **Compartidos** (shared) | Its share of the place's shared expenses and of waste. |
| **Resultado** | What was left, in pesos and %. |

Tapping a unit opens its detail: **Por canal** (per channel: orders, sales, commission and what each channel left), **Lo que consumió** (what it used), and **Cada producto** (each product) with **Unidades**, **Ventas**, **Dejó** (left) and **Parte** (share). Products that did not sell say «No se vendió en este período» (not sold in this period).

Further down, **Consumo de insumos** (stock consumption: each item with its quantity, its cost and how much each unit used) and **Gastos del período** (the period's expenses: each category, shared or charged to one unit), with three notes: **Mermas** (waste), **Compras de insumos** (stock purchases: «No son gasto del período: pasan a serlo cuando los pedidos usan lo que se compró.», they become an expense once orders use what was bought) and **IVA**.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/reportes-rentabilidad-consumo.jpg' | relative_url }}" alt="Stock consumption with quantity, cost and split per business unit, and the period's expenses with one shared category and the notes on waste, stock purchases and VAT" loading="lazy" width="1440" height="520">
  <figcaption>What was used and what was spent in a demo month.</figcaption>
</figure>

<div class="callout tip"><p class="callout-title">Tip</p><p>Shared expenses and waste are split among units by what each one sold before VAT (in equal parts if none sold). An order cancelled after it was confirmed is a loss for its unit, because its stock was already used.</p></div>

<div class="callout"><p class="callout-title">Good to know</p><p>The <b>Insumos</b> column uses what each item cost when it left the stock. <b>Dejó</b>, in each product's detail, uses today's costs. If prices changed during the period, the two numbers will not match, and that is expected.</p></div>

### Exporting

**Exportar** downloads a spreadsheet with one row per unit plus the total (orders, cancelled, sales, sales before VAT, commissions, stock, lost in cancellations, contribution, own expenses, shared expenses and result), followed by the consumption of each item with its quantity, unit and cost. The spreadsheet keeps the cents. The screen shows whole pesos.

### What Reports adds to the home page

People with Reportes see the **Cómo te fue** (how it went) card on the home page: **Ventas** against the previous period, **Resultado** (the share of sales before VAT that was left), **Pedidos** with the average ticket, and **Cancelados**. Below that, the wages notice when it applies and a table with each unit per channel.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/reportes-inicio.jpg' | relative_url }}" alt="The Cómo te fue card on the home page: the wages notice, a table with what each brand sold and left on own orders and on Rappi, each brand's result, and the Resumen de ventas and Rentabilidad buttons" loading="lazy" width="1440" height="628">
  <ol class="marks">
    <li>The wages notice.</li>
    <li>What one brand sold on one channel, and what it left («deja»).</li>
    <li>Each brand's <b>Resultado</b>, after its expenses.</li>
    <li><b>Resumen de ventas</b> and <b>Rentabilidad</b>, to see more.</li>
  </ol>
  <figcaption>The demo's home page: four brands on own orders and on Rappi.</figcaption>
</figure>

«Deja: lo vendido sin IVA, menos la comisión del canal y los insumos de esos pedidos. El resultado además resta los gastos de la unidad y su parte de los compartidos.» (what it leaves: sales before VAT, minus the channel's commission and the stock those orders used. The result also takes off the unit's expenses and its share of the shared ones).
