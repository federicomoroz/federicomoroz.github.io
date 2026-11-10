---
layout: manual
manual: cocina-y-reparto
title: "In the kitchen and on the road · Fornu manual"
description: "How to pair the tablet or phone, how each person signs in with a PIN, how clocking in works, what the staff app shows, how to log waste and batches, and how couriers deliver."
permalink: /en/projects/fornu/manual/cocina-y-reparto/
---

## Pairing the device {#vincular}

The kitchen tablet, each courier's phone or the counter PC is paired with the kitchen once, using a code. From then on nobody needs the owner's password: each person taps their name and types their PIN.

<p class="perm"><span>Who can:</span> <span class="tag">Dispositivos</span> to create the code. On the device, anyone who types it.</p>

### Creating the code

1. In the back office, go to Ajustes › Dispositivos (settings, devices) and tap **Vincular dispositivo** (pair a device).
2. Fill in **Nombre para reconocerlo** (a name to recognise it), such as «Tablet de la parrilla» (grill tablet) or «Celular de Martín» (Martín's phone).
3. Tap **Generar código** (create code). A code like XXXX-XXXX appears, saying until what time it is valid. It works only once.
{: .steps}

The Dispositivos screen is covered in [Settings]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#dispositivos).

### Pairing the device

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-vincular.jpg' | relative_url }}" alt="The Vincular este dispositivo screen on a phone, with the Código field, the Vincular button and the Volver a ingresar con email link" loading="lazy" width="390" height="600">
  <ol class="marks">
    <li><b>Código</b> (code): the one you created in Dispositivos.</li>
    <li><b>Vincular</b> (pair): turns on once all eight letters and digits are in.</li>
    <li><b>Volver a ingresar con email</b> (back to email sign-in): to go back.</li>
  </ol>
  <figcaption>Vincular este dispositivo (pair this device), on a phone.</figcaption>
</figure>

1. On the tablet or phone, open Fornu. On the sign-in screen, tap **Usar este celular o PC en una cocina, con PIN** (use this phone or PC in a kitchen, with a PIN).
2. **Vincular este dispositivo** opens. Type the code in **Código**. Upper or lower case doesn't matter.
3. Tap **Vincular**. You'll see «Dispositivo vinculado» (device paired) and then the [PIN screen](#pin).
{: .steps}

If the code is wrong or no longer valid, it says «El código no es válido. Revisalo o generá otro.» (the code isn't valid, check it or create another). Create a new one in Dispositivos.

<div class="callout tip"><p class="callout-title">Tip</p><p>Pick names that make sense at a glance. The name shows on the PIN screen and in the Dispositivos list, and it is what tells you which one to remove if a phone gets lost.</p></div>

### Unpairing

- **From the device itself**: on the PIN screen, tap **Desvincular este dispositivo** (unpair this device). Fornu asks «¿Desvincular este dispositivo?» and warns that using it with a PIN again will need a new code. Tap **Desvincular**. This only makes that browser forget the kitchen: the device stays in the Dispositivos list.
- **From the back office**: in Ajustes › Dispositivos, **Dar de baja** (remove). Whoever is using it is signed out right then. That is the way to go when a phone gets lost or a courier stops using theirs.

## The PIN screen {#pin}

It is the first thing a paired device shows: the list of the kitchen's people. Each one taps their name and types their PIN to sign in or to clock in.

<p class="perm"><span>Who can:</span> anyone with a PIN. PINs are set in <a href="{{ '/en/projects/fornu/manual/personal/' | relative_url }}">Staff</a>.</p>

<div class="shot-pair">
<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-pin.jpg' | relative_url }}" alt="Martín's PIN pad on his phone, on shift since 18:25, with the Fichar salida and Entrar buttons" loading="lazy" width="390" height="844">
  <ol class="marks">
    <li>Who is signing in and, if on shift, since when.</li>
    <li>The dots and the keypad. <b>Volver</b> (back) returns to the names and ⌫ deletes.</li>
    <li><b>Fichar salida</b> (clock out): ends the shift without signing in.</li>
    <li><b>Entrar</b> (sign in): opens the app.</li>
  </ol>
  <figcaption>The PIN pad for someone already on shift.</figcaption>
</figure>
<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-nombres.jpg' | relative_url }}" alt="The PIN screen of Cocina de prueba on the Cocina tablet, with seven names and their roles, three of them on shift, the links Ingresar con email and Desvincular este dispositivo, and the theme switch at the top" loading="lazy" width="900" height="700">
  <ol class="marks">
    <li>The kitchen's name and, below it, the device's.</li>
    <li>One card per person, with their roles and, if on shift, since when.</li>
    <li><b>Ingresar con email</b> (sign in with email): for the owner or manager, on the same device.</li>
    <li><b>Desvincular este dispositivo</b> (unpair this device).</li>
    <li>This device's theme.</li>
  </ol>
  <figcaption>The list of names on a tablet.</figcaption>
</figure>
</div>

### The names

Under each name are their roles, separated by « · », or **Solo ficha** (clock-in only) when their roles give no permissions. Whoever has clocked in shows «En turno desde las 13:05» (on shift since 13:05). Active people with a PIN are listed. If there are none yet, the screen says «Nadie de esta cocina tiene PIN todavía. Se carga en Personal.» (nobody in this kitchen has a PIN yet, it is set in Personal).

### Signing in with the PIN

1. Tap your name.
2. Type your PIN, 4 to 6 digits, on the screen's keypad or the device's keyboard.
3. Tap the right button. The buttons turn on from the fourth digit, and <kbd>Enter</kbd> presses the main one.
{: .steps}

The buttons change depending on who you are and whether you have clocked in:

| Who | Buttons | What the main one does |
|---|---|---|
| Uses the app, not on shift | **Entrar sin fichar** (sign in without clocking in) and **Fichar y entrar** (clock in and sign in) | Clocks in and opens the app, in one tap. |
| Uses the app, already on shift | **Fichar salida** and **Entrar** | Opens the app. |
| Clock-in only | **Fichar entrada** (clock in) or **Fichar salida** | Clocks, nothing else. |

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-pin-sin-turno.jpg' | relative_url }}" alt="Lucía's PIN pad, before she clocked in, with the Entrar sin fichar and Fichar y entrar buttons" loading="lazy" width="412" height="915">
  <ol class="marks">
    <li>Who is signing in. No «En turno desde las…»: she hasn't clocked in yet.</li>
    <li><b>Entrar sin fichar</b>: opens the app without clocking in.</li>
    <li><b>Fichar y entrar</b>: the main one, clocks in and opens the app.</li>
  </ol>
  <figcaption>The PIN pad for someone who hasn't clocked in yet.</figcaption>
</figure>

A wrong PIN shows «PIN incorrecto · quedan 3 intentos.» (wrong PIN, 3 tries left). After five wrong tries in a row, that person is locked for 15 minutes: «PIN incorrecto: Martín queda bloqueado 15 min.» If you forgot your PIN, ask whoever manages the team to set a new one.

<div class="callout tip"><p class="callout-title">Tip</p><p>The theme is chosen with the icons at the top of this screen, and it applies to this device. The kitchen tablet can stay dark even if the office uses light.</p></div>

## Clocking in and out {#fichar}

Clocking records when each person starts and finishes, with their PIN, on any paired device. It always works, with or without the Personal module. With the module, those clock-ins feed the attendance and the attendance sheet in [Staff]({{ '/en/projects/fornu/manual/personal/' | relative_url }}).

<p class="perm"><span>Who can:</span> anyone with a PIN, even if their role has no permissions.</p>

### When you arrive

1. Tap your name and type your PIN.
2. Tap **Fichar y entrar** (or press <kbd>Enter</kbd>). Your clock-in is recorded and your app opens.
{: .steps}

If you only need to check something and aren't starting your shift, use **Entrar sin fichar**.

### During the shift

At the top of the app there is a box with your shift:

- If you haven't clocked in, it says **Fichar entrada**, highlighted. Tap it and you'll see «Entrada fichada» (clocked in).
- If you are on shift, it says «En turno desde las 13:05 · Fichar salida». On narrow screens, like a phone, only «En turno desde las 13:05» shows.

### When you leave

1. Tap the shift box. Fornu asks «¿Fichar la salida?» (clock out?) and tells you how long you've been in: «Entraste a las 13:05: van 8 h 10 min.»
2. Tap **Fichar salida**. You'll see «Salida fichada» (clocked out).
{: .steps}

You can also do it from the PIN screen: your name, your PIN and **Fichar salida**. A card appears there, which closes by itself after 6 seconds or with **Listo** (done).

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-fichado.jpg' | relative_url }}" alt="The card confirming the clock-out: Salida de Martín: 18:22, Trabajaste 4 min., with the Listo button" loading="lazy" width="390" height="570">
  <figcaption>The clock-out, with the time worked («Trabajaste 4 min.», you worked 4 min). On clocking in, the card says «¡Buen turno!» (have a good shift).</figcaption>
</figure>

A few rules:

- You can't clock out within the first minute after clocking in: «Fichaste la entrada recién: la salida se ficha al terminar el turno.» (you just clocked in, clock out at the end of your shift).
- A shift left open for longer than the hours set in Ajustes › Configuración (16 unless someone changed it) counts as forgotten. The next tap starts a new shift, and the forgotten one waits for a manager to fix it in Personal › Asistencia.
- People who sign in to the back office with an email don't clock: the clock buttons only exist in the staff app. If the owner also wants to clock in, they need a name and a PIN in Personal.

### Fichar a alguien

On the kitchen tablet, the app stays open on the board all shift. So someone else can clock in without closing anything, there is **Fichar a alguien** (clock someone in).

1. Tap **Fichar a alguien**, at the top of the app.
2. **Fichar entrada o salida** (clock in or out) opens, with each name and its state: «En turno desde las…» or «Sin fichar» (not clocked in).
3. Tap the name and have that person type their PIN.
4. Tap **Fichar entrada** or **Fichar salida**. The card says «Entrada de Rosa: 13:05» and «¡Buen turno!», or the clock-out with the time worked. Tap **Listo**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-fichar-a-alguien.jpg' | relative_url }}" alt="Fichar entrada o salida open over the tablet's board, with seven names: four on shift, with the time they came in, and three not clocked in" loading="lazy" width="820" height="300">
  <ol class="marks">
    <li>Someone who hasn't clocked in: «Sin fichar».</li>
    <li>Someone on shift: «En turno desde las 18:18».</li>
  </ol>
  <figcaption>Fichar entrada o salida, on top of the board.</figcaption>
</figure>

Nobody signs in or out of the app, and the board underneath keeps chiming with every new order.

### People who only clock in

A person whose roles have no permissions shows as **Solo ficha**: their PIN records arrivals and departures and opens no screen. It suits the dishwasher, the cleaning staff or anyone who doesn't use Fornu but has to clock in. Roles are set up in [Staff]({{ '/en/projects/fornu/manual/personal/' | relative_url }}#roles).

## The staff app {#app}

Whoever signs in with a PIN only sees the screens for their job, as tabs. The cook sees the board and the waste screen, the courier their deliveries, the waiter the tables.

<p class="perm"><span>Who can:</span> anyone whose role has permissions. Each tab asks for its own.</p>

<div class="shot-pair">
<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-app-celular.jpg' | relative_url }}" alt="The staff app on a waitress's phone: at the top Fichar entrada highlighted, Fichar a alguien and Sofía, and below the Venta screen with the tables" loading="lazy" width="390" height="640">
  <ol class="marks">
    <li><b>Fichar entrada</b>: she hasn't clocked in yet.</li>
    <li><b>Fichar a alguien</b>.</li>
    <li>Who is using the app. A tap goes back to the names.</li>
  </ol>
  <figcaption>A waitress with a single screen, Venta (sale): no tabs.</figcaption>
</figure>
<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-app-tablet.jpg' | relative_url }}" alt="The staff app on the Cocina tablet, on the Pedidos tab, with Diego Ruiz's shift open, Fichar a alguien, the Pedidos and Merma y producción tabs, his name and the board showing only the Plancha station" loading="lazy" width="820" height="620">
  <ol class="marks">
    <li>The shift: «En turno desde las…».</li>
    <li><b>Fichar a alguien</b>.</li>
    <li>The tabs: <b>Pedidos</b> (orders) and <b>Merma y producción</b> (waste and batches).</li>
    <li>Who is using the app.</li>
    <li><b>Todo</b> (all), one button per station and one per brand: what this board shows.</li>
    <li>Another station's lines look faded.</li>
  </ol>
  <figcaption>The griddle's tablet, showing only its own station.</figcaption>
</figure>
</div>

### What's at the top

- On the left, Fornu with the kitchen's name and, as the title, the open tab.
- The shift box and **Fichar a alguien**, explained in [Clocking in and out](#fichar).
- The tabs, when there is more than one. The first one opens.
- The theme switch, on wide screens.
- Your name with «· Cambiar de persona» (switch person), or just the name on a phone. A tap goes back to the list of names without asking: on a shared tablet, whoever finishes hands it to the next person.

If the connection drops, the band «Sin conexión en vivo: los pedidos nuevos pueden tardar en aparecer. Reintentando…» appears.

### Tabs by role

| Tab | Shown to whoever has | What it is |
|---|---|---|
| **Venta** (sale) | Atender mesas or Cobrar mesas, with the Salón module | Tables and counter. See [Dining room]({{ '/en/projects/fornu/manual/salon/' | relative_url }}). |
| **Pedidos** | Cocina | The [orders board](#tablero). |
| **Merma y producción** | Cocina | What was thrown away and what was made. See [Merma y producción](#merma). |
| **Mis entregas** (my deliveries) | Mensajería | The courier's orders. See [The courier's phone](#mensajero). |
| **Arqueo** (cash count) and **Movimientos** (movements) | Caja | Opening, counting and closing the till. See [Cash and sales]({{ '/en/projects/fornu/manual/caja/' | relative_url }}). |
| **Stock** | Stock | Stock and its counts. See [Stock items and stock]({{ '/en/projects/fornu/manual/insumos-y-stock/' | relative_url }}). |
| **Compras** (purchases) | Gastos, with the Proveedores y compras module | Stock purchases. See [Purchases and expenses]({{ '/en/projects/fornu/manual/compras-y-gastos/' | relative_url }}). |
| **Gastos** (expenses) | Gastos | Expenses. See [Purchases and expenses]({{ '/en/projects/fornu/manual/compras-y-gastos/' | relative_url }}). |

For example, someone with the **Cocina** role sees **Pedidos** and **Merma y producción**. A courier with the **Mensajería** role only sees **Mis entregas**, with no tabs. A manager with the **Encargado/a** role sees **Pedidos**, **Merma y producción**, **Arqueo**, **Movimientos**, **Stock** and **Gastos**, plus **Compras** if the account has Proveedores y compras.

## The kitchen tablet {#tablero}

The **Pedidos** tab is the same board as in the back office, made to stay in sight next to the griddle: each order lands in **A confirmar** (to confirm) with a chime, then moves through **En preparación** (cooking) and **Listo para entregar** (ready for pickup) with a tap each. Everything you do on the board is covered in [Orders and delivery]({{ '/en/projects/fornu/manual/pedidos/' | relative_url }}#tablero). This section covers what is specific to the tablet.

<p class="perm"><span>Who can:</span> <span class="tag">Cocina</span></p>

### One station per tablet

Above the board there is a row of buttons that choose what it shows: **Todo** (all), one per station with orders in progress (such as **Parrilla**, grill, **Barra**, bar, or **Cocina**, kitchen) and one per brand when more than one brand has orders.

1. On the grill's tablet, tap **Parrilla**.
2. That's it. The tablet remembers and stays on the grill, even if someone signs out and back in.
{: .steps}

With a station chosen, only the orders with something for it show up, and the other stations' lines look faded, as in the picture above. Dining-room rounds are filtered the same way. With a brand chosen, only its orders show up.

To know how much of each thing to turn out, **Ver sumado** (see totals, in the **En preparación** column) or **Sumado** (totals, on a phone) adds up everything being cooked, for example 4 Papas fritas and 3 Doble cheddar. With a station chosen, it only adds that station's lines.

### The chime

Each new order to confirm plays a two-note chime, and it repeats every 20 seconds while any order is waiting. Each new round from the dining room chimes too.

Some browsers won't let a page play sound until someone touches it. When that happens the board says so: «El sonido de los pedidos nuevos está apagado: tocá cualquier parte de la pantalla para prenderlo.» (new-order sound is off, tap anywhere on the screen to turn it on), with a **Prender el sonido** (turn on sound) button.

### The screen stays on

While the board is open, the tablet doesn't go to sleep, on devices that allow it.

<div class="callout tip"><p class="callout-title">Tip</p><p>Leave the tablet plugged in and open on <b>Pedidos</b>. To clock in without leaving the board, use <b>Fichar a alguien</b>. After logging waste, go back to <b>Pedidos</b>: it is the tab that keeps the screen on and shows what comes in.</p></div>

## Merma y producción {#merma}

Merma y producción (waste and batches) lets the kitchen record what it throws away and what it makes, right when it happens, from the tablet, without hunting for a spreadsheet. Each entry moves the stock immediately.

<p class="perm"><span>Who can:</span> <span class="tag">Cocina</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-merma.jpg' | relative_url }}" alt="The Merma y producción tab on a tablet: Se tiró un producto with the brands Doble Smash, Pollo Crocante, Bowl Verde and Pizzería and the Doble Smash products, and Se tiró un insumo with its search box" loading="lazy" width="820" height="770">
  <ol class="marks">
    <li>The brands, when there is more than one.</li>
    <li>The products, without prices. A tap opens the deduction.</li>
    <li><b>Buscar insumo…</b> (find an item): for things thrown away that aren't a dish.</li>
  </ol>
  <figcaption>Merma y producción: what was thrown away, at the top.</figcaption>
</figure>

### Se tiró un producto

Se tiró un producto (a product was thrown away): a burger that burned, an order made by mistake. Everything in its recipe comes out of stock.

1. If there are several brands, pick the product's brand.
2. Tap the product. **Se tiró: Doble cheddar** opens.
3. Set how many units with **−** and **+**.
4. Choose why: **Se quemó** (burned), **Se cayó** (dropped), **Salió mal** (came out wrong), **Vencido** (expired) or **Error de pedido** (order mistake). Until you choose, the footer says «Elegí por qué» (choose why).
5. Tap **Descontar del stock** (take out of stock). You'll see «Descontado: 2 × Doble cheddar (se quemó)».
{: .steps}

A product sold out for today can be logged too: what was thrown away still counts.

### Se tiró un insumo

Se tiró un insumo (an item was thrown away): vegetables gone bad, a tray that fell, an expired sauce.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-merma-insumo.jpg' | relative_url }}" alt="The Se tiró: Arroz dialog, with Cuánto, en kg set to 0,5, the reason Vencido chosen and the Volver and Descontar del stock buttons" loading="lazy" width="820" height="283">
  <ol class="marks">
    <li><b>Cuánto</b> (how much), in kilos, litres or units depending on the item.</li>
    <li>Why it was thrown away.</li>
    <li><b>Descontar del stock</b>.</li>
  </ol>
  <figcaption>Half a kilo of expired rice.</figcaption>
</figure>

1. In **Buscar insumo…**, type two letters or more. Up to eight items show up.
2. Tap the one thrown away. **Se tiró: Arroz** opens.
3. In **Cuánto, en kg** (or in l, or in u), type the amount. For example, 0,5 for half a kilo (the app uses a decimal comma).
4. Choose why.
5. Tap **Descontar del stock**. You'll see «Descontado: 500 g de Arroz (vencido)».
{: .steps}

If nothing matches, it says «No hay ningún insumo que se llame así.» (no item is called that). While something is missing, the footer says «Poné cuánto» (enter how much) or «Elegí por qué».

### Producí

Producí (I made): when the kitchen makes a batch of something prepared in-house, like a sauce or the patties, it logs it here. The batch goes into stock and the items it uses come out.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-produci.jpg' | relative_url }}" alt="The Producí section: Bollo de pizza grande in red with Faltó registrar lo producido: se usaron 300 u de más, Cebolla caramelizada with Hay 400 g, other prepared items, and the notice Descontado: 500 g de Arroz (vencido) at the bottom" loading="lazy" width="820" height="420">
  <ol class="marks">
    <li>In red, what is short: it comes first.</li>
    <li>How much there is.</li>
    <li>The notice for the last thing logged.</li>
  </ol>
  <figcaption>Producí, with the most urgent first.</figcaption>
</figure>

Each prepared item shows how much there is, and the ones running short come first, in red:

| It says | What it means |
|---|---|
| «Hay 400 g» (there is 400 g) | What is in stock. |
| «Hay 1 kg · faltan 2 kg para el mínimo» (2 kg short of the minimum) | It is below its minimum. Time to make a batch. |
| «Faltó registrar lo producido: se usaron 300 u de más» (a batch wasn't logged: 300 u more were used) | Orders used more than was logged. Someone made a batch and didn't record it. |
| «Sin receta» (no recipe) | It has no recipe, so it can't be made from here. |

1. Tap what you made. For example, **Producí: Salsa de la casa** opens, saying how much one batch makes and how much there is.
2. Set how much you made with **−** and **+**. Each tap adds or removes one batch.
3. Tap **Registrar** (log). You'll see «Producido: 3 kg de Salsa de la casa».
{: .steps}

If the kitchen has no prepared items, it says «La cocina todavía no tiene elaboraciones cargadas.» (the kitchen has no prepared items yet). Prepared items and their recipes are set up in [Stock items and stock]({{ '/en/projects/fornu/manual/insumos-y-stock/' | relative_url }}). From the back office, anyone with the Stock permission can log waste and batches too.

<div class="callout tip"><p class="callout-title">Tip</p><p>A prepared item in red with «Faltó registrar lo producido» means a batch was made and nobody logged it. Log it and the numbers add up again.</p></div>

## The courier's phone {#mensajero}

The restaurant's own couriers deliver its own orders from their phone: they see what is ready to go, take it, get there with the map and mark it delivered. At the top they see how much cash they are carrying.

<p class="perm"><span>Who can:</span> <span class="tag">Mensajería</span></p>

The courier's phone is [paired](#vincular) once, like the tablet. After that the courier taps their name, types their PIN and goes straight to **Mis entregas** (my deliveries).

Rappi and PedidosYa orders don't show up here: each platform's own rider picks them up.

### What it shows

- **The cash you carry.** If you have cash from delivered orders, the top says «Tenés $ 23.600 en efectivo de 2 pedidos: rendilo al terminar.» (you have $ 23,600 in cash from 2 orders, hand it over when you finish).
- **Para retirar** (to pick up). Every own order ready for pickup, for any courier. Each shows «#12 · Doble Smash», the time it was ready, the address, the customer with the total, what to collect and what goes in the bag, so you can check it before leaving. At the bottom, the big **Me lo llevo** (I'll take it) button. With nothing ready, it says «No hay pedidos listos.» (no orders ready).
- **En camino** (on the way). Only the ones you are carrying: when it left, the address in large type, the customer and phone, what goes in the bag, the **Abrir en el mapa** (open in maps), **Llamar** (call) and **WhatsApp** buttons, the order's note and what to collect (or «Total del pedido: $ …», the order total, when the order doesn't say how it is paid). At the bottom, the big **Entregado** (delivered) button. With nothing on you, it says «No estás llevando nada.» (you're not carrying anything).
- At the bottom, how many you delivered: «Entregaste 5 pedidos hoy.» (you delivered 5 orders today).

<div class="shot-phones">
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-entregas.jpg' | relative_url }}" alt="Mis entregas on Martín's phone: at the top the cash he carries, 13,500 pesos from one order, and below Para retirar with two orders ready, each with its address, the customer, what to collect, what goes in the bag and the Me lo llevo button" loading="lazy" width="390" height="935">
    <ol class="marks">
      <li>The cash you carry, to hand over at the end.</li>
      <li>What to collect. For cash, what they pay with and the change.</li>
      <li>What goes in the bag.</li>
      <li><b>Me lo llevo</b>.</li>
    </ol>
    <figcaption>Para retirar: two orders ready.</figcaption>
  </figure>
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-en-camino.jpg' | relative_url }}" alt="En camino: order 2 from Pollo Crocante, with the address in large type, the customer and phone, the Abrir en el mapa, Llamar and WhatsApp buttons, what to collect and the Entregado button" loading="lazy" width="390" height="480">
    <ol class="marks">
      <li>The address and the customer, with their phone.</li>
      <li><b>Abrir en el mapa</b>, <b>Llamar</b> and <b>WhatsApp</b>.</li>
      <li>What to collect.</li>
      <li><b>Entregado</b>.</li>
    </ol>
    <figcaption>En camino: the one Martín is carrying.</figcaption>
  </figure>
</div>

What to collect reads the same as in the kitchen:

| It says | What to do |
|---|---|
| «Ya pagó: no hay que cobrar nada» (already paid, nothing to collect) | Hand it over and you're done. |
| «Cobrar $ 19.600 en efectivo» (collect $ 19,600 in cash) | Collect that amount in cash. |
| «Cobrar $ 19.600 en efectivo · paga con $ 20.000: llevá $ 400 de vuelto» (pays with $ 20,000, take $ 400 change) | Leave with the change. |
| «Cobrar $ 19.600 con tarjeta de débito: llevá el posnet» (debit card, take the card reader) | Take the card reader (same for credit). |
| «Cobrar $ 19.600 con QR: llevá el código» (QR, take the code) | Take the QR code. |
| «Cobrar $ 19.600 por transferencia» or «por Mercado Pago» (bank transfer, Mercado Pago) | Collect on arrival that way. |

### Delivering an order

1. When the kitchen taps **Listo** (ready) on the board, the order shows up under **Para retirar**.
2. Check the bag against the list of what it carries.
3. Tap **Me lo llevo**. The order moves to **En camino** under your name and you'll see «#12 en camino». If another courier took it a second earlier, it says «El pedido #12 lo lleva otra persona.» (someone else is taking order #12).
4. Tap **Abrir en el mapa** to go with Google Maps. If needed, **Llamar** opens the phone with the customer's number and **WhatsApp** opens a chat with them.
5. At the door, collect what the order says and tap **Entregado**. You'll see «#12 entregado».
{: .steps}

### Cash and handing it over

Each own order paid in cash that you deliver adds to what you carry, and the line at the top shows it right away. Card, QR, transfer and already-paid orders don't add up.

At the end of the shift, hand the cash to the manager or the cashier. They count it and record it in Pedidos › Efectivo, as explained in [Couriers' cash]({{ '/en/projects/fornu/manual/pedidos/' | relative_url }}#efectivo). Any shortfall or surplus is written down there.

<div class="callout tip"><p class="callout-title">Tip</p><p>If an order isn't under <b>Para retirar</b>, most likely the kitchen hasn't tapped <b>Listo</b>. Tell the kitchen before leaving without it.</p></div>
