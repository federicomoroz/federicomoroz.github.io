---
layout: manual
manual: ajustes
title: "Ajustes · Manual de Fornu"
description: "Las unidades de negocio con sus canales y tiendas, los dispositivos, las estaciones e impresoras, los medios de pago, los descuentos, las integraciones, los usuarios y la configuración de la cuenta."
permalink: /es/projects/fornu/manual/ajustes/
---

## Unidades de negocio {#unidades}

Son las marcas que salen de esta cocina, como Doble Smash o Pollo Crocante en la demo. Todas comparten la misma cocina y el mismo stock, y cada una tiene sus canales de venta, lo que se queda cada canal y lo que llevan sus pedidos además de la receta. La pestaña dice **Unidades** y el título, **Unidades de negocio**.

<p class="perm"><span>Quién puede:</span> <span class="tag">Ajustes</span> <span class="tag">Carta</span> (publicar la carta)</p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-unidades.jpg' | relative_url }}" alt="La lista de unidades de negocio de la demo, cada una con sus canales y comisiones, la espera sugerida, los adicionales, sus tiendas de Rappi y PedidosYa y el botón Publicar en Rappi" loading="lazy" width="1440" height="560">
  <ol class="marks">
    <li><b>Unidad de negocio</b>: crea una marca nueva.</li>
    <li><b>Canales</b>: dónde vende y la comisión de cada plataforma.</li>
    <li><b>Espera sugerida</b>: el tiempo que propone la cocina al confirmar un pedido de esa marca.</li>
    <li><b>Adicionales</b>: la caja, la bolsa, los cubiertos y lo demás que llevan sus ventas.</li>
    <li>Sus tiendas en las plataformas y el botón para publicarles la carta.</li>
  </ol>
  <figcaption>Las cuatro marcas de la demo. Las tiendas aparecen con el módulo Delivery por plataformas.</figcaption>
</figure>

### Crear o cambiar una unidad

1. Tocá **Unidad de negocio**, o la fila de una que ya existe.
2. Escribí el **Nombre** y elegí el **Color**: la distingue en las pantallas de la cocina y en las etiquetas.
3. Poné la **Espera sugerida (min)**. Se propone al confirmar un pedido y se puede cambiar en cada uno.
4. En **Canales de venta**, prendé **Vende** en cada canal donde vende y completá lo que se queda ese canal.
5. Tocá **Guardar**. Aparece «Guardado: Doble Smash».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-unidad.jpg' | relative_url }}" alt="El formulario de una unidad de negocio nueva: nombre, color, espera sugerida, orden y la tabla de canales con comisión, costo fijo y productos por pedido" loading="lazy" width="880" height="900">
  <ol class="marks">
    <li><b>Color</b>: el de la marca en la cocina y en las etiquetas.</li>
    <li><b>Espera sugerida (min)</b>: el tiempo que se propone al confirmar.</li>
    <li><b>Vende</b>: prendé cada canal donde vende la marca.</li>
    <li><b>Comisión (%)</b>: al prender Rappi propone 23 %, y se cambia si la marca tiene otra.</li>
    <li><b>Costo fijo por unidad</b> y <b>Productos por pedido</b>: para que los márgenes cuenten bien lo que cobra cada canal.</li>
  </ol>
  <figcaption>Una unidad nueva. El canal Salón aparece con el módulo Salón.</figcaption>
</figure>

Lo que significa cada columna de **Canales de venta**:

| Columna | Qué es |
|---|---|
| **Canal** | **Pedidos propios** siempre. **Rappi** y **PedidosYa** con el módulo Delivery por plataformas. **Salón** con el módulo Salón. |
| **Vende** | Si la marca vende por ese canal. |
| **Comisión (%)** | Lo que se queda el canal sobre lo que paga el cliente. |
| **Costo fijo por unidad** | Lo que cobra el canal por cada producto vendido, en los que cobran así. |
| **Productos por pedido** | Cuántos productos tiene un pedido promedio. Lo que lleva cada pedido se reparte entre ellos en los márgenes. |

**Orden** dice en qué lugar aparece la marca en las listas. Las unidades no se borran: para dejar de usar una, apagá **Activa**.

### Cargar los adicionales

Los adicionales son lo que llevan las ventas además de la receta, y se descuentan del stock con cada pedido: la caja de cada producto, la bolsa, los cubiertos, el sticker.

1. En la fila de la unidad, tocá **Adicionales**.
2. Tocá **+ Adicional**.
3. Elegí el **Canal** (**Todos**, **Propios**, **Rappi**, **PedidosYa** o **Salón**) y dónde **Va en**: **Cada pedido**, **Cada producto** o solo cada producto de una categoría.
4. Elegí el **Insumo** y la **Cantidad**. Al lado se ve el **Costo**.
5. Tocá **Guardar**. Aparece «Adicionales guardados».
{: .steps}

En los márgenes, lo que va en cada pedido se reparte entre los productos de un pedido promedio del canal. Se ve en [Costos y reportes]({{ '/es/projects/fornu/manual/costos-y-reportes/' | relative_url }}).

### Las tiendas de Rappi y PedidosYa {#tiendas}

Con el módulo Delivery por plataformas, cada unidad de negocio es una tienda en cada plataforma, con el número que le da la plataforma. La fila de la unidad dice cómo está cada una:

| Dice | Significa |
|---|---|
| «Rappi: sin tienda vinculada (la vincula Fornu)» | Esa marca vende en Rappi pero su tienda todavía no está vinculada. |
| «Rappi: tienda 900100001 · carta al día» | La tienda muestra la carta como está hoy. |
| «· cambios sin publicar» | La carta cambió después de la última publicación. |
| «· carta sin publicar» | La carta nunca se publicó desde Fornu en esa tienda. |

El estado de la carta lo ve quien tiene el permiso Carta.

**Cómo se vincula una tienda:** pasale a Fornu el número de tienda de cada unidad de negocio en cada plataforma, y Fornu la vincula. Hasta entonces, los pedidos de esa tienda se cargan a mano en el tablero, con el número que muestra la tablet de la plataforma. Se explica en [Pedidos y delivery]({{ '/es/projects/fornu/manual/pedidos/' | relative_url }}).

### Publicar la carta en Rappi o PedidosYa

1. En la fila de la unidad, tocá **Publicar en Rappi** o **Publicar en PedidosYa**. Hay un botón por cada tienda vinculada.
2. Fornu publica la carta de esa marca en su tienda, con los precios de esa plataforma. Aparece «Carta publicada en Rappi», con la cantidad de productos y el número de tienda.
{: .steps}

<div class="callout tip"><p class="callout-title">Consejo</p><p>Después de cambiar precios o productos, Carta › Productos avisa «La carta de Rappi no está al día.» con un botón para publicarla. Hasta que se publique otra vez, la plataforma muestra los precios y productos de antes.</p></div>

## Dispositivos {#dispositivos}

Son los celulares, tablets y PC donde el personal entra con su PIN, y la PC que imprime las comandas. Cada uno se vincula una sola vez, con un código. Después el equipo entra con su PIN, sin tu contraseña.

<p class="perm"><span>Quién puede:</span> <span class="tag">Dispositivos</span></p>

La lista muestra cada **Dispositivo** con el nombre que le pusiste, cuándo se **Vinculó** y su **Último ingreso** con PIN. Los dados de baja dicen «dado de baja».

### Vincular un celular, una tablet o una PC

1. Tocá **Vincular dispositivo**.
2. Poné un **Nombre para reconocerlo**: «Celular de Martín», «PC del mostrador», «Impresora de comandas».
3. Tocá **Generar código**. Aparece un código como ABCD-1234. Vale hasta la hora que dice el diálogo y sirve una sola vez.
4. En el dispositivo, abrí Fornu y tocá **Usar este celular o PC en una cocina, con PIN**.
5. Escribí el código y tocá **Vincular**. Aparece «Dispositivo vinculado».
{: .steps}

Lo que se ve después en el dispositivo, la lista de nombres y el PIN, está en [En la cocina y en la calle]({{ '/es/projects/fornu/manual/cocina-y-reparto/' | relative_url }}#vincular). Si el código no anda, dice «El código no es válido. Revisalo o generá otro.»

### La PC que imprime las comandas

Las comandas salen por una PC del local que está junto a la impresora, con el agente de impresión de Fornu. Al generar el código, el mismo diálogo muestra lo que hay que escribir en esa PC para vincularla. Si el agente no está conectado, las pruebas de impresión lo avisan.

### Dar de baja un dispositivo

1. En su fila, tocá **Dar de baja**.
2. Confirmá. Quien lo esté usando queda afuera, y para volver a usarlo hace falta un código nuevo.
{: .steps}

En el mismo dispositivo, **Desvincular este dispositivo** hace que ese navegador olvide la vinculación. La lista de Ajustes lo sigue mostrando hasta que alguien toque **Dar de baja**.

## Estaciones de cocina {#estaciones}

Cada estación imprime su comanda: la parrilla lo de la parrilla, la barra las bebidas. Sin estaciones, todo sale por la impresora de la cocina. La pestaña dice **Estaciones**.

<p class="perm"><span>Quién puede:</span> <span class="tag">Ajustes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-estaciones.jpg' | relative_url }}" alt="La lista de estaciones con la cocina sin impresora y una barra con su impresora, y debajo qué prepara cada estación para cada categoría de Doble Smash" loading="lazy" width="1440" height="600">
  <ol class="marks">
    <li><b>Nueva estación</b>: suma una.</li>
    <li><b>Cocina (la de Configuración)</b>: prepara todo lo que no va a otra estación. Su impresora se elige en <a href="#impresion">Configuración</a>.</li>
    <li>La impresora de la estación. Sin una, su comanda sale por la de la cocina con el nombre de la estación arriba.</li>
    <li><b>Prueba</b>: imprime una comanda de prueba en esa estación.</li>
    <li>Qué prepara cada estación: una lista por categoría, en cada unidad de negocio.</li>
  </ol>
  <figcaption>Una cocina con una estación de barra, todavía sin categorías asignadas.</figcaption>
</figure>

### Crear una estación

1. Tocá **Nueva estación**.
2. Poné el **Nombre**: Parrilla, Barra, Cocina fría.
3. Si la estación tiene su impresora, escribí su dirección en **Impresora (opcional)**, como 192.168.0.51.
4. Tocá **Guardar**. Aparece «Estación guardada.»
{: .steps}

Al editarla aparece **Activa: si no, sus categorías salen por la cocina**.

### Elegir qué prepara cada estación

Debajo de la lista hay una tarjeta por unidad de negocio, como «Doble Smash: qué prepara cada estación». Cada categoría de la carta tiene su lista: elegí **Cocina** o una estación. Se guarda al elegir y aparece, por ejemplo, «Burgers: guardado.». Estas tarjetas aparecen cuando hay al menos una estación activa.

### Imprimir una prueba

Tocá **Prueba** en la fila de la estación. Este botón aparece cuando la estación tiene impresora propia. La prueba de la impresora de la cocina está en [Configuración](#impresion). Las dos contestan lo mismo:

- «Prueba en cola: sale en unos segundos.»
- «Prueba en cola, pero el agente de impresión todavía no se conectó: instalalo en una PC del local y vinculalo en Dispositivos.»

## Medios de pago {#medios-de-pago}

Es lo que la caja ofrece al cobrar una mesa, con el nombre que usa el local: Cuenta DNI, Modo, Débito Visa. Cada medio es de un tipo. El efectivo entra en la caja, y el resto se cobra por otro lado y se controla en el arqueo.

<p class="perm"><span>Quién puede:</span> <span class="tag">Ajustes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-medios-de-pago.jpg' | relative_url }}" alt="La lista de medios de pago con los seis de entrada, y al costado el formulario para agregar uno con su nombre y su tipo" loading="lazy" width="1440" height="600">
  <ol class="marks">
    <li>Los medios de pago de la cuenta, cada uno con su tipo.</li>
    <li><b>Nombre</b>: como lo llama el local.</li>
    <li><b>Tipo</b>: decide en qué línea del arqueo cuenta lo cobrado.</li>
  </ol>
  <figcaption>Una cuenta nueva arranca con Efectivo, Débito, Crédito, QR, Transferencia y Mercado Pago.</figcaption>
</figure>

1. Tocá **Agregar**.
2. Poné el **Nombre**, hasta 40 letras.
3. Elegí el **Tipo**: **Efectivo**, **Débito**, **Crédito**, **QR**, **Transferencia** o **Mercado Pago**.
4. Tocá **Guardar**.
{: .steps}

Los medios no se borran: para dejar de ofrecer uno, tocalo y apagá **Activo**. Los usa el cobro del [Salón]({{ '/es/projects/fornu/manual/salon/' | relative_url }}#cobrar), y el arqueo los cuenta según su tipo, como se ve en [Caja y ventas]({{ '/es/projects/fornu/manual/caja/' | relative_url }}#arqueo).

## Motivos de descuento {#descuentos}

Dicen por qué se descuenta. La caja elige uno al hacer un descuento, a toda la cuenta o a una línea, y así después se sabe qué se descontó y por qué. Cada motivo sugiere un porcentaje que se puede cambiar en el momento. La pestaña dice **Descuentos**.

<p class="perm"><span>Quién puede:</span> <span class="tag">Ajustes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-descuentos.jpg' | relative_url }}" alt="Los cuatro motivos de descuento de entrada: Invita la casa y Consumo del personal al 100 %, Cliente habitual y Demora al 10 %" loading="lazy" width="1440" height="390">
  <ol class="marks">
    <li><b>Agregar</b>: suma un motivo.</li>
    <li><b>Sugiere</b>: el porcentaje que propone. Un regalo es 100 %.</li>
  </ol>
  <figcaption>Los motivos con los que arranca una cuenta.</figcaption>
</figure>

1. Tocá **Agregar**.
2. Escribí el **Motivo** como lo dice el local: Invita la casa, Dueños, Cliente habitual.
3. Poné el **Porcentaje sugerido**, de 0 a 100.
4. Tocá **Guardar**.
{: .steps}

Los usan los descuentos del Salón (permiso **Descontar e invitar**) y los clientes de Pedidos que traen un descuento propio. Una línea descontada sigue contando como vendida: las facturas y los reportes toman lo que se cobró de verdad, y una línea regalada al 100 % no va en la factura. Los motivos no se borran: se apagan con **Activo**.

## Integraciones {#integraciones}

Hay una tarjeta por cada servicio de afuera con el que Fornu se puede conectar. Cada una dice cómo está y lleva a donde se configura. Fornu funciona sin ninguna.

<p class="perm"><span>Quién puede:</span> <span class="tag">Ajustes</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-integraciones.jpg' | relative_url }}" alt="Las tarjetas de Rappi, PedidosYa y ARCA, cada una con su estado, una línea que explica qué falta y su botón" loading="lazy" width="1440" height="400">
  <ol class="marks">
    <li>El estado de la integración.</li>
    <li>Qué le falta o cómo está, y <b>Configurar</b> para ir a donde se arma.</li>
    <li><b>Conectar</b>: lleva a donde se empieza a conectar.</li>
    <li><b>Próximamente</b>: todavía no se puede conectar, y no tiene botón.</li>
  </ol>
  <figcaption>Las tarjetas de la demo.</figcaption>
</figure>

| Estado | Significa |
|---|---|
| **Conectada** | Tiene todo lo que pide. En Rappi y PedidosYa, cada unidad que vende ahí tiene su tienda vinculada. En ARCA, la facturación está activa con el CUIT y el punto de venta. |
| **A medias** | Falta un paso: algunas unidades tienen su tienda y otras no, o el CUIT está cargado pero falta activar la facturación. |
| **Sin conectar** | Todavía no se configuró. |
| **Próximamente** | Todavía no se puede conectar desde Fornu. |
| **No está en tu plan** | El módulo no está prendido en la cuenta. La tarjeta dice «Pedile a Fornu que la sume a tu plan.» |

- **Rappi** y **PedidosYa**: sus pedidos entran solos al tablero, y la carta y lo agotado se publican desde Fornu. El botón lleva a [Unidades de negocio](#tiendas), donde se ve cada tienda. Si ninguna marca vende en esa plataforma, la tarjeta dice que se activa en la fila de la unidad.
- **ARCA · Factura electrónica**: factura las ventas con CAE, sola o con un toque, y las notas de crédito. El botón lleva a Ajustes › Facturación, que pide el permiso **Configurar la facturación**.

Quien no puede configurar una integración ve «La conecta quien administra la cuenta.»

## Usuarios {#usuarios}

Son quienes entran a Fornu con email y contraseña, desde cualquier navegador. La Administración puede todo, y los demás pueden lo que permiten sus roles. Los roles son los mismos del personal con PIN y se arman en [Personal › Configuración]({{ '/es/projects/fornu/manual/personal/' | relative_url }}#roles).

<p class="perm"><span>Quién puede:</span> <span class="tag">Administración</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-usuarios.jpg' | relative_url }}" alt="La pantalla Usuarios con el usuario de Administración, un usuario de API llamado Tablero 1 y la sección Visitas de soporte" loading="lazy" width="1440" height="690">
  <ol class="marks">
    <li><b>Agregar</b>: suma un usuario con email y contraseña.</li>
    <li><b>Contraseña</b>: le pone una contraseña nueva a ese usuario.</li>
    <li><b>Nuevo usuario de API</b>: para que otro sistema lea la cuenta.</li>
    <li><b>Secreto nuevo</b>: cambia el secreto de ese usuario de API en el acto.</li>
    <li><b>Visitas de soporte</b>: cuándo entró alguien de Fornu a ayudarte.</li>
  </ol>
  <figcaption>La columna <b>Puede</b> dice «Todo», los roles del usuario o «Sin roles: no entra».</figcaption>
</figure>

### Sumar un usuario

1. Tocá **Agregar**.
2. Escribí el **Nombre** y el **Email** con el que va a entrar.
3. Elegí el **Tipo**: **Administración** puede todo y **Con roles** puede lo que permiten sus roles.
4. Si es **Con roles**, elegí sus **Roles**. Sin ninguno no puede entrar.
5. Poné la **Contraseña inicial**: al menos 10 caracteres.
6. Tocá **Guardar**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-usuario.jpg' | relative_url }}" alt="El formulario para agregar un usuario: nombre, email, tipo Con roles, los roles para elegir y la contraseña inicial" loading="lazy" width="620" height="540">
  <ol class="marks">
    <li><b>Tipo</b>: <b>Administración</b> o <b>Con roles</b>.</li>
    <li><b>Roles</b>: los mismos del equipo.</li>
    <li><b>Contraseña inicial</b>: dásela en persona, y que la cambie desde Mi cuenta.</li>
  </ol>
  <figcaption>Un usuario nuevo con roles.</figcaption>
</figure>

Si alguien con roles no tiene ninguno, al entrar ve «Lucía todavía no tiene permisos: pedile a la administración que le dé un rol.»

### Cambiar una contraseña o desactivar a alguien

- **Contraseña**: tocá **Contraseña** en su fila, escribí la **Nueva contraseña** y tocá **Cambiar**. Aparece «Contraseña cambiada».
- **Desactivar**: tocá su fila, apagá **Activo** y tocá **Guardar**. Siempre tiene que quedar un administrador activo: «Tiene que quedar al menos un administrador activo.»

Cada uno cambia su propio email y contraseña desde su nombre, arriba a la derecha, en **Mi cuenta: email y contraseña**. Se explica en [Entrar y moverse]({{ '/es/projects/fornu/manual/empezar/' | relative_url }}#mi-cuenta).

### Usuarios de API {#usuarios-de-api}

Sirven para que otro sistema lea esta cuenta: un tablero del dueño, la herramienta del contador, una integración. Un usuario de API ve lo que permiten sus roles y solo consulta, no cambia nada. La única excepción es **Carga pedidos**.

1. Tocá **Nuevo usuario de API**.
2. Poné un **Nombre** que diga para qué es o de quién: «Tablero del dueño», «Estudio contable».
3. Elegí sus **Roles**: lee las ventas con Caja, la carta con Carta, y así.
4. Si el otro sistema tiene que cargar pedidos, prendé **Carga pedidos** y escribí en **Avisos a** la dirección donde Fornu le avisa cada paso de esos pedidos: confirmado, listo, en camino, entregado o rechazado.
5. Tocá **Guardar**. Se abre la ventana con la **Clave** y el **Secreto**, cada uno con **Copiar**.
6. Copiá los dos, pasáselos a quien arma el otro sistema y tocá **Ya los guardé**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-usuario-api.jpg' | relative_url }}" alt="El formulario de un usuario de API nuevo llamado Tablero 1, con el rol Encargado/a elegido y la opción Carga pedidos apagada" loading="lazy" width="620" height="340">
  <ol class="marks">
    <li><b>Roles</b>: lo que puede leer.</li>
    <li><b>Carga pedidos</b>: deja que ese sistema cargue pedidos.</li>
  </ol>
  <figcaption>Un tablero que lee lo que ve el encargado.</figcaption>
</figure>

<div class="callout"><p class="callout-title">Importante</p><p>El secreto se muestra una sola vez: copialo antes de cerrar la ventana. Si se pierde, <b>Secreto nuevo</b> da otro en el acto, sin preguntar, y lo que usaba el anterior deja de andar: «Secreto nuevo: el anterior ya no sirve.»</p></div>

La lista muestra la **Clave** de cada uno, lo que **Puede leer**, su **Último uso** (o «Nunca») y si está apagado o carga pedidos. **Editar** cambia el nombre, los roles o lo apaga.

### Visitas de soporte

Dice cuándo entró alguien de Fornu a esta cuenta para ayudarte, y qué miró o cambió mientras estaba, de los últimos 90 días. Muestra 15 y un botón para ver todas. Si no hubo ninguna: «Nadie de Fornu entró a esta cuenta en los últimos 90 días.»

<div class="callout tip"><p class="callout-title">Consejo</p><p>En la demo, los usuarios y las contraseñas no se cambian: «En la demo esto no se cambia: la usa todo el que la prueba. En tu cuenta, sí.»</p></div>

## Configuración {#configuracion}

Son los datos de la cuenta y su cocina, que son una sola cosa: un solo stock, del que salen todas sus unidades de negocio. Arriba hay tres atajos que bajan a cada parte: **La cocina y la caja**, **Impresión** y **Costos y precios**. Personal tiene otra pestaña que también se llama Configuración: es la [del equipo]({{ '/es/projects/fornu/manual/personal/' | relative_url }}#roles).

<p class="perm"><span>Quién puede:</span> <span class="tag">Ajustes</span></p>

### La cocina y la caja

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-configuracion.jpg' | relative_url }}" alt="Los campos de la cocina y la caja: nombre, dirección, zona horaria, hora en que empieza el día, horas para dar por olvidado un fichaje, tolerancia del arqueo, tolerancia para llegar y la opción de pausar lo que no alcanza con el stock" loading="lazy" width="1440" height="470">
  <ol class="marks">
    <li><b>El día empieza a las</b>: un pedido de las 2 de la mañana es del día anterior si el día empieza a las 6.</li>
    <li><b>Un fichaje sin salida se da por olvidado a las (horas)</b>: pasadas esas horas, el próximo PIN empieza un turno nuevo.</li>
    <li><b>Tolerancia del arqueo</b>: cuánto puede no coincidir un medio de pago al cerrar la caja sin decir por qué.</li>
    <li><b>Tolerancia para llegar (minutos)</b>: hasta cuántos minutos después de su horario no es llegada tarde.</li>
    <li><b>Pausar lo que no alcanza con el stock</b>: deja de ofrecer lo que no se puede hacer.</li>
  </ol>
  <figcaption>Los valores con los que arranca una cuenta.</figcaption>
</figure>

| Campo | De entrada | Qué es |
|---|---|---|
| **Nombre de la cocina** | | Es también el nombre de la cuenta. |
| **Dirección** | | La del local. |
| **Zona horaria** | Argentina | Dónde empieza y termina cada día de trabajo. También Uruguay, Chile, Paraguay, Brasil (São Paulo), Perú, Colombia y México. |
| **El día empieza a las** | 6 | Hora local, de 0 a 23. Con 6, un pedido de las 2 de la mañana cuenta en el día anterior. |
| **Un fichaje sin salida se da por olvidado a las (horas)** | 16 | De 6 a 24. Pasadas esas horas desde la entrada, el próximo toque del PIN empieza un turno nuevo y el anterior queda para corregir en [Asistencia]({{ '/es/projects/fornu/manual/personal/' | relative_url }}#asistencia). |
| **Tolerancia del arqueo** | $ 0 | Cuánto puede no coincidir un medio de pago al cerrar la caja sin elegir por qué. En $ 0, toda diferencia dice por qué. Ver [Caja y ventas]({{ '/es/projects/fornu/manual/caja/' | relative_url }}#arqueo). |
| **Tolerancia para llegar (minutos)** | 10 | Con el módulo Personal. Quien ficha hasta estos minutos después de su horario no cuenta como llegada tarde. |

### Pausar lo que no alcanza con el stock {#pausar}

Con esta opción, si el stock no alcanza para hacer un producto, ni preparando lo que falta, el producto deja de ofrecerse en los pedidos propios y se apaga en las tiendas de las plataformas, si las hay. Vuelve solo cuando entra el stock, y desde **Agotados** se puede ofrecer igual por el día (ver [Pedidos y delivery]({{ '/es/projects/fornu/manual/pedidos/' | relative_url }})).

Al tildarla, antes de guardar, Fornu muestra qué pausaría con el stock de ahora: «Con el stock de ahora no se pausaría nada.», o «Con el stock de ahora se pausarían 3 productos:» con cada producto, su marca y lo que le falta.

<div class="callout tip"><p class="callout-title">Consejo</p><p>Prendela solo si las compras y los conteos están al día. Con un stock desactualizado, la lista de lo que se pausaría es casi toda la carta: mirala antes de guardar.</p></div>

### Impresión {#impresion}

Dice dónde salen las comandas y cómo se ven en el papel.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-impresion.jpg' | relative_url }}" alt="La parte Impresión: la dirección de la impresora de comandas, el papel de 80 o 58 mm, el botón Imprimir prueba y la vista previa de una comanda en papel de 58 mm" loading="lazy" width="900" height="522">
  <ol class="marks">
    <li><b>Impresora de comandas</b>: su dirección en la red del local, como 192.168.0.50. Vacía si no hay.</li>
    <li><b>Papel</b>: <b>80 mm</b>, el común, o <b>58 mm</b>, el de las impresoras chicas. Vale para todas las impresoras de la cocina.</li>
    <li><b>Imprimir prueba</b> y, al lado, qué falta para poder probar.</li>
    <li>Así sale una comanda con ese papel: 42 letras por línea en 80 mm, 32 en 58 mm.</li>
  </ol>
  <figcaption>Una impresora recién cargada y todavía sin guardar: la prueba espera a que se guarde.</figcaption>
</figure>

1. Escribí la dirección de la impresora en **Impresora de comandas**.
2. Elegí el **Papel**. La vista previa cambia en el momento.
3. Tocá **Guardar**.
4. Tocá **Imprimir prueba**. Sale esa misma comanda, con el papel elegido.
{: .steps}

Al lado del botón, Fornu dice qué pasa: «Cargá la impresora y guardá para probarla.», «Guardá los cambios para probar con ellos.» o «Sale esta misma comanda, con el papel de arriba.». Después de imprimir dice «Prueba en cola: sale en unos segundos.», o avisa que el agente de impresión todavía no se conectó y que hay que vincularlo en [Dispositivos](#dispositivos). Las impresoras de cada estación se cargan en [Estaciones de cocina](#estaciones).

### Costos y precios

Dice cómo se calcula el costo de cada insumo y el margen de cada venta.

| Campo | De entrada | Qué es |
|---|---|---|
| **Condición frente al IVA** | Monotributo | Con **Monotributo**, el IVA de las compras no se recupera y es parte del costo de cada insumo. Con **Responsable inscripto**, los insumos cuestan su precio sin IVA. |
| **IVA de los precios de venta** | 21 % | Solo para Responsable inscripto: 21 %, 10,5 %, 27 %, 5 % o 2,5 %. Los márgenes se calculan sobre el precio sin IVA. |
| **Ganancia sobre el costo (%)** | 35 % | Lo que el precio sugerido le suma al costo de cada producto que no tiene una propia. |
| **Un precio es viejo a los (días)** | 30 | Pasado ese plazo, el insumo avisa que conviene confirmar su precio. |
| **El ritmo de consumo mira los últimos (días)** | 14 | De 3 a 90. Con lo usado en esos días se calcula cuántos días dura lo que queda de cada insumo. |

Lo que hacen estos números se ve en [Costos y reportes]({{ '/es/projects/fornu/manual/costos-y-reportes/' | relative_url }}) y en [Insumos y stock]({{ '/es/projects/fornu/manual/insumos-y-stock/' | relative_url }}).

### Guardar los cambios

**Guardar** está apagado hasta que cambiás algo. Con el primer cambio, la barra de guardar queda fija abajo de la pantalla, siempre a mano, con «Hay cambios sin guardar.», **Deshacer los cambios** y **Guardar**. En el teléfono queda arriba de la barra de abajo. Al guardar aparece «Configuración guardada».

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-costos-guardar.jpg' | relative_url }}" alt="La parte Costos y precios con la condición frente al IVA y la ganancia sobre el costo, y abajo la barra fija con Hay cambios sin guardar, Deshacer los cambios y Guardar" loading="lazy" width="1440" height="260">
  <ol class="marks">
    <li><b>Condición frente al IVA</b>: decide si el IVA de las compras es costo.</li>
    <li><b>Ganancia sobre el costo (%)</b>: la que usa el precio sugerido.</li>
    <li>La barra fija: <b>Deshacer los cambios</b> vuelve todo como estaba y <b>Guardar</b> los guarda.</li>
  </ol>
  <figcaption>Con un cambio sin guardar, la barra queda a la vista.</figcaption>
</figure>

## Tus datos {#tus-datos}

Todo lo que la cuenta cargó y operó en Fornu es de la cuenta. Acá se descarga entero, cuando quieras, y se explica cómo dar de baja la cuenta.

<p class="perm"><span>Quién puede:</span> <span class="tag">Administración</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/ajustes-tus-datos.jpg' | relative_url }}" alt="La pantalla Tus datos con el botón Descargar todos los datos y la explicación de cómo dar de baja la cuenta" loading="lazy" width="1440" height="480">
  <ol class="marks">
    <li><b>Descargar todos los datos</b>: baja un ZIP con una planilla por tabla.</li>
    <li><b>Dar de baja la cuenta</b>: se pide a Fornu.</li>
  </ol>
  <figcaption>La descarga incluye la carta, los insumos, las recetas, los pedidos, las compras, los gastos, la caja, el personal y los clientes.</figcaption>
</figure>

1. Tocá **Descargar todos los datos**.
2. Se baja el archivo fornu-datos.zip y aparece «Descargado: todos los datos de la cuenta».
3. Abrí cada planilla con Excel o Google Sheets.
{: .steps}

No van las contraseñas, los PIN ni las claves: se guardan cifrados y no se entregan. En la demo el botón está apagado: «En la demo no se descargan: la usa todo el que la prueba.»

Para dar de baja la cuenta, pedíselo a Fornu. Con la baja se borran todos los datos de la cuenta, así que conviene descargarlos antes. Los detalles están en los términos y la política de privacidad, con links en la misma pantalla.

## Facturación {#facturacion}

Con el módulo Facturación electrónica, Ajustes tiene una pestaña más, **Facturación**, donde se cargan los datos fiscales y el punto de venta, y se prende la facturación con ARCA. Pide el permiso **Configurar la facturación** y se explica en [Facturación electrónica]({{ '/es/projects/fornu/manual/facturacion/' | relative_url }}#configurar).

## Los módulos de tu cuenta {#modulos}

Los módulos de cada cuenta los prende Fornu. Desde la cuenta se nota en las pantallas:

- Un módulo prendido suma sus pestañas, y también campos, columnas, botones y avisos en otras pantallas. Por ejemplo, Personal suma **Estado** y **Cobra** al equipo y **Tolerancia para llegar** a esta configuración.
- Un módulo apagado no aparece en ningún lado, ni como botón gris. Sus permisos desaparecen del editor de roles pero quedan guardados, y su tarjeta de [Integraciones](#integraciones) dice «No está en tu plan».
- Nada de lo que guardó un módulo se borra al apagarlo: vuelve todo cuando se prende de nuevo.

Los módulos también vienen en grupos pensados para cada tipo de local: **Dark kitchen**, **Restaurante**, **Cafetería** y **Salón Pro**. Qué trae cada módulo y cada grupo está en el [índice del manual]({{ '/es/projects/fornu/manual/' | relative_url }}#modulos).

<div class="callout tip"><p class="callout-title">Consejo</p><p>En el teléfono, Ajustes está dentro de <b>Más</b>, en la barra de abajo, con cada pestaña por su nombre completo.</p></div>
