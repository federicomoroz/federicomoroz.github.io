---
layout: manual
manual: cocina-y-reparto
title: "En la cocina y en la calle · Manual de Fornu"
description: "Cómo se vincula la tablet o el celular, cómo entra cada persona con su PIN, cómo se ficha, qué muestra la app del personal, cómo se cargan mermas y producción y cómo reparte el mensajero."
permalink: /es/projects/fornu/manual/cocina-y-reparto/
---

## Vincular el dispositivo {#vincular}

La tablet de la cocina, el celular de cada mensajero o la PC del mostrador se vinculan una sola vez a la cocina, con un código. Desde ahí nadie necesita la contraseña del dueño: cada persona toca su nombre y pone su PIN.

<p class="perm"><span>Quién puede:</span> <span class="tag">Dispositivos</span> para generar el código. En el equipo, cualquiera que lo escriba.</p>

### Generar el código

1. En la oficina, entrá a Ajustes › Dispositivos y tocá **Vincular dispositivo**.
2. Poné un **Nombre para reconocerlo**, como «Tablet de la parrilla» o «Celular de Martín».
3. Tocá **Generar código**. Aparece un código como XXXX-XXXX, que dice hasta qué hora vale y sirve una sola vez.
{: .steps}

La pantalla de Dispositivos se explica en [Ajustes]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#dispositivos).

### Vincular el equipo

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-vincular.jpg' | relative_url }}" alt="La pantalla Vincular este dispositivo en un celular, con el campo Código, el botón Vincular y el enlace Volver a ingresar con email" loading="lazy" width="390" height="600">
  <ol class="marks">
    <li><b>Código</b>: el que generaste en Dispositivos.</li>
    <li><b>Vincular</b>: se prende cuando están las ocho letras y números.</li>
    <li><b>Volver a ingresar con email</b>: para volver atrás.</li>
  </ol>
  <figcaption>Vincular este dispositivo, en el celular.</figcaption>
</figure>

1. En la tablet o el celular, abrí Fornu. En la pantalla para entrar, tocá **Usar este celular o PC en una cocina, con PIN**.
2. Se abre **Vincular este dispositivo**. Escribí el código en **Código**. No importa si va en mayúsculas o minúsculas.
3. Tocá **Vincular**. Aparece «Dispositivo vinculado» y, enseguida, la [pantalla de PIN](#pin).
{: .steps}

Si el código está mal o ya venció, aparece «El código no es válido. Revisalo o generá otro.» Generá uno nuevo en Dispositivos.

<div class="callout tip"><p class="callout-title">Consejo</p><p>Poné nombres que se entiendan de un vistazo. El nombre aparece en la pantalla de PIN y en la lista de Dispositivos, y es lo que te va a decir cuál dar de baja si un celular se pierde.</p></div>

### Desvincular

- **Desde el mismo equipo**: en la pantalla de PIN, tocá **Desvincular este dispositivo**. Fornu pregunta «¿Desvincular este dispositivo?» y avisa que para volver a usarlo con PIN hará falta un código nuevo. Tocá **Desvincular**. Esto solo hace que ese navegador se olvide de la cocina: el equipo sigue en la lista de Dispositivos.
- **Desde la oficina**: en Ajustes › Dispositivos, **Dar de baja**. Quien lo esté usando queda afuera en ese momento. Es lo que conviene si un celular se pierde o un mensajero deja de usar el suyo.

## La pantalla de PIN {#pin}

Es lo primero que muestra un equipo vinculado: la lista de las personas de la cocina. Cada una toca su nombre y pone su PIN para entrar o para fichar.

<p class="perm"><span>Quién puede:</span> todo el que tiene PIN. El PIN se carga en <a href="{{ '/es/projects/fornu/manual/personal/' | relative_url }}">Personal</a>.</p>

<div class="shot-pair">
<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-pin.jpg' | relative_url }}" alt="El teclado del PIN de Martín en su celular, en turno desde las 18:25, con los botones Fichar salida y Entrar" loading="lazy" width="390" height="844">
  <ol class="marks">
    <li>Quién está entrando y, si está en turno, desde qué hora.</li>
    <li>Los puntos y el teclado. <b>Volver</b> regresa a los nombres y ⌫ borra.</li>
    <li><b>Fichar salida</b>: cierra el turno, sin entrar.</li>
    <li><b>Entrar</b>: abre la app.</li>
  </ol>
  <figcaption>El teclado del PIN para alguien que ya está en turno.</figcaption>
</figure>
<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-nombres.jpg' | relative_url }}" alt="La pantalla de PIN de la Cocina de prueba en la tablet Cocina, con siete nombres y sus roles, tres de ellos en turno, los enlaces Ingresar con email y Desvincular este dispositivo, y el selector de tema arriba" loading="lazy" width="900" height="700">
  <ol class="marks">
    <li>El nombre de la cocina y, debajo, el del dispositivo.</li>
    <li>Una tarjeta por persona, con sus roles y, si está en turno, desde qué hora.</li>
    <li><b>Ingresar con email</b>: para el dueño o el encargado, en el mismo equipo.</li>
    <li><b>Desvincular este dispositivo</b>.</li>
    <li>El tema de este equipo.</li>
  </ol>
  <figcaption>La lista de nombres en una tablet.</figcaption>
</figure>
</div>

### Los nombres

Debajo de cada nombre van sus roles, separados por « · », o **Solo ficha** si sus roles no le dan ningún permiso. Quien ya fichó la entrada muestra «En turno desde las 13:05». Aparecen las personas activas que tienen PIN. Si todavía no hay ninguna, la pantalla dice «Nadie de esta cocina tiene PIN todavía. Se carga en Personal.»

### Entrar con el PIN

1. Tocá tu nombre.
2. Escribí tu PIN, de 4 a 6 números, con el teclado de la pantalla o con el del equipo.
3. Tocá el botón que corresponda. Los botones se prenden desde el cuarto número, y <kbd>Enter</kbd> aprieta el principal.
{: .steps}

Los botones cambian según quién sos y si ya fichaste:

| Quién | Botones | Qué hace el principal |
|---|---|---|
| Usa la app y no está en turno | **Entrar sin fichar** y **Fichar y entrar** | Ficha la entrada y abre la app, en un toque. |
| Usa la app y ya está en turno | **Fichar salida** y **Entrar** | Abre la app. |
| Solo ficha | **Fichar entrada** o **Fichar salida** | Ficha, y nada más. |

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-pin-sin-turno.jpg' | relative_url }}" alt="El teclado del PIN de Lucía, que todavía no fichó, con los botones Entrar sin fichar y Fichar y entrar" loading="lazy" width="412" height="915">
  <ol class="marks">
    <li>Quién entra. No dice «En turno desde las…»: todavía no fichó.</li>
    <li><b>Entrar sin fichar</b>: abre la app y no anota la entrada.</li>
    <li><b>Fichar y entrar</b>: el principal, ficha la entrada y abre la app.</li>
  </ol>
  <figcaption>El teclado para alguien que todavía no fichó.</figcaption>
</figure>

Si el PIN está mal, dice «PIN incorrecto · quedan 3 intentos.» Después de cinco intentos fallidos seguidos, la persona queda bloqueada 15 minutos: «PIN incorrecto: Martín queda bloqueado 15 min.» Si te olvidaste el PIN, pedile a quien administra el equipo que te cargue uno nuevo.

<div class="callout tip"><p class="callout-title">Consejo</p><p>El tema se elige con los íconos de arriba de esta pantalla, y vale para este equipo. La tablet de la cocina puede quedar en oscuro aunque la oficina use el claro.</p></div>

## Fichar la entrada y la salida {#fichar}

Fichar deja anotado cuándo entra y cuándo sale cada persona, con su PIN, en cualquier equipo vinculado. Funciona siempre, con o sin el módulo Personal. Con el módulo, esas fichadas alimentan la asistencia y el presentismo de [Personal]({{ '/es/projects/fornu/manual/personal/' | relative_url }}).

<p class="perm"><span>Quién puede:</span> todo el que tiene PIN, aunque su rol no tenga ningún permiso.</p>

### Al llegar

1. Tocá tu nombre y escribí tu PIN.
2. Tocá **Fichar y entrar** (o apretá <kbd>Enter</kbd>). Queda fichada la entrada y se abre tu app.
{: .steps}

Si solo vas a mirar algo y no empezás tu turno, usá **Entrar sin fichar**.

### Durante el turno

Arriba de la app hay un recuadro con tu turno:

- Si no fichaste, dice **Fichar entrada**, resaltado. Tocalo y aparece «Entrada fichada».
- Si estás en turno, dice «En turno desde las 13:05 · Fichar salida». En pantallas angostas, como el celular, se ve solo «En turno desde las 13:05».

### Al irte

1. Tocá el recuadro del turno. Fornu pregunta «¿Fichar la salida?» y te dice cuánto llevás: «Entraste a las 13:05: van 8 h 10 min.»
2. Tocá **Fichar salida**. Aparece «Salida fichada».
{: .steps}

También se puede desde la pantalla de PIN: tu nombre, tu PIN y **Fichar salida**. Ahí aparece una tarjeta que se cierra sola a los 6 segundos, o con **Listo**.

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-fichado.jpg' | relative_url }}" alt="La tarjeta que confirma la salida: Salida de Martín: 18:22, Trabajaste 4 min., con el botón Listo" loading="lazy" width="390" height="570">
  <figcaption>La salida fichada, con las horas trabajadas. Al entrar, la tarjeta dice «¡Buen turno!».</figcaption>
</figure>

Algunas reglas:

- La salida no se puede fichar en el primer minuto después de la entrada: «Fichaste la entrada recién: la salida se ficha al terminar el turno.»
- Un turno que queda abierto más horas de las que dice Ajustes › Configuración (16, si nadie lo cambió) se da por olvidado. El siguiente toque empieza un turno nuevo, y el olvidado queda para que el encargado lo corrija en Personal › Asistencia.
- Quien entra con email en la oficina no ficha: los botones de fichar están solo en la app del personal. Si el dueño también quiere fichar, necesita su nombre y su PIN en Personal.

### Fichar a alguien

En la tablet de la cocina, la app queda abierta en el tablero todo el turno. Para que otra persona fiche sin cerrar nada, está **Fichar a alguien**.

1. Tocá **Fichar a alguien**, arriba de la app.
2. Se abre **Fichar entrada o salida**, con cada nombre y su estado: «En turno desde las…» o «Sin fichar».
3. Tocá el nombre y que esa persona escriba su PIN.
4. Tocá **Fichar entrada** o **Fichar salida**. La tarjeta dice «Entrada de Lucía: 13:05» y «¡Buen turno!», o la salida con lo trabajado. Tocá **Listo**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-fichar-a-alguien.jpg' | relative_url }}" alt="Fichar entrada o salida abierto sobre el tablero de la tablet, con siete nombres: cuatro en turno, con la hora en que entraron, y tres sin fichar" loading="lazy" width="820" height="300">
  <ol class="marks">
    <li>Alguien que todavía no fichó: «Sin fichar».</li>
    <li>Alguien en turno: «En turno desde las 18:18».</li>
  </ol>
  <figcaption>Fichar entrada o salida, encima del tablero.</figcaption>
</figure>

Nadie entra ni sale de la app, y el tablero de abajo sigue sonando con cada pedido nuevo.

### La gente que solo ficha

Una persona cuyos roles no tienen permisos aparece como **Solo ficha**: su PIN marca la entrada y la salida, y no abre ninguna pantalla. Sirve para el bachero, la limpieza o cualquiera que no use Fornu pero tenga que fichar. Los roles se arman en [Personal]({{ '/es/projects/fornu/manual/personal/' | relative_url }}#roles).

## La app del personal {#app}

Quien entra con su PIN ve solo las pantallas de su trabajo, como pestañas. El cocinero ve el tablero y la merma, el mensajero sus entregas, el mozo las mesas.

<p class="perm"><span>Quién puede:</span> todo el que tiene un rol con permisos. Cada pestaña pide el suyo.</p>

<div class="shot-pair">
<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-app-celular.jpg' | relative_url }}" alt="La app del personal en el celular de una moza: arriba Fichar entrada resaltado, Fichar a alguien y Sofía, y debajo la pantalla Venta con las mesas" loading="lazy" width="390" height="640">
  <ol class="marks">
    <li><b>Fichar entrada</b>: todavía no fichó.</li>
    <li><b>Fichar a alguien</b>.</li>
    <li>Quién está usando la app. Un toque vuelve a los nombres.</li>
  </ol>
  <figcaption>Una moza con una sola pantalla, Venta: no hay pestañas.</figcaption>
</figure>
<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-app-tablet.jpg' | relative_url }}" alt="La app del personal en la tablet Cocina, en la pestaña Pedidos, con el turno de Diego Ruiz abierto, Fichar a alguien, las pestañas Pedidos y Merma y producción, su nombre y el tablero mostrando solo la estación Plancha" loading="lazy" width="820" height="620">
  <ol class="marks">
    <li>El turno: «En turno desde las…».</li>
    <li><b>Fichar a alguien</b>.</li>
    <li>Las pestañas: <b>Pedidos</b> y <b>Merma y producción</b>.</li>
    <li>Quién está usando la app.</li>
    <li><b>Todo</b>, un botón por estación y uno por marca: qué muestra este tablero.</li>
    <li>Lo de otra estación se ve apagado.</li>
  </ol>
  <figcaption>La tablet de la plancha, que muestra solo lo de su estación.</figcaption>
</figure>
</div>

### Lo que hay arriba

- A la izquierda, Fornu con el nombre de la cocina y, como título, la pestaña abierta.
- El recuadro del turno y **Fichar a alguien**, que se explican en [Fichar](#fichar).
- Las pestañas, cuando hay más de una. Se abre la primera.
- El tema, en pantallas anchas.
- Tu nombre con «· Cambiar de persona» (en el celular, solo el nombre). Un toque vuelve a la lista de nombres sin preguntar: en una tablet compartida, el que termina se la pasa al siguiente.

Si se corta la conexión, aparece la franja «Sin conexión en vivo: los pedidos nuevos pueden tardar en aparecer. Reintentando…».

### Las pestañas según el rol

| Pestaña | La ve quien tiene | Qué es |
|---|---|---|
| **Venta** | Atender mesas o Cobrar mesas, con el módulo Salón | Las mesas y el mostrador. Ver [Salón]({{ '/es/projects/fornu/manual/salon/' | relative_url }}). |
| **Pedidos** | Cocina | El [tablero de pedidos](#tablero). |
| **Merma y producción** | Cocina | Lo que se tiró y lo que se hizo. Ver [Merma y producción](#merma). |
| **Mis entregas** | Mensajería | Los pedidos del mensajero. Ver [El celular del mensajero](#mensajero). |
| **Arqueo** y **Movimientos** | Caja | Abrir, contar y cerrar la caja. Ver [Caja y ventas]({{ '/es/projects/fornu/manual/caja/' | relative_url }}). |
| **Stock** | Stock | El stock con sus conteos. Ver [Insumos y stock]({{ '/es/projects/fornu/manual/insumos-y-stock/' | relative_url }}). |
| **Compras** | Gastos, con el módulo Proveedores y compras | Las compras de insumos. Ver [Compras y gastos]({{ '/es/projects/fornu/manual/compras-y-gastos/' | relative_url }}). |
| **Gastos** | Gastos | Los gastos. Ver [Compras y gastos]({{ '/es/projects/fornu/manual/compras-y-gastos/' | relative_url }}). |

Por ejemplo, alguien con el rol **Cocina** ve **Pedidos** y **Merma y producción**. Un mensajero con el rol **Mensajería** ve solo **Mis entregas**, sin pestañas. Un encargado con el rol **Encargado/a** ve **Pedidos**, **Merma y producción**, **Arqueo**, **Movimientos**, **Stock** y **Gastos**, más **Compras** si la cuenta tiene Proveedores y compras.

## La tablet de la cocina {#tablero}

La pestaña **Pedidos** es el mismo tablero de la oficina, pensado para quedar a la vista junto a la plancha: cada pedido entra en **A confirmar** y suena, y pasa por **En preparación** y **Listo para entregar** con un toque. Todo lo que se hace en el tablero se explica en [Pedidos y delivery]({{ '/es/projects/fornu/manual/pedidos/' | relative_url }}#tablero). Acá va lo propio de la tablet.

<p class="perm"><span>Quién puede:</span> <span class="tag">Cocina</span></p>

### Cada tablet, su estación

Arriba del tablero hay una fila de botones que eligen qué muestra: **Todo**, uno por cada estación con pedidos en curso (como **Parrilla**, **Barra** o **Cocina**) y uno por marca cuando hay pedidos de más de una.

1. En la tablet de la parrilla, tocá **Parrilla**.
2. Listo. La tablet se acuerda y queda en la parrilla, aunque alguien cierre y vuelva a entrar.
{: .steps}

Con una estación elegida, aparecen solo los pedidos que tienen algo para ella, y las líneas de las otras estaciones se ven apagadas, como en la imagen de arriba. Las rondas del salón se filtran igual. Con una marca elegida, aparecen solo sus pedidos.

Para saber cuánto sacar de cada cosa, **Ver sumado** (en la columna **En preparación**) o **Sumado** (en el celular) junta todo lo que se está preparando, por ejemplo 4 Papas fritas y 3 Doble cheddar. Con una estación elegida, suma solo lo de esa estación.

### El timbre

Cada pedido nuevo para confirmar suena con un timbre de dos notas, y vuelve a sonar cada 20 segundos mientras haya alguno esperando. Cada ronda nueva del salón también suena.

Algunos navegadores no dejan sonar una página hasta que alguien la toca. Si pasa, el tablero lo dice: «El sonido de los pedidos nuevos está apagado: tocá cualquier parte de la pantalla para prenderlo.», con el botón **Prender el sonido**.

### La pantalla siempre prendida

Mientras el tablero está abierto, la tablet no se apaga sola, en los equipos que lo permiten.

<div class="callout tip"><p class="callout-title">Consejo</p><p>Dejá la tablet enchufada y abierta en <b>Pedidos</b>. Para fichar sin sacarla del tablero, usá <b>Fichar a alguien</b>. Después de cargar una merma, volvé a <b>Pedidos</b>: es la pestaña que mantiene la pantalla prendida y muestra lo que entra.</p></div>

## Merma y producción {#merma}

Para que la cocina anote lo que se tira y lo que produce en el momento, desde la tablet, sin buscar una planilla. Cada registro mueve el stock enseguida.

<p class="perm"><span>Quién puede:</span> <span class="tag">Cocina</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-merma.jpg' | relative_url }}" alt="La pestaña Merma y producción en una tablet: Se tiró un producto con las marcas Doble Smash, Pollo Crocante, Bowl Verde y Pizzería y los productos de Doble Smash, y Se tiró un insumo con el buscador" loading="lazy" width="820" height="770">
  <ol class="marks">
    <li>Las marcas, cuando hay más de una.</li>
    <li>Los productos, sin precio. Un toque abre el descuento.</li>
    <li><b>Buscar insumo…</b>: para lo que se tiró sin ser un plato.</li>
  </ol>
  <figcaption>Merma y producción: lo que se tiró, arriba.</figcaption>
</figure>

### Se tiró un producto

Una hamburguesa que se quemó, un pedido armado por error. Sale del stock todo lo que lleva su receta.

1. Si hay varias marcas, elegí la del producto.
2. Tocá el producto. Se abre **Se tiró: Doble cheddar**.
3. Con **−** y **+**, poné cuántas unidades.
4. Elegí por qué: **Se quemó**, **Se cayó**, **Salió mal**, **Vencido** o **Error de pedido**. Hasta que elijas, el pie dice «Elegí por qué».
5. Tocá **Descontar del stock**. Aparece «Descontado: 2 × Doble cheddar (se quemó)».
{: .steps}

También se puede descontar un producto agotado por hoy: lo que se tiró cuenta igual.

### Se tiró un insumo

Una verdura que se pasó, una bandeja que se cayó, una salsa vencida.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-merma-insumo.jpg' | relative_url }}" alt="El diálogo Se tiró: Arroz, con Cuánto, en kg en 0,5, el motivo Vencido elegido y los botones Volver y Descontar del stock" loading="lazy" width="820" height="283">
  <ol class="marks">
    <li><b>Cuánto</b>, en kilos, litros o unidades según el insumo.</li>
    <li>Por qué se tiró.</li>
    <li><b>Descontar del stock</b>.</li>
  </ol>
  <figcaption>Medio kilo de arroz vencido.</figcaption>
</figure>

1. En **Buscar insumo…**, escribí dos letras o más. Aparecen hasta ocho insumos.
2. Tocá el que se tiró. Se abre **Se tiró: Arroz**.
3. En **Cuánto, en kg** (o en l, o en u), poné la cantidad. Por ejemplo, 0,5 para medio kilo.
4. Elegí por qué.
5. Tocá **Descontar del stock**. Aparece «Descontado: 500 g de Arroz (vencido)».
{: .steps}

Si no aparece nada, dice «No hay ningún insumo que se llame así.» Mientras falte algo, el pie dice «Poné cuánto» o «Elegí por qué».

### Producí

Cuando la cocina hace una tanda de algo que se elabora, como una salsa o los medallones, la anota acá: lo producido entra al stock y salen los insumos que lleva.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-produci.jpg' | relative_url }}" alt="La parte Producí: Bollo de pizza grande en rojo con Faltó registrar lo producido: se usaron 300 u de más, Cebolla caramelizada con Hay 400 g, otras elaboraciones, y el aviso Descontado: 500 g de Arroz (vencido) abajo" loading="lazy" width="820" height="420">
  <ol class="marks">
    <li>En rojo, lo que falta: aparece primero.</li>
    <li>Cuánto hay.</li>
    <li>El aviso de lo último que se cargó.</li>
  </ol>
  <figcaption>Producí, con lo más urgente adelante.</figcaption>
</figure>

Cada elaboración muestra cuánto hay, y las que faltan aparecen primero, en rojo:

| Dice | Qué quiere decir |
|---|---|
| «Hay 400 g» | Lo que hay en stock. |
| «Hay 1 kg · faltan 2 kg para el mínimo» | Está por debajo del mínimo. Conviene hacer una tanda. |
| «Faltó registrar lo producido: se usaron 300 u de más» | Los pedidos usaron más de lo que se anotó. Alguien hizo una tanda y no la cargó. |
| «Sin receta» | No tiene receta cargada, y no se puede producir desde acá. |

1. Tocá lo que hiciste. Se abre, por ejemplo, **Producí: Salsa de la casa**, que dice cuánto hace una tanda y cuánto hay.
2. Con **−** y **+**, poné cuánto hiciste. Cada toque suma o resta una tanda.
3. Tocá **Registrar**. Aparece «Producido: 3 kg de Salsa de la casa».
{: .steps}

Si la cocina no tiene elaboraciones, dice «La cocina todavía no tiene elaboraciones cargadas.» Las elaboraciones y sus recetas se cargan en [Insumos y stock]({{ '/es/projects/fornu/manual/insumos-y-stock/' | relative_url }}). Desde la oficina, quien tiene el permiso Stock también puede cargar mermas y producción.

<div class="callout tip"><p class="callout-title">Consejo</p><p>Una elaboración en rojo con «Faltó registrar lo producido» quiere decir que se hizo una tanda y nadie la anotó. Registrala y el número vuelve a cuadrar.</p></div>

## El celular del mensajero {#mensajero}

Los mensajeros del local reparten los pedidos propios desde su celular: ven qué está listo para salir, se lo llevan, llegan con el mapa y lo marcan entregado. Arriba ven cuánto efectivo llevan encima.

<p class="perm"><span>Quién puede:</span> <span class="tag">Mensajería</span></p>

El celular del mensajero se [vincula](#vincular) una vez, como la tablet. Después el mensajero toca su nombre, pone su PIN y entra directo a **Mis entregas**.

Los pedidos de Rappi y PedidosYa no aparecen acá: los retira el repartidor de cada plataforma.

### Lo que muestra

- **Lo que llevás.** Si tenés efectivo de pedidos entregados, arriba dice «Tenés $ 23.600 en efectivo de 2 pedidos: rendilo al terminar.»
- **Para retirar.** Todos los pedidos propios listos para entregar, de cualquier mensajero. Cada uno muestra «#12 · Doble Smash», a qué hora quedó listo, la dirección, el cliente con el total, qué hay que cobrar y lo que va en la bolsa, para revisarla antes de salir. Abajo, el botón grande **Me lo llevo**. Si no hay nada, dice «No hay pedidos listos.»
- **En camino.** Solo los que llevás vos: a qué hora salió, la dirección en grande, el cliente con su teléfono, lo que va en la bolsa, los botones **Abrir en el mapa**, **Llamar** y **WhatsApp**, la nota del pedido y qué cobrar (o «Total del pedido: $ …» si el pedido no dice cómo paga). Abajo, el botón grande **Entregado**. Si no llevás nada, dice «No estás llevando nada.»
- Al pie, cuántos entregaste: «Entregaste 5 pedidos hoy.»

<div class="shot-phones">
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-entregas.jpg' | relative_url }}" alt="Mis entregas en el celular de Martín: arriba el efectivo que lleva, 13.500 pesos de un pedido, y debajo Para retirar con dos pedidos listos, cada uno con su dirección, el cliente, qué cobrar, lo que va en la bolsa y el botón Me lo llevo" loading="lazy" width="390" height="935">
    <ol class="marks">
      <li>Lo que llevás en efectivo, para rendir al terminar.</li>
      <li>Qué cobrar. En efectivo, con cuánto paga y el vuelto.</li>
      <li>Lo que va en la bolsa.</li>
      <li><b>Me lo llevo</b>.</li>
    </ol>
    <figcaption>Para retirar: dos pedidos listos.</figcaption>
  </figure>
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/cocina-y-reparto-en-camino.jpg' | relative_url }}" alt="En camino: el pedido 2 de Pollo Crocante, con la dirección en grande, el cliente con su teléfono, los botones Abrir en el mapa, Llamar y WhatsApp, qué cobrar y el botón Entregado" loading="lazy" width="390" height="480">
    <ol class="marks">
      <li>La dirección y el cliente, con su teléfono.</li>
      <li><b>Abrir en el mapa</b>, <b>Llamar</b> y <b>WhatsApp</b>.</li>
      <li>Qué cobrar.</li>
      <li><b>Entregado</b>.</li>
    </ol>
    <figcaption>En camino: el que lleva Martín.</figcaption>
  </figure>
</div>

Lo que hay que cobrar se lee igual que en la cocina:

| Dice | Qué hacer |
|---|---|
| «Ya pagó: no hay que cobrar nada» | Entregar y listo. |
| «Cobrar $ 19.600 en efectivo» | Cobrar ese monto en efectivo. |
| «Cobrar $ 19.600 en efectivo · paga con $ 20.000: llevá $ 400 de vuelto» | Salir con el vuelto. |
| «Cobrar $ 19.600 con tarjeta de débito: llevá el posnet» | Llevar el posnet (igual con crédito). |
| «Cobrar $ 19.600 con QR: llevá el código» | Llevar el código QR. |
| «Cobrar $ 19.600 por transferencia» o «por Mercado Pago» | Cobrar al llegar por ese medio. |

### Repartir un pedido

1. Cuando la cocina toca **Listo** en el tablero, el pedido aparece en **Para retirar**.
2. Revisá la bolsa con la lista de lo que lleva.
3. Tocá **Me lo llevo**. El pedido pasa a **En camino** a tu nombre y aparece «#12 en camino». Si otro mensajero lo tomó un segundo antes, dice «El pedido #12 lo lleva otra persona.»
4. Tocá **Abrir en el mapa** para ir con Google Maps. Si hace falta, **Llamar** abre el teléfono con el número del cliente y **WhatsApp** abre un chat con él.
5. En la puerta, cobrá lo que dice el pedido y tocá **Entregado**. Aparece «#12 entregado».
{: .steps}

### El efectivo y la rendición

Cada pedido propio pagado en efectivo que entregás se suma a lo que llevás, y la línea de arriba lo muestra al instante. Lo que se paga con tarjeta, QR, transferencia o que ya estaba pagado no se suma.

Al terminar el turno, entregale el efectivo al encargado o a la caja. Lo cuentan y lo registran en Pedidos › Efectivo, como se explica en [Efectivo de los mensajeros]({{ '/es/projects/fornu/manual/pedidos/' | relative_url }}#efectivo). Ahí queda anotado si faltó o sobró algo.

<div class="callout tip"><p class="callout-title">Consejo</p><p>Si un pedido no aparece en <b>Para retirar</b>, lo más probable es que la cocina no haya tocado <b>Listo</b>. Avisá en la cocina antes de salir sin él.</p></div>
