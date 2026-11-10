---
layout: manual
manual: carta
title: "Menu · Fornu manual"
description: "How to set up each business unit's products with their price on every channel, their recipe, extras and modifier groups, how to change many prices at once and how to import it all from a spreadsheet."
permalink: /en/projects/fornu/manual/carta/
---

## Products {#productos}

This is each business unit's menu: what it sells, what it charges on each channel, what each item costs to make and what it leaves. You add new products here, change prices and build the recipe that takes stock out with every sale.

It lives in Carta › **Productos** (menu › products). Along the top there is a colored tab for each business unit: tap one and the list shows only its menu.

<p class="perm"><span>Who can:</span> <span class="tag">Carta</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-productos.jpg' | relative_url }}" alt="Doble Smash's product list, grouped into Burgers and sides, with each product's base price, Rappi price, PedidosYa price, cost, margin in pesos and margin as a percentage." loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li><b>Doble Smash · Pollo Crocante · Bowl Verde · Pizzería</b>: one tab per business unit, each with its own menu.</li>
    <li><b>Importar planilla</b> (import spreadsheet), <b>Actualizar precios</b> (update prices) and <b>Nuevo producto</b> (new product): load many at once, raise the prices of the whole menu or one category, or add one by hand.</li>
    <li>A platform notice. It shows when the menu changed after it was published to that store, or when it was never published from Fornu. <b>Publicar en Rappi</b> (publish to Rappi) sends today's menu.</li>
    <li><b>Precio base</b> (base price) and each platform's price. Tap one to change it without opening the product.</li>
    <li><b>Costo</b> (cost), <b>Margen $</b> and <b>Margen %</b> (margin): what the recipe costs and what one unit leaves on the channel that leaves least.</li>
    <li>The <b>⋯</b> menu: recipe, extras, modifier groups, duplicate and pause.</li>
  </ol>
  <figcaption>Doble Smash's menu in the demo, with what each product leaves.</figcaption>
</figure>

The list is grouped by category. Under each name, in grey, it says how many stock items the recipe has, how many extras and which modifier groups the product carries, such as «5 insumos · Extras · Sumale una bebida». The **Solo como opción** (option only) tag marks products that are not sold on their own. Paused products are dimmed.

| Column | What it shows |
|---|---|
| **Producto** | The name and, underneath, the recipe, extras and groups. |
| **Precio base** | What own delivery orders pay, and what any platform without its own price charges. |
| **Rappi**, **PedidosYa** | One column per platform switched on for the business unit. The price is grey when the product has no price of its own there and uses the base price. |
| **Costo** | What one unit's recipe costs, to the cent. «Sin receta» (no recipe) if it has none yet. |
| **Margen $** | What one unit leaves on the channel that leaves least, after that channel's commission and the extras. A dash if the recipe or the price is missing. |
| **Margen %** | The same margin as a percentage, with the channel's name underneath. Red if it loses money, amber if the price is below the suggested one. Hover to see why. |

The search box finds products by name or category. With the Costs and margins module, tapping **Margen %** opens the product's cost sheet with each channel broken down, covered in [Costs and reports]({{ '/en/projects/fornu/manual/costos-y-reportes/' | relative_url }}#ficha). That takes the **Costos** permission.

### Change a price in the list {#precio-en-lista}

1. Tap the price you want to change, under **Precio base** or a platform's column. It turns into a field.
2. Type the new price.
3. Press <kbd>Enter</kbd> or tap outside it. To leave it as it was, press <kbd>Esc</kbd>.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-precio-en-lista.jpg' | relative_url }}" alt="The Doble cheddar row with its base price just changed to 9,900 pesos and, at the bottom left, the confirmation «Doble cheddar: $ 9.900»." loading="lazy" width="1440" height="450">
  <ol class="marks">
    <li>The price just changed, right there in the list.</li>
    <li>«Doble cheddar: $ 9.900»: Fornu's confirmation.</li>
  </ol>
  <figcaption>A price changed without opening the product.</figcaption>
</figure>

A price is saved only if it is above zero and different from the old one. Typing a price in a platform's column gives the product its own price on that platform from then on. Until then it used the base price.

### Add a new product {#nuevo-producto}

1. Tap **Nuevo producto**.
2. Type the **Nombre** (name) and pick the **Categoría** (category). If it does not exist yet, tap **+ Categoría nueva** (new category), type its name and tap **Crear** (create).
3. Type the **Precio base**: it is the price for own orders and for every platform without a price of its own.
4. Tap **Guardar** (save), or press <kbd>Ctrl</kbd> + <kbd>Enter</kbd>.
5. The product opens again on **Receta** (recipe), with the note «Doble cheddar ya está en la carta. Falta su receta: sin ella no hay costo, márgenes ni descuento de stock.» (it is on the menu, but without a recipe there is no cost, no margins and no stock deduction). Add the stock items and save again.
{: .steps}

<div class="callout tip"><p class="callout-title">Tip</p><p>If the business unit has only one category, it comes already picked. If it has none, the product opens straight on the field to create one.</p></div>

## Inside a product {#ficha}

Everything about a product sits in one panel, split into tabs. Tap its row to open it on **Datos** (details), or use the **⋯** menu to open it straight on **Receta**, **Adicionales** (extras) or **Grupos modificadores** (modifier groups). On a computer it opens on the right with the list still in view. On a phone it slides up from the bottom.

<p class="perm"><span>Who can:</span> <span class="tag">Carta</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-ficha.jpg' | relative_url }}" alt="The Doble cheddar panel on the Datos tab, with the Precios, Receta, Adicionales and Grupos modificadores tabs along the top and, at the bottom, a cost of 3,177.35 pesos and each channel's margin." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li>The tabs. The number is how many lines the recipe has, or how many groups the product carries. A tab with a problem gets a mark.</li>
    <li><b>Código</b> (code): a short code to type at the till instead of the name.</li>
    <li><b>Se vende suelto</b> (sold on its own): switch it off for things that are only ordered inside another product.</li>
    <li>The footer: the cost and each channel's margin. They follow what you type, on any tab.</li>
  </ol>
  <figcaption>The demo's Doble cheddar, on the Datos tab.</figcaption>
</figure>

The footer keeps up with everything you type. Once there is a recipe it shows the **Costo** and the margin for **Propios** (own orders), each platform and **Salón** (dining room) if the unit sells there, in red when a channel loses money and amber when it sits below the suggested price. With no recipe it reads «Sin receta todavía: sin costo ni márgenes.» If something blocks saving, the footer says what, with a link to the tab where it is.

### Datos {#ficha-datos}

| Field | What it is for |
|---|---|
| **Nombre** | Required. |
| **Código** | Up to 10 letters and digits, in capitals, such as 12 or PIZ3. Used to key the product in at the till. It cannot repeat within the business unit. |
| **Categoría** | The menu section. **+ Categoría nueva** creates one without leaving the product. |
| **Precio base** | Only shown when adding a new product. After that, prices are changed on **Precios** (prices) or in the list. |
| **Descripción (opcional)** | A short description. |
| **Orden** (order) | Where it appears. Lower numbers come first. |
| **Activo** (active) | Off, the product is paused. |
| **Se vende suelto** | Off, the product is only offered inside its modifier groups, like extra cheddar. It does not show on its own on the platforms or in own orders, and it has no extras. |

### Precios {#ficha-precios}

- **Precio base**: the price for own orders. If it is 0 and the product is sold on its own, it warns «Se vendería gratis.» (it would be sold for free).
- **Precio en Rappi** and **Precio en PedidosYa**: with **Propio** (own) off, the platform charges the base price, shown in grey. Switch it on and type that platform's price, which starts at the base price.
- **Ganancia sobre el costo** (markup on cost): how much the suggested price leaves above what the product costs. With **Propia** off it uses the account's markup, set in [Ajustes › Configuración]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#configuracion). Switch it on to set one for this product only.
- **Márgenes con estos precios** (margins at these prices): a table with each channel, its price, what it leaves in pesos and as a percentage, and the **Sugerido** (suggested) price. When a price is below the suggested one, a **Usar $ …** (use) button replaces it with the suggestion rounded up to $ 10. Without a recipe there is no cost, and the table asks you to add one.

### Receta {#ficha-receta}

The stock items each unit sold uses, and how much of each. Every time the product sells, Fornu takes what the recipe says out of stock.

1. Tap **+ Agregar** (add).
2. Pick the stock item. The list groups them by category: ingredients first, then prepared items, then supplies.
3. Type the quantity, in the item's unit: grams, millilitres or units. The line's cost shows next to it.
{: .steps}

The whole recipe's cost shows at the bottom. The ✕ removes a line. If a stock item does not exist yet, **+ Nuevo insumo** (new stock item) opens its form without leaving the product: you choose whether it is an ingredient, a prepared item or a supply, and once saved it joins the recipe with a quantity of 1. That button shows when your role also has the **Insumos** permission.

<div class="callout tip"><p class="callout-title">Tip</p><p>The product's box or bag goes in <b>Adicionales</b>, not in the recipe. That way the packaging can differ between delivery and the dining room.</p></div>

### Adicionales {#ficha-adicionales}

What each unit of the product carries besides its recipe, on every channel or on one: its box, a sauce sachet for delivery. It comes out of stock with every unit sold and counts in the margins.

Each line has a **Canal** (channel: **Todos** for all, **Propios**, each platform that is on, and **Salón** if the unit sells in the dining room), an **Insumo** (stock item), a **Cantidad** (quantity) and its **Costo**. **+ Adicional** adds a line. Anything every product of the business unit carries, or that goes once per order, is set up once in the business unit's own extras, in [Settings]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#unidades).

This tab shows while **Se vende suelto** is on.

### Grupos modificadores {#ficha-grupos}

Tick the groups offered when this product is ordered, such as its extras or the drink in a combo. Each card says how many options are chosen, for example «Opcional, hasta 3» (optional, up to 3). A group that has this same product among its options is greyed out. Groups are built in [Modifier groups](#modificadores).

### What blocks saving {#ficha-errores}

**Guardar** stays disabled while something is missing, and the footer says what:

- «Falta el nombre.» (the name is missing)
- «Elegí la categoría.» (pick the category)
- «Falta el precio: se vendería a $ 0.» (no price, it would sell at $ 0), when the product is active and sold on its own.
- «Elegí el insumo de cada línea de la receta.» or «Hay una línea de la receta sin cantidad.» (a recipe line has no item, or no quantity)
- «Hay un adicional sin cantidad.» or «Hay un adicional repetido.» (an extra has no quantity, or appears twice)

## Duplicate, pause and reactivate {#pausar}

All of these are in each product's **⋯** menu.

<p class="perm"><span>Who can:</span> <span class="tag">Carta</span></p>

- **Duplicar** (duplicate) creates «Doble cheddar (copia)» with the same recipe, extras, prices, markup and groups. The copy starts paused, so you can check it before selling it, and opens on **Datos** so you can rename it.
- **Pausar** (pause) takes the product off sale. Fornu says «Doble cheddar pausado. Publicá la carta para que las plataformas lo vean.» (paused, publish the menu so the platforms see it) and offers **Deshacer** (undo) in case it was a slip.
- **Reactivar** (reactivate) puts it back on the menu: «Doble cheddar vuelve a la carta».

Products are never deleted. Pausing takes them off sale and keeps their sales and their history.

<div class="callout"><p class="callout-title">Good to know</p><p>A new price or a paused product reaches a platform when the menu is published to that store. If something is still unpublished, the notice above the list says so and carries the publish button.</p></div>

## Change many prices at once {#precios}

When everything goes up, there is no need to go product by product. **Actualizar precios** raises or lowers the whole menu, or one category, by a percentage. **Cambiar precios** (change prices) changes only the products you tick, by a percentage or an amount, on the channel you choose.

<p class="perm"><span>Who can:</span> <span class="tag">Carta</span></p>

### Update the prices of the whole menu or one category {#actualizar-precios}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-actualizar-precios.jpg' | relative_url }}" alt="The Actualizar precios panel set to the whole menu, 10 percent and rounding to 50 pesos, with both boxes ticked and a preview of seven products with their current price and the new one." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li><b>Qué productos</b> (which products): <b>Toda la carta</b> (whole menu) or one category.</li>
    <li><b>Cuánto (%)</b> (how much): 10 raises prices by 10%. A negative number lowers them: -5 takes 5% off.</li>
    <li><b>Redondeo</b> (rounding): none, or to $ 1, $ 10, $ 50, $ 100, $ 500 or $ 1,000. It starts at $ 50.</li>
    <li>The two boxes: also change each platform's own price, and the product's price inside modifier groups.</li>
    <li>The preview: where each base price ends up. It shows the first eight and counts the rest.</li>
    <li><b>Actualizar 7 productos</b>: applies the change.</li>
  </ol>
  <figcaption>A 10% rise across Doble Smash's whole menu.</figcaption>
</figure>

1. Tap **Actualizar precios**.
2. Choose the products, the percentage and the rounding. The percentage goes from -90% to 500%.
3. Check the preview and tap **Actualizar N productos**.
{: .steps}

For a big change, 30% or more up or 20% or more down, Fornu asks first, for example «¿Subir un 30% el precio de 12 productos?» (raise 12 products by 30%?), and you confirm with **Subir 30%**. When it is done it says how many products and options changed and reminds you to publish the menu so the platforms see the new prices. A price of 0 stays at 0.

### Change the price of the ticked products {#cambiar-precios}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-cambiar-precios.jpg' | relative_url }}" alt="Two products ticked in the list and, on the right, the panel to change the price of 2 products, set to a percentage of 10, rounding to 10 pesos and all prices, with a table of each product's before and after on each channel." loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li>The selection bar: how many products are ticked, <b>Cambiar precios</b> and <b>Quitar la selección</b> (clear selection).</li>
    <li><b>Cómo</b> (how): <b>Porcentaje</b> (percentage) or <b>Monto</b> (amount).</li>
    <li><b>Cuánto</b>: 12 raises by 12% and -5 lowers by 5%. As an amount, 500 adds $ 500 to each price and -200 takes $ 200 off.</li>
    <li><b>En qué canal</b> (which channel): <b>Todos los precios</b> (all prices), only <b>Pedidos propios</b> (own orders), or one platform.</li>
    <li>The preview, price by price and channel by channel. Prices that do not change are dimmed.</li>
    <li><b>Aplicar</b> (apply): saves the new prices.</li>
  </ol>
  <figcaption>Two burgers up 10% on all their channels.</figcaption>
</figure>

1. Tick the products in the list. The box in the header ticks every product currently shown.
2. Tap **Cambiar precios** in the bar that appears above the list.
3. Choose how, how much, the rounding (to the cent, or to $ 1, $ 10, $ 50 or $ 100) and the channel. Wait for the preview.
4. Tap **Aplicar**. Fornu confirms «Precios cambiados» (prices changed).
{: .steps}

On own orders it changes the base price. On a platform it changes that platform's own price, and a product that had no own price there gets one.

### Fix a price that loses money {#arreglar-precio}

When a product loses money or sits below the suggested price on some channel, Fornu flags it in [Costos › Para revisar]({{ '/en/projects/fornu/manual/costos-y-reportes/' | relative_url }}#revisar) (costs › to review), and also in the box that shows after a purchase that moved costs ([Purchases and expenses]({{ '/en/projects/fornu/manual/compras-y-gastos/' | relative_url }}#margenes)). From either place, **Revisar precio** (review price) opens the product on **Precios**, ready to fix:

- A banner at the top says what is wrong, for example «Pierde $ … por unidad en Rappi · $ … debajo del sugerido en Pedidos propios» (loses $ … per unit on Rappi, $ … below the suggestion on own orders).
- In the margins table you type each channel's price right there, and the margin updates as you type.
- Once everything is fine, the banner turns into «Con estos precios ningún canal pierde plata ni queda debajo del sugerido. Guardá para dejarlo así.» (no channel loses money or sits below the suggestion, save to keep it).
- Closing takes you back to where you came from.

## Menu categories {#categorias}

These are the sections of each business unit's menu, such as Burgers or Drinks. They are in a second list below the products, on the same screen. They can also be created from a new product, with **+ Categoría nueva**.

<p class="perm"><span>Who can:</span> <span class="tag">Carta</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-categorias.jpg' | relative_url }}" alt="The Categorías list with Burgers, sides and Extras, which course each one is, how many products it holds and its order, plus the Agregar button." loading="lazy" width="1384" height="276">
  <ol class="marks">
    <li><b>Agregar</b> (add): a new category.</li>
    <li><b>Va de</b> (course): when that category goes out in the dining room.</li>
    <li><b>Orden</b>: where it appears on the menu.</li>
  </ol>
  <figcaption>Doble Smash's three categories in the demo.</figcaption>
</figure>

Tap **Agregar**, or a category to change it:

| Field | What it is for |
|---|---|
| **Nombre** | The section title. |
| **Orden** | The section's position. A new one goes last. |
| **Va de** | **Principal** (main), **Ya** (right away), **Entrada** (starter) or **Postre** (dessert). In the dining room it sets when this category goes out: drinks right away, desserts at the end. What comes later waits in the kitchen until the waiter fires it. Outside the dining room it changes nothing. |
| **Notas rápidas** (quick notes) | One per line, such as «Jugoso», «A punto» and «Cocido» (rare, medium, well done). When ordering a product of this category, you tap them instead of typing. Up to 12 notes of 40 characters. |
| **Color** | The color of its tile and its products on the express counter. If none is picked, it uses the business unit's color. |

How courses are fired and where quick notes show up is covered in [Dining room]({{ '/en/projects/fornu/manual/salon/' | relative_url }}#tiempos).

To delete a category, open it and tap **Borrar** (delete). If it still has products, Fornu keeps it and asks you to move them to another category or pause them first.

## Modifier groups {#modificadores}

These are the choices made when ordering: a burger's «Extras» or «Elegí tu bebida» (pick your drink) in a combo. Each group is built from products on the menu, each with what it adds to the price inside the group and how many units fit.

They are in Carta › **Grupos modificadores** (the tab reads **Modificadores**), with the same business unit tabs as the products.

<p class="perm"><span>Who can:</span> <span class="tag">Carta</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-modificadores.jpg' | relative_url }}" alt="Doble Smash's modifier groups: Extras, optional up to 3, with cheddar, bacon and caramelized onion, and Sumale una bebida, optional up to 1, with the soda. Both are used by the Doble cheddar and the Triple bacon." loading="lazy" width="1440" height="450">
  <ol class="marks">
    <li><b>Nuevo grupo</b> (new group).</li>
    <li><b>Se eligen</b> (chosen): the group's rule. «Opcional, hasta 3» allows from none up to three options.</li>
    <li><b>Productos</b>: the options, with what each one adds («+$ 1.500», or «sin cargo» for free) and how many of each fit («hasta 2», up to 2).</li>
    <li><b>Lo llevan</b> (used by): the products that offer this group.</li>
  </ol>
  <figcaption>Doble Smash's two groups in the demo.</figcaption>
</figure>

### Build a group {#armar-grupo}

1. Tap **Nuevo grupo**.
2. Type the **Nombre**, such as «Extras».
3. Set **Mínimo a elegir** and **Máximo a elegir** (minimum and maximum to choose). The resulting rule reads underneath: «Opcional, hasta 3», «Elegir 1» (choose 1) or «De 1 a 2» (1 to 2).
4. Tap **+ Agregar producto** (add product) for each option, and adjust **Hasta** (up to) and **Precio** (price).
5. Tap **Guardar**.
6. Open each product that carries the group and tick it on its **Grupos modificadores** tab.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-grupo.jpg' | relative_url }}" alt="The Extras group panel with a minimum of 0 and a maximum of 3, and three products: cheddar and bacon up to 2, caramelized onion up to 1, each with its price and cost." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li><b>Mínimo a elegir</b> and <b>Máximo a elegir</b>. A minimum of 0 makes the group optional. They count units: two of the same are two.</li>
    <li><b>Producto</b>: each option is a product on the menu. Those not sold on their own read «(solo como opción)».</li>
    <li><b>Hasta</b> and <b>Precio</b>: how many units of that option fit, from 1 to 20, and what each one adds. The price starts at the product's own price and can be changed. At 0 it is free.</li>
    <li><b>+ Agregar producto</b>: adds an option. It suggests products sold only as options first.</li>
    <li><b>Borrar</b>: the group stops being offered on the products that carried it.</li>
  </ol>
  <figcaption>The demo's Extras group, open for editing.</figcaption>
</figure>

The minimum cannot be higher than the maximum, and the maximum is at least 1. If the business unit has no products yet, the group asks you to add them in Productos first.

<div class="callout tip"><p class="callout-title">Tip</p><p>Set up an extra like cheddar in Productos first, with <b>Se vende suelto</b> off. It then never shows on its own on any menu, and it has its own recipe: when someone picks it, Fornu takes what it uses out of stock.</p></div>

A product that carries a group cannot be one of that group's options.

## Import from a spreadsheet {#importar}

To add or change many products, stock items or recipes at once from Excel or Google Sheets. Before saving, Fornu shows what will happen to every row, and nothing is saved until you confirm.

| From | Opens on | Permission |
|---|---|---|
| Carta › Productos › **Importar planilla** | **Carta** (menu), with a **Recetas** (recipes) tab next to it | Carta |
| Insumos › Ingredientes or Inventario › **Importar planilla** | **Insumos** (stock items), with a **Recetas** tab next to it | Insumos |
| Insumos › Producción › **Importar planilla** | **Recetas** | Insumos |
| Inicio (home), in the first steps: «Importarla de una planilla» or «Importarlos de una planilla» | The menu or the ingredients | Carta or Insumos |

Product recipes take the **Carta** permission, and prepared items' recipes take **Insumos**.

<p class="perm"><span>Who can:</span> <span class="tag">Carta</span> <span class="tag">Insumos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-importar.jpg' | relative_url }}" alt="The Importar desde una planilla panel on the Insumos tab, with the Descargar la planilla and Elegir archivo buttons, the box to paste rows into and an explanation of each column." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li>The tabs: which spreadsheet you are loading.</li>
    <li><b>Descargar la planilla</b> (download the spreadsheet) and <b>Elegir archivo</b> (choose file).</li>
    <li><b>O pegá las filas</b> (or paste the rows): copy the rows from the spreadsheet, headings included, and paste them here.</li>
    <li><b>Las columnas</b> (the columns): which ones Fornu understands and what an empty cell means.</li>
    <li><b>Revisar</b> (check): builds the preview. Pasting several rows shows it straight away.</li>
  </ol>
  <figcaption>Importing stock items, before loading the spreadsheet.</figcaption>
</figure>

1. Tap **Descargar la planilla**. It downloads a file with what you already have, or with example rows if you have nothing yet.
2. Open it in Excel or Google Sheets. Change what you need and add rows.
3. Back in Fornu, tap **Elegir archivo**. Or select the rows with their headings in the spreadsheet, copy them with <kbd>Ctrl</kbd> + <kbd>C</kbd> and paste them into **O pegá las filas** with <kbd>Ctrl</kbd> + <kbd>V</kbd>.
4. Read the preview. Tap a counter to see only those rows.
5. Tap **Importar N filas** (import N rows), or press <kbd>Ctrl</kbd> + <kbd>Enter</kbd>.
{: .steps}

Fornu reports how many rows were added and how many were updated, and the list reloads.

It reads .xlsx files (the first sheet), .csv, .tsv and .txt, up to 4 MB, and up to 3,000 rows at a time. An old Excel file (.xls) cannot be read: save it as .xlsx, or copy the rows and paste them.

The first row names the columns. Their order does not matter, and columns Fornu does not know are ignored. The preview lists the ones left out. Headings do not need to be exact: «rubro», «costo», «pvp», «presentación» or «alícuota» work too. If the price column is titled «con IVA» or «sin IVA» (with or without VAT), that applies to the whole column.

### The menu spreadsheet {#planilla-carta}

| Column | What goes in it |
|---|---|
| **Unidad de negocio** | The business unit. Needed when the account has more than one. |
| **Categoría** | Created if it does not exist. |
| **Producto** | Updated if it already exists in that business unit. |
| **Descripción** | The product's description. |
| **Precio** | The base price. |

### The stock items spreadsheet {#planilla-insumos}

For ingredients and supplies. Prepared items are created in Producción, and their recipe goes in the recipes spreadsheet.

| Column | What goes in it |
|---|---|
| **Nombre** | Updated if it already exists. An empty cell leaves that value as it is. |
| **Categoría** | Created under Ingredientes if it does not exist. |
| **Unidad** | kg, g, l, ml or unidad (unit). **Cuánto trae** and the minimum use this unit. |
| **Se compra por** | How it is bought: bolsa, caja, maple (bag, box, egg tray)… Empty means by the kg, l or unit. |
| **Cuánto trae** | How much each one holds. Empty means 1. |
| **Precio** | Per pack, as shown on the invoice or receipt. |
| **IVA** | VAT: 21, 10.5, 27… Empty means 21. |
| **El precio es** | «con IVA» or «sin IVA». |
| **Stock mínimo** | The minimum stock. Below it, Fornu warns. |

### The recipes spreadsheet {#planilla-recetas}

| Column | What goes in it |
|---|---|
| **Unidad de negocio** | Only when products with the same name exist in more than one business unit. |
| **Producto o elaboración** | Whose recipe it is. One row per stock item it uses, and the rows replace its old recipe. |
| **Insumo** | The stock item. It must already exist. |
| **Cantidad** | Per unit sold, or per batch for a prepared item. |
| **Unidad** | Empty means the stock item's own unit. |

<div class="callout"><p class="callout-title">Good to know</p><p>In the recipes spreadsheet, one row with an error leaves that whole recipe out, so it is never saved half done. Fix the row and load the file again.</p></div>

### Read the preview {#vista-previa}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-importar-revisar.jpg' | relative_url }}" alt="The preview of a recipes spreadsheet: the Doble cheddar recipe changes and one row fails because the product does not exist. At the bottom, the Importar 1 fila button." loading="lazy" width="880" height="494">
  <ol class="marks">
    <li>The counters: <b>nuevos</b> (new), <b>cambian</b> (changed), <b>sin cambios</b> (unchanged) and <b>con error</b> (with errors). Tap one to see only those rows.</li>
    <li><b>Qué pasa</b> (what happens) to each row: <b>Nuevo</b>, <b>Cambia</b>, <b>Igual</b> or <b>Error</b>.</li>
    <li><b>Detalle</b> (detail): what will be saved, or why the row is left out.</li>
    <li>Rows with errors are left out: fix them in the spreadsheet and load it again.</li>
    <li><b>Importar 1 fila</b>: saves the rows that are fine.</li>
  </ol>
  <figcaption>A recipe that changes and a row with an error.</figcaption>
</figure>

The top also lists which categories will be created. Some reasons that can show under **Detalle**:

| Message | What to do |
|---|---|
| «Falta la unidad: kg, g, l, ml o unidad.» | Fill in the **Unidad** column. |
| «No hay un insumo llamado …» | Add that stock item first, or fix the name. |
| «Ya está en la fila 4: va una sola vez.» | Keep one row per name. |
| «Falta la unidad de negocio: hay 2, …» | Add the **Unidad de negocio** column. |
| «Está en g: la unidad no se cambia…» | A stock item's unit is fixed. Use the one it has. |
| «Es una elaboración: su receta va en la planilla de recetas, y lo demás en su ficha.» | Prepared items are changed in Producción. |
| «Ya está así.» | The row changes nothing. |
| «Ojo: pasa de $ … a $ …» | The price changes a lot, more than three times up or down. Check it is the price per pack. |
