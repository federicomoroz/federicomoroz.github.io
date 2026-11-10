---
layout: manual
manual: compras-y-gastos
title: "Compras y gastos · Manual de Fornu"
description: "Cómo se cargan las compras de insumos que entran al stock, los proveedores con su CUIT y lo que se les debe, los gastos del local, cómo se pagan uno o varios juntos y cómo se exportan para el contador."
permalink: /es/projects/fornu/manual/compras-y-gastos/
---

## Compras de insumos {#compras}

Acá se carga lo que llega de los proveedores, con su comprobante. Al guardar una compra, los insumos entran al stock, el precio y el IVA de cada uno quedan al día y, si se pagó en efectivo, la plata sale de la caja. También se ve cuánto se les debe a los proveedores y se les paga.

Está en Compras › **Compras de insumos** (la pestaña dice **Compras**) y viene con el módulo Proveedores y compras. También es la pestaña **Compras** del dispositivo del local.

<p class="perm"><span>Quién puede:</span> <span class="tag">Gastos</span></p>

El rol **Encargado/a** de una cuenta nueva ya lo tiene. El campo **Proveedor** de la compra aparece si el rol tiene también el permiso **Proveedores**.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/compras-lista.jpg' | relative_url }}" alt="La lista Compras de insumos del mes, con 1.598.400 pesos en compras y 666.000 a pagar, una compra a un frigorífico a pagar con su botón Pagar y una compra semanal pagada por transferencia." loading="lazy" width="1440" height="838">
  <ol class="marks">
    <li><b>Exportar</b> y <b>Compra de insumos</b>.</li>
    <li>El período: <b>Hoy</b>, <b>Ayer</b>, <b>Semana pasada</b>, <b>Últimos 7 días</b>, <b>Este mes</b> o <b>Mes pasado</b>, o las fechas <b>Desde</b> y <b>Hasta</b>. <b>Ver anulados</b> suma las compras anuladas.</li>
    <li><b>A pagar</b>: todo lo que se debe de compras, sea del período que sea. Tocalo para pagar.</li>
    <li><b>Estado</b>: <b>A pagar</b>, <b>Vencido</b> (en rojo, con la fecha), <b>Pagado</b> (con el medio y la fecha) o <b>Anulado</b> (con el motivo).</li>
    <li><b>Pagar</b>, en las que se deben, y el menú <b>⋯</b>, con <b>Repetir compra</b> y <b>Anular</b>.</li>
    <li>La confirmación al guardar una compra.</li>
  </ol>
  <figcaption>Dos compras de la demo, una a pagar y otra pagada.</figcaption>
</figure>

Cada fila muestra la fecha, el proveedor con la descripción abajo, la categoría con cuántos insumos entraron al stock, el comprobante con su número, la unidad de negocio (o «Compartido») y el total.

### Cargar una compra {#cargar-compra}

1. Tocá **Compra de insumos**.
2. Elegí el **Proveedor**. Si le compraste en los últimos 120 días, aparece **Cargar lo de la última compra**: está explicado más abajo.
3. Elegí el **Comprobante** y escribí el **Número**, que es obligatorio en las facturas A, B y C y en las notas de crédito.
4. Elegí si los precios que vas a escribir son **Precios con IVA** o **Precios sin IVA**, como figuran en el comprobante.
5. Agregá cada insumo con **+ Insumo**: buscalo por el nombre, escribí la cantidad en la unidad en que llega (bolsas, cajas, kilos) y revisá el precio y el IVA.
6. Elegí **Pagado**, con el medio y la fecha, o **A pagar (cuenta corriente)**, con el vencimiento si lo tiene.
7. Tocá **Guardar**, o apretá <kbd>Ctrl</kbd> + <kbd>Enter</kbd>.
{: .steps}

Fornu confirma «Compra cargada: los insumos ya están en el stock».

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/compras-dialogo.jpg' | relative_url }}" alt="Dos partes de una compra de insumos: a la izquierda la fecha, el proveedor, la categoría, la unidad de negocio, el comprobante y los precios con IVA. A la derecha, tres carnes con su cantidad, precio e IVA, los importes y el pago a cuenta corriente." loading="lazy" width="1440" height="728">
  <ol class="marks">
    <li><b>Proveedor</b>. <b>+ Proveedor nuevo</b> lo crea ahí mismo. Al elegirlo se completa su categoría habitual.</li>
    <li><b>Unidad de negocio</b>: <b>Compartido entre todas</b> reparte el gasto entre las marcas según lo que vende cada una. O elegí una sola.</li>
    <li><b>Comprobante</b> y <b>Número</b>.</li>
    <li><b>Precios con IVA</b> o <b>Precios sin IVA</b>: arranca según el comprobante, sin IVA para la factura A.</li>
    <li>Los insumos, cada uno con su cantidad, su precio y su IVA. Abajo del nombre dice cómo se compra, como «caja de 10 kg».</li>
    <li><b>Pagado</b> o <b>A pagar (cuenta corriente)</b>.</li>
  </ol>
  <figcaption>El principio y el final de una compra de tres insumos a cuenta corriente.</figcaption>
</figure>

| Campo | Para qué sirve |
|---|---|
| **Fecha** | Arranca en hoy. Si ponés una fecha futura, avisa. |
| **Proveedor** | A quién se le compró. |
| **Categoría** | Arranca en **Insumos**, o en la categoría habitual del proveedor. |
| **Unidad de negocio** | **Compartido entre todas**, o una marca. |
| **Comprobante** | Factura A, B, C o X, Ticket, Remito (el de siempre en compras), Nota de crédito, Recibo o Sin comprobante. |
| **Número** | Como 0001-00012345. Obligatorio en las facturas A, B y C y en las notas de crédito, opcional en los demás. |
| **Descripción** | Por ejemplo, «Pedido semanal de verdura». |
| **Insumos** | Los ingredientes y artículos de inventario activos. Cada línea trae el último precio y el IVA del insumo. Si escribís otro precio, abajo dice cuánto cambió, como «Antes $ 9.000 · +12%». |
| **Neto (sin IVA)** e **IVA** | Se calculan solos con las líneas. Debajo del IVA dice cuánto va a cada alícuota. |
| **Percepciones y otros impuestos** | Lo que el comprobante suma aparte. |
| **Pago** | **Pagado**, con su **Medio de pago** (Efectivo, Transferencia, Tarjeta de débito, Tarjeta de crédito, Mercado Pago o Cheque) y **Pagado el**. O **A pagar (cuenta corriente)**, con **Vence (opcional)**. |

Cada insumo lleva su IVA, aunque la factura sea una sola. Al guardar, el precio y el IVA de cada línea pasan a ser los del insumo, y los márgenes de lo que lo usa se recalculan.

<div class="callout"><p class="callout-title">Importante</p><p>Una compra nueva arranca como <b>Pagado</b> en <b>Efectivo</b>, con fecha de hoy. Si la guardás así, la plata sale de la caja. Si la vas a pagar más adelante, elegí <b>A pagar (cuenta corriente)</b> antes de guardar.</p></div>

Una nota de crédito no trae insumos. Fornu pide cargarla como gasto, y sacar lo devuelto del stock en Stock.

### Cargar lo de la última compra {#ultima-compra}

Si al proveedor le compraste en los últimos 120 días, al elegirlo aparece **Cargar lo de la última compra**, con cuántos insumos tenía, la fecha y «a los precios de hoy». Tocalo antes de cargar líneas: se llenan los mismos insumos a los precios actuales, y el pago queda como la última vez, pagado o a pagar y con el mismo medio. Ajustá las cantidades y guardá.

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/compras-dialogo-telefono.jpg' | relative_url }}" alt="Una compra de insumos en el celular, con el aceite de girasol y el agua sin gas cargados desde la última compra, cada uno en una tarjeta con su cantidad, precio con IVA e IVA, y el total abajo." loading="lazy" width="390" height="844">
  <figcaption>En el celular del local, cada insumo de la compra es una tarjeta.</figcaption>
</figure>

### Qué productos cambiaron de margen {#margenes}

Cuando una compra cambia el precio de algún insumo, al guardarla aparece un recuadro arriba de la lista, por ejemplo «Cambió el precio de 2 insumos: Harina +12% · …. Toca 5 productos:». Una tabla muestra cada producto afectado con su unidad de negocio, el costo antes y después, y el margen del canal que menos deja, antes y después.

**Revisar precio** abre ese producto en **Precios**, listo para corregir ([Carta]({{ '/es/projects/fornu/manual/carta/' | relative_url }}#arreglar-precio)). Si ningún producto a la venta usa esos insumos, el recuadro dice «No toca ningún producto a la venta.» Se cierra con la ✕.

### Repetir una compra {#repetir}

**⋯** › **Repetir compra** abre una compra nueva con el mismo proveedor, la misma categoría, unidad de negocio, comprobante, descripción e insumos, a los precios de hoy. La fecha es hoy, el número queda vacío y el pago es pagado hoy con el mismo medio, o en efectivo si no había. Una nota de crédito se repite como remito, y los insumos desactivados quedan afuera.

### Corregir una compra {#editar}

Tocá la fila. Se puede cambiar todo menos los insumos, incluso si está pagada o a pagar. Los insumos ya entraron al stock: para corregirlos, anulá la compra y cargala de nuevo. Fornu confirma «Cambios guardados».

### Anular una compra {#anular-compra}

1. Tocá **⋯** › **Anular**.
2. Escribí el **Motivo**. Fornu avisa que los insumos que trajo salen del stock.
3. Tocá **Anular**.
{: .steps}

La compra sigue en la lista, más clara, cuando prendés **Ver anulados**. El precio de cada insumo vuelve al que tenía antes, salvo que una compra posterior haya puesto otro.

## Proveedores {#proveedores}

A quién se le compra o se le paga, con su CUIT, su contacto, su categoría habitual y lo que se le debe. Cargarlos sirve para elegirlos en cada compra y ver el saldo de cada uno.

Está en Compras › **Proveedores** y viene con el módulo Proveedores y compras.

<p class="perm"><span>Quién puede:</span> <span class="tag">Proveedores</span></p>

Para pagarle desde acá hace falta también el permiso **Gastos**.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/compras-proveedores.jpg' | relative_url }}" alt="La lista de proveedores con una carnicería y una verdulería, su categoría habitual Insumos y nada a pagar." loading="lazy" width="1440" height="350">
  <ol class="marks">
    <li><b>Agregar</b>: un proveedor nuevo.</li>
    <li><b>CUIT</b>: Fornu lo controla al cargarlo.</li>
    <li><b>Categoría habitual</b>: la que se propone al cargarle un gasto.</li>
    <li><b>A pagar</b>: lo que se le debe, con <b>Pagar</b> al lado cuando hay algo.</li>
  </ol>
  <figcaption>Dos proveedores de la demo, al día.</figcaption>
</figure>

| Campo | Para qué sirve |
|---|---|
| **Nombre** | Obligatorio, y no se repite. |
| **CUIT** | Con o sin guiones. Opcional. |
| **Teléfono** y **Email** | Se ven juntos en la columna **Contacto**. |
| **Categoría habitual** | **Ninguna**, o una categoría de gastos activa. Se propone al cargarle un gasto o una compra. |
| **Dirección** y **Notas** | Para tenerlo a mano. |
| **Activo** | Al editarlo. Un proveedor desactivado deja de aparecer para elegir, y conserva sus compras y sus pagos. |

Los proveedores se desactivan en vez de borrarse. Si el CUIT está mal, Fornu avisa por qué: «El CUIT … tiene que tener 11 números.», «El CUIT … no es válido: revisá los números.» o «El CUIT … ya es de …».

**Pagar** abre «Pagarle a …» con todos los comprobantes de ese proveedor tildados. Funciona como [Pagar varios juntos](#pagar-varios).

El buscador de arriba (<kbd>Ctrl</kbd> + <kbd>K</kbd>) también encuentra proveedores, marcados como «Proveedor», y los abre.

## Gastos {#gastos}

Todo lo que se pagó o hay que pagar: compras de insumos, alquiler, servicios y sueldos. Cada gasto es de una unidad de negocio o se reparte entre todas según lo que vende cada una. Lo pagado en efectivo sale de la caja.

Está en Balances › **Gastos**. En el celular, Balances está dentro de **Más**. También es la pestaña **Gastos** del dispositivo del local.

<p class="perm"><span>Quién puede:</span> <span class="tag">Gastos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/gastos-lista.jpg' | relative_url }}" alt="La lista de gastos del mes: dos compras a un frigorífico a pagar, una factura de luz y gas pagada y una compra semanal pagada, con el total del período, lo que hay que pagar y las compras de insumos arriba." loading="lazy" width="1440" height="725">
  <ol class="marks">
    <li><b>Exportar</b>: la lista en un archivo para Excel.</li>
    <li><b>Nuevo gasto</b>: alquiler, luz, mantenimiento, cualquier gasto que no trae insumos.</li>
    <li><b>Compra de insumos</b>: la misma compra de Compras, con el módulo Proveedores y compras.</li>
    <li><b>A pagar</b>: todo lo que se debe, sin contar sueldos, sea del período que sea. Tocalo para pagar varios juntos.</li>
    <li><b>Pagar</b>: paga ese comprobante.</li>
    <li>El menú <b>⋯</b>: <b>Repetir compra</b>, en las compras, y <b>Anular</b>.</li>
  </ol>
  <figcaption>Los gastos de la demo en lo que va del mes.</figcaption>
</figure>

Arriba están el **Total del período**, lo que hay **A pagar** y las **Compras de insumos**. El período funciona igual que en Compras, y el que elijas se mantiene en las otras pantallas que piden un período mientras la pestaña del navegador siga abierta.

Los sueldos aparecen con la etiqueta «sueldo» y dicen «Se cambia en Personal › Liquidación»: no se abren ni se anulan desde acá. Se explican en [Personal]({{ '/es/projects/fornu/manual/personal/' | relative_url }}#liquidacion).

### Cargar un gasto {#nuevo-gasto}

1. Tocá **Nuevo gasto**.
2. Elegí el **Proveedor**, si tiene, y la **Categoría**.
3. Elegí la **Unidad de negocio**, o dejalo en **Compartido entre todas**.
4. Elegí el **Comprobante**, que arranca en **Factura B**, y escribí el **Número**.
5. Escribí el **Neto** y el **IVA**. **21% del neto** y **10,5% del neto** completan el IVA con un toque. Sumá las percepciones, si hay.
6. Elegí **Pagado** o **A pagar**, y tocá **Guardar**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/gastos-nuevo.jpg' | relative_url }}" alt="El panel Nuevo gasto con la fecha, el proveedor, la categoría sin elegir, compartido entre todas, factura B, el número, la descripción, el neto y el IVA con los atajos de 21 y 10,5 por ciento." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li><b>Proveedor</b>, con <b>+ Proveedor nuevo</b>.</li>
    <li><b>Unidad de negocio</b>.</li>
    <li><b>Comprobante</b> y <b>Número</b>.</li>
    <li><b>21% del neto</b> y <b>10,5% del neto</b>: calculan el IVA.</li>
    <li>El total y lo que falta para poder guardar.</li>
  </ol>
  <figcaption>Un gasto nuevo, antes de elegir la categoría.</figcaption>
</figure>

Fornu confirma «Gasto cargado». Igual que las compras, un gasto nuevo arranca pagado en efectivo con fecha de hoy.

### Pagar un gasto {#pagar}

1. Tocá **Pagar** en la fila.
2. Elegí el **Medio de pago**, que arranca en Transferencia, y la **Fecha de pago**.
3. Tocá **Registrar pago**. Fornu confirma «Pago registrado».
{: .steps}

Si mientras tanto alguien ya lo pagó, avisa «Ya está pagado» con la fecha.

### Pagar varios juntos {#pagar-varios}

Tocá **A pagar**, en Gastos o en Compras. También se llega desde los avisos de pagos vencidos o por vencer de Inicio, y desde **Pagar** en Proveedores.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/gastos-pagar-varios.jpg' | relative_url }}" alt="El panel Lo que hay que pagar, con un botón por proveedor, tres comprobantes de los que hay dos tildados, transferencia, la fecha de pago y el botón Pagar 123.000 pesos." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li>Un botón por proveedor, con su total: tilda todos sus comprobantes.</li>
    <li>Los comprobantes, con su fecha, número y vencimiento.</li>
    <li><b>Medio de pago</b> y <b>Fecha de pago</b>.</li>
    <li>Cuánto suma lo tildado y cuántos son.</li>
    <li><b>Pagar $ …</b>.</li>
  </ol>
  <figcaption>Dos comprobantes de la verdulería, pagados juntos por transferencia.</figcaption>
</figure>

1. Tildá lo que vas a pagar, o tocá el botón de un proveedor. Vienen tildados los vencidos, o todos los del proveedor si entraste desde Proveedores.
2. Elegí el medio y la fecha.
3. Tocá **Pagar $ …**.
{: .steps}

Fornu confirma cuántos comprobantes pagó y por cuánto. Se pagan todos o ninguno: si alguno ya estaba pagado, avisa cuál para sacarlo de la lista. Desde Compras de insumos, la lista trae solo compras.

### Si la caja está cerrada {#caja-cerrada}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/gastos-caja-cerrada.jpg' | relative_url }}" alt="El aviso La caja está cerrada, que explica que ese efectivo saldría de una caja que nadie abrió, con los botones Volver y Pagar igual." loading="lazy" width="500" height="266">
  <figcaption>El aviso antes de pagar en efectivo con la caja cerrada.</figcaption>
</figure>

Cuando pagás en efectivo y la caja no está abierta, Fornu pregunta antes: «La caja está cerrada». Pasa al guardar un gasto o una compra pagados en efectivo, y al pagar uno o varios en efectivo. Ese efectivo saldría de una caja que nadie abrió, y al abrirla el arqueo no lo va a cuadrar. Tenés tres salidas:

- **Volver** y abrir la caja antes, en Balances › Arqueo ([Caja y ventas]({{ '/es/projects/fornu/manual/caja/' | relative_url }}#arqueo)).
- **Volver** y elegir otro medio, si la plata salió de otro lado.
- **Pagar igual**.

Al editar un gasto que ya existe no pregunta. Si el pago cae antes de un arqueo que ya lo tuvo en cuenta, Fornu avisa que la caja ya se contó con ese efectivo y no la mueve otra vez. Si la plata no está como dice, se corrige con un movimiento en Caja.

### Anular un gasto {#anular}

1. Tocá **⋯** › **Anular**.
2. Escribí el **Motivo**.
3. Tocá **Anular**. Fornu confirma «Anulado».
{: .steps}

El gasto sigue en la lista, más claro, cuando prendés **Ver anulados**. Los sueldos se anulan desde Personal › Liquidación.

### Exportar para el contador {#exportar}

**Exportar** baja un archivo para Excel en castellano, con las columnas separadas por punto y coma y los decimales con coma. Trae lo que está en la lista: el período elegido, y las anuladas si están a la vista. El archivo se llama con las fechas, como `compras-y-gastos-2026-11-01-a-2026-11-30.csv`.

Trae una fila por comprobante, con la fecha, el comprobante y su número, el proveedor y su CUIT, la categoría, la unidad de negocio, la descripción, el neto y el IVA de cada alícuota (21%, 10,5%, 27% y otras), lo no gravado o exento, lo que no tiene IVA discriminado, las percepciones, el total, el estado, la fecha y el medio de pago, y el vencimiento.

## Categorías de gastos {#categorias-gastos}

Sirven para agrupar los gastos y ver en Rentabilidad en qué se va la plata ([Costos y reportes]({{ '/es/projects/fornu/manual/costos-y-reportes/' | relative_url }}#rentabilidad)).

Están en Compras › **Categorías de gastos** (la pestaña dice **Categorías**).

<p class="perm"><span>Quién puede:</span> <span class="tag">Ajustes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/compras-categorias-gastos.jpg' | relative_url }}" alt="La lista de categorías de gastos de una cuenta nueva, de Insumos a Otros, con su orden." loading="lazy" width="1440" height="650">
  <ol class="marks">
    <li><b>Agregar</b>: una categoría nueva.</li>
    <li><b>Insumos</b>: la que eligen solas las compras nuevas.</li>
    <li><b>Orden</b>: en qué lugar aparece en las listas.</li>
  </ol>
  <figcaption>Las categorías con que arranca una cuenta.</figcaption>
</figure>

Una cuenta nueva arranca con Insumos, Packaging, Alquiler, Servicios (luz, gas, internet), Sueldos y cargas sociales, Mantenimiento y limpieza, Impuestos y tasas, Comisiones y gastos bancarios, Publicidad y Otros.

Tocá **Agregar**, o una categoría para cambiarla. Cada una tiene **Nombre**, **Orden** (una nueva va al final) y, al editarla, **Activa**. Las categorías se desactivan en vez de borrarse. Una desactivada deja de ofrecerse, y los gastos que ya la tenían la conservan.

<div class="callout tip"><p class="callout-title">Consejo</p><p>Dejá una categoría que se llame exactamente <b>Insumos</b>. Las compras nuevas, y las que arma el plan de producción, la eligen solas.</p></div>
