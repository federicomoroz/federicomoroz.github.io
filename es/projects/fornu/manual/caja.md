---
layout: manual
manual: caja
title: "Caja y ventas · Manual de Fornu"
description: "La lista de ventas con todos sus filtros, los ingresos y egresos de la caja, y cómo se abre, se cuenta y se cierra la caja, también a ciegas."
permalink: /es/projects/fornu/manual/caja/
---

Todo esto está en el grupo **Balances**. En el celular, Balances está dentro de **Más**. Los gastos del local también están en Balances, pero se explican en [Compras y gastos]({{ '/es/projects/fornu/manual/compras-y-gastos/' | relative_url }}#gastos).

## Elegir el período {#periodo}

Ventas, Movimientos de caja, Facturas, Resumen de ventas y Rentabilidad usan el mismo selector de fechas. Lo elegís una vez y te acompaña de una pantalla a la otra mientras la pestaña del navegador siga abierta.

| Botón | Qué abarca |
|---|---|
| **Hoy** | El día de trabajo de la cocina, que no siempre termina a la medianoche (ver abajo). |
| **Ayer** | El día de trabajo anterior. |
| **Semana pasada** | De lunes a domingo de la semana anterior. |
| **Últimos 7 días** | Los siete días completos hasta ayer. |
| **Este mes** | Desde el 1 del mes hasta hoy. |
| **Mes pasado** | El mes anterior entero. |
| **Desde** / **Hasta** | Cualquier otro rango, con dos fechas. |

- **Hoy** es el día de la cocina. En Ajustes › Configuración, **El día empieza a las** dice a qué hora arranca: si empieza a las 6, a la una de la mañana lo vendido a la noche sigue siendo de hoy. Se explica en [Ajustes]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#configuracion).
- Los botones se recalculan solos: si mañana volvés a la pantalla con **Ayer** elegido, muestra el ayer de mañana.
- Cada pantalla arranca con su período de siempre (Ventas con **Hoy**, Rentabilidad con **Este mes**) solo la primera vez. Después manda lo último que elegiste.
- En el celular las fechas se esconden detrás de **Otras fechas**.

## Ventas {#ventas}

Es la lista de todo lo que se vendió: cada venta con su canal, su hora, quién la atendió y cómo se pagó. Sirve para contestar las preguntas del día a día: cuánto entró por QR, qué cobró Lucía en el turno noche, cuánto dejó el patio, qué se canceló y por qué. Tocás una venta y ves todo lo que pasó con ella, desde que entró hasta que se cobró.

Muestra los pedidos confirmados del período, también los que todavía están en preparación y las mesas abiertas. Los cancelados van aparte. El período puede ser de hasta 92 días. Para más, Fornu responde «Elegí hasta 92 días. Para períodos más largos está el Resumen de ventas.»

<p class="perm"><span>Quién puede:</span> <span class="tag">Caja</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-ventas.jpg' | relative_url }}" alt="Pantalla Ventas con el selector de período, los filtros, cinco cifras (3 pedidos vendidos, 13.500 pesos), Más info abierto con Efectivo y Por cobrar, y la lista de ventas de mesas sin facturar" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li><b>Hoy · Ayer · …</b>: el período. Debajo, el buscador por cliente, número o código de la plataforma.</li>
    <li>Los filtros. Aparecen solo los que tienen sentido en tu local: sin mozos no hay <b>Atendió</b>, sin mesas no hay <b>Mesa</b>.</li>
    <li>Las cifras de lo que dejan los filtros. <b>Pedidos vendidos</b> y <b>Cancelados</b> cambian la lista de abajo.</li>
    <li><b>Más info</b>: cuánto entró por cada medio de pago, las propinas, los descuentos y los motivos de cancelación.</li>
    <li><b>Comprobante</b>: si la venta está facturada y con qué factura.</li>
    <li><b>Exportar</b>: baja la lista a una planilla.</li>
  </ol>
  <figcaption>Ventas de hoy en la cocina de prueba de la demo.</figcaption>
</figure>

### Buscar una venta

Escribí en **Cliente, número o código…**. Encuentra el número exacto del pedido (con o sin #), el nombre del cliente o el código que le puso la plataforma.

### Filtrar la lista

| Filtro | Qué deja ver | Cuándo aparece |
|---|---|---|
| **Canal** | **Pedidos propios**, **Rappi**, **PedidosYa** o **Salón**. | Solo los canales que la cuenta tiene prendidos. |
| **Unidad de negocio** | Una de tus marcas. | Siempre. |
| **Medio de pago** | Un medio, o **Todo menos efectivo** (ver abajo). | Siempre. |
| **Atendió** | Lo que atendió un mozo. | Cuando alguna venta tiene mozo. |
| **Sector** | Un sector del salón: patio, terraza, salón. | Con dos sectores o más. |
| **Mesa** | Una mesa. | Cuando hay mesas. |
| **Arqueo** | Lo que se cobró o se canceló mientras una caja estaba abierta, o sea lo que esa caja tiene que rendir. Cada caja aparece como «10/11 12:00 → 23:40», o «→ abierta» si sigue abierta. | Para quien tiene Caja. Muestra las últimas 30. |
| **Comprobante** | **Facturadas** o **Sin facturar**. | Siempre. |
| **Turno** | **Mañana (6 a 12)**, **Mediodía (12 a 16)**, **Tarde (16 a 20)** o **Noche (20 a 6)**. Llena las dos horas de un toque. | Siempre. |
| **Desde las** / **Hasta las** | Un rango de horas a mano. Puede pasar la medianoche: de 20 a 2 es de las 20 a las 2 de la mañana. | Siempre. |

Cuando elegís horas aparece **Abiertas** / **Cerradas**. Con **Abiertas** (la de siempre) cuenta la hora en que se abrió la venta. Con **Cerradas**, la hora en que se cobró o se canceló. Sirve para separar, por ejemplo, las mesas que se sentaron antes de las 23 de las que se cobraron después.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-ventas-hora.jpg' | relative_url }}" alt="Ventas de ayer filtradas por Turno Noche, de 20 a 6, con Abiertas o Cerradas en Cerradas, las cifras y la lista" loading="lazy" width="1440" height="614">
  <ol class="marks">
    <li><b>Turno</b>: <b>Noche (20 a 6)</b> llena las dos horas.</li>
    <li><b>Abiertas</b> / <b>Cerradas</b>: qué hora de cada venta cuenta.</li>
  </ol>
  <figcaption>La noche de ayer, por la hora en que se cerró cada venta.</figcaption>
</figure>

Cuando hay algún filtro o una búsqueda aparece **Sacar filtros**, que limpia todo menos el período.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-ventas-filtro.jpg' | relative_url }}" alt="Filtros de Ventas con Medio de pago en Todo menos efectivo, el filtro Arqueo, el enlace Sacar filtros y una sola venta pagada con tarjeta de débito en la lista" loading="lazy" width="1440" height="535">
  <ol class="marks">
    <li><b>Medio de pago</b> en <b>Todo menos efectivo</b>.</li>
    <li><b>Arqueo</b>: elegí una caja para ver solo lo que pasó mientras estuvo abierta.</li>
    <li><b>Sacar filtros</b>: vuelve a la lista completa del período.</li>
    <li>Queda la venta pagada con tarjeta. La de efectivo no aparece.</li>
  </ol>
  <figcaption>Lo que no se pagó en efectivo, listo para facturar al final del día.</figcaption>
</figure>

**Todo menos efectivo** junta lo que pagó la plataforma, las tarjetas, el QR, la transferencia, Mercado Pago y lo **Pagado antes**. Deja afuera todo lo que tenga efectivo (aunque sea una parte de un pago mixto), lo que está **Por cobrar** y lo que figura **Sin dato**. Es el filtro de quien factura al final del día lo que dejó rastro en el banco.

<div class="callout tip"><p class="callout-title">Consejo</p><p>Las preguntas de siempre tienen su filtro. ¿Cuánto vendió el turno noche? <b>Turno</b> › <b>Noche (20 a 6)</b>. ¿Qué tiene que rendir la caja de hoy? <b>Arqueo</b> › la caja abierta. ¿Qué atendió Martín en el patio? <b>Atendió</b> › Martín y <b>Sector</b> › Patio.</p></div>

### Leer las cifras y Más info

- **Pedidos vendidos**: cuántas ventas hubo. Tocá la cifra para ver la lista de lo vendido.
- **Ventas**: el total cobrado, en pesos enteros.
- **Ticket promedio**: lo que deja cada venta en promedio.
- **Cancelados**: cuántas se cancelaron. Tocá la cifra y la lista pasa a mostrar las canceladas, con la columna **Motivo**. Tocala otra vez para volver.
- **Comensales**: aparece cuando hubo gente sentada, con lo que dejó cada uno («$ 1.500 por comensal»).

Todas cuentan solo lo que dejan los filtros. Lo cancelado nunca suma en **Ventas**.

**Más info** se despliega con un toque y muestra una tarjeta por cada forma de pago, con el total y cuántas ventas. Tocar una tarjeta filtra por esa forma de pago, y tocarla de nuevo saca el filtro. Así se llega también a **Varios medios** (cuentas pagadas en partes), **Por cobrar** y **Sin dato**, que no están en el filtro de arriba. La tarjeta de **Varios medios** dice además cuánto entró por cada medio, sin las propinas.

Con dos sectores o más aparece **Por sector**, con una tarjeta por sector que también filtra. Abajo, tres datos: **Propinas**, **Cortesías y descuentos** («$X en N ventas») y **Cancelaciones**, con cada motivo y cuántas veces pasó.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-ventas-mas-info.jpg' | relative_url }}" alt="Más info desplegado: tarjeta Efectivo, tarjeta Varios medios con 4.500 en efectivo y 4.500 con tarjeta de débito, y tarjetas Por sector para Patio y Salón" loading="lazy" width="1440" height="400">
  <ol class="marks">
    <li><b>Comensales</b>: 4 personas sentadas, 4.500 pesos por cabeza.</li>
    <li><b>Varios medios</b>: una cuenta pagada mitad en efectivo y mitad con débito.</li>
    <li><b>Por sector</b>: cuánto dejó cada sector del salón.</li>
  </ol>
  <figcaption>Más info en un día con dos mesas, una en el patio y otra en el salón.</figcaption>
</figure>

### Leer la lista

| Columna | Qué dice |
|---|---|
| **#** | El número del pedido. |
| **Día y hora** | Cuándo se abrió. |
| **Unidad de negocio** | La marca, el canal y, si vino de una plataforma, su código. |
| **Cliente** | A nombre de quién está, o la mesa. |
| **Atendió** | La mesa, el mozo y los comensales, por ejemplo «Mesa 4 · Lucía · 3 comensales». Solo si hay mozos. |
| **Medio de pago** | El medio, **Por la plataforma**, **Varios medios**, **Por cobrar** o **Sin dato**, y la propina si hubo. |
| **Total** | Lo cobrado. |
| **Comprobante** | **Facturada · Factura B 00003-00000012** en verde, o **Sin facturar** con la razón al lado: (anulada), (esperando a ARCA), (pedida: motivo) o (rechazada). Una cancelada dice «—». |

Las canceladas aparecen más claras. La lista dibuja 200 ventas por vez: para ver el resto tocá **Ver N más de M** al final.

### Ver todo lo que pasó con una venta

1. Tocá la venta en la lista.
2. Se abre su detalle a la derecha (en pantallas chicas ocupa toda la pantalla): el canal, el estado, lo que se pidió con el total, el cliente con su teléfono, la entrega, la nota, el pago y, si la cuenta factura, la factura.
3. Abajo está la historia completa, paso a paso y con la hora: cuándo entró, cuándo se confirmó, cada ronda que fue a la cocina, quién cobró y cuánto, cuándo se facturó.
4. Con el detalle abierto, las flechas <kbd>↑</kbd> y <kbd>↓</kbd> pasan a la venta anterior o a la siguiente sin cerrar nada.
5. Cerralo con la X.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-ventas-detalle.jpg' | relative_url }}" alt="Detalle del pedido 2 de Doble Smash abierto a la derecha de la lista: una papas fritas por 4.500 pesos y la historia de la venta desde que entró hasta que se entregó" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li>El pedido y su marca. La X lo cierra.</li>
    <li>Lo que se pidió y el total.</li>
    <li>La historia: entró, se confirmó, se sentó la mesa, la ronda fue a la cocina, se cobró en efectivo y se entregó.</li>
  </ol>
  <figcaption>Una mesa de la demo, de punta a punta.</figcaption>
</figure>

Las flechas no hacen nada mientras estás escribiendo en un campo o con un diálogo abierto.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-ventas-factura.jpg' | relative_url }}" alt="El detalle de un pedido de Pizzería de Rappi con su producto, el cliente, la entrega y la línea Factura con Factura C 00003-00000044 Autorizada" loading="lazy" width="470" height="498">
  <ol class="marks">
    <li><b>Factura</b>: el comprobante de la venta y su estado. Un toque lo abre.</li>
  </ol>
  <figcaption>Con Facturación, el detalle dice qué factura tiene la venta.</figcaption>
</figure>

### Exportar

**Exportar** baja una planilla (un archivo CSV) con la lista que estás viendo: las vendidas o las canceladas, con los filtros puestos y todas las filas, no solo las 200 dibujadas. Se abre bien en Excel en castellano.

Trae el día, la hora, el número, la unidad de negocio, el canal, el código de la plataforma, el cliente, quién atendió, el sector, los comensales, el medio de pago (un pago en partes sale como «Efectivo 5000 + QR 3000»), la propina, la cortesía, el total, el comprobante, el estado y el motivo de cancelación. El botón se apaga cuando la lista está vacía.

### Facturar lo que quedó sin facturar

Si la cuenta factura, debajo de las cifras aparece **Facturar N sin facturar**: hace una factura a consumidor final por cada venta de la lista que todavía no tiene. Lo de siempre es filtrar **Todo menos efectivo** y tocarlo al final del día. Está explicado en [Facturación electrónica]({{ '/es/projects/fornu/manual/facturacion/' | relative_url }}#fin-del-dia).

### En el celular

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/caja-ventas-telefono.jpg' | relative_url }}" alt="Ventas en un celular, en modo oscuro: el botón Exportar a lo ancho, el período con el enlace Otras fechas, el botón Filtros y las cifras en dos columnas" loading="lazy" width="390" height="844">
  <figcaption>Ventas en el celular. Los filtros esperan detrás de <b>Filtros</b>.</figcaption>
</figure>

En el celular los filtros se pliegan detrás de **Filtros**, que dice cuántos tenés puestos. Las fechas se esconden detrás de **Otras fechas**, las cifras van en dos columnas y cada venta es una tarjeta con el nombre del cliente al lado del número («#12 · Juan»).

## Movimientos de caja {#movimientos}

Es el libro de la caja: lo que entra y sale del cajón. Muchas cosas se anotan solas: la rendición de un mensajero, un gasto pagado en efectivo, el cobro en efectivo de una mesa, un adelanto o un sueldo pagado en efectivo, la diferencia de un arqueo. Lo demás lo cargás vos: el cambio que se pone a la mañana, lo que se lleva el dueño, una propina repartida.

La pestaña dice **Movimientos** y el título de la pantalla, **Movimientos de caja**. En la tablet del local es la pestaña **Movimientos** de quien entra con su PIN y tiene Caja.

<p class="perm"><span>Quién puede:</span> <span class="tag">Caja</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-movimientos.jpg' | relative_url }}" alt="Movimientos de caja de hoy: 27.250 pesos en la caja según el sistema, un adelanto y un sueldo pagados de la caja, un egreso por hielo cargado a mano con su botón Anular, y un ingreso de cambio para la caja" loading="lazy" width="1440" height="690">
  <ol class="marks">
    <li><b>Egreso</b> e <b>Ingreso</b>: cargar plata que sale o que entra.</li>
    <li><b>Efectivo en la caja ahora</b>: lo que debería haber en el cajón según el sistema.</li>
    <li><b>Origen</b>: de dónde salió cada movimiento. Este se cargó <b>A mano</b>.</li>
    <li><b>Anular</b>, solo en lo cargado a mano.</li>
  </ol>
  <figcaption>Un día con un adelanto y un sueldo pagados de la caja, y dos movimientos cargados a mano.</figcaption>
</figure>

Arriba hay tres cifras. **Efectivo en la caja ahora** es lo que debería haber en el cajón en este momento. **Ingresos del período** y **Egresos del período** suman todo lo que entró y salió en las fechas elegidas, sea del medio que sea. El período arranca en **Hoy** y llega hasta un año.

Cada fila dice **Cuándo**, el **Concepto** (con la nota y quién lo cargó), el **Medio**, el **Origen** y el importe en **Ingreso** o **Egreso**.

| Origen | De dónde sale | Cómo se corrige |
|---|---|---|
| **A mano** | Alguien lo cargó con **Ingreso** o **Egreso**. | Con **Anular**, hasta que se vuelva a contar la caja. |
| **Rendición** | Un mensajero rindió el efectivo de sus pedidos: «Rendición de Martín», con cuántos pedidos. | No se anula desde la caja. |
| **Gasto** | Un gasto pagado en efectivo. El origen es un enlace a Gastos. | Desde Gastos. |
| **Personal** | Un adelanto o un sueldo pagado en efectivo. | Desde Personal. |
| **Mesa** | El cobro y la propina en efectivo de una mesa: «Cobro de …», «Propina de …». | Si se deshace el cobro, aparece «Anulado: …». |
| **Arqueo** | El **Saldo inicial** al abrir, y el sobrante o faltante de una apertura o un cierre. | El próximo arqueo lo corrige. |

De las mesas solo llega el efectivo. Lo que se cobra con tarjeta, QR o transferencia va directo a lo que el arqueo espera de ese medio.

### Cargar un ingreso o un egreso

1. Tocá **Ingreso** si entra plata o **Egreso** si sale.
2. En **Cuánto**, poné el importe.
3. En **Medio** queda **Efectivo**, que mueve el efectivo del cajón. Si elegís otro medio, se suma a lo que el arqueo espera de ese medio.
4. Escribí **De dónde viene** o **Para qué sale**, hasta 80 letras. Al escribir, Fornu sugiere «Cambio para la caja», «Aporte del dueño», «Cobro de una deuda» o «Propinas» para un ingreso, y «Retiro del dueño», «Cambio para un mensajero», «Pago en el momento» o «Propinas repartidas» para un egreso.
5. Si hace falta, sumá una **Nota (opcional)**.
6. Tocá **Guardar** o apretá <kbd>Ctrl</kbd> + <kbd>Enter</kbd>. Aparece «Ingreso anotado» o «Egreso anotado».
{: .steps}

Si **Guardar** no se prende, el pie del diálogo dice qué falta: «Poné cuánta plata es», «Decí de dónde viene» o «Decí para qué sale».

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-egreso.jpg' | relative_url }}" alt="Diálogo Egreso de la caja con los campos Cuánto, Medio en Efectivo, Para qué sale y Nota, y el aviso de cargar los gastos del negocio en Gastos" loading="lazy" width="619" height="430">
  <figcaption>El egreso. El aviso de abajo recuerda dónde van los gastos del negocio.</figcaption>
</figure>

<div class="callout"><p class="callout-title">Importante</p><p>Si la plata sale para un gasto del negocio (la verdura, el gas, un arreglo), cargala en <a href="{{ '/es/projects/fornu/manual/compras-y-gastos/' | relative_url }}#gastos">Gastos</a> como pagada en efectivo. Sale de la caja sola y además cuenta en la rentabilidad. Un egreso a mano no cuenta como gasto.</p></div>

### Anular un movimiento

1. En la fila del movimiento, tocá **Anular**.
2. Fornu muestra «¿Anular «concepto»?» con el importe, el medio y la fecha.
3. Escribí **Por qué se anula**, por ejemplo «Lo cargué dos veces».
4. Tocá **Anular**. Aparece «Movimiento anulado».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-anular-movimiento.jpg' | relative_url }}" alt="El panel ¿Anular «Hielo para la barra»? con el importe, el medio y la fecha, y Por qué se anula escrito" loading="lazy" width="620" height="240">
  <figcaption>Anular un egreso cargado a mano.</figcaption>
</figure>

El movimiento sigue en la lista, más claro, con la marca **anulado** y el motivo. Los movimientos nunca se editan: si un importe estaba mal, se anula y se carga de nuevo.

Solo se anulan los cargados a mano, y solo hasta que la caja se vuelve a contar al abrirla o cerrarla. Después Fornu responde «La caja se contó después de este movimiento: cargá otro que lo corrija.» Los que vienen de otro lado dicen dónde se corrigen, por ejemplo «Sale de un gasto pagado en efectivo: se corrige desde Gastos.»

## Arqueo de caja {#arqueo}

Es la apertura y el cierre de la caja. Se abre contando el efectivo con el que arranca el turno. Se cierra contando cada medio de pago: el efectivo del cajón, el cierre del posnet para las tarjetas y lo que entró por QR, transferencia y Mercado Pago. Fornu compara lo contado con lo que dice el sistema y anota la diferencia, con su causa.

La pestaña dice **Arqueo** y el título, **Arqueo de caja**. En la tablet del local es la pestaña **Arqueo** de quien entra con su PIN y tiene Caja.

<p class="perm"><span>Quién puede:</span> <span class="tag">Caja</span> <span class="tag">Ver lo esperado</span> <span class="tag">Recontar la caja</span></p>

Con **Caja** se abre, se cuenta y se cierra. **Ver lo esperado** deja ver lo que el sistema espera antes de contar: sin él, el arqueo es ciego. **Recontar la caja** deja contar de nuevo después de confirmar un conteo. Los dos últimos necesitan Caja. El rol **Encargado/a** viene con los tres.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-arqueo.jpg' | relative_url }}" alt="Arqueo de caja con la caja abierta desde el 9/11 a las 10:26 con 30.000 pesos, la tabla Según el sistema por medio de pago y la lista vacía de cierres anteriores" loading="lazy" width="1440" height="640">
  <ol class="marks">
    <li><b>Cerrar caja</b>. Con la caja cerrada dice <b>Abrir caja</b>, y con un conteo ya confirmado, <b>Ver el conteo y cerrar</b>.</li>
    <li>El estado: <b>Abierta</b>, desde cuándo, quién la abrió y con cuánto.</li>
    <li><b>Según el sistema</b>: lo que debería haber de cada medio. Solo lo ve quien tiene Ver lo esperado.</li>
    <li><b>Cierres anteriores</b>: las últimas 30 cajas, con su diferencia.</li>
  </ol>
  <figcaption>La caja abierta, vista por alguien que puede ver lo esperado.</figcaption>
</figure>

Con la caja cerrada, la banda dice **Cerrada** y «Se cerró el 10/11, 23:40. Según el sistema hay $X en efectivo.» La primera vez de todas dice «Todavía no se abrió nunca: al abrirla, lo que cuentes es con lo que empieza.»

Si los mensajeros tienen efectivo sin rendir, arriba aparece «Los mensajeros todavía tienen $X de N pedidos en efectivo sin rendir: no está en la caja hasta que lo rindan.» con el enlace **Ir a rendir**. Conviene rendirlo antes de cerrar, porque esa plata no está en el cajón. Se explica en [Pedidos y delivery]({{ '/es/projects/fornu/manual/pedidos/' | relative_url }}).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-arqueo-tablet.jpg' | relative_url }}" alt="Pantalla de la tablet del local con las pestañas de Sofía, Arqueo elegida, y el botón Abrir caja sobre una caja que todavía no se abrió nunca" loading="lazy" width="1180" height="460">
  <ol class="marks">
    <li><b>Arqueo</b> y <b>Movimientos</b> en la tablet, para quien entra con su PIN y tiene Caja.</li>
    <li><b>Abrir caja</b>.</li>
  </ol>
  <figcaption>En la tablet de la cocina, la cajera abre y cierra sin salir de su sesión.</figcaption>
</figure>

### Qué es «Según el sistema»

- **Efectivo**: la suma de todos los movimientos de efectivo desde la apertura: el saldo inicial, los cobros de mesas en efectivo, las rendiciones, los gastos en efectivo y los ingresos y egresos cargados a mano.
- **Los demás medios**: los pedidos propios entregados mientras la caja estaba abierta y pagados con ese medio, más los cobros de mesas con ese medio (importe y propina), más los movimientos a mano de ese medio.

### Abrir la caja

1. Tocá **Abrir caja**. Se abre «Abrir la caja».
2. Arriba ves **Según el sistema**, lo que dejó el último cierre. La primera vez no aparece.
3. Contá el efectivo. Con **Contar el efectivo billete por billete** tildado, poné cuántos billetes hay de cada valor, de $20.000 a $10. Cada valor muestra su subtotal y la suma llena **Efectivo que hay**. Si lo destildás, escribí el total directo.
4. Debajo del total, Fornu compara con el último cierre: «Coincide con el último cierre.», «Faltan $X.» o «Sobran $X.». Si no coincide, escribí **Por qué no coincide**, por ejemplo «El dueño retiró al cerrar».
5. Tocá **Abrir caja**. Aparece «Caja abierta».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-abrir.jpg' | relative_url }}" alt="Diálogo Abrir la caja contando billete por billete: 3 billetes de 10.000 y 4 de 1.000 suman 34.000 pesos de efectivo" loading="lazy" width="880" height="690">
  <ol class="marks">
    <li><b>Efectivo que hay</b>: se llena solo con la suma de los billetes.</li>
    <li><b>Contar el efectivo billete por billete</b>. Viene tildado y cada equipo recuerda si alguien lo destilda.</li>
    <li>Tres billetes de $10.000 son $30.000.</li>
  </ol>
  <figcaption>La primera apertura de la caja: lo que se cuenta es con lo que empieza.</figcaption>
</figure>

Si lo contado no coincide con el último cierre, la diferencia se anota como un movimiento de **Arqueo**. Así la caja arranca con lo que realmente hay.

### Contar a ciegas

Un arqueo ciego es el que se hace sin saber cuánto debería dar. La cajera cuenta y confirma, y recién después ve si sobra o falta. Así nadie acomoda el conteo a lo que espera el sistema.

Lo decide el permiso **Ver lo esperado**. Quien tiene Caja sin ese permiso cuenta a ciegas, y la pantalla lo dice: «El arqueo es ciego: la diferencia se ve después de confirmar el conteo.»

| | Con **Ver lo esperado** | Sin él (ciego) |
|---|---|---|
| Caja abierta | La tabla **Según el sistema** y con cuánto se abrió. | «Arqueo ciego: lo que espera el sistema se ve después de confirmar el conteo.» y quién la abrió, sin el importe. |
| Al contar | **Según el sistema** y **Diferencia** al lado de cada medio, mientras se escribe. | Solo la columna **Contado**. |
| Un medio que el sistema espera en $0 | Ya cuenta como contado. | También pide una cifra, aunque sea 0. |
| Movimientos de caja | Los importes y el efectivo de ahora. | «—» mientras la caja está abierta: «se ve después de contar la caja». |
| Después de confirmar | Igual que antes. | Ve la diferencia. El conteo ya no se cambia. |

<div class="callout tip"><p class="callout-title">Consejo</p><p>Para que la cajera cuente a ciegas, dale a su rol <b>Caja</b> sin <b>Ver lo esperado</b>. Los roles se arman en <a href="{{ '/es/projects/fornu/manual/personal/' | relative_url }}#roles">Personal</a>.</p></div>

### Cerrar la caja: contar y confirmar

1. Tocá **Cerrar caja**. Se abre «Cerrar la caja · contá».
2. Para cada medio, poné lo **Contado**: el efectivo del cajón, el cierre del posnet para débito y crédito, y lo que entró por QR, transferencia y Mercado Pago. Si de un medio no entró nada, **Nada** pone 0 de un toque.
3. El efectivo se puede contar billete por billete, con la misma grilla que al abrir.
4. Tocá **Confirmar conteo · $total**. Si falta un medio, el pie lo dice: «Falta contar tarjeta de débito».
5. Aparece «Conteo confirmado.». El conteo queda guardado tal cual y no se puede cambiar.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-contar.jpg' | relative_url }}" alt="Diálogo Cerrar la caja, contá, en modo ciego: solo la columna Contado con 3.000 pesos en efectivo y 0 en los demás medios, y el botón Confirmar conteo por 3.000" loading="lazy" width="880" height="900">
  <ol class="marks">
    <li>El aviso del arqueo ciego y qué hay que contar.</li>
    <li><b>Contado</b>: una cifra por medio de pago.</li>
    <li><b>Contar el efectivo billete por billete</b>.</li>
    <li><b>Confirmar conteo</b>, con el total contado.</li>
  </ol>
  <figcaption>El conteo a ciegas: no se ve lo que espera el sistema.</figcaption>
</figure>

### Cerrar la caja: el resultado

Al confirmar, el diálogo pasa a «Cerrar la caja · resultado». Dice quién contó y a qué hora, y muestra cada medio con **Según el sistema**, **Contado** y **Diferencia**. La diferencia se lee en palabras: «Faltan $2.000», «Sobran $500» o «—» si coincide. La fila **Total** dice cuánto falta o sobra en total, o «Coincide».

1. Si algún medio no coincide, elegí **Por qué no coincide**: **Error en el vuelto**, **Venta sin cargar**, **Gasto o retiro sin cargar**, **Billete falso** u **Otro**.
2. Con **Otro**, escribí **Qué pasó**. Con las demás causas, la **Nota (opcional)** sirve para dar detalles.
3. Tocá **Cerrar la caja**. Aparece «Caja cerrada.» y se abre el detalle del cierre.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-resultado.jpg' | relative_url }}" alt="Resultado del cierre: el sistema esperaba 5.000 pesos en efectivo, se contaron 3.000, faltan 2.000. Abajo, las causas para elegir y el botón Cerrar la caja apagado" loading="lazy" width="880" height="900">
  <ol class="marks">
    <li>La diferencia en palabras: faltan $2.000 de efectivo.</li>
    <li><b>Por qué no coincide</b>: la causa, obligatoria cuando la diferencia pasa la tolerancia.</li>
    <li><b>Recontar</b>, por si el conteo estuvo mal. El candado indica que pide autorización.</li>
    <li>Por qué el botón está apagado: «Elegí por qué no coincide».</li>
    <li><b>Cerrar la caja</b>.</li>
  </ol>
  <figcaption>Faltan 2.000 pesos: antes de cerrar hay que decir por qué.</figcaption>
</figure>

Un faltante o sobrante de efectivo se anota en Movimientos como «Faltante del arqueo» o «Sobrante del arqueo», y el cajón queda con lo contado. Las diferencias en los otros medios solo quedan escritas en el cierre.

Si tocás **Cancelar** después de confirmar, el conteo queda guardado. El botón de arriba pasa a **Ver el conteo y cerrar** y te lleva de vuelta al resultado.

### Recontar

A veces el conteo estuvo mal: un billete pegado, el cierre del posnet que no se imprimió. **Recontar** permite contar de nuevo, y los dos conteos quedan guardados.

1. En el resultado, tocá **Recontar**. Se abre «Recontar la caja». **← Volver al resultado** vuelve sin cambiar nada.
2. Contá de nuevo cada medio y confirmá.
3. Si no tenés **Recontar la caja**, aparece «Hace falta autorización». Elegí en **¿Quién autoriza?** a alguien que lo tenga (al lado dice «· en turno» si está trabajando), que escriba su PIN y toque **Autorizar**.
4. El resultado muestra el nuevo conteo y lo dice: «Contó Sofía (autorizó Marta) a las 12:38 · 2 conteos, quedan todos guardados.»
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-autorizar.jpg' | relative_url }}" alt="Diálogo Hace falta autorización para Recontar la caja, con Marta elegida para autorizar y el teclado para su PIN" loading="lazy" width="880" height="560">
  <ol class="marks">
    <li><b>¿Quién autoriza?</b>: las personas que tienen el permiso.</li>
    <li>Su PIN, en el teclado.</li>
  </ol>
  <figcaption>Sofía no puede recontar sola: Marta la autoriza con su PIN.</figcaption>
</figure>

Si nadie del local tiene el permiso, Fornu lo avisa: «Nadie de este local puede autorizar esto con su PIN: se da en Personal → Configuración, en el rol de quien corresponda.»

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/caja-recontado.jpg' | relative_url }}" alt="Resultado después de recontar: dos conteos guardados, faltan 300 pesos de efectivo y el aviso de que cada medio coincide dentro de la tolerancia de 500 pesos" loading="lazy" width="880" height="580">
  <ol class="marks">
    <li>Quién contó, quién autorizó y cuántos conteos hubo.</li>
    <li>Faltan $300, pero la tolerancia es de $500: no hace falta elegir causa.</li>
  </ol>
  <figcaption>El segundo conteo da mucho más cerca.</figcaption>
</figure>

### La tolerancia

En Ajustes › Configuración, **Tolerancia del arqueo** dice cuánto puede no coincidir un medio de pago al cerrar sin tener que elegir por qué. Con una tolerancia de $500, si faltan $300 de efectivo el cierre dice «Cada medio coincide dentro de la tolerancia de $500.» y solo ofrece la nota. En $0, toda diferencia pide su causa.

La tolerancia vale para cada medio por separado, no para el total.

### Si entra plata después de contar

Si después del conteo entra un pedido o un movimiento, ese conteo deja de valer y el diálogo lo avisa: «Entró plata después del último conteo: contá de nuevo.». Contar de nuevo en ese caso no pide permiso.

La excepción es un movimiento cargado a mano después de contar. Ahí volver a contar es un recuento y Fornu lo dice: «Después del conteo se cargó un movimiento a mano: contarla de nuevo es un recuento, con «Recontar».»

### Ver un cierre anterior

**Cierres anteriores** lista las últimas 30 cajas: **Abrió**, **Cerró** (con cuántos conteos hubo), **Sistema**, **Contado** y **Diferencia** con su causa. Tocá una para ver «Cierre del …»:

- Quién la abrió, cuándo y con cuánto, la diferencia contra el cierre anterior con su nota, y quién la cerró.
- La tabla de cada medio.
- Cuántos billetes de cada valor se contaron, si se contó billete por billete.
- Los conteos anteriores, por ejemplo «Antes se contó faltan $2.000 (Sofía, 10/11, 12:38).»
- **Por qué no coincidió**, con la causa y la nota.

<div class="callout tip"><p class="callout-title">Consejo</p><p>Abrí la caja antes de pagar algo en efectivo. Si está cerrada, Gastos, los adelantos y los sueldos avisan «La caja está cerrada» y preguntan «¿Pagar igual?», porque esa plata saldría de una caja que nadie abrió y el arqueo no la cuadraría.</p></div>
