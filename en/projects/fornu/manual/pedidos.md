---
layout: manual
manual: pedidos
title: "Orders and delivery · Fornu manual"
description: "The orders board, phone orders, platform orders, what ran out, the order history, the couriers' cash and the customer list."
permalink: /en/projects/fornu/manual/pedidos/
---

## The board {#tablero}

This is the screen for the kitchen and whoever dispatches. Every order shows up in **A confirmar** (to confirm) the moment it arrives, with a chime. From there it moves through **En preparación** (cooking) and **Listo para entregar** (ready for pickup) to **En camino** (on the way), one tap per step. It refreshes on its own: nobody has to reload the page to see new orders.

It lives under Pedidos › **En curso** (in progress; the page itself is called **Pedidos**), and it is also the **Pedidos** tab on the kitchen tablet.

<p class="perm"><span>Who can:</span> <span class="tag">Cocina</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-tablero.jpg' | relative_url }}" alt="The demo's orders board with three orders to confirm, three cooking and three ready for pickup, from four brands" loading="lazy" width="1440" height="720">
  <ol class="marks">
    <li><b>Impresora de comandas</b> (ticket printer): online, tickets waiting, or not set up yet.</li>
    <li><b>Agotados</b> (sold out): what ran out today. When something is out, it shows how many.</li>
    <li><b>Nuevo pedido</b> (new order): an order of your own, by phone or message. Shortcut <kbd>N</kbd>.</li>
    <li><b>Todo</b> (all) and one button per brand or station: what this board shows.</li>
    <li><b>Confirmar · 15 min</b>, with the clock to pick another time and the cross to cancel.</li>
    <li><b>Ver sumado</b> (see totals): everything being cooked, added up per product.</li>
    <li><b>Listo</b> (ready): the order is done and packed.</li>
    <li><b>Deshacer</b> (undo, for two minutes) and <b>Se lo llevó</b> (picked up).</li>
  </ol>
  <figcaption>The demo's board, with four brands cooked in the same kitchen.</figcaption>
</figure>

### What each column holds

| Column | What is there | What you do |
|---|---|---|
| **A confirmar** | Orders that just came in, in order of arrival. The card's clock turns amber at 2 minutes and red at 4. | Confirm it with its time, or cancel it. |
| **En preparación** | What is cooking, the one due first at the top. The card says what time it is due, and a bar fills up towards that time; past it, the bar turns red and the card says «Atrasado» (late). | Mark it **Listo**. |
| **Listo para entregar** | What is waiting for a rider. Orders whose platform rider has already arrived go first. | **Se lo llevó**, or wait for the courier to take it from their phone. |
| **En camino** | What is out for delivery, who has it and since when. | **Entregado** (delivered). |

Below the columns, **Ver los cerrados de hoy** (see today's closed orders) lists what was delivered and cancelled today.

Each card shows the number, the brand, the customer, the total, the items with their options, and the note. A platform order also carries its chip (**Rappi** or **PedidosYa**) and the number the rider will ask for. If a line says **agotado** (sold out), that product was marked out after the order came in: tell the platform before confirming it. If it says **sin vincular** (not linked), the product is not on the brand's menu and takes nothing from stock.

### Confirming an order

1. Check on the card what was ordered and for which brand.
2. Tap **Confirmar · 15 min**. The time is that brand's usual one (20 minutes if the brand has none).
3. If today it will take longer, tap the clock next to it. Pick 10, 15, 20, 25, 30, 40, 50 or 60 minutes, or type another time, and tap **Confirmar**.
{: .steps}

The time is how long until the order is cooked and packed: it is what the rider is told so they come at the right moment. On confirming, Fornu takes from stock what each product, its options and the brand's packaging use, sends the ticket to every station that makes a part of it, and, for a platform order, tells the platform you accepted it.

### Cancelling an order

Only an order still in **A confirmar** can be cancelled. Once confirmed, the kitchen has started it.

1. Tap the cross on the card.
2. Pick a reason with one tap, or type one. The quick ones are **Falta un producto** (something is missing), **No llegamos con el tiempo** (we can't make it in time), **Fuera de la zona de entrega** (outside the delivery area) and **Lo canceló el cliente** (the customer cancelled).
3. Tap **Cancelar pedido**.
{: .steps}

Since it was never confirmed, nothing left the stock. If it came from a platform, the platform is told you rejected it.

### Marking ready and delivering

1. When the order is cooked and packed, tap **Listo**. It moves to **Listo para entregar** and, for a platform order, the platform is told.
2. When it leaves, tap **Se lo llevó**. An order of your own moves to **En camino**. One keyed in from a platform's tablet closes, because the platform's rider took it.
3. When it arrives, tap **Entregado**.
{: .steps}

Usually your own couriers tap **Me lo llevo** (I'm taking it) and **Entregado** on their phones, so Fornu knows who took it and how much cash they collected. That is explained in [In the kitchen and on the road]({{ '/en/projects/fornu/manual/cocina-y-reparto/' | relative_url }}#mensajero). Orders from a platform whose store is linked move on their own when the rider picks them up.

<div class="callout tip"><p class="callout-title">Tip</p><p>If you tapped <b>Listo</b> by mistake, you have two minutes to tap <b>Deshacer</b> and the order goes back to cooking. After two minutes it stays ready.</p></div>

### Everything to cook, added up

When several orders are cooking, the button on the **En preparación** column switches to **Ver sumado**: every product across all orders and table rounds, added up. The grill sees "12 Papas fritas" instead of hunting for them card by card.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-sumado.jpg' | relative_url }}" alt="The En preparación column in the added-up view: 12 fries and 5 canned sodas, across eight orders" loading="lazy" width="1440" height="400">
  <ol class="marks">
    <li><b>Ver pedidos</b> (see orders) goes back to the cards.</li>
    <li>Each product with its total. Tap it and the cards come back with the orders that carry it highlighted.</li>
  </ol>
</figure>

### Seeing the whole order

Tap the card anywhere except a button, or tap its number. The order opens with its items and prices, the customer and their phone (tap to call, with a **WhatsApp** button next to it), the address, the note, and what to collect, for example «Cobrar $ 4.500 en efectivo · paga con $ 10.000: llevá $ 5.500 de vuelto» (collect $4,500 in cash, pays with $10,000, bring $5,500 change). Below are its steps with their times: when it came in, when it was confirmed and with how many minutes, who took it, when it was delivered. If the place has the dining room or invoicing modules, they add their own steps, such as a table's rounds or the invoice.

### Showing one station or one brand

Above the columns, **Todo** shows every order. Next to it there is a button for each kitchen station and each brand that has orders in progress. With a station picked, the board shows only orders that have something for that station, and dims the other stations' lines. The choice is kept on that device: the grill's tablet stays on the grill even after it is switched off.

### The ticket printer

If the kitchen works with a thermal printer, the board says how it is doing: **Impresora de comandas en línea** (printer online), how many tickets are waiting for the printer, or that the print agent has not answered since a certain time. With a printer set up, each card in preparation says whether its ticket printed, and the printer icon prints it again, marked as a copy. Without a printer, whoever holds the **Ajustes** permission sees **Sin impresora de comandas · Configurar** (no ticket printer, set it up). The printer is set up in [Ajustes › Configuración]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#impresion). Working with the tablet alone is a valid choice too.

### Sound

Each new order plays two rising notes, and the chime repeats every 20 seconds while something is waiting to be confirmed. A platform cancelling an order that was already confirmed plays falling notes, and the card stays crossed out with «No lo prepares» (don't make it) until someone taps **Entendido** (got it). If the browser is blocking sound, the board says so: tap anywhere on the screen or tap **Prender el sonido** (turn sound on). On a tablet, the board keeps the screen awake while it is open, where the device allows it.

### On a phone

<div class="shot-pair">
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/pedidos-tablero-celular.jpg' | relative_url }}" alt="The board on a phone: one column at a time, picked with tabs, and the module bar at the bottom" loading="lazy" width="585" height="1266">
    <ol class="marks">
      <li>The columns as tabs, each with its count.</li>
      <li>The modules, at the bottom.</li>
    </ol>
  </figure>
  <div>
    <p>On a phone you see one column at a time, picked with tabs that stay pinned at the top. The board opens on the first column that has orders, and the <b>A confirmar</b> tab flashes when something comes in while you are looking at another.</p>
    <p>On the kitchen tablet, held either way, three columns fit: <b>A confirmar</b>, <b>En preparación</b>, and <b>Listo para entregar</b> sharing the third with <b>En camino</b>. On a computer all four fit, each scrolling on its own.</p>
  </div>
</div>

## Taking an order of your own {#pedido-propio}

An order of your own (**pedido propio**) is one the place takes by phone or message and delivers with its own couriers. The form follows the order of the call: first who it is, then what they want, and last how they pay.

<p class="perm"><span>Who can:</span> <span class="tag">Cocina</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-nuevo.jpg' | relative_url }}" alt="The Nuevo pedido form with the phone of a customer who ordered before, her name and address filled in, the Repetir su último pedido button and the first brand's menu" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li><b>Propio</b> (own) or a platform, only when a store is not linked yet.</li>
    <li><b>Teléfono</b> (phone): from 6 digits, it shows who it is if they ordered before.</li>
    <li><b>Repetir su último pedido</b> (repeat their last order), at today's prices.</li>
    <li>The brand, and its menu by category below.</li>
    <li><b>Crear y empezar</b> (create and start): creates the order and confirms it with the brand's time.</li>
  </ol>
</figure>

1. Tap **Nuevo pedido**, or press <kbd>N</kbd> on the board.
2. Type the phone number. If that person ordered before, they appear below under «Ya pidieron con este número» (already ordered with this number): tap them, or press <kbd>Enter</kbd>, and the name, phone and address fill in. Dashes, spaces or a leading +54 9 make no difference.
3. Fill in **Cliente** (customer) and **Dirección de entrega** (delivery address) if they did not fill in by themselves.
4. If they ordered before, **Repetir su último pedido** loads last time's items at today's prices, leaving out anything no longer sold or sold out.
5. Pick the brand and tap the products. If a product has options (doneness, extras, the combo's drink), a window opens to choose them, with the quantity and a note such as «Sin pepinos» (no pickles).
6. Under **Pago** (payment), choose **Cómo paga** (how they pay): **Efectivo** (cash), **Débito**, **Crédito**, **QR**, **Transferencia** (bank transfer), **Mercado Pago** or **Ya pagó** (already paid). For cash, **Paga con** (pays with) offers **Justo** (exact) and the likely notes, and works out the change so the courier brings it.
7. If needed, add a note for the kitchen or the courier.
8. Tap **Crear y empezar · 20 min**.
{: .steps}

The order goes straight to **En preparación** with the brand's time: it takes stock and sends the ticket like any confirmed order. The foot of the form shows the total and what is missing («Falta el cliente», customer missing; «Falta cómo paga», payment method missing), and the button lights up once everything is there.

<div class="callout tip"><p class="callout-title">Tip</p><p>An order belongs to one brand. If you switch brands with items already loaded, Fornu asks before emptying the order. Tapping the button twice, or retrying after a dropped connection, never creates two orders.</p></div>

## Platform orders keyed in by hand {#plataformas}

While a brand's Rappi or PedidosYa store is not linked, its orders only reach the platform's own tablet. So that they still take stock, print the ticket and count in sales with that platform's prices and commission, they are keyed into Fornu with the number that tablet shows. Nothing you mark here reaches the platform.

<p class="perm"><span>Who can:</span> <span class="tag">Cocina</span></p>

1. Tap **Nuevo pedido** and pick the platform at the top, next to **Propio**.
2. Type **N.º del pedido en Rappi** (or PedidosYa): the one the tablet shows, which is what the rider asks for.
3. Optionally, the customer's name.
4. Load the products. The menu shows that platform's prices, and sold-out products can be added because the platform already sold them.
5. Tap **Cargar y empezar** (load and start).
{: .steps}

The same number cannot be keyed in twice: Fornu says it is already loaded and under which order number. These orders close when the rider takes them (**Se lo llevó**). If the platform cancels one after you confirmed it, open the order and tap **Rappi lo canceló** (or **PedidosYa lo canceló**), with the reason. Whatever already left the stock stays deducted, because it was cooked or thrown away.

Once the store is linked, its orders reach the board on their own and the platform no longer appears in **Nuevo pedido**. Linking is explained in [Settings]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#tiendas).

## Sold out for today {#agotados}

When something runs out in the middle of service, the kitchen marks it with one tap and it stops being offered everywhere: in your own orders, in the linked platform stores and in the options that use it. It comes back by itself when the kitchen's next day starts, so nobody has to remember to switch it back on.

<p class="perm"><span>Who can:</span> <span class="tag">Cocina</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-agotados.jpg' | relative_url }}" alt="The Agotado por hoy panel with the search box and each brand's products, each with Marcar agotado, and En las 2 marcas on products two brands sell" loading="lazy" width="620" height="900">
  <ol class="marks">
    <li><b>Buscar un producto</b> (find a product), by name.</li>
    <li><b>Marcar agotado</b> (mark sold out), for that brand only.</li>
    <li><b>En las 2 marcas</b> (in both brands): the same product, sold out in every brand that sells it.</li>
    <li><b>Listo</b> closes the panel.</li>
  </ol>
</figure>

1. Tap **Agotados** on the board. It also opens from the search (<kbd>Ctrl</kbd> <kbd>K</kbd>) by typing «agotado» or «sin stock».
2. Find the product, or scroll the list grouped by brand.
3. Tap **Marcar agotado**, or **En las 2 marcas** if several brands sell it.
4. Tap **Listo**.
{: .steps}

At the top of the list, **Agotado ahora** (out now) shows each product, since when and who marked it, with **Volver a ofrecer** (offer again) in case it is back. Under each product you can see what happened on each platform: «Apagado en Rappi» (switched off on Rappi), «Avisando a Rappi…» (telling Rappi), or that there is no linked store and it has to be paused on the platform's tablet.

If the stock pause is on in [Ajustes › Configuración]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#pausar), there is also **No alcanza el stock** (not enough stock): whatever the recipe cannot make with what is in stock pauses by itself. If the stock figures are wrong and the kitchen does have it, **Hay: ofrecer igual** (we have it, offer it anyway) offers it again until the day ends.

## Venta › Delivery {#venta}

**Venta** (sale) is the screen for selling from one place, with a tab for each point of sale. **Delivery** shows the orders that leave the kitchen, your own and the platforms', grouped by status, and opens the one you tap in a panel on the right without losing the list. With the dining room module there are also **Mesas** (tables), **Mostrador** (counter) and **Mostrador express**, explained in [Dining room]({{ '/en/projects/fornu/manual/salon/' | relative_url }}).

<p class="perm"><span>Who can:</span> <span class="tag">Cocina</span> for Delivery</p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-venta.jpg' | relative_url }}" alt="Venta on the Delivery point: an order being cooked on the left and the same order open on the right, with its customer, address, payment, steps and the Listo button" loading="lazy" width="1440" height="780">
  <ol class="marks">
    <li>The points of sale. Each person sees the ones they can use.</li>
    <li>The cash drawer: open since what time, or closed.</li>
    <li><b>Nuevo pedido</b>, same as on the board.</li>
    <li>The cards, with the same buttons as on the board.</li>
    <li>The open order, in full.</li>
    <li>The next step: <b>Confirmar</b>, <b>Listo</b>, <b>Se lo llevó</b> or <b>Entregado</b>.</li>
  </ol>
</figure>

It suits whoever answers the phone at the counter: take the order, see it in the panel and follow it until it leaves. On narrow screens the open order takes the whole screen, and closing it brings the list back.

## Order history {#historial}

The orders of any day, your own and the platforms', with everything that happened to each one. It is for a complaint ("what time did it leave?"), for finding an order by customer or by platform code, and for taking the day into a spreadsheet.

It lives under Pedidos › **Historial** (the page is called **Historial de pedidos**).

<p class="perm"><span>Who can:</span> <span class="tag">Pedidos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-historial.jpg' | relative_url }}" alt="The order history of one day, with the date picker, the filters, the search box, four figures and the list of orders with their status" loading="lazy" width="1440" height="700">
  <ol class="marks">
    <li>The day: arrows for the previous and next one, or the date.</li>
    <li><b>Todos</b> (all), <b>Entregados</b> (delivered), <b>Cancelados</b> (cancelled) or <b>En curso</b> (in progress).</li>
    <li>Search by customer, number, product or platform code.</li>
    <li>The day's orders, sales, average ticket and cancellations.</li>
    <li><b>Exportar</b> (export): what is on screen, as a spreadsheet.</li>
  </ol>
</figure>

Tap a row to open the order with its steps. The day is the kitchen's: if the day starts at 6, an order placed at 1 a.m. counts in the previous day. **Exportar** downloads a CSV file that opens in Excel, with the number, time, brand, channel, platform code, customer, products, total, status and cancellation reason.

From the app-wide search (<kbd>Ctrl</kbd> <kbd>K</kbd>), typing an order number or a customer opens the history on that day with the order already open. With the invoicing module, the detail also shows the order's invoice and, to whoever can invoice, a **Facturar** (invoice) button.

## Couriers' cash {#efectivo}

Each order of your own paid in cash stays with whoever delivered it until they hand the money in. This screen says who holds how much and from which orders, and records the handover with any difference. The natural moment is when each courier ends their shift.

It lives under Pedidos › **Efectivo** (the page is called **Efectivo de los mensajeros**).

<p class="perm"><span>Who can:</span> <span class="tag">Pedidos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-efectivo.jpg' | relative_url }}" alt="Couriers' cash: a card with three delivered cash orders, a total of 33,000 pesos and the Rendir button" loading="lazy" width="1440" height="600">
  <ol class="marks">
    <li>Who holds the cash and from how many orders. Orders sent out from the kitchen with <b>Se lo llevó</b> fall under «Sin mensajero marcado» (no courier marked).</li>
    <li><b>Rendir</b> (hand in), with the total they should hand over.</li>
    <li><b>Últimas rendiciones</b> (latest handovers): who, what they owed, what they handed in and the difference.</li>
  </ol>
</figure>

1. Tap **Rendir** on the person's card.
2. Check **Pedidos que rinde** (orders handed in): all are ticked. Untick one to leave it for later.
3. In **Entregó** (handed in), type what they actually handed over. Fornu says whether it matches, or how much is short or over.
4. If it does not match, write why (for example «Le faltó cambio en un pedido», he ran out of change on one order). It is required.
5. Tap **Guardar rendición** (save handover).
{: .steps}

The money handed in enters the cash drawer as a movement, «Rendición de» plus the name, so the cash count includes it. Inicio warns when cash from earlier days was never handed in. The courier sees on their phone how much they are carrying. Card, QR and already-paid orders do not appear here.

## Customers {#clientes}

The people the place knows: regulars, the owners, the staff. Each one can carry a discount that applies by itself when the sale is theirs, such as the owners at 100% and the staff at 50%, and the discount is recorded with the chosen reason or with their name. Their details also fill in an order of your own when their phone number is typed.

It lives under Pedidos › **Clientes**.

<p class="perm"><span>Who can:</span> <span class="tag">Ajustes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-clientes.jpg' | relative_url }}" alt="The customer list with Dueños at 100 percent and Personal at 50 percent" loading="lazy" width="1440" height="300">
  <ol class="marks">
    <li><b>Agregar</b> (add) a customer.</li>
    <li>Their automatic discount and the reason it is recorded under.</li>
  </ol>
</figure>

1. Tap **Agregar**, or a row to change it.
2. Type the **Nombre** (name) the place knows them by («Dueños», «Personal», «Ana Pérez»), and optionally the phone, email and address.
3. In **Descuento automático (%)**, from 0 to 100, the discount they get. In **Motivo del descuento**, the reason it is recorded under (reasons are set up in [Ajustes › Motivos de descuento]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#descuentos)), or **Su nombre** (their name).
4. Tap **Guardar** (save).
{: .steps}

Customers are not deleted: switch **Activo** off when editing. The discount applies when the customer is assigned to a table or to an express sale in the dining room, as [Dining room]({{ '/en/projects/fornu/manual/salon/' | relative_url }}#cliente) explains.

<div class="callout tip"><p class="callout-title">Tip</p><p>Setting up «Dueños» (owners) at 100% is how the house's own consumption gets recorded: the sale closes at no charge and stays visible in the sales list.</p></div>
