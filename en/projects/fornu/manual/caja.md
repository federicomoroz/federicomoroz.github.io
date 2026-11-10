---
layout: manual
manual: caja
title: "Cash and sales · Fornu manual"
description: "The sales list and all its filters, cash going in and out of the drawer, and how the drawer is opened, counted and closed, blind if you want."
permalink: /en/projects/fornu/manual/caja/
---

All of this lives in the **Balances** group. On a phone, Balances sits under **Más** (more). The place's expenses are in Balances too, but they are covered in [Purchases and expenses]({{ '/en/projects/fornu/manual/compras-y-gastos/' | relative_url }}#gastos).

## Choosing the period {#periodo}

Sales, cash movements, invoices, the sales summary and profitability all share the same date picker. Pick a period once and it follows you from screen to screen for as long as the browser tab stays open.

| Button | What it covers |
|---|---|
| **Hoy** (today) | The kitchen's business day, which does not always end at midnight (see below). |
| **Ayer** (yesterday) | The previous business day. |
| **Semana pasada** (last week) | Monday to Sunday of the previous week. |
| **Últimos 7 días** (last 7 days) | The seven full days up to yesterday. |
| **Este mes** (this month) | From the 1st of the month to today. |
| **Mes pasado** (last month) | The whole previous month. |
| **Desde** / **Hasta** (from / to) | Any other range, with two dates. |

- **Hoy** is the kitchen's day. In Ajustes › Configuración, **El día empieza a las** (the day starts at) sets when it begins: if it starts at 6, at one in the morning the night's sales still count as today. See [Settings]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#configuracion).
- The buttons are relative: come back tomorrow with **Ayer** selected and you get tomorrow's yesterday.
- Each screen opens on its usual period (Sales on **Hoy**, Profitability on **Este mes**) only the first time. After that, your last choice wins.
- On a phone the dates hide behind **Otras fechas** (other dates).

## Sales {#ventas}

This is the list of everything that was sold: each sale with its channel, its time, who served it and how it was paid. It answers the everyday questions: how much came in by QR, what Lucía took on the night shift, how much the patio brought in, what was cancelled and why. Tap a sale and you see its whole story, from the moment it came in until it was paid.

It shows the confirmed orders of the period, including those still being prepared and tables still open. Cancelled sales are kept apart. The period can span up to 92 days. Beyond that, Fornu answers «Elegí hasta 92 días. Para períodos más largos está el Resumen de ventas.» (pick up to 92 days; for longer periods there is the sales summary).

<p class="perm"><span>Who can:</span> <span class="tag">Caja</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-ventas.jpg' | relative_url }}" alt="The Ventas screen with the period picker, the filters, five figures (3 orders sold, 13,500 pesos), Más info open with Efectivo and Por cobrar, and a list of table sales not yet invoiced" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li><b>Hoy · Ayer · …</b>: the period. Below it, the search box for customer, order number or platform code.</li>
    <li>The filters. Only the ones that make sense for your place appear: with no waiters there is no <b>Atendió</b> (served by), with no tables there is no <b>Mesa</b> (table).</li>
    <li>The figures for whatever the filters leave. <b>Pedidos vendidos</b> (orders sold) and <b>Cancelados</b> (cancelled) switch the list below.</li>
    <li><b>Más info</b> (more info): how much came in by each payment method, tips, discounts and cancellation reasons.</li>
    <li><b>Comprobante</b> (receipt): whether the sale is invoiced, and with which invoice.</li>
    <li><b>Exportar</b> (export): downloads the list as a spreadsheet.</li>
  </ol>
  <figcaption>Today's sales in the demo's test kitchen.</figcaption>
</figure>

### Finding a sale

Type into **Cliente, número o código…** (customer, number or code). It finds the exact order number (with or without #), the customer's name or the code the platform gave the order.

### Filtering the list

| Filter | What it shows | When it appears |
|---|---|---|
| **Canal** (channel) | **Pedidos propios** (own orders), **Rappi**, **PedidosYa** or **Salón** (dining room). | Only channels the account has switched on. |
| **Unidad de negocio** (business unit) | One of your brands. | Always. |
| **Medio de pago** (payment method) | One method, or **Todo menos efectivo** (everything but cash, see below). | Always. |
| **Atendió** (served by) | What one waiter served. | When some sale has a waiter. |
| **Sector** | One area of the dining room: patio, terrace, main room. | With two or more areas. |
| **Mesa** (table) | One table. | When there are tables. |
| **Arqueo** (cash count) | What was paid or cancelled while one drawer session was open, that is, what that drawer has to account for. Each session reads like «10/11 12:00 → 23:40», or «→ abierta» (open) if it still is. | For people with Caja. Shows the last 30. |
| **Comprobante** (receipt) | **Facturadas** (invoiced) or **Sin facturar** (not invoiced). | Always. |
| **Turno** (shift) | **Mañana (6 a 12)**, **Mediodía (12 a 16)**, **Tarde (16 a 20)** or **Noche (20 a 6)**: morning, midday, afternoon, night. Fills both hours in one tap. | Always. |
| **Desde las** / **Hasta las** (from / until) | A range of hours by hand. It can cross midnight: 20 to 2 means 8 pm to 2 am. | Always. |

Once you pick hours, **Abiertas** / **Cerradas** (opened / closed) appears. With **Abiertas**, the default, the filter reads the hour the sale was opened. With **Cerradas**, the hour it was paid or cancelled. That separates, for example, the tables seated before 11 pm from the ones paid after it.

Whenever a filter or a search is on, **Sacar filtros** (clear filters) appears. It clears everything except the period.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-ventas-filtro.jpg' | relative_url }}" alt="Sales filters with Medio de pago set to Todo menos efectivo, the Arqueo filter, the Sacar filtros link and a single sale paid by debit card left in the list" loading="lazy" width="1440" height="535">
  <ol class="marks">
    <li><b>Medio de pago</b> set to <b>Todo menos efectivo</b>.</li>
    <li><b>Arqueo</b>: pick a drawer session to see only what happened while it was open.</li>
    <li><b>Sacar filtros</b>: back to the whole period.</li>
    <li>The card sale stays. The cash sale is gone.</li>
  </ol>
  <figcaption>Everything not paid in cash, ready to invoice at the end of the day.</figcaption>
</figure>

**Todo menos efectivo** gathers what the platform collected, cards, QR, transfers, Mercado Pago and anything **Pagado antes** (paid in advance). It leaves out anything with cash in it (even as part of a split payment), anything **Por cobrar** (still to collect) and anything marked **Sin dato** (no data). It is the filter for places that invoice, at the end of the day, whatever left a trace at the bank.

<div class="callout tip"><p class="callout-title">Tip</p><p>The usual questions each have their filter. How much did the night shift sell? <b>Turno</b> › <b>Noche (20 a 6)</b>. What does today's drawer have to account for? <b>Arqueo</b> › the open session. What did Martín serve on the patio? <b>Atendió</b> › Martín and <b>Sector</b> › Patio.</p></div>

### Reading the figures and Más info

- **Pedidos vendidos** (orders sold): how many sales there were. Tap it to see the sold list.
- **Ventas** (sales): the total taken, in whole pesos.
- **Ticket promedio** (average ticket): what each sale brings in on average.
- **Cancelados** (cancelled): how many were cancelled. Tap it and the list switches to the cancelled sales, with a **Motivo** (reason) column. Tap it again to go back.
- **Comensales** (guests): shows up when people were seated, with what each one spent («$ 1.500 por comensal», per guest).

They all count only what the filters leave. Cancelled sales never add to **Ventas**.

**Más info** opens with a tap and shows one card per way of paying, with the total and how many sales. Tapping a card filters by it, and tapping it again removes the filter. That is also how you reach **Varios medios** (split payments), **Por cobrar** and **Sin dato**, which are not in the dropdown above. The **Varios medios** card also says how much came in by each method, without tips.

With two or more areas you also get **Por sector** (by area), one card per area, which filter too. Below them, three facts: **Propinas** (tips), **Cortesías y descuentos** (comps and discounts, «$X en N ventas») and **Cancelaciones** (cancellations), with each reason and how many times it happened.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-ventas-mas-info.jpg' | relative_url }}" alt="Más info open: an Efectivo card, a Varios medios card with 4,500 in cash and 4,500 by debit card, and Por sector cards for Patio and Salón" loading="lazy" width="1440" height="400">
  <ol class="marks">
    <li><b>Comensales</b>: 4 people seated, 4,500 pesos each.</li>
    <li><b>Varios medios</b>: one bill paid half in cash and half by debit card.</li>
    <li><b>Por sector</b>: what each area of the dining room brought in.</li>
  </ol>
  <figcaption>Más info on a day with two tables, one on the patio and one inside.</figcaption>
</figure>

### Reading the list

| Column | What it says |
|---|---|
| **#** | The order number. |
| **Día y hora** (day and time) | When it was opened. |
| **Unidad de negocio** | The brand, the channel and, for platform orders, the platform's code. |
| **Cliente** (customer) | Whose name it is under, or the table. |
| **Atendió** | Table, waiter and guests, for example «Mesa 4 · Lucía · 3 comensales». Only when there are waiters. |
| **Medio de pago** | The method, **Por la plataforma** (paid through the platform), **Varios medios**, **Por cobrar** or **Sin dato**, plus the tip if there was one. |
| **Total** | What was charged. |
| **Comprobante** | A green **Facturada · Factura B 00003-00000012** (invoiced, with its number), or **Sin facturar** (not invoiced) with the reason beside it: (anulada) voided, (esperando a ARCA) waiting for ARCA, (pedida: motivo) requested, with the reason, or (rechazada) rejected. A cancelled sale shows «—». |

Cancelled rows are dimmed. The list draws 200 sales at a time: to see the rest, tap **Ver N más de M** (see N more of M) at the bottom.

### Seeing everything that happened to a sale

1. Tap the sale in the list.
2. Its detail opens on the right (on small screens it takes the whole screen): channel, status, what was ordered with the total, the customer and their phone, delivery, note, payment and, if the account invoices, the invoice.
3. Below is the full story, step by step and with times: when it came in, when it was confirmed, each round sent to the kitchen, who took the payment and how much, when it was invoiced.
4. With the detail open, the <kbd>↑</kbd> and <kbd>↓</kbd> keys move to the previous or next sale without closing anything.
5. Close it with the X.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-ventas-detalle.jpg' | relative_url }}" alt="Detail of Doble Smash order 2 open beside the list: one portion of fries for 4,500 pesos and the sale's story from arrival to delivery" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li>The order and its brand. The X closes it.</li>
    <li>What was ordered and the total.</li>
    <li>The story: in, confirmed, table seated, round sent to the kitchen, paid in cash, delivered.</li>
  </ol>
  <figcaption>A demo table, start to finish.</figcaption>
</figure>

The arrow keys do nothing while you are typing in a field or have a dialog open.

### Exporting

**Exportar** downloads a spreadsheet (a CSV file) with the list you are looking at: sold or cancelled, with your filters on and every row, not just the 200 drawn. It opens cleanly in Excel set to Spanish.

It has the day, time, number, business unit, channel, platform code, customer, waiter, area, guests, payment method (a split payment reads «Efectivo 5000 + QR 3000»), tip, comp, total, receipt, status and cancellation reason. The button is off when the list is empty.

### Invoicing what was left uninvoiced

If the account invoices, a **Facturar N sin facturar** (invoice N uninvoiced) button appears under the figures. It issues one final-consumer invoice for each sale in the list that does not have one yet. The usual move is to filter **Todo menos efectivo** and press it at the end of the day. It is explained in [Electronic invoicing]({{ '/en/projects/fornu/manual/facturacion/' | relative_url }}#fin-del-dia).

### On a phone

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/caja-ventas-telefono.jpg' | relative_url }}" alt="Sales on a phone in dark mode: a full-width Exportar button, the period with the Otras fechas link, the Filtros button and the figures in two columns" loading="lazy" width="390" height="844">
  <figcaption>Sales on a phone. The filters wait behind <b>Filtros</b>.</figcaption>
</figure>

On a phone the filters fold behind **Filtros** (filters), which shows how many are on. The dates hide behind **Otras fechas**, the figures go in two columns and each sale becomes a card with the customer's name next to the number («#12 · Juan»).

## Cash movements {#movimientos}

This is the drawer's ledger: what goes in and out of it. Plenty of entries write themselves: a courier handing over cash, an expense paid in cash, a table paid in cash, an advance or a wage paid in cash, the difference found by a cash count. The rest you enter yourself: the change put in each morning, what the owner takes out, tips handed out.

The tab says **Movimientos** and the screen title says **Movimientos de caja** (cash movements). On the shared tablet it is the **Movimientos** tab for anyone who logs in with their PIN and has Caja.

<p class="perm"><span>Who can:</span> <span class="tag">Caja</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-movimientos.jpg' | relative_url }}" alt="Today's cash movements: 30,000 pesos in the drawer according to the system, 50,000 in as the opening balance and 20,000 out as an advance to an employee" loading="lazy" width="1440" height="560">
  <ol class="marks">
    <li><b>Egreso</b> (money out) and <b>Ingreso</b> (money in): enter cash leaving or coming in.</li>
    <li><b>Efectivo en la caja ahora</b> (cash in the drawer now): what should be there according to the system.</li>
    <li><b>Origen</b> (source): where each movement came from.</li>
  </ol>
  <figcaption>A day that started with 50,000 pesos and paid a 20,000 advance out of the drawer.</figcaption>
</figure>

Three figures sit at the top. **Efectivo en la caja ahora** is what should be in the drawer right now. **Ingresos del período** and **Egresos del período** (money in and out for the period) add up everything that came in and went out in the chosen dates, whatever the method. The period starts on **Hoy** and can span up to a year.

Each row shows **Cuándo** (when), the **Concepto** (description, with the note and who entered it), the **Medio** (method), the **Origen** and the amount under **Ingreso** or **Egreso**.

| Origen | Where it comes from | How to fix it |
|---|---|---|
| **A mano** (by hand) | Someone entered it with **Ingreso** or **Egreso**. | With **Anular** (void), until the drawer is counted again. |
| **Rendición** (handover) | A courier handed over the cash of their orders: «Rendición de Martín», with how many orders. | Not from the drawer screen. |
| **Gasto** (expense) | An expense paid in cash. The source links to Gastos. | From Gastos. |
| **Personal** (staff) | An advance or a wage paid in cash. | From Personal. |
| **Mesa** (table) | A table's cash payment and tip: «Cobro de …», «Propina de …». | If the payment is undone, an «Anulado: …» entry appears. |
| **Arqueo** (cash count) | The **Saldo inicial** (opening balance), and the surplus or shortfall found when opening or closing. | The next count corrects it. |

Only cash comes in from tables. Card, QR and transfer payments go straight into what the cash count expects for that method.

### Entering money in or out

1. Tap **Ingreso** if money comes in or **Egreso** if it goes out.
2. Under **Cuánto** (how much), type the amount.
3. **Medio** stays on **Efectivo** (cash), which moves cash in the drawer. Pick another method and the amount adds to what the cash count expects for that method instead.
4. Fill in **De dónde viene** (where it comes from) or **Para qué sale** (what it's for), up to 80 characters. As you type, Fornu suggests «Cambio para la caja» (change for the drawer), «Aporte del dueño» (owner's contribution), «Cobro de una deuda» (debt collected) or «Propinas» (tips) for money in, and «Retiro del dueño» (owner's withdrawal), «Cambio para un mensajero» (change for a courier), «Pago en el momento» (paid on the spot) or «Propinas repartidas» (tips handed out) for money out.
5. Add a **Nota (opcional)** (note) if it helps.
6. Tap **Guardar** (save) or press <kbd>Ctrl</kbd> + <kbd>Enter</kbd>. You get «Ingreso anotado» or «Egreso anotado» (recorded).
{: .steps}

If **Guardar** stays off, the dialog footer says what is missing: «Poné cuánta plata es» (enter the amount), «Decí de dónde viene» or «Decí para qué sale».

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-egreso.jpg' | relative_url }}" alt="The Egreso de la caja dialog with the Cuánto, Medio (set to Efectivo), Para qué sale and Nota fields, and the reminder to enter business expenses in Gastos" loading="lazy" width="619" height="430">
  <figcaption>Money out. The line at the bottom says where business expenses belong.</figcaption>
</figure>

<div class="callout"><p class="callout-title">Good to know</p><p>If the money pays for a business expense (vegetables, gas, a repair), enter it in <a href="{{ '/en/projects/fornu/manual/compras-y-gastos/' | relative_url }}#gastos">Gastos</a> as paid in cash. It leaves the drawer on its own and also counts in profitability. A hand-entered <b>Egreso</b> does not count as an expense.</p></div>

### Voiding a movement

1. On the movement's row, tap **Anular** (void).
2. Fornu shows «¿Anular «concepto»?» with the amount, method and date.
3. Write **Por qué se anula** (why it is voided), for example «Lo cargué dos veces» (I entered it twice).
4. Tap **Anular**. You get «Movimiento anulado».
{: .steps}

The movement stays in the list, dimmed, tagged **anulado** and with the reason. Movements are never edited: if an amount was wrong, void it and enter it again.

Only hand-entered movements can be voided, and only until the drawer is counted again when opening or closing it. After that Fornu answers «La caja se contó después de este movimiento: cargá otro que lo corrija.» (the drawer was counted after this movement: enter another one to correct it). Movements that come from elsewhere say where to fix them, for example «Sale de un gasto pagado en efectivo: se corrige desde Gastos.»

## Cash count {#arqueo}

This is where the drawer opens and closes. You open it by counting the cash the shift starts with. You close it by counting each payment method: the cash in the drawer, the card terminal's closing slip for cards, and what came in by QR, transfer and Mercado Pago. Fornu compares the count with what the system says and records the difference, with its cause.

The tab says **Arqueo** and the title **Arqueo de caja** (cash count). On the shared tablet it is the **Arqueo** tab for anyone who logs in with their PIN and has Caja.

<p class="perm"><span>Who can:</span> <span class="tag">Caja</span> <span class="tag">Ver lo esperado</span> <span class="tag">Recontar la caja</span></p>

With **Caja** you open, count and close. **Ver lo esperado** (see the expected amount) shows what the system expects before counting: without it, the count is blind. **Recontar la caja** (recount the drawer) lets someone count again after a count was confirmed. Both need Caja. The **Encargado/a** (manager) role comes with all three.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-arqueo.jpg' | relative_url }}" alt="Cash count with the drawer open since 9/11 at 10:26 with 30,000 pesos, the Según el sistema table per payment method and an empty list of previous closings" loading="lazy" width="1440" height="640">
  <ol class="marks">
    <li><b>Cerrar caja</b> (close the drawer). With the drawer closed it reads <b>Abrir caja</b> (open), and once a count is confirmed, <b>Ver el conteo y cerrar</b> (see the count and close).</li>
    <li>The state: <b>Abierta</b> (open), since when, who opened it and with how much.</li>
    <li><b>Según el sistema</b> (according to the system): what there should be of each method. Only people with Ver lo esperado see it.</li>
    <li><b>Cierres anteriores</b> (previous closings): the last 30 sessions, with their difference.</li>
  </ol>
  <figcaption>The open drawer, as seen by someone who can see the expected amounts.</figcaption>
</figure>

With the drawer closed, the band says **Cerrada** (closed) and «Se cerró el 10/11, 23:40. Según el sistema hay $X en efectivo.» (closed on…, the system says there is $X in cash). The very first time it says «Todavía no se abrió nunca: al abrirla, lo que cuentes es con lo que empieza.» (never opened yet: what you count when opening is what it starts with).

If couriers still hold cash they haven't handed over, the top shows «Los mensajeros todavía tienen $X de N pedidos en efectivo sin rendir: no está en la caja hasta que lo rindan.» with an **Ir a rendir** (go hand it over) link. Settle it before closing, since that money is not in the drawer yet. See [Orders and delivery]({{ '/en/projects/fornu/manual/pedidos/' | relative_url }}).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-arqueo-tablet.jpg' | relative_url }}" alt="The shared tablet with Sofía's tabs, Arqueo selected, and the Abrir caja button over a drawer that has never been opened" loading="lazy" width="1180" height="460">
  <ol class="marks">
    <li><b>Arqueo</b> and <b>Movimientos</b> on the tablet, for anyone with Caja who logs in with their PIN.</li>
    <li><b>Abrir caja</b>.</li>
  </ol>
  <figcaption>On the kitchen tablet the cashier opens and closes without leaving her session.</figcaption>
</figure>

### What «Según el sistema» means

- **Efectivo** (cash): the sum of every cash movement since opening: the opening balance, tables paid in cash, courier handovers, cash expenses and money entered in or out by hand.
- **The other methods**: own orders delivered while the drawer was open and paid with that method, plus table payments with that method (amount and tip), plus hand-entered movements with that method.

### Opening the drawer

1. Tap **Abrir caja**. The «Abrir la caja» dialog opens.
2. At the top you see **Según el sistema**: what the last closing left. The very first time it is not shown.
3. Count the cash. With **Contar el efectivo billete por billete** (count the cash note by note) ticked, enter how many notes there are of each value, from $20,000 down to $10. Each value shows its subtotal and the sum fills **Efectivo que hay** (cash on hand). Untick it to type the total directly.
4. Under the total, Fornu compares with the last closing: «Coincide con el último cierre.» (matches), «Faltan $X.» (short by $X) or «Sobran $X.» (over by $X). If it does not match, write **Por qué no coincide** (why it doesn't match), for example «El dueño retiró al cerrar» (the owner took some out at closing).
5. Tap **Abrir caja**. You get «Caja abierta».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-abrir.jpg' | relative_url }}" alt="The Abrir la caja dialog counting note by note: 3 notes of 10,000 and 4 of 1,000 add up to 34,000 pesos in cash" loading="lazy" width="880" height="690">
  <ol class="marks">
    <li><b>Efectivo que hay</b>: fills itself with the sum of the notes.</li>
    <li><b>Contar el efectivo billete por billete</b>. It comes ticked, and each device remembers if someone unticks it.</li>
    <li>Three $10,000 notes make $30,000.</li>
  </ol>
  <figcaption>The drawer's first opening: what you count is what it starts with.</figcaption>
</figure>

If the count does not match the last closing, the difference is recorded as an **Arqueo** movement, so the drawer starts with what is really there.

### Counting blind

A blind count is one done without knowing what it should come to. The cashier counts and confirms, and only then sees whether there is a surplus or a shortfall. That way nobody adjusts the count to fit what the system expects.

The **Ver lo esperado** permission decides it. Someone with Caja but without that permission counts blind, and the screen says so: «El arqueo es ciego: la diferencia se ve después de confirmar el conteo.» (the count is blind: the difference shows after confirming the count).

| | With **Ver lo esperado** | Without it (blind) |
|---|---|---|
| Open drawer | The **Según el sistema** table and the opening amount. | «Arqueo ciego: lo que espera el sistema se ve después de confirmar el conteo.» and who opened it, without the amount. |
| While counting | **Según el sistema** and **Diferencia** (difference) next to each method, as you type. | Only the **Contado** (counted) column. |
| A method the system expects at $0 | Already counts as done. | Still needs a figure, even 0. |
| Cash movements | The amounts and the cash on hand now. | «—» while the drawer is open: «se ve después de contar la caja» (shows after counting). |
| After confirming | Same as before. | Sees the difference. The count can no longer change. |

<div class="callout tip"><p class="callout-title">Tip</p><p>To make a cashier count blind, give her role <b>Caja</b> without <b>Ver lo esperado</b>. Roles are set up in <a href="{{ '/en/projects/fornu/manual/personal/' | relative_url }}#roles">Staff</a>.</p></div>

### Closing the drawer: count and confirm

1. Tap **Cerrar caja**. «Cerrar la caja · contá» (close the drawer: count) opens.
2. For each method, enter what was **Contado**: the cash in the drawer, the card terminal's closing slip for debit and credit, and what came in by QR, transfer and Mercado Pago. If nothing came in by a method, **Nada** (nothing) sets it to 0 in one tap.
3. Cash can be counted note by note, with the same grid as when opening.
4. Tap **Confirmar conteo · $total** (confirm count). If a method is missing, the footer says which: «Falta contar tarjeta de débito» (debit card still to count).
5. You get «Conteo confirmado.». The count is saved as it is and cannot be changed.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-contar.jpg' | relative_url }}" alt="The blind Cerrar la caja count dialog: only the Contado column, 3,000 pesos in cash and 0 for the other methods, and the Confirmar conteo button for 3,000" loading="lazy" width="880" height="900">
  <ol class="marks">
    <li>The blind-count notice and what to count.</li>
    <li><b>Contado</b>: one figure per payment method.</li>
    <li><b>Contar el efectivo billete por billete</b>.</li>
    <li><b>Confirmar conteo</b>, with the counted total.</li>
  </ol>
  <figcaption>A blind count: what the system expects is not shown.</figcaption>
</figure>

### Closing the drawer: the result

Once confirmed, the dialog turns into «Cerrar la caja · resultado» (result). It says who counted and when, and shows each method with **Según el sistema**, **Contado** and **Diferencia**. The difference reads in words: «Faltan $2.000» (short $2,000), «Sobran $500» (over $500) or «—» when it matches. The **Total** row says the overall shortfall or surplus, or «Coincide» (matches).

1. If any method does not match, pick **Por qué no coincide**: **Error en el vuelto** (wrong change given), **Venta sin cargar** (sale not entered), **Gasto o retiro sin cargar** (expense or withdrawal not entered), **Billete falso** (counterfeit note) or **Otro** (other).
2. With **Otro**, describe **Qué pasó** (what happened). With the other causes, the **Nota (opcional)** takes any detail.
3. Tap **Cerrar la caja**. You get «Caja cerrada.» and the closing's detail opens.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-resultado.jpg' | relative_url }}" alt="Closing result: the system expected 5,000 pesos in cash, 3,000 were counted, 2,000 are missing. Below, the causes to choose from and the Cerrar la caja button switched off" loading="lazy" width="880" height="900">
  <ol class="marks">
    <li>The difference in words: $2,000 of cash missing.</li>
    <li><b>Por qué no coincide</b>: the cause, required when the difference goes past the tolerance.</li>
    <li><b>Recontar</b> (recount), in case the count was wrong. The padlock means it asks for authorization.</li>
    <li>Why the button is off: «Elegí por qué no coincide» (choose why it doesn't match).</li>
    <li><b>Cerrar la caja</b>.</li>
  </ol>
  <figcaption>2,000 pesos short: before closing you have to say why.</figcaption>
</figure>

A cash shortfall or surplus is recorded in cash movements as «Faltante del arqueo» or «Sobrante del arqueo», and the drawer is left holding what was counted. Differences in the other methods are only written down in the closing.

If you tap **Cancelar** (cancel) after confirming, the count stays saved. The button at the top becomes **Ver el conteo y cerrar** and takes you back to the result.

### Recounting

Sometimes the count was wrong: two notes stuck together, the terminal slip that did not print. **Recontar** lets you count again, and both counts are kept.

1. In the result, tap **Recontar**. «Recontar la caja» opens. **← Volver al resultado** (back to the result) returns without changing anything.
2. Count each method again and confirm.
3. If you lack **Recontar la caja**, «Hace falta autorización» (authorization needed) appears. Under **¿Quién autoriza?** (who authorizes?) pick someone who holds it (it says «· en turno» if they are on shift), they type their PIN and tap **Autorizar**.
4. The result shows the new count and says so: «Contó Sofía (autorizó Marta) a las 12:38 · 2 conteos, quedan todos guardados.» (Sofía counted, Marta authorized, 2 counts, all kept).
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-autorizar.jpg' | relative_url }}" alt="The Hace falta autorización dialog for Recontar la caja, with Marta chosen to authorize and the keypad for her PIN" loading="lazy" width="880" height="560">
  <ol class="marks">
    <li><b>¿Quién autoriza?</b>: the people who hold the permission.</li>
    <li>Their PIN, on the keypad.</li>
  </ol>
  <figcaption>Sofía cannot recount on her own: Marta authorizes it with her PIN.</figcaption>
</figure>

If nobody at the place holds the permission, Fornu says so: «Nadie de este local puede autorizar esto con su PIN: se da en Personal → Configuración, en el rol de quien corresponda.» (nobody here can authorize this with their PIN: it is granted in Personal › Configuración, on the right person's role).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-recontado.jpg' | relative_url }}" alt="The result after recounting: two counts kept, 300 pesos of cash missing and a note that each method matches within the 500-peso tolerance" loading="lazy" width="880" height="580">
  <ol class="marks">
    <li>Who counted, who authorized and how many counts there were.</li>
    <li>$300 short, but the tolerance is $500: no cause needed.</li>
  </ol>
  <figcaption>The second count comes much closer.</figcaption>
</figure>

### The tolerance

In Ajustes › Configuración, **Tolerancia del arqueo** (cash count tolerance) sets how far a payment method can be off at closing without having to say why. With a $500 tolerance, if cash is $300 short the closing says «Cada medio coincide dentro de la tolerancia de $500.» (each method matches within the tolerance) and only offers the note. At $0, every difference needs its cause.

The tolerance applies to each method separately, not to the total.

### If money comes in after counting

If an order or a movement comes in after the count, that count no longer holds and the dialog warns «Entró plata después del último conteo: contá de nuevo.» (money came in after the last count: count again). Counting again in that case needs no permission.

The exception is a movement entered by hand after counting. Counting again then is a recount, and Fornu says so: «Después del conteo se cargó un movimiento a mano: contarla de nuevo es un recuento, con «Recontar».»

### Looking at a past closing

**Cierres anteriores** lists the last 30 sessions: **Abrió** (opened), **Cerró** (closed, with how many counts there were), **Sistema**, **Contado** and **Diferencia** with its cause. Tap one to see «Cierre del …» (closing of…):

- Who opened it, when and with how much, the difference against the previous closing with its note, and who closed it.
- The table for each method.
- How many notes of each value were counted, if it was counted note by note.
- Earlier counts, for example «Antes se contó faltan $2.000 (Sofía, 10/11, 12:38).»
- **Por qué no coincidió** (why it didn't match), with the cause and the note.

<div class="callout tip"><p class="callout-title">Tip</p><p>Open the drawer before paying anything in cash. If it is closed, Gastos, advances and wages warn «La caja está cerrada» (the drawer is closed) and ask «¿Pagar igual?» (pay anyway?), because that money would leave a drawer nobody opened and the count would not add up.</p></div>
