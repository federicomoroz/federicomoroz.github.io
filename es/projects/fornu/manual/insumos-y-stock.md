---
layout: manual
manual: insumos-y-stock
title: "Insumos y stock · Manual de Fornu"
description: "Cómo se cargan los ingredientes, las elaboraciones y el inventario con su costo, cómo se lleva el stock con entradas, producción, mermas y conteos, y cómo se planifica una producción."
permalink: /es/projects/fornu/manual/insumos-y-stock/
---

## Ingredientes, producción e inventario {#insumos}

Los insumos son todo lo que la cocina usa para hacer la carta, cada uno con lo que cuesta. Con ellos se arman las recetas, y de ellos sale el costo de cada producto. Están repartidos en tres pestañas de Insumos:

- **Ingredientes**: la materia prima que se compra para cocinar.
- **Producción**: lo que la cocina hace por tandas con una receta y no se vende solo, como los medallones porcionados o una salsa. Cada uno es una elaboración.
- **Inventario**: lo que se compra y se usa sin cocinarlo, como descartables y packaging, limpieza, bazar y librería.

Cualquier receta puede usar insumos de las tres. Cada pestaña tiene su botón para cargar uno nuevo (**Ingrediente**, **Elaboración** o **Artículo**) y **Importar planilla**.

<p class="perm"><span>Quién puede:</span> <span class="tag">Insumos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-ingredientes.jpg' | relative_url }}" alt="La lista de ingredientes agrupada en Carnes y Verduras y frutas, con cómo se compra cada uno y a cuánto, el proveedor, el rendimiento y el costo de cada kilo que se usa." loading="lazy" width="1440" height="675">
  <ol class="marks">
    <li><b>Cómo entra</b>: cómo se compra, a cuánto y desde cuándo vale ese precio, como «caja de 10 kg a $ 75.000».</li>
    <li><b>Proveedor</b>: a quién se le compra, con el módulo Proveedores y compras.</li>
    <li><b>Rinde</b>: cuánto se aprovecha de lo que entra.</li>
    <li><b>Costo utilizable</b>: lo que cuesta cada kilo, litro o unidad que se usa de verdad, con el rendimiento ya descontado.</li>
    <li><b>Estado</b>: lo que conviene revisar de ese insumo.</li>
  </ol>
  <figcaption>Los ingredientes de la demo, agrupados por categoría.</figcaption>
</figure>

El rendimiento cambia el costo. La pechuga de pollo cuesta $ 75.000 la caja de 10 kg, o sea $ 7.500 el kilo, pero rinde 92%: cada kilo que se usa cuesta $ 8.152,17.

El buscador encuentra insumos por nombre, categoría o proveedor. Un ⓘ al lado del nombre quiere decir que el insumo tiene una nota: pasá el mouse para leerla. Los insumos desactivados se ven más claros.

La columna **Estado** muestra lo más importante y cuántos avisos más hay («+2»). Pasá el mouse para verlos todos:

| Aviso | Qué quiere decir |
|---|---|
| «Falta el precio» | Sin precio, todo lo que lo usa queda sin costo. |
| «Sin receta» | Una elaboración que todavía no tiene receta. |
| «… no tiene precio» | La receta de la elaboración lleva un insumo sin precio. |
| «Precio de hace N días» o «Precio sin fecha» | El precio puede estar viejo. A partir de cuántos días se avisa se fija en [Ajustes › Configuración]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#configuracion). |
| «Tiene una nota» | Alguien dejó una nota en el insumo. |
| «Lleva …, que está desactivado» | La receta usa un insumo apagado. |

### Cargar un ingrediente o un artículo {#nuevo-insumo}

1. Tocá **Ingrediente**, o **Artículo** en Inventario.
2. Escribí el **Nombre**, elegí la **Categoría** y la **Unidad**.
3. Completá cómo se compra: **Se compra por**, **Cuánto trae**, el precio de cada una y su IVA.
4. Si se pierde algo al limpiarlo, poné el **Rendimiento**. Si querés que Fornu avise cuando queda poco, poné el **Stock mínimo**.
5. Tocá **Guardar**, o apretá <kbd>Ctrl</kbd> + <kbd>Enter</kbd>.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-ficha.jpg' | relative_url }}" alt="Dos paneles de un ingrediente: a la izquierda el principio de uno nuevo, con unidad, cómo se compra, precio e IVA. A la derecha, el final de la carne picada, con rendimiento, stock mínimo, nota, historial de precios y dónde se usa." loading="lazy" width="1260" height="900">
  <ol class="marks">
    <li><b>Unidad</b>: gramos, mililitros o unidades. Las recetas, el stock y los conteos usan esta. Después no se cambia.</li>
    <li><b>Se compra por</b> y <b>Cuánto trae</b>: la presentación (bolsa, caja, maple) y lo que trae, en la unidad del insumo.</li>
    <li><b>Precio de cada una</b>, <b>El precio es</b> e <b>IVA</b>: el precio de una presentación, como figura en el comprobante.</li>
    <li><b>Rendimiento (%)</b>: lo que se puede usar de lo que entra.</li>
    <li><b>Historial de precios</b>: cada precio que tuvo, desde cuándo y de dónde vino.</li>
    <li><b>Dónde se usa</b>: las recetas y los adicionales que lo llevan.</li>
  </ol>
  <figcaption>A la izquierda, el principio de un ingrediente nuevo. A la derecha, el final de uno que ya existe.</figcaption>
</figure>

| Campo | Para qué sirve |
|---|---|
| **Nombre** | Obligatorio. |
| **Categoría** | Una de las categorías activas de esa pestaña. |
| **Unidad** | **Gramos**, **Mililitros** o **Unidades**. En Inventario arranca en unidades. Queda fija al guardar, porque el stock y las recetas están en esa unidad. |
| **Se compra por** | La presentación: caja, bolsa, kg, pack. Hace falta para guardar: sin ella, el pie dice «Falta cómo se compra (caja, bolsa, kg…).». |
| **Cuánto trae** | Lo que trae cada presentación, en la unidad del insumo. Arranca en 1.000 g, o en 1 u. También hace falta para guardar: sin ella, el pie dice, por ejemplo, «Falta cuántos g trae cada bolsa.». |
| **Precio de cada una** | El precio de una presentación. Debajo dice cuánto le cuesta a la cuenta. Las compras con precio lo actualizan solas. |
| **El precio es** | **Con IVA, como en un ticket** o **Sin IVA, como en una factura A**. |
| **IVA** | 21%, 10,5%, 27%, 5%, 2,5% o **Exento (0%)**. Carnes, frutas, verduras y harinas suelen ir al 10,5%. |
| **Precio desde** | La fecha del precio. Salta a hoy cuando cambiás el precio, salvo que elijas otra fecha a mano. Sin fecha, Fornu no sabe si está al día. |
| **Proveedor** | A quién se le compra. **+ Proveedor nuevo** lo crea ahí mismo con su nombre y su CUIT. Aparece con el módulo Proveedores y compras, para quien tiene el permiso **Proveedores**. |
| **Rendimiento (%)** | En Ingredientes y Producción. Poné 80% si se pierde un 20% al limpiarlo. El costo utilizable sube en esa proporción. |
| **Stock mínimo** | Cuando el stock llega a este número, el insumo aparece en el mínimo, en Stock y en Inicio. |
| **Activo** | Apagado, el insumo deja de ofrecerse en las compras y en el conteo. Los insumos se desactivan en vez de borrarse. |
| **Nota** | Hasta 400 letras para quien carga los precios. No se imprime en ningún lado. |

Cuánto cuesta un insumo depende de la **Condición frente al IVA** de la cuenta, en [Ajustes › Configuración]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#configuracion). Con Responsable inscripto, el costo es sin IVA, porque el IVA se recupera. Con Monotributo, es con IVA. Debajo del precio, la ficha dice cuál de los dos usa, y **El precio es** arranca en el que corresponde.

<div class="callout"><p class="callout-title">Importante</p><p>Si desactivás un insumo que está en alguna receta, Fornu avisa: «Desactivado, las recetas que lo llevan lo siguen descontando, pero no se pueden guardar cambios en ellas hasta sacarlo o reactivarlo.» Mirá <b>Dónde se usa</b> antes de apagarlo.</p></div>

### Historial de precios y dónde se usa {#historial-precios}

En un insumo que ya existe, **Historial de precios** muestra los últimos seis precios, y **Ver los N** muestra el resto. Cada fila tiene desde cuándo, el precio, el IVA, cuánto cambió (en rojo si subió, en verde si bajó) y de dónde vino. Pasá el mouse para ver quién lo cambió y cuándo.

| Origen | Qué fue |
|---|---|
| **Alta** | El precio con que se cargó. |
| **Editado** | Alguien lo cambió a mano. |
| **Compra** | Lo trajo una compra de insumos. |
| **Compra en Stock** | Una entrada de mercadería desde Stock. |
| **Cambio masivo** | Un **Cambiar precio** sobre varios insumos. |
| **Compra anulada** | Se anuló la compra que lo había puesto y volvió el anterior. |

**Dónde se usa** lista los productos, las elaboraciones (como «Producción: Salsa de la casa») y los adicionales de cada unidad de negocio que llevan el insumo. Si no lo usa nadie, dice «Ninguna receta ni adicional lo lleva.»

### Cargar una elaboración y su receta {#elaboracion}

Una elaboración cuesta lo que lleva su receta, así que se carga en dos pasos.

1. En Producción, tocá **Elaboración**.
2. Escribí el nombre, la categoría, la unidad y cuánto rinde una tanda en **Una tanda rinde**. Tocá **Guardar**.
3. En su fila, tocá **Receta**.
4. Agregá los insumos que lleva una tanda, con su cantidad, y tocá **Guardar**. Fornu confirma «Receta guardada».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-produccion.jpg' | relative_url }}" alt="La lista de producción con el bollo de pizza grande en Porcionados y cinco semielaborados, cada uno con el tamaño de su tanda, el costo de cada kilo o unidad y un botón Receta." loading="lazy" width="1440" height="610">
  <ol class="marks">
    <li><b>Cómo entra</b>: el tamaño de la tanda y cuántos insumos lleva, como «Tanda de 1,5 kg con 4 insumos».</li>
    <li><b>Costo utilizable</b>: lo que cuesta cada kilo o unidad, según su receta.</li>
    <li><b>Receta</b>: abre lo que lleva una tanda.</li>
  </ol>
  <figcaption>Las elaboraciones de la demo.</figcaption>
</figure>

Arriba de la receta dice cuánto rinde la tanda y cuánto cuesta, entera y por kilo o unidad. Hasta cargarla, el estado de la elaboración dice «Sin receta». Una receta lleva al menos un insumo, y una elaboración no puede llevarse a sí misma, ni siquiera a través de otra elaboración.

### Cambiar muchos a la vez {#cambios-masivos}

Tildá los insumos en la lista y usá la barra que aparece arriba:

- **Cambiar precio**: sube o baja por porcentaje o por monto, con redondeo. Cada precio nuevo vale desde hoy y queda en el historial del insumo. Los que no tienen precio no cambian. No está en Producción, porque el costo de una elaboración sale de su receta.
- **Cambiar categoría**: pasan todos a la misma categoría.
- **Cambiar proveedor**: todos pasan a comprarse al mismo proveedor. Está con el módulo Proveedores y compras.
- **Quitar la selección**.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-cambiar-proveedor.jpg' | relative_url }}" alt="Un ingrediente tildado, la barra con Cambiar precio, Cambiar categoría, Cambiar proveedor y Quitar la selección, y a la derecha el panel Proveedor de 1 ingrediente con el campo Se compran a." loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li>La barra de la selección, con cuántos insumos tildaste.</li>
    <li><b>Se compran a</b>: el proveedor para todos los tildados.</li>
    <li><b>Aplicar</b>.</li>
  </ol>
  <figcaption>Cambiar el proveedor de varios ingredientes juntos.</figcaption>
</figure>

<div class="callout"><p class="callout-title">Importante</p><p><b>Cambiar proveedor</b> arranca en <b>Sin proveedor</b>. Si tocás <b>Aplicar</b> sin elegir uno, les saca el proveedor a todos los tildados.</p></div>

### Categorías de insumos {#categorias-insumos}

Debajo de cada lista está la de sus categorías, con cuántos insumos tiene cada una y su orden. Una cuenta nueva arranca con estas:

| Pestaña | Categorías |
|---|---|
| Ingredientes | Carnes, Verduras y frutas, Lácteos y fiambres, Panificados, Almacén y Bebidas |
| Producción | Porcionados y Semielaborados |
| Inventario | Descartables y packaging, Limpieza, Bazar y Librería |

Cada categoría tiene **Nombre**, **Orden** y, al editarla, **Activa**. Una categoría con insumos no se borra. Movelos a otra, o desactivala para que deje de ofrecerse en los insumos nuevos. Si una pestaña se queda sin categorías activas, el botón para cargar insumos se apaga y la pantalla pide «Creá primero una categoría, más abajo.»

## Stock {#stock}

Lo que hay de cada insumo en esta cocina, para cuántos días alcanza, cuánto vale y qué falta. Acá se cargan las entradas rápidas, la producción, las mermas y los conteos. Cada cambio queda como un movimiento en el historial del insumo, así que siempre se puede ver qué pasó.

Está en Insumos › **Stock**. También es la pestaña **Stock** del dispositivo del local, para quien tiene el permiso.

<p class="perm"><span>Quién puede:</span> <span class="tag">Stock</span></p>

El rol **Encargado/a** de una cuenta nueva ya lo tiene.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-stock.jpg' | relative_url }}" alt="La pantalla Stock con el valor del stock, cinco insumos en el mínimo, cinco que se acaban en siete días y lo que está sin uso, y dos elaboraciones que avisan que faltó registrar lo producido." loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li>Las cifras: <b>Valor del stock</b>, <b>En el mínimo</b>, <b>Se acaban en 7 días</b> y <b>Sin uso en 2 semanas</b> (el plazo de la cuenta). Tocá una para filtrar la lista.</li>
    <li><b>Todo</b>, <b>Ingredientes</b>, <b>Producción</b> o <b>Inventario</b>. Abajo, el buscador.</li>
    <li>«Faltó registrar lo producido»: se vendió más de una elaboración de lo que se registró como producido. <b>Registrar lo usado</b> lo carga.</li>
    <li><b>Alcanza para</b>: cuántos días dura al ritmo de consumo.</li>
    <li><b>Producir</b> (o <b>Entrada</b>, en un insumo que se compra) y el menú <b>⋯</b>, con <b>Conteo</b>, <b>Merma</b> e <b>Historial</b>.</li>
    <li><b>Contar stock</b>: el conteo de todo el stock.</li>
  </ol>
  <figcaption>El stock de la demo. Las dos elaboraciones de arriba se vendieron sin registrar su producción.</figcaption>
</figure>

| Cifra | Qué dice |
|---|---|
| **Valor del stock** | Lo que vale todo lo que hay, al costo de hoy. |
| **En el mínimo** | Cuántos insumos están en su stock mínimo o debajo. En rojo si hay alguno. |
| **Se acaban en 7 días** | Los que no llegan a una semana al ritmo de consumo: debajo dice, por ejemplo, «al ritmo de las últimas 2 semanas». Al tocarla, ordena por los que se acaban primero. |
| **Sin uso en 2 semanas** (o en el plazo de la cuenta, como «Sin uso en 10 días») | Lo que está parado: cuánto vale y cuántos insumos son. Al tocarla, ordena por valor. |

| Columna | Qué muestra |
|---|---|
| **Insumo** | El nombre y la categoría. Si tiene mínimo, una barra muestra qué tan cerca está: ámbar cerca del mínimo, rojo en el mínimo o debajo. |
| **Hay** | Lo que hay, en gramos, mililitros o unidades. En rojo si está bajo. |
| **Mínimo** | El stock mínimo del insumo. |
| **Usa por día** | Lo que se usa por día, contando pedidos y producción. |
| **Alcanza para** | «N días», «Menos de 1 día», «Más de 60 días», «Sin stock» o «Sin uso reciente». En rojo menos de 3 días, en ámbar menos de 7. |
| **Valor** | Lo que vale lo que hay. |

La lista arranca con lo que falta primero. Tocá **Insumo**, **Alcanza para** o **Valor** para ordenarla por eso. El ritmo de consumo mira lo que se usó en el plazo de la cuenta, que se fija en **El ritmo de consumo mira los últimos (días)** de [Ajustes › Configuración]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#configuracion): 14 días si nadie lo cambió, que la pantalla muestra como «las últimas 2 semanas».

En Inicio, los avisos «N insumos están en el mínimo» y «N insumos se acaban antes de una semana» abren esta pantalla ya filtrada.

Con **Pausar lo que no alcanza con el stock**, en [Ajustes › Configuración]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#pausar), un producto que no se puede hacer con lo que hay deja de ofrecerse en los pedidos propios y se apaga en las plataformas, hasta que entra stock. Para que funcione bien, las compras y los conteos tienen que estar al día.

### Entrada de mercadería {#entrada}

Para sumar algo que llegó sin pasar por Compras: una reposición chica, algo que trajo el dueño.

1. Tocá **Entrada** en la fila del insumo.
2. Escribí cuántas presentaciones entraron. El campo dice cuál es, como **Cantidad (bolsa)**, y abajo aparece cuánto suma: «Cada bolsa trae 25 kg: entran 50 kg.»
3. Revisá el precio por presentación, si es con o sin IVA y el IVA. Viene el último precio.
4. Si querés, anotá de dónde vino.
5. Tocá **Registrar**. Fornu confirma «Entrada registrada».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-entrada.jpg' | relative_url }}" alt="El panel Entrada de mercadería del pan de papa: Cantidad 2 bolsas, Cada bolsa trae 12 u: entran 24 u, el precio por bolsa, si es con IVA, el IVA y De dónde vino" loading="lazy" width="620" height="900">
  <figcaption>Dos bolsas de pan de papa: entran 24 unidades.</figcaption>
</figure>

El precio que pongas actualiza el costo del insumo y los márgenes de todo lo que lo usa, y queda en el historial de precios como **Compra en Stock**.

<div class="callout"><p class="callout-title">Importante</p><p>Una entrada no genera comprobante ni deuda con el proveedor. Para cargar el remito o la factura de un proveedor, usá <a href="{{ '/es/projects/fornu/manual/compras-y-gastos/' | relative_url }}#compras">Compras de insumos</a>.</p></div>

### Producir {#producir}

Para registrar una tanda de una elaboración: entra al stock lo que se hizo y salen los insumos de su receta, en proporción a lo producido.

1. Tocá **Producir** en la fila de la elaboración.
2. Escribí la **Cantidad producida**, en la unidad de la elaboración.
3. Si querés, agregá una nota. Tocá **Registrar producción**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-producir.jpg' | relative_url }}" alt="El panel Producir de la salsa de la casa con Cantidad producida en 3000 gramos, que abajo dice 3 kg, y la nota opcional" loading="lazy" width="620" height="560">
  <figcaption>Una tanda de 3 kg de salsa.</figcaption>
</figure>

Si la elaboración no tiene receta o está desactivada, Fornu no la registra y dice por qué.

Cuando se vende algo que lleva una elaboración que nadie registró como producida, la fila avisa «Faltó registrar lo producido» y cuánto se usó de más. **Registrar lo usado** abre **Producir** con esa cantidad ya puesta.

En la cocina, los cocineros cargan la producción y las mermas desde la tablet, con su PIN y sin entrar a esta pantalla. Se explica en [En la cocina y en la calle]({{ '/es/projects/fornu/manual/cocina-y-reparto/' | relative_url }}#merma).

### Contar un solo insumo {#conteo-uno}

1. Tocá **⋯** › **Conteo** en la fila del insumo.
2. Escribí lo que contaste en **Cantidad contada**. Viene con lo que dice el sistema, y abajo dice «El sistema espera …».
3. Si querés, agregá una nota. Tocá **Registrar**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-conteo-uno.jpg' | relative_url }}" alt="El panel Conteo de la carne picada con Cantidad contada en 23500 gramos y abajo El sistema espera 24,1 kg" loading="lazy" width="620" height="560">
  <figcaption>Contar la carne picada: el sistema esperaba 24,1 kg.</figcaption>
</figure>

Si lo contado coincide, Fornu avisa que no hay nada que ajustar. Si alguien contó ese insumo después que vos, queda su conteo.

### Cargar una merma {#merma}

1. Tocá **⋯** › **Merma**.
2. Escribí la **Cantidad perdida** y el **Motivo**, como «se quemó» o «se venció». El motivo es obligatorio.
3. Tocá **Registrar**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-merma.jpg' | relative_url }}" alt="El panel Merma de la carne picada con 500 gramos perdidos y el motivo Se pasó de fecha" loading="lazy" width="620" height="560">
  <figcaption>Medio kilo de carne picada que se pasó de fecha.</figcaption>
</figure>

### Ver el historial de un insumo {#historial}

**⋯** › **Historial** muestra cada movimiento del insumo: cuándo fue, qué fue (**Compra**, **Ajuste por conteo**, **Merma**, **Usado en producción**, **Producción** o **Pedido**, con el precio cuando lo hay), la cantidad que sumó o restó, quién lo hizo y la nota. El historial es de a un insumo por vez.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-historial.jpg' | relative_url }}" alt="El historial de la carne picada: una compra de 10 kg a 9.900 pesos, y debajo lo que usó cada pedido y cada mesa, con quién lo hizo" loading="lazy" width="880" height="392">
  <figcaption>El historial de la carne picada: la compra y lo que usó cada venta.</figcaption>
</figure>

### En el celular y en el dispositivo del local {#stock-celular}

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/insumos-stock-telefono.jpg' | relative_url }}" alt="La pestaña Stock en el celular del local, con el botón Contar stock, las cuatro cifras y cada insumo en una tarjeta con lo que hay, para cuánto alcanza y su botón Producir o Entrada." loading="lazy" width="390" height="844">
  <figcaption>La pestaña Stock en el celular del local.</figcaption>
</figure>

En el celular, cada insumo es una tarjeta con lo que hay, para cuánto alcanza y sus botones. El mínimo, el uso por día y el valor no se muestran, y la lista se ordena tocando las cifras de arriba.

## Contar todo el stock {#conteo}

El conteo pone el stock igual a lo que hay de verdad. Conviene hacerlo al cerrar, o una vez por semana, recorriendo la cocina con el celular o la tablet en la mano.

<p class="perm"><span>Quién puede:</span> <span class="tag">Stock</span></p>

<div class="shot-pair">
<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/insumos-conteo-telefono.jpg' | relative_url }}" alt="El conteo de stock en el celular: el aceite de girasol con 7 ml contados y la diferencia en rojo, y abajo Guardar conteo." loading="lazy" width="390" height="844">
  <figcaption>En el celular, el conteo se recorre de arriba abajo.</figcaption>
</figure>
<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-conteo.jpg' | relative_url }}" alt="El panel Conteo de stock con la casilla Ver lo que dice el sistema apagada, las categorías para contar de a una y cada insumo con dos casillas, presentaciones enteras más lo suelto." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li><b>Ver lo que dice el sistema</b>: apagado de entrada, para contar sin mirar.</li>
    <li>Las categorías: tocá una para contar de a una.</li>
    <li>Lo que se compra por presentación tiene dos casillas: las presentaciones enteras más lo suelto.</li>
    <li>La diferencia con lo que esperaba el sistema, en verde o en rojo.</li>
    <li>Cuántos contaste y cuántos dieron distinto.</li>
    <li><b>Guardar conteo</b>.</li>
  </ol>
  <figcaption>El mismo conteo en la computadora.</figcaption>
</figure>
</div>

1. Tocá **Contar stock**.
2. Contá sin mirar lo que dice el sistema. Para lo que comprás por presentación, escribí las enteras en la primera casilla y lo suelto en la segunda, como 2 bolsas de 25 kg más 3.500 g.
3. Dejá vacío lo que no contaste: no se cuenta y no cambia.
4. Si querés, escribí una nota, como «Conteo de cierre».
5. Tocá **Guardar conteo**. Si algo dio distinto, Fornu pregunta «¿Ajustar N insumos a lo contado?» y aclara que el stock pasa a ser lo que escribiste y la diferencia queda en el historial de cada uno. Tocá **Guardar conteo** otra vez.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-ajustar.jpg' | relative_url }}" alt="La confirmación ¿Ajustar 4 insumos a lo contado?, que explica que el stock pasa a ser lo escrito y la diferencia queda en el historial, con Volver y Guardar conteo" loading="lazy" width="500" height="220">
  <figcaption>Antes de guardar, Fornu pregunta.</figcaption>
</figure>

Fornu confirma, por ejemplo, «Conteo guardado: 3 ajustes, 9 sin cambios». La lista muestra solo los insumos activos, agrupados por categoría, y se puede filtrar por grupo o buscar. Mientras haya un número que no se entiende, el pie lo cuenta y no deja guardar.

Lo que se movió después de que contaste un insumo, como un pedido o una entrega, se suma a tu conteo. Si otra persona contó el mismo insumo después que vos, queda su conteo, y Fornu lo avisa al guardar.

<div class="callout tip"><p class="callout-title">Consejo</p><p>El conteo se guarda en el dispositivo a medida que escribís. Si el celular se bloquea o se cierra la pestaña, al tocar <b>Contar stock</b> de nuevo aparece «Hay un conteo sin guardar de las 18:40: 12 insumos contados.», con <b>Seguir ese conteo</b> o <b>Empezar de cero</b>. Un conteo de hace más de dos días ya no se guarda: hay que contar de nuevo.</p></div>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-conteo-sin-guardar.jpg' | relative_url }}" alt="El conteo de stock abierto con el aviso Hay un conteo sin guardar de las 18:54: 4 insumos contados, y los botones Seguir ese conteo y Empezar de cero" loading="lazy" width="880" height="320">
  <figcaption>Un conteo que quedó sin guardar.</figcaption>
</figure>

## Planificar producción {#planificar}

Para preparar un día fuerte o un evento. Decís qué querés producir y cuánto, y Fornu calcula qué elaboraciones preparar antes, en tandas, y qué comprar, en presentaciones enteras, descontando lo que ya hay.

Está en Insumos › **Planificar producción** (la pestaña dice **Planificar**).

<p class="perm"><span>Quién puede:</span> <span class="tag">Stock</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-planificar.jpg' | relative_url }}" alt="Planificar producción con 300 Doble cheddar, 120 pizzas grandes y 150 Tiras crocantes, un costo de la producción de 1.913.166 pesos, 920.500 para comprar, cuatro elaboraciones para preparar antes y lo que hay que comprar a tres proveedores, con un botón Cargar compra para cada uno" loading="lazy" width="1440" height="1640">
  <ol class="marks">
    <li><b>Qué producir</b>: cada fila es un producto de la carta o una elaboración, con su cantidad.</li>
    <li><b>+ Agregar</b>, <b>Vaciar la lista</b> y <b>Restar lo que hay en el stock</b>.</li>
    <li>Las cifras: <b>Costo de la producción</b>, <b>Para comprar</b> y <b>Para preparar antes</b>.</li>
    <li><b>Preparar antes</b>: cada elaboración con lo que hace falta, lo que hay, lo que hay que preparar, en cuántas tandas y cuánto cuesta.</li>
    <li><b>Imprimir</b> y <b>Registrar producción</b>.</li>
    <li><b>Comprar</b>: lo que falta, por proveedor, con su total y <b>Cargar compra</b>.</li>
  </ol>
  <figcaption>Un día fuerte: lo que hay que preparar y lo que hay que comprar a cada proveedor.</figcaption>
</figure>

1. Tocá **+ Agregar** y elegí qué hacer: un producto de cualquier unidad de negocio, o una elaboración.
2. Escribí la cantidad: unidades para un producto, y la unidad de la elaboración para una elaboración.
3. Repetí con lo demás. El plan se recalcula solo.
{: .steps}

- Si hay elaboraciones debajo del mínimo, arriba aparece «Debajo del mínimo: …» con **Sumar al plan**. Suma cada una en tandas enteras, lo suficiente para llegar al mínimo y cubrir un día más de uso.
- **Restar lo que hay en el stock** viene prendido. Apagalo para calcular todo como si no hubiera nada.
- Un producto sin receta no suma nada, y el plan lo avisa: «Sin receta, … no suma nada al plan: cargala para que cuente.»
- La lista queda guardada en este navegador hasta que tocás **Vaciar la lista**.

### Imprimir la hoja de cocina {#imprimir}

**Imprimir** abre la impresión del navegador con una hoja limpia: el título Producción, la cocina y la fecha, qué producir, qué preparar antes con sus tandas y qué comprar con sus presentaciones. Cada línea tiene un casillero para tildar a mano, y al pie va el costo de la producción y lo que hay que comprar.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/insumos-hoja-produccion.jpg' | relative_url }}" alt="La hoja Producción impresa: la cocina y la fecha, Qué producir, Preparar antes con sus tandas y Comprar con sus presentaciones, cada línea con un casillero, y al pie el costo y lo que hay que comprar" loading="lazy" width="1440" height="790">
  <figcaption>La hoja de cocina, para tildar a mano.</figcaption>
</figure>

### Registrar la producción {#registrar-produccion}

**Registrar producción** pide confirmar, con un resumen como «Entran al stock 2 kg de Salsa, … y salen los insumos que llevan.», y registra solo las elaboraciones que faltan. Las compras no se registran desde acá. El botón queda apagado si no hay nada para producir, o si una elaboración del plan no tiene receta.

### Cargar la compra de lo que falta {#compra-del-plan}

En **Comprar**, cada proveedor tiene su total y un botón **Cargar compra**. Abre una compra de insumos ya armada: ese proveedor, la categoría Insumos, el comprobante **Remito**, la descripción «Lo que falta para el plan de producción», cada insumo en presentaciones enteras al precio de hoy, y pagada en efectivo hoy. Revisala y guardala como cualquier compra, en [Compras y gastos]({{ '/es/projects/fornu/manual/compras-y-gastos/' | relative_url }}#cargar-compra). Lo que no tiene proveedor va al final, en «Sin proveedor».

<div class="callout"><p class="callout-title">Importante</p><p>Guardar la compra pide el permiso <b>Gastos</b>. Y como arranca pagada en efectivo, si la vas a pagar más adelante cambiala a <b>A pagar</b> antes de guardar.</p></div>

## Importar desde una planilla {#importar}

Los ingredientes, los artículos de inventario y las recetas de las elaboraciones también se cargan desde una planilla, con **Importar planilla** en cada pestaña. En Ingredientes e Inventario se abre en **Insumos**, y en Producción, en **Recetas**. Las elaboraciones se crean a mano, y la planilla les carga la receta. El paso a paso y las columnas están en [Carta › Importar desde una planilla]({{ '/es/projects/fornu/manual/carta/' | relative_url }}#importar).
