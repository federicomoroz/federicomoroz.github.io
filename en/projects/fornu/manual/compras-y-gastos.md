---
layout: manual
manual: compras-y-gastos
title: "Purchases and expenses · Fornu manual"
description: "How to record stock purchases that go into stock, suppliers with their tax ID and what is owed to them, the place's expenses, how to pay one or several at once and how to export them for the accountant."
permalink: /en/projects/fornu/manual/compras-y-gastos/
---

## Stock purchases {#compras}

This is where deliveries from suppliers are recorded, with their voucher. When a purchase is saved, the items go into stock, each item's price and VAT are brought up to date and, if it was paid in cash, the money comes out of the cash drawer. It also shows what is owed to suppliers, and pays them.

It lives in Compras › **Compras de insumos** (purchases › stock purchases), whose tab reads **Compras**, and comes with the Suppliers and purchases module. It is also the **Compras** tab on the shop's device.

<p class="perm"><span>Who can:</span> <span class="tag">Gastos</span></p>

The **Encargado/a** (manager) role of a new account already has it. Anyone with Gastos picks the purchase's **Proveedor** (supplier) and sees **Cargar lo de la última compra** (load the last purchase). Creating a supplier right there, with **+ Proveedor nuevo**, also takes the **Proveedores** permission.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/compras-lista.jpg' | relative_url }}" alt="The Compras de insumos list for the month, with 1,598,400 pesos in purchases and 666,000 to pay, one purchase from a meat supplier still to pay with its Pagar button and a weekly purchase paid by transfer." loading="lazy" width="1440" height="838">
  <ol class="marks">
    <li><b>Exportar</b> (export) and <b>Compra de insumos</b> (stock purchase).</li>
    <li>The period: <b>Hoy</b> (today), <b>Ayer</b> (yesterday), <b>Semana pasada</b> (last week), <b>Últimos 7 días</b> (last 7 days), <b>Este mes</b> (this month) or <b>Mes pasado</b> (last month), or the <b>Desde</b> and <b>Hasta</b> dates (from, to). <b>Ver anulados</b> (show voided) adds voided purchases.</li>
    <li><b>A pagar</b> (to pay): everything owed on purchases, whatever the period. Tap it to pay.</li>
    <li><b>Estado</b> (status): <b>A pagar</b>, <b>Vencido</b> (overdue, in red, with the date), <b>Pagado</b> (paid, with the method and date) or <b>Anulado</b> (voided, with the reason).</li>
    <li><b>Pagar</b> (pay), on the ones still owed, and the <b>⋯</b> menu with <b>Repetir compra</b> (repeat purchase) and <b>Anular</b> (void).</li>
    <li>The confirmation when a purchase is saved.</li>
  </ol>
  <figcaption>Two demo purchases, one still to pay and one paid.</figcaption>
</figure>

Each row shows the date, the supplier with the description underneath, the category with how many items went into stock, the voucher with its number, the business unit (or «Compartido», shared) and the total.

### Record a purchase {#cargar-compra}

1. Tap **Compra de insumos**.
2. Pick the **Proveedor**. If you bought from them in the last 120 days, **Cargar lo de la última compra** (load the last purchase) appears: see below.
3. Pick the **Comprobante** (voucher) and type the **Número** (number), which is required for A, B and C invoices and for credit notes.
4. Choose whether the prices you are about to type are **Precios con IVA** or **Precios sin IVA** (with or without VAT), as on the voucher.
5. Add each item with **+ Insumo** (add item): search for it by name, type the quantity in the unit it comes in (bags, boxes, kilos) and check its price and VAT.
6. Choose **Pagado** (paid), with the method and date, or **A pagar (cuenta corriente)** (to pay, on account), with the due date if there is one.
7. Tap **Guardar** (save), or press <kbd>Ctrl</kbd> + <kbd>Enter</kbd>.
{: .steps}

Fornu confirms «Compra cargada: los insumos ya están en el stock» (purchase recorded, the items are in stock).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/compras-dialogo.jpg' | relative_url }}" alt="Two parts of a stock purchase: on the left the date, supplier, category, business unit, voucher and prices with VAT. On the right three cuts of meat with their quantity, price and VAT, the amounts and payment on account." loading="lazy" width="1440" height="728">
  <ol class="marks">
    <li><b>Proveedor</b>. <b>+ Proveedor nuevo</b> (new supplier) creates one right there, with the Proveedores permission. Picking a supplier fills in their usual category.</li>
    <li><b>Unidad de negocio</b> (business unit): <b>Compartido entre todas</b> (shared by all) splits the cost across the brands by what each one sells. Or pick a single one.</li>
    <li><b>Comprobante</b> and <b>Número</b>.</li>
    <li><b>Precios con IVA</b> or <b>Precios sin IVA</b>: it starts according to the voucher, without VAT for an A invoice.</li>
    <li>The items, each with its quantity, price and VAT. Under the name it says how it is bought, such as «caja de 10 kg» (a 10 kg box).</li>
    <li><b>Pagado</b> or <b>A pagar (cuenta corriente)</b>.</li>
  </ol>
  <figcaption>The start and the end of a three-item purchase on account.</figcaption>
</figure>

| Field | What it is for |
|---|---|
| **Fecha** (date) | Starts at today. It warns if the date is in the future. |
| **Proveedor** | Who it was bought from. |
| **Categoría** (category) | Starts at **Insumos**, or at the supplier's usual category. |
| **Unidad de negocio** | **Compartido entre todas**, or one brand. |
| **Comprobante** | Factura A, B, C or X (invoice types), Ticket (receipt), Remito (delivery note, the usual one for purchases), Nota de crédito (credit note), Recibo (receipt) or Sin comprobante (no voucher). |
| **Número** | Such as 0001-00012345. Required for A, B and C invoices and for credit notes, optional for the rest. |
| **Descripción** (description) | For example «Pedido semanal de verdura» (weekly vegetable order). |
| **Insumos** (items) | Active ingredients and supplies. Each line brings the item's last price and VAT. If you type a different price, it shows how much it moved, such as «Antes $ 9.000 · +12%» (before $ 9,000, up 12%). |
| **Neto (sin IVA)** and **IVA** | Net and VAT, worked out from the lines. Under the VAT it shows how much goes to each rate. |
| **Percepciones y otros impuestos** | Withholdings and other taxes the voucher adds on top. |
| **Pago** (payment) | **Pagado**, with its **Medio de pago** (method: Efectivo cash, Transferencia, Tarjeta de débito, Tarjeta de crédito, Mercado Pago or Cheque) and **Pagado el** (paid on). Or **A pagar (cuenta corriente)**, with **Vence (opcional)** (due date). |

Each item carries its own VAT, even when the invoice is a single one. On saving, each line's price and VAT become the item's, and the margins of whatever uses it are recalculated.

<div class="callout"><p class="callout-title">Good to know</p><p>A new purchase starts as <b>Pagado</b> in <b>Efectivo</b> (cash), dated today. Saved like that, the money comes out of the cash drawer. If you will pay later, choose <b>A pagar (cuenta corriente)</b> before saving.</p></div>

A credit note brings no items. Fornu asks you to record it as an expense, and to take whatever was returned out of stock in Stock.

### Load the last purchase {#ultima-compra}

If you bought from a supplier in the last 120 days, picking them shows **Cargar lo de la última compra**, with how many items it had, its date and «a los precios de hoy» (at today's prices). Tap it before adding any lines: the same items fill in at current prices, and the payment is set as last time, paid or to pay and with the same method. Adjust the quantities and save.

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/compras-dialogo-telefono.jpg' | relative_url }}" alt="A stock purchase on a phone, with sunflower oil and still water loaded from the last purchase, each on a card with its quantity, price with VAT and VAT rate, and the total at the bottom." loading="lazy" width="390" height="844">
  <figcaption>On the shop's phone, each item in the purchase is a card.</figcaption>
</figure>

### Which products' margins moved {#margenes}

When a purchase changes an item's price, a box appears above the list after saving, for example «Cambió el precio de 2 insumos: Harina +12% · …. Toca 5 productos:» (2 items changed price, flour up 12%, affecting 5 products). A table shows each affected product with its business unit, its cost before and after, and the margin of the channel that leaves least, before and after.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/compras-margenes.jpg' | relative_url }}" alt="The box that shows after saving a purchase: Cambió el precio de 1 insumo: Carne picada 80/20 +10%. Toca 2 productos, with the Doble cheddar and the Triple bacon, their cost before and after, the margin of the channel that leaves least, and the Revisar precio button" loading="lazy" width="1440" height="290">
  <figcaption>Ground beef went up 10%: the Doble cheddar and the Triple bacon leave less.</figcaption>
</figure>

**Revisar precio** (review price) opens that product on **Precios** (prices), ready to fix ([Menu]({{ '/en/projects/fornu/manual/carta/' | relative_url }}#arreglar-precio)). If no product on sale uses those items, the box reads «No toca ningún producto a la venta.» (no product on sale is affected). Close it with the ✕.

### Repeat a purchase {#repetir}

**⋯** › **Repetir compra** opens a new purchase with the same supplier, category, business unit, voucher, description and items, at today's prices. The date is today, the number is empty and the payment is paid today with the same method, or cash if there was none. A credit note is repeated as a delivery note, and items that were switched off are left out.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/compras-repetir.jpg' | relative_url }}" alt="The Repetir compra panel with today's date, the supplier Distribuidora La Plata, the Insumos category, Compartido entre todas, the Remito voucher with an empty number, and the items further down" loading="lazy" width="880" height="900">
  <figcaption>Repeating the distributor's purchase: all the same, at today's prices.</figcaption>
</figure>

### Correct a purchase {#editar}

Tap the row. You can change everything except the items, including whether it is paid or still to pay. The items are already in stock: to correct them, void the purchase and record it again. Fornu confirms «Cambios guardados» (changes saved).

### Void a purchase {#anular-compra}

1. Tap **⋯** › **Anular**.
2. Type the **Motivo** (reason). Fornu warns that the items it brought go back out of stock.
3. Tap **Anular**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/compras-anular.jpg' | relative_url }}" alt="The Anular compra de $ 64.000 panel with the notice Los insumos que trajo salen del stock, the Motivo filled in and the Volver and Anular buttons" loading="lazy" width="620" height="560">
  <figcaption>Voiding a purchase asks for the reason.</figcaption>
</figure>

The purchase stays in the list, dimmed, when **Ver anulados** is on. Each item's price goes back to what it was before, unless a later purchase has set another.

## Suppliers {#proveedores}

Who the place buys from or pays, with their CUIT (tax ID), contact details, usual category and what is owed to them. Having them on file means you can pick them on every purchase and see each one's balance.

It lives in Compras › **Proveedores** (suppliers) and comes with the Suppliers and purchases module.

<p class="perm"><span>Who can:</span> <span class="tag">Proveedores</span></p>

Paying them from here also takes the **Gastos** permission.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/compras-proveedores.jpg' | relative_url }}" alt="The supplier list: Distribuidora La Plata with 64,000 pesos to pay, Frigorífico Don Pedro with 99,000, each with its Pagar button, and Panificadora del Sur and Verdulería Don Tito up to date" loading="lazy" width="1440" height="420">
  <ol class="marks">
    <li><b>Agregar</b> (add): a new supplier.</li>
    <li><b>A pagar</b> (to pay): what is owed, with <b>Pagar</b> (pay) next to it.</li>
  </ol>
  <figcaption>Four suppliers, two with purchases to pay.</figcaption>
</figure>

| Field | What it is for |
|---|---|
| **Nombre** (name) | Required, and unique. |
| **CUIT** | With or without dashes. Optional. |
| **Teléfono** and **Email** | Phone and email, shown together in the **Contacto** column. |
| **Categoría habitual** | **Ninguna** (none), or an active expense category. Suggested when recording an expense or purchase for them. |
| **Dirección** and **Notas** | Address and notes, to keep at hand. |
| **Activo** (active) | When editing. A supplier that is switched off no longer appears in pickers, and keeps its purchases and payments. |

Suppliers are switched off rather than deleted. If the CUIT is wrong, Fornu says why: «El CUIT … tiene que tener 11 números.» (it needs 11 digits), «El CUIT … no es válido: revisá los números.» (it is not valid) or «El CUIT … ya es de …» (it already belongs to another supplier).

**Pagar** opens «Pagarle a …» (pay …) with all of that supplier's vouchers ticked. It works like [Pay several at once](#pagar-varios).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/compras-pagar-proveedor.jpg' | relative_url }}" alt="The Pagarle a Frigorífico Don Pedro panel with its purchase from 10/11/2026 ticked for 99,000 pesos, Medio de pago on Transferencia, the payment date and the Pagar $ 99.000 button" loading="lazy" width="880" height="560">
  <ol class="marks">
    <li>The vouchers being paid, ticked.</li>
    <li><b>Medio de pago</b> (payment method).</li>
    <li><b>Pagar $ …</b>, with the total of what is ticked.</li>
  </ol>
  <figcaption>Paying a supplier everything that is owed.</figcaption>
</figure>

The search at the top (<kbd>Ctrl</kbd> + <kbd>K</kbd>) also finds suppliers, tagged «Proveedor», and opens them.

## Expenses {#gastos}

Everything paid or still to pay: stock purchases, rent, utilities and wages. Each expense belongs to one business unit or is split across all of them by what each one sells. What is paid in cash comes out of the cash drawer.

It lives in Balances › **Gastos** (expenses). On a phone, Balances is under **Más** (more). It is also the **Gastos** tab on the shop's device.

<p class="perm"><span>Who can:</span> <span class="tag">Gastos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/gastos-lista.jpg' | relative_url }}" alt="The month's expenses: two purchases from a meat supplier still to pay, a paid electricity and gas invoice and a paid weekly purchase, with the period total, what is owed and stock purchases at the top." loading="lazy" width="1440" height="725">
  <ol class="marks">
    <li><b>Exportar</b>: the list as a file for Excel.</li>
    <li><b>Nuevo gasto</b> (new expense): rent, electricity, maintenance, any expense that brings no stock items.</li>
    <li><b>Compra de insumos</b>: the same purchase as in Compras, with the Suppliers and purchases module.</li>
    <li><b>A pagar</b>: everything owed, wages aside, whatever the period. Tap it to pay several at once.</li>
    <li><b>Pagar</b>: pays that voucher.</li>
    <li>The <b>⋯</b> menu: <b>Repetir compra</b>, on purchases, and <b>Anular</b>.</li>
  </ol>
  <figcaption>The demo's expenses so far this month.</figcaption>
</figure>

At the top are the **Total del período** (period total), what is **A pagar** and the **Compras de insumos**. The period works as in Compras, and the one you choose carries over to the other screens that use a period while the browser tab stays open.

Wages show with a «sueldo» (wage) tag and read «Se cambia en Personal › Liquidación» (changed in Staff › Payroll): they cannot be opened or voided from here. They are covered in [Staff]({{ '/en/projects/fornu/manual/personal/' | relative_url }}#liquidacion).

### Record an expense {#nuevo-gasto}

1. Tap **Nuevo gasto**.
2. Pick the **Proveedor**, if there is one, and the **Categoría**.
3. Pick the **Unidad de negocio**, or leave it on **Compartido entre todas**.
4. Pick the **Comprobante**, which starts on **Factura B**, and type the **Número**.
5. Type the **Neto** (net) and the **IVA**. **21% del neto** and **10,5% del neto** (21% or 10.5% of net) fill in the VAT in one tap. Add any withholdings.
6. Choose **Pagado** or **A pagar**, and tap **Guardar**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/gastos-nuevo.jpg' | relative_url }}" alt="The Nuevo gasto panel with the date, supplier, no category yet, shared by all, a B invoice, the number, the description, the net amount and the VAT with the 21 and 10.5 percent shortcuts." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li><b>Proveedor</b>, with <b>+ Proveedor nuevo</b>.</li>
    <li><b>Unidad de negocio</b>.</li>
    <li><b>Comprobante</b> and <b>Número</b>.</li>
    <li><b>21% del neto</b> and <b>10,5% del neto</b>: they work out the VAT.</li>
    <li>The total and what is still missing before it can be saved.</li>
  </ol>
  <figcaption>A new expense, before the category is picked.</figcaption>
</figure>

Fornu confirms «Gasto cargado» (expense recorded). Like purchases, a new expense starts as paid in cash, dated today.

### Pay an expense {#pagar}

1. Tap **Pagar** on the row.
2. Pick the **Medio de pago**, which starts on Transferencia (bank transfer), and the **Fecha de pago** (payment date).
3. Tap **Registrar pago** (record payment). Fornu confirms «Pago registrado».
{: .steps}

If someone paid it in the meantime, it warns «Ya está pagado» (already paid) with the date.

### Pay several at once {#pagar-varios}

Tap **A pagar**, in Gastos or in Compras. You also get here from the home page's warnings about overdue or upcoming payments, and from **Pagar** in Proveedores.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/gastos-pagar-varios.jpg' | relative_url }}" alt="The Lo que hay que pagar panel, with one button per supplier, three vouchers of which two are ticked, bank transfer, the payment date and the Pagar 123,000 pesos button." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li>One button per supplier, with their total: it ticks all their vouchers.</li>
    <li>The vouchers, with their date, number and due date.</li>
    <li><b>Medio de pago</b> and <b>Fecha de pago</b>.</li>
    <li>What the ticked vouchers add up to, and how many there are.</li>
    <li><b>Pagar $ …</b>.</li>
  </ol>
  <figcaption>Two of the greengrocer's vouchers, paid together by transfer.</figcaption>
</figure>

1. Tick what you are paying, or tap a supplier's button. Overdue vouchers come ticked, or all of the supplier's if you came from Proveedores.
2. Pick the method and the date.
3. Tap **Pagar $ …**.
{: .steps}

Fornu confirms how many vouchers it paid and the total. It is all or nothing: if one was already paid, it says which, so you can untick it. From stock purchases, the list holds purchases only.

### If the cash drawer is closed {#caja-cerrada}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/gastos-caja-cerrada.jpg' | relative_url }}" alt="The La caja está cerrada warning, explaining that the cash would come out of a drawer nobody opened, with the Volver and Pagar igual buttons." loading="lazy" width="500" height="266">
  <figcaption>The warning before paying cash with the drawer closed.</figcaption>
</figure>

When you pay in cash and the drawer is not open, Fornu asks first: «La caja está cerrada» (the cash drawer is closed). It happens when saving an expense or purchase as paid in cash, and when paying one or several in cash. That cash would come out of a drawer nobody opened, and the count would not balance once it is opened. You have three ways out:

- **Volver** (back), then open the drawer first in Balances › Arqueo (cash count), see [Cash and sales]({{ '/en/projects/fornu/manual/caja/' | relative_url }}#arqueo).
- **Volver**, then pick another method, if the money came from somewhere else.
- **Pagar igual** (pay anyway).

Editing an existing expense does not ask. If the payment falls before a cash count that already took it into account, Fornu says the drawer was already counted with that cash and does not move it again. If the money is not where it should be, fix it with a movement in Caja.

### Void an expense {#anular}

1. Tap **⋯** › **Anular**.
2. Type the **Motivo**.
3. Tap **Anular**. Fornu confirms «Anulado» (voided).
{: .steps}

The expense stays in the list, dimmed, when **Ver anulados** is on. Wages are voided from Personal › Liquidación.

### Export for the accountant {#exportar}

**Exportar** downloads a file for Excel set up for Spanish, with columns separated by semicolons and a decimal comma. It holds what is in the list: the chosen period, plus voided entries if they are showing. The file is named after the dates, such as `compras-y-gastos-2026-11-01-a-2026-11-30.csv`.

There is one row per voucher, with the date, the voucher and its number, the supplier and their CUIT, the category, the business unit, the description, the net amount and VAT for each rate (21%, 10.5%, 27% and others), untaxed or exempt amounts, amounts without itemised VAT, withholdings, the total, the status, the payment date and method, and the due date.

## Expense categories {#categorias-gastos}

They group expenses so you can see in Rentabilidad (profitability) where the money goes ([Costs and reports]({{ '/en/projects/fornu/manual/costos-y-reportes/' | relative_url }}#rentabilidad)).

They live in Compras › **Categorías de gastos** (expense categories). The tab reads **Categorías**.

<p class="perm"><span>Who can:</span> <span class="tag">Ajustes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/compras-categorias-gastos.jpg' | relative_url }}" alt="A new account's expense categories, from Insumos to Otros, with their order." loading="lazy" width="1440" height="650">
  <ol class="marks">
    <li><b>Agregar</b>: a new category.</li>
    <li><b>Insumos</b>: the one new purchases pick on their own.</li>
    <li><b>Orden</b> (order): where it appears in the lists.</li>
  </ol>
  <figcaption>The categories a new account starts with.</figcaption>
</figure>

A new account starts with Insumos, Packaging, Alquiler, Servicios (luz, gas, internet), Sueldos y cargas sociales, Mantenimiento y limpieza, Impuestos y tasas, Comisiones y gastos bancarios, Publicidad and Otros (stock items, packaging, rent, utilities, wages and social charges, maintenance and cleaning, taxes and fees, bank charges, advertising, other).

Tap **Agregar**, or a category to change it. Each one has **Nombre**, **Orden** (a new one goes last) and, when editing, **Activa** (active). Categories are switched off rather than deleted. One that is switched off is no longer offered, and the expenses already filed under it keep it.

<div class="callout tip"><p class="callout-title">Tip</p><p>Keep a category named exactly <b>Insumos</b>. New purchases, and the ones the production plan builds, pick it on their own.</p></div>
