---
layout: manual
manual: espacios
title: "Spaces: the floor plan · Fornu manual"
description: "The space builder: drawing the dining room with walls, floors, openings and objects, the Basic, Cenital and Isométrica views, your own places, objects and textures, tracing, printing and exporting, and how waiters use the plan."
permalink: /en/projects/fornu/manual/espacios/
---

## What it is for {#para-que}

With Salón (the dining room module), each section has a plan where you arrange the tables. The Constructor de espacios (space builder) turns that sketch into the real place: walls, floors, doors and windows, columns, a bar, plants, umbrellas and whatever else is there, with their materials, seen from above or in an isometric view. You put it together like a building game, and the waiters then serve on that same plan.

The Constructor de espacios is a module that adds to Salón. If your account does not have it, each section's plan works as described in [Sections and tables]({{ '/en/projects/fornu/manual/salon/' | relative_url }}#armar), and the bar does not show the **Espacios** (spaces) group.

| Where | What for | Who can |
|---|---|---|
| **Salón › Sectores y mesas** (sections and tables) | Draw each section's plan and place its tables. | Armar el salón |
| **Espacios › Lugares** (places) | Saved places, to build other plans on top of them. | Biblioteca |
| **Espacios › Objetos propios** (your own objects) | Objects built from pieces, added to the catalog. | Biblioteca |
| **Espacios › Texturas propias** (your own textures) | Photos of floors, walls or logos, added to the materials. | Biblioteca |

The **Biblioteca** (library) permission («Guarda lugares, objetos y texturas propios, y arma espacios a partir de ellos.», saves your own places, objects and textures and builds spaces from them) is never lent with a PIN. Administración (the admin) can do everything.

## With Salón alone and with the builder {#dos-planos}

The same editor changes with what the account has:

| | With Salón alone | With the Constructor de espacios |
|---|---|---|
| A new section starts as | a 10 × 8 m floor | an empty 20 × 15 m grid: nothing comes ready-made |
| Tools | **Elegir y mover** (select and move), undo, redo and **Grilla** (grid) | all of them: rooms, walls, floor, paint, eyedropper and sledgehammer |
| Catalog | unplaced tables and the table models | also doors, windows, seating, structure, service, decor, outdoor, events and your own objects |
| Views | **Basic**, a top-down sketch | **Basic**, **Cenital** (overhead) and **Isométrica** (isometric), with textures |
| Measurements | the section's width and depth | also each room's area in m² and each wall's length |
| Extras | | **Lugares**, **Calcar un plano** (trace a plan), **Imagen** (image), **Imprimir** (print) and **Vaciar el plano** (clear the plan) |

With Salón alone, tapping anything that is not a table says «Acá solo se acomodan las mesas.» (only tables are arranged here).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-croquis.jpg' | relative_url }}" alt="A section's plan with Salón alone: a plain floor with nine placed tables, El espacio on the right with Ancho 10 and Fondo 8 and the help text Arrastrá al plano una mesa del catálogo, and at the bottom the size 10,00 m × 8,00 m and the Descartar and Guardar el plano buttons." loading="lazy" width="1340" height="710">
  <ol class="marks">
    <li><b>El espacio</b> (the space): the section's <b>Ancho (m)</b> (width) and <b>Fondo (m)</b> (depth), when nothing is selected.</li>
    <li>The editor's help text.</li>
    <li>The plan's size. If something is wrong, the first error shows here.</li>
    <li><b>Descartar</b> (discard) and <b>Guardar el plano</b> (save the plan).</li>
  </ol>
  <figcaption>With Salón alone, the plan is a sketch for arranging tables.</figcaption>
</figure>

If the account ever stops having the builder, plans keep their walls and floors, but only tables can be arranged and the view goes back to Basic.

## The editor {#editor}

It opens in Salón › Sectores y mesas, below the section tabs, and also in Espacios › Lugares. Use it from a computer or a tablet: on a phone, Sectores y mesas shows the tables as a list and says «El plano se arma desde una computadora o una tablet.» (the plan is built from a computer or a tablet).

<p class="perm"><span>Who can:</span> <span class="tag">Armar el salón</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-editor.jpg' | relative_url }}" alt="The editor with the builder: at the top the tools Elegir y mover, Habitación, Pared, Piso, Pintura, Cuentagotas and Mazo, undo, redo and Grilla. Below, Lugares, Calcar un plano, Imagen and Imprimir. On the plan, the Basic view, an L-shaped room of 18.1 m², a closed room of 74.4 m² with a door selected on its wall, and a new table. On the right, the catalog with Puertas y ventanas and Mesas." loading="lazy" width="1340" height="790">
  <ol class="marks">
    <li>The tools: <b>Elegir y mover</b>, <b>Habitación</b> (room), <b>Pared</b> (wall), <b>Piso</b> (floor), <b>Pintura</b> (paint), <b>Cuentagotas</b> (eyedropper) and <b>Mazo</b> (sledgehammer).</li>
    <li>Undo, redo and <b>Grilla</b> (each cell is 25 cm).</li>
    <li><b>Lugares</b>, <b>Calcar un plano</b>, <b>Imagen</b> and <b>Imprimir</b>.</li>
    <li>The view: <b>Basic</b>, <b>Cenital</b> or <b>Isométrica</b>.</li>
    <li>A selected door, with its bar: flip which way it opens, and remove it.</li>
    <li><b>Agregar</b> (add, the catalog) and <b>Editar</b> (edit, the selection).</li>
  </ol>
  <figcaption>The full editor, with two rooms and a door.</figcaption>
</figure>

In one corner of the plan are **Acercar** (zoom in), **Alejar** (zoom out) and **Ver todo** (fit all). Below it, a line shows the tool's name or what is happening while you draw: a length («3,50 m»), an area («12,5 m²») or why something does not fit. On the right, **Agregar** shows the catalog and **Editar** what you selected: selecting something by hand switches to Editar, and placing something from the catalog stays on Agregar so you can keep going. At the bottom are the plan's size («20,00 m × 15,00 m»), **Descartar** and **Guardar el plano**, which says «Plano guardado.» (plan saved).

### The views {#vistas}

| View | What it looks like |
|---|---|
| **Basic** | A flat sketch, from above. The only view with Salón alone. |
| **Cenital** | From above, with materials and textures. |
| **Isométrica** | In three dimensions, at an angle. |

Outside Basic, a **Texturas** (textures) checkbox shows materials with their pattern or as plain colors. The isometric view adds how walls are drawn, **Paredes altas** (full walls), **Paredes recortadas** (cut-away walls, the default) or **Paredes bajas** (low walls), and the ↺ ↻ buttons that turn the view a quarter at a time. The choice is saved on that device and applies to every plan, the live dining room included.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-vistas.jpg' | relative_url }}" alt="A dining room in the Isométrica view, with Texturas ticked and Paredes recortadas: brick walls, a light floor, three tables for four with their chairs, a dark bar and the label 193,8 m² on the floor." loading="lazy" width="1040" height="680">
  <ol class="marks">
    <li><b>Basic</b>, <b>Cenital</b> or <b>Isométrica</b>.</li>
    <li><b>Texturas</b>: materials with their pattern.</li>
    <li>How walls are drawn: full, cut away or low.</li>
    <li>↺ ↻: turn the view.</li>
    <li>The room's area.</li>
  </ol>
  <figcaption>The demo's dining room in isometric view.</figcaption>
</figure>

### The tools {#herramientas}

| Tool | What it does |
|---|---|
| **Elegir y mover** | Tap something to select it, and <kbd>Shift</kbd> adds to or removes from the selection. Drag to move it: it snaps to the grid, and with <kbd>Alt</kbd> it moves freely. If it does not fit where you drop it, it does not move and the line below says why. Doors slide along their wall. |
| **Habitación** | Paints a whole room: floor and walls at once. Painting over another room joins them (two rectangles make an L) and the walls follow the edge by themselves. With Borrar or <kbd>Alt</kbd>, it cuts the room. |
| **Pared** | Raises walls. As a line, also diagonal at 45°. Segment by segment, one tap raises the nearest segment and a stroke bends at right angles. As a rectangle, drag diagonally. With Borrar or <kbd>Alt</kbd>, it removes them. |
| **Piso** | Lays tiles: one at a time, half tiles, in a line, as a rectangle or as a fill. <kbd>Shift</kbd> and a tap fills the room. <kbd>Alt</kbd> removes. |
| **Pintura** | Tap a wall or an object to give it the chosen material. With <kbd>Shift</kbd> it paints all connected walls, or every part of the object. |
| **Cuentagotas** | Tap a wall, an object or the floor to pick up its material (and a wall's height). Then it returns to the previous tool. |
| **Mazo** | Tap anything to remove it. Dragging along a wall removes just that stretch. |

While dragging a rectangle with Habitación you can type its size, for example «4 x 3,5» (meters, with a decimal comma), and press <kbd>Enter</kbd>. If it is mistyped, Fornu says «Escribí ancho x fondo en metros, como 4 x 3,5.» (type width x depth in meters). With Pared as a line, type the length («3,5») and press <kbd>Enter</kbd>.

### The brushes

With Habitación, Pared, Piso, Pintura or Cuentagotas, a second bar appears with how to paint and the materials:

- **The shape.** Piso: **De a una baldosa** (tile by tile), **Media baldosa** (half tile), **Línea** (line), **Rectángulo** (rectangle) and **Rellenar** (fill). Pared: **Línea**, **De a un tramo** (segment by segment) and **Rectángulo**. Habitación: **Rectángulo**, **De a una celda** (cell by cell) and **Línea**. Each tool remembers its own.
- **Media baldosa** adds ↺ ↻ to turn the half tile, also with <kbd>R</kbd> or <kbd>Shift</kbd> + <kbd>R</kbd>.
- **Borrar** (erase): «Saca en vez de poner, con la misma forma (o mantené Alt)» (removes instead of adding, with the same shape, or hold Alt).
- **Material**: floors for Piso and Habitación, walls and objects for Pintura, everything for Cuentagotas.
- **Paredes** (walls), with Habitación and Pared: the walls' material and height, **Completa · 2,60 m** (full), **Media · 2,20 m** (half) or **Baja · 1,10 m** (low).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-paredes.jpg' | relative_url }}" alt="The Pared tool bar: Línea, De a un tramo selected and Rectángulo, the Borrar button, the materials and the Paredes heading. Below, the wall materials and the height Completa · 2,60 m. On the plan, an L-shaped room of 18.1 m² and a closed room of 74.4 m²." loading="lazy" width="1090" height="750">
  <ol class="marks">
    <li>The shape: <b>Línea</b>, <b>De a un tramo</b> or <b>Rectángulo</b>.</li>
    <li><b>Material</b>, and on the right the <b>Paredes</b> heading of the row below.</li>
    <li>The walls' material and height.</li>
    <li>Two rectangles painted with Habitación make an L.</li>
    <li>Each closed room shows its area.</li>
  </ol>
  <figcaption>Raising walls and rooms.</figcaption>
</figure>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-piso.jpg' | relative_url }}" alt="The Piso tool bar: De a una baldosa, Media baldosa selected, Línea, Rectángulo and Rellenar, the buttons to turn the half tile, Borrar and the materials. On the plan, a square of tiles with three half tiles set diagonally beside it." loading="lazy" width="1090" height="620">
  <ol class="marks">
    <li>How the floor is laid.</li>
    <li>↺ ↻: turn the half tile.</li>
    <li><b>Borrar</b>: removes with the same shape.</li>
    <li>Half tiles, for diagonal edges.</li>
    <li>A floor laid as a rectangle.</li>
  </ol>
  <figcaption>Laying the floor.</figcaption>
</figure>

### Building a dining room from scratch

1. With nothing selected, set the place's **Ancho (m)** and **Fondo (m)** (2 to 120 m per side).
2. With **Habitación** set to **Rectángulo**, drag out the room. While dragging, you can type «12 x 8» and press <kbd>Enter</kbd>.
3. For a kitchen or a restroom, paint another room right next to it: the walls sort themselves out.
4. Under **Agregar**, drag doors and windows onto the walls.
5. With **Piso** and **Pintura**, choose the materials.
6. Place the tables: the ones waiting under **Sin ubicar** (unplaced) and new ones from the **Mesas** group. Add the bar, the till, the columns and the rest.
7. Tap **Guardar el plano**.
{: .steps}

### The catalog {#catalogo}

Under **Agregar** is everything you can place, drawn as seen from above, chairs included:

| Group | What it has |
|---|---|
| **Sin ubicar** (unplaced) | The section's tables that are not on the plan yet. |
| **Puertas y ventanas** (doors and windows) | Puerta, Puerta doble, Ventana, Ventanal, Paso (door, double door, window, large window, opening). |
| **Mesas** (tables) | Mesa de 2, Mesa de 4, Mesa de 6, Mesa larga, Redonda de 4, Redonda de 6, Redonda de 10, Mesa alta (tables for 2, 4 and 6, long table, round tables, high table). |
| **Asientos** (seating) | Silla, Banqueta, Box, Sillón, Butaca (chair, stool, booth, armchair, seat). |
| **Estructura** (structure) | Columna redonda, Columna cuadrada, Escalera (round column, square column, stairs). |
| **Servicio** (service) | Pase de cocina, Barra, Caja, Heladera exhibidora, Estación de café, Atril de recepción (kitchen pass, bar, till, display fridge, coffee station, host stand). |
| **Deco** (decor) | Planta, Planta alta, Cantero, Alfombra, Biombo, Cartel, Cuadro (plant, tall plant, planter, rug, screen, sign, picture). |
| **Exterior** (outdoor) | Sombrilla, Estufa de exterior, Pérgola, Deck, Árbol, Banco, Valla (umbrella, patio heater, pergola, deck, tree, bench, fence). |
| **Eventos** (events) | Escenario, Pista de baile, Cabina de DJ, Mesa de buffet, Mesa dulce, Living (stage, dance floor, DJ booth, buffet table, dessert table, lounge). |
| **Propios** (your own) | The account's [own objects](#objetos). |

To place something:

- **With a mouse or a pen**, drag it onto the plan. While you carry it, a green or red outline tells you whether it fits there, and it stays where you drop it. Dropping it off the plan does nothing.
- **With a finger**, tap it: it stays «in your hand». Each tap on the plan places one, one after another. To stop, press <kbd>Esc</kbd> or tap the object in the catalog again.
- **Doors and windows** go on a wall: drag them onto one, or tap them and then tap the wall. They open toward the side you place them from, and they do not go on diagonal walls. If they do not fit, the line below says «Acercate a una pared.» (get closer to a wall), «Las aberturas van sobre una pared.» (openings go on a wall) or «La abertura tiene que quedar entera sobre la pared.» (the opening has to sit fully on the wall).
- **To remove something**, drag it from the plan back onto the catalog, where it reads «Soltalo acá para sacarlo del plano» (drop it here to take it off the plan).

A table brought from the Mesas group is a new dining room table: it reads «Nueva» (new) until you save, and then takes the next number and the chairs you gave it (4 if you changed nothing).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-catalogo.jpg' | relative_url }}" alt="The editor in isometric view with an own object, a barrel, selected on the plan with its bar above it. On the right, the catalog at the Exterior, Eventos (Escenario, Pista de baile, Cabina de DJ, Mesa de buffet, Mesa dulce, Living) and Propios groups, with the Barril." loading="lazy" width="1340" height="790">
  <ol class="marks">
    <li><b>Agregar</b> and <b>Editar</b>.</li>
    <li>A catalog group: <b>Eventos</b>.</li>
    <li><b>Propios</b>: a barrel built under Objetos propios.</li>
    <li>The barrel on the plan, with its bar.</li>
  </ol>
  <figcaption>The catalog, with one of your own objects.</figcaption>
</figure>

### The selection: its bar, rotation and the Editar panel {#girar}

When you select something, a bar appears next to it:

- **↺** and **↻**: turn left or right (<kbd>R</kbd>).
- **Duplicar** (duplicate, <kbd>Ctrl</kbd> + <kbd>D</kbd>): the copy goes beside it. If it does not fit, it says «La copia no entra al lado.» (the copy does not fit beside it).
- On tables, **− 4 sillas +** (chairs), up to as many as fit.
- On doors, **⇄**: «Dar vuelta hacia dónde abre (F)» (flip which way it opens).
- **✕**: «Sacar del plano (Supr)» (take off the plan, Delete).

Below the object there is a handle to turn it by hand: in 15° steps, 45° with <kbd>Shift</kbd>, freely with <kbd>Alt</kbd>.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-girar.jpg' | relative_url }}" alt="A table for six turned diagonally, reading Nueva, with its bar above it (turn, turn, duplicate, minus 6 sillas plus, remove) and the rotation handle below." loading="lazy" width="1040" height="570">
  <ol class="marks">
    <li>The bar: turn, duplicate, chairs and remove.</li>
    <li>The handle to turn it by hand.</li>
    <li>A new table, turned.</li>
  </ol>
  <figcaption>Turning a table on the terrace.</figcaption>
</figure>

The **Editar** panel shows what is selected. On a table, «Mesa 1 · 4 sillas» and an **Editar la mesa** button (its number, chairs and section), the **Modelo** (model), the rotation in degrees with ↺ ↻, and **Sillas** with «Le entran hasta 6.» (fits up to 6). Resizable items have **Largo (cm)** (length) and **Ancho (cm)** (width): the Mesa larga goes from 120 to 600 cm. At the bottom, the size and **Sacar del plano** (on tables) or **Quitar** (remove, on everything else).

With nothing selected, the panel shows **El espacio**: the **Ancho (m)** and **Fondo (m)**, 2 to 120 m per side in 25 cm steps, and a hint: «Poné el piso baldosa por baldosa con Piso, levantá las paredes con Pared, y arrastrá lo demás del catálogo al plano.» (lay the floor tile by tile with Piso, raise the walls with Pared, and drag everything else from the catalog onto the plan).

### Measurements

Each room closed by walls shows its area in m², and a selected wall shows its length. While you draw, the line below the plan shows the length or size of what you are drawing.

### Clearing the plan

With nothing selected, **Vaciar el plano** removes the floor, the walls, the doors and the fixed items, to start again on the bare grid. It asks first: «Se saca el piso, las paredes, las puertas y lo fijo: queda la grilla para armarlo de nuevo. Las mesas quedan. Se puede deshacer.» (the floor, walls, doors and fixed items go, the grid stays, the tables stay, and it can be undone).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-vaciar.jpg' | relative_url }}" alt="The Vaciar el plano confirmation: the floor, walls, doors and fixed items go, the grid stays, the tables stay and it can be undone, with Volver and Vaciar" loading="lazy" width="500" height="240">
  <figcaption>Before clearing, Fornu asks.</figcaption>
</figure>

### What blocks saving

**Guardar el plano** does nothing while there is an error, and the first one shows at the bottom:

- «Mesa 1 y Barra se pisan.» (table 1 and the bar overlap)
- «Mesa 4 atraviesa una pared.» (table 4 goes through a wall)
- «Planta tapa el paso de una puerta.» (a plant blocks a doorway)
- «Mesa 9: queda fuera del espacio.» (table 9 is outside the space)
- «Mesa 2: le entran hasta 4 sillas.» (table 2 fits up to 4 chairs)

If another device saved the same plan while you were drawing, Fornu says «Otro dispositivo guardó este plano mientras dibujabas. Descartá lo tuyo para ver el suyo.» (another device saved this plan while you were drawing, discard yours to see theirs). If you leave with unsaved changes, it asks first: «El plano tiene cambios que no se guardaron.».

### Touch, mouse and keyboard

- **Touch**: one finger uses the tool, two fingers zoom and pan. Putting a second finger down mid-stroke cancels the stroke.
- **Mouse**: the wheel zooms. To pan, hold the space bar and drag, or drag with the middle or right button.
- **Keyboard**: click the editor first. Keys do nothing while you are typing in a field.

| Key | What it does |
|---|---|
| <kbd>Ctrl</kbd> + <kbd>Z</kbd> | Undo |
| <kbd>Ctrl</kbd> + <kbd>Y</kbd> or <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Z</kbd> | Redo |
| <kbd>Ctrl</kbd> + <kbd>S</kbd> | Save the plan |
| <kbd>R</kbd> / <kbd>Shift</kbd> + <kbd>R</kbd> | Turn the selection, or what you are carrying, 90° or 45°. With Piso, turns the half tile. |
| <kbd>F</kbd> | Flip a door |
| <kbd>Delete</kbd> or <kbd>Backspace</kbd> | Remove the selection |
| <kbd>Ctrl</kbd> + <kbd>D</kbd> | Duplicate |
| Arrows | Move 25 cm |
| <kbd>Alt</kbd> + arrows | Move 1 cm |
| <kbd>Esc</kbd> | Deselect, stop placing or cancel a drag |
| Numbers and <kbd>Enter</kbd> while dragging | The exact length or size |

## Tracing a plan {#calcar}

If you have the place's floor plan as a photo or an image, put it underneath and draw on top.

1. With nothing selected, set the place's real **Ancho (m)** and **Fondo (m)**. The image is stretched over the whole space, so the measurements have to match.
2. Tap **Calcar un plano** and choose the image. It appears under the drawing, half transparent.
3. Use the **Calco** (tracing) slider to make it lighter or darker.
4. Draw over it with **Habitación** and **Pared**.
5. When you are done, tap **Quitar el calco** (remove the tracing) and **Guardar el plano**.
{: .steps}

The tracing stays on this screen only: it is not saved with the plan.

<div class="callout tip"><p class="callout-title">Tip</p><p>If the plan has a measurement written on it, an 8 m wall for example, use it to set the width and depth before tracing. That way the walls you draw on top come out at their real length.</p></div>

## Printing and exporting {#imprimir}

- **Imagen** downloads the plan as a 2400 × 1600 PNG image, exactly as you are seeing it: the same view, textures and names. Fornu says «Imagen descargada.» (image downloaded). Use it to send by message or drop into a presentation.
- **Imprimir** prints the plan on its own, on a landscape page.

The image comes out in the view you are using: an isometric view with textures to show the place off, Basic for a clean sheet with the table numbers.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-imagen.jpg' | relative_url }}" alt="The image that Imagen downloads: the dining room in isometric view with six tables for four on the floor" loading="lazy" width="1200" height="800">
  <figcaption>What <b>Imagen</b> downloads, in isometric view (scaled down).</figcaption>
</figure>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-imprimir.jpg' | relative_url }}" alt="The Imprimir sheet, landscape: the dining room seen from above with six tables and their numbers" loading="lazy" width="1047" height="718">
  <figcaption>The sheet <b>Imprimir</b> prints.</figcaption>
</figure>

## Espacios › Lugares {#lugares}

A place keeps a space's floor, walls, openings and fixed items, so you can build other plans on top of it: a rented hall, a country house, a marquee. It is useful if you set up events in different venues, or to keep your empty premises and try out layouts.

<p class="perm"><span>Who can:</span> <span class="tag">Biblioteca</span></p>

**From the editor**, the **Lugares** button opens the list of saved places:

- **Usar como base** (use as base) puts that place under the plan: «El lugar del plano (piso, paredes y lo fijo) se reemplaza por este; lo acomodado queda.» (the plan's place, floor, walls and fixed items, is replaced by this one, and what is arranged stays). Confirm with **Usar este lugar** (use this place). It can be undone, and you need to tap **Guardar el plano** to keep it.
- **Guardar este plano como lugar** (save this plan as a place): type a name (for example «Quinta Los Álamos») and tap **Guardar**. Fornu says «Lugar guardado.» (place saved). It saves the place's fixed parts, without the tables.

With none saved, it reads «Todavía no hay lugares guardados.» (no saved places yet).

**Under Espacios › Lugares** are all of them, one per tab with its size, and the full editor underneath. **Nuevo lugar** (new place) creates «Lugar 1», 10 × 8 m with a smooth cement floor («Lugar creado.», place created). **Borrar el lugar** (delete the place) removes it, and spaces built on it do not change. With no places, the screen reads «Todavía no hay lugares. Creá uno, o guardá el plano de un sector como lugar desde su editor.» (no places yet, create one or save a section's plan as a place from its editor).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-lugares.jpg' | relative_url }}" alt="Espacios, Lugares with a new 10 by 8 metre place: its tab, Nuevo lugar, Borrar el lugar, and the editor below with its tools, Lugares, Calcar un plano, Imagen and Imprimir" loading="lazy" width="1440" height="838">
  <ol class="marks">
    <li>The place, with its size. There is one tab per place.</li>
    <li><b>Nuevo lugar</b> (new place).</li>
    <li><b>Borrar el lugar</b> (delete the place).</li>
    <li><b>Lugares</b>, in the editor: use one as a base or save the plan as a place.</li>
  </ol>
  <figcaption>A freshly created place: 10 × 8 m of smooth concrete.</figcaption>
</figure>

## Espacios › Objetos propios {#objetos}

If the catalog lacks something your place has, build it from simple pieces: a barrel, a drinks fridge, a counter with shelves. Your own objects are added to the builder's catalog, in the **Propios** group. The bar reads **Objetos** and the page title is **Objetos propios**.

<p class="perm"><span>Who can:</span> <span class="tag">Biblioteca</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-objeto.jpg' | relative_url }}" alt="The object composer: Nombre Barril, Va set to En la disposición: se mueve, Ancho 100, Fondo 60, Alto 90, Sólido ticked, Empezar de with Caja, Cilindro (selected), Mesa con patas and Estante, Materiales with Principal, the Piezas table with one cylinder, and on the right the preview of a brown cylinder. At the bottom, Cancelar and Guardar el objeto." loading="lazy" width="1440" height="790">
  <ol class="marks">
    <li><b>Nombre</b> (name), <b>Va</b> (whether it moves or stays fixed in the place), its size in cm and <b>Sólido</b> (solid).</li>
    <li><b>Empezar de</b> (start from): a base shape.</li>
    <li><b>Materiales</b> (materials): up to three, each with its color and name.</li>
    <li><b>Piezas</b> (pieces): each piece with its shape, material, position and size.</li>
    <li><b>Cómo se ve</b> (how it looks): the preview, in isometric view.</li>
    <li><b>Guardar el objeto</b> (save the object).</li>
  </ol>
  <figcaption>A barrel made from one cylinder.</figcaption>
</figure>

1. Tap **Nuevo objeto** (new object).
2. Type the **Nombre** (for example «Barril»).
3. Under **Va**, choose **En la disposición: se mueve** (part of the layout, it moves), like a table, or **Fijo en el lugar** (fixed in the place), like a column, which is saved with the place.
4. Set the **Ancho**, **Fondo** and **Alto** (width, depth and height) in centimeters. **Sólido: nada se le encima** (solid, nothing goes on top) keeps anything else from being placed over it.
5. Under **Empezar de**, choose a base: **Caja** (box), **Cilindro** (cylinder), **Mesa con patas** (table with legs) or **Estante** (shelf).
6. Under **Materiales**, set up to three colors with their names (**+ Material**).
7. Under **Piezas**, adjust each piece: its shape (Caja or Cilindro), its material, **X** and **Y** (how far it shifts from the object's center), **Desde** (the height it starts at), **Ancho**, **Fondo** and **Alto**. **+ Pieza** adds another. Everything is in centimeters.
8. Check **Cómo se ve** and tap **Guardar el objeto**. Fornu says «Objeto guardado: ya está en el catálogo.» (object saved, it is in the catalog now).
{: .steps}

Each object becomes a card with its size and how many pieces it has, with **Editar** and **Borrar** (delete). Deleting it takes it out of the catalog, and a plan that already has it asks you to remove it the next time it is saved.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-objetos.jpg' | relative_url }}" alt="Espacios, Objetos propios with two cards, Barril and Heladera de bebidas, each with its size, its pieces and the Editar and Borrar buttons" loading="lazy" width="1440" height="340">
  <figcaption>Two custom objects, already in the catalog.</figcaption>
</figure>

## Espacios › Texturas propias {#texturas}

Photos of your place's floor, walls or tiles, and your logo for a sign: they are added to the builder's materials, so the plan looks like the real thing. The bar reads **Texturas** and the page title is **Texturas propias**.

<p class="perm"><span>Who can:</span> <span class="tag">Biblioteca</span></p>

1. Tap **Subir una textura** (upload a texture) and choose the photo.
2. In **Nueva textura** (new texture), check under **Cómo se repite** (how it repeats) how it tiles.
3. Type the **Nombre** (for example «Baldosa del patio», patio tile).
4. Under **Una copia cubre (cm)** (one copy covers), enter how big what the photo shows is in real life: a 20 cm tile, a 90 cm logo. It goes from 20 to 1000, and starts at 100.
5. Under **Va en** (goes on), tick where it is used: **Pisos** (floors), **Paredes** (walls) or **Objetos** (objects).
6. Tap **Guardar**. Fornu says «Textura guardada: ya está en los pinceles.» (texture saved, it is in the brushes now).
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-textura.jpg' | relative_url }}" alt="The Nueva textura dialog: Nombre Baldosa del patio, Una copia cubre (cm) at 100 with the hint Lo que mide en el local lo que se ve en la foto, and Va en with Pisos ticked and Paredes and Objetos unticked." loading="lazy" width="620" height="265">
  <ol class="marks">
    <li><b>Nombre</b>.</li>
    <li><b>Una copia cubre (cm)</b>: the real size of what the photo shows.</li>
    <li><b>Va en</b>: floors, walls or objects.</li>
  </ol>
  <figcaption>Uploading the patio tile.</figcaption>
</figure>

When you delete a texture, wherever it was used keeps its color. With none of your own, the screen reads «Todavía no hay texturas propias.» (no textures of your own yet).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-texturas.jpg' | relative_url }}" alt="Espacios, Texturas propias with one card, Baldosa del patio, for floors and 40 cm, with the Borrar button" loading="lazy" width="1440" height="340">
  <figcaption>A custom texture, ready among the brushes.</figcaption>
</figure>

Besides your own, the builder comes with these materials:

| For | Materials |
|---|---|
| Floors | Parquet claro, Madera oscura, Madera rústica, Damero, Calcáreo, Laja, Césped (light parquet, dark wood, rustic wood, checkerboard, patterned tile, flagstone, grass) |
| Floors and walls | Piedra gris, Venecitas, Cemento alisado, Cemento oscuro (grey stone, mosaic, smooth cement, dark cement) |
| Floors and objects | Alfombra, Mármol blanco, Mármol negro (carpet, white marble, black marble) |
| Walls | Revoque blanco, Revoque arena, Revoque verde, Piedra, Ladrillo, Ladrillo reciclado (white, sand and green plaster, stone, brick, reclaimed brick) |
| Objects | Madera (also walls), Acero, Tela roja, Tela gris (wood, steel, red fabric, grey fabric) |
| Paints for walls and objects | Blanco, Verde salvia, Azul petróleo, Terracota, Negro (white, sage green, petrol blue, terracotta, black) |

## How the waiters see it {#en-el-salon}

The plan you built is what the waiters see under [Salón › Mesas]({{ '/en/projects/fornu/manual/salon/' | relative_url }}#mesas) in the **Plano** view: the same walls and objects, with each table painted in its state's color. Each device picks its view (Basic, Cenital or Isométrica) and remembers it.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-mesas.jpg' | relative_url }}" alt="Salón › Mesas in the Plano view, isometric with textures: the brick dining room with three tables and a bar, table 1 marked in blue with 0 min, and table 1's open bill on the right." loading="lazy" width="1440" height="710">
  <ol class="marks">
    <li>The view, chosen on this device.</li>
    <li><b>Texturas</b>, the walls and the rotation, as in the editor.</li>
    <li>Table 1, busy, in blue. One tap opens its bill.</li>
    <li>The table's bill, alongside.</li>
  </ol>
  <figcaption>Serving on the plan in isometric view.</figcaption>
</figure>

On the live floor the plan is only looked at and tapped: a tap on a table opens it (or seats it, if it is free), and dragging with one finger pans the plan. With the keyboard, <kbd>Tab</kbd> moves from table to table and <kbd>Enter</kbd> or the space bar opens it. To change anything on the plan, go back to the [editor](#editor).
