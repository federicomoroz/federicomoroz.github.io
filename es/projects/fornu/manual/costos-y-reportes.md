---
layout: manual
manual: costos-y-reportes
title: "Costos y reportes · Manual de Fornu"
description: "Qué revisar en precios y recetas, la ficha de cada producto e insumo, el margen en cada canal y cómo se calcula, las estadísticas de la carta, el resumen de ventas y la rentabilidad."
permalink: /es/projects/fornu/manual/costos-y-reportes/
---

Costos y Reportes son dos módulos de la cuenta, con su grupo cada uno. **Costos** mira la carta: cuánto cuesta cada producto y cuánto deja en cada canal, venda o no venda. **Reportes** mira lo que pasó: cuánto se vendió y cuánto quedó. En el celular, Costos está dentro de **Más** y Reportes en la barra de abajo. Si la cuenta no tiene un módulo prendido, su grupo no aparece.

## Para revisar {#revisar}

Es la lista de lo que conviene mirar en costos y precios: un ingrediente sin precio, un producto que en Rappi pierde plata, un precio que no se toca hace meses. Primero lo que está mal, después lo que vale la pena revisar. Es el lugar para arrancar cuando cambian los precios de los proveedores.

<p class="perm"><span>Quién puede:</span> <span class="tag">Costos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/costos-revisar.jpg' | relative_url }}" alt="Para revisar con un problema y un aviso: el Doble cheddar pierde 720,35 pesos por unidad en Rappi y el Triple bacon queda debajo del sugerido en Rappi, cada uno con Ficha y Corregir" loading="lazy" width="1440" height="620">
  <ol class="marks">
    <li><b>Problemas</b>: números mal o que faltan.</li>
    <li><b>Avisos</b>: números bien, pero para mirar.</li>
    <li><b>Recordatorios</b>: precios viejos y notas.</li>
    <li>Lo que pasa, por ejemplo «Pierde $ 720,35 por unidad en Rappi».</li>
    <li><b>Corregir</b>: abre justo lo que hay que arreglar.</li>
  </ol>
  <figcaption>Un precio que en Rappi pierde plata.</figcaption>
</figure>

Tocar una cifra filtra la lista. Arriba también están **Todo** / **Problemas** / **Avisos** / **Recordatorios** y el buscador **Buscar producto o insumo…**.

Cada fila dice el nombre y, abajo, la unidad de negocio o qué es (**Ingrediente**, **Elaboración**, **Inventario** o **Unidad de negocio**). Al lado, lo que pasa, y dos botones: **Ficha**, que abre la [ficha](#ficha), y **Corregir**, que abre justo el formulario para arreglarlo: la receta o los precios del producto en Carta, el insumo en Insumos o los adicionales de la unidad en Unidades de negocio.

| Nivel | Lo que dice | Qué pasa |
|---|---|---|
| Problema | «Falta el precio» | Un insumo que se compra no tiene precio. |
| Problema | «Sin receta» | Una elaboración, o un producto activo, no tiene receta. |
| Problema | «Harina no tiene precio» | Una elaboración usa un insumo sin precio. |
| Problema | «Sin precio» | Un producto de la carta tiene precio 0. |
| Problema | «Pierde $X por unidad en Rappi» | El margen en ese canal es negativo. |
| Aviso | «$X debajo del sugerido en Rappi» | Deja plata, pero menos de lo que debería. |
| Aviso | «Lleva Cheddar, que está desactivado» | Usa un insumo apagado, en la receta o en sus adicionales. |
| Recordatorio | «Precio de hace N días» o «Precio sin fecha» | El precio pasó el plazo de Ajustes › Configuración, **Un precio es viejo a los (días)**. |
| Recordatorio | «Tiene una nota» | El insumo tiene una nota. |

Si pasa en varios canales, va en una sola línea: «Pierde $ 620 por unidad en Rappi, $ 410 en PedidosYa».

### Corregir un problema

1. Tocá la cifra **Problemas**.
2. En la fila, tocá **Corregir**. Se abre el formulario justo.
3. Cargá lo que falta y guardá. Cuando el número queda bien, deja de aparecer en la lista.
{: .steps}

Hay dos lugares más que avisan: arriba, Costos muestra un número con los problemas para revisar, y en Inicio, **Para atender** dice «N problemas de precios o recetas para revisar». Los dos cuentan solo los problemas, no los avisos ni los recordatorios.

## Ficha {#ficha}

Es todo lo de un producto o un insumo en una pantalla: lo que cuesta, lo que deja en cada canal, de qué está hecho y dónde se usa. Sirve para entender un número antes de cambiar un precio.

<p class="perm"><span>Quién puede:</span> <span class="tag">Costos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/costos-ficha.jpg' | relative_url }}" alt="Ficha del Doble cheddar de Doble Smash: costo de la receta 3.177,35 pesos, 35% de ganancia sobre el costo, margen más bajo 45,9% en Rappi, la tabla de precios por canal y una barra por canal" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li><b>Producto</b> / <b>Insumo</b>, y cuál ver.</li>
    <li>El nombre, la unidad y la categoría, y lo que haya para revisar. Acá, «Sin nada para revisar».</li>
    <li><b>Editar producto</b> y <b>Receta</b>: para cambiarlo sin salir a buscarlo.</li>
    <li>Las cifras: costo, ganancia sobre el costo, el margen más bajo y en cuántos canales está debajo del sugerido.</li>
    <li><b>Precios por canal</b>: precio, lo que se queda el canal, adicionales, margen y precio sugerido.</li>
    <li>Cómo se reparte el precio en cada canal.</li>
  </ol>
  <figcaption>La ficha de un producto de la demo.</figcaption>
</figure>

### La ficha de un producto

- **Costo de la receta**, o «Sin receta» si no tiene.
- **Ganancia sobre el costo**: la propia del producto o «la de la cuenta».
- **Margen más bajo**, con el canal donde pasa.
- **Debajo del sugerido**: en cuántos canales.
- **Precios por canal**: una fila por canal con **Precio**, **Se queda el canal**, **Adicionales**, **Margen** ($ y %) y **Sugerido**. Debajo, una barra por canal partida en **Receta**, **Adicionales**, **Se queda el canal**, IVA (si la cuenta es responsable inscripto) y **Margen** o **Pérdida**.
- **Receta**: cada insumo con su cantidad, su costo y qué parte del costo es. Tocá uno para abrir su ficha.
- **Adicionales**: lo que va con el producto además de la receta (la caja, la bolsa), por canal, y si va con cada unidad, una vez por pedido o es propio del producto.

En el selector aparecen los productos que se venden solos, agrupados por unidad de negocio. Los insumos van por categoría.

### La ficha de un insumo

- Arriba, el grupo, la categoría y el proveedor, su nota y lo que haya para revisar, con **Editar insumo**.
- Si se compra: **Precio por** la unidad en que se compra (exento, con IVA 21% o sin IVA 21%), **Costo utilizable** (lo que cuesta lo que se usa de verdad, con cuánto rinde), **Precio desde** (hoy o hace N días) y **Último cambio**.
- Si se elabora: **Costo de la tanda**, **Costo utilizable**, **Se usa en** (en cuántos lugares) y la **Receta de la tanda**.
- **Se usa en**: cada producto, elaboración o adicional que lo lleva, con la cantidad, el costo y qué parte de esa receta es.
- **Historial de precios** (si se compra): los últimos 60 cambios con la fecha, el precio, el IVA, cuánto cambió, de dónde vino (**Alta**, **Editado**, **Compra**, **Compra en Stock**, **Cambio masivo**, **Compra anulada**) y quién lo hizo.

<div class="callout tip"><p class="callout-title">Consejo</p><p>Cuando un proveedor sube un precio, abrí la ficha del insumo y mirá <b>Se usa en</b>: ahí están todos los productos que cambian de margen. Desde Carta también se llega: el margen de cada producto lleva a su ficha.</p></div>

## Márgenes por canal {#margenes}

Es la carta entera de una unidad de negocio con lo que deja cada producto en cada canal. De un vistazo se ve qué está barato en Rappi, qué quedó debajo del sugerido y qué no tiene receta.

La pestaña dice **Márgenes** y el título, **Márgenes por canal**.

<p class="perm"><span>Quién puede:</span> <span class="tag">Costos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/costos-margenes.jpg' | relative_url }}" alt="Márgenes de Doble Smash: una columna por canal con la comisión de cada uno, y por producto el precio, el margen en pesos y porcentaje y los adicionales" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li>Una pestaña por unidad de negocio.</li>
    <li><b>¿Cómo se calcula?</b>: la cuenta, explicada.</li>
    <li>Cada canal con lo que se queda: «comisión 25%».</li>
    <li>Una celda: precio, margen en pesos y en %, y adicionales. Tocala para ver la cuenta.</li>
  </ol>
  <figcaption>Los márgenes de Doble Smash, en la demo.</figcaption>
</figure>

La tabla tiene **Producto**, **Costo** («Sin receta» si falta) y una columna por cada canal donde vende la unidad. Cada canal dice lo que se queda: «comisión X%», más «$Y por unidad» si cobra un fijo. Los productos van por categoría y los inactivos aparecen más claros.

Cada celda muestra el precio, el margen («$ 5.279,65 · 45,9%»), «adicionales $X» y, si el precio está por debajo del sugerido, «sugerido $X» en naranja. Al tocar una celda (o al pasar el mouse) se abre la cuenta entera, «Doble cheddar en Rappi»:

| Línea | Ejemplo: Doble cheddar en Rappi |
|---|---|
| **Precio** | $ 11.500 |
| **Se queda el canal** | −$ 2.875 (el 25% de $ 11.500) |
| **Receta** | −$ 3.177,35 |
| **Adicionales** | −$ 168 |
| **Margen** | $ 5.279,65 (45,9%) |
| **Sugerido** | $ 5.943,24, con 35% sobre el costo |

La cuenta de la demo es monotributo. En una cuenta responsable inscripto aparece además la línea **Sin IVA**, debajo del precio. En el celular cada celda muestra solo el precio y el %, y el resto está a un toque.

### Cómo se calcula el margen

**¿Cómo se calcula?** lo resume: «Precio sin IVA (21%), menos lo que se queda el canal, el costo de la receta y los adicionales: lo que lleva cada unidad, más su parte de lo que lleva cada pedido. En naranja, los precios por debajo del sugerido. Tocá un margen para ver la cuenta.» En una cuenta monotributo empieza por «Precio completo (sin IVA de venta, como monotributo)».

- **Margen** = precio sin IVA − lo que se queda el canal − receta − adicionales.
- **Lo que se queda el canal** es su comisión sobre el precio completo, el que paga el cliente con IVA, más el fijo por unidad si lo tiene. La comisión y el fijo de cada canal se cargan en Ajustes › Unidades de negocio.
- **Adicionales** son lo que lleva cada unidad (la caja de la hamburguesa) más la parte de lo que lleva cada pedido (la bolsa, el sticker), repartido entre los productos de un pedido promedio de ese canal.
- El **%** del margen es sobre el precio sin IVA.

En una cuenta responsable inscripto, el mismo Doble cheddar a $ 11.500 en Rappi quedaría así: sin IVA son $ 9.504,13, el canal se queda $ 2.875 (el 25% del precio con IVA), y el margen es $ 9.504,13 − $ 2.875 − $ 3.177,35 − $ 168 = $ 3.283,78, un 34,6%.

### Cómo se calcula el precio sugerido

El sugerido es el precio que deja la ganancia buscada después de pagar todo. Se arma así: el costo de la receta más la **Ganancia sobre el costo**, más los adicionales y el fijo del canal, y eso llevado a un precio que, después del IVA y la comisión, deje justo ese monto.

Para el Doble cheddar en Rappi: $ 3.177,35 más el 35% son $ 4.289,42. Con los $ 168 de adicionales, $ 4.457,42. Como Rappi se queda el 25%, el precio tiene que ser $ 4.457,42 ÷ 0,75 = $ 5.943,24. En Pedidos propios, sin comisión, el sugerido es $ 4.457,43.

La ganancia sobre el costo es la del producto si tiene una propia, o la de Ajustes › Configuración, **Ganancia sobre el costo (%)**: «Lo que el precio sugerido le suma al costo de cada producto, si no tiene una propia.»

## Estadísticas {#estadisticas}

Es lo que dicen los márgenes de toda la carta junta: cuánto dejan en promedio, qué productos dejan más y menos, cómo se reparte cada precio y cómo se movieron los precios de los insumos. Sirve para revisar la carta entera de una vez, por ejemplo antes de una actualización de precios.

<p class="perm"><span>Quién puede:</span> <span class="tag">Costos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/costos-estadisticas.jpg' | relative_url }}" alt="Estadísticas de toda la carta: margen promedio 52,9%, 33 precios para leer, ninguno debajo del sugerido, el gráfico de margen por producto, la dona de cómo están los precios y las barras de cómo se reparte el precio por canal" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li>Qué mirar: todas las unidades o una, y todos los canales o uno.</li>
    <li>Las cifras de la carta.</li>
    <li><b>Margen por producto</b>, del que más deja al que menos.</li>
    <li><b>Cómo están los precios</b>: bien, debajo del sugerido, perdiendo plata o sin precio o receta.</li>
    <li><b>Cómo se reparte el precio</b>, en promedio, en cada canal.</li>
  </ol>
  <figcaption>Las estadísticas de las cuatro marcas de la demo juntas.</figcaption>
</figure>

**Cifras**: **Margen promedio**, **Deja por unidad** (en promedio), **Precios para leer** (cuántos tienen todo para calcular, de cuántos), **Debajo del sugerido**, **Pierden plata** y **Sin precio o receta**.

**Gráficos**:

- **Margen por producto**.
- **Cómo están los precios**: **Bien**, **Debajo del sugerido**, **Pierden plata** y **Sin precio o receta**.
- **Cómo se reparte el precio**: promedio por canal.
- **Contra el precio sugerido**: cuánto más o menos que el sugerido está cada precio.
- **Margen por categoría**.
- **Precios de los insumos, mes a mes**: el cambio promedio de los insumos que cambiaron de precio, en los últimos 12 meses.

**Listas de cinco**, que al tocar una fila abren su ficha: **Los que más dejan**, **Los que menos dejan**, **Más debajo del sugerido**, **Insumos que más subieron** e **Insumos que más se usan**.

<div class="callout"><p class="callout-title">Importante</p><p>Los promedios son simples: cada producto en cada canal cuenta lo mismo, se haya vendido mucho o poco. Solo entran las unidades activas y los productos que están en la carta. Para lo que dejó lo que se vendió de verdad, mirá <a href="#rentabilidad">Rentabilidad</a>.</p></div>

## Resumen de ventas {#resumen}

Es cómo te fue en un período comparado con el anterior del mismo largo: cuánto se vendió, qué días y a qué hora, por qué canales y qué marcas, y qué es lo que más sale.

La pestaña dice **Resumen** y el título, **Resumen de ventas**.

<p class="perm"><span>Quién puede:</span> <span class="tag">Reportes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/reportes-resumen.jpg' | relative_url }}" alt="Resumen de ventas de la semana pasada comparada con la anterior: 2.911.600 pesos, 165 pedidos, ticket promedio, venta por día y cancelados, cada uno con su variación, y el gráfico de ventas y pedidos por día" loading="lazy" width="1440" height="808">
  <ol class="marks">
    <li>El período. Arranca en <b>Últimos 7 días</b>.</li>
    <li>Contra qué se compara: los mismos días, justo antes.</li>
    <li>Las cifras, cada una con su variación.</li>
    <li><b>Evolución de las ventas</b>: las barras son las ventas de cada día y la línea, los pedidos.</li>
  </ol>
  <figcaption>Una semana de la demo contra la anterior.</figcaption>
</figure>

**Cifras**: **Ventas**, **Pedidos**, **Ticket promedio**, **Venta por día** (el total dividido por los días del período) y **Cancelados** (cuántos y por cuánto). Cada una dice cuánto cambió: «↑ +3,1 % vs. período anterior». Verde es buena noticia y rojo, mala. En **Cancelados**, bajar es bueno, por eso un −30% sale en verde. Si no hubo nada antes, dice «Sin datos del período anterior».

Más abajo, los gráficos:

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/reportes-resumen-graficos.jpg' | relative_url }}" alt="Gráficos del resumen: ventas por día de la semana, ventas por hora con dos picos al mediodía y a la noche, canales, unidades de negocio y los diez productos más vendidos" loading="lazy" width="1440" height="1000">
  <figcaption>Qué días, a qué hora, por dónde y qué se vende más.</figcaption>
</figure>

- **Por día de la semana**: qué días se vende más.
- **Por hora**: a qué hora entran los pedidos, en la hora de la cocina.
- **Canales**: cuánto entró por cada canal, con su parte y sus pedidos.
- **Unidades de negocio**: lo que vendió cada marca.
- **Lo más vendido**: los diez productos con más unidades, con cuántas y por cuánto.

Una venta, acá, es cualquier pedido confirmado que no se canceló, también los que todavía se están preparando. Las ventas van con IVA. El período puede ser de hasta un año.

## Rentabilidad {#rentabilidad}

Es lo que quedó de verdad: las ventas sin IVA, menos lo que se quedaron los canales y los insumos al costo de cada día, y después los gastos propios de cada unidad y su parte de los compartidos. Sirve para saber qué marca y qué canal dejan plata, y cuánto.

<p class="perm"><span>Quién puede:</span> <span class="tag">Reportes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/reportes-rentabilidad.jpg' | relative_url }}" alt="Rentabilidad de este mes: ventas sin IVA, costo de insumos, comisiones, gastos y resultado, el aviso de que el resultado no incluye sueldos, el gráfico de a dónde va cada peso vendido y la tabla por unidad de negocio" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li><b>Exportar</b>: la tabla a una planilla.</li>
    <li>Las cifras del período.</li>
    <li>El aviso de sueldos.</li>
    <li><b>A dónde va cada peso vendido</b>, para toda la cocina y para cada unidad.</li>
    <li>La tabla por unidad de negocio. Tocá una para ver su detalle.</li>
  </ol>
  <figcaption>La rentabilidad del mes en la demo, con una sola venta.</figcaption>
</figure>

El período arranca en **Este mes**.

**Cifras**: **Ventas sin IVA** (con cuántos pedidos), **Costo de insumos** (en % y en pesos, incluido lo que se perdió en pedidos cancelados), **Comisiones**, **Gastos** y **Resultado**, o **Pérdida** si dio negativo.

### Los sueldos

Si en el período no hay ningún sueldo, la pantalla avisa: «Este resultado no incluye sueldos: en el período no hay ninguno pagado ni cargado como gasto. Se pagan en Personal › Liquidación, o se cargan en Gastos con la categoría de sueldos.»

Esto pasa cuando los sueldos se pagan por fuera de Fornu: por transferencia desde el banco, en mano desde el bolsillo del dueño. El resultado entonces parece mejor de lo que es. Hay dos formas de que entren:

- Pagarlos desde [Personal]({{ '/es/projects/fornu/manual/personal/' | relative_url }}#liquidacion), en **Liquidación**.
- Cargarlos en [Gastos]({{ '/es/projects/fornu/manual/compras-y-gastos/' | relative_url }}#gastos) con una categoría de sueldos. Fornu la reconoce si su nombre tiene la palabra sueldo, como Sueldos o Sueldos de cocina.

### El gráfico y la tabla

**A dónde va cada peso vendido** tiene una fila para **Toda la cocina** y una por unidad, partidas en **Insumos**, **Comisiones**, **Gastos** y **Resultado**. Tocá una fila para ver cada monto.

La tabla tiene una fila por unidad y el **Total** abajo:

| Columna | Qué es |
|---|---|
| **Pedidos** | Cuántos, y cuántos cancelados. |
| **Ventas** / **Sin IVA** | Lo vendido, con y sin IVA. |
| **Comisiones** | Lo que se quedaron los canales. |
| **Insumos** | Lo que costó lo que se usó, más lo perdido en cancelados. |
| **Contribución** | Lo que queda antes de los gastos. |
| **Gastos propios** | Los gastos cargados a esa unidad. |
| **Compartidos** | Su parte de los gastos de todo el local y de las mermas. |
| **Resultado** | Lo que quedó, en pesos y en %. |

Al tocar una unidad se abre su detalle: **Por canal** (pedidos, ventas, comisión y lo que dejó cada canal), **Lo que consumió**, y **Cada producto** con **Unidades**, **Ventas**, **Dejó** y **Parte**. Los que no se vendieron dicen «No se vendió en este período».

Más abajo, **Consumo de insumos** (cada insumo con su cantidad, su costo y cuánto usó cada unidad) y **Gastos del período** (cada categoría, compartida o de una unidad), con tres notas: las **Mermas**, las **Compras de insumos** («No son gasto del período: pasan a serlo cuando los pedidos usan lo que se compró.») y el **IVA**.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/reportes-rentabilidad-consumo.jpg' | relative_url }}" alt="Consumo de insumos con cantidad, costo y reparto por unidad de negocio, y Gastos del período con una categoría compartida y las notas de mermas, compras de insumos e IVA" loading="lazy" width="1440" height="520">
  <figcaption>Lo que se consumió y lo que se gastó en un mes de la demo.</figcaption>
</figure>

<div class="callout tip"><p class="callout-title">Consejo</p><p>Los gastos compartidos y las mermas se reparten entre las unidades según lo que vendió cada una sin IVA (en partes iguales si no vendió ninguna). Un pedido cancelado después de confirmado es pérdida para su unidad, porque el stock ya se usó.</p></div>

<div class="callout"><p class="callout-title">Importante</p><p>La columna <b>Insumos</b> usa lo que costaba cada insumo cuando salió del stock. <b>Dejó</b>, en el detalle de cada producto, usa los costos de hoy. Si los precios cambiaron en el período, los dos números no coinciden, y está bien.</p></div>

### Exportar

**Exportar** baja una planilla con una fila por unidad y el total (pedidos, cancelados, ventas, ventas sin IVA, comisiones, insumos, perdido en cancelados, contribución, gastos propios, gastos compartidos y resultado), y después el consumo de cada insumo con su cantidad, su unidad y su costo. En la planilla van los centavos. En pantalla, pesos enteros.

### Lo que Reportes suma en Inicio

Quien tiene Reportes ve en Inicio la tarjeta **Cómo te fue**: **Ventas** contra el período anterior, **Resultado** (qué parte de lo vendido sin IVA quedó), **Pedidos** con el ticket y **Cancelados**. Abajo, el aviso de sueldos si corresponde y una tabla con cada unidad por canal.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/reportes-inicio.jpg' | relative_url }}" alt="Tarjeta Cómo te fue en Inicio: el aviso de sueldos, una tabla con lo que vendió y dejó cada marca en pedidos propios y en Rappi, el resultado de cada una y los botones Resumen de ventas y Rentabilidad" loading="lazy" width="1440" height="628">
  <ol class="marks">
    <li>El aviso de sueldos.</li>
    <li>Lo que vendió una marca en un canal y lo que dejó.</li>
    <li><b>Resultado</b> de cada marca, después de sus gastos.</li>
    <li><b>Resumen de ventas</b> y <b>Rentabilidad</b>, para ver más.</li>
  </ol>
  <figcaption>Inicio en la demo: las cuatro marcas en pedidos propios y en Rappi.</figcaption>
</figure>

«Deja: lo vendido sin IVA, menos la comisión del canal y los insumos de esos pedidos. El resultado además resta los gastos de la unidad y su parte de los compartidos.»
