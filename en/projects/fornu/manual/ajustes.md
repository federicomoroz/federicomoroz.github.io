---
layout: manual
manual: ajustes
title: "Settings · Fornu manual"
description: "Business units with their channels and stores, devices, kitchen stations and printers, payment methods, discount reasons, integrations, users and the account's configuration."
permalink: /en/projects/fornu/manual/ajustes/
---

## Unidades de negocio {#unidades}

**Unidades de negocio** (business units) are the brands that come out of this kitchen, like Doble Smash or Pollo Crocante in the demo. They all share the same kitchen and the same stock, and each has its own sales channels, what each channel keeps, and what its orders carry besides the recipe. The tab reads **Unidades** and the page title **Unidades de negocio**.

<p class="perm"><span>Who can:</span> <span class="tag">Ajustes</span> <span class="tag">Carta</span> (publishing the menu)</p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-unidades.jpg' | relative_url }}" alt="The demo's business units, each with its channels and commissions, suggested wait, extras, its Rappi and PedidosYa stores and the Publicar en Rappi button" loading="lazy" width="1440" height="560">
  <ol class="marks">
    <li><b>Unidad de negocio</b>: creates a new brand.</li>
    <li><b>Canales</b> (channels): where it sells and each platform's commission.</li>
    <li><b>Espera sugerida</b> (suggested wait): the time the kitchen proposes when confirming an order for that brand.</li>
    <li><b>Adicionales</b> (extras): the box, the bag, the cutlery and anything else its sales carry.</li>
    <li>Its stores on the platforms and the button to publish the menu to them.</li>
  </ol>
  <figcaption>The demo's four brands. Stores show with the Delivery por plataformas module.</figcaption>
</figure>

### Create or change a unit

1. Tap **Unidad de negocio**, or the row of an existing one.
2. Type the **Nombre** (name) and pick the **Color**: it tells the brand apart on the kitchen screens and on labels.
3. Set the **Espera sugerida (min)**. It is proposed when confirming an order and can be changed on each one.
4. Under **Canales de venta** (sales channels), turn on **Vende** (sells) for each channel the brand sells on and fill in what that channel keeps.
5. Tap **Guardar** (save). You see «Guardado: Doble Smash».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-unidad.jpg' | relative_url }}" alt="The new business unit form: name, color, suggested wait, order and the channels table with commission, fixed cost and products per order" loading="lazy" width="880" height="900">
  <ol class="marks">
    <li><b>Color</b>: the brand's color in the kitchen and on labels.</li>
    <li><b>Espera sugerida (min)</b>: the time proposed when confirming.</li>
    <li><b>Vende</b>: turn on each channel the brand sells on.</li>
    <li><b>Comisión (%)</b> (commission): turning Rappi on proposes 23 %, to be changed if the brand pays a different one.</li>
    <li><b>Costo fijo por unidad</b> (fixed cost per item) and <b>Productos por pedido</b> (products per order): so margins count what each channel charges.</li>
  </ol>
  <figcaption>A new unit. The Salón channel shows with the Salón module.</figcaption>
</figure>

What each column under **Canales de venta** means:

| Column | What it is |
|---|---|
| **Canal** | **Pedidos propios** (own orders) always. **Rappi** and **PedidosYa** with the Delivery por plataformas module. **Salón** (dining room) with the Salón module. |
| **Vende** | Whether the brand sells on that channel. |
| **Comisión (%)** | What the channel keeps from what the customer pays. |
| **Costo fijo por unidad** | What the channel charges per product sold, on channels that charge that way. |
| **Productos por pedido** | How many products an average order has. What each order carries is spread over them in the margins. |

**Orden** (order) sets where the brand shows in lists. Units are never deleted: to stop using one, turn off **Activa** (active).

### Add the extras

Extras are what sales carry besides the recipe, and they come off the stock with each order: the box for each product, the bag, the cutlery, the sticker.

1. On the unit's row, tap **Adicionales**.
2. Tap **+ Adicional** (add extra).
3. Pick the **Canal** (**Todos**, all, **Propios**, **Rappi**, **PedidosYa** or **Salón**) and where it **Va en** (goes on): **Cada pedido** (each order), **Cada producto** (each product) or only each product of one category.
4. Pick the **Insumo** (stock item) and the **Cantidad** (quantity). The **Costo** shows next to it.
5. Tap **Guardar**. You see «Adicionales guardados» (extras saved).
{: .steps}

In the margins, what goes on each order is spread over the products of an average order on that channel. See [Costs and reports]({{ '/en/projects/fornu/manual/costos-y-reportes/' | relative_url }}).

### Rappi and PedidosYa stores {#tiendas}

With the Delivery por plataformas module, each business unit is a store on each platform, with the number the platform gives it. The unit's row says how each one stands:

| Shows | Means |
|---|---|
| «Rappi: sin tienda vinculada (la vincula Fornu)» | The brand sells on Rappi but its store is not linked yet (Fornu links it). |
| «Rappi: tienda 900100001 · carta al día» | The store shows the menu as it is today. |
| «· cambios sin publicar» | The menu changed after it was last published. |
| «· carta sin publicar» | The menu was never published from Fornu to that store. |

The menu's state is shown to people with the Carta (menu) permission.

**How a store gets linked:** give Fornu the store number of each business unit on each platform, and Fornu links it. Until then, that store's orders are keyed in by hand on the board, with the number the platform's tablet shows. See [Orders and delivery]({{ '/en/projects/fornu/manual/pedidos/' | relative_url }}).

### Publish the menu to Rappi or PedidosYa

1. On the unit's row, tap **Publicar en Rappi** or **Publicar en PedidosYa** (publish to). There is one button per linked store.
2. Fornu publishes that brand's menu to its store, with that platform's prices. You see «Carta publicada en Rappi» (menu published to Rappi), with the number of products and the store number.
{: .steps}

<div class="callout tip"><p class="callout-title">Tip</p><p>After you change prices or products, Carta › Productos warns «La carta de Rappi no está al día.» (the Rappi menu is out of date) with a button to publish it. Until it is published again, the platform shows the old prices and products.</p></div>

## Dispositivos {#dispositivos}

**Dispositivos** (devices) are the phones, tablets and PCs where staff get in with their PIN, plus the PC that prints the kitchen tickets. Each one is paired once, with a code. After that the team gets in with their PIN, without your password.

<p class="perm"><span>Who can:</span> <span class="tag">Dispositivos</span></p>

The list shows each **Dispositivo** by the name you gave it, when it was **Vinculado** (paired) and its **Último ingreso** (last PIN login). Unpaired ones say «dado de baja» (removed).

### Pair a phone, tablet or PC

1. Tap **Vincular dispositivo** (pair device).
2. Give it a **Nombre para reconocerlo** (a name to recognize it): «Celular de Martín» (Martín's phone), «PC del mostrador» (counter PC), «Impresora de comandas» (ticket printer).
3. Tap **Generar código** (generate code). A code like ABCD-1234 appears. It is valid until the time the dialog shows and works only once.
4. On the device, open Fornu and tap **Usar este celular o PC en una cocina, con PIN** (use this phone or PC in a kitchen, with PIN).
5. Type the code and tap **Vincular**. You see «Dispositivo vinculado» (device paired).
{: .steps}

What the device shows afterwards, the list of names and the PIN pad, is in [In the kitchen and on the road]({{ '/en/projects/fornu/manual/cocina-y-reparto/' | relative_url }}#vincular). If the code doesn't work, it says «El código no es válido. Revisalo o generá otro.» (the code is not valid, check it or make another).

### The PC that prints the kitchen tickets

Kitchen tickets print from a PC at the place, next to the printer, running Fornu's print agent. When you generate the code, the same dialog shows what to type on that PC to pair it. If the agent is not connected, test prints say so.

### Remove a device

1. On its row, tap **Dar de baja** (remove).
2. Confirm. Whoever is using it is shut out, and using it again needs a new code.
{: .steps}

On the device itself, **Desvincular este dispositivo** (unpair this device) makes that browser forget the pairing. The list in Ajustes keeps showing it until someone taps **Dar de baja**.

## Estaciones de cocina {#estaciones}

**Estaciones de cocina** (kitchen stations): each station prints its own ticket, so the grill gets what goes on the grill and the bar gets the drinks. Without stations, everything prints on the kitchen's printer. The tab reads **Estaciones**.

<p class="perm"><span>Who can:</span> <span class="tag">Ajustes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-estaciones.jpg' | relative_url }}" alt="The stations list with the kitchen without a printer and a bar station with its own printer, and below, what each station prepares for each Doble Smash category" loading="lazy" width="1440" height="600">
  <ol class="marks">
    <li><b>Nueva estación</b> (new station): adds one.</li>
    <li><b>Cocina (la de Configuración)</b> (the kitchen, from Configuración): prepares everything that doesn't go to another station. Its printer is set in <a href="#impresion">Configuración</a>.</li>
    <li>The station's printer. Without one, its ticket prints on the kitchen's printer with the station's name on top.</li>
    <li><b>Prueba</b> (test): prints a test ticket at that station.</li>
    <li>What each station prepares: one list per category, for each business unit.</li>
  </ol>
  <figcaption>A kitchen with a bar station, no categories assigned yet.</figcaption>
</figure>

### Create a station

1. Tap **Nueva estación**.
2. Give it a **Nombre**: Parrilla (grill), Barra (bar), Cocina fría (cold kitchen).
3. If the station has its own printer, type its address in **Impresora (opcional)** (printer, optional), like 192.168.0.51.
4. Tap **Guardar**. You see «Estación guardada.» (station saved).
{: .steps}

When editing it, **Activa: si no, sus categorías salen por la cocina** shows (active, otherwise its categories print in the kitchen).

### Choose what each station prepares

Below the list there is a card per business unit, such as «Doble Smash: qué prepara cada estación» (what each station prepares). Each menu category has its own list: pick **Cocina** or a station. It saves as you pick, showing for example «Burgers: guardado.». These cards show once there is at least one active station.

### Print a test

Tap **Prueba** on the station's row. The button shows when the station has its own printer. The kitchen printer's test is in [Configuración](#impresion). Both answer the same way:

- «Prueba en cola: sale en unos segundos.» (test queued, it prints in a few seconds)
- «Prueba en cola, pero el agente de impresión todavía no se conectó: instalalo en una PC del local y vinculalo en Dispositivos.» (queued, but the print agent hasn't connected yet: install it on a PC at the place and pair it in Dispositivos)

## Medios de pago {#medios-de-pago}

**Medios de pago** (payment methods) are what the cash desk offers when a table pays, under the names the place uses: Cuenta DNI, Modo, Débito Visa. Each method has a type. Cash goes into the drawer, and the rest is collected elsewhere and checked in the cash count.

<p class="perm"><span>Who can:</span> <span class="tag">Ajustes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-medios-de-pago.jpg' | relative_url }}" alt="The payment methods list with the six default ones, and beside it the form for adding one with its name and type" loading="lazy" width="1440" height="600">
  <ol class="marks">
    <li>The account's payment methods, each with its type.</li>
    <li><b>Nombre</b>: what the place calls it.</li>
    <li><b>Tipo</b> (type): decides which line of the cash count the money goes to.</li>
  </ol>
  <figcaption>A new account starts with Efectivo, Débito, Crédito, QR, Transferencia and Mercado Pago.</figcaption>
</figure>

1. Tap **Agregar** (add).
2. Type the **Nombre**, up to 40 characters.
3. Pick the **Tipo**: **Efectivo** (cash), **Débito**, **Crédito**, **QR**, **Transferencia** (transfer) or **Mercado Pago**.
4. Tap **Guardar**.
{: .steps}

Methods are never deleted: to stop offering one, tap it and turn off **Activo**. They are used when taking payment in the [Salón]({{ '/en/projects/fornu/manual/salon/' | relative_url }}#cobrar), and the cash count adds them up by type, as shown in [Cash and sales]({{ '/en/projects/fornu/manual/caja/' | relative_url }}#arqueo).

## Motivos de descuento {#descuentos}

**Motivos de descuento** (discount reasons) say why something was discounted. The cashier picks one when discounting the whole bill or a line, so later you know what was discounted and why. Each reason suggests a percentage that can be changed on the spot. The tab reads **Descuentos**.

<p class="perm"><span>Who can:</span> <span class="tag">Ajustes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-descuentos.jpg' | relative_url }}" alt="The four default discount reasons: Invita la casa and Consumo del personal at 100 %, Cliente habitual and Demora at 10 %" loading="lazy" width="1440" height="390">
  <ol class="marks">
    <li><b>Agregar</b>: adds a reason.</li>
    <li><b>Sugiere</b> (suggests): the percentage it proposes. A comp is 100 %.</li>
  </ol>
  <figcaption>The reasons a new account starts with: on the house, staff meals, regular customer and delay.</figcaption>
</figure>

1. Tap **Agregar**.
2. Type the **Motivo** (reason) the way the place says it: Invita la casa (on the house), Dueños (owners), Cliente habitual (regular).
3. Set the **Porcentaje sugerido** (suggested percentage), from 0 to 100.
4. Tap **Guardar**.
{: .steps}

They are used by Salón discounts (permission **Descontar e invitar**) and by customers in Pedidos who carry their own discount. A discounted line still counts as sold: invoices and reports take what was actually charged, and a line comped at 100 % stays off the invoice. Reasons are never deleted: switch them off with **Activo**.

## Integraciones {#integraciones}

**Integraciones** (integrations) has a card for each outside service Fornu can connect to. Each card says how it stands and leads to where it is set up. Fornu works without any of them.

<p class="perm"><span>Who can:</span> <span class="tag">Ajustes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-integraciones.jpg' | relative_url }}" alt="The Rappi, PedidosYa and ARCA cards, each with its status, a line explaining what is missing and its button" loading="lazy" width="1440" height="400">
  <ol class="marks">
    <li>The integration's status.</li>
    <li>What it is missing or how it stands, and <b>Configurar</b> (set up) to go where it is set up.</li>
    <li><b>Conectar</b> (connect): leads to where connecting starts.</li>
    <li><b>Próximamente</b> (coming soon): can't be connected yet, and has no button.</li>
  </ol>
  <figcaption>The demo's cards.</figcaption>
</figure>

| Status | Means |
|---|---|
| **Conectada** (connected) | It has everything it asks for. On Rappi and PedidosYa, each unit selling there has its store linked. On ARCA, invoicing is active with the tax ID (CUIT) and point of sale. |
| **A medias** (halfway) | One step is missing: some units have their store and others don't, or the CUIT is entered but invoicing is not active yet. |
| **Sin conectar** (not connected) | Not set up yet. |
| **Próximamente** | It can't be connected from Fornu yet. |
| **No está en tu plan** (not in your plan) | The module is not on for the account. The card says «Pedile a Fornu que la sume a tu plan.» (ask Fornu to add it to your plan). |

- **Rappi** and **PedidosYa**: their orders come into the board by themselves, and the menu and sold-out items are published from Fornu. The button leads to [Unidades de negocio](#tiendas), where each store shows. If no brand sells on that platform, the card says it is turned on in the unit's row.
- **ARCA · Factura electrónica** (electronic invoicing with ARCA, the tax agency): invoices sales with a CAE, automatically or with one tap, plus credit notes. The button leads to Ajustes › Facturación, which needs the **Configurar la facturación** permission.

Someone who can't set up an integration sees «La conecta quien administra la cuenta.» (whoever runs the account connects it).

## Usuarios {#usuarios}

**Usuarios** (users) are the people who get into Fornu with email and password, from any browser. Administración (admin) can do everything, and everyone else can do what their roles allow. The roles are the same ones the PIN staff use, and they are set up in [Personal › Configuración]({{ '/en/projects/fornu/manual/personal/' | relative_url }}#roles).

<p class="perm"><span>Who can:</span> <span class="tag">Administración</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-usuarios.jpg' | relative_url }}" alt="The Usuarios screen with the admin user, an API user called Tablero 1 and the Visitas de soporte section" loading="lazy" width="1440" height="690">
  <ol class="marks">
    <li><b>Agregar</b>: adds a user with email and password.</li>
    <li><b>Contraseña</b> (password): sets a new password for that user.</li>
    <li><b>Nuevo usuario de API</b> (new API user): lets another system read the account.</li>
    <li><b>Secreto nuevo</b> (new secret): replaces that API user's secret at once.</li>
    <li><b>Visitas de soporte</b> (support visits): when someone from Fornu came in to help you.</li>
  </ol>
  <figcaption>The <b>Puede</b> (can) column shows «Todo» (everything), the user's roles or «Sin roles: no entra» (no roles, can't get in).</figcaption>
</figure>

### Add a user

1. Tap **Agregar**.
2. Type the **Nombre** and the **Email** they will sign in with.
3. Pick the **Tipo** (type): **Administración** can do everything and **Con roles** (with roles) can do what their roles allow.
4. For **Con roles**, pick their **Roles**. With none, they can't get in.
5. Set the **Contraseña inicial** (first password): at least 10 characters.
6. Tap **Guardar**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-usuario.jpg' | relative_url }}" alt="The form for adding a user: name, email, type set to Con roles, the roles to pick from and the first password" loading="lazy" width="620" height="540">
  <ol class="marks">
    <li><b>Tipo</b>: <b>Administración</b> or <b>Con roles</b>.</li>
    <li><b>Roles</b>: the same ones as the team.</li>
    <li><b>Contraseña inicial</b>: hand it over in person, and have them change it from Mi cuenta (my account).</li>
  </ol>
  <figcaption>A new user with roles.</figcaption>
</figure>

If a user with roles has none, signing in shows «Lucía todavía no tiene permisos: pedile a la administración que le dé un rol.» (Lucía has no permissions yet, ask the admin for a role).

### Change a password or switch someone off

- **Password**: tap **Contraseña** on their row, type the **Nueva contraseña** (new password) and tap **Cambiar** (change). You see «Contraseña cambiada» (password changed).
- **Switch off**: tap their row, turn off **Activo** and tap **Guardar**. There must always be one active admin: «Tiene que quedar al menos un administrador activo.»

Everyone changes their own email and password from their name at the top right, in **Mi cuenta: email y contraseña**. See [Getting in and around]({{ '/en/projects/fornu/manual/empezar/' | relative_url }}#mi-cuenta).

### API users {#usuarios-de-api}

**Usuarios de API** let another system read this account: the owner's dashboard, the accountant's tool, an integration. An API user sees what its roles allow and only reads: it never changes anything. The one exception is **Carga pedidos** (loads orders).

1. Tap **Nuevo usuario de API**.
2. Give it a **Nombre** that says what it is for or whose it is: «Tablero del dueño» (owner's dashboard), «Estudio contable» (accounting firm).
3. Pick its **Roles**: it reads sales with Caja, the menu with Carta, and so on.
4. If the other system has to load orders, turn on **Carga pedidos** and type in **Avisos a** (notify) the address where Fornu reports each step of those orders: confirmed, ready, on the way, delivered or rejected.
5. Tap **Guardar**. A window opens with the **Clave** (key) and the **Secreto** (secret), each with **Copiar** (copy).
6. Copy both, hand them to whoever sets up the other system, and tap **Ya los guardé** (I saved them).
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-usuario-api.jpg' | relative_url }}" alt="The form for a new API user called Tablero 1, with the Encargado/a role picked and Carga pedidos off" loading="lazy" width="620" height="340">
  <ol class="marks">
    <li><b>Roles</b>: what it can read.</li>
    <li><b>Carga pedidos</b>: lets that system load orders.</li>
  </ol>
  <figcaption>A dashboard that reads what the manager sees.</figcaption>
</figure>

<div class="callout"><p class="callout-title">Good to know</p><p>The secret is shown only once: copy it before closing the window. If it gets lost, <b>Secreto nuevo</b> issues another one at once, without asking, and whatever used the old one stops working: «Secreto nuevo: el anterior ya no sirve.» (new secret, the old one no longer works).</p></div>

The list shows each one's **Clave**, what it **Puede leer** (can read), its **Último uso** (last use, or «Nunca», never) and whether it is off or loads orders. **Editar** (edit) changes its name and roles, or switches it off.

### Support visits

**Visitas de soporte** shows when someone from Fornu came into this account to help you, and what they looked at or changed while there, over the last 90 days. It shows 15, with a button to see them all. If there were none: «Nadie de Fornu entró a esta cuenta en los últimos 90 días.»

<div class="callout tip"><p class="callout-title">Tip</p><p>In the demo, users and passwords can't be changed: «En la demo esto no se cambia: la usa todo el que la prueba. En tu cuenta, sí.» (this can't be changed in the demo, everyone who tries it uses it, but it can in your account).</p></div>

## Configuración {#configuracion}

**Configuración** (configuration) holds the account and its kitchen, which are one and the same: one stock that all its business units draw from. At the top, three shortcuts jump to each part: **La cocina y la caja** (the kitchen and the cash), **Impresión** (printing) and **Costos y precios** (costs and prices). Personal has another tab also called Configuración: that one is [the team's]({{ '/en/projects/fornu/manual/personal/' | relative_url }}#roles).

<p class="perm"><span>Who can:</span> <span class="tag">Ajustes</span></p>

### The kitchen and the cash

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-configuracion.jpg' | relative_url }}" alt="The kitchen and cash fields: name, address, time zone, the hour the day starts, hours before a clock-in counts as forgotten, cash count tolerance, late tolerance and the option to pause what the stock can't cover" loading="lazy" width="1440" height="470">
  <ol class="marks">
    <li><b>El día empieza a las</b> (the day starts at): an order at 2 a.m. belongs to the previous day if the day starts at 6.</li>
    <li><b>Un fichaje sin salida se da por olvidado a las (horas)</b> (a clock-in with no clock-out counts as forgotten after, hours): after that, the next PIN starts a new shift.</li>
    <li><b>Tolerancia del arqueo</b> (cash count tolerance): how far a payment method can be off when closing the drawer without saying why.</li>
    <li><b>Tolerancia para llegar (minutos)</b> (late tolerance, minutes): how many minutes after the schedule still aren't late.</li>
    <li><b>Pausar lo que no alcanza con el stock</b> (pause what the stock can't cover): stops offering what can't be made.</li>
  </ol>
  <figcaption>A new account's values.</figcaption>
</figure>

| Field | Default | What it is |
|---|---|---|
| **Nombre de la cocina** (kitchen name) | | Also the account's name. |
| **Dirección** (address) | | The place's address. |
| **Zona horaria** (time zone) | Argentina | Where each working day starts and ends. Also Uruguay, Chile, Paraguay, Brasil (São Paulo), Perú, Colombia and México. |
| **El día empieza a las** | 6 | Local hour, 0 to 23. With 6, an order at 2 a.m. counts on the previous day. |
| **Un fichaje sin salida se da por olvidado a las (horas)** | 16 | 6 to 24. After that many hours since clocking in, the next PIN tap starts a new shift and the earlier one waits to be fixed in [Asistencia]({{ '/en/projects/fornu/manual/personal/' | relative_url }}#asistencia). |
| **Tolerancia del arqueo** | $ 0 | How far a payment method can be off when closing the drawer without picking a reason. At $ 0, every difference asks why. See [Cash and sales]({{ '/en/projects/fornu/manual/caja/' | relative_url }}#arqueo). |
| **Tolerancia para llegar (minutos)** | 10 | With the Personal module. Clocking in up to this many minutes after the schedule doesn't count as late. |

### Pause what the stock can't cover {#pausar}

With this option, if the stock isn't enough to make a product, even preparing what is missing, the product is no longer offered on own orders and is switched off in the platform stores, if there are any. It comes back by itself when stock comes in, and from **Agotados** (sold out) it can be offered anyway for the day (see [Orders and delivery]({{ '/en/projects/fornu/manual/pedidos/' | relative_url }})).

When you tick it, before saving, Fornu shows what it would pause with today's stock: «Con el stock de ahora no se pausaría nada.» (nothing would be paused), or «Con el stock de ahora se pausarían 3 productos:» (3 products would be paused) with each product, its brand and what it is missing.

<div class="callout tip"><p class="callout-title">Tip</p><p>Turn it on only if purchases and stock counts are up to date. With stale stock, the list of what would be paused is most of the menu: look at it before saving.</p></div>

### Printing {#impresion}

**Impresión** sets where kitchen tickets come out and how they look on paper.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-impresion.jpg' | relative_url }}" alt="The Impresión part: the ticket printer's address, 80 or 58 mm paper, the Imprimir prueba button and a preview of a ticket on 58 mm paper" loading="lazy" width="900" height="522">
  <ol class="marks">
    <li><b>Impresora de comandas</b> (ticket printer): its address on the place's network, like 192.168.0.50. Empty if there is none.</li>
    <li><b>Papel</b> (paper): <b>80 mm</b>, the usual one, or <b>58 mm</b>, for small printers. It applies to every printer in the kitchen.</li>
    <li><b>Imprimir prueba</b> (print a test) and, next to it, what is still needed to test.</li>
    <li>How a ticket comes out on that paper: 42 characters per line on 80 mm, 32 on 58 mm.</li>
  </ol>
  <figcaption>A printer just typed in and not saved yet: the test waits for the save.</figcaption>
</figure>

1. Type the printer's address in **Impresora de comandas**.
2. Pick the **Papel**. The preview changes right away.
3. Tap **Guardar**.
4. Tap **Imprimir prueba**. That same ticket prints, on the chosen paper.
{: .steps}

Next to the button, Fornu says where things stand: «Cargá la impresora y guardá para probarla.» (enter the printer and save to test it), «Guardá los cambios para probar con ellos.» (save the changes to test them) or «Sale esta misma comanda, con el papel de arriba.» (this same ticket prints, on the paper above). After printing it says «Prueba en cola: sale en unos segundos.», or warns that the print agent hasn't connected yet and has to be paired in [Dispositivos](#dispositivos). Each station's printer is set in [Estaciones de cocina](#estaciones).

### Costs and prices

**Costos y precios** sets how the cost of each stock item and the margin of each sale are worked out.

| Field | Default | What it is |
|---|---|---|
| **Condición frente al IVA** (VAT status) | Monotributo | With **Monotributo** (simplified regime), VAT on purchases is not recovered and is part of each item's cost. With **Responsable inscripto** (VAT registered), items cost their price without VAT. |
| **IVA de los precios de venta** (VAT on sale prices) | 21 % | Only for Responsable inscripto: 21 %, 10,5 %, 27 %, 5 % or 2,5 %. Margins are worked out on the price without VAT. |
| **Ganancia sobre el costo (%)** (markup on cost) | 35 % | What the suggested price adds to the cost of each product that has no markup of its own. |
| **Un precio es viejo a los (días)** (a price is old after, days) | 30 | After that, the item warns that its price should be confirmed. |
| **El ritmo de consumo mira los últimos (días)** (usage looks at the last, days) | 14 | 3 to 90. What was used in those days works out how many days each item's stock will last. |

What these numbers do is shown in [Costs and reports]({{ '/en/projects/fornu/manual/costos-y-reportes/' | relative_url }}) and [Stock items and stock]({{ '/en/projects/fornu/manual/insumos-y-stock/' | relative_url }}).

### Save the changes

**Guardar** stays off until you change something. With the first change, the save bar sticks to the bottom of the screen, always at hand, with «Hay cambios sin guardar.» (unsaved changes), **Deshacer los cambios** (undo the changes) and **Guardar**. On a phone it sits above the bottom bar. Saving shows «Configuración guardada» (configuration saved).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-costos-guardar.jpg' | relative_url }}" alt="The Costos y precios part with the VAT status and the markup on cost, and below it the fixed bar with Hay cambios sin guardar, Deshacer los cambios and Guardar" loading="lazy" width="1440" height="260">
  <ol class="marks">
    <li><b>Condición frente al IVA</b>: decides whether VAT on purchases is a cost.</li>
    <li><b>Ganancia sobre el costo (%)</b>: the one the suggested price uses.</li>
    <li>The fixed bar: <b>Deshacer los cambios</b> puts everything back and <b>Guardar</b> saves it.</li>
  </ol>
  <figcaption>With an unsaved change, the bar stays in view.</figcaption>
</figure>

## Tus datos {#tus-datos}

**Tus datos** (your data): everything the account entered and ran in Fornu belongs to the account. This is where you download all of it, whenever you like, and where it explains how to close the account.

<p class="perm"><span>Who can:</span> <span class="tag">Administración</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-tus-datos.jpg' | relative_url }}" alt="The Tus datos screen with the Descargar todos los datos button and the explanation of how to close the account" loading="lazy" width="1440" height="480">
  <ol class="marks">
    <li><b>Descargar todos los datos</b> (download all the data): a ZIP with one spreadsheet per table.</li>
    <li><b>Dar de baja la cuenta</b> (close the account): requested from Fornu.</li>
  </ol>
  <figcaption>The download includes the menu, stock items, recipes, orders, purchases, expenses, cash, staff and customers.</figcaption>
</figure>

1. Tap **Descargar todos los datos**.
2. The file fornu-datos.zip downloads and you see «Descargado: todos los datos de la cuenta» (downloaded: all the account's data).
3. Open each spreadsheet in Excel or Google Sheets.
{: .steps}

Passwords, PINs and keys are not included: they are stored encrypted and never handed out. In the demo the button is off: «En la demo no se descargan: la usa todo el que la prueba.» (not downloaded in the demo, everyone who tries it uses it).

To close the account, ask Fornu. Closing it deletes all the account's data, so download it first. The details are in the terms and the privacy policy, linked on the same screen.

## Facturación {#facturacion}

With the Facturación electrónica (electronic invoicing) module, Ajustes has one more tab, **Facturación**, where the tax details and the point of sale are entered and invoicing with ARCA is switched on. It needs the **Configurar la facturación** permission and is explained in [Electronic invoicing]({{ '/en/projects/fornu/manual/facturacion/' | relative_url }}#configurar).

## Your account's modules {#modulos}

Fornu turns the modules on for each account. From inside the account, you notice it on the screens:

- A module that is on adds its tabs, plus fields, columns, buttons and notices on other screens. For example, Personal adds **Estado** and **Cobra** to the team and **Tolerancia para llegar** to this configuration.
- A module that is off shows nowhere, not even as a grey button. Its permissions vanish from the role editor but stay saved, and its card in [Integraciones](#integraciones) says «No está en tu plan».
- Nothing a module saved is deleted when it is turned off: it all comes back when it is turned on again.

Modules also come in bundles for each kind of place: **Dark kitchen**, **Restaurante** (restaurant), **Cafetería** (café) and **Salón Pro**. What each module and bundle brings is in the [manual's index]({{ '/en/projects/fornu/manual/' | relative_url }}#modulos).

<div class="callout tip"><p class="callout-title">Tip</p><p>On a phone, Ajustes sits under <b>Más</b> (more) in the bottom bar, with each tab by its full name.</p></div>
