---
layout: manual
manual: empezar
title: "Getting in and around · Fornu manual"
description: "How to get into Fornu with an email or the demo, how the screen is laid out, notices and dialogs, the search box, the home page and every keyboard shortcut."
permalink: /en/projects/fornu/manual/empezar/
---

## Signing in with email and password {#ingresar}

This is the way into the back office. The owner, the managers and the cashier sign in with their email and password from any browser, on a PC, a tablet or a phone, and see every screen their roles allow.

<p class="perm"><span>Who can:</span> anyone with an email user. Users are created in <a href="{{ '/en/projects/fornu/manual/ajustes/' | relative_url }}">Settings</a> › Usuarios.</p>

The app is in Spanish, so this manual names every button and message exactly as the screen shows it, with a short English gloss the first time.

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/empezar-ingresar.jpg' | relative_url }}" alt="The Ingresar screen on a phone: the theme switch at the top, the Email and Contraseña fields with the Entrar button, the link to use the device with a PIN, the Probar la demo button and the Conocé qué hace Fornu link" loading="lazy" width="390" height="844">
  <ol class="marks">
    <li><b>Claro · Oscuro · Como el dispositivo</b> (light, dark, same as the device): this device's theme. See <a href="#tema">The theme</a>.</li>
    <li><b>Email</b>, <b>Contraseña</b> (password) and <b>Entrar</b> (sign in). The button turns on once both fields are filled in.</li>
    <li><b>Usar este celular o PC en una cocina, con PIN</b> (use this phone or PC in a kitchen, with a PIN): pairs the device so staff can sign in with their PIN.</li>
    <li><b>Probar la demo</b> (try the demo): a sample kitchen, no account needed.</li>
    <li><b>Conocé qué hace Fornu</b> (see what Fornu does): the presentation page.</li>
  </ol>
  <figcaption>The sign-in screen on a phone.</figcaption>
</figure>

### Sign in

1. Type your email in **Email** and your password in **Contraseña**.
2. Tap **Entrar** or press <kbd>Enter</kbd>.
3. The [Inicio](#inicio) (home) page opens, with whatever needs your attention.
{: .steps}

If something goes wrong, the screen says so under the fields:

| Message | What happened |
|---|---|
| «El email o la contraseña no son correctos.» (the email or the password is wrong) | One of the two is wrong. The password is cleared so you can type it again. |
| «Demasiados intentos fallidos: probá de nuevo en X min.» (too many failed attempts, try again in X min) | Several wrong passwords in a row. Wait the minutes it says. |
| «Esta cuenta está desactivada.» (this account is deactivated) | The restaurant's account is deactivated, for all its users. |
| «Lucía todavía no tiene permisos: pedile a la administración que le dé un rol.» (Lucía has no permissions yet, ask the admin for a role) | Your user exists but has no role yet. Whoever runs the account gives you one in Ajustes › Usuarios. |

If your session expires while you work, Fornu brings you back to this screen on its own. The first time you open Fornu in a browser you may land on the presentation page instead: the **Ingresar** (sign in) button at the top right brings you here.

### Using the device with a PIN

The kitchen tablet, a courier's phone or the counter PC don't use your password. They are paired once with a code, and from then on each person signs in with their name and PIN. To do it, tap **Usar este celular o PC en una cocina, con PIN** and follow [Pairing the device]({{ '/en/projects/fornu/manual/cocina-y-reparto/' | relative_url }}#vincular).

## Trying the demo {#demo}

The demo lets you see Fornu working before you have an account, or practice without touching your restaurant's data. It is a sample kitchen with four brands (Doble Smash, Pollo Crocante, Bowl Verde and Pizzería) and two weeks of orders.

<p class="perm"><span>Who can:</span> anyone, without signing up.</p>

1. On the sign-in screen, tap **Probar la demo**. The presentation page has the same button.
2. You come in as the demo's administrator, with every module and every permission.
3. Every screen shows a band under the tabs: «Estás en la demo de Fornu: probá lo que quieras. Todos la comparten, y cada noche vuelve a como estaba.» (You're in the Fornu demo: try anything. Everyone shares it, and every night it goes back to how it was.)
{: .steps}

If the demo is being rebuilt, the screen says «La demo se está preparando: probá de nuevo en un rato.» (the demo is getting ready, try again in a while).

In the demo you can take orders, charge, change the menu, load stock and almost everything else. A few things stay locked, because everyone who tries the demo uses it:

- your own email and password, in **Mi cuenta** (my account),
- users and their passwords, in Ajustes › Usuarios, including the ones other systems use to read the account,
- downloading the account's data, in Ajustes › Tus datos,
- the tax details, the ARCA connection test and the delegation, in Ajustes › Facturación.

If you try, it says «En la demo esto no se cambia: la usa todo el que la prueba. En tu cuenta, sí.» (this can't be changed in the demo because everyone uses it, but in your own account it can).

<div class="callout"><p class="callout-title">Good to know</p><p>The demo is shared: whatever you load, others trying it at the same time can see. Don't type real customer or restaurant data.</p></div>

## The screen {#pantalla}

Every back-office screen has the same frame. At the top, the module groups (Pedidos, Carta, Insumos…). Below them, the sections of the open group as tabs. Then the page title with its explanation and its buttons. And under that, the page itself.

<p class="perm"><span>Who can:</span> everyone who signs in with an email. Each person only sees the groups and sections their roles allow.</p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/empezar-pantalla.jpg' | relative_url }}" alt="The demo's back office on Pedidos › Historial: the group bar at the top, the Pedidos tabs below, the demo band, the title Historial de pedidos with its explanation, and on the right the search button, the theme switch, the connection dot and the time" loading="lazy" width="1440" height="660">
  <ol class="marks">
    <li><b>Inicio · Pedidos · Carta…</b> (home, orders, menu): the groups. A tap opens the group's first section.</li>
    <li><b>En curso · Venta · Historial…</b> (current, sale, history): the open group's sections, by their short name.</li>
    <li>The page title, with its full name, and a line on what the page is for. Its buttons sit on the right, like <b>Exportar</b> (export).</li>
    <li><b>Buscar</b> (search): the search box. Shortcut <kbd>Ctrl</kbd>+<kbd>K</kbd>.</li>
    <li>The theme: light, dark or same as the device.</li>
    <li>The green connection dot and the time.</li>
  </ol>
  <figcaption>The demo open on Pedidos › Historial (order history). At the very top, the demo band.</figcaption>
</figure>

### Groups and sections

The groups come in this order: **Inicio** (home), **Pedidos** (orders), **Salón** (dining room), **Espacios** (spaces), **Carta** (menu), **Insumos** (stock items), **Costos** (costs), **Compras** (purchases), **Balances**, **Personal** (staff), **Reportes** (reports) and **Ajustes** (settings). A group only shows up if you can open at least one of its sections, and the groups of a module that is off never show. That is why each person sees a different bar.

Some groups carry a number. **Pedidos** shows how many orders are waiting to be confirmed. **Costos** shows how many problems there are to review. The number goes away when nothing is left.

A tab shows the section's short name and the page title shows the full one: the **Historial** tab opens the **Historial de pedidos** page. This manual writes paths with ›, as in Pedidos › Historial.

### The Más button {#mas}

When the groups don't fit across the screen, the last ones move into a **Más** (more) button at the end of the bar. It lights up when the open section is inside it, and it adds up the numbers of the groups it holds.

<div class="shot-pair">
<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/empezar-celular.jpg' | relative_url }}" alt="The demo on a phone: the search button, theme and time at the top, and at the bottom the bar with Inicio, Pedidos, Insumos, Compras and Más" loading="lazy" width="390" height="844">
  <ol class="marks">
    <li>The bottom bar, with up to four groups.</li>
    <li><b>Más</b>: every group and its sections.</li>
  </ol>
  <figcaption>On a phone, the groups move to the bottom.</figcaption>
</figure>
<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/empezar-mas.jpg' | relative_url }}" alt="A 1024-pixel screen with the Más button open, listing Personal, Reportes and Ajustes" loading="lazy" width="1024" height="330">
  <ol class="marks">
    <li><b>Más</b>: the groups that didn't fit.</li>
    <li>A tap opens the group.</li>
  </ol>
  <figcaption>On a narrow screen, Personal, Reportes and Ajustes sit behind Más.</figcaption>
</figure>
</div>

### On a phone

On a phone, or in a narrow window, the screen rearranges itself for your thumb:

- The groups move to a bar at the bottom, with up to four of these, in this order: Inicio, Pedidos, Salón, Insumos, Compras and Reportes. The rest, including Personal and Ajustes, go into **Más**.
- **Más** opens a sheet with every group and its sections, by their full names and with their numbers. Its own number adds up whatever is waiting in the groups that aren't on the bar.
- The section tabs slide sideways, and the open one stays in view.
- Each page's explanation shows two lines: tap it to read the rest.
- The page's buttons take the full width, under the title.
- Dialogs rise from the bottom as a sheet.
- The top keeps the search button, the theme, the time and your initial.

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/empezar-mas-celular.jpg' | relative_url }}" alt="The Más sheet open on a phone: the groups Inicio, Pedidos, Salón, Espacios and Carta, each with its sections as buttons" loading="lazy" width="390" height="844">
  <figcaption>The <b>Más</b> sheet on a phone: every group with its sections.</figcaption>
</figure>

### The clock and «En vivo» {#en-vivo}

On the right of the bar there is a dot and the time, large enough to read from the kitchen. On very wide screens you also see the day, the date and a word next to the dot:

| Dot | What it means |
|---|---|
| Green, **En vivo** (live) | Orders arrive by themselves, no reloading. |
| Amber, **Conectando** (connecting) | It is reconnecting. |
| **Sin conexión** (offline) | New orders may take a while to show up. |

If the connection drops for more than a few seconds, a band appears under the bar: «Sin conexión en vivo: los pedidos nuevos pueden tardar en aparecer. Reintentando…» (no live connection, new orders may be late, retrying). It goes away when the connection is back.

Anyone with the **Cocina** (kitchen) permission hears a chime when an order arrives to be confirmed, whatever section they are in. The browser tab warns too: with three orders waiting, its title starts with «(3)».

<div class="callout tip"><p class="callout-title">Tip</p><p>One look at the dot tells you whether the board is up to date. If it isn't green, don't assume nothing came in.</p></div>

### The theme: light or dark {#tema}

The three icons on the bar choose how Fornu looks on this device: **Claro** (light, the sun), **Oscuro** (dark, the moon) or **Como el dispositivo** (same as the device, the monitor), which follows the device's own setting. It starts on **Como el dispositivo**.

The choice is kept in this browser, and any other window of the same browser follows it at once. The switch is also on the sign-in screen and the PIN screen.

<div class="callout tip"><p class="callout-title">Tip</p><p>Since it is chosen per device, the kitchen tablet can stay dark while the office PC stays light.</p></div>

### Your user: Mi cuenta and Cerrar sesión {#mi-cuenta}

Your initial sits at the top right. On wide screens you also see your name and your kind of user: **Administración** (admin) if you run the account, **Con roles** (with roles) if you sign in with the roles you were given. Tap it to open the menu.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/empezar-usuario.jpg' | relative_url }}" alt="The user menu open at the top right: Administración, Mi cuenta: email y contraseña, and Cerrar sesión" loading="lazy" width="440" height="250">
  <ol class="marks">
    <li>Your initial: opens the menu.</li>
    <li><b>Mi cuenta: email y contraseña</b>.</li>
    <li><b>Cerrar sesión</b> (sign out).</li>
  </ol>
  <figcaption>Your user menu.</figcaption>
</figure>

<p class="perm"><span>Who can:</span> everyone who signs in with an email. Staff who sign in with a PIN have no Mi cuenta.</p>

To change your email or your password:

1. Tap your initial and choose **Mi cuenta: email y contraseña** (my account: email and password).
2. Change the **Email** if needed.
3. To change the password, type it in **Contraseña nueva** (new password, at least 8 characters) and again in **Repetila** (repeat it). Leave it empty to keep the current one.
4. Type your **Contraseña actual** (current password) to confirm it's you.
5. Tap **Guardar** (save). You'll see «Tus datos quedaron guardados» (your details were saved).
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/empezar-mi-cuenta.jpg' | relative_url }}" alt="The Mi cuenta panel with the email, a seven-character new password, Repetila and Contraseña actual empty, and at the bottom the notice that the new password needs at least 8 characters" loading="lazy" width="620" height="900">
  <ol class="marks">
    <li><b>Email</b>: the one you sign in with.</li>
    <li><b>Contraseña nueva</b>, and below it <b>Repetila</b>.</li>
    <li><b>Contraseña actual</b>: needed to save.</li>
    <li>What is missing, in one line.</li>
    <li><b>Guardar</b>: turns on when nothing is missing.</li>
  </ol>
  <figcaption>Mi cuenta, with a new password that is too short.</figcaption>
</figure>

While something is missing, the left of the buttons says what: «La contraseña nueva tiene que tener al menos 8 caracteres.» (the new password needs at least 8 characters), «Las contraseñas nuevas no coinciden.» (the new passwords don't match) or «Falta la contraseña actual.» (the current password is missing). A wrong current password shows «La contraseña actual no es correcta.»

To leave, tap **Cerrar sesión** (sign out). Fornu asks «¿Cerrar la sesión?» and warns that signing back in on this device will need the email and password. Tap **Cerrar sesión** to confirm, or **Volver** (back) to stay.

## Notices and Deshacer {#avisos}

Fornu confirms what you did with a short notice, and when something fails it says so where you will see it.

- **Things that worked** show in a green box in a corner (at the top on a phone). It disappears after 4 seconds. For example, «Descontado: 500 g de Arroz (vencido)» (deducted: 500 g of rice, expired).
- **Deshacer** (undo). Some notices carry that button and last 8 seconds, so you can change your mind in time: when you hide the first steps on Inicio, pause a menu product, take something off a table or move a table. Tap it and everything goes back to how it was.
- **Errors** stay on the page, under the title, until you close them with the × or do something else.
- **Inside a dialog**, the error shows above its buttons.
- **On the orders board**, each card shows its own error: «No se pudo: …» (couldn't do it).
- **If a section doesn't load**, it says «No se pudo cargar: …» (couldn't load) with a **Reintentar** (retry) button.
- **If a screen breaks**, it says «Algo falló en esta pantalla» (something failed on this screen) and «Lo demás sigue andando. Si vuelve a pasar, recargá la página.» (everything else keeps working, and if it happens again, reload the page), with **Reintentar** and **Recargar la página** (reload the page).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/empezar-deshacer.jpg' | relative_url }}" alt="The notice Doble cheddar pausado, at the bottom left of the menu, with the Deshacer button" loading="lazy" width="760" height="340">
  <ol class="marks">
    <li><b>Deshacer</b> (undo): puts everything back.</li>
  </ol>
  <figcaption>Pausing a product leaves eight seconds to change your mind.</figcaption>
</figure>

## How dialogs behave {#dialogos}

Forms and confirmations open in a dialog over the page. They all work the same way:

- They close with the ×, with <kbd>Esc</kbd> or with a click outside.
- If you typed something, they ask first: «Hay cambios sin guardar.» (there are unsaved changes), with **Seguir editando** (keep editing) and **Descartar** (discard). One stray tap won't wipe what you loaded.
- While a field is missing, the left of the buttons says what is missing, and the main button stays off until it's filled in.
- <kbd>Ctrl</kbd>+<kbd>Enter</kbd> presses the main button without reaching for the mouse. On a PC, the dialog's footer reminds you.
- Confirmations have **Volver** to back out.
- On a phone they rise from the bottom as a sheet.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/empezar-sin-guardar.jpg' | relative_url }}" alt="The footer of a dialog with the text Hay cambios sin guardar and the Seguir editando and Descartar buttons" loading="lazy" width="620" height="88">
  <figcaption>Closing a dialog with changes: the footer asks first.</figcaption>
</figure>

## Searching with Ctrl+K {#buscar}

One box to jump to any section, product, stock item, order or supplier without going through the menus. Open it with the **Buscar** button on the bar, with <kbd>Ctrl</kbd>+<kbd>K</kbd> (<kbd>Cmd</kbd>+<kbd>K</kbd> on a Mac) or, on a phone, with the magnifier.

<p class="perm"><span>Who can:</span> everyone. Each kind of result only shows to whoever can open it.</p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/empezar-buscar.jpg' | relative_url }}" alt="The search box with the word papas: two Papas fritas products from different brands, the prepared item Papas cortadas and the supply Cono para papas, each with its tag" loading="lazy" width="980" height="380">
  <ol class="marks">
    <li>What you type. Accents don't matter.</li>
    <li>What each result is: <b>Producto</b> (product), <b>Producción</b> (prepared item), <b>Inventario</b> (supply)…</li>
  </ol>
  <figcaption>Searching for «papas» (potatoes): products from two brands, a prepared item and a supply.</figcaption>
</figure>

### What it finds

| Result | Tag | Opens | Needs |
|---|---|---|---|
| Menu products, with their brand and category (and «pausado», paused, if they are) | **Producto** | The menu, on that product | Carta |
| Stock items | **Ingrediente**, **Producción** or **Inventario** | Their list, with the item open | Insumos |
| Orders from the last 60 days, like «#12 · Lucía Fernández» | **Pedido** (order) | That day's history, with the order open | Pedidos |
| Suppliers | **Proveedor** (supplier) | Proveedores | Proveedores, with the Proveedores y compras module |
| **Marcar agotados** (mark sold out) | **Pedidos** | The board, with the sold-out list open | Cocina |
| Sections | Their group | The section | The section's permission |

A few details that save time:

- A number, like «12» or «#12», finds that order on any day. Any other text is matched against the customer's name and the platform's order number.
- Sections can also be found by everyday words: «rendir» (hand over cash) leads to the couriers' cash, «ayer» (yesterday) to the history, «vender» (sell) to Venta, «pin» to the team and «vincular» (pair) to Dispositivos.
- «agotado», «se acabó», «sin stock» or «pausar» (sold out, ran out, out of stock, pause) go straight to marking what ran out.
- With the box empty, it lists every section you can open.
- Products, items and orders show up from the second letter. Sections, from the first.
- While it looks it says «Buscando…» (searching). With no match, «Nada coincide con «…».» (nothing matches).

### With the keyboard

1. Press <kbd>Ctrl</kbd>+<kbd>K</kbd> and type.
2. Move with <kbd>↑</kbd> and <kbd>↓</kbd>.
3. Press <kbd>Enter</kbd> to open the highlighted result. If the answer is still arriving, it waits and then opens it.
4. <kbd>Esc</kbd> closes the box without going anywhere.
{: .steps}

## Inicio {#inicio}

Inicio (home) is where everyone lands: what needs attention right now, the first steps of a new account and, with the Reportes module, how each brand's sales are going.

<p class="perm"><span>Who can:</span> everyone. Each part only shows to whoever can deal with it.</p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/empezar-inicio.jpg' | relative_url }}" alt="Inicio on a 1024-pixel screen: Para atender with the line 1 insumo está en el mínimo, the first steps with 4 de 5 listos and the step left, the line with what is done, and the start of Cómo te fue with the period buttons" loading="lazy" width="1024" height="768">
  <ol class="marks">
    <li>A line in <b>Para atender</b> (to deal with). Tap it and it takes you where it gets solved.</li>
    <li><b>Primeros pasos para empezar a vender</b> (first steps to start selling) and how many are done.</li>
    <li><b>Ocultar</b> (hide): removes the first steps from this device.</li>
    <li>The next step, with its button.</li>
    <li>The steps already done, on one line.</li>
    <li><b>Cómo te fue</b> (how it went): the sales period.</li>
  </ol>
  <figcaption>Inicio for an account that is almost set up.</figcaption>
</figure>

### Para atender

A short list of what is worth sorting out today. Each line is a button that takes you to the screen where it gets solved, and red lines come first.

| Line | Colour | Shown to whoever has | Takes you to |
|---|---|---|---|
| «2 pedidos esperan confirmación» (2 orders waiting to be confirmed) | Red | Cocina | The orders board |
| «1 pago vencido · $ 85.000» (1 overdue payment) | Red | Gastos | Expenses, filtered to what must be paid |
| «3 insumos están en el mínimo» (3 items at their minimum) | Amber | Stock | Stock, the items at their minimum |
| «4 insumos se acaban antes de una semana» (4 items run out within a week) | Amber | Stock | Stock, the items running out soon |
| «$ 12.000 en efectivo de días anteriores sin rendir · Martín» (cash from earlier days not handed over) | Amber | Pedidos | Couriers' cash |
| «2 pagos vencen en los próximos 7 días · $ 140.000» (2 payments due in the next 7 days) | Amber | Gastos | Expenses |
| «3 problemas de precios o recetas para revisar» (3 price or recipe problems to review) | Amber | Costos | Costos › Para revisar |

The last one only exists with the Costos y márgenes module. When there is nothing, it says «Nada urgente: pedidos, costos, stock y pagos están al día.» (nothing urgent: orders, costs, stock and payments are up to date).

### Primeros pasos para empezar a vender

A checklist that gets a new account ready to sell, in order. It shows how many steps are done («3 de 5 listos», 3 of 5 done), a progress bar and only the steps still missing. The next one has the highlighted button.

<p class="perm"><span>Who can:</span> <span class="tag">Ajustes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/empezar-primeros-pasos.jpg' | relative_url }}" alt="Inicio for a new account: Para atender says Nada urgente, and the first steps show 0 de 5 listos with the five steps and their buttons" loading="lazy" width="1440" height="740">
  <figcaption>A brand-new account: five steps to go.</figcaption>
</figure>

| Step | What for | Button |
|---|---|---|
| **Creá tu primera unidad de negocio** (create your first business unit) | The brand you sell: its name, its colour and the channels it sells on. | **Crear** (create) |
| **Cargá un producto con su precio** (add a product with its price) | What the menu offers, in its category. | **Ir a la carta** (go to the menu), or **Importarla de una planilla** (import it from a spreadsheet) |
| **Cargá los ingredientes y la receta de un producto** (add the ingredients and recipe of a product) | Without a recipe there is no cost, no margin and no stock deduction. | **Cargar ingredientes** (add ingredients), or **Importarlos de una planilla** |
| **Tomá un pedido propio de prueba** (take a test order of your own) | You see how it reaches the kitchen and what it takes out of stock. | **Ir a pedidos** (go to orders) |
| **Sumá a tu equipo y vinculá la tablet de la cocina** (add your team and pair the kitchen tablet) | Each person signs in on the tablet with their PIN, without your password. | **Sumar personal** (add staff), or **Vincular la tablet** (pair the tablet) once there is staff |

The steps already done are gathered on one line, «Listo: …» (done). A last line at the bottom talks about the ticket printer («Si tenés impresora de comandas, cargala en Configuración; sin ella, la cocina trabaja con la tablet.», meaning set up the ticket printer in Configuración if you have one, or the kitchen works from the tablet) and, with the Delivery por plataformas module, about the Rappi or PedidosYa store: if it is already linked, it reminds you to publish the menu from Unidades de negocio, and if not, it says «Para vender en las plataformas, pedile a Fornu que vincule tu tienda.» (to sell on the platforms, ask Fornu to link your store).

The list disappears by itself once all five steps are done. To remove it sooner, tap **Ocultar**: you'll see «Primeros pasos guardados» (first steps put away) with **Deshacer**.

<div class="callout tip"><p class="callout-title">Tip</p><p><b>Ocultar</b> only applies to this device. On another PC or on your phone the list keeps showing until you hide it there too.</p></div>

### Cómo te fue

Sales and what was left over for each brand and each channel, over the period you pick. It is a quick summary: the detail lives in the reports.

<p class="perm"><span>Who can:</span> <span class="tag">Reportes</span>, with the Reportes module on.</p>

For people with Ajustes, it shows up once the account has at least one order.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/empezar-como-te-fue.jpg' | relative_url }}" alt="Cómo te fue in the demo: the figures for sales, result, orders and cancelled, the wages warning, the table by brand with Propios, Rappi, Total and Resultado, the note explaining deja, and the Resumen de ventas and Rentabilidad buttons" loading="lazy" width="1440" height="870">
  <ol class="marks">
    <li><b>Ventas</b> (sales), <b>Resultado</b> (result), <b>Pedidos</b> (orders) and <b>Cancelados</b> (cancelled) for the period.</li>
    <li>A warning when the result leaves out wages.</li>
    <li>One column for each channel that sold.</li>
    <li>What was sold and, below it, what it <b>deja</b> (leaves).</li>
    <li>What <b>deja</b> and <b>resultado</b> mean.</li>
    <li>The full reports.</li>
  </ol>
  <figcaption>Cómo te fue in the demo, for last week.</figcaption>
</figure>

To choose the period, tap **Hoy** (today), **Ayer** (yesterday), **Semana pasada** (last week, Monday to Sunday, the default), **Últimos 7 días** (last 7 days, up to yesterday, whole days), **Este mes** (this month), **Mes pasado** (last month) or **Otras fechas** (other dates), which shows **Desde** and **Hasta** (from, to). The reports use the same period for as long as the browser tab stays open.

- **Ventas** compares with the period before: «+5,2 % vs. la semana anterior» (vs. the week before).
- **Resultado** says what share of the sales without VAT was left, in green or red.
- **Pedidos** carries the average ticket, and **Cancelados** the amount.
- If the period has no wages paid or loaded as an expense, it warns that the result leaves them out and says where they are loaded.
- The table has a row per business unit and a column per channel (**Propios**, own orders, **Rappi**, **PedidosYa**, **Salón**), plus **Total** and **Resultado**. Each cell shows what was sold and «deja $ …», in red when negative. With more than one brand, the **Todas** (all) row adds them up.
- **Deja** is what was sold without VAT, minus the channel's commission and the stock those orders used. The **resultado** also takes off the unit's expenses and its share of the shared ones.
- **Resumen de ventas** (sales summary) and **Rentabilidad** (profitability) open the full reports, covered in [Costs and reports]({{ '/en/projects/fornu/manual/costos-y-reportes/' | relative_url }}).

If no brand sold anything, it says «Ninguna unidad de negocio vendió en este período.» (no business unit sold in this period). On a phone the table turns into one card per brand.

<div class="callout tip"><p class="callout-title">Tip</p><p><b>Hoy</b> follows the kitchen's business day, which starts at the configured hour. At 1 a.m., the night's sales still count as «today».</p></div>

## Keyboard shortcuts {#atajos}

On a PC the keyboard saves trips to the mouse. On a phone the keyboard hints are hidden.

| Keys | Where | What it does |
|---|---|---|
| <kbd>Ctrl</kbd>+<kbd>K</kbd> (<kbd>Cmd</kbd>+<kbd>K</kbd> on a Mac) | Any back-office screen | Opens and closes the [search box](#buscar). |
| <kbd>↑</kbd> <kbd>↓</kbd> | In the search box | Moves through the results. |
| <kbd>Enter</kbd> | In the search box | Opens the highlighted result. |
| <kbd>N</kbd> | On the orders board | Opens **Nuevo pedido** (new order). Not while you are typing in a field or with a dialog open. |
| <kbd>Enter</kbd> | In the phone field of a new order | Picks the first matching customer. |
| <kbd>Ctrl</kbd>+<kbd>Enter</kbd> (<kbd>Cmd</kbd>+<kbd>Enter</kbd> on a Mac) | In any dialog | Presses the main button. |
| <kbd>Esc</kbd> | In a dialog or the search box | Closes it. With unsaved changes, it asks first. |
| <kbd>0</kbd> to <kbd>9</kbd>, <kbd>Backspace</kbd>, <kbd>Enter</kbd> | On the PIN pad | Types the PIN, deletes the last digit and signs in. |
| <kbd>Enter</kbd> | On the sign-in screen | Signs in with the email and password. |
