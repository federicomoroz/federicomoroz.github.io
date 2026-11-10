---
layout: manual
manual: facturacion
title: "Electronic invoicing · Fornu manual"
description: "Which invoice the account issues, how it is set up with ARCA, how to invoice by hand, at the table and at the end of the day, and what to do with invoices that wait or get rejected."
permalink: /en/projects/fornu/manual/facturacion/
---

## What Fornu issues {#que-se-emite}

With invoicing switched on, Fornu asks ARCA (Argentina's tax agency) for a CAE, the authorization code, for every sale that has to be invoiced, and the invoice is kept with the order, with its number, CAE and QR code. Some sales are invoiced on their own when delivered. Others are invoiced by hand, when the customer asks for an invoice with their DNI (national ID) or CUIT (tax ID).

The invoice type depends on the account's VAT status, set in Ajustes › Configuración, **Condición frente al IVA** (VAT status):

| The account is | To a final consumer | To a customer with a CUIT who is a registered VAT payer or a monotributista | To another identified customer (with a DNI, or a VAT-exempt CUIT) |
|---|---|---|---|
| **Monotributo** (simplified regime) | Factura C | Factura C | Factura C |
| **Responsable inscripto** (registered VAT payer) | Factura B, VAT included | Factura A, with net and 21% VAT shown separately | Factura B |

A Factura C shows only the total. A B shows the total and, below it, **IVA contenido (21%)** (VAT included). An A splits **Neto gravado** (net taxable), **IVA 21%** and **Total**, and carries the customer's legal name. An invoice is voided with a credit note of the same type.

Electronic invoicing is an account module. When it is off, Balances › Facturas, Ajustes › Facturación and the **Facturar** (invoice) buttons do not appear.

| Permission | What it allows |
|---|---|
| **Facturar** | Invoicing a sale by hand, with a DNI or CUIT if asked. |
| **Ver facturas** (see invoices) | Seeing the list of invoices and credit notes, resending the ones waiting, and voiding. |
| **Configurar la facturación** (set up invoicing) | Entering the tax details and the point of sale, and testing the connection with ARCA. |

**Administración** holds all three. The **Encargado/a** (manager) role comes with none: add them in [Staff]({{ '/en/projects/fornu/manual/personal/' | relative_url }}#roles) to whoever needs them.

<div class="callout"><p class="callout-title">Good to know</p><p>In the demo, invoices come from a test ARCA. They have a CAE and a QR code, but they say they have no fiscal validity: the voucher shows «Comprobante de prueba: lo autorizó un simulador de ARCA y no tiene validez fiscal.» (test voucher, authorized by an ARCA simulator, no fiscal validity) and prints with «Comprobante de prueba · sin validez fiscal». In the demo, Ajustes › Facturación cannot be changed either: «En la demo esto no se cambia: la usa todo el que la prueba. En tu cuenta, sí.» (this can't be changed in the demo, which everyone uses, but it can in your account).</p></div>

## Setting up invoicing {#configurar}

It is done once, in Ajustes › Facturación, by the owner or whoever runs the account, with the tax password at hand.

<p class="perm"><span>Who can:</span> <span class="tag">Configurar la facturación</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/facturacion-ajustes.jpg' | relative_url }}" alt="Ajustes, Facturación: the Prender la facturación button, the notice that the server is not connected to ARCA, the tax details, Identificar al cliente desde set to 10,000,000 and the Qué se factura solo checkboxes" loading="lazy" width="1440" height="838">
  <ol class="marks">
    <li><b>Prender la facturación</b> (switch invoicing on). It also saves whatever is typed in the form.</li>
    <li>The state of this server's connection with ARCA. While it says it is not connected, nothing can be invoiced.</li>
    <li>What the account issues given its VAT status, with a link to change it.</li>
    <li><b>Punto de venta</b> (point of sale): the one registered with ARCA for web-service invoicing.</li>
    <li><b>Identificar al cliente desde</b> (identify the customer from): ARCA's threshold for invoicing without a DNI or CUIT.</li>
    <li><b>Qué se factura solo</b> (what is invoiced automatically): the channels and payment methods invoiced on delivery.</li>
  </ol>
  <figcaption>Ajustes › Facturación on a monotributo account, still empty.</figcaption>
</figure>

### Entering the tax details

They are printed on every invoice.

| Field | What goes in |
|---|---|
| **CUIT** | The business's tax ID. Required. |
| **Razón social** (legal name) | As registered with ARCA. Required. |
| **Domicilio comercial** (business address) | Required. |
| **Punto de venta** | «El que se dio de alta en ARCA para facturar por web service.» (the one registered with ARCA for web-service invoicing). Required. |
| **Ingresos Brutos** (provincial gross income tax) | «El número, o «Exento».» (the number, or "Exento" if exempt). |
| **Inicio de actividades** (start of activities) | The date. |
| **Identificar al cliente desde** | The total from which ARCA requires the customer's DNI or CUIT. It comes set to $10,000,000 (see [ARCA's threshold](#tope)). |

Above the fields, the text says what the account issues: «Monotributo, que emite Factura C.» or «Responsable inscripto, que emite Factura A y B con IVA 21%.». To change it, use **Cambiarla en Configuración** (change it in settings).

### Delegating in ARCA and testing the connection

Fornu invoices on the business's behalf. For that, the business's CUIT delegates electronic invoicing to Fornu's CUIT on ARCA's website. The **Conexión con ARCA** (connection with ARCA) block lists the steps:

1. Log in to ARCA's website with the tax password of the account's CUIT.
2. Open the **Administrador de Relaciones de Clave Fiscal** (tax password relations manager) and choose **Nueva relación** (new relation).
3. Look for **ARCA → WebServices → Facturación electrónica**.
4. As the representative, enter Fornu's CUIT, which the screen shows in that step.
5. Come back to Fornu and tap **Probar la conexión** (test the connection). ARCA can take a few hours to pick up the delegation.
{: .steps}

**Probar la conexión** needs the CUIT saved first. What it can answer:

| Answer | What it means |
|---|---|
| «ARCA responde: el punto de venta N todavía no tiene comprobantes.» | All good. It is a new point of sale with no vouchers yet. |
| «ARCA responde: el último comprobante del punto de venta N es el número M.» | All good. The next invoice follows that numbering. |
| «ARCA no ve que el CUIT … haya delegado la facturación electrónica en el de Fornu (…).» | The delegation is missing or ARCA has not picked it up yet. Check the steps or wait a few hours. |
| «ARCA no tiene ese punto de venta habilitado para facturar por web service.» | That point of sale is not a web-service one. Check it in ARCA or enter the right one. |
| «No se pudo hablar con ARCA: …» | ARCA did not answer. Try again later. |

If the top of the page says «Este servidor todavía no está conectado con ARCA: por ahora no se puede facturar.» (this server is not connected to ARCA yet: no invoicing for now), invoicing is not possible from there yet: **Prender la facturación** and **Probar la conexión** stay off. If the account is connected to a test environment, the screen says so too, and those invoices have no fiscal validity. In Ajustes › Integraciones, the **ARCA · Factura electrónica** card sums up the connection in one line.

### Choosing what is invoiced automatically

**Qué se factura solo** has two parts:

- **Channels**: «Los pedidos de estos canales se facturan al entregarse, a consumidor final. Los demás, a mano desde el pedido.» (orders from these channels are invoiced on delivery, to a final consumer, and the rest by hand from the order). **Pedidos propios**, **Rappi** and **PedidosYa** come ticked. **Salón** comes unticked, because at the table the invoice is requested when paying.
- **Payment methods**: «Y las ventas pagadas con estos medios, de cualquier canal: la tarjeta, el QR y las transferencias dejan rastro.» (and sales paid with these methods, from any channel: cards, QR and transfers leave a trace). None come ticked. Tick **Tarjeta de débito** and tables paid by debit card are invoiced automatically even with **Salón** unticked.

Then tap **Guardar** (save), which lights up once you change something.

Automatic invoicing covers, to a final consumer, what was delivered since the day invoicing was switched on, looking back at most 5 business days: anything older is invoiced by hand. If you switch invoicing off and on again, that date starts over, and what was delivered while it was off is not invoiced automatically.

### Switching invoicing on

1. Fill in CUIT, legal name, address and point of sale.
2. Tap **Prender la facturación**. You get «Facturación prendida».
3. The top now says **Facturando** (invoicing) «desde el … Lo entregado antes se factura a mano, desde el pedido.» (since…, with anything delivered earlier invoiced by hand, from the order).
{: .steps}

If something is missing, Fornu says «Completá antes el CUIT, la razón social, el domicilio y el punto de venta.». To stop invoicing, use **Apagar la facturación** (switch invoicing off).

## Invoicing a sale by hand {#a-mano}

This is for the customer who asks for an invoice with their DNI or CUIT, or for a sale that was not invoiced automatically: a table, an order from before invoicing was switched on, one from an unticked channel.

<p class="perm"><span>Who can:</span> <span class="tag">Facturar</span></p>

The **Facturar** button shows up in three places:

- In Balances › Ventas, in the **Comprobante** column of each sale without an invoice.
- On the **Factura** line of an order's detail.
- On a closed table in the Salón.

If the last invoice was rejected or voided, it reads **Facturar de nuevo** (invoice again). It does not appear on cancelled orders or on orders waiting to be confirmed. A table is invoiced once it is paid. An own order can be invoiced even while it is still being prepared.

1. Tap **Facturar** on the sale. «Facturar el pedido #N» opens, or «Facturar Mesa 4» for a table.
2. Choose who it is for: **Consumidor final** (final consumer, the default), **Con DNI** (with DNI) or **Con CUIT** (with CUIT).
3. With a DNI or CUIT, type the number. From the seventh digit on, **Ya se facturó a este número** (already invoiced to this number) lists the customers already invoiced with that number: name, CUIT or DNI, VAT status, address and the last time. Tap the right one and everything fills in.
4. Fill in the **Nombre** (name), or the **Razón social** with a CUIT. With a CUIT, choose the **Condición frente al IVA**: **Responsable inscripto**, **Monotributista**, **Exento** (exempt) or **Consumidor final**. For a registered VAT payer or a monotributista, the legal name is required.
5. Tap **Facturar $X**.
{: .steps}

«La factura se guarda ahora y ARCA la autoriza en unos segundos. Si ARCA no responde, se vuelve a intentar sola.» (the invoice is saved now and ARCA authorizes it in a few seconds, and if ARCA does not answer it retries on its own). Meanwhile the sale reads **Sin facturar (esperando a ARCA)**, and once ARCA authorizes it, it turns into **Facturada** with its number.

What Fornu may answer:

| Message | What to do |
|---|---|
| «El pedido #N ya tiene la Factura B …: anulala antes de facturarlo de nuevo.» (the order already has an invoice) | Void the old invoice from [Facturas](#facturas), or use **Corregir**. |
| «Desde $X hay que identificar al cliente con DNI o CUIT.» (from $X the customer must be identified) | The total is over [ARCA's threshold](#tope): invoice **Con DNI** or **Con CUIT**. |
| «La Factura A lleva la razón social del cliente.» (a Factura A needs the legal name) | Fill in the legal name. |
| «Un cliente que factura con su condición frente al IVA se identifica con su CUIT.» (a customer invoicing with their VAT status uses their CUIT) | Choose **Con CUIT**. |
| «La facturación está apagada: prendela en Facturación.» (invoicing is off) | Switch it on in Ajustes › Facturación. |
| «La cuenta de … se factura cuando está cobrada.» (the bill is invoiced once paid) | Take the payment first. |

<div class="callout tip"><p class="callout-title">Tip</p><p>Regular customers who ask for invoices are entered once. Next time, the first digits of their CUIT bring them back with their legal name, VAT status and address.</p></div>

## Invoicing when a table pays {#en-la-mesa}

In the Salón, the invoice is requested at the moment of paying. Taking the payment is covered in [Dining room]({{ '/en/projects/fornu/manual/salon/' | relative_url }}#cobrar). Here is just the invoice part.

<p class="perm"><span>Who can:</span> <span class="tag">Cobrar mesas</span></p>

1. In «Cobrar Mesa N» (charge table N), scroll down to **Comprobante** and switch on **Facturar esta cuenta** (invoice this bill).
2. Choose the customer's **Condición frente al IVA**. For a registered VAT payer, a monotributista or an exempt customer, **Documento** stays on CUIT. For a final consumer you can leave it **Sin identificar** (unidentified) or ask for a DNI or CUIT.
3. Type the number. «Si ya se le facturó, aparece abajo y se completa solo.» (if they were invoiced before, they show up below and fill in on their own).
4. Fill in the **Razón social** (or **Nombre**), the **Domicilio** (address), which goes on the invoice, and optionally the **Teléfono** and **Email** («Para mandarle el comprobante.», to send them the invoice).
5. Fornu previews what will be issued, for example «Saldrá una Factura B por $ 4.500 a consumidor final. ARCA la autoriza en unos segundos.», and the button becomes **Cobrar $ 4.500 en Efectivo y facturar** (charge and invoice).
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/facturacion-mesa.jpg' | relative_url }}" alt="The Comprobante block when charging a table: Facturar esta cuenta switched on, status Responsable inscripto, a CUIT typed and, below it, the already-invoiced customer Distribuidora Sur S.A." loading="lazy" width="700" height="440">
  <ol class="marks">
    <li><b>Facturar esta cuenta</b>.</li>
    <li>The customer's <b>Condición frente al IVA</b>.</li>
    <li>The CUIT. If they were invoiced before, they appear below.</li>
    <li>The known customer: one tap fills legal name, VAT status and address.</li>
  </ol>
  <figcaption>A demo customer who asked for an invoice before.</figcaption>
</figure>

If invoicing is off, the payment dialog says so: «La facturación está apagada en esta cuenta: prendela en Facturación para emitir el comprobante.». If the invoice was requested while invoicing was not ready, the table closes anyway. The sale reads **Sin facturar (pedida: …)** with the reason, its story says «Comprobante pedido · espera: …», and the invoice goes out on its own as soon as it can. Meanwhile it can also be invoiced by hand.

## Invoicing what was left uninvoiced {#fin-del-dia}

Many places invoice at the end of the day whatever was paid by card, QR or transfer. In Balances › Ventas you filter those sales and invoice them all at once.

<p class="perm"><span>Who can:</span> <span class="tag">Facturar</span> <span class="tag">Caja</span></p>

1. Go to Balances › Ventas and leave the period on **Hoy**.
2. Under **Medio de pago**, choose **Todo menos efectivo** (everything but cash). With **Comprobante** › **Sin facturar** you see only what is pending.
3. Under the figures, tap **Facturar N sin facturar** (invoice N uninvoiced).
4. Fornu asks «¿Facturar N ventas por $X?» and explains: «Sale una factura a consumidor final por cada una, las que muestra la lista ahora. La que necesite CUIT o DNI se factura sola, desde su fila.» (one final-consumer invoice per sale in the list, while any that needs a CUIT or DNI is invoiced on its own, from its row). Tap **Facturar N**.
5. You get «N facturas pedidas a ARCA.» (N invoices requested from ARCA). Each sale reads **Sin facturar (esperando a ARCA)** until ARCA authorizes it.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/facturacion-sin-facturar.jpg' | relative_url }}" alt="Sales with two uninvoiced own orders, each with its Facturar button, and the Facturar 2 sin facturar button under the figures" loading="lazy" width="1440" height="450">
  <ol class="marks">
    <li><b>Comprobante</b>: filter invoiced or uninvoiced sales.</li>
    <li><b>Facturar 2 sin facturar</b>: every sale in the list, at once.</li>
    <li><b>Facturar</b> on each row: a single sale, with a DNI or CUIT if needed.</li>
  </ol>
  <figcaption>Two pending sales in the demo.</figcaption>
</figure>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/facturacion-esperando.jpg' | relative_url }}" alt="Both sales now read Sin facturar, esperando a ARCA, and below them the notice 2 facturas pedidas a ARCA" loading="lazy" width="1440" height="380">
  <ol class="marks">
    <li>Both sales wait for their CAE: «(esperando a ARCA)».</li>
    <li>The notice: «2 facturas pedidas a ARCA.»</li>
  </ol>
  <figcaption>A few seconds later, both turn into Facturada.</figcaption>
</figure>

Every sale the list shows is included, not only the 200 drawn, as long as it was delivered, its total is above zero, it has no invoice in force and it did not ask for an invoice with a DNI or CUIT. Those last ones are invoiced on their own, in their customer's name. Up to 300 sales are invoiced at a time.

If some fail, the notice says so with the first reason: «… M ventas quedaron sin facturar: …» (M sales were left uninvoiced).

## Balances › Facturas {#facturas}

This is the list of invoices and credit notes issued, with their CAE. Use it to hand the month over to the accountant, reprint an invoice, resend one that is waiting or void one that went out wrong.

<p class="perm"><span>Who can:</span> <span class="tag">Ver facturas</span></p>

- The period starts on **Este mes** and spans up to a year. The search box finds by **Número, cliente o pedido…** (number, customer or order).
- Four figures: **Comprobantes** (vouchers: the authorized ones, tap it to see all), **Facturado** (invoiced: invoices minus credit notes), **IVA** (VAT), and **Esperando o rechazadas** (waiting or rejected), which filters to those when tapped.
- Each row shows **Fecha** (date), **Comprobante** (for example **Factura B** 00003-00000012), **Pedido** (order), **Cliente**, **Neto** (net), **IVA**, **Total** (credit notes in negative) and **Estado** (status).
- If the period holds test invoices, it says so: «Las facturas de este período son de prueba: no tienen validez fiscal.»

| Status | What it means |
|---|---|
| **Autorizada** (authorized) | It has a CAE. It is valid. |
| **Esperando a ARCA** (waiting for ARCA) | It is saved and Fornu keeps sending it until ARCA answers. |
| **Rechazada** (rejected) | ARCA did not accept it. Hover over the status to read the reason. |
| **Anulada** (voided) | It was voided with a credit note. |

Voided and rejected rows are dimmed.

### Viewing, printing or resending an invoice

Tap a row (or the **Factura** line of an order's detail). The voucher opens as it prints: the business's details, the type letter with its code, number, date, CUIT, gross income tax number and start of activities, the customer and order, the lines with **Cant.**, **Detalle**, **Precio** and **Importe** (quantity, item, price, amount), the totals for that type, the **CAE** with its due date and ARCA's QR code.

| Button | What it does |
|---|---|
| **Imprimir** (print) | Prints the invoice. Only when authorized. |
| **Mandar de nuevo** (send again) | Sends it to ARCA right now, if it is waiting or was rejected. You get «Se manda de nuevo a ARCA». |
| **Anular** (void) | Issues a credit note for the full amount. |
| **Corregir** (correct) | Voids and re-invoices to another customer, together. It also needs **Facturar**. |
| **Listo** (done) | Closes it. |

### Voiding an invoice with a credit note

1. Open the invoice and tap **Anular**.
2. Fornu asks «¿Anular la Factura B …?» and warns: «Se emite una nota de crédito por el total. El pedido queda sin factura y se puede facturar de nuevo.» (a credit note is issued for the total, and the order is left without an invoice and can be invoiced again).
3. Tap **Anular con nota de crédito** (void with a credit note). You get «Nota de crédito pedida a ARCA» and the credit note opens.
{: .steps}

### Correcting an invoice issued to the wrong customer

When the CUIT, the name or the VAT status were wrong, **Corregir** does both things in one step.

1. Open the invoice and tap **Corregir**. «Corregir la Factura B …» opens: «Sale una nota de crédito por esta factura y una nueva a quien corresponda, las dos juntas. Cargá a quién va la nueva.» (a credit note for this invoice and a new one to the right customer, both together: enter who the new one is for).
2. Enter the right customer, as when invoicing by hand.
3. Tap **Anular y facturar de nuevo** (void and invoice again).
{: .steps}

Both go out together or neither does, so the sale is never left with a voided invoice and no new one.

### Exporting for the accountant

**Exportar** downloads a spreadsheet (a CSV file) with the period's authorized vouchers: date, voucher type, number, customer, net, VAT, total, CAE, order, business unit, channel and status. It opens cleanly in Excel set to Spanish. The button is off if the period has no authorized voucher.

<div class="callout tip"><p class="callout-title">Tip</p><p>At the start of each month, pick <b>Mes pasado</b> and tap <b>Exportar</b>: that is the file the accountant needs for the sales ledger.</p></div>

## When ARCA does not answer or rejects {#arca}

### If ARCA does not answer

The invoice is saved anyway as **Esperando a ARCA** and the sale carries on: the kitchen never waits for ARCA. Fornu resends it on its own after 10 seconds, 30 seconds, 2 minutes, 5, 15, and then every 15 minutes, without giving up. Opening it shows «Esperando a ARCA: … Se vuelve a intentar sola, la próxima vez a las 13:05.» (retries on its own, next time at 13:05).

Rather than wait, **Mandar de nuevo** sends it right away. If an answer got lost on the way, Fornu first asks ARCA for its last voucher, so a sale never ends up with two numbers.

### If ARCA rejects it

The invoice becomes **Rechazada** and, when opened, says «No salió:» (it didn't go through) with ARCA's reason. Fix what is wrong (a detail in Ajustes › Facturación, for example) and tap **Mandar de nuevo**: it goes out dated today.

- If the order was invoiced some other way in the meantime, Fornu answers «El pedido ya tiene otra factura: esta queda rechazada.» (the order already has another invoice, so this one stays rejected).
- If what was rejected is a credit note, the invoice it was voiding stays in force.
- If the module is switched off, nothing new is invoiced, but invoices already saved keep going after their CAE.

## ARCA's threshold for identifying the customer {#tope}

ARCA requires the customer's DNI or CUIT from a certain total. That amount lives in Ajustes › Facturación, **Identificar al cliente desde**: «Desde este total, ARCA pide el DNI o CUIT del cliente (hoy, $ 10.000.000). Esos pedidos se facturan a mano.» (from this total ARCA asks for the customer's DNI or CUIT, today $10,000,000, and those orders are invoiced by hand).

A sale invoiced automatically that reaches that total is kept **Rechazada** with «Desde $X hay que identificar al cliente con DNI o CUIT: facturalo a mano.». Invoice it by hand, **Con DNI** or **Con CUIT**. If ARCA changes the amount, update the field.
