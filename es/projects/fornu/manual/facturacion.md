---
layout: manual
manual: facturacion
title: "Facturación electrónica · Manual de Fornu"
description: "Qué factura emite la cuenta, cómo se configura con ARCA, cómo se factura a mano, en la mesa y al final del día, y qué hacer con las facturas que esperan o se rechazan."
permalink: /es/projects/fornu/manual/facturacion/
---

## Qué factura Fornu {#que-se-emite}

Con la facturación prendida, Fornu le pide el CAE a ARCA por cada venta que tiene que facturarse y la factura queda guardada en el pedido, con su número, su CAE y su QR. Algunas ventas se facturan solas al entregarse y otras se facturan a mano, cuando el cliente pide factura con su DNI o su CUIT.

La letra depende de la condición frente al IVA de la cuenta, que se elige en Ajustes › Configuración, **Condición frente al IVA**:

| La cuenta es | Al consumidor final | A un cliente con CUIT responsable inscripto o monotributista | A otro cliente identificado (con DNI, o con CUIT exento) |
|---|---|---|---|
| **Monotributo** | Factura C | Factura C | Factura C |
| **Responsable inscripto** | Factura B, con el IVA contenido | Factura A, con el neto y el IVA 21% aparte | Factura B |

La Factura C lleva solo el total. La B lleva el total y abajo el **IVA contenido (21%)**. La A separa **Neto gravado**, **IVA 21%** y **Total**, y lleva la razón social del cliente. Una factura se anula con una nota de crédito de la misma letra.

Facturación electrónica es un módulo de la cuenta. Si está apagado, no aparecen Balances › Facturas, Ajustes › Facturación ni los botones **Facturar**.

| Permiso | Qué deja hacer |
|---|---|
| **Facturar** | Hacer la factura de una venta a mano, con DNI o CUIT si la piden. |
| **Ver facturas** | Ver el listado de facturas y notas de crédito, mandar de nuevo las que esperan y anular. |
| **Configurar la facturación** | Cargar los datos fiscales y el punto de venta, y probar la conexión con ARCA. |

**Administración** tiene los tres. El rol **Encargado/a** no trae ninguno: se suman en [Personal]({{ '/es/projects/fornu/manual/personal/' | relative_url }}#roles) a quien corresponda.

<div class="callout"><p class="callout-title">Importante</p><p>En la demo, las facturas salen de un ARCA de prueba. Tienen CAE y QR, pero dicen que no tienen validez fiscal: el comprobante muestra «Comprobante de prueba: lo autorizó un simulador de ARCA y no tiene validez fiscal.» y al imprimirse sale «Comprobante de prueba · sin validez fiscal». En la demo, además, Ajustes › Facturación no se puede cambiar: «En la demo esto no se cambia: la usa todo el que la prueba. En tu cuenta, sí.»</p></div>

## Configurar la facturación {#configurar}

Se hace una vez, en Ajustes › Facturación. Lo hace el dueño o quien administra la cuenta, con la clave fiscal a mano.

<p class="perm"><span>Quién puede:</span> <span class="tag">Configurar la facturación</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/facturacion-ajustes.jpg' | relative_url }}" alt="Ajustes, Facturación con la facturación prendida: el botón Apagar la facturación, el aviso de que Fornu está conectado a un ARCA de prueba, Facturando desde el 10/11/2026, los datos fiscales completos e Identificar al cliente desde, y las casillas de Qué se factura solo" loading="lazy" width="1440" height="850">
  <ol class="marks">
    <li><b>Apagar la facturación</b>. Con la facturación apagada, en su lugar está <b>Prender la facturación</b>, que guarda además lo que esté escrito en el formulario.</li>
    <li>El estado de la conexión con ARCA en este servidor. Acá, un ARCA de prueba: las facturas salen con CAE y QR, sin validez fiscal.</li>
    <li><b>Facturando</b> desde el día en que se prendió.</li>
    <li>Los datos fiscales, con el <b>Punto de venta</b> y <b>Identificar al cliente desde</b>, el tope de ARCA para facturar sin DNI ni CUIT.</li>
    <li><b>Qué se factura solo</b>: los canales y los medios de pago que se facturan al entregarse.</li>
  </ol>
  <figcaption>Ajustes › Facturación en una cuenta monotributo que ya factura.</figcaption>
</figure>

### Cargar los datos fiscales

Salen impresos en cada factura.

| Campo | Qué va |
|---|---|
| **CUIT** | El del negocio. Obligatorio. |
| **Razón social** | Como figura en ARCA. Obligatorio. |
| **Domicilio comercial** | Obligatorio. |
| **Punto de venta** | «El que se dio de alta en ARCA para facturar por web service.» Obligatorio. |
| **Ingresos Brutos** | «El número, o «Exento».» |
| **Inicio de actividades** | La fecha. |
| **Identificar al cliente desde** | El total desde el cual ARCA pide el DNI o el CUIT del cliente. Viene en $10.000.000 (ver [el tope de ARCA](#tope)). |

Arriba, el texto dice qué emite la cuenta: «Monotributo, que emite Factura C.» o «Responsable inscripto, que emite Factura A y B con IVA 21%.». Para cambiarlo, **Cambiarla en Configuración**.

### Delegar en ARCA y probar la conexión

Fornu factura en nombre del negocio. Para eso, el CUIT del negocio le delega la facturación electrónica al de Fornu en el sitio de ARCA. El bloque **Conexión con ARCA** muestra los pasos:

1. Entrá al sitio de ARCA con la clave fiscal del CUIT de la cuenta.
2. Abrí el **Administrador de Relaciones de Clave Fiscal** y elegí **Nueva relación**.
3. Buscá **ARCA → WebServices → Facturación electrónica**.
4. Como representante, poné el CUIT de Fornu, que la pantalla muestra en ese paso.
5. Volvé a Fornu y tocá **Probar la conexión**. ARCA puede tardar unas horas en tomar la delegación.
{: .steps}

**Probar la conexión** necesita el CUIT guardado. Lo que puede contestar:

| Respuesta | Qué quiere decir |
|---|---|
| «ARCA responde: el punto de venta N todavía no tiene comprobantes.» | Todo bien. Es un punto de venta nuevo. |
| «ARCA responde: el último comprobante del punto de venta N es el número M.» | Todo bien. La próxima factura sigue esa numeración. |
| «ARCA no ve que el CUIT … haya delegado la facturación electrónica en el de Fornu (…).» | La delegación falta o ARCA todavía no la tomó. Revisá los pasos o esperá unas horas. |
| «ARCA no tiene ese punto de venta habilitado para facturar por web service.» | Ese punto de venta no es de web service. Revisalo en ARCA o cargá el correcto. |
| «No se pudo hablar con ARCA: …» | ARCA no contestó. Probá más tarde. |

Si arriba aparece «Este servidor todavía no está conectado con ARCA: por ahora no se puede facturar.», todavía no se puede facturar desde ahí: **Prender la facturación** y **Probar la conexión** quedan apagados. Si la cuenta está conectada a un ambiente de prueba, la pantalla también lo avisa, y esas facturas no tienen validez fiscal. En Ajustes › Integraciones, la tarjeta **ARCA · Factura electrónica** dice en una línea cómo está la conexión.

### Elegir qué se factura solo

En **Qué se factura solo** se eligen dos cosas:

- **Canales**: «Los pedidos de estos canales se facturan al entregarse, a consumidor final. Los demás, a mano desde el pedido.» Vienen tildados **Pedidos propios**, **Rappi** y **PedidosYa**. **Salón** viene sin tildar, porque en la mesa la factura se pide al cobrar.
- **Medios de pago**: «Y las ventas pagadas con estos medios, de cualquier canal: la tarjeta, el QR y las transferencias dejan rastro.» No viene ninguno tildado. Si tildás **Tarjeta de débito**, las mesas pagadas con débito se facturan solas aunque **Salón** no esté tildado.

Después tocá **Guardar**, que se prende cuando cambiaste algo.

Lo automático factura a consumidor final lo entregado desde el día en que se prendió la facturación, y mira hacia atrás hasta 5 días hábiles: lo más viejo se factura a mano. Si apagás y volvés a prender la facturación, la fecha vuelve a empezar, y lo entregado mientras estuvo apagada no se factura solo.

### Prender la facturación

1. Completá CUIT, razón social, domicilio y punto de venta.
2. Tocá **Prender la facturación**. Aparece «Facturación prendida».
3. Arriba queda **Facturando** «desde el … Lo entregado antes se factura a mano, desde el pedido.»
{: .steps}

Si falta algún dato, Fornu avisa: «Completá antes el CUIT, la razón social, el domicilio y el punto de venta.». Para dejar de facturar, **Apagar la facturación**.

## Facturar una venta a mano {#a-mano}

Es para el cliente que pide factura con su DNI o su CUIT, o para una venta que no se facturó sola: una mesa, un pedido de antes de prender la facturación, uno de un canal sin tildar.

<p class="perm"><span>Quién puede:</span> <span class="tag">Facturar</span></p>

El botón **Facturar** aparece en tres lugares:

- En Balances › Ventas, en la columna **Comprobante** de cada venta sin factura.
- En la línea **Factura** del detalle de un pedido.
- En una mesa cerrada del Salón.

Si la última factura fue rechazada o anulada, dice **Facturar de nuevo**. No aparece en pedidos cancelados ni en los que esperan confirmación. Una mesa se factura cuando está cobrada. Un pedido propio se puede facturar aunque todavía se esté preparando.

1. Tocá **Facturar** en la venta. Se abre «Facturar el pedido #N», o «Facturar Mesa 4» si es una mesa.
2. Elegí a quién: **Consumidor final** (el de siempre), **Con DNI** o **Con CUIT**.
3. Con DNI o CUIT, escribí el número. Desde el séptimo dígito aparecen debajo los clientes a los que ya se les facturó con ese número: nombre, CUIT o DNI, condición, domicilio y la última vez. Tocá el que es y se completa todo.
4. Completá el **Nombre**, o la **Razón social** si es con CUIT. Con CUIT, elegí la **Condición frente al IVA**: **Responsable inscripto**, **Monotributista**, **Exento** o **Consumidor final**. Para responsable inscripto y monotributista, la razón social es obligatoria.
5. Tocá **Facturar $X**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/facturacion-a-mano.jpg' | relative_url }}" alt="El panel Facturar el pedido #6 con Con CUIT elegido, los primeros siete números de un CUIT y debajo el cliente ya facturado Distribuidora Ejemplo S.A., responsable inscripto, con su domicilio y la última vez" loading="lazy" width="620" height="900">
  <ol class="marks">
    <li><b>Consumidor final</b>, <b>Con DNI</b> o <b>Con CUIT</b>.</li>
    <li>El número. Desde el séptimo dígito busca.</li>
    <li>Un cliente al que ya se le facturó con ese número: un toque completa todo.</li>
    <li><b>Facturar $ …</b>.</li>
  </ol>
  <figcaption>Facturar un pedido a una empresa que ya pidió factura antes.</figcaption>
</figure>

«La factura se guarda ahora y ARCA la autoriza en unos segundos. Si ARCA no responde, se vuelve a intentar sola.» Mientras tanto la venta dice **Sin facturar (esperando a ARCA)**, y cuando ARCA la autoriza pasa a **Facturada** con su número.

Lo que puede contestar Fornu:

| Mensaje | Qué hacer |
|---|---|
| «El pedido #N ya tiene la Factura B …: anulala antes de facturarlo de nuevo.» | Anulá la factura vieja desde [Facturas](#facturas), o usá **Corregir**. |
| «Desde $X hay que identificar al cliente con DNI o CUIT.» | El total pasa [el tope de ARCA](#tope): facturá **Con DNI** o **Con CUIT**. |
| «La Factura A lleva la razón social del cliente.» | Completá la razón social. |
| «Un cliente que factura con su condición frente al IVA se identifica con su CUIT.» | Elegí **Con CUIT**. |
| «La facturación está apagada: prendela en Facturación.» | Prendela en Ajustes › Facturación. |
| «La cuenta de … se factura cuando está cobrada.» | Cobrá la mesa primero. |

<div class="callout tip"><p class="callout-title">Consejo</p><p>Los clientes que piden factura siempre se cargan una sola vez. La próxima, alcanza con los primeros dígitos del CUIT para que aparezca con su razón social, su condición y su domicilio.</p></div>

## Facturar al cobrar una mesa {#en-la-mesa}

En el Salón, la factura se pide en el mismo momento de cobrar. El cobro está explicado en [Salón]({{ '/es/projects/fornu/manual/salon/' | relative_url }}#cobrar). Acá va solo la parte de la factura.

<p class="perm"><span>Quién puede:</span> <span class="tag">Cobrar mesas</span></p>

1. En «Cobrar Mesa N», bajá hasta **Comprobante** y prendé **Facturar esta cuenta**.
2. Elegí la **Condición frente al IVA** del cliente. Si es responsable inscripto, monotributista o exento, el **Documento** queda en CUIT. Para un consumidor final podés dejarlo **Sin identificar** o pedir DNI o CUIT.
3. Escribí el número. «Si ya se le facturó, aparece abajo y se completa solo.»
4. Completá la **Razón social** (o el **Nombre**), el **Domicilio**, que va en la factura, y si querés el **Teléfono** y el **Email** («Para mandarle el comprobante.»).
5. Fornu muestra qué va a salir, por ejemplo «Saldrá una Factura B por $ 4.500 a consumidor final. ARCA la autoriza en unos segundos.», y el botón pasa a **Cobrar $ 4.500 en Efectivo y facturar**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/facturacion-mesa.jpg' | relative_url }}" alt="Bloque Comprobante del cobro de una mesa: Facturar esta cuenta prendido, condición Responsable inscripto, un CUIT escrito y debajo el cliente ya facturado Distribuidora Ejemplo S.A." loading="lazy" width="700" height="440">
  <ol class="marks">
    <li><b>Facturar esta cuenta</b>.</li>
    <li><b>Condición frente al IVA</b> del cliente.</li>
    <li>El CUIT. Si ya se le facturó, aparece abajo.</li>
    <li>El cliente conocido: un toque completa razón social, condición y domicilio.</li>
  </ol>
  <figcaption>Un cliente de la demo que ya pidió factura antes.</figcaption>
</figure>

Si la facturación está apagada, el cobro lo avisa: «La facturación está apagada en esta cuenta: prendela en Facturación para emitir el comprobante.». Si la factura se pidió cuando la facturación no estaba lista, la mesa se cierra igual. La venta queda **Sin facturar (pedida: …)** con el motivo, su historia dice «Comprobante pedido · espera: …» y la factura sale sola apenas se puede. Mientras tanto también se puede facturar a mano.

## Facturar lo que quedó sin facturar {#fin-del-dia}

Muchos locales facturan al final del día lo que se cobró con tarjeta, QR o transferencia. En Balances › Ventas, filtrás eso y lo facturás todo de una vez.

<p class="perm"><span>Quién puede:</span> <span class="tag">Facturar</span> <span class="tag">Caja</span></p>

1. Entrá a Balances › Ventas y dejá el período en **Hoy**.
2. En **Medio de pago**, elegí **Todo menos efectivo**. Con **Comprobante** › **Sin facturar** ves solo lo pendiente.
3. Debajo de las cifras, tocá **Facturar N sin facturar**.
4. Fornu pregunta «¿Facturar N ventas por $X?» y explica: «Sale una factura a consumidor final por cada una, las que muestra la lista ahora. La que necesite CUIT o DNI se factura sola, desde su fila.» Tocá **Facturar N**.
5. Aparece «N facturas pedidas a ARCA.». Cada venta dice **Sin facturar (esperando a ARCA)** hasta que ARCA la autoriza.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/facturacion-sin-facturar.jpg' | relative_url }}" alt="Ventas con dos pedidos propios sin facturar, cada uno con su botón Facturar, y el botón Facturar 2 sin facturar debajo de las cifras" loading="lazy" width="1440" height="450">
  <ol class="marks">
    <li><b>Comprobante</b>: filtrá las facturadas o las sin facturar.</li>
    <li><b>Facturar 2 sin facturar</b>: todas las de la lista, de una vez.</li>
    <li><b>Facturar</b> en cada fila: una sola venta, con DNI o CUIT si hace falta.</li>
  </ol>
  <figcaption>Dos ventas pendientes en la demo.</figcaption>
</figure>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/facturacion-esperando.jpg' | relative_url }}" alt="Las dos ventas ahora dicen Sin facturar esperando a ARCA, y abajo el aviso 2 facturas pedidas a ARCA" loading="lazy" width="1440" height="380">
  <ol class="marks">
    <li>Las dos ventas esperan el CAE: «(esperando a ARCA)».</li>
    <li>El aviso: «2 facturas pedidas a ARCA.»</li>
  </ol>
  <figcaption>Unos segundos después, las dos pasan a Facturada.</figcaption>
</figure>

Entran todas las ventas que muestra la lista, no solo las 200 dibujadas, siempre que estén entregadas, tengan un total mayor a cero, no tengan una factura vigente y no hayan pedido factura con DNI o CUIT. Esas últimas se facturan solas, a nombre de su cliente. Se facturan hasta 300 ventas por vez.

Si alguna no sale, el aviso lo dice con el primer motivo: «… M ventas quedaron sin facturar: …».

## Balances › Facturas {#facturas}

Es el listado de las facturas y notas de crédito emitidas, con su CAE. Sirve para pasarle al contador lo del mes, reimprimir una factura, mandar de nuevo una que espera o anular una que salió mal.

<p class="perm"><span>Quién puede:</span> <span class="tag">Ver facturas</span></p>

- El período arranca en **Este mes** y llega hasta un año. El buscador encuentra por **Número, cliente o pedido…**.
- Cuatro cifras: **Comprobantes** (las autorizadas, que al tocarla muestra todas), **Facturado** (las facturas menos las notas de crédito), **IVA**, y **Esperando o rechazadas**, que al tocarla deja solo esas.
- Cada fila dice **Fecha**, **Comprobante** (por ejemplo **Factura B** 00003-00000012), **Pedido**, **Cliente**, **Neto**, **IVA**, **Total** (las notas de crédito en negativo) y **Estado**.
- Si en el período hay facturas de prueba, lo avisa: «Las facturas de este período son de prueba: no tienen validez fiscal.»

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/facturacion-facturas.jpg' | relative_url }}" alt="Balances, Facturas del mes: el período y el buscador, las cifras Comprobantes 46, Facturado 850.000 pesos, IVA 0 y Esperando o rechazadas 1, y la lista con una factura a una empresa, una rechazada, una nota de crédito en negativo, otra factura a la misma empresa y una anulada" loading="lazy" width="1440" height="720">
  <ol class="marks">
    <li>El período y el buscador.</li>
    <li>Las cifras. <b>Esperando o rechazadas</b> deja solo las que tienen un problema.</li>
    <li>Una factura <b>Rechazada</b>: ARCA no la aceptó.</li>
    <li>Una nota de crédito, en negativo. Dos filas más abajo está la factura que anuló, <b>Anulada</b>.</li>
    <li><b>Exportar</b>.</li>
  </ol>
  <figcaption>Las facturas del mes, con una rechazada y una anulada con su nota de crédito.</figcaption>
</figure>

| Estado | Qué quiere decir |
|---|---|
| **Autorizada** | Tiene CAE. Es válida. |
| **Esperando a ARCA** | Está guardada y Fornu la sigue mandando hasta que ARCA conteste. |
| **Rechazada** | ARCA no la aceptó. Al pasar el mouse por el estado se lee el motivo. |
| **Anulada** | Se anuló con una nota de crédito. |

Las anuladas y las rechazadas aparecen más claras.

### Ver, imprimir o mandar de nuevo una factura

Tocá una fila (o la línea **Factura** del detalle de un pedido). Se abre el comprobante como se imprime: los datos del negocio, la letra con su código, el número, la fecha, el CUIT, Ingresos Brutos e inicio de actividades, el cliente y el pedido, el detalle con **Cant.**, **Detalle**, **Precio** e **Importe**, los totales según la letra, el **CAE** con su vencimiento y el QR de ARCA.

| Botón | Qué hace |
|---|---|
| **Imprimir** | Imprime la factura. Solo cuando está autorizada. |
| **Mandar de nuevo** | La manda a ARCA ya, si está esperando o fue rechazada. Aparece «Se manda de nuevo a ARCA». |
| **Anular** | Emite una nota de crédito por el total. |
| **Corregir** | Anula y factura de nuevo a otro cliente, todo junto. Necesita además **Facturar**. |
| **Listo** | Cierra. |

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/facturacion-factura.jpg' | relative_url }}" alt="Una Factura C abierta: los datos del negocio, la letra C con su código, el número y la fecha, el cliente Distribuidora Ejemplo S.A. responsable inscripto con su CUIT y domicilio, una pizza, el total, el QR y el CAE con su vencimiento, y los botones Anular, Corregir, Imprimir y Listo" loading="lazy" width="880" height="760">
  <ol class="marks">
    <li>El <b>CAE</b> y su vencimiento.</li>
    <li>El QR de ARCA.</li>
    <li><b>Anular</b>.</li>
    <li><b>Corregir</b>.</li>
    <li><b>Imprimir</b>.</li>
  </ol>
  <figcaption>Una factura C a un responsable inscripto, autorizada por el ARCA de prueba.</figcaption>
</figure>

### Anular una factura con nota de crédito

1. Abrí la factura y tocá **Anular**.
2. Fornu pregunta «¿Anular la Factura B …?» y avisa: «Se emite una nota de crédito por el total. El pedido queda sin factura y se puede facturar de nuevo.»
3. Tocá **Anular con nota de crédito**. Aparece «Nota de crédito pedida a ARCA» y se abre la nota de crédito.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/facturacion-nota-de-credito.jpg' | relative_url }}" alt="Una Nota de crédito C abierta: dice Anula la Factura C 00003-00000043, con su producto, el total, el QR y su propio CAE" loading="lazy" width="880" height="640">
  <ol class="marks">
    <li>Qué factura anula.</li>
    <li>Su propio CAE.</li>
  </ol>
  <figcaption>La nota de crédito, con su CAE.</figcaption>
</figure>

### Corregir una factura con el cliente mal

Cuando el CUIT, el nombre o la condición estaban mal, **Corregir** hace las dos cosas en un paso.

1. Abrí la factura y tocá **Corregir**. Se abre «Corregir la Factura B …»: «Sale una nota de crédito por esta factura y una nueva a quien corresponda, las dos juntas. Cargá a quién va la nueva.»
2. Cargá el cliente correcto, como al facturar a mano.
3. Tocá **Anular y facturar de nuevo**.
{: .steps}

Salen las dos juntas o ninguna, así la venta nunca queda con la factura anulada y sin la nueva.

### Exportar para el contador

**Exportar** baja una planilla (un archivo CSV) con los comprobantes autorizados del período: fecha, comprobante, número, cliente, neto, IVA, total, CAE, pedido, unidad de negocio, canal y estado. Se abre bien en Excel en castellano. El botón se apaga si en el período no hay ninguno autorizado.

<div class="callout tip"><p class="callout-title">Consejo</p><p>A principio de mes, elegí <b>Mes pasado</b> y tocá <b>Exportar</b>: es el archivo que pide el contador para el libro de ventas.</p></div>

## Cuando ARCA no responde o rechaza {#arca}

### Si ARCA no responde

La factura se guarda igual como **Esperando a ARCA** y la venta sigue su curso: la cocina nunca espera a ARCA. Fornu la vuelve a mandar sola a los 10 segundos, a los 30, a los 2 minutos, a los 5, a los 15, y después cada 15 minutos, sin rendirse. Al abrirla dice «Esperando a ARCA: … Se vuelve a intentar sola, la próxima vez a las 13:05.»

Para no esperar, **Mandar de nuevo** la manda en el momento. Si se perdió una respuesta en el camino, Fornu primero le pregunta a ARCA cuál fue su último comprobante, así una venta nunca queda con dos números.

### Si ARCA la rechaza

La factura queda **Rechazada** y al abrirla dice «No salió:» con el motivo que dio ARCA. Corregí lo que falta (por ejemplo, un dato en Ajustes › Facturación) y tocá **Mandar de nuevo**: sale con la fecha de hoy.

- Si mientras tanto el pedido se facturó de otra forma, Fornu responde «El pedido ya tiene otra factura: esta queda rechazada.»
- Si lo rechazado es una nota de crédito, la factura que anulaba sigue vigente.
- Si se apaga el módulo, no se factura nada nuevo, pero las facturas ya guardadas siguen buscando su CAE.

## El tope de ARCA para identificar al cliente {#tope}

ARCA pide el DNI o el CUIT del cliente desde cierto total. Ese monto va en Ajustes › Facturación, **Identificar al cliente desde**: «Desde este total, ARCA pide el DNI o CUIT del cliente (hoy, $ 10.000.000). Esos pedidos se facturan a mano.»

Una venta que se factura sola y llega a ese total queda **Rechazada** con «Desde $X hay que identificar al cliente con DNI o CUIT: facturalo a mano.». Facturala a mano, **Con DNI** o **Con CUIT**. Si ARCA cambia el monto, actualizá el campo.
