---
layout: manual
manual: carta
title: "Carta · Manual de Fornu"
description: "Cómo se cargan los productos de cada unidad de negocio con sus precios por canal, su receta, sus adicionales y sus grupos modificadores, cómo se cambian muchos precios a la vez y cómo se importa todo desde una planilla."
permalink: /es/projects/fornu/manual/carta/
---

## Productos {#productos}

Es la carta de cada unidad de negocio: lo que vende, a cuánto en cada canal, cuánto cuesta hacerlo y cuánto deja. Desde acá se cargan los productos nuevos, se cambian los precios y se arma la receta que descuenta el stock en cada venta.

Está en Carta › **Productos**. Arriba hay una pestaña de color por unidad de negocio: tocá la que querés ver y la lista muestra solo su carta.

<p class="perm"><span>Quién puede:</span> <span class="tag">Carta</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-productos.jpg' | relative_url }}" alt="La lista de productos de Doble Smash, agrupada en Burgers y Para acompañar, con el precio base, el de Rappi y el de PedidosYa, el costo, el margen en pesos y el margen en porcentaje de cada producto." loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li><b>Doble Smash · Pollo Crocante · Bowl Verde · Pizzería</b>: una pestaña por unidad de negocio. Cada una tiene su carta.</li>
    <li><b>Importar planilla</b>, <b>Actualizar precios</b> y <b>Nuevo producto</b>: cargar muchos de una vez, subir los precios de toda la carta o de una categoría, y cargar uno a mano.</li>
    <li>El aviso de una plataforma: aparece cuando la carta cambió después de publicarla en esa tienda, o cuando todavía no se publicó desde Fornu. <b>Publicar en Rappi</b> le manda la carta de hoy.</li>
    <li><b>Precio base</b> y el precio de cada plataforma. Se cambian tocándolos, sin abrir el producto.</li>
    <li><b>Costo</b>, <b>Margen $</b> y <b>Margen %</b>: lo que cuesta la receta y lo que deja una unidad en el canal que menos deja.</li>
    <li>El menú <b>⋯</b>: receta, adicionales, grupos modificadores, duplicar y pausar.</li>
  </ol>
  <figcaption>La carta de Doble Smash en la demo, con lo que deja cada producto.</figcaption>
</figure>

La lista está agrupada por categoría. Debajo de cada nombre, en gris, dice cuántos insumos lleva la receta, cuántos adicionales tiene y en qué grupos modificadores está, como «5 insumos · Extras · Sumale una bebida». La etiqueta **Solo como opción** marca los productos que no se venden sueltos. Los productos pausados se ven más claros.

| Columna | Qué muestra |
|---|---|
| **Producto** | El nombre y, abajo, la receta, los adicionales y los grupos. |
| **Precio base** | Lo que se cobra en los pedidos propios y en cada plataforma que no tiene precio propio. |
| **Rappi**, **PedidosYa** | Una columna por plataforma prendida en la unidad de negocio. El precio se ve en gris cuando el producto no tiene precio propio ahí y usa el base. |
| **Costo** | Lo que cuesta la receta de una unidad, con centavos. «Sin receta» si todavía no tiene. |
| **Margen $** | Lo que deja una unidad en el canal que menos deja, ya restados la comisión del canal y los adicionales. Una raya si falta la receta o el precio. |
| **Margen %** | Ese mismo margen en porcentaje, con el nombre del canal abajo. En rojo si pierde plata, en ámbar si queda debajo del precio sugerido. Pasá el mouse para ver el motivo. |

El buscador encuentra productos por nombre o por categoría. Con el módulo Costos y márgenes, tocar el **Margen %** abre la ficha de costo del producto, con el reparto de cada canal, que se explica en [Costos y reportes]({{ '/es/projects/fornu/manual/costos-y-reportes/' | relative_url }}#ficha). Para eso hace falta el permiso **Costos**.

### Cambiar un precio en la lista {#precio-en-lista}

1. Tocá el precio que querés cambiar, en **Precio base** o en la columna de una plataforma. Se convierte en un campo.
2. Escribí el precio nuevo.
3. Apretá <kbd>Enter</kbd> o tocá afuera. Para dejarlo como estaba, apretá <kbd>Esc</kbd>.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-precio-en-lista.jpg' | relative_url }}" alt="La fila del Doble cheddar con el precio base recién cambiado a 9.900 pesos y, abajo a la izquierda, la confirmación «Doble cheddar: $ 9.900»." loading="lazy" width="1440" height="450">
  <ol class="marks">
    <li>El precio que se acaba de cambiar, ahí mismo en la lista.</li>
    <li>«Doble cheddar: $ 9.900»: la confirmación de Fornu.</li>
  </ol>
  <figcaption>Un precio cambiado sin abrir el producto.</figcaption>
</figure>

Solo se guarda un precio mayor que cero y distinto del que había. Si escribís un precio en la columna de una plataforma, el producto pasa a tener precio propio ahí. Hasta ese momento usaba el base.

### Cargar un producto nuevo {#nuevo-producto}

1. Tocá **Nuevo producto**.
2. Escribí el **Nombre** y elegí la **Categoría**. Si todavía no existe, tocá **+ Categoría nueva**, escribí el nombre y tocá **Crear**.
3. Escribí el **Precio base**: es el de los pedidos propios y el de cada plataforma sin precio propio.
4. Tocá **Guardar**, o apretá <kbd>Ctrl</kbd> + <kbd>Enter</kbd>.
5. El producto se vuelve a abrir en **Receta**, con el aviso «Doble cheddar ya está en la carta. Falta su receta: sin ella no hay costo, márgenes ni descuento de stock.» Agregá los insumos y guardá de nuevo.
{: .steps}

<div class="callout tip"><p class="callout-title">Consejo</p><p>Si la unidad de negocio tiene una sola categoría, ya viene elegida. Si no tiene ninguna, el producto se abre directo con el campo para crearla.</p></div>

## El producto por dentro {#ficha}

Todo lo de un producto está en un mismo panel, repartido en pestañas. Se abre tocando su fila, que empieza en **Datos**, o desde el menú **⋯**, que lo abre directo en **Receta**, **Adicionales** o **Grupos modificadores**. En la computadora aparece a la derecha y la lista sigue a la vista. En el celular sube desde abajo.

<p class="perm"><span>Quién puede:</span> <span class="tag">Carta</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-ficha.jpg' | relative_url }}" alt="El panel del Doble cheddar en la pestaña Datos, con las pestañas Precios, Receta, Adicionales y Grupos modificadores arriba y, al pie, el costo de 3.177,35 pesos y el margen de cada canal." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li>Las pestañas. El número dice cuántas líneas tiene la receta o cuántos grupos lleva. Si una pestaña tiene un problema, queda marcada.</li>
    <li><b>Código</b>: corto, para tipearlo en la caja en vez del nombre.</li>
    <li><b>Se vende suelto</b>: apagalo para lo que solo se pide dentro de otro producto.</li>
    <li>El pie: el costo y el margen en cada canal. Cambian mientras escribís, en cualquier pestaña.</li>
  </ol>
  <figcaption>El Doble cheddar de la demo, en la pestaña Datos.</figcaption>
</figure>

El pie acompaña todo lo que escribís: con la receta cargada muestra el **Costo** y el margen de **Propios**, de cada plataforma y del **Salón** si la unidad vende ahí, en rojo si un canal pierde y en ámbar si queda debajo del sugerido. Sin receta dice «Sin receta todavía: sin costo ni márgenes.» Si algo impide guardar, el pie lo dice con un link a la pestaña donde está.

### Datos {#ficha-datos}

| Campo | Para qué sirve |
|---|---|
| **Nombre** | Obligatorio. |
| **Código** | Hasta 10 letras y números, en mayúsculas, como 12 o PIZ3. Sirve para tipear el producto en la caja. No se repite dentro de la unidad de negocio. |
| **Categoría** | La sección de la carta. **+ Categoría nueva** la crea sin salir del producto. |
| **Precio base** | Aparece solo al cargar un producto nuevo. Después, los precios se cambian en **Precios** o en la lista. |
| **Descripción (opcional)** | Un texto corto sobre el producto. |
| **Orden** | En qué lugar aparece. Los números más bajos van primero. |
| **Activo** | Apagado, el producto queda pausado. |
| **Se vende suelto** | Apagado, el producto solo se ofrece dentro de sus grupos modificadores, como un extra de cheddar. No aparece suelto en las plataformas ni en los pedidos propios, y no tiene adicionales. |

### Precios {#ficha-precios}

- **Precio base**: el de los pedidos propios. Si queda en 0 y el producto se vende suelto, avisa «Se vendería gratis.»
- **Precio en Rappi** y **Precio en PedidosYa**: con **Propio** apagado, la plataforma cobra el precio base, que se ve en gris. Prendelo y escribí el precio de esa plataforma, que arranca en el base.
- **Ganancia sobre el costo**: cuánto deja el precio sugerido por encima de lo que cuesta. Con **Propia** apagado usa la de la cuenta, que se fija en [Ajustes › Configuración]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#configuracion). Prendido, ponés una solo para este producto.
- **Márgenes con estos precios**: una tabla con cada canal, su precio, lo que deja en pesos y en porcentaje, y el **Sugerido**. Cuando un precio queda debajo del sugerido aparece **Usar $ …**, que lo reemplaza por el sugerido redondeado para arriba a $ 10. Sin receta no hay costo, y la tabla pide cargarla.

### Receta {#ficha-receta}

Los insumos que lleva cada unidad vendida y en qué cantidad. Cada vez que se vende el producto, Fornu descuenta del stock lo que dice la receta.

1. Tocá **+ Agregar**.
2. Elegí el insumo. La lista los agrupa por categoría: primero los ingredientes, después la producción y al final el inventario.
3. Escribí la cantidad, en la unidad del insumo: gramos, mililitros o unidades. Al lado aparece lo que cuesta esa línea.
{: .steps}

Abajo se ve el costo de toda la receta. La ✕ quita una línea. Si un insumo todavía no existe, **+ Nuevo insumo** abre su carga sin salir del producto: elegís si es un ingrediente, una elaboración o un artículo de inventario, y al guardarlo entra a la receta con cantidad 1. Ese botón aparece si tu rol tiene también el permiso **Insumos**.

<div class="callout tip"><p class="callout-title">Consejo</p><p>La caja o la bolsa del producto van en <b>Adicionales</b>, no en la receta. Así el envase puede ser distinto en el delivery y en el salón.</p></div>

### Adicionales {#ficha-adicionales}

Lo que lleva cada unidad del producto además de su receta, en todos los canales o en uno: su caja, un sobre de salsa en el delivery. Se descuenta del stock con cada unidad vendida y cuenta en sus márgenes.

Cada línea tiene **Canal** (**Todos**, **Propios**, cada plataforma prendida y **Salón** si la unidad vende en el salón), **Insumo**, **Cantidad** y su **Costo**. **+ Adicional** suma una línea. Lo que llevan todos los productos de la unidad de negocio, o cada pedido entero, se carga una sola vez en los adicionales de la unidad de negocio, en [Ajustes]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#unidades).

Esta pestaña aparece mientras **Se vende suelto** está prendido.

### Grupos modificadores {#ficha-grupos}

Tildá los grupos que se ofrecen al pedir este producto, como sus extras o la bebida del combo. Cada tarjeta dice cuántas opciones se eligen, por ejemplo «Opcional, hasta 3». Un grupo que tiene a este mismo producto entre sus opciones aparece apagado. Los grupos se arman en [Grupos modificadores](#modificadores).

### Lo que no deja guardar {#ficha-errores}

**Guardar** queda apagado mientras falte algo, y el pie dice qué:

- «Falta el nombre.»
- «Elegí la categoría.»
- «Falta el precio: se vendería a $ 0.», si el producto está activo y se vende suelto.
- «Elegí el insumo de cada línea de la receta.» o «Hay una línea de la receta sin cantidad.»
- «Hay un adicional sin cantidad.» o «Hay un adicional repetido.»

## Duplicar, pausar y reactivar {#pausar}

Todo esto está en el menú **⋯** de cada producto.

<p class="perm"><span>Quién puede:</span> <span class="tag">Carta</span></p>

- **Duplicar** crea «Doble cheddar (copia)» con la misma receta, los mismos adicionales, precios, ganancia y grupos. La copia nace pausada, para que la revises antes de venderla, y se abre en **Datos** para que le cambies el nombre.
- **Pausar** saca el producto de la venta. Fornu avisa «Doble cheddar pausado. Publicá la carta para que las plataformas lo vean.» y ofrece **Deshacer** por si fue sin querer.
- **Reactivar** lo vuelve a la carta: «Doble cheddar vuelve a la carta».

Los productos no se borran. Pausar los saca de la venta y conserva sus ventas y su historia.

<div class="callout"><p class="callout-title">Importante</p><p>Un precio nuevo o un producto pausado llegan a una plataforma cuando se publica la carta en esa tienda. Si quedó algo sin publicar, el aviso de arriba de la lista lo dice y trae el botón para publicar.</p></div>

## Cambiar muchos precios a la vez {#precios}

Cuando sube todo, no hace falta tocar producto por producto. **Actualizar precios** sube o baja un porcentaje a toda la carta o a una categoría. **Cambiar precios** cambia solo los productos que tildes, por porcentaje o por monto, y en el canal que elijas.

<p class="perm"><span>Quién puede:</span> <span class="tag">Carta</span></p>

### Actualizar los precios de toda la carta o de una categoría {#actualizar-precios}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-actualizar-precios.jpg' | relative_url }}" alt="El panel Actualizar precios con toda la carta, 10 por ciento y redondeo a 50 pesos, las dos casillas tildadas y una vista previa de siete productos con su precio de ahora y el que queda." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li><b>Qué productos</b>: <b>Toda la carta</b> o una categoría.</li>
    <li><b>Cuánto (%)</b>: 10 sube un 10%. Con un número negativo baja: -5 baja un 5%.</li>
    <li><b>Redondeo</b>: sin redondeo, o a $ 1, $ 10, $ 50, $ 100, $ 500 o $ 1.000. Arranca en $ 50.</li>
    <li>Las dos casillas: cambiar también el precio propio de cada plataforma y el precio del producto dentro de los grupos modificadores.</li>
    <li>La vista previa: cómo queda cada precio base. Muestra los primeros ocho y cuenta el resto.</li>
    <li><b>Actualizar 7 productos</b>: aplica el cambio.</li>
  </ol>
  <figcaption>Un aumento del 10% para toda la carta de Doble Smash.</figcaption>
</figure>

1. Tocá **Actualizar precios**.
2. Elegí qué productos, el porcentaje y el redondeo. El porcentaje va de -90% a 500%.
3. Revisá la vista previa y tocá **Actualizar N productos**.
{: .steps}

Si el cambio es grande, de 30% o más para arriba o de 20% o más para abajo, Fornu pregunta antes, por ejemplo «¿Subir un 30% el precio de 12 productos?», y hay que confirmar con **Subir 30%**. Al terminar avisa cuántos productos y opciones cambió, y recuerda publicar la carta para que las plataformas vean los precios nuevos. Un precio en 0 queda en 0.

### Cambiar el precio de los productos tildados {#cambiar-precios}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-cambiar-precios.jpg' | relative_url }}" alt="Dos productos tildados en la lista y, a la derecha, el panel Cambiar el precio de 2 productos con porcentaje, 10, redondeo a 10 pesos, todos los precios y una tabla con el antes y el después de cada producto en cada canal." loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li>La barra de la selección: cuántos productos tildaste, <b>Cambiar precios</b> y <b>Quitar la selección</b>.</li>
    <li><b>Cómo</b>: <b>Porcentaje</b> o <b>Monto</b>.</li>
    <li><b>Cuánto</b>: 12 sube un 12% y -5 baja un 5%. En monto, 500 suma $ 500 a cada precio y -200 le resta $ 200.</li>
    <li><b>En qué canal</b>: <b>Todos los precios</b>, solo <b>Pedidos propios</b> o una plataforma.</li>
    <li>La vista previa, precio por precio y canal por canal. Lo que no cambia se ve más claro.</li>
    <li><b>Aplicar</b>: guarda los precios nuevos.</li>
  </ol>
  <figcaption>Un 10% más para dos hamburguesas, en todos sus canales.</figcaption>
</figure>

1. Tildá los productos en la lista. La casilla del título tilda todos los que se ven.
2. Tocá **Cambiar precios**, en la barra que aparece arriba.
3. Elegí cómo, cuánto, el redondeo (al centavo, o a $ 1, $ 10, $ 50 o $ 100) y el canal. Esperá la vista previa.
4. Tocá **Aplicar**. Fornu confirma «Precios cambiados».
{: .steps}

En pedidos propios cambia el precio base. En una plataforma cambia su precio propio, y el producto que no tenía precio propio ahí pasa a tenerlo.

### Arreglar un precio que pierde plata {#arreglar-precio}

Cuando un producto pierde plata o queda debajo del sugerido en algún canal, Fornu lo marca en [Costos › Para revisar]({{ '/es/projects/fornu/manual/costos-y-reportes/' | relative_url }}#revisar), y también en el recuadro que aparece después de una compra que movió costos ([Compras y gastos]({{ '/es/projects/fornu/manual/compras-y-gastos/' | relative_url }}#margenes)). Desde los dos lugares, **Revisar precio** abre el producto en **Precios**, listo para corregir:

- Arriba, un aviso dice qué pasa, por ejemplo «Pierde $ … por unidad en Rappi · $ … debajo del sugerido en Pedidos propios».
- En la tabla de márgenes se escribe el precio de cada canal ahí mismo, y el margen se recalcula al escribir.
- Cuando todo queda bien, el aviso cambia a «Con estos precios ningún canal pierde plata ni queda debajo del sugerido. Guardá para dejarlo así.»
- Al cerrar volvés a la pantalla de donde viniste.

## Categorías de la carta {#categorias}

Son las secciones de la carta de cada unidad de negocio, como Burgers o Bebidas. Están en una segunda lista, debajo de los productos, en la misma pantalla. También se crean desde un producto nuevo, con **+ Categoría nueva**.

<p class="perm"><span>Quién puede:</span> <span class="tag">Carta</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-categorias.jpg' | relative_url }}" alt="La lista Categorías con Burgers, Para acompañar y Extras, cuándo va cada una, cuántos productos tiene y su orden, y el botón Agregar." loading="lazy" width="1384" height="276">
  <ol class="marks">
    <li><b>Agregar</b>: una categoría nueva.</li>
    <li><b>Va de</b>: cuándo sale lo de esa categoría en el salón.</li>
    <li><b>Orden</b>: en qué lugar aparece en la carta.</li>
  </ol>
  <figcaption>Las tres categorías de Doble Smash en la demo.</figcaption>
</figure>

Tocá **Agregar**, o una categoría para cambiarla:

| Campo | Para qué sirve |
|---|---|
| **Nombre** | El título de la sección. |
| **Orden** | El lugar de la sección. Una nueva va al final. |
| **Va de** | **Principal**, **Ya**, **Entrada** o **Postre**. En el salón dice cuándo sale lo de esta categoría: las bebidas ya, los postres al final. Lo que viene después espera en la cocina hasta que el mozo lo marcha. Fuera del salón no cambia nada. |
| **Notas rápidas** | Una por línea, como «Jugoso», «A punto» y «Cocido». Al cargar un producto de esta categoría se tocan en vez de escribirlas. Hasta 12 notas de 40 letras. |
| **Color** | El de su baldosa y sus productos en el mostrador express. Sin elegir, usa el de la unidad de negocio. |

Cómo se marchan los tiempos y dónde aparecen las notas rápidas está en [Salón]({{ '/es/projects/fornu/manual/salon/' | relative_url }}#tiempos).

Para borrar una categoría, abrila y tocá **Borrar**. Si todavía tiene productos, Fornu no la borra y pide moverlos a otra categoría o pausarlos antes.

## Grupos modificadores {#modificadores}

Son las elecciones que se hacen al pedir: los «Extras» de una hamburguesa o «Elegí tu bebida» en un combo. Cada grupo se arma con productos de la carta, cada uno con lo que suma dentro del grupo y cuántas unidades entran.

Están en Carta › **Grupos modificadores** (la pestaña dice **Modificadores**), con las mismas pestañas por unidad de negocio que los productos.

<p class="perm"><span>Quién puede:</span> <span class="tag">Carta</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-modificadores.jpg' | relative_url }}" alt="La lista de grupos modificadores de Doble Smash: Extras, opcional hasta 3, con cheddar, panceta y cebolla caramelizada, y Sumale una bebida, opcional hasta 1, con la gaseosa. Los dos los llevan el Doble cheddar y el Triple bacon." loading="lazy" width="1440" height="450">
  <ol class="marks">
    <li><b>Nuevo grupo</b>.</li>
    <li><b>Se eligen</b>: la regla del grupo. «Opcional, hasta 3» deja elegir de ninguna a tres opciones.</li>
    <li><b>Productos</b>: las opciones, con lo que suma cada una («+$ 1.500», o «sin cargo») y cuántas entran de cada una («hasta 2»).</li>
    <li><b>Lo llevan</b>: los productos que ofrecen este grupo.</li>
  </ol>
  <figcaption>Los dos grupos de Doble Smash en la demo.</figcaption>
</figure>

### Armar un grupo {#armar-grupo}

1. Tocá **Nuevo grupo**.
2. Escribí el **Nombre**, como «Extras».
3. Poné el **Mínimo a elegir** y el **Máximo a elegir**. Abajo se lee la regla que queda: «Opcional, hasta 3», «Elegir 1» o «De 1 a 2».
4. Tocá **+ Agregar producto** por cada opción, y ajustá **Hasta** y **Precio**.
5. Tocá **Guardar**.
6. Abrí cada producto que lleva el grupo y tildalo en su pestaña **Grupos modificadores**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-grupo.jpg' | relative_url }}" alt="El panel del grupo Extras con mínimo 0 y máximo 3, y tres productos: cheddar y panceta hasta 2, cebolla caramelizada hasta 1, cada uno con su precio y su costo." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li><b>Mínimo a elegir</b> y <b>Máximo a elegir</b>. Un mínimo de 0 lo hace opcional. Cuentan unidades: dos del mismo son dos.</li>
    <li><b>Producto</b>: cada opción es un producto de la carta. Los que no se venden sueltos dicen «(solo como opción)».</li>
    <li><b>Hasta</b> y <b>Precio</b>: cuántas unidades de esa opción entran, de 1 a 20, y lo que suma cada una. El precio arranca en el del producto y se puede cambiar. En 0 es sin cargo.</li>
    <li><b>+ Agregar producto</b>: suma una opción. Propone primero los productos que solo se venden como opción.</li>
    <li><b>Borrar</b>: el grupo deja de ofrecerse en los productos que lo llevaban.</li>
  </ol>
  <figcaption>El grupo Extras de la demo, abierto para cambiarlo.</figcaption>
</figure>

El mínimo no puede pasar al máximo, y el máximo es al menos 1. Si la unidad de negocio todavía no tiene productos, el grupo pide cargarlos primero en Productos.

<div class="callout tip"><p class="callout-title">Consejo</p><p>Un extra como el cheddar se carga primero en Productos con <b>Se vende suelto</b> apagado. Así no aparece suelto en ninguna carta, y tiene su propia receta: cuando alguien lo elige, Fornu descuenta del stock lo que lleva.</p></div>

Un producto que lleva un grupo no puede ser una de sus opciones.

## Importar desde una planilla {#importar}

Para cargar o cambiar muchos productos, insumos o recetas de una vez desde Excel o Google Sheets. Antes de guardar, Fornu muestra qué va a pasar con cada fila, y nada se guarda hasta que confirmás.

| Desde | Se abre en | Pide el permiso |
|---|---|---|
| Carta › Productos › **Importar planilla** | **Carta**, con la pestaña **Recetas** al lado | Carta |
| Insumos › Ingredientes o Inventario › **Importar planilla** | **Insumos**, con la pestaña **Recetas** al lado | Insumos |
| Insumos › Producción › **Importar planilla** | **Recetas** | Insumos |
| Inicio, en los primeros pasos: «Importarla de una planilla» o «Importarlos de una planilla» | La carta o los ingredientes | Carta o Insumos |

Las recetas de los productos piden el permiso **Carta**, y las de las elaboraciones, **Insumos**.

<p class="perm"><span>Quién puede:</span> <span class="tag">Carta</span> <span class="tag">Insumos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-importar.jpg' | relative_url }}" alt="El panel Importar desde una planilla en la pestaña Insumos, con los botones Descargar la planilla y Elegir archivo, el recuadro para pegar las filas y la explicación de cada columna." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li>Las pestañas: qué planilla vas a cargar.</li>
    <li><b>Descargar la planilla</b> y <b>Elegir archivo</b>.</li>
    <li><b>O pegá las filas</b>: copiá las filas de la planilla, con los títulos, y pegalas acá.</li>
    <li><b>Las columnas</b>: cuáles entiende Fornu y qué pasa si una celda queda vacía.</li>
    <li><b>Revisar</b>: arma la vista previa. Si pegás varias filas, aparece sola.</li>
  </ol>
  <figcaption>La importación de insumos, antes de cargar la planilla.</figcaption>
</figure>

1. Tocá **Descargar la planilla**. Baja un archivo con lo que ya tenés cargado, o con filas de ejemplo si todavía no cargaste nada.
2. Abrilo en Excel o Google Sheets. Cambiá lo que quieras y agregá filas.
3. Volvé a Fornu y tocá **Elegir archivo**. O seleccioná en la planilla las filas con sus títulos, copialas con <kbd>Ctrl</kbd> + <kbd>C</kbd> y pegalas en **O pegá las filas** con <kbd>Ctrl</kbd> + <kbd>V</kbd>.
4. Leé la vista previa. Tocá un contador para ver solo esas filas.
5. Tocá **Importar N filas**, o apretá <kbd>Ctrl</kbd> + <kbd>Enter</kbd>.
{: .steps}

Fornu avisa cuántos quedaron nuevos y cuántos se actualizaron, y la lista se recarga.

Lee archivos .xlsx (la primera hoja), .csv, .tsv y .txt de hasta 4 MB, y hasta 3.000 filas por vez. Un Excel viejo (.xls) no se lee: guardalo como .xlsx, o copiá las filas y pegalas.

La primera fila nombra las columnas. El orden no importa, y las columnas que Fornu no conoce se ignoran. La vista previa dice cuáles quedaron afuera. Los títulos se reconocen aunque no sean exactos: «rubro», «costo», «pvp», «presentación» o «alícuota» también sirven. Si la columna del precio se llama «con IVA» o «sin IVA», eso vale para toda la columna.

### La planilla de la carta {#planilla-carta}

| Columna | Qué va |
|---|---|
| **Unidad de negocio** | Hace falta si la cuenta tiene más de una. |
| **Categoría** | Si no existe, se crea. |
| **Producto** | Si ya existe en esa unidad de negocio, se actualiza. |
| **Descripción** | El texto del producto. |
| **Precio** | El precio base. |

### La planilla de insumos {#planilla-insumos}

Sirve para los ingredientes y los artículos de inventario. Las elaboraciones se crean en Producción, y su receta va en la planilla de recetas.

| Columna | Qué va |
|---|---|
| **Nombre** | Si ya existe, se actualiza con lo que diga la fila. Una celda vacía deja el dato como está. |
| **Categoría** | La que no existe se crea, en Ingredientes. |
| **Unidad** | kg, g, l, ml o unidad. **Cuánto trae** y el mínimo van en esa unidad. |
| **Se compra por** | Bolsa, caja, maple… Vacía: por kg, l o unidad. |
| **Cuánto trae** | Lo que trae cada una. Vacía: 1. |
| **Precio** | De cada una, como figura en la factura o el ticket. |
| **IVA** | 21, 10,5, 27… Vacía: 21. |
| **El precio es** | «con IVA» o «sin IVA». |
| **Stock mínimo** | Debajo de esto, avisa. |

### La planilla de recetas {#planilla-recetas}

| Columna | Qué va |
|---|---|
| **Unidad de negocio** | Solo si hay productos con el mismo nombre en más de una. |
| **Producto o elaboración** | A quién es la receta. Va una fila por cada insumo que lleva, y las filas reemplazan la receta que tenía. |
| **Insumo** | Tiene que existir ya. |
| **Cantidad** | Por unidad vendida, o por tanda si es una elaboración. |
| **Unidad** | Vacía: la del insumo. |

<div class="callout"><p class="callout-title">Importante</p><p>En la planilla de recetas, una fila con error deja afuera toda esa receta, para no guardarla a medias. Corregí la fila y volvé a cargar.</p></div>

### Leer la vista previa {#vista-previa}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/carta-importar-revisar.jpg' | relative_url }}" alt="La vista previa de una planilla de recetas: la receta del Doble cheddar cambia y una fila da error porque no existe el producto. Al pie, el botón Importar 1 fila." loading="lazy" width="880" height="494">
  <ol class="marks">
    <li>Los contadores: <b>nuevos</b>, <b>cambian</b>, <b>sin cambios</b> y <b>con error</b>. Tocá uno para ver solo esas filas.</li>
    <li><b>Qué pasa</b> con cada fila: <b>Nuevo</b>, <b>Cambia</b>, <b>Igual</b> o <b>Error</b>.</li>
    <li><b>Detalle</b>: qué se va a guardar, o por qué la fila no entra.</li>
    <li>Las filas con error quedan afuera: se corrigen en la planilla y se vuelve a cargar.</li>
    <li><b>Importar 1 fila</b>: guarda las que están bien.</li>
  </ol>
  <figcaption>Una receta que cambia y una fila con error.</figcaption>
</figure>

Arriba también dice qué categorías se van a crear. Algunos motivos que pueden aparecer en **Detalle**:

| Mensaje | Qué hacer |
|---|---|
| «Falta la unidad: kg, g, l, ml o unidad.» | Completá la columna **Unidad**. |
| «No hay un insumo llamado …» | Cargá el insumo antes, o corregí el nombre. |
| «Ya está en la fila 4: va una sola vez.» | Dejá una sola fila para ese nombre. |
| «Falta la unidad de negocio: hay 2, …» | Agregá la columna **Unidad de negocio**. |
| «Está en g: la unidad no se cambia…» | La unidad de un insumo queda fija. Usá la que tiene. |
| «Es una elaboración: su receta va en la planilla de recetas, y lo demás en su ficha.» | Las elaboraciones se cambian en Producción. |
| «Ya está así.» | La fila no cambia nada. |
| «Ojo: pasa de $ … a $ …» | El precio cambia mucho (más del triple, o menos de un tercio). Revisá que sea el precio de cada presentación. |
