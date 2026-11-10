---
layout: manual
manual: pedidos
title: "Pedidos y delivery · Manual de Fornu"
description: "El tablero de pedidos, el pedido propio por teléfono, los pedidos de las plataformas, lo agotado, el historial, el efectivo de los mensajeros y los clientes."
permalink: /es/projects/fornu/manual/pedidos/
---

## El tablero {#tablero}

Es la pantalla de la cocina y del que despacha. Cada pedido aparece en **A confirmar** apenas entra, y suena. De ahí pasa por **En preparación** y **Listo para entregar** hasta **En camino**, y cada paso es un toque. Se actualiza solo: nadie tiene que recargar la página para ver lo nuevo.

Está en Pedidos › **En curso** (la página se llama **Pedidos**), y es también la pestaña **Pedidos** de la tablet de la cocina.

<p class="perm"><span>Quién puede:</span> <span class="tag">Cocina</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-tablero.jpg' | relative_url }}" alt="El tablero de pedidos de la demo con tres pedidos a confirmar, tres en preparación y tres listos para entregar, de cuatro marcas" loading="lazy" width="1440" height="720">
  <ol class="marks">
    <li><b>Impresora de comandas</b>: si está en línea, si quedaron comandas esperando o si falta configurarla.</li>
    <li><b>Agotados</b>: lo que se acabó hoy. Cuando hay algo agotado dice cuántos.</li>
    <li><b>Nuevo pedido</b>: un pedido propio, por teléfono o por mensaje. Atajo <kbd>N</kbd>.</li>
    <li><b>Todo</b> y una opción por marca o por estación: qué muestra este tablero.</li>
    <li><b>Confirmar · 15 min</b>, con el reloj para elegir otro tiempo y la cruz para cancelar.</li>
    <li><b>Ver sumado</b>: todo lo que está en preparación, sumado por producto.</li>
    <li><b>Listo</b>: el pedido terminó y está empaquetado.</li>
    <li><b>Deshacer</b> (durante dos minutos) y <b>Se lo llevó</b>.</li>
  </ol>
  <figcaption>El tablero de la demo, con cuatro marcas que salen de la misma cocina.</figcaption>
</figure>

### Qué dice cada columna

| Columna | Qué hay | Qué se hace |
|---|---|---|
| **A confirmar** | Los pedidos que acaban de entrar, por orden de llegada. El reloj de la tarjeta se pone ámbar a los 2 minutos y rojo a los 4. | Confirmarlo con su tiempo, o cancelarlo. |
| **En preparación** | Lo que se está cocinando, primero lo que vence antes. La tarjeta dice para qué hora tiene que estar y una barra se llena hasta esa hora; si se pasa, se pone roja y dice «Atrasado». | Marcarlo **Listo**. |
| **Listo para entregar** | Lo que espera al repartidor. Primero los pedidos cuyo repartidor de la plataforma ya llegó. | **Se lo llevó**, o esperar a que el mensajero lo tome desde su celular. |
| **En camino** | Lo que está en la calle, con quién lo lleva y desde qué hora. | **Entregado**. |

Abajo de las columnas, **Ver los cerrados de hoy** muestra lo entregado y lo cancelado del día.

En cada tarjeta se ven el número, la marca, el cliente, el total, lo que pidió con sus opciones y la nota. Un pedido de una plataforma lleva además su chip (**Rappi** o **PedidosYa**) y el número con el que lo pide el repartidor. Si una línea dice **agotado**, ese producto se marcó agotado después de que entró el pedido: avisale a la plataforma antes de confirmarlo. Si dice **sin vincular**, ese producto no está en la carta de la marca y no descuenta stock.

### Confirmar un pedido

1. Fijate en la tarjeta qué pidió y para qué marca es.
2. Tocá **Confirmar · 15 min**. El tiempo es el de siempre de esa marca (20 minutos si la marca no tiene uno).
3. Si hoy tarda otra cosa, tocá el reloj de al lado. Elegí 10, 15, 20, 25, 30, 40, 50 o 60 minutos, o escribí otro tiempo, y tocá **Confirmar**.
{: .steps}

El tiempo es lo que tarda en estar terminado y empaquetado: es lo que se le informa al mensajero para que pase a buscarlo. Al confirmar, Fornu descuenta del stock lo que lleva cada producto, sus opciones y el packaging de la marca, manda la comanda a cada estación que prepara una parte y, si el pedido vino de una plataforma, le avisa que lo aceptaste.

### Cancelar un pedido

Solo se cancela un pedido que todavía está **A confirmar**. Una vez confirmado, la cocina ya lo empezó.

1. Tocá la cruz de la tarjeta.
2. Elegí el motivo de un toque (**Falta un producto**, **No llegamos con el tiempo**, **Fuera de la zona de entrega**, **Lo canceló el cliente**) o escribilo.
3. Tocá **Cancelar pedido**.
{: .steps}

Como todavía no se había confirmado, no salió nada del stock. Si era de una plataforma, se le avisa que lo rechazaste.

### Marcar listo y entregar

1. Cuando el pedido está terminado y empaquetado, tocá **Listo**. Pasa a **Listo para entregar** y, si es de una plataforma, se le avisa.
2. Cuando sale, tocá **Se lo llevó**. Un pedido propio pasa a **En camino**; uno cargado desde la tablet de una plataforma se cierra, porque se lo llevó su repartidor.
3. Cuando llega, tocá **Entregado**.
{: .steps}

Lo normal es que los mensajeros propios marquen **Me lo llevo** y **Entregado** desde su celular: así queda quién lo llevó y el efectivo que cobró. Se explica en [En la cocina y en la calle]({{ '/es/projects/fornu/manual/cocina-y-reparto/' | relative_url }}#mensajero). Los pedidos de una plataforma con la tienda vinculada se mueven solos cuando el repartidor lo retira.

<div class="callout tip"><p class="callout-title">Consejo</p><p>Si marcaste <b>Listo</b> por error, tenés dos minutos para tocar <b>Deshacer</b> y el pedido vuelve a preparación. Pasados los dos minutos ya no vuelve.</p></div>

### Lo que hay que hacer, sumado

Cuando hay varios pedidos en preparación, el botón de la columna **En preparación** cambia la vista a **Ver sumado**: todos los productos de todos los pedidos y rondas, sumados. La parrilla ve «12 Papas fritas» en vez de buscarlas tarjeta por tarjeta.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-sumado.jpg' | relative_url }}" alt="La columna En preparación en la vista sumada: 12 papas fritas y 5 gaseosas en lata, de ocho pedidos" loading="lazy" width="1440" height="400">
  <ol class="marks">
    <li><b>Ver pedidos</b> vuelve a las tarjetas.</li>
    <li>Cada producto con la cantidad total. Tocalo y vuelven las tarjetas, con resaltados los pedidos que lo llevan.</li>
  </ol>
</figure>

### Ver el pedido entero

Tocá la tarjeta en cualquier lugar que no sea un botón, o su número. Se abre el pedido con sus productos y precios, el cliente con su teléfono (se toca para llamar, y al lado está **WhatsApp**), la dirección, la nota y qué cobrar, por ejemplo «Cobrar $ 4.500 en efectivo · paga con $ 10.000: llevá $ 5.500 de vuelto». Abajo están los pasos con su hora: cuándo entró, cuándo se confirmó y con cuántos minutos, quién lo llevó, cuándo se entregó. Si el local tiene salón o facturación, esos módulos suman sus pasos, como las rondas de una mesa o la factura.

### Mostrar solo una estación o una marca

Arriba de las columnas, **Todo** muestra todos los pedidos. Al lado aparece un botón por cada estación de la cocina y por cada marca que tiene pedidos en curso. Con una estación elegida, el tablero muestra solo los pedidos que tienen algo para esa estación y deja tenues las líneas de las otras. La elección queda guardada en ese dispositivo: la tablet de la parrilla queda en la parrilla aunque se apague.

### La impresora de comandas

Si la cocina trabaja con una impresora térmica, el tablero dice cómo está: **Impresora de comandas en línea**, cuántas comandas esperan la impresora, o que el agente de impresión no responde desde cierta hora. Con la impresora cargada, cada tarjeta en preparación dice si su comanda se imprimió, y el ícono de la impresora la vuelve a imprimir marcada como copia. Sin impresora, quien tiene el permiso **Ajustes** ve **Sin impresora de comandas · Configurar**. La impresora se carga en [Ajustes › Configuración]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#impresion). Trabajar solo con la tablet también es una forma válida.

### El sonido

Cada pedido nuevo suena con dos notas que suben, y el sonido se repite cada 20 segundos mientras haya algo esperando confirmación. Una plataforma que cancela un pedido ya confirmado suena con notas que bajan, y la tarjeta queda tachada con «No lo prepares» hasta que alguien toca **Entendido**. Si el navegador tiene el sonido bloqueado, el tablero lo dice: tocá cualquier parte de la pantalla o **Prender el sonido**. En una tablet, el tablero mantiene la pantalla encendida mientras está abierto, si el equipo lo permite.

### En el celular

<div class="shot-pair">
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/pedidos-tablero-celular.jpg' | relative_url }}" alt="El tablero en un celular: una columna por vez, elegida con pestañas, y la barra de módulos abajo" loading="lazy" width="585" height="1266">
    <ol class="marks">
      <li>Las columnas como pestañas, con cuántos pedidos tiene cada una.</li>
      <li>Los módulos, abajo.</li>
    </ol>
  </figure>
  <div>
    <p>En un celular se ve una columna por vez, elegida con pestañas que quedan fijas arriba. El tablero abre en la primera que tiene pedidos, y la pestaña <b>A confirmar</b> titila cuando entra algo y estás mirando otra.</p>
    <p>En la tablet de la cocina, parada o acostada, entran tres columnas: <b>A confirmar</b>, <b>En preparación</b>, y <b>Listo para entregar</b> con <b>En camino</b> compartiendo la tercera. En una PC entran las cuatro, cada una con su propio desplazamiento.</p>
  </div>
</div>

## Tomar un pedido propio {#pedido-propio}

Un pedido propio es el que toma el local por teléfono o por mensaje y reparten sus mensajeros. La pantalla sigue el orden de la llamada: primero quién es, después qué pide y al final cómo paga.

<p class="perm"><span>Quién puede:</span> <span class="tag">Cocina</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-nuevo.jpg' | relative_url }}" alt="El formulario Nuevo pedido con el teléfono de una clienta que ya pidió, su nombre y dirección completados, el botón Repetir su último pedido y la carta de la primera marca" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li><b>Propio</b> o una plataforma, solo si hay una tienda sin vincular.</li>
    <li><b>Teléfono</b>: desde 6 números aparece quién es, si ya pidió.</li>
    <li><b>Repetir su último pedido</b>, a los precios de hoy.</li>
    <li>La marca, y debajo su carta por categoría.</li>
    <li><b>Crear y empezar</b>: crea el pedido y lo confirma con el tiempo de la marca.</li>
  </ol>
</figure>

1. Tocá **Nuevo pedido** o apretá <kbd>N</kbd> en el tablero.
2. Escribí el teléfono. Si esa persona ya pidió, aparece abajo en «Ya pidieron con este número»: tocala, o apretá <kbd>Enter</kbd>, y se completan el nombre, el teléfono y la dirección. Da igual si escribís guiones, espacios o el +54 9.
3. Completá **Cliente** y **Dirección de entrega** si no se completaron solos.
4. Si ya había pedido, **Repetir su último pedido** carga lo de la última vez a los precios de hoy, sin lo que ya no se vende o se agotó.
5. Elegí la marca y tocá los productos. Si un producto tiene opciones (el punto, los extras, la bebida del combo), se abre una ventana para elegirlas, con la cantidad y una aclaración como «Sin pepinos».
6. En **Pago**, elegí **Cómo paga**: **Efectivo**, **Débito**, **Crédito**, **QR**, **Transferencia**, **Mercado Pago** o **Ya pagó**. Con efectivo, **Paga con** ofrece **Justo** y los billetes probables, y calcula el vuelto para que el mensajero lo lleve.
7. Si hace falta, escribí una nota para la cocina o el mensajero.
8. Tocá **Crear y empezar · 20 min**.
{: .steps}

El pedido entra directo a **En preparación**, con el tiempo de la marca: descuenta el stock y manda la comanda como cualquier pedido confirmado. Al pie del formulario se ve el total y lo que falta («Falta el cliente», «Falta cómo paga»), y el botón se prende cuando está todo.

<div class="callout tip"><p class="callout-title">Consejo</p><p>Un pedido es de una sola marca. Si cambiás de marca con productos cargados, Fornu pregunta antes de vaciar el pedido. Tocar dos veces el botón, o reintentar por un corte de conexión, nunca crea dos pedidos.</p></div>

## Pedidos de una plataforma cargados a mano {#plataformas}

Mientras la tienda de Rappi o PedidosYa de una marca no está vinculada, sus pedidos llegan solo a la tablet de la plataforma. Para que igual descuenten stock, impriman la comanda y cuenten en las ventas con los precios y la comisión de esa plataforma, se cargan en Fornu con el número que muestra esa tablet. A la plataforma no le llega nada de lo que se marque acá.

<p class="perm"><span>Quién puede:</span> <span class="tag">Cocina</span></p>

1. Tocá **Nuevo pedido** y elegí la plataforma arriba, al lado de **Propio**.
2. Escribí **N.º del pedido en Rappi** (o en PedidosYa): el que muestra la tablet, que es el que pide el repartidor.
3. Si querés, el nombre del cliente.
4. Cargá los productos. La carta aparece con los precios de esa plataforma, y se pueden cargar productos agotados porque la plataforma ya los vendió.
5. Tocá **Cargar y empezar**.
{: .steps}

El mismo número no se carga dos veces: Fornu avisa que ya está cargado y con qué número quedó. Estos pedidos se cierran cuando el repartidor se los lleva (**Se lo llevó**). Si la plataforma lo cancela después de confirmado, abrí el pedido y tocá **Rappi lo canceló** (o **PedidosYa lo canceló**), con el motivo. Lo que ya salió del stock queda descontado, porque se cocinó o se tira.

Cuando la tienda queda vinculada, sus pedidos entran solos al tablero y la plataforma deja de aparecer en **Nuevo pedido**. La vinculación se explica en [Ajustes]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#tiendas).

## Agotado por hoy {#agotados}

Cuando algo se acaba en medio del servicio, la cocina lo marca en un toque y deja de ofrecerse en todos lados: en los pedidos propios, en las tiendas de las plataformas vinculadas y en las opciones que lo usan. Vuelve solo cuando empieza el día siguiente de la cocina, así que nadie tiene que acordarse de volver a prenderlo.

<p class="perm"><span>Quién puede:</span> <span class="tag">Cocina</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-agotados.jpg' | relative_url }}" alt="El panel Agotado por hoy con el buscador y la lista de productos de cada marca, cada uno con Marcar agotado, y En las 2 marcas en los que venden dos marcas" loading="lazy" width="620" height="900">
  <ol class="marks">
    <li><b>Buscar un producto</b>, por nombre.</li>
    <li><b>Marcar agotado</b>, solo en esa marca.</li>
    <li><b>En las 2 marcas</b>: el mismo producto, agotado en todas las marcas que lo venden.</li>
    <li><b>Listo</b> cierra el panel.</li>
  </ol>
</figure>

1. Tocá **Agotados** en el tablero. También se abre desde el buscador (<kbd>Ctrl</kbd> <kbd>K</kbd>) escribiendo «agotado» o «sin stock».
2. Buscá el producto o recorré la lista, agrupada por marca.
3. Tocá **Marcar agotado**, o **En las 2 marcas** si lo venden varias.
4. Tocá **Listo**.
{: .steps}

Arriba de la lista queda **Agotado ahora**, con cada producto, desde qué hora y quién lo marcó, y el botón **Volver a ofrecer** por si vuelve a haber. Debajo de cada producto se ve qué pasó en cada plataforma: «Apagado en Rappi», «Avisando a Rappi…», o que no tiene tienda vinculada y hay que pausarlo en su tablet.

Si en [Ajustes › Configuración]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#pausar) está prendida la pausa por stock, aparece también **No alcanza el stock**: lo que la receta no puede hacer con lo que hay se pausa solo. Si el stock está mal cargado y en la cocina sí hay, **Hay: ofrecer igual** lo vuelve a ofrecer hasta que termine el día.

## Venta › Delivery {#venta}

**Venta** es la pantalla para vender desde un solo lugar, con una pestaña por cada punto de venta. **Delivery** muestra los pedidos que salen de la cocina, propios y de las plataformas, agrupados por estado, y abre el que tocás en un panel a la derecha sin perder la lista. Con el módulo Salón aparecen además **Mesas**, **Mostrador** y **Mostrador express**, que se explican en [Salón]({{ '/es/projects/fornu/manual/salon/' | relative_url }}).

<p class="perm"><span>Quién puede:</span> <span class="tag">Cocina</span> para Delivery</p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-venta.jpg' | relative_url }}" alt="Venta en el punto Delivery: un pedido en preparación a la izquierda y el mismo pedido abierto a la derecha, con su cliente, dirección, pago, pasos y el botón Listo" loading="lazy" width="1440" height="780">
  <ol class="marks">
    <li>Los puntos de venta. Se ven los que la persona puede usar.</li>
    <li>La caja: abierta desde qué hora, o cerrada.</li>
    <li><b>Nuevo pedido</b>, igual que en el tablero.</li>
    <li>Las tarjetas, con los mismos botones del tablero.</li>
    <li>El pedido abierto, con todo su detalle.</li>
    <li>El paso siguiente: <b>Confirmar</b>, <b>Listo</b>, <b>Se lo llevó</b> o <b>Entregado</b>.</li>
  </ol>
</figure>

Es cómoda para quien atiende el teléfono en el mostrador: toma el pedido, lo ve en el panel y lo sigue hasta que sale. En pantallas angostas, el pedido abierto ocupa toda la pantalla y al cerrarlo vuelve la lista.

## Historial de pedidos {#historial}

Los pedidos de cualquier día, propios y de las plataformas, con todo lo que pasó con cada uno. Sirve para un reclamo («¿a qué hora salió?»), para encontrar un pedido por el cliente o por el código de la plataforma, y para bajar el día a una planilla.

Está en Pedidos › **Historial** (la página se llama **Historial de pedidos**).

<p class="perm"><span>Quién puede:</span> <span class="tag">Pedidos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-historial.jpg' | relative_url }}" alt="Historial de pedidos de un día, con el selector de fecha, los filtros, el buscador, cuatro cifras y la lista de pedidos con su estado" loading="lazy" width="1440" height="700">
  <ol class="marks">
    <li>El día: flechas para el anterior y el siguiente, o la fecha.</li>
    <li><b>Todos</b>, <b>Entregados</b>, <b>Cancelados</b> o <b>En curso</b>.</li>
    <li>Buscar por cliente, número, producto o código de la plataforma.</li>
    <li>Pedidos, ventas, ticket promedio y cancelados del día.</li>
    <li><b>Exportar</b>: lo que se ve, en una planilla.</li>
  </ol>
</figure>

Tocá una fila para abrir el pedido con sus pasos. El día es el de la cocina: si el día empieza a las 6, un pedido de la 1 de la mañana cuenta en el día anterior. **Exportar** baja un archivo CSV que abre Excel, con el número, la hora, la marca, el canal, el código de la plataforma, el cliente, los productos, el total, el estado y el motivo de cancelación.

Desde el buscador general (<kbd>Ctrl</kbd> <kbd>K</kbd>), escribir un número de pedido o un cliente abre el historial en ese día con el pedido ya abierto. Con el módulo Facturación, el detalle muestra además la factura del pedido y, a quien puede facturar, el botón **Facturar**.

## Efectivo de los mensajeros {#efectivo}

Cada pedido propio pagado en efectivo queda a cargo de quien lo entregó hasta que lo rinde. Esta pantalla dice quién tiene cuánto y de qué pedidos, y registra la rendición con la diferencia si la hay. Conviene usarla cuando cada mensajero termina su turno.

Está en Pedidos › **Efectivo** (la página se llama **Efectivo de los mensajeros**).

<p class="perm"><span>Quién puede:</span> <span class="tag">Pedidos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-efectivo.jpg' | relative_url }}" alt="Efectivo de los mensajeros: una tarjeta con tres pedidos en efectivo entregados, el total de 33.000 pesos y el botón Rendir" loading="lazy" width="1440" height="600">
  <ol class="marks">
    <li>Quién tiene el efectivo y de cuántos pedidos. Lo que salió con <b>Se lo llevó</b> desde la cocina queda en «Sin mensajero marcado».</li>
    <li><b>Rendir</b>, con el total que tendría que entregar.</li>
    <li><b>Últimas rendiciones</b>: quién rindió, cuánto debía, cuánto entregó y la diferencia.</li>
  </ol>
</figure>

1. Tocá **Rendir** en la tarjeta de la persona.
2. Revisá **Pedidos que rinde**: vienen todos marcados. Desmarcá uno si lo rinde después.
3. En **Entregó**, escribí lo que entregó de verdad. Fornu dice si coincide, si faltan o si sobran.
4. Si no coincide, escribí por qué (por ejemplo, «Le faltó cambio en un pedido»). Es obligatorio.
5. Tocá **Guardar rendición**.
{: .steps}

Lo entregado entra a la caja como un movimiento, «Rendición de» y el nombre, así el arqueo lo cuenta. Inicio avisa cuando quedó efectivo de días anteriores sin rendir. El mensajero ve en su celular cuánto tiene encima. Lo cobrado con tarjeta, QR o lo que ya estaba pagado no entra acá.

## Clientes {#clientes}

Las personas que el local conoce: los habituales, los dueños, el personal. Cada uno puede tener un descuento que se aplica solo cuando su venta es de él, por ejemplo los dueños al 100% y el personal al 50%, y el descuento queda registrado con el motivo elegido o con su nombre. Sus datos también completan solos un pedido propio cuando se escribe su teléfono.

Está en Pedidos › **Clientes**.

<p class="perm"><span>Quién puede:</span> <span class="tag">Ajustes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/pedidos-clientes.jpg' | relative_url }}" alt="La lista de clientes con Dueños al 100 por ciento y Personal al 50 por ciento" loading="lazy" width="1440" height="300">
  <ol class="marks">
    <li><b>Agregar</b> un cliente.</li>
    <li>Su descuento automático y el motivo con que queda registrado.</li>
  </ol>
</figure>

1. Tocá **Agregar**, o una fila para cambiarla.
2. Escribí el **Nombre** como lo conoce el local («Dueños», «Personal», «Ana Pérez»), y si querés el teléfono, el email y la dirección.
3. En **Descuento automático (%)**, de 0 a 100, lo que se le descuenta. En **Motivo del descuento**, con qué motivo queda registrado (los motivos se arman en [Ajustes › Motivos de descuento]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#descuentos)), o **Su nombre**.
4. Tocá **Guardar**.
{: .steps}

Un cliente no se borra: se apaga **Activo** al editarlo. El descuento se aplica al asignar el cliente a una mesa o a una venta express en el salón, como se explica en [Salón]({{ '/es/projects/fornu/manual/salon/' | relative_url }}#cliente).

<div class="callout tip"><p class="callout-title">Consejo</p><p>Cargar a «Dueños» con su 100% es la forma de registrar lo que se consume en la casa: la venta se cierra sin cargo y queda a la vista en la lista de ventas.</p></div>
