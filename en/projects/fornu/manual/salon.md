---
layout: manual
manual: salon
title: "Dining room: tables, counter and payment · Fornu manual"
description: "How to seat a table, load orders and send them to the kitchen by course, move and join tables, split the bill, and use the counter, the express sale, the day's bills and the room setup."
permalink: /en/projects/fornu/manual/salon/
---

## Where you sell {#venta}

The whole dining room runs from one sale screen. You find it under **Salón › Mesas** (dining room › tables) and also under **Pedidos › Venta** (orders › sale): it is the same screen, opened where it belongs. Along the top there is a tab for each place you sell from, and each person only sees the tabs their role allows.

| Tab | What it is for | Who sees it |
|---|---|---|
| **Mesas** (tables) | The live dining room: seat guests, load what they order, send it to the kitchen and take payment. | Atender mesas or Cobrar mesas |
| **Delivery** | Your own delivery orders and the platforms'. Covered in [Orders and delivery]({{ '/en/projects/fornu/manual/pedidos/' | relative_url }}). | Cocina |
| **Mostrador** (counter) | Take-away or eating at the bar, each sale under a name to call the customer. | Atender mesas or Cobrar mesas |
| **Mostrador express** (express counter) | Load, send to the kitchen and charge in one go. On a phone the tab reads **Express**. | Cobrar mesas |

Anyone who handles money also sees whether the cash drawer is open, next to the tabs: **Caja abierta desde las 21:05** (drawer open since 21:05) in green, or **Caja cerrada** (drawer closed) in red.

On a staff device (the tablet or phone paired to the place, where each person signs in with their PIN) the screen is called **Venta**. On a phone outside a staff device, **Salón** sits in the bottom bar.

If the screen is empty, it tells you why:

- «Ninguna unidad de negocio atiende en el salón todavía.» (no business unit serves the dining room yet): some unit has to sell on the Salón channel. Anyone with the Ajustes permission gets a **Prender el Salón en una unidad** button (turn on the dining room for a unit), which leads to Ajustes › Unidades de negocio.
- «El salón todavía no tiene mesas.» (the dining room has no tables yet): whoever can set up the room gets **Armar sectores y mesas** (set up sections and tables). See [Sections and tables](#armar).
- «Todavía no hay dónde vender: pedile a quien administra la cuenta que te dé acceso.» (nowhere to sell yet, ask your account admin for access): your role has no sales permission.

<div class="callout"><p class="callout-title">Good to know</p><p>Salón is a module. If your account does not have it, you will not see <b>Salón</b> in the bar, nor the <b>Mesas</b> and <b>Mostrador</b> tabs.</p></div>

## Three ways to run the dining room {#formas}

Every place works its own way, and Fornu supports the three most common setups. You can mix them: an order desk loads the indoor tables while the patio waiters load from their phones.

### One order desk for the whole room

Waiters take the order at the table and pass it to one fixed person, the order desk (the *adicionista*), who loads everything from a computer or a tablet. The order desk opens each table in the name of the waiter serving it, so each bill belongs to whoever served it and you can later filter by waiter in [the day's bills](#cuentas). That takes the **Asignar quién atiende** permission (assign who serves), which the Adicionista role already has.

With a keyboard this is the fastest setup: a table number and <kbd>Enter</kbd> opens the table, a product code and <kbd>Enter</kbd> loads the product.

### Every waiter is their own order desk

There is a tablet or a computer in the room, paired to the place. Each waiter signs in with their PIN and loads their own tables, which open in their name without choosing anything. To hand the device over, tap the name in the top right corner (**Cambiar de persona**, switch person) and the next one signs in with their PIN. Pairing a device and signing in with a PIN are covered in [In the kitchen and on the road]({{ '/en/projects/fornu/manual/cocina-y-reparto/' | relative_url }}).

### The waiter with a phone

Each waiter carries a phone paired to the place, signs in with their PIN and loads the order at the table while the guests are ordering. They send it to the kitchen without walking anywhere, and the floor tells them which table has something ready to serve. With the Mozo (waiter) role they do not take payment: when the table asks for the bill they tap **Pidió la cuenta** (asked for the bill), the table turns green on every device and the cash desk takes it from there.

<div class="shot-pair">
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-telefono-mozo.jpg' | relative_url }}" alt="A waitress's phone on the Venta screen: Fichar entrada, Fichar a alguien and her name at the top, and below the dining room's tables, two busy and six free." loading="lazy" width="390" height="640">
    <figcaption>A waitress's phone, signed in with her PIN.</figcaption>
  </figure>
  <figure class="shot">
    <img src="{{ '/assets/img/fornu/manual/salon-adicionista.jpg' | relative_url }}" alt="The Venta screen on the dining room's computer: the current user's name at the top right, table 3 just opened in Valentina's name on the left, and that table's bill on the right with Valentina Sosa as the waitress" loading="lazy" width="1440" height="650">
    <ol class="marks">
      <li><b>Tomás Romero · Cambiar de persona</b> (switch person): who is using the device. Tap it to let someone else in.</li>
      <li>Table 3, open in Valentina's name.</li>
      <li>The bill says who serves it. With <b>Asignar quién atiende</b>, the name can be tapped to hand the table to someone else.</li>
    </ol>
    <figcaption>The dining room computer: Tomás loads on Valentina's table.</figcaption>
  </figure>
</div>

### Keyboard or touch

Everything works with a tap, and nearly everything with the keyboard:

| To | By touch | By keyboard |
|---|---|---|
| Open a table | Tap it on the floor. | Type its number in **Ir a mesa…** (go to table) and press <kbd>Enter</kbd>. |
| Load a product | Tap it on the menu. | Type its name or code in **Buscar producto…** (search product), pick with <kbd>↑</kbd> <kbd>↓</kbd> and press <kbd>Enter</kbd>. |
| Confirm a dialog | Tap the bottom button. | <kbd>Ctrl</kbd> + <kbd>Enter</kbd>. |
| Close a dialog | Tap the ✕ or outside it. | <kbd>Esc</kbd>. If you changed something it asks first: «Hay cambios sin guardar.» (unsaved changes). |
| Pick from a searchable list | Tap the row. | Type until one is left and press <kbd>Enter</kbd>. |
| Authorize with a PIN | The on-screen keypad. | The number keys and <kbd>Enter</kbd>. |

On a phone, if every table is named with numbers only, **Ir a mesa…** brings up the numeric keypad. Dialogs slide up from the bottom.

## Dining room permissions {#permisos}

In the dining room each action has its own permission, so each role does its part: the waiter loads and sends, the cash desk takes payment, the manager voids and discounts. Permissions are given by role, in [Staff]({{ '/en/projects/fornu/manual/personal/' | relative_url }}). Administración (the admin) can do everything.

| Permission | What it lets you do | With someone else's PIN |
|---|---|---|
| **Atender mesas** (serve tables) | Open tables in your name, load orders, remove what has not been sent yet, send it to the kitchen and mark that the table asked for the bill. | No |
| **Asignar quién atiende** (assign who serves) | Open a table in another waiter's name, or hand it over. This is what the order desk uses. | To hand a table over |
| **Mover mesas** (move tables) | Move a table to a free one, move items to another table and join tables. | Yes |
| **Anular lo mandado** (void what was sent) | Take off the bill something that already went to the kitchen, with a reason. The station gets a notice. | Yes |
| **Descontar e invitar** (discount and comp) | Discount a line or the whole bill with a reason, put something on the house, and assign customers who bring a discount. | On a line |
| **Cobrar mesas** (take payment) | Take payment in parts with tips, close the table, sell at the express counter and see the day's bills. | No |
| **Deshacer cobros** (undo payments) | Remove a payment already taken on an open table. | Yes |
| **Cancelar mesas** (cancel tables) | Cancel a whole table, with a reason. | Yes |
| **Armar el salón** (set up the room) | Create sections and tables, place them on the floor plan and set the cover charge. | Never |

The others, except Armar el salón, also need Atender mesas, and Deshacer cobros needs Cobrar mesas. How a permission is lent with a PIN is in [Borrowing a permission with someone's PIN](#autorizar).

When an account turns on Salón, Fornu creates three starter roles, unless some role already had dining room permissions. You change them like any other role, in Personal › Configuración:

| Role | Permissions |
|---|---|
| **Mozo** (waiter) | Atender mesas, Mover mesas |
| **Adicionista** (order desk) | Atender mesas, Asignar quién atiende, Mover mesas, Anular lo mandado, Descontar e invitar, Cobrar mesas |
| **Caja** (cash desk) | Atender mesas, Cobrar mesas, Descontar e invitar, Anular lo mandado, Deshacer cobros, Cancelar mesas |

Any active person whose role holds some dining room permission, other than Armar el salón, can be named as a table's waiter.

## Salón › Mesas {#mesas}

This is the live dining room. Each table shows its state by color, how long it has been open, its running total and who is serving it. It updates by itself whenever any device changes a table, so the order desk, the waiters and the cash desk all see the same thing at the same time.

<p class="perm"><span>Who can:</span> <span class="tag">Atender mesas</span> <span class="tag">Cobrar mesas</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-mesas.jpg' | relative_url }}" alt="The demo dining room in List view: two sections, Salón and Vereda, with twelve and four tables. Table 3 is busy with 8,500 pesos and the Pidió la cuenta flag. V1 is busy with 12,000. The rest read Libre." loading="lazy" width="1440" height="700">
  <ol class="marks">
    <li><b>Mesas · Delivery · Mostrador · Mostrador express</b>: where you sell. Each person sees their own.</li>
    <li><b>Caja abierta desde las…</b>: shown to whoever takes payment, so they know whether cash goes into a cash count.</li>
    <li>How many tables are busy, how many guests are seated, and what each color means.</li>
    <li><b>Plano</b> (plan) or <b>Lista</b> (list): how you see the room. Each device remembers your choice.</li>
    <li><b>Ir a mesa…</b>: a number and <kbd>Enter</kbd> open the table.</li>
    <li>A busy table: minutes open, total, guests, waiter and its flag, here <b>Pidió la cuenta</b>.</li>
  </ol>
  <figcaption>Pedidos › Venta in the demo, with the room as a list.</figcaption>
</figure>

### List or plan

In **Lista**, each section has its heading and its tables as tiles. A free table is dashed and grey, with its chairs («4 sillas», 4 chairs) and the word «Libre» (free). A busy one shows how many minutes it has been open, the total, the guests and the waiter. If part of the bill is already paid, it shows what is left.

In **Plano**, each section is drawn the way it is laid out in the place, with every table painted in its state's color, with its number and its minutes. With more than one section there is a tab per section with its count of open tables. Tables not yet placed on the plan appear underneath, under «Sin ubicar en el plano:» (not placed on the plan), and work the same when tapped.

The first time, the room opens in Plano if any table is already placed, and in Lista otherwise. With the Constructor de espacios (space builder) the plan can also show walls, textures and an isometric view (see [Spaces]({{ '/en/projects/fornu/manual/espacios/' | relative_url }}#en-el-salon)).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-plano.jpg' | relative_url }}" alt="The room in Plano view: tabs Salón with 2 open tables and Vereda with 0, and the plan with nine tables. Table 2 is painted blue and table 3 amber, both at 0 min." loading="lazy" width="1440" height="630">
  <ol class="marks">
    <li><b>Plano</b>: the room as drawn.</li>
    <li>One section per tab, with how many tables it has open.</li>
    <li>Table 2, in blue: busy.</li>
    <li>Table 3, in amber: something loaded has not been sent to the kitchen.</li>
  </ol>
  <figcaption>The same room, as a plan.</figcaption>
</figure>

### What each color means

A table shows one state only: when several apply, the one highest in this table, which is the most urgent.

| State | Color | What is going on | What the tile says |
|---|---|---|---|
| **Para servir** (ready to serve) | Orange | The kitchen finished a round and it has to go out. | «1 ronda para servir» (1 round to serve) |
| **Sin mandar** (not sent) | Amber | Something is loaded that the kitchen has not received. | «2 sin mandar» |
| **En espera** (on hold) | Dashed blue | A course is waiting for the waiter to fire it. | «Principal en espera · 12 min» (main course on hold) |
| **Pagando** (paying) | Dark green | Part of the bill is paid and the rest is pending. | «Pagando», and what is left |
| **Pidió la cuenta** (asked for the bill) | Green | The table asked for the bill. | «Pidió la cuenta» |
| **Ocupada** (busy) | Blue | Being served, nothing pending. | The total, the guests and the waiter |
| **Libre** (free) | Dashed outline | Nobody there. | «Libre» |

### Seating a table

1. Tap a free table. A small box opens next to it with the table's name and chairs.
2. If more than one business unit serves the room, pick the unit first.
3. Under **¿Cuántos se sientan?** (how many are sitting down?), tap the number. The button matching the table's chairs is highlighted.
{: .steps}

That one tap opens the table in your name and opens its bill alongside, ready to load. The box closes if you tap outside it or press <kbd>Esc</kbd>.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-sentar.jpg' | relative_url }}" alt="The box that opens on tapping free table 1: Mesa 1 · 4 sillas, the question ¿Cuántos se sientan?, buttons 1 to 8 with 4 highlighted, and the Más opciones link." loading="lazy" width="740" height="370">
  <ol class="marks">
    <li><b>¿Cuántos se sientan?</b>: one tap opens the table with that many guests.</li>
    <li><b>Más opciones…</b> (more options): for more than 8 guests, or to open it in someone else's name.</li>
  </ol>
  <figcaption>Seating four at table 1.</figcaption>
</figure>

**Más opciones…** opens the full dialog, with **Comensales** (guests, 1 to 99) and, for whoever has Asignar quién atiende, **Atiende** (served by): tap the waiter who will serve the table. If you pick nobody, the table stays in your name. Then tap **Abrir la mesa** (open the table).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-atiende.jpg' | relative_url }}" alt="The Mesa 3 dialog with the units Doble Smash and Pizzería, Comensales at 2, the note La mesa tiene 4 sillas, and Atiende with Tomás Romero and Valentina Sosa, selected" loading="lazy" width="620" height="330">
  <ol class="marks">
    <li><b>Comensales</b>, with the table's chairs as a reference.</li>
    <li><b>Atiende</b>: the order desk opens the table in Valentina's name.</li>
  </ol>
  <figcaption>Opening a table for another waitress.</figcaption>
</figure>

If two people seat the same table at once, the second one gets «La mesa 4 ya está ocupada.» (table 4 is already taken) and the floor updates.

### Going to a table by number

For the order desk on a keyboard, or the waiter who already knows the number:

1. Type the number in **Ir a mesa…**.
2. Press <kbd>Enter</kbd> or tap the arrow.
{: .steps}

It opens the table whether it is free or busy. It first looks for a table named exactly that, and otherwise for the only table with that number: «07» opens 7, and «12» opens M12 if it is the only 12. If there is none, or more than one, it says «No hay una mesa 99» (there is no table 99). A free table opened this way shows the full dialog, with the guests.

<div class="shot-phones">
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-telefono-mesas.jpg' | relative_url }}" alt="The dining room on a phone: three tables per row, table 1 busy and the rest free, with the Ir a mesa field at the top and the bottom bar with Inicio, Pedidos, Salón, Insumos and Más." loading="lazy" width="390" height="844">
    <figcaption>The floor on a phone, three tables per row.</figcaption>
  </figure>
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-telefono-ir-a-mesa.jpg' | relative_url }}" alt="On a phone, the Mesa 3 dialog sliding up from the bottom, with Comensales at 2, the note La mesa tiene 4 sillas and the buttons Cancelar and Abrir la mesa." loading="lazy" width="360" height="740">
    <figcaption>Going to table 3, which was free.</figcaption>
  </figure>
</div>

## The open table {#mesa}

Tapping a busy table opens its bill. On a computer it appears next to the floor, so you never lose sight of the room. On a smaller screen it takes the whole space, with an arrow at the top to go back. This is where you load what the table orders, send it to the kitchen in rounds, and mark or take the bill.

<p class="perm"><span>Who can:</span> <span class="tag">Atender mesas</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-mesa.jpg' | relative_url }}" alt="Table 1 open next to the floor: two guests, no customer chosen, the Abierta state, the Cuenta tab with a 2, the product search, the Sin mandar block with a Doble cheddar and a Triple bacon, the cover charge for two guests and the Mandar a la cocina · 2 button." loading="lazy" width="1440" height="630">
  <ol class="marks">
    <li>The table on the floor: «2 sin mandar» warns that the kitchen has not received something yet.</li>
    <li>Guests, customer and state. Above them, the bill number, business unit, waiter and how long it has been open.</li>
    <li><b>Carta</b> (menu) and <b>Cuenta</b> (bill). The number next to Cuenta is what is still unsent.</li>
    <li><b>Buscar producto…</b>: by name, category or code.</li>
    <li><b>Sin mandar</b>: what is loaded, with the pencil to change it and the ✕ to remove it.</li>
    <li><b>Mandar a la cocina · 2</b> (send to the kitchen): sends what is loaded as one round.</li>
  </ol>
  <figcaption>Table 1 with two products loaded.</figcaption>
</figure>

The bar at the bottom always holds the next step: **Mandar a la cocina** when something is loaded, **Marchar** (fire) when a course is on hold, **Pidió la cuenta** and, for whoever takes payment, **Cobrar $ …** (charge), or **Cerrar sin cargo** (close at no charge) when the bill comes to zero. The bill's state can be **Abierta** (open), **Pidió la cuenta**, **Cobrada** (paid) or **Cancelada** (cancelled), and the **Más acciones** (⋯, more actions) menu gathers what applies to the whole table.

### Loading what they order

There are three ways, and you can mix them:

- **Tapping the menu.** Products are grouped by category, each with its code if it has one, its name and its price. A product without options goes on the bill with one tap. Tapping it again adds one to the same line: three sodas are one line of 3.
- **Searching.** Type part of the name or category in **Buscar producto…**. Pick with <kbd>↑</kbd> <kbd>↓</kbd> and add it with <kbd>Enter</kbd>. <kbd>Esc</kbd> clears the search.
- **By code.** If products have a code in the [Menu]({{ '/en/projects/fornu/manual/carta/' | relative_url }}), like «A7», type the whole code and press <kbd>Enter</kbd>: the product with that code comes first. It is the fastest way for the order desk.

Each line is saved the moment you add it, so every other device sees it right away. Sold-out products read «Agotado hoy» (sold out today) on the menu and «Agotado» in the search, and cannot be added.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-buscar.jpg' | relative_url }}" alt="The search box with the word Papa and one suggestion: Papas fritas, in the Para acompañar category, at 4,500 pesos. Underneath, the menu with Burgers and Para acompañar." loading="lazy" width="510" height="390">
  <figcaption>Searching «Papa»: <kbd>Enter</kbd> adds the fries.</figcaption>
</figure>

A product with options (how the meat is cooked, extras) opens a dialog first. Each group says how many to choose («elegí 1», choose 1, «hasta 2», up to 2, «de 1 a 3», 1 to 3) and each option its extra price («+$ 800») or «agotado». At the bottom are **Cantidad** (quantity) and **Aclaración (opcional)** (special request), for example «Sin pepinos» (no pickles). Tap **Agregar · $ …** (add). If a required group is missing, Fornu tells you which one.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-opciones.jpg' | relative_url }}" alt="The Doble cheddar dialog with Extras up to 3, one Extra cheddar chosen, Sumale una bebida up to 1 with the soda chosen, Cantidad 1, the note Sin pepinos and the Agregar · $ 12.800 button" loading="lazy" width="620" height="900">
  <ol class="marks">
    <li>A group and how many to choose: «hasta 3» (up to 3). Options that can be ordered more than once have − and +.</li>
    <li>Another group, «hasta 1»: one tap chooses.</li>
    <li><b>Cantidad</b> (quantity).</li>
    <li><b>Aclaración (opcional)</b> (note).</li>
    <li><b>Agregar · $ …</b> (add), with the price of what was chosen.</li>
  </ol>
  <figcaption>A Doble cheddar with extra cheddar and a soda.</figcaption>
</figure>

### Courses: Cargando para {#tiempos}

If your menu uses courses, what you load does not all go out together. The kitchen gets what comes first, and the rest waits until the waiter fires it. That way the main course does not come out with the starter.

Courses appear once some menu category has a **Va de** (goes as) other than Principal, set under Carta › Categorías. The bill then shows the **Cargando para** row (loading for):

| Option | What it does |
|---|---|
| **Según la carta** (as on the menu) | Each product goes in its category's course. Categories without one go as Principal. This is the default. |
| **Ya** (now) | Goes out with the next round, like drinks. |
| **Entrada**, **Principal**, **Postre** (starter, main, dessert) | Everything you load now goes in that course, whatever its category. |

Pick the course before tapping the products. Unsent lines show a small tag with their course.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-cargando-para.jpg' | relative_url }}" alt="Table 1 with the Cargando para row: Según la carta, Ya, Entrada, Principal selected and Postre. On the floor the table reads 2 sin mandar, and the Cuenta tab has a 2." loading="lazy" width="1440" height="630">
  <ol class="marks">
    <li>The table shows «2 sin mandar».</li>
    <li><b>Cargando para</b>: here, the next items go as main course.</li>
    <li>The bill, with two lines still to send.</li>
  </ol>
  <figcaption>Whatever is loaded now goes out as main course.</figcaption>
</figure>

Sending takes everything in **Ya** plus the first course loaded, unless that course already has something on hold. Later courses stay **en espera** (on hold): they take no stock and print no ticket until fired. The floor shows it, for example «Principal en espera · 12 min», so the waiter knows how long it has been waiting.

When the time comes, tap **Marchar principal** (fire the main course), in the block on hold or in the bottom bar. It goes out as the next round and Fornu says «Principal marchado a la cocina.» (main course fired).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-en-espera.jpg' | relative_url }}" alt="Table 1 with the tile Principal en espera · 0 min, and on the bill the block Principal · en espera with a canned soda and the Marchar principal button, Ronda 1 in the kitchen underneath, and at the bottom the Marchar principal and Pidió la cuenta buttons." loading="lazy" width="1440" height="510">
  <ol class="marks">
    <li>On the floor: which course is waiting and for how long.</li>
    <li><b>Principal · en espera</b>: what has not gone to the kitchen, with its own button to fire it.</li>
    <li><b>Marchar principal</b>, also in the bottom bar.</li>
  </ol>
  <figcaption>Round 1 is in the kitchen and the main course is on hold.</figcaption>
</figure>

<div class="callout tip"><p class="callout-title">Tip</p><p>Sending never sends a later course. If a table wants everything at once, load it under <b>Ya</b>.</p></div>

### Sending to the kitchen

1. Check the **Sin mandar** block.
2. Tap **Mandar a la cocina · 2**. The number is how many units go out.
3. Fornu says «Mandado a la cocina.» (sent to the kitchen) and what was loaded becomes **Ronda 1** (round 1).
{: .steps}

Each round takes its stock, prints a ticket at every station that makes something in it (see [Kitchen stations]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#estaciones)) and shows up on the [kitchen board]({{ '/en/projects/fornu/manual/pedidos/' | relative_url }}#tablero). If there is nothing new, Fornu says «No hay nada nuevo para mandar a la cocina.» (nothing new to send), and if what is left is a course on hold, «Lo que queda está en espera: marchalo cuando sea su tiempo.» (what is left is on hold, fire it when it is time).

On the bill, rounds are listed newest first. Each shows its state (**En la cocina**, in the kitchen, **Lista para servir**, ready to serve, or **En la mesa**, at the table), the time it went out and, if it went to more than one station, which ones.

### Changing or removing what has not been sent

Until it is sent, a line can be changed or removed without leaving a trace.

- **The pencil** opens the line with its name at the top: **Cantidad** (1 to 99), **Va de** if the menu uses courses, and **Nota para la cocina (opcional)** (note for the kitchen), for example «Sin sal, bien cocido, sin hielo…» (no salt, well done, no ice). Below are its category's quick notes: tap one to add it to the note, tap again to remove it. Tap **Guardar** (save), or **Sacar de la mesa** (remove from the table) to take it off.
- **The ✕** removes it at once. Fornu says «Sacaste 1 × Doble cheddar.» (you removed 1 × Doble cheddar) with a **Deshacer** (undo) button that puts it back exactly as it was.

If another device changed the same line while you were editing it, Fornu tells you how many there are now and asks you to look again.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-nota.jpg' | relative_url }}" alt="The dialog for an unsent canned soda: Cantidad 1, Va de with Principal selected, the note Sin sal, and the quick notes Sin sal, selected, and Con cheddar." loading="lazy" width="620" height="380">
  <ol class="marks">
    <li><b>Cantidad</b>.</li>
    <li><b>Va de</b>: which course it goes in.</li>
    <li><b>Nota para la cocina</b>: printed on the ticket.</li>
    <li>The category's quick notes: one tap instead of typing.</li>
  </ol>
  <figcaption>Changing a line before sending it.</figcaption>
</figure>

<div class="callout tip"><p class="callout-title">Tip</p><p>Quick notes are set per category under Carta › Categorías, one per line (for example «Jugoso», «A punto», «Cocido»: rare, medium, well done). They appear when you tap the pencil on an unsent line, not when you first load the product.</p></div>

<div class="callout"><p class="callout-title">Good to know</p><p>Once sent, a line can only be <a href="#anular">voided</a>, with a reason, and Fornu records who did it.</p></div>

### Ready to serve and La llevé

When the kitchen marks a round as ready, the table turns orange on the floor with «1 ronda para servir», and on the bill that round reads **Lista para servir**. The waiter takes it out and taps **La llevé** (I took it): the round becomes **En la mesa**, Fornu says «Ronda 1 en la mesa.» (round 1 at the table) and the card leaves the kitchen board.

<div class="shot-phones">
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-ronda-para-servir.jpg' | relative_url }}" alt="The floor on a phone, dark theme: table 1 with an orange edge and the flag 1 ronda para servir, and table 2 in green with Pidió la cuenta." loading="lazy" width="390" height="640">
    <figcaption>Table 1 has something to serve.</figcaption>
  </figure>
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-la-lleve.jpg' | relative_url }}" alt="Table 1's bill on the phone: Ronda 1 with the Lista para servir tag and the La llevé button, two portions of fries with the note Bien cocidas." loading="lazy" width="390" height="640">
    <figcaption>The round is ready: <b>La llevé</b>.</figcaption>
  </figure>
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-en-la-mesa.jpg' | relative_url }}" alt="The same bill after tapping La llevé: the message Ronda 1 en la mesa and the round in the En la mesa state." loading="lazy" width="390" height="640">
    <figcaption>Round 1 at the table.</figcaption>
  </figure>
</div>

### Guests and cover charge

Change the guests with − and + in the bill's header, while the table is open and has no payments. If the place charges a cover (set in [Sections and tables](#armar)), the bill adds it per guest: «Cubierto · 2 × $ 1.500».

Below the lines, the bill shows **Productos** (products, when there is a cover or a discount), **Cubierto** (cover), **Descuento** (discount) with its reason, **Total**, **IVA contenido** (VAT included) if the account is a Responsable Inscripto, and **Pagado** (paid) and **Saldo** (balance) once there are payments.

### The table asked for the bill

1. When the table asks for the bill, tap **Pidió la cuenta**.
2. The table turns green on every device and the bill reads **Pidió la cuenta**.
3. If the kitchen has a receipt printer, the pre-bill prints: «La mesa pidió la cuenta: la precuenta sale por la impresora.» (the pre-bill is printing).
{: .steps}

The pre-bill (*precuenta*) prints by itself the first time. For another copy, use **Más acciones** (⋯) › **Imprimir la precuenta** (print the pre-bill). Without a receipt printer, the browser's print dialog opens with a sheet carrying the place's name, the table and its number, the date, who served, the guests, the lines, the cover, the discount, the total, the VAT included, what was paid and the balance, and at the foot «No válido como factura.» (not valid as an invoice).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-precuenta.jpg' | relative_url }}" alt="Table 4's printed pre-bill: the kitchen, the table and its number, the date, who served, two guests, each line with its amount, the cover charge and the total" loading="lazy" width="330" height="300">
  <figcaption>The pre-bill printed from the browser.</figcaption>
</figure>

If anything else is loaded afterwards, the table no longer counts as having asked for the bill. If a course is still on hold, Fornu will not mark it: «Hay postre en espera: marchalo o sacalo antes de cobrar.» (dessert is on hold, fire it or remove it before charging).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-pidio-la-cuenta.jpg' | relative_url }}" alt="Table 1 in green with the Pidió la cuenta flag, its bill with the Pidió la cuenta state, the three-dot menu below, and the message La mesa pidió la cuenta: la precuenta sale por la impresora." loading="lazy" width="1440" height="630">
  <ol class="marks">
    <li>On the floor, the table turns green.</li>
    <li>The bill's state.</li>
    <li><b>Más acciones</b> (⋯): to reprint the pre-bill.</li>
    <li>The message that the pre-bill printed.</li>
  </ol>
  <figcaption>Table 1 asked for the bill.</figcaption>
</figure>

### On a phone

On a phone the bill takes the whole screen, and the arrow at the top goes back to the floor. **Carta** and **Cuenta** are two tabs. While you are on the menu with something loaded, a bar appears at the bottom with «2 sin mandar · $ 25.700» (tap it to see the bill) and a **Mandar** (send) button, so you can send without switching tabs.

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/salon-telefono-sin-mandar.jpg' | relative_url }}" alt="Table 9 on a waitress's phone, on the Carta tab, with the bottom bar reading 2 sin mandar · $ 6.500 and the Mandar button" loading="lazy" width="390" height="844">
  <ol class="marks">
    <li>What is left to send: tap it to see the bill.</li>
    <li><b>Mandar</b> (send), without leaving the menu.</li>
  </ol>
  <figcaption>The bar for what is left to send, on a phone.</figcaption>
</figure>

## On a line or on the whole table {#acciones}

Whatever already went to the kitchen gets voided, discounted or moved, and Fornu always records who did it. Each sent line has its own ⋯ menu, and the table has its own, **Más acciones** (⋯), in the header. A line's menu appears while the table is open, the line is not voided and there are no payments yet.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-menu-mesa.jpg' | relative_url }}" alt="Table 2's Más acciones menu open: Mover la mesa entera, Mover ítems, Unir con otra mesa, Pasarla a otro mozo, Reimprimir la ronda 1, Imprimir la precuenta and Cancelar la mesa" loading="lazy" width="510" height="520">
  <figcaption>A table's <b>Más acciones</b> (⋯) menu.</figcaption>
</figure>

An option with a padlock means your role lacks that permission: you can still use it, and Fornu asks for the PIN of someone who has it (see [Borrowing a permission with someone's PIN](#autorizar)).

### Voiding what was sent {#anular}

<p class="perm"><span>Who can:</span> <span class="tag">Anular lo mandado</span></p>

1. Tap ⋯ on the line and choose **Anular** (void).
2. If the line has several units, choose how many under **Cuántos** (how many, «1 de 2»).
3. Choose **¿Por qué?** (why?): Error de carga (loading mistake), Se arrepintió (changed their mind), Salió mal (came out wrong), Demora (delay), No había (we were out) or Otro (other). With Otro, explain in **Nota**.
4. Tap **Anular** (or **Anular 1 de 2**).
{: .steps}

The line stays on the bill, struck through, with «Anulado por Administración: Salió mal» (voided by Administración: came out wrong). The stock stays taken, since the kitchen already used it. If that station's ticket was already printed, the station gets an **ANULADO** (voided) ticket with the reason and who voided it. If it had not printed yet, the line simply does not appear on it.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-anular.jpg' | relative_url }}" alt="The Anular 2 × Papas fritas dialog: the text Ronda 1, mandada a las 12:41, Cuántos at 1 de 2, the reasons Error de carga, Se arrepintió, Salió mal (selected), Demora, No había and Otro, and the Nota field." loading="lazy" width="620" height="420">
  <ol class="marks">
    <li><b>Cuántos</b>: one of the two portions.</li>
    <li><b>¿Por qué?</b>: the reason is required.</li>
    <li><b>Nota</b>: optional, added to the reason. Required with «Otro».</li>
  </ol>
  <figcaption>Voiding one of two portions of fries.</figcaption>
</figure>

### Discounting or comping a line {#descontar}

<p class="perm"><span>Who can:</span> <span class="tag">Descontar e invitar</span></p>

1. Tap ⋯ on the line and choose **Descontar…** (discount).
2. If it has several units, choose how many.
3. Choose the **Motivo** (reason). Each reason brings its percentage, which you can change under **Porcentaje**. The footer says how much comes off: «Se descuentan $ 2.000».
4. Tap **Descontar**. At 100%, the button reads **Invitar** (on the house).
{: .steps}

The line stays on the bill and still counts as sold, so its stock is taken. It shows the old price struck through and «−10% · Cliente habitual» (regular customer) or «Invitado · Invita la casa» (on the house). To undo it, ⋯ › **Sacar el descuento** (remove the discount). Reasons and their percentages are set under Ajustes › Descuentos (see [Settings]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }})). If there are none, Fornu says «No hay motivos de descuento: cargalos en Ajustes.» (no discount reasons, add them in Settings).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-descontar.jpg' | relative_url }}" alt="The Descontar Gaseosa en lata dialog: the text Queda en la cuenta con su descuento y se vende igual, the reasons Invita la casa 100% (selected), Consumo del personal 100%, Cliente habitual 10% and Demora 10%, and Porcentaje at 100." loading="lazy" width="620" height="370">
  <ol class="marks">
    <li><b>Motivo</b>: the account's reasons, with their percentage.</li>
    <li><b>Porcentaje</b>: filled in for you, and editable.</li>
  </ol>
  <figcaption>Putting a soda on the house.</figcaption>
</figure>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-cuenta-descuentos.jpg' | relative_url }}" alt="Round 1 of a bill: fries struck through with Anulado por Administración: Salió mal, a soda with its 2,000 price struck through, 0 pesos and Invitado · Invita la casa, and more fries at 4,500 with their three-dot menu." loading="lazy" width="510" height="240">
  <ol class="marks">
    <li>A voided line, with who and why.</li>
    <li>A comped line, with its price struck through.</li>
    <li>The ⋯ menu of a sent line.</li>
  </ol>
  <figcaption>How they look on the bill.</figcaption>
</figure>

A discount on the whole bill is applied when [taking payment](#descuento-cuenta).

### Assigning a customer {#cliente}

<p class="perm"><span>Who can:</span> <span class="tag">Atender mesas</span> <span class="tag">Descontar e invitar</span></p>

A known customer can bring their own discount: the owners who eat for free, the staff at 50%. Assign them and the discount applies itself.

1. Tap **Cliente** (customer) in the bill's header.
2. Under **¿Para quién es?** (who is it for?), search by name or phone. Each row shows the phone and the discount («100% · Invita la casa») or «Sin descuento» (no discount).
3. Tap the customer.
{: .steps}

The customer's discount applies to the whole bill and is recorded under its reason or the customer's name. A discount typed by hand afterwards replaces it. **Sin cliente** (no customer) removes the customer and the discount it brought.

Anyone who serves tables can assign a customer without a discount. Customers with a discount are greyed out for anyone without Descontar e invitar, reading «Trae 100% de descuento: lo asigna quien puede descontar.» (brings 100% off, assigned by whoever can discount), and this cannot be lent with a PIN. Customers are added under Pedidos › Clientes. With none yet: «Todavía no hay clientes: se cargan en Pedidos → Clientes.».

<div class="shot-pair">
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-cliente-telefono.jpg' | relative_url }}" alt="On a waitress's phone, the ¿Para quién es? dialog with the search box, the customer Ana with her phone number, and Dueños greyed out with the text Trae 100% de descuento: lo asigna quien puede descontar." loading="lazy" width="390" height="314">
    <figcaption>For a waitress, Dueños (owners) is greyed out.</figcaption>
  </figure>
  <figure class="shot">
    <img src="{{ '/assets/img/fornu/manual/salon-cliente.jpg' | relative_url }}" alt="Table 1's bill with the customer Dueños in the header, fries at 4,500, the line Descuento 100% · Invita la casa for minus 4,500 and the Cerrar sin cargo button." loading="lazy" width="510" height="630">
    <ol class="marks">
      <li>The assigned customer, in place of «Cliente».</li>
      <li>Its discount, on the whole bill.</li>
      <li><b>Cerrar sin cargo</b>: the bill came to zero.</li>
    </ol>
    <figcaption>The owners' table.</figcaption>
  </figure>
</div>

### Moving items to another table {#mover}

<p class="perm"><span>Who can:</span> <span class="tag">Mover mesas</span></p>

For when someone changes tables, or part of a table moves to the bar.

1. Tap **Más acciones** (⋯) › **Mover ítems…** (move items). From a line, ⋯ › **Mover a otra mesa…** (move to another table) opens the same thing with that line already ticked.
2. Tick what moves, or **Todo** (everything). Each line says whether it is unsent, on hold or which round it is in. For lines with several units, choose how many.
3. Under **¿A qué mesa?** (to which table?), tap the table. Free ones read «4 sillas · libre». Busy ones show their total, guests and waiter.
4. If the table is free, set the **Comensales**: it opens with what you move, in the same waiter's name.
5. Tap **Mover a Mesa 2** (move to table 2).
{: .steps}

If the other table is busy, what you move is added to its bill. Sent items keep their round and their place in the kitchen, and unsent ones wait to be sent from the other table. That table stops counting as having asked for the bill. Voided lines do not move, and both tables have to sell from the same menu.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-mover.jpg' | relative_url }}" alt="The Mover ítems de Mesa 1 dialog: the Todo checkbox, the line Papas fritas · ronda 1 ticked with 1 de 2, and below ¿A qué mesa? with tables 2 to 8 of the Salón section, all 4 sillas · libre." loading="lazy" width="620" height="440">
  <ol class="marks">
    <li><b>Todo</b>: moves the whole bill.</li>
    <li>A ticked line, with how many units move.</li>
    <li><b>¿A qué mesa?</b>: the place's tables, by section.</li>
  </ol>
  <figcaption>Moving one portion of fries to another table.</figcaption>
</figure>

### Moving the whole table

<p class="perm"><span>Who can:</span> <span class="tag">Mover mesas</span></p>

**Más acciones** (⋯) › **Mover la mesa entera** (move the whole table) lists the free tables by section. Tap one and the table moves with everything on it. Fornu says «Mesa 1 → Mesa 2.» with a **Deshacer** button that moves it back.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-mover-mesa.jpg' | relative_url }}" alt="The Mover Mesa 2 panel with the free tables in the Salón and the Vereda, each with its chairs" loading="lazy" width="620" height="420">
  <figcaption>Free tables, by section. One tap moves the table.</figcaption>
</figure>

### Joining with another table

<p class="perm"><span>Who can:</span> <span class="tag">Mover mesas</span></p>

1. Tap **Más acciones** (⋯) › **Unir con otra mesa…** (join with another table). Only busy tables are listed.
2. Choose the table. Fornu explains what will happen: «3 comensales y todo lo pedido pasan a Mesa 2, con su ronda y su lugar en la cocina. Mesa 1 queda libre.» (3 guests and everything ordered move to table 2, keeping their round and place in the kitchen, table 1 becomes free).
3. Tap **Unir con Mesa 2**.
{: .steps}

The screen jumps to the table that received everything. The other one closes as cancelled, with «Unida a Mesa 2» (joined to table 2).

### Handing it to another waiter

<p class="perm"><span>Who can:</span> <span class="tag">Asignar quién atiende</span></p>

When the shift changes or a waiter leaves: **Más acciones** (⋯) › **Pasarla a otro mozo** (hand it to another waiter), or tap the waiter's name in the header. Under **¿Quién la atiende?** (who serves it?) search for the name and tap it (<kbd>Enter</kbd> picks the only one left). Fornu says «La mesa cambió de mozo.» (the table changed waiter).

If nobody can serve, Fornu says «Nadie del local tiene un rol que atienda mesas: se asigna en Personal → Equipo.» (nobody here has a role that serves tables, assign one under Staff › Team).

### Reprinting a round

**Más acciones** (⋯) › **Reimprimir la ronda 1** (reprint round 1) sends another copy of that ticket, marked **REIMPRESIÓN** (reprint): «Ronda 1: sale otra copia.».

### Cancelling the table

<p class="perm"><span>Who can:</span> <span class="tag">Cancelar mesas</span></p>

For the table that gets up and leaves, or one opened by mistake. It also works for a counter sale.

1. Tap **Más acciones** (⋯) › **Cancelar la mesa** (cancel the table).
2. Read what will happen: «Lo que no se mandó sale; lo mandado queda anulado con este motivo, y su stock sigue descontado.» (unsent items are removed, sent items are voided with this reason and their stock stays taken).
3. Choose the reason, from the same list as when voiding. If nothing was sent, the reason is optional and it is recorded as «Se levantó sin pedir» (left without ordering).
4. Tap **Cancelar la mesa**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-cancelar-mesa.jpg' | relative_url }}" alt="The Cancelar Mesa 2 panel with what will happen, the reasons Error de carga, Se arrepintió, Salió mal, Demora, No había and Otro, and the optional note" loading="lazy" width="620" height="420">
  <figcaption>Cancelling a table asks for the reason.</figcaption>
</figure>

Stations that had already printed something get their **ANULADO** notice. Fornu says «Mesa cancelada.».

<div class="callout"><p class="callout-title">Good to know</p><p>Once payments are taken the bill is locked: no voiding, no discounts, no changing guests or customer, no moving items, no joining and no cancelling. First <a href="#anular-pago">remove the payments</a>, which takes the Deshacer cobros permission.</p></div>

## Borrowing a permission with someone's PIN {#autorizar}

A waiter does not need every permission to sort things out at the table. If their role lacks one of the permissions that can be lent, the option shows a padlock. They use it anyway, and before it goes through Fornu asks for the PIN of someone who has it, like the manager.

1. Choose the option with the padlock and fill in the usual dialog: the reason, the discount or the target table.
2. **Hace falta autorización** (authorization needed) appears, with a summary of the action, for example «Anular 1 × Papas fritas (ronda 1) de Mesa 1».
3. Under **¿Quién autoriza?** (who authorizes?), tap the person. People on shift come first, marked «· en turno» (on shift). If there is only one, they are already selected.
4. That person types their PIN, 4 to 6 digits, on the on-screen keypad or the device's keyboard, and taps **Autorizar** (authorize).
{: .steps}

The authorization covers that one action and lasts two minutes. The bill records who did it and who authorized it: «Anulado por Mariana (autorizó Diego): Se arrepintió» (voided by Mariana, authorized by Diego: changed their mind).

<div class="shot-phones">
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-autorizar-menu.jpg' | relative_url }}" alt="Table 1's bill on Mariana's phone, with a line's menu open: Descontar with a padlock, Mover a otra mesa without one, and Anular in red with a padlock." loading="lazy" width="390" height="520">
    <figcaption>Mariana can move, but not void or discount.</figcaption>
  </figure>
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-autorizar-pin.jpg' | relative_url }}" alt="The Hace falta autorización dialog: the summary Anular 1 × Papas fritas (ronda 1) de Mesa 1, ¿Quién autoriza? with Diego selected, four circles for the PIN and a 0 to 9 keypad." loading="lazy" width="390" height="560">
    <figcaption>Diego authorizes with his PIN.</figcaption>
  </figure>
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-autorizar-hecho.jpg' | relative_url }}" alt="The bill afterwards: the message Papas fritas: anulado, and the line struck through with Anulado por Mariana (autorizó Diego): Se arrepintió. The total is 0." loading="lazy" width="390" height="660">
    <figcaption>The bill records who voided and who authorized.</figcaption>
  </figure>
</div>

These go through a PIN when the permission is missing:

- **Anular** on a line.
- **Descontar…** and **Sacar el descuento** on a line.
- **Mover la mesa entera**, **Mover ítems…**, **Mover a otra mesa…** and **Unir con otra mesa…**.
- **Pasarla a otro mozo**.
- **Anular este pago** (void this payment).
- **Cancelar la mesa**.

These do not go through a PIN, and without the permission they simply do not appear: taking payment, the whole-bill discount when taking payment, assigning a customer who brings a discount, and opening a table in someone else's name. **Armar el salón** is never lent.

What can go wrong:

- «PIN incorrecto · quedan 4 intentos.» (wrong PIN, 4 attempts left). After too many attempts, that person is locked out for a few minutes, just like at sign-in.
- «Diego no puede autorizar eso.» (Diego cannot authorize that) or «Diego todavía no tiene PIN: pedíselo a la administración.» (Diego has no PIN yet).
- «Nadie de este local puede autorizar esto con su PIN: se da en Personal → Configuración, en el rol de quien corresponda.» (nobody here can authorize this, it is given under Staff › Configuration, in the right person's role).

## Taking payment {#cobrar}

The cash desk takes payment from the table's bill: all at once, by what each person had, or in equal parts, with one or several payment methods and with tips. Without the Cobrar mesas permission the button does not appear, and the waiter uses **Pidió la cuenta** instead.

<p class="perm"><span>Who can:</span> <span class="tag">Cobrar mesas</span></p>

The **Cobrar $ …** button appears at the bottom once nothing is unsent or on hold. If the bill comes to zero (the owners' table, say), it reads **Cerrar sin cargo**. It opens the dialog «Cobrar Mesa 1» (charge table 1), or «Cobrar Mesa 1 · saldo $ 7.500» (balance) if there are payments already.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-cobrar.jpg' | relative_url }}" alt="The Cobrar Mesa 1 dialog on Todo: on the left what was had, three sodas and two portions of fries for 15,000. On the right Aplicar un descuento, the payment methods with Efectivo selected, Monto 15,000, Propina 0, Paga con 30,000, the buttons Justo, 20,000, 30,000 and 50,000, Vuelto 15,000, Otro pago, Comprobante with Facturar esta cuenta, and at the bottom Cobrar $ 15.000 en Efectivo." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li><b>Todo</b> (all), <b>Por ítems</b> (by items) or <b>Partes iguales</b> (equal parts): how the bill is split.</li>
    <li><b>Aplicar un descuento</b> (apply a discount): on the whole bill, before the first payment.</li>
    <li><b>Medio de pago</b> (payment method): one button per method. Cash comes selected if the account takes it.</li>
    <li><b>Monto</b> (amount) and <b>Propina</b> (tip).</li>
    <li><b>Paga con</b> (pays with), the likely bills and the <b>Vuelto</b> (change).</li>
    <li>The button says how much is charged and how.</li>
  </ol>
  <figcaption>Charging 15,000 in cash for a 30,000 note.</figcaption>
</figure>

### Charging it all at once

1. Tap **Cobrar $ …**. The dialog opens on **Todo**, with the balance in **Monto**.
2. Choose the **Medio de pago**.
3. If they leave a tip, type it under **Propina**. A line below shows how much to run through with the tip included.
4. For cash, tap what they hand you: **Justo** (exact) or one of the notes Fornu suggests. The **Vuelto** shows in large type.
5. Tap **Cobrar $ 15.000 en Efectivo** (charge in cash) or press <kbd>Ctrl</kbd> + <kbd>Enter</kbd>.
{: .steps}

The table closes and Fornu says «Mesa cerrada.» (table closed). The cash goes into the drawer, with the tip recorded separately.

The suggested notes are the total rounded up to 1,000, 10,000, 20,000, 50,000 or 100,000, the three smallest. If what they hand you is not enough, Fornu says «Es menos que $ 15.000.» (that is less than $ 15,000).

### Paying with more than one method

**Otro pago** (another payment) adds a row with what is missing. If nothing is missing, it splits the last row in two. Each row has its method, its amount, its tip and a ✕ to remove it, which gives its amount back to the row above. A line says «Los pagos cubren la cuenta.» (the payments cover the bill), «Faltan $ 2.000.» (2,000 missing) or «Sobran $ 500.» (500 too much), and the button becomes **Cobrar 2 pagos** (charge 2 payments).

### By items: each person pays for their own

1. Tap **Por ítems**.
2. Under **Qué paga esta persona** (what this person pays), tick their items. For lines with several units, choose how many («1 de 2»).
3. If there is a cover charge, add their **Cubiertos**.
4. Choose the method and the tip, and tap **Cobrar**.
{: .steps}

The dialog stays open for the next person, with the same payment method, and what was paid moves to **Ya pagado** (already paid) with its payment number. On the right, **Este pago** (this payment) shows the items, the cover, the share of the discount if there is one, and what they pay. When that payment settles the bill, it reads **Lo que queda** (what is left). If the amount is more than what is left, Fornu asks you to charge it under **Todo**.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-por-items.jpg' | relative_url }}" alt="Cobrar Mesa 1 on Por ítems: 1 of 2 portions of fries ticked, a soda unticked, Cubiertos 1 of 3. On the right Este pago, 1 ítem 4,500, Cubierto × 1 500, Paga 5,000, Débito selected and the note Después de este pago quedan $ 7.500: la mesa sigue abierta." loading="lazy" width="880" height="570">
  <ol class="marks">
    <li><b>Qué paga esta persona</b>: their items, with how many units.</li>
    <li><b>Cubiertos</b>: this person's cover.</li>
    <li><b>Este pago</b>: the breakdown and what they pay.</li>
    <li>What is left afterwards, and that the table stays open.</li>
  </ol>
  <figcaption>One guest pays for their fries and cover by debit card.</figcaption>
</figure>

### Equal parts

1. Tap **Partes iguales**.
2. Under **Entre** (split between), set the number of parts. It starts at the number of guests, or at what was chosen in an earlier payment.
3. Charge «Parte 1 de 3» (part 1 of 3), then part 2, and so on.
{: .steps}

Each part is what is left divided by the parts still to pay. The last one takes the leftover cents. You cannot go below the parts already paid plus one, and the hint reads «Ya pagaron 1 de 2.» (1 of 2 already paid). You can combine modes: one guest pays for their own by items and the rest is split equally.

While something is still owed, the table reads **Pagando** on the floor and its tile shows what is left.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-partes.jpg' | relative_url }}" alt="Cobrar Mesa 1 · saldo 7.500 on Partes iguales: on the left what was had and an earlier 5,000 debit payment for 1 item and 1 cover. On the right Entre 2, La mesa tiene 3 comensales, Parte 1 de 2 for 3,750. On the floor, table 1 reads Pagando." loading="lazy" width="1440" height="480">
  <ol class="marks">
    <li>On the floor, the table is paying in parts.</li>
    <li><b>Partes iguales</b>.</li>
    <li><b>Entre</b>: how many parts.</li>
    <li>The part being charged now.</li>
    <li>The earlier payment, made by items.</li>
  </ol>
  <figcaption>After a payment by items, the rest split between two.</figcaption>
</figure>

### Discount on the whole bill {#descuento-cuenta}

<p class="perm"><span>Who can:</span> <span class="tag">Descontar e invitar</span></p>

**Aplicar un descuento** appears before the first payment, only for whoever can discount. It lists the reasons with their percentage: tapping one that has a percentage applies it right away («Descuento aplicado.», discount applied). You can also type the **Porcentaje** and tap **Aplicar el descuento**, or **Invitar la cuenta** (put the bill on the house) at 100%. **Sacar el descuento** removes it. If you left a change unapplied, Fornu says «Aplicá el descuento antes de cobrar.» (apply the discount before charging).

If the bill comes to zero, the dialog says «No hay nada que cobrar» (nothing to charge) and the button becomes **Cerrar sin cargo**.

### Invoicing when you charge

With the Facturación (invoicing) module, the payment that closes the table has a **Comprobante** (receipt) section with **Facturar esta cuenta** (invoice this bill). Tick it and these appear:

- **Condición frente al IVA** (VAT status): Consumidor final (end consumer), Responsable inscripto, Monotributista or Exento.
- **Documento** (ID type): Sin identificar (none), DNI or CUIT. Any status other than end consumer requires a CUIT.
- **CUIT** or **DNI**. From the seventh digit on, Fornu shows underneath who has already been invoiced with that number, and one tap fills everything in.
- **Razón social** (company name) or **Nombre**, **Domicilio** (address), **Teléfono** and **Email**, to send them the receipt.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-facturar.jpg' | relative_url }}" alt="The Comprobante section of the payment dialog: Facturar esta cuenta ticked, Condición frente al IVA set to Responsable inscripto and Documento locked to CUIT. Under the typed CUIT, a company already invoiced with that number, with its VAT status, its address and the last time. Further down Razón social, Domicilio, Teléfono and Email, and the notice La facturación está apagada en esta cuenta: prendela en Facturación para emitir el comprobante." loading="lazy" width="485" height="750">
  <ol class="marks">
    <li><b>Facturar esta cuenta</b>.</li>
    <li><b>Condición frente al IVA</b> and <b>Documento</b>: a Responsable inscripto requires a CUIT.</li>
    <li>The <b>CUIT</b>.</li>
    <li>Who has already been invoiced with that number: one tap fills in their details.</li>
    <li>With invoicing turned off in the account, Fornu warns you («La facturación está apagada en esta cuenta…», invoicing is off in this account), and the table still closes.</li>
  </ol>
  <figcaption>Invoicing a Responsable inscripto when taking payment.</figcaption>
</figure>

Below, it says what will be issued, for example «Saldrá una Factura B por $ 15.000 a consumidor final. ARCA la autoriza en unos segundos.» (a type B invoice for $ 15,000 to an end consumer, ARCA authorizes it in a few seconds), and the button adds «y facturar» (and invoice). On charging, Fornu says «Mesa cerrada. El comprobante se emite en unos segundos.» (table closed, the receipt is issued in a few seconds).

If invoicing is turned off in the account or ARCA is not connected, the table still closes and the invoice request is kept to be issued later. A Responsable inscripto without a CUIT cannot be invoiced. The rest is in [Electronic invoicing]({{ '/en/projects/fornu/manual/facturacion/' | relative_url }}).

### With the drawer closed

If the cash drawer is closed and the payment is in cash, Fornu asks before charging:

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-caja-cerrada.jpg' | relative_url }}" alt="The La caja está cerrada notice: Este efectivo no entra en ningún arqueo hasta que se abra la caja, en Balances → Arqueo. ¿Cobrar igual?, with the Volver and Cobrar igual buttons." loading="lazy" width="480" height="224">
  <figcaption>«This cash goes into no cash count until the drawer is opened. Charge anyway?»</figcaption>
</figure>

**Cobrar igual** (charge anyway) takes the payment, but that cash goes into no cash count until the drawer is opened. How to open it is in [Cash and sales]({{ '/en/projects/fornu/manual/caja/' | relative_url }}#arqueo).

### Voiding a payment {#anular-pago}

<p class="perm"><span>Who can:</span> <span class="tag">Cobrar mesas</span> <span class="tag">Deshacer cobros</span></p>

Payments are listed on the bill, for example «Débito · parte 1 de 2 · 12:38 · Administración», with their amount and tip. While the table is still open:

1. Tap the payment's ✕ (**Anular este pago**).
2. Confirm under **Anular el pago** (void the payment): «Efectivo por $ 15.000 vuelve al saldo de la mesa.» (cash for $ 15,000 goes back to the table's balance).
3. Without the Deshacer cobros permission, Fornu asks for the PIN of someone who has it.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-anular-pago.jpg' | relative_url }}" alt="The Anular el pago confirmation: Débito por $ 15.100 vuelve al saldo de la mesa, with Volver and Anular el pago" loading="lazy" width="500" height="200">
  <figcaption>A debit payment going back to the balance.</figcaption>
</figure>

Fornu says «Pago anulado.» (payment voided) and, if it was cash, it leaves the drawer.

### The paid table

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-cobrada.jpg' | relative_url }}" alt="Table 1's paid bill: the Cobrada state, Ronda 1, the 12,500 total, three debit payments (1 item and 1 cover, part 1 of 2, part 2 of 2), Cobrada a las 12:38 por Administración and the Volver a Mesas button." loading="lazy" width="510" height="560">
  <ol class="marks">
    <li><b>Cobrada</b>.</li>
    <li>Each payment, with its method, which part, the time and who took it.</li>
    <li><b>Volver a Mesas</b> (back to tables).</li>
  </ol>
  <figcaption>A table paid in three payments.</figcaption>
</figure>

The closed bill says when and by whom it was paid, and the tip if there was one. **Más acciones** (⋯) still reprints rounds and offers **Imprimir la cuenta** (print the bill). With Facturación, the receipt shows with its status (Autorizada, Esperando a ARCA, Pedida, Rechazada or Anulada: authorized, waiting for ARCA, requested, rejected or voided) or, if there is none yet, a **Facturar** (invoice) button.

If another device changed the bill while you were charging, Fornu does not charge and says so, for example «La cuenta cambió: eso ahora es $ 12.500. Volvé a elegir.» (the bill changed, that is now $ 12,500, choose again).

## Mostrador {#mostrador}

For take-away or eating at the bar. Each sale opens under a name to call the customer and stays open until it is paid, like a table without a chair.

<p class="perm"><span>Who can:</span> <span class="tag">Atender mesas</span> <span class="tag">Cobrar mesas</span></p>

1. On the **Mostrador** tab, tap **Nueva venta** (new sale).
2. If there is more than one business unit, choose the unit.
3. Type the **Nombre para llamarlo** (name to call them by), for example «Juan». With Asignar quién atiende, also choose who serves.
4. Tap **Abrir** (open). The sale opens alongside, ready to load.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-nueva-venta.jpg' | relative_url }}" alt="The Mostrador o para llevar dialog with the units Doble Smash and Pizzería, the name Lucas and Atiende with Tomás Romero and Valentina Sosa, none chosen" loading="lazy" width="620" height="330">
  <figcaption>A new sale for Lucas. Without choosing who serves, it stays in your name.</figcaption>
</figure>

You load it like a table. The differences:

- No guests and no cover charge.
- The sale cannot be moved as a whole or joined with another.
- **Mandar a la cocina** sends everything at once, without courses.
- Whoever takes payment also gets **Mandar y cobrar $ …** (send and charge), which sends the round and opens the payment dialog in one tap. A waiter without Cobrar mesas only sees **Mandar a la cocina** and **Pidió la cuenta**.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-mostrador.jpg' | relative_url }}" alt="The Mostrador tab with two open sales, Camila and Lucas, the Nueva venta button and Lucas's bill alongside with the menu" loading="lazy" width="1440" height="650">
  <ol class="marks">
    <li><b>Nueva venta</b> (new sale): opens with a name.</li>
    <li>The open sale: name, minutes, total and who serves it. Lucas's has something not sent yet.</li>
    <li>Its bill, alongside, like a table's.</li>
  </ol>
  <figcaption>Two open sales at the counter.</figcaption>
</figure>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-mandar-y-cobrar.jpg' | relative_url }}" alt="A counter sale's bill with an unsent Doble cheddar, a 9,800 total and the buttons Mandar a la cocina · 1 and Mandar y cobrar $ 9.800." loading="lazy" width="510" height="300">
  <ol class="marks">
    <li>What is loaded, not yet sent.</li>
    <li><b>Mandar a la cocina</b>: if they pay later.</li>
    <li><b>Mandar y cobrar</b>: sends and opens the payment dialog.</li>
  </ol>
  <figcaption>Send and charge in one tap.</figcaption>
</figure>

If nothing is open, the tab reads «Nada abierto en el mostrador. Una venta para llevar o para comer en la barra se abre con un nombre para llamar al cliente.» (nothing open at the counter, a take-away or bar sale opens under a name to call the customer).

## Mostrador express {#express}

For the quick till: load, send to the kitchen and charge in one go. Nothing stays open.

<p class="perm"><span>Who can:</span> <span class="tag">Cobrar mesas</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-express.jpg' | relative_url }}" alt="The Mostrador express: on the left the search box, the tiles Todo, Burgers 2 and Para acompañar 2, and the products in their colors, the canned soda with the code A7. On the right the Ticket with one soda, the 2,000 total, the payment methods with Efectivo selected, Paga con and the notes Justo, 10,000, 20,000 and 50,000, Nombre para llamarlo and the Cobrar $ 2.000 en Efectivo button." loading="lazy" width="1440" height="710">
  <ol class="marks">
    <li><b>Buscar producto…</b>: by code and <kbd>Enter</kbd> too.</li>
    <li><b>Todo</b> (all) and one tile per category, with its color and how many products it has.</li>
    <li>The product's code, to load it without searching.</li>
    <li><b>Ticket</b>: each product with − and +.</li>
    <li><b>Medio de pago</b> and, for cash, <b>Paga con</b> with the likely notes.</li>
    <li>The button charges, sends to the kitchen and leaves everything ready for the next sale.</li>
  </ol>
  <figcaption>A soda loaded by its code.</figcaption>
</figure>

1. Load: tap products, filter by category, or type the code and press <kbd>Enter</kbd>.
2. Adjust quantities with − and + in the **Ticket**.
3. For a known customer, choose them under **Cliente (opcional)**: their discount applies itself, for example «Descuento de Dueños: 100% · Invita la casa.».
4. Choose the **Medio de pago** and, for cash, what they pay with.
5. If you like, add a **Nombre para llamarlo (opcional)**. Otherwise the sale goes out as «Mostrador».
6. Tap **Cobrar $ … en …**, or **Cerrar sin cargo** if the customer brings 100% off.
{: .steps}

Fornu says «Cobrado $ 19.600 con Efectivo.» (charged $ 19,600 in cash), the round reaches the kitchen board under its name, and the paid sale stays alongside with **Nueva venta** to carry on. Each category's color is chosen under Carta › Categorías.

- The express sale has no tip and does not ask about invoicing. With Facturación, invoice it afterwards from the paid sale, with **Facturar**.
- If you switch business unit with something loaded, Fornu asks «¿Vaciar el ticket y pasar a…?» (empty the ticket and switch?), because a sale belongs to a single unit.
- If a price changed since the menu was loaded, it does not charge: «Los precios cambiaron…» (prices changed). The menu has already refreshed: check the ticket and charge again.
- On a phone, the ticket sits below the menu and a bar at the bottom shows «2 ítems · $ 19.600 · Efectivo» with **Cobrar**.

## Salón › Cuentas del día {#cuentas}

For the cash desk and the manager: what is open right now and how much is still owed, and below it what has already been paid or cancelled, with who served and how many ate. The bar reads **Cuentas** (bills) and the page title is **Cuentas del día** (the day's bills).

<p class="perm"><span>Who can:</span> <span class="tag">Cobrar mesas</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-cuentas.jpg' | relative_url }}" alt="Cuentas del día: Abiertas ahora · 2 with Mesa V1 and Mesa 3, their waiter, time, total and balance. Below, Cobradas y canceladas with the Hoy period, the search box, Exportar, the filters and the cards Pedidos vendidos, Ventas, Ticket promedio, Cancelados and Comensales, 2 at 12,850 per guest." loading="lazy" width="1440" height="790">
  <ol class="marks">
    <li><b>Abiertas ahora</b> (open now): each bill with who serves it, since when, the total and the balance. Tap one to open it.</li>
    <li>The period and the search («Cliente, número o código…», customer, number or code).</li>
    <li><b>Exportar</b> (export): the list, for a spreadsheet.</li>
    <li>The filters: unit, payment method, who served, section, table, cash count, receipt, shift and time.</li>
    <li><b>Comensales</b>: how many ate and the average per guest.</li>
  </ol>
  <figcaption>The day's bills in the demo.</figcaption>
</figure>

**Abiertas ahora** includes counter sales and tables from earlier days that are still open. With none it reads «No hay mesas abiertas.» (no open tables). A bill opened from here comes back to this list with the **Cuentas** arrow.

**Cobradas y canceladas** (paid and cancelled) is the dining room's sales list, already filtered to closed sales. The payment method filter has a «Todo menos efectivo» option (everything but cash), and **Desde las** and **Hasta las** (from, until) apply to opening or closing time. Tap a sale to see it alongside, and walk the list with <kbd>↑</kbd> <kbd>↓</kbd>. **Más info** (more info) unfolds more figures. On a phone the filters sit behind **Filtros**. With Facturación there is a **Comprobante** column and an action to invoice in one go the ones left without an invoice, for example **Facturar 3 sin facturar** (invoice 3 uninvoiced). The full sales list is covered in [Cash and sales]({{ '/en/projects/fornu/manual/caja/' | relative_url }}).

## Salón › Sectores y mesas {#armar}

This is where the dining room is set up: the sections (Salón, Patio, Vereda, that is indoor, patio and sidewalk), their tables with their chairs, the cover charge and where each table goes on the plan. The bar reads **Mesas y sectores** and the page title is **Sectores y mesas** (sections and tables). The owner or the manager does this, and the permission is never lent with a PIN.

<p class="perm"><span>Who can:</span> <span class="tag">Armar el salón</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-sectores.jpg' | relative_url }}" alt="Sectores y mesas: at the top Cubierto por comensal with its Guardar button and Nuevo sector. The Salón and Vereda tabs with the arrows, Editar sector and + Mesas. The plan editor with Elegir y mover, nine placed tables and the Mesas catalog on the right." loading="lazy" width="1440" height="790">
  <ol class="marks">
    <li><b>Cubierto por comensal</b> (cover per guest) and <b>Guardar</b>.</li>
    <li><b>Nuevo sector</b> (new section).</li>
    <li>One section per tab.</li>
    <li>The arrows change the section's order. <b>Editar sector</b> and <b>+ Mesas</b> (add tables).</li>
    <li><b>Elegir y mover</b> (select and move): with Salón alone, the plan is for arranging tables.</li>
    <li>The catalog: unplaced tables and the table models.</li>
  </ol>
  <figcaption>The demo's dining room, set up.</figcaption>
</figure>

### The cover charge

1. Type the price under **Cubierto por comensal**.
2. Tap **Guardar**. Fornu says «Cubierto guardado.» (cover saved).
{: .steps}

It is added per guest at a table, never at the counter. At 0, no cover is charged.

### Sections

A new account already has a section called «Salón». **Nuevo sector** asks for the **Nombre** («Salón, Patio, Vereda»). **Editar sector** renames it and has **Activo: sus mesas se ven en el salón** (active, its tables show on the floor), to take a section out of view without losing it: its tab then reads «Desactivado» (inactive). The ← and → arrows move it («Orden guardado.», order saved).

### Creating many tables at once

1. Choose the section and tap **+ Mesas**.
2. **Desde el número** (starting number): Fornu suggests the one after the highest.
3. **Cuántas** (how many, 1 to 60, 10 by default) and **Sillas de cada una** (chairs each, 4 by default).
4. Optionally, a **Letra antes del número (opcional)** (letter before the number): «P» gives P1, P2… for the patio.
5. Tap **Crear de P1 a P10** (create P1 to P10), or **Crear la mesa P1** for a single one.
{: .steps}

Fornu says «10 mesas creadas.» (10 tables created). If a table with that name exists: «Ya hay una mesa P1.» (there is already a table P1).

### Changing a table

Select the table on the plan and tap **Editar la mesa** (edit the table) in the right-hand panel. The dialog has **Número o nombre** (number or name, up to 20 characters), **Sillas** (chairs, 1 to 40), **Sector** (to move it to another section) and **Activa: se ve en el salón** (active, shows on the floor). Fornu says «Mesa guardada.» (table saved).

A table you no longer use is deactivated, and the bills served at it keep it. On a phone there is no plan: tables show as a list of buttons, and a note says «El plano se arma desde una computadora o una tablet.» (the plan is built from a computer or a tablet).

### Placing tables on the plan

Each section has its own plan. With Salón alone, the plan is a top-down sketch where you arrange the tables: no walls to draw.

1. Tables not yet on the plan wait under **Sin ubicar** (unplaced), on the right, each with its seats.
2. Drag one onto the plan. On a touch screen, tap it and then tap the spot.
3. To move it, drag it. <kbd>R</kbd> turns it.
4. Tap **Guardar el plano** (save the plan). Fornu says «Plano guardado.».
{: .steps}

Each table is drawn with a model that fits its chairs: up to 2, Mesa de 2. Up to 4, Mesa de 4. Up to 6, Mesa de 6. Up to 8, Mesa larga (long table). More, Redonda de 10 (round for 10). A table dragged from the **Mesas** catalog (Mesa de 2, de 4, de 6, Mesa larga, Redonda de 4, de 6 and de 10, Mesa alta) is a new table: it reads «Nueva» (new) until you save, and then takes the next number.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-ubicar.jpg' | relative_url }}" alt="The plan editor with table 1 selected and its bar above it (turn left, turn right, duplicate, minus 4 sillas plus, remove), a round table reading Nueva, and on the right the Editar panel with Mesa de 4 · 1, Modelo, the rotation at 0°, Sillas 4, Le entran hasta 4, 80 cm × 80 cm and Sacar del plano." loading="lazy" width="1340" height="790">
  <ol class="marks">
    <li>The selected table's bar: turn, duplicate, chairs and take off the plan. Below it, the handle to turn it by hand.</li>
    <li>A new table, brought from the catalog.</li>
    <li><b>Editar</b> (edit): the model, the rotation, the chairs («Le entran hasta 4.», fits up to 4) and <b>Sacar del plano</b> (take off the plan).</li>
  </ol>
  <figcaption>Arranging the dining room's tables.</figcaption>
</figure>

**Sacar del plano** sends the table back to **Sin ubicar**: the table itself still exists. With nothing selected, the panel shows **El espacio** (the space), with the section's **Ancho (m)** (width) and **Fondo (m)** (depth). Fornu will not save while something is wrong, and says what: «Mesa 1 y Mesa 2 se pisan.» (tables 1 and 2 overlap), «Mesa 9: queda fuera del espacio.» (outside the space) or «Mesa 4: le entran hasta 4 sillas.» (fits up to 4 chairs). If you switch section without saving, it asks before discarding.

With the Constructor de espacios module, the same editor draws walls, floors, doors and objects: see [Spaces: the floor plan]({{ '/en/projects/fornu/manual/espacios/' | relative_url }}).

## Rounds in the kitchen {#cocina}

Each round sent from the dining room is a card under **En preparación** (in preparation) on the [kitchen board]({{ '/en/projects/fornu/manual/pedidos/' | relative_url }}#tablero), and it chimes just like a new order. Counter and express sales arrive as rounds too, under their name.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-tablero.jpg' | relative_url }}" alt="The orders board: under En preparación the card Mesa 2 · Ronda 1 with Atiende Administración, one portion of fries and the Lista button. Under Listo para entregar the card Mesa 1 · Ronda 1 with Lista and the time, two portions of fries with the note Bien cocidas and the Se llevó a la mesa button." loading="lazy" width="1024" height="580">
  <ol class="marks">
    <li>A round in preparation: the table, the round number, who serves and what is in it. <b>Lista</b> (ready) moves it to the next column.</li>
    <li>A ready round, waiting for the waiter to take it.</li>
  </ol>
  <figcaption>Dining room rounds on the board.</figcaption>
</figure>

The card shows the table in large type, «Ronda 1», the minutes since it went out (they change color after 20), who serves, each line with its station and, under **Después** (later), what is on hold for later, for example «Principal: 2 × Bife · Postre: 1 × Flan». Tapping **Lista** turns the table orange on the floor. **Se llevó a la mesa** (taken to the table) in the kitchen and the waiter's **La llevé** do the same thing: they take the card off the board.

Each round prints one ticket per station, with the table in large type, «RONDA 1», the waiter and the guests, the time and the lines with their notes. Copies read REIMPRESIÓN and void notices read ANULADO, with the reason and who voided. Which station makes each category is chosen under [Kitchen stations]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#estaciones).
