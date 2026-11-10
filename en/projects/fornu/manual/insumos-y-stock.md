---
layout: manual
manual: insumos-y-stock
title: "Stock items and stock · Fornu manual"
description: "How to set up ingredients, prepared items and supplies with their cost, how to keep stock with deliveries, batches, waste and counts, and how to plan a production run."
permalink: /en/projects/fornu/manual/insumos-y-stock/
---

## Ingredients, prepared items and supplies {#insumos}

Stock items are everything the kitchen uses to make the menu, each with what it costs. Recipes are built from them, and every product's cost comes from them. They are split across three tabs under Insumos (stock items):

- **Ingredientes** (ingredients): the raw materials bought to cook with.
- **Producción** (prepared items): what the kitchen makes in batches from a recipe and does not sell on its own, such as portioned patties or a sauce. Each one is an «elaboración».
- **Inventario** (supplies): what is bought and used without cooking it, such as disposables and packaging, cleaning products, tableware and stationery.

Any recipe can use items from all three. Each tab has its own button to add one (**Ingrediente**, **Elaboración** or **Artículo**) and **Importar planilla** (import spreadsheet).

<p class="perm"><span>Who can:</span> <span class="tag">Insumos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-ingredientes.jpg' | relative_url }}" alt="The ingredients list grouped into Meat and Fruit and vegetables, with how each one is bought and at what price, the supplier, the yield and the cost of each usable kilo." loading="lazy" width="1440" height="675">
  <ol class="marks">
    <li><b>Cómo entra</b> (how it comes in): how it is bought, at what price and since when that price holds, such as «caja de 10 kg a $ 75.000» (a 10 kg box at $ 75,000).</li>
    <li><b>Proveedor</b> (supplier): who it is bought from, with the Suppliers and purchases module.</li>
    <li><b>Rinde</b> (yield): how much of what comes in can be used.</li>
    <li><b>Costo utilizable</b> (usable cost): what each kilo, litre or unit actually used costs, with the yield already taken into account.</li>
    <li><b>Estado</b> (status): what is worth checking on that item.</li>
  </ol>
  <figcaption>The demo's ingredients, grouped by category.</figcaption>
</figure>

Yield changes the cost. Chicken breast costs $ 75,000 for a 10 kg box, which is $ 7,500 a kilo, but it yields 92%: each kilo actually used costs $ 8,152.17.

The search box finds items by name, category or supplier. An ⓘ next to a name means the item has a note: hover to read it. Inactive items are dimmed.

The **Estado** column shows the most important warning and how many more there are («+2»). Hover to see them all:

| Warning | What it means |
|---|---|
| «Falta el precio» | The price is missing, so everything that uses the item has no cost. |
| «Sin receta» | A prepared item with no recipe yet. |
| «… no tiene precio» | The prepared item's recipe uses an item with no price. |
| «Precio de hace N días» or «Precio sin fecha» | The price is N days old, or has no date, and may be out of date. How many days count as old is set in [Ajustes › Configuración]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#configuracion). |
| «Tiene una nota» | Someone left a note on the item. |
| «Lleva …, que está desactivado» | The recipe uses an item that is switched off. |

### Add an ingredient or a supply {#nuevo-insumo}

1. Tap **Ingrediente**, or **Artículo** in Inventario.
2. Type the **Nombre** (name), pick the **Categoría** (category) and the **Unidad** (unit).
3. Fill in how it is bought: **Se compra por** (bought by), **Cuánto trae** (how much it holds), the price of each pack and its VAT.
4. If some is lost when cleaning it, set the **Rendimiento** (yield). If you want Fornu to warn when it runs low, set the **Stock mínimo** (minimum stock).
5. Tap **Guardar** (save), or press <kbd>Ctrl</kbd> + <kbd>Enter</kbd>.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-ficha.jpg' | relative_url }}" alt="Two ingredient panels: on the left the top of a new one, with unit, how it is bought, price and VAT. On the right the bottom of the minced beef, with yield, minimum stock, note, price history and where it is used." loading="lazy" width="1260" height="900">
  <ol class="marks">
    <li><b>Unidad</b>: grams, millilitres or units. Recipes, stock and counts all use it. It cannot be changed later.</li>
    <li><b>Se compra por</b> and <b>Cuánto trae</b>: the pack (bag, box, egg tray) and how much it holds, in the item's unit.</li>
    <li><b>Precio de cada una</b> (price of each), <b>El precio es</b> (the price is) and <b>IVA</b> (VAT): the price of one pack, as shown on the voucher.</li>
    <li><b>Rendimiento (%)</b>: how much of what comes in can be used.</li>
    <li><b>Historial de precios</b> (price history): every price it has had, since when and where it came from.</li>
    <li><b>Dónde se usa</b> (where it is used): the recipes and extras that use it.</li>
  </ol>
  <figcaption>Left, the top of a new ingredient. Right, the bottom of an existing one.</figcaption>
</figure>

| Field | What it is for |
|---|---|
| **Nombre** | Required. |
| **Categoría** | One of the tab's active categories. |
| **Unidad** | **Gramos**, **Mililitros** or **Unidades**. Supplies start in units. It is fixed once saved, because stock and recipes are kept in that unit. |
| **Se compra por** | The pack: box, bag, kg, pack. Needed to save: without it, the footer says «Falta cómo se compra (caja, bolsa, kg…).» (how it is bought is missing). |
| **Cuánto trae** | How much each pack holds, in the item's unit. It starts at 1,000 g, or 1 unit. Also needed to save: without it, the footer says, for example, «Falta cuántos g trae cada bolsa.» (how many grams each bag holds is missing). |
| **Precio de cada una** | The price of one pack. Underneath, it says what it costs the account. Purchases with a price update it on their own. |
| **El precio es** | **Con IVA, como en un ticket** (with VAT, as on a receipt) or **Sin IVA, como en una factura A** (without VAT, as on an A invoice). |
| **IVA** | 21%, 10.5%, 27%, 5%, 2.5% or **Exento (0%)** (exempt). Meat, fruit, vegetables and flour usually carry 10.5%. |
| **Precio desde** (price since) | The price's date. It jumps to today when you change the price, unless you pick another date by hand. Without a date, Fornu cannot tell whether the price is current. |
| **Proveedor** | Who it is bought from. **+ Proveedor nuevo** (new supplier) creates one right there with its name and CUIT (tax ID). It shows with the Suppliers and purchases module, for people with the **Proveedores** permission. |
| **Rendimiento (%)** | In Ingredientes and Producción. Use 80% if a fifth is lost when cleaning it. The usable cost rises in proportion. |
| **Stock mínimo** | When stock reaches this number, the item shows as at its minimum, in Stock and on the home page. |
| **Activo** (active) | Off, the item is no longer offered in purchases or counts. Items are switched off rather than deleted. |
| **Nota** (note) | Up to 400 characters for whoever keeps the prices. It is never printed. |

What an item costs depends on the account's **Condición frente al IVA** (VAT status) in [Ajustes › Configuración]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#configuracion). For a Responsable inscripto (VAT-registered business), cost excludes VAT, because the VAT is recovered. For a Monotributo (simplified regime), cost includes it. Under the price, the form says which one it uses, and **El precio es** starts on the matching option.

<div class="callout"><p class="callout-title">Good to know</p><p>If you switch off an item that a recipe uses, Fornu warns: «Desactivado, las recetas que lo llevan lo siguen descontando, pero no se pueden guardar cambios en ellas hasta sacarlo o reactivarlo.» (those recipes still deduct it, but they cannot be changed until it is removed or switched back on). Check <b>Dónde se usa</b> first.</p></div>

### Price history and where it is used {#historial-precios}

On an existing item, **Historial de precios** shows the last six prices, and **Ver los N** (see all N) shows the rest. Each row has the date, the price, the VAT, how much it moved (red if it went up, green if it went down) and where it came from. Hover to see who changed it and when.

| Origin | What happened |
|---|---|
| **Alta** | The price it was created with. |
| **Editado** | Someone changed it by hand. |
| **Compra** | A stock purchase brought it in. |
| **Compra en Stock** | A delivery logged from Stock. |
| **Cambio masivo** | A **Cambiar precio** on several items at once. |
| **Compra anulada** | The purchase that set it was voided, and the earlier price came back. |

**Dónde se usa** lists the products, the prepared items (such as «Producción: Salsa de la casa») and each business unit's extras that use the item. If nothing does, it reads «Ninguna receta ni adicional lo lleva.» (no recipe or extra uses it).

### Add a prepared item and its recipe {#elaboracion}

A prepared item costs whatever its recipe uses, so it is set up in two steps.

1. In Producción, tap **Elaboración**.
2. Type the name, category, unit and how much one batch makes, in **Una tanda rinde** (one batch makes). Tap **Guardar**.
3. On its row, tap **Receta** (recipe).
4. Add the items one batch uses, with their quantities, and tap **Guardar**. Fornu confirms «Receta guardada».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-produccion.jpg' | relative_url }}" alt="The prepared items list with the large pizza dough ball under portioned items and five semi-prepared items, each with its batch size, the cost of each kilo or unit and a Receta button." loading="lazy" width="1440" height="610">
  <ol class="marks">
    <li><b>Cómo entra</b>: the batch size and how many items it uses, such as «Tanda de 1,5 kg con 4 insumos» (a 1.5 kg batch with 4 items).</li>
    <li><b>Costo utilizable</b>: what each kilo or unit costs, from its recipe.</li>
    <li><b>Receta</b>: opens what one batch uses.</li>
  </ol>
  <figcaption>The demo's prepared items.</figcaption>
</figure>

The top of the recipe shows what one batch makes and what it costs, whole and per kilo or unit. Until it has a recipe, the item's status reads «Sin receta». A recipe needs at least one item, and a prepared item cannot contain itself, not even through another prepared item.

### Change many at once {#cambios-masivos}

Tick the items in the list and use the bar that appears above it:

- **Cambiar precio** (change price): up or down by a percentage or an amount, with rounding. Each new price applies from today and goes into the item's history. Items without a price stay as they are. It is not offered in Producción, since a prepared item's cost comes from its recipe.
- **Cambiar categoría** (change category): moves them all to the same category.
- **Cambiar proveedor** (change supplier): they are all bought from the same supplier from now on. It comes with the Suppliers and purchases module.
- **Quitar la selección** (clear selection).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-cambiar-proveedor.jpg' | relative_url }}" alt="One ingredient ticked, the bar with Cambiar precio, Cambiar categoría, Cambiar proveedor and Quitar la selección, and on the right the panel to set the supplier of 1 ingredient with the Se compran a field." loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li>The selection bar, with how many items are ticked.</li>
    <li><b>Se compran a</b> (bought from): the supplier for every ticked item.</li>
    <li><b>Aplicar</b> (apply).</li>
  </ol>
  <figcaption>Setting the supplier of several ingredients at once.</figcaption>
</figure>

<div class="callout"><p class="callout-title">Good to know</p><p><b>Cambiar proveedor</b> starts on <b>Sin proveedor</b> (no supplier). Tapping <b>Aplicar</b> without picking one removes the supplier from every ticked item.</p></div>

### Stock item categories {#categorias-insumos}

Below each list is the list of its categories, with how many items each holds and its order. A new account starts with these:

| Tab | Categories |
|---|---|
| Ingredientes | Carnes, Verduras y frutas, Lácteos y fiambres, Panificados, Almacén and Bebidas (meat, fruit and vegetables, dairy and cold cuts, bread, dry goods, drinks) |
| Producción | Porcionados and Semielaborados (portioned, semi-prepared) |
| Inventario | Descartables y packaging, Limpieza, Bazar and Librería (disposables and packaging, cleaning, tableware, stationery) |

Each category has **Nombre**, **Orden** (order) and, when editing, **Activa** (active). A category that holds items cannot be deleted. Move them elsewhere, or switch it off so new items no longer get it. If a tab has no active categories left, its add button is disabled and the screen asks «Creá primero una categoría, más abajo.» (create a category first, further down).

## Stock {#stock}

How much of each item this kitchen has, how many days it lasts, what it is worth and what is running short. Quick deliveries, batches, waste and counts are all logged here. Every change is kept as a movement in the item's history, so you can always see what happened.

It lives in Insumos › **Stock**. It is also the **Stock** tab on the shop's device, for people with the permission.

<p class="perm"><span>Who can:</span> <span class="tag">Stock</span></p>

The **Encargado/a** (manager) role of a new account already has it.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-stock.jpg' | relative_url }}" alt="The Stock screen with the stock value, five items at their minimum, five running out within seven days and what is sitting unused, and two prepared items warning that their production was not logged." loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li>The figures: <b>Valor del stock</b> (stock value), <b>En el mínimo</b> (at minimum), <b>Se acaban en 7 días</b> (run out within 7 days) and <b>Sin uso en 2 semanas</b> (unused for 2 weeks, or the account's window). Tap one to filter the list.</li>
    <li><b>Todo</b> (all), <b>Ingredientes</b>, <b>Producción</b> or <b>Inventario</b>. The search box is below.</li>
    <li>«Faltó registrar lo producido» (production not logged): more of a prepared item was sold than was logged as made. <b>Registrar lo usado</b> (log what was used) fixes it.</li>
    <li><b>Alcanza para</b> (lasts): how many days it lasts at the current rate of use.</li>
    <li><b>Producir</b> (make), or <b>Entrada</b> (delivery) on a bought item, and the <b>⋯</b> menu with <b>Conteo</b> (count), <b>Merma</b> (waste) and <b>Historial</b> (history).</li>
    <li><b>Contar stock</b> (count stock): a count of the whole stock.</li>
  </ol>
  <figcaption>The demo's stock. The two prepared items at the top were sold without their batches being logged.</figcaption>
</figure>

| Figure | What it says |
|---|---|
| **Valor del stock** | What everything on hand is worth, at today's cost. |
| **En el mínimo** | How many items are at or below their minimum. Red if there are any. |
| **Se acaban en 7 días** | Items that will not last a week at the current rate: below it says, for example, «al ritmo de las últimas 2 semanas» (at the rate of the last 2 weeks). Tapping it sorts by what runs out first. |
| **Sin uso en 2 semanas** (or the account's window, such as «Sin uso en 10 días») | What is sitting idle: its value and how many items. Tapping it sorts by value. |

| Column | What it shows |
|---|---|
| **Insumo** | The name and category. If the item has a minimum, a bar shows how close it is: amber near the minimum, red at it or below. |
| **Hay** (on hand) | What there is, in grams, millilitres or units. Red when low. |
| **Mínimo** | The item's minimum stock. |
| **Usa por día** (used per day) | Daily use, counting orders and production. |
| **Alcanza para** | «N días», «Menos de 1 día», «Más de 60 días», «Sin stock» (out of stock) or «Sin uso reciente» (no recent use). Red under 3 days, amber under 7. |
| **Valor** (value) | What the stock on hand is worth. |

The list starts with what is short. Tap **Insumo**, **Alcanza para** or **Valor** to sort by it. The rate of use looks at the account's window, set in **El ritmo de consumo mira los últimos (días)** in [Ajustes › Configuración]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#configuracion): 14 days unless someone changed it, which the screen shows as «las últimas 2 semanas» (the last 2 weeks).

On the home page, the warnings «N insumos están en el mínimo» and «N insumos se acaban antes de una semana» open this screen already filtered.

With **Pausar lo que no alcanza con el stock** (pause what stock cannot cover) on, in [Ajustes › Configuración]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#pausar), a product that cannot be made with what is on hand stops being offered for own orders and is switched off on the platforms until stock comes in. For that to work well, purchases and counts need to be up to date.

### Log a delivery {#entrada}

To add something that arrived without going through Purchases: a small top-up, something the owner brought in.

1. Tap **Entrada** on the item's row.
2. Type how many packs came in. The field names the pack, as in **Cantidad (bolsa)** (quantity, bags), and underneath it shows the total: «Cada bolsa trae 25 kg: entran 50 kg.» (each bag holds 25 kg, 50 kg come in).
3. Check the price per pack, whether it includes VAT, and the VAT rate. It starts at the last price.
4. If you like, note where it came from.
5. Tap **Registrar** (log). Fornu confirms «Entrada registrada».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-entrada.jpg' | relative_url }}" alt="The Entrada de mercadería panel for pan de papa: Cantidad 2 bags, Cada bolsa trae 12 u: entran 24 u, the price per bag, whether it includes VAT, the VAT and De dónde vino" loading="lazy" width="620" height="900">
  <figcaption>Two bags of pan de papa: 24 units come in.</figcaption>
</figure>

The price you enter updates the item's cost and the margins of everything that uses it, and goes into the price history as **Compra en Stock**.

<div class="callout"><p class="callout-title">Good to know</p><p>A delivery logged here creates no voucher and no debt with the supplier. To record a supplier's delivery note or invoice, use <a href="{{ '/en/projects/fornu/manual/compras-y-gastos/' | relative_url }}#compras">stock purchases</a>.</p></div>

### Make a batch {#producir}

To log a batch of a prepared item: what was made goes into stock, and the items in its recipe come out, in proportion to the amount made.

1. Tap **Producir** on the prepared item's row.
2. Type the **Cantidad producida** (quantity made), in the item's unit.
3. Add a note if you like. Tap **Registrar producción** (log production).
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-producir.jpg' | relative_url }}" alt="The Producir panel for the house sauce with Cantidad producida at 3000 grams, which reads 3 kg below, and the optional note" loading="lazy" width="620" height="560">
  <figcaption>A 3 kg batch of sauce.</figcaption>
</figure>

If the item has no recipe or is switched off, Fornu does not log it and says why.

When something that uses a prepared item is sold but nobody logged that item as made, its row warns «Faltó registrar lo producido» and shows how much was used beyond what was made. **Registrar lo usado** opens **Producir** with that quantity already filled in.

In the kitchen, cooks log batches and waste from the tablet, with their PIN, without coming to this screen. That is covered in [In the kitchen and on the road]({{ '/en/projects/fornu/manual/cocina-y-reparto/' | relative_url }}#merma).

### Count one item {#conteo-uno}

1. Tap **⋯** › **Conteo** on the item's row.
2. Type what you counted in **Cantidad contada** (quantity counted). It starts at the system's figure, and underneath it says «El sistema espera …» (the system expects …).
3. Add a note if you like. Tap **Registrar**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-conteo-uno.jpg' | relative_url }}" alt="The Conteo panel for ground beef with Cantidad contada at 23500 grams and below it El sistema espera 24,1 kg" loading="lazy" width="620" height="560">
  <figcaption>Counting the ground beef: the system expected 24.1 kg.</figcaption>
</figure>

If your count matches, Fornu says there is nothing to adjust. If someone counted that item after you, their count stands.

### Log waste {#merma}

1. Tap **⋯** › **Merma**.
2. Type the **Cantidad perdida** (quantity lost) and the **Motivo** (reason), such as «se quemó» (burnt) or «se venció» (expired). The reason is required.
3. Tap **Registrar**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-merma.jpg' | relative_url }}" alt="The Merma panel for ground beef with 500 grams lost and the reason Se pasó de fecha" loading="lazy" width="620" height="560">
  <figcaption>Half a kilo of ground beef past its date.</figcaption>
</figure>

### See an item's history {#historial}

**⋯** › **Historial** shows every movement of the item: when, what it was (**Compra** purchase, **Ajuste por conteo** count adjustment, **Merma** waste, **Usado en producción** used in production, **Producción** production or **Pedido** order, with the price where there is one), the quantity added or taken out, who did it and the note. History is kept one item at a time.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-historial.jpg' | relative_url }}" alt="Ground beef's history: a purchase of 10 kg at 9,900 pesos, and below it what each order and table used, with who did it" loading="lazy" width="880" height="392">
  <figcaption>Ground beef's history: the purchase and what each sale used.</figcaption>
</figure>

### On a phone and on the shop's device {#stock-celular}

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/insumos-stock-telefono.jpg' | relative_url }}" alt="The Stock tab on the shop's phone, with the Contar stock button, the four figures and each item on a card with what is on hand, how long it lasts and its Producir or Entrada button." loading="lazy" width="390" height="844">
  <figcaption>The Stock tab on the shop's phone.</figcaption>
</figure>

On a phone, each item is a card with what is on hand, how long it lasts and its buttons. The minimum, daily use and value are hidden, and the list is sorted by tapping the figures at the top.

## Count the whole stock {#conteo}

A count sets stock to what is really there. It is worth doing at closing time, or once a week, walking round the kitchen with the phone or tablet in hand.

<p class="perm"><span>Who can:</span> <span class="tag">Stock</span></p>

<div class="shot-pair">
<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/insumos-conteo-telefono.jpg' | relative_url }}" alt="The stock count on a phone: sunflower oil with 7 ml counted and the difference in red, and Guardar conteo at the bottom." loading="lazy" width="390" height="844">
  <figcaption>On a phone, the count scrolls from top to bottom.</figcaption>
</figure>
<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-conteo.jpg' | relative_url }}" alt="The Conteo de stock panel with the Ver lo que dice el sistema box off, the categories to count one at a time, and each item with two boxes, whole packs plus loose quantity." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li><b>Ver lo que dice el sistema</b> (show what the system says): off at first, so you count without looking.</li>
    <li>The categories: tap one to count one at a time.</li>
    <li>Anything bought in packs has two boxes: whole packs plus what is loose.</li>
    <li>The difference from what the system expected, in green or red.</li>
    <li>How many you counted and how many came out different.</li>
    <li><b>Guardar conteo</b> (save count).</li>
  </ol>
  <figcaption>The same count on a computer.</figcaption>
</figure>
</div>

1. Tap **Contar stock**.
2. Count without looking at what the system says. For anything bought in packs, type the whole packs in the first box and what is loose in the second, such as 2 bags of 25 kg plus 3,500 g.
3. Leave empty whatever you did not count: it is not counted and does not change.
4. Add a note if you like, such as «Conteo de cierre» (closing count).
5. Tap **Guardar conteo**. If anything differs, Fornu asks «¿Ajustar N insumos a lo contado?» (adjust N items to the count?) and explains that stock becomes what you typed and the difference is kept in each item's history. Tap **Guardar conteo** again.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-ajustar.jpg' | relative_url }}" alt="The confirmation ¿Ajustar 4 insumos a lo contado?, explaining that the stock becomes what was typed and the difference stays in the history, with Volver and Guardar conteo" loading="lazy" width="500" height="220">
  <figcaption>Before saving, Fornu asks.</figcaption>
</figure>

Fornu confirms, for example, «Conteo guardado: 3 ajustes, 9 sin cambios» (3 adjusted, 9 unchanged). The list holds only active items, grouped by category, and can be filtered by group or searched. While a number cannot be read, the footer counts it and saving stays blocked.

Anything that moved after you counted an item, such as an order or a delivery, is added on top of your count. If someone else counted the same item after you, their count stands, and Fornu says so when saving.

<div class="callout tip"><p class="callout-title">Tip</p><p>The count is kept on the device as you type. If the phone locks or the tab closes, tapping <b>Contar stock</b> again shows «Hay un conteo sin guardar de las 18:40: 12 insumos contados.» (an unsaved count from 18:40, 12 items counted), with <b>Seguir ese conteo</b> (continue that count) or <b>Empezar de cero</b> (start over). A count more than two days old can no longer be saved: count again.</p></div>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-conteo-sin-guardar.jpg' | relative_url }}" alt="The stock count open with the notice Hay un conteo sin guardar de las 18:54: 4 insumos contados, and the Seguir ese conteo and Empezar de cero buttons" loading="lazy" width="880" height="320">
  <figcaption>A count that was left unsaved.</figcaption>
</figure>

## Plan production {#planificar}

For getting ready for a busy day or an event. You say what you want to make and how much, and Fornu works out which prepared items to make first, in batches, and what to buy, in whole packs, after taking off what is already in stock.

It lives in Insumos › **Planificar producción** (plan production). The tab reads **Planificar**.

<p class="perm"><span>Who can:</span> <span class="tag">Stock</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-planificar.jpg' | relative_url }}" alt="Planificar producción with 300 Doble cheddar, 120 large pizzas and 150 Tiras crocantes, a production cost of 1,913,166 pesos, 920,500 to buy, four prepared items to make first and what to buy from three suppliers, with a Cargar compra button for each" loading="lazy" width="1440" height="1640">
  <ol class="marks">
    <li><b>Qué producir</b> (what to make): each row is a menu product or a prepared item, with its quantity.</li>
    <li><b>+ Agregar</b> (add), <b>Vaciar la lista</b> (clear the list) and <b>Restar lo que hay en el stock</b> (subtract what is in stock).</li>
    <li>The figures: <b>Costo de la producción</b> (production cost), <b>Para comprar</b> (to buy) and <b>Para preparar antes</b> (to make first).</li>
    <li><b>Preparar antes</b>: each prepared item with what is needed, what is on hand, what to make, in how many batches and what it costs.</li>
    <li><b>Imprimir</b> (print) and <b>Registrar producción</b> (log production).</li>
    <li><b>Comprar</b> (buy): what is missing, by supplier, with its total and <b>Cargar compra</b> (load purchase).</li>
  </ol>
  <figcaption>A busy day: what to make first and what to buy from each supplier.</figcaption>
</figure>

1. Tap **+ Agregar** and pick what to make: a product from any business unit, or a prepared item.
2. Type the quantity: units for a product, the item's own unit for a prepared item.
3. Repeat for the rest. The plan recalculates by itself.
{: .steps}

- When prepared items are below their minimum, a line «Debajo del mínimo: …» (below minimum) appears with **Sumar al plan** (add to plan). It adds each one in whole batches, enough to reach the minimum and cover one more day of use.
- **Restar lo que hay en el stock** starts on. Switch it off to work everything out as if nothing were in stock.
- A product with no recipe adds nothing, and the plan says so: «Sin receta, … no suma nada al plan: cargala para que cuente.»
- The list stays saved in this browser until you tap **Vaciar la lista**.

### Print the kitchen sheet {#imprimir}

**Imprimir** opens the browser's print dialog with a clean sheet: the title Producción, the kitchen and the date, what to make, what to make first with its batches and what to buy with its packs. Each line has a box to tick by hand, and the footer shows the production cost and what needs buying.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-hoja-produccion.jpg' | relative_url }}" alt="The printed Producción sheet: the kitchen and the date, Qué producir, Preparar antes with its batches and Comprar with its packs, each line with a box, and at the foot the cost and what to buy" loading="lazy" width="1440" height="790">
  <figcaption>The kitchen sheet, to tick by hand.</figcaption>
</figure>

### Log the production {#registrar-produccion}

**Registrar producción** asks you to confirm, with a summary such as «Entran al stock 2 kg de Salsa, … y salen los insumos que llevan.» (2 kg of sauce come into stock, and the items they use go out), and logs only the prepared items that are missing. Purchases are not logged from here. The button is disabled when there is nothing to make, or when a prepared item in the plan has no recipe.

### Load the purchase for what is missing {#compra-del-plan}

Under **Comprar**, each supplier has its total and a **Cargar compra** (load purchase) button. It opens a stock purchase already filled in: that supplier, the Insumos category, a **Remito** (delivery note) voucher, the description «Lo que falta para el plan de producción», each item in whole packs at today's price, and paid in cash today. Check it and save it like any purchase, as explained in [Purchases and expenses]({{ '/en/projects/fornu/manual/compras-y-gastos/' | relative_url }}#cargar-compra). Items without a supplier come last, under «Sin proveedor».

<div class="callout"><p class="callout-title">Good to know</p><p>Saving the purchase takes the <b>Gastos</b> permission. And since it starts as paid in cash, switch it to <b>A pagar</b> (to pay) before saving if you will pay later.</p></div>

## Import from a spreadsheet {#importar}

Ingredients, supplies and the recipes of prepared items can also be loaded from a spreadsheet, with **Importar planilla** on each tab. In Ingredientes and Inventario it opens on **Insumos**, and in Producción on **Recetas** (recipes). Prepared items are created by hand, and the spreadsheet fills in their recipes. The steps and the columns are in [Menu › Import from a spreadsheet]({{ '/en/projects/fornu/manual/carta/' | relative_url }}#importar).
