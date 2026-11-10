---
layout: manual
manual: salon
title: "Salón: mesas, mostrador y cobro · Manual de Fornu"
description: "Cómo se sienta una mesa, se carga y se manda a la cocina por tiempos, se mueven y se unen mesas, se cobra en partes, y cómo se usan el mostrador, el express, las cuentas del día y el armado del salón."
permalink: /es/projects/fornu/manual/salon/
---

## Dónde se vende {#venta}

Todo el salón se atiende desde una sola pantalla de venta. Está en **Salón › Mesas** y también en **Pedidos › Venta**: es la misma pantalla, abierta en el lugar que corresponde. Arriba tiene una pestaña por cada lugar donde se vende, y cada persona ve solo las que su rol le permite.

| Pestaña | Para qué sirve | Quién la ve |
|---|---|---|
| **Mesas** | El salón en vivo: sentar gente, cargar lo que piden, mandarlo a la cocina y cobrar. | Atender mesas o Cobrar mesas |
| **Delivery** | Los pedidos propios y los de las plataformas. Está en [Pedidos y delivery]({{ '/es/projects/fornu/manual/pedidos/' | relative_url }}). | Cocina |
| **Mostrador** | Para llevar o para comer en la barra, cada venta con un nombre para llamar al cliente. | Atender mesas o Cobrar mesas |
| **Mostrador express** | Se carga, se manda a la cocina y se cobra de una vez. En el teléfono dice **Express**. | Cobrar mesas |

Quien maneja plata ve, al lado de las pestañas, si la caja está abierta: **Caja abierta desde las 21:05** en verde o **Caja cerrada** en rojo.

En un equipo del personal (la tablet o el teléfono vinculados al local, donde cada uno entra con su PIN) la pantalla se llama **Venta**. En el teléfono, fuera de un equipo del personal, **Salón** está en la barra de abajo.

Si la pantalla aparece vacía, dice por qué:

- «Ninguna unidad de negocio atiende en el salón todavía.»: alguna unidad tiene que vender en el canal Salón. Quien tiene el permiso Ajustes ve el botón **Prender el Salón en una unidad**, que lleva a Ajustes › Unidades de negocio.
- «El salón todavía no tiene mesas.»: quien puede armar el salón ve **Armar sectores y mesas** (ver [Sectores y mesas](#armar)).
- «Todavía no hay dónde vender: pedile a quien administra la cuenta que te dé acceso.»: tu rol no tiene ningún permiso de venta.

<div class="callout"><p class="callout-title">Importante</p><p>El Salón es un módulo. Si tu cuenta no lo tiene, no vas a ver <b>Salón</b> en la barra ni las pestañas <b>Mesas</b> y <b>Mostrador</b>.</p></div>

## Tres formas de atender el salón {#formas}

Cada local trabaja a su manera, y Fornu acompaña las tres más comunes. Se pueden mezclar: un adicionista carga las mesas del salón mientras los mozos de la vereda cargan desde su teléfono.

### Un adicionista para todo el salón

Los mozos toman el pedido en la mesa y se lo pasan a una persona fija, el adicionista, que carga todo desde una computadora o una tablet. El adicionista abre cada mesa a nombre del mozo que la atiende, así cada cuenta queda de quien la sirvió y después se puede filtrar por mozo en [Cuentas del día](#cuentas). Para eso necesita el permiso **Asignar quién atiende**, que ya trae el rol Adicionista.

Con teclado es lo más rápido: el número de mesa y <kbd>Enter</kbd> la abre, el código del producto y <kbd>Enter</kbd> lo carga.

### Cada mozo es su propio adicionista

Hay una tablet o una computadora en el salón, vinculada al local. Cada mozo entra con su PIN, carga sus mesas y las mesas que abre quedan a su nombre sin elegir nada. Para dejarle el equipo al que sigue, se toca el nombre arriba a la derecha (**Cambiar de persona**) y entra el otro con su PIN. Cómo se vincula un equipo y cómo se entra con PIN está en [En la cocina y en la calle]({{ '/es/projects/fornu/manual/cocina-y-reparto/' | relative_url }}).

### El mozo con su teléfono

Cada mozo lleva su teléfono vinculado al local, entra con su PIN y carga en la mesa misma, mientras le dictan. Manda a la cocina sin moverse y ve en el salón qué mesa tiene algo para servir. Con el rol Mozo no cobra: cuando la mesa pide la cuenta toca **Pidió la cuenta**, la mesa se pone verde en todos los equipos y la caja cobra.

<div class="shot-pair">
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-telefono-mozo.jpg' | relative_url }}" alt="El teléfono de una moza con la pantalla Venta: arriba Fichar entrada, Fichar a alguien y su nombre, y abajo las mesas del salón, dos ocupadas y seis libres." loading="lazy" width="390" height="640">
    <figcaption>El teléfono de una moza, con su PIN.</figcaption>
  </figure>
  <figure class="shot">
    <img src="{{ '/assets/img/fornu/manual/salon-adicionista.jpg' | relative_url }}" alt="La pantalla Venta en la computadora del salón: arriba a la derecha el nombre de quien la usa, a la izquierda la mesa 3 recién abierta a nombre de Valentina, y a la derecha la cuenta de esa mesa con Valentina Sosa como moza" loading="lazy" width="1440" height="650">
    <ol class="marks">
      <li><b>Tomás Romero · Cambiar de persona</b>: quién está usando el equipo. Tocalo para que entre otro.</li>
      <li>La mesa 3, abierta a nombre de Valentina.</li>
      <li>La cuenta dice quién atiende. Con <b>Asignar quién atiende</b>, el nombre se toca para pasarle la mesa a otro.</li>
    </ol>
    <figcaption>La computadora del salón: Tomás carga en la mesa de Valentina.</figcaption>
  </figure>
</div>

### Con teclado o con el dedo

Todo se puede hacer tocando la pantalla y casi todo con el teclado:

| Para | Con el dedo | Con el teclado |
|---|---|---|
| Abrir una mesa | Tocala en el salón. | Escribí el número en **Ir a mesa…** y <kbd>Enter</kbd>. |
| Cargar un producto | Tocalo en la carta. | Escribí el nombre o el código en **Buscar producto…**, elegí con <kbd>↑</kbd> <kbd>↓</kbd> y <kbd>Enter</kbd>. |
| Confirmar un diálogo | Tocá el botón de abajo. | <kbd>Ctrl</kbd> + <kbd>Enter</kbd>. |
| Cerrar un diálogo | Tocá la ✕ o afuera. | <kbd>Esc</kbd>. Si cambiaste algo, pregunta antes: «Hay cambios sin guardar.» |
| Elegir en una lista con buscador | Tocá la fila. | Escribí hasta que quede una y <kbd>Enter</kbd>. |
| Autorizar con PIN | El teclado de la pantalla. | Los números del teclado y <kbd>Enter</kbd>. |

En el teléfono, si todas las mesas se llaman con números, **Ir a mesa…** abre el teclado numérico. Los diálogos suben desde abajo.

## Los permisos del salón {#permisos}

En el salón cada cosa tiene su permiso, para que cada rol haga lo suyo: el mozo carga y manda, la caja cobra, el encargado anula y descuenta. Los permisos se dan por rol, en [Personal]({{ '/es/projects/fornu/manual/personal/' | relative_url }}). Administración puede todo.

| Permiso | Qué deja hacer | Con el PIN de otro |
|---|---|---|
| **Atender mesas** | Abrir mesas a su nombre, cargar lo que piden, sacar lo que todavía no se mandó, mandarlo a la cocina y pedir la cuenta. | No |
| **Asignar quién atiende** | Abrir una mesa a nombre de otro mozo, o pasársela. Es lo que usa el adicionista. | Para pasar la mesa |
| **Mover mesas** | Pasar una mesa a otra libre, mover ítems a otra mesa y unir mesas. | Sí |
| **Anular lo mandado** | Sacar de la cuenta lo que ya fue a la cocina, con la causa. La estación recibe un aviso. | Sí |
| **Descontar e invitar** | Descontar una línea o toda la cuenta con un motivo, invitar la casa y asignar clientes que traen descuento. | En una línea |
| **Cobrar mesas** | Cobrar en partes con propina, cerrar la mesa, vender en el mostrador express y ver las cuentas del día. | No |
| **Deshacer cobros** | Sacar un pago ya cargado de una mesa abierta. | Sí |
| **Cancelar mesas** | Cancelar una mesa entera, con la causa. | Sí |
| **Armar el salón** | Crear sectores y mesas, ubicarlas en el plano y fijar el precio del cubierto. | Nunca |

Los demás, salvo Armar el salón, piden también Atender mesas, y Deshacer cobros pide Cobrar mesas. Cómo se presta un permiso con un PIN está en [Pedir un permiso con el PIN de otro](#autorizar).

Cuando la cuenta prende el Salón, Fornu crea tres roles para empezar, si ningún rol tenía ya permisos del salón. Se cambian como cualquier otro rol, en Personal › Configuración:

| Rol | Permisos |
|---|---|
| **Mozo** | Atender mesas, Mover mesas |
| **Adicionista** | Atender mesas, Asignar quién atiende, Mover mesas, Anular lo mandado, Descontar e invitar, Cobrar mesas |
| **Caja** | Atender mesas, Cobrar mesas, Descontar e invitar, Anular lo mandado, Deshacer cobros, Cancelar mesas |

Como mozo de una mesa puede figurar cualquier persona activa del local cuyo rol tenga algún permiso del salón, salvo Armar el salón.

## Salón › Mesas {#mesas}

Es el salón en vivo. Cada mesa muestra su estado con un color, cuánto hace que está abierta, cuánto lleva y quién la atiende. Se actualiza solo cada vez que cualquier equipo cambia una mesa, así el adicionista, los mozos y la caja ven lo mismo al mismo tiempo.

<p class="perm"><span>Quién puede:</span> <span class="tag">Atender mesas</span> <span class="tag">Cobrar mesas</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-mesas.jpg' | relative_url }}" alt="El salón de la demo en vista Lista: dos sectores, Salón y Vereda, con doce y cuatro mesas. La mesa 3 está ocupada con 8.500 pesos y el aviso Pidió la cuenta. La V1 está ocupada con 12.000. Las demás dicen Libre." loading="lazy" width="1440" height="700">
  <ol class="marks">
    <li><b>Mesas · Delivery · Mostrador · Mostrador express</b>: dónde se vende. Cada uno ve las suyas.</li>
    <li><b>Caja abierta desde las…</b>: lo ve quien cobra, para saber si el efectivo entra en un arqueo.</li>
    <li>Cuántas mesas están ocupadas y cuántos comensales hay, y qué quiere decir cada color.</li>
    <li><b>Plano</b> o <b>Lista</b>: cómo ves el salón. Cada equipo recuerda lo que elegiste.</li>
    <li><b>Ir a mesa…</b>: el número y <kbd>Enter</kbd> abren la mesa.</li>
    <li>Una mesa ocupada: minutos abierta, total, comensales, mozo y su aviso, acá <b>Pidió la cuenta</b>.</li>
  </ol>
  <figcaption>Pedidos › Venta en la demo, con el salón en lista.</figcaption>
</figure>

### Lista o plano

En **Lista**, cada sector tiene su título y sus mesas en baldosas. Una mesa libre se ve punteada y gris, con sus sillas («4 sillas») y la palabra «Libre». Una ocupada muestra los minutos que lleva abierta, el total, los comensales y el mozo. Si ya pagaron una parte, muestra lo que falta.

En **Plano**, cada sector se ve como está armado en el local, con las mesas pintadas del color de su estado, su número y sus minutos. Si hay más de un sector, arriba hay una pestaña por sector con la cantidad de mesas abiertas. Las mesas que todavía no se ubicaron en el plano aparecen abajo, en «Sin ubicar en el plano:», y se tocan igual.

La primera vez, el salón abre en Plano si alguna mesa ya está ubicada, y si no en Lista. Con el Constructor de espacios el plano además se puede ver con paredes, texturas y en isométrica (ver [Espacios]({{ '/es/projects/fornu/manual/espacios/' | relative_url }}#en-el-salon)).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-plano.jpg' | relative_url }}" alt="El salón en vista Plano: pestañas Salón con 2 mesas abiertas y Vereda con 0, y el plano con nueve mesas. La 2 pintada de azul y la 3 de ámbar, las dos con 0 min." loading="lazy" width="1440" height="630">
  <ol class="marks">
    <li><b>Plano</b>: el salón dibujado.</li>
    <li>Un sector por pestaña, con cuántas mesas tiene abiertas.</li>
    <li>La mesa 2, en azul: ocupada.</li>
    <li>La mesa 3, en ámbar: tiene algo cargado sin mandar a la cocina.</li>
  </ol>
  <figcaption>El mismo salón, en plano.</figcaption>
</figure>

### Qué quiere decir cada color

Cada mesa muestra un solo estado: si le corresponde más de uno, el de más arriba en esta tabla, que es el más urgente.

| Estado | Color | Qué pasa | Qué dice la baldosa |
|---|---|---|---|
| **Para servir** | Naranja | La cocina terminó una ronda y hay que llevarla. | «1 ronda para servir» |
| **Sin mandar** | Ámbar | Hay algo cargado que la cocina todavía no recibió. | «2 sin mandar» |
| **En espera** | Azul punteado | Un tiempo está esperando que el mozo lo marche. | «Principal en espera · 12 min» |
| **Pagando** | Verde oscuro | Ya pagó una parte y falta el resto. | «Pagando», y lo que falta |
| **Pidió la cuenta** | Verde | La mesa pidió la cuenta. | «Pidió la cuenta» |
| **Ocupada** | Azul | Está atendida y no falta nada. | El total, los comensales y el mozo |
| **Libre** | Borde punteado | No hay nadie. | «Libre» |

### Sentar una mesa

1. Tocá una mesa libre. Al lado se abre un cuadro chico con el nombre de la mesa y sus sillas.
2. Si más de una unidad de negocio atiende en el salón, elegí primero la unidad.
3. En **¿Cuántos se sientan?**, tocá la cantidad. Aparece marcado el número igual a las sillas de la mesa.
{: .steps}

Con ese toque la mesa queda abierta a tu nombre y su cuenta se abre al lado, lista para cargar. El cuadro se cierra si tocás afuera o apretás <kbd>Esc</kbd>.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-sentar.jpg' | relative_url }}" alt="El cuadro que se abre al tocar la mesa 1 libre: Mesa 1 · 4 sillas, la pregunta ¿Cuántos se sientan?, botones del 1 al 8 con el 4 marcado, y el link Más opciones." loading="lazy" width="740" height="370">
  <ol class="marks">
    <li><b>¿Cuántos se sientan?</b>: un toque abre la mesa con esa cantidad.</li>
    <li><b>Más opciones…</b>: para más de 8 comensales o para abrirla a nombre de otro.</li>
  </ol>
  <figcaption>Sentar a cuatro en la mesa 1.</figcaption>
</figure>

**Más opciones…** abre el diálogo completo, con **Comensales** (de 1 a 99) y, para quien tiene Asignar quién atiende, **Atiende**: tocá el mozo que va a servir la mesa. Si no elegís a nadie, la mesa queda a tu nombre. Después tocá **Abrir la mesa**.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-atiende.jpg' | relative_url }}" alt="El diálogo Mesa 3 con las unidades Doble Smash y Pizzería, Comensales en 2, la nota La mesa tiene 4 sillas, y Atiende con Tomás Romero y Valentina Sosa, elegida" loading="lazy" width="620" height="330">
  <ol class="marks">
    <li><b>Comensales</b>, con las sillas que tiene la mesa como referencia.</li>
    <li><b>Atiende</b>: el adicionista abre la mesa a nombre de Valentina.</li>
  </ol>
  <figcaption>Abrir una mesa para otra moza.</figcaption>
</figure>

Si dos personas sientan la misma mesa a la vez, la segunda ve «La mesa 4 ya está ocupada.» y el salón se actualiza.

### Ir a una mesa por número

Para el adicionista con teclado, o el mozo que ya sabe el número:

1. Escribí el número en **Ir a mesa…**.
2. Apretá <kbd>Enter</kbd> o tocá la flecha.
{: .steps}

Abre la mesa esté libre u ocupada. Busca primero una mesa que se llame exactamente así, y si no la única con ese número: «07» abre la 7, y «12» abre la M12 si es la única 12. Si no hay ninguna, o hay más de una, avisa «No hay una mesa 99». Una mesa libre abierta así muestra el diálogo completo, con los comensales.

<div class="shot-phones">
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-telefono-mesas.jpg' | relative_url }}" alt="El salón en un teléfono: tres mesas por fila, la 1 ocupada y las demás libres, con el campo Ir a mesa arriba y la barra de abajo con Inicio, Pedidos, Salón, Insumos y Más." loading="lazy" width="390" height="844">
    <figcaption>El salón en el teléfono, tres mesas por fila.</figcaption>
  </figure>
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-telefono-ir-a-mesa.jpg' | relative_url }}" alt="En el teléfono, el diálogo Mesa 3 que sube desde abajo, con Comensales en 2, la nota La mesa tiene 4 sillas y los botones Cancelar y Abrir la mesa." loading="lazy" width="360" height="740">
    <figcaption>Ir a la mesa 3, que estaba libre.</figcaption>
  </figure>
</div>

## La mesa abierta {#mesa}

Al tocar una mesa ocupada se abre su cuenta. En la computadora aparece al lado del salón, para no perderlo de vista. En una pantalla más chica ocupa todo el lugar, con una flecha arriba para volver. Ahí se carga lo que piden, se manda a la cocina por rondas y se pide o se cobra la cuenta.

<p class="perm"><span>Quién puede:</span> <span class="tag">Atender mesas</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-mesa.jpg' | relative_url }}" alt="La mesa 1 abierta al lado del salón: dos comensales, el cliente sin elegir, el estado Abierta, la pestaña Cuenta con un 2, el buscador de productos, el bloque Sin mandar con un Doble cheddar y un Triple bacon, el cubierto de dos comensales y el botón Mandar a la cocina · 2." loading="lazy" width="1440" height="630">
  <ol class="marks">
    <li>La mesa en el salón: «2 sin mandar» avisa que hay algo que la cocina todavía no recibió.</li>
    <li>Comensales, cliente y estado. Arriba, el número de cuenta, la unidad de negocio, el mozo y hace cuánto está abierta.</li>
    <li><b>Carta</b> y <b>Cuenta</b>. El número al lado de Cuenta es lo que falta mandar.</li>
    <li><b>Buscar producto…</b>: por nombre, categoría o código.</li>
    <li><b>Sin mandar</b>: lo cargado, con el lápiz para cambiarlo y la ✕ para sacarlo.</li>
    <li><b>Mandar a la cocina · 2</b>: manda lo cargado como una ronda.</li>
  </ol>
  <figcaption>La mesa 1 con dos productos cargados.</figcaption>
</figure>

La barra de abajo siempre tiene a mano el próximo paso: **Mandar a la cocina** si hay algo cargado, **Marchar** si un tiempo espera, **Pidió la cuenta** y, para quien cobra, **Cobrar $ …** (o **Cerrar sin cargo** si la cuenta da cero). El estado de la cuenta puede ser **Abierta**, **Pidió la cuenta**, **Cobrada** o **Cancelada**, y el menú **Más acciones** (⋯) junta lo que se hace sobre toda la mesa.

### Cargar lo que piden

Hay tres maneras, y se mezclan:

- **Tocando la carta.** Los productos están agrupados por categoría, con su código si tiene, su nombre y su precio. Un producto sin opciones entra a la cuenta con un toque. Tocarlo otra vez suma uno a la misma línea: tres gaseosas son una línea de 3.
- **Buscando.** Escribí en **Buscar producto…** parte del nombre o de la categoría. Elegí con <kbd>↑</kbd> <kbd>↓</kbd> y agregalo con <kbd>Enter</kbd>. <kbd>Esc</kbd> borra la búsqueda.
- **Por código.** Si los productos tienen código en la [Carta]({{ '/es/projects/fornu/manual/carta/' | relative_url }}), como «A7», escribí el código entero y apretá <kbd>Enter</kbd>: el producto con ese código sale primero. Es la forma más rápida para el adicionista.

Cada línea se guarda en el momento, así cualquier otro equipo la ve enseguida. Lo agotado dice «Agotado hoy» en la carta y «Agotado» en la búsqueda, y no se puede cargar.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-buscar.jpg' | relative_url }}" alt="El buscador con la palabra Papa y una sola sugerencia: Papas fritas, de la categoría Para acompañar, a 4.500 pesos. Debajo, la carta con Burgers y Para acompañar." loading="lazy" width="510" height="390">
  <figcaption>Buscar «Papa»: <kbd>Enter</kbd> agrega las papas fritas.</figcaption>
</figure>

Un producto con opciones (el punto de la carne, los adicionales) abre un diálogo antes de entrar. Cada grupo dice cuántas se eligen («elegí 1», «hasta 2», «de 1 a 3») y cada opción su precio extra («+$ 800») o «agotado». Abajo están **Cantidad** y **Aclaración (opcional)**, por ejemplo «Sin pepinos». Tocá **Agregar · $ …**. Si falta elegir en un grupo obligatorio, Fornu dice cuál.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-opciones.jpg' | relative_url }}" alt="El diálogo del Doble cheddar con Extras hasta 3, un Extra cheddar elegido, Sumale una bebida hasta 1 con la gaseosa elegida, Cantidad 1, la aclaración Sin pepinos y el botón Agregar · $ 12.800" loading="lazy" width="620" height="900">
  <ol class="marks">
    <li>Un grupo y cuántas se eligen: «hasta 3». Las que se pueden pedir más de una vez tienen − y +.</li>
    <li>Otro grupo, «hasta 1»: un toque elige.</li>
    <li><b>Cantidad</b>.</li>
    <li><b>Aclaración (opcional)</b>.</li>
    <li><b>Agregar · $ …</b>, con el precio de lo elegido.</li>
  </ol>
  <figcaption>Un Doble cheddar con extra cheddar y gaseosa.</figcaption>
</figure>

### Los tiempos: Cargando para {#tiempos}

Si la carta usa tiempos, lo que se carga no sale todo junto. La cocina recibe primero lo que va primero, y el resto espera hasta que el mozo lo marcha. Así el principal no sale con la entrada.

Los tiempos aparecen cuando alguna categoría de la carta tiene un **Va de** distinto de Principal (se elige en Carta › Categorías). Entonces la cuenta muestra la fila **Cargando para**:

| Opción | Qué hace |
|---|---|
| **Según la carta** | Cada producto va en el tiempo de su categoría. Las categorías sin tiempo van como Principal. Es la opción de siempre. |
| **Ya** | Sale con la próxima ronda, como las bebidas. |
| **Entrada**, **Principal**, **Postre** | Todo lo que cargues ahora va en ese tiempo, sea de la categoría que sea. |

Elegí el tiempo antes de tocar los productos. Las líneas sin mandar muestran una etiqueta chica con su tiempo.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-cargando-para.jpg' | relative_url }}" alt="La mesa 1 con la fila Cargando para: Según la carta, Ya, Entrada, Principal marcado y Postre. En el salón la mesa dice 2 sin mandar y la pestaña Cuenta tiene un 2." loading="lazy" width="1440" height="630">
  <ol class="marks">
    <li>La mesa avisa «2 sin mandar».</li>
    <li><b>Cargando para</b>: acá, lo próximo va como principal.</li>
    <li>La cuenta, con dos líneas por mandar.</li>
  </ol>
  <figcaption>Lo que se cargue ahora sale como principal.</figcaption>
</figure>

Al mandar, sale todo lo que va en **Ya** y el primer tiempo cargado, salvo que ese tiempo ya tenga algo esperando. Los tiempos que siguen quedan **en espera**: no descuentan stock ni imprimen comanda hasta que se marchan. La mesa lo muestra en el salón, por ejemplo «Principal en espera · 12 min», para que el mozo sepa cuánto hace que espera.

Cuando es el momento, tocá **Marchar principal** (en el bloque que espera o en la barra de abajo). Sale como la próxima ronda y Fornu avisa «Principal marchado a la cocina.».

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-en-espera.jpg' | relative_url }}" alt="La mesa 1 con la baldosa Principal en espera · 0 min, y en la cuenta el bloque Principal · en espera con una Gaseosa en lata y el botón Marchar principal, debajo la Ronda 1 en la cocina, y abajo los botones Marchar principal y Pidió la cuenta." loading="lazy" width="1440" height="510">
  <ol class="marks">
    <li>En el salón: qué tiempo espera y hace cuánto.</li>
    <li><b>Principal · en espera</b>: lo que todavía no fue a la cocina, con su propio botón para marcharlo.</li>
    <li><b>Marchar principal</b>, también en la barra de abajo.</li>
  </ol>
  <figcaption>La ronda 1 ya está en la cocina y el principal espera.</figcaption>
</figure>

<div class="callout tip"><p class="callout-title">Consejo</p><p>Mandar nunca manda un tiempo que viene después. Si una mesa quiere todo junto, cargalo en <b>Ya</b>.</p></div>

### Mandar a la cocina

1. Revisá el bloque **Sin mandar**.
2. Tocá **Mandar a la cocina · 2**. El número son las unidades que salen.
3. Fornu avisa «Mandado a la cocina.» y lo cargado pasa a ser la **Ronda 1**.
{: .steps}

Cada ronda descuenta su stock, imprime una comanda en cada estación que prepara algo de ella (ver [Estaciones de cocina]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#estaciones)) y aparece en el [tablero de la cocina]({{ '/es/projects/fornu/manual/pedidos/' | relative_url }}#tablero). Si no hay nada nuevo, Fornu avisa «No hay nada nuevo para mandar a la cocina.», y si lo que queda es un tiempo en espera, «Lo que queda está en espera: marchalo cuando sea su tiempo.».

En la cuenta, las rondas se ven de la más nueva a la más vieja. Cada una dice su estado (**En la cocina**, **Lista para servir** o **En la mesa**), la hora en que salió y, si fue a más de una estación, a cuáles.

### Cambiar o sacar lo que todavía no se mandó

Mientras no se mandó, una línea se cambia o se saca sin dejar rastro.

- **El lápiz** abre la línea con su nombre arriba: **Cantidad** (de 1 a 99), **Va de** si la carta usa tiempos, y **Nota para la cocina (opcional)**, por ejemplo «Sin sal, bien cocido, sin hielo…». Debajo están las notas rápidas de su categoría: tocá una para sumarla a la nota y otra vez para sacarla. Tocá **Guardar**, o **Sacar de la mesa** para quitarla.
- **La ✕** la saca en el momento. Fornu avisa «Sacaste 1 × Doble cheddar.» con un botón **Deshacer** que la vuelve a cargar igual.

Si otro equipo cambió la misma línea mientras la editabas, Fornu avisa cuántas hay ahora y te pide que la mires de nuevo.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-nota.jpg' | relative_url }}" alt="El diálogo de una Gaseosa en lata sin mandar: Cantidad 1, Va de con Principal marcado, la nota Sin sal, y las notas rápidas Sin sal, marcada, y Con cheddar." loading="lazy" width="620" height="380">
  <ol class="marks">
    <li><b>Cantidad</b>.</li>
    <li><b>Va de</b>: en qué tiempo sale.</li>
    <li><b>Nota para la cocina</b>: sale en la comanda.</li>
    <li>Las notas rápidas de la categoría: un toque en vez de escribir.</li>
  </ol>
  <figcaption>Cambiar una línea antes de mandarla.</figcaption>
</figure>

<div class="callout tip"><p class="callout-title">Consejo</p><p>Las notas rápidas se cargan en Carta › Categorías, una por línea (por ejemplo «Jugoso», «A punto», «Cocido»). Aparecen al tocar el lápiz de una línea sin mandar, no al cargar el producto.</p></div>

<div class="callout"><p class="callout-title">Importante</p><p>Una vez mandada, una línea solo se puede <a href="#anular">anular</a>, con una causa, y queda registrado quién lo hizo.</p></div>

### Para servir y La llevé

Cuando la cocina marca una ronda como lista, la mesa se pone naranja en el salón con «1 ronda para servir», y en la cuenta esa ronda dice **Lista para servir**. El mozo la lleva y toca **La llevé**: la ronda pasa a **En la mesa**, Fornu avisa «Ronda 1 en la mesa.» y la tarjeta sale del tablero de la cocina.

<div class="shot-phones">
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-ronda-para-servir.jpg' | relative_url }}" alt="El salón en el teléfono, en tema oscuro: la mesa 1 con borde naranja y el aviso 1 ronda para servir, y la mesa 2 en verde con Pidió la cuenta." loading="lazy" width="390" height="640">
    <figcaption>La mesa 1 tiene algo para servir.</figcaption>
  </figure>
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-la-lleve.jpg' | relative_url }}" alt="La cuenta de la mesa 1 en el teléfono: la Ronda 1 con la etiqueta Lista para servir y el botón La llevé, dos papas fritas con la nota Bien cocidas." loading="lazy" width="390" height="640">
    <figcaption>La ronda está lista: <b>La llevé</b>.</figcaption>
  </figure>
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-en-la-mesa.jpg' | relative_url }}" alt="La misma cuenta después de tocar La llevé: el aviso Ronda 1 en la mesa y la ronda con el estado En la mesa." loading="lazy" width="390" height="640">
    <figcaption>Ronda 1 en la mesa.</figcaption>
  </figure>
</div>

### Comensales y cubierto

Los comensales se cambian con − y + en la cabecera de la cuenta, mientras la mesa está abierta y no tiene pagos. Si el local cobra cubierto (se fija en [Sectores y mesas](#armar)), la cuenta lo suma por cada comensal: «Cubierto · 2 × $ 1.500».

Abajo de las líneas, la cuenta muestra **Productos** (cuando hay cubierto o descuento), **Cubierto**, **Descuento** con su motivo, **Total**, **IVA contenido** si la cuenta es Responsable Inscripto, y **Pagado** y **Saldo** cuando ya hay pagos.

### Pidió la cuenta

1. Cuando la mesa pide la cuenta, tocá **Pidió la cuenta**.
2. La mesa se pone verde en todos los equipos y la cuenta dice **Pidió la cuenta**.
3. Si la cocina tiene impresora de tickets, sale la precuenta: «La mesa pidió la cuenta: la precuenta sale por la impresora.».
{: .steps}

La precuenta se imprime sola la primera vez. Para otra copia, **Más acciones** (⋯) › **Imprimir la precuenta**. Sin impresora de tickets se abre la impresión del navegador con una hoja que lleva el nombre del local, la mesa y su número, la fecha, quién atendió, los comensales, las líneas, el cubierto, el descuento, el total, el IVA contenido, lo pagado y el saldo, y al pie «No válido como factura.».

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-precuenta.jpg' | relative_url }}" alt="La precuenta impresa de la mesa 4: la cocina, la mesa y su número, la fecha, quién atendió, dos comensales, cada línea con su importe, el cubierto y el total" loading="lazy" width="330" height="300">
  <figcaption>La precuenta que sale por la impresora del navegador.</figcaption>
</figure>

Si después se carga algo más, la mesa deja de figurar como que pidió la cuenta. Si queda un tiempo en espera, Fornu no deja pedirla: «Hay postre en espera: marchalo o sacalo antes de cobrar.».

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-pidio-la-cuenta.jpg' | relative_url }}" alt="La mesa 1 en verde con el aviso Pidió la cuenta, su cuenta con el estado Pidió la cuenta, el menú de tres puntos debajo, y el mensaje La mesa pidió la cuenta: la precuenta sale por la impresora." loading="lazy" width="1440" height="630">
  <ol class="marks">
    <li>En el salón, la mesa en verde.</li>
    <li>El estado de la cuenta.</li>
    <li><b>Más acciones</b> (⋯): para reimprimir la precuenta.</li>
    <li>El aviso de que la precuenta salió.</li>
  </ol>
  <figcaption>La mesa 1 pidió la cuenta.</figcaption>
</figure>

### En el teléfono

En el teléfono la cuenta ocupa toda la pantalla, y la flecha de arriba vuelve al salón. **Carta** y **Cuenta** son dos pestañas. Mientras estás en la carta con algo cargado, abajo aparece una barra con «2 sin mandar · $ 25.700» (tocala para ver la cuenta) y el botón **Mandar**, para mandar sin cambiar de pestaña.

<figure class="shot phone">
  <img src="{{ '/assets/img/fornu/manual/salon-telefono-sin-mandar.jpg' | relative_url }}" alt="La mesa 9 en el teléfono de una moza, en la pestaña Carta, con la barra de abajo que dice 2 sin mandar · $ 6.500 y el botón Mandar" loading="lazy" width="390" height="844">
  <ol class="marks">
    <li>Lo que falta mandar: tocalo para ver la cuenta.</li>
    <li><b>Mandar</b>, sin salir de la carta.</li>
  </ol>
  <figcaption>La barra de lo que falta mandar, en el teléfono.</figcaption>
</figure>

## Sobre una línea o sobre la mesa {#acciones}

Lo que ya fue a la cocina se anula, se descuenta o se mueve, y siempre queda registrado quién lo hizo. Cada línea mandada tiene su menú ⋯, y la mesa tiene el suyo, **Más acciones** (⋯), en la cabecera. El menú de una línea aparece mientras la mesa está abierta, la línea no está anulada y todavía no hay pagos.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-menu-mesa.jpg' | relative_url }}" alt="El menú Más acciones de la mesa 2 abierto: Mover la mesa entera, Mover ítems, Unir con otra mesa, Pasarla a otro mozo, Reimprimir la ronda 1, Imprimir la precuenta y Cancelar la mesa" loading="lazy" width="510" height="520">
  <figcaption>El menú <b>Más acciones</b> (⋯) de una mesa.</figcaption>
</figure>

Si una opción tiene un candado, tu rol no tiene ese permiso: la podés usar igual y Fornu pide el PIN de alguien que lo tenga (ver [Pedir un permiso con el PIN de otro](#autorizar)).

### Anular lo mandado {#anular}

<p class="perm"><span>Quién puede:</span> <span class="tag">Anular lo mandado</span></p>

1. Tocá ⋯ en la línea y elegí **Anular**.
2. Si la línea tiene varias unidades, elegí cuántas en **Cuántos** («1 de 2»).
3. Elegí **¿Por qué?**: Error de carga, Se arrepintió, Salió mal, Demora, No había u Otro. Con Otro, contá el motivo en **Nota**.
4. Tocá **Anular** (o **Anular 1 de 2**).
{: .steps}

La línea queda tachada en la cuenta, con «Anulado por Administración: Salió mal». El stock sigue descontado, porque la cocina ya lo usó. Si la comanda de esa estación ya estaba impresa, la estación recibe un ticket **ANULADO** con el motivo y quién anuló. Si todavía no se había impreso, la línea directamente no sale.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-anular.jpg' | relative_url }}" alt="El diálogo Anular 2 × Papas fritas: el texto Ronda 1, mandada a las 12:41, Cuántos en 1 de 2, las causas Error de carga, Se arrepintió, Salió mal (marcada), Demora, No había y Otro, y el campo Nota." loading="lazy" width="620" height="420">
  <ol class="marks">
    <li><b>Cuántos</b>: una de las dos porciones.</li>
    <li><b>¿Por qué?</b>: la causa es obligatoria.</li>
    <li><b>Nota</b>: opcional, se suma al motivo. Con «Otro», obligatoria.</li>
  </ol>
  <figcaption>Anular una de dos porciones de papas.</figcaption>
</figure>

### Descontar o invitar una línea {#descontar}

<p class="perm"><span>Quién puede:</span> <span class="tag">Descontar e invitar</span></p>

1. Tocá ⋯ en la línea y elegí **Descontar…**.
2. Si tiene varias unidades, elegí cuántas.
3. Elegí el **Motivo**. Cada motivo trae su porcentaje, que se puede cambiar en **Porcentaje**. Abajo dice cuánto se descuenta: «Se descuentan $ 2.000».
4. Tocá **Descontar**. Al 100%, el botón dice **Invitar**.
{: .steps}

La línea queda en la cuenta y se vende igual, así que su stock se descuenta. Se ve con el precio viejo tachado y «−10% · Cliente habitual» o «Invitado · Invita la casa». Para volver atrás, ⋯ › **Sacar el descuento**. Los motivos y sus porcentajes se cargan en Ajustes › Descuentos (ver [Ajustes]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }})). Si no hay ninguno, Fornu avisa «No hay motivos de descuento: cargalos en Ajustes.».

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-descontar.jpg' | relative_url }}" alt="El diálogo Descontar Gaseosa en lata: el texto Queda en la cuenta con su descuento y se vende igual, los motivos Invita la casa 100% (marcado), Consumo del personal 100%, Cliente habitual 10% y Demora 10%, y Porcentaje en 100." loading="lazy" width="620" height="370">
  <ol class="marks">
    <li><b>Motivo</b>: los de la cuenta, con su porcentaje.</li>
    <li><b>Porcentaje</b>: se completa solo y se puede cambiar.</li>
  </ol>
  <figcaption>Invitar una gaseosa.</figcaption>
</figure>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-cuenta-descuentos.jpg' | relative_url }}" alt="La Ronda 1 de una cuenta: unas papas fritas tachadas con Anulado por Administración: Salió mal, una gaseosa con el precio de 2.000 tachado, 0 pesos e Invitado · Invita la casa, y otras papas fritas a 4.500 con su menú de tres puntos." loading="lazy" width="510" height="240">
  <ol class="marks">
    <li>Una línea anulada, con quién y por qué.</li>
    <li>Una línea invitada, con el precio tachado.</li>
    <li>El menú ⋯ de una línea mandada.</li>
  </ol>
  <figcaption>Cómo quedan en la cuenta.</figcaption>
</figure>

El descuento a toda la cuenta se hace al [cobrar](#descuento-cuenta).

### Asignar un cliente {#cliente}

<p class="perm"><span>Quién puede:</span> <span class="tag">Atender mesas</span> <span class="tag">Descontar e invitar</span></p>

Un cliente conocido puede traer su descuento: los dueños que comen gratis, el personal con el 50%. Al asignarlo, el descuento se aplica solo.

1. Tocá **Cliente** en la cabecera de la cuenta.
2. En **¿Para quién es?**, buscá por nombre o teléfono. Cada fila muestra su teléfono y su descuento («100% · Invita la casa») o «Sin descuento».
3. Tocá el cliente.
{: .steps}

El descuento del cliente se aplica a toda la cuenta y queda registrado con su motivo o con el nombre del cliente. Si después alguien escribe un descuento a mano, reemplaza al del cliente. **Sin cliente** saca el cliente y el descuento que trajo.

Cualquiera que atiende mesas puede asignar un cliente sin descuento. Los clientes con descuento aparecen en gris para quien no tiene Descontar e invitar, con «Trae 100% de descuento: lo asigna quien puede descontar.», y esto no se presta con PIN. Los clientes se cargan en Pedidos › Clientes. Si no hay ninguno: «Todavía no hay clientes: se cargan en Pedidos → Clientes.».

<div class="shot-pair">
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-cliente-telefono.jpg' | relative_url }}" alt="En el teléfono de una moza, el diálogo ¿Para quién es? con el buscador, la clienta Ana con su teléfono, y Dueños en gris con el texto Trae 100% de descuento: lo asigna quien puede descontar." loading="lazy" width="390" height="314">
    <figcaption>Para una moza, Dueños está en gris.</figcaption>
  </figure>
  <figure class="shot">
    <img src="{{ '/assets/img/fornu/manual/salon-cliente.jpg' | relative_url }}" alt="La cuenta de la mesa 1 con el cliente Dueños en la cabecera, unas papas fritas de 4.500, la línea Descuento 100% · Invita la casa por menos 4.500 y el botón Cerrar sin cargo." loading="lazy" width="510" height="630">
    <ol class="marks">
      <li>El cliente asignado, en lugar de «Cliente».</li>
      <li>Su descuento, a toda la cuenta.</li>
      <li><b>Cerrar sin cargo</b>: la cuenta quedó en cero.</li>
    </ol>
    <figcaption>La mesa de los dueños.</figcaption>
  </figure>
</div>

### Mover ítems a otra mesa {#mover}

<p class="perm"><span>Quién puede:</span> <span class="tag">Mover mesas</span></p>

Para cuando alguien se cambia de mesa, o una parte de la mesa se va a la barra.

1. Tocá **Más acciones** (⋯) › **Mover ítems…**. Desde una línea, ⋯ › **Mover a otra mesa…** abre lo mismo con esa línea ya tildada.
2. Tildá lo que se mueve, o **Todo**. Cada línea dice si está sin mandar, en espera o en qué ronda. En las de varias unidades elegí cuántas.
3. En **¿A qué mesa?** tocá la mesa. Las libres dicen «4 sillas · libre». Las ocupadas muestran su total, comensales y mozo.
4. Si la mesa está libre, poné los **Comensales**: se abre con lo que se mueve, a nombre del mismo mozo.
5. Tocá **Mover a Mesa 2**.
{: .steps}

Si la otra mesa está ocupada, lo movido se suma a su cuenta. Lo mandado conserva su ronda y su lugar en la cocina, y lo que no se mandó queda para mandar desde la otra mesa. Esa mesa deja de figurar como que pidió la cuenta. Lo anulado no se mueve, y las dos mesas tienen que vender la misma carta.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-mover.jpg' | relative_url }}" alt="El diálogo Mover ítems de Mesa 1: la casilla Todo, la línea Papas fritas · ronda 1 tildada con 1 de 2, y debajo ¿A qué mesa? con las mesas 2 a 8 del Salón, todas 4 sillas · libre." loading="lazy" width="620" height="440">
  <ol class="marks">
    <li><b>Todo</b>: mueve toda la cuenta.</li>
    <li>Una línea tildada, con cuántas unidades se mueven.</li>
    <li><b>¿A qué mesa?</b>: las mesas del local, por sector.</li>
  </ol>
  <figcaption>Mover una porción de papas a otra mesa.</figcaption>
</figure>

### Mover la mesa entera

<p class="perm"><span>Quién puede:</span> <span class="tag">Mover mesas</span></p>

**Más acciones** (⋯) › **Mover la mesa entera** muestra las mesas libres por sector. Tocá una y la mesa se muda con todo. Fornu avisa «Mesa 1 → Mesa 2.» con un botón **Deshacer** que la vuelve a su lugar.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-mover-mesa.jpg' | relative_url }}" alt="El panel Mover Mesa 2 con las mesas libres del Salón y de la Vereda, cada una con sus sillas" loading="lazy" width="620" height="420">
  <figcaption>Las mesas libres, por sector. Un toque muda la mesa.</figcaption>
</figure>

### Unir con otra mesa

<p class="perm"><span>Quién puede:</span> <span class="tag">Mover mesas</span></p>

1. Tocá **Más acciones** (⋯) › **Unir con otra mesa…**. Aparecen solo las mesas ocupadas.
2. Elegí la mesa. Fornu explica qué va a pasar: «3 comensales y todo lo pedido pasan a Mesa 2, con su ronda y su lugar en la cocina. Mesa 1 queda libre.».
3. Tocá **Unir con Mesa 2**.
{: .steps}

La pantalla salta a la mesa que recibió todo. La otra se cierra como cancelada con «Unida a Mesa 2».

### Pasarla a otro mozo

<p class="perm"><span>Quién puede:</span> <span class="tag">Asignar quién atiende</span></p>

Cuando cambia el turno o un mozo se va: **Más acciones** (⋯) › **Pasarla a otro mozo**, o tocá el nombre del mozo en la cabecera. En **¿Quién la atiende?** buscá el nombre y tocalo (con <kbd>Enter</kbd> elegís el único que quedó). Fornu avisa «La mesa cambió de mozo.».

Si nadie puede atender, Fornu avisa «Nadie del local tiene un rol que atienda mesas: se asigna en Personal → Equipo.».

### Reimprimir una ronda

**Más acciones** (⋯) › **Reimprimir la ronda 1** manda otra copia de esa comanda, marcada **REIMPRESIÓN**: «Ronda 1: sale otra copia.».

### Cancelar la mesa

<p class="perm"><span>Quién puede:</span> <span class="tag">Cancelar mesas</span></p>

Para la mesa que se levanta y se va, o la que se abrió por error. También sirve para una venta del mostrador.

1. Tocá **Más acciones** (⋯) › **Cancelar la mesa**.
2. Leé lo que va a pasar: «Lo que no se mandó sale; lo mandado queda anulado con este motivo, y su stock sigue descontado.».
3. Elegí la causa, con las mismas opciones que al anular. Si no se mandó nada, la causa es opcional y queda como «Se levantó sin pedir».
4. Tocá **Cancelar la mesa**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-cancelar-mesa.jpg' | relative_url }}" alt="El panel Cancelar Mesa 2 con lo que va a pasar, las causas Error de carga, Se arrepintió, Salió mal, Demora, No había y Otro, y la nota opcional" loading="lazy" width="620" height="420">
  <figcaption>Cancelar una mesa pide la causa.</figcaption>
</figure>

Las estaciones que ya habían impreso algo reciben su aviso **ANULADO**. Fornu avisa «Mesa cancelada.».

<div class="callout"><p class="callout-title">Importante</p><p>Con pagos cargados la cuenta queda fija: no se anula, no se descuenta, no se cambian los comensales ni el cliente, no se mueven ítems, no se une ni se cancela. Primero hay que <a href="#anular-pago">anular los pagos</a>, con el permiso Deshacer cobros.</p></div>

## Pedir un permiso con el PIN de otro {#autorizar}

Un mozo no necesita todos los permisos para resolver en la mesa. Si su rol no tiene uno de los que se prestan, la opción aparece con un candado. La usa igual, y antes de hacerse Fornu pide el PIN de alguien que sí lo tiene, como el encargado.

1. Elegí la opción con candado y completá el diálogo de siempre: la causa, el descuento o la mesa de destino.
2. Aparece **Hace falta autorización**, con un resumen de lo que se va a hacer, por ejemplo «Anular 1 × Papas fritas (ronda 1) de Mesa 1».
3. En **¿Quién autoriza?**, tocá a la persona. Los que están en turno aparecen primero, con «· en turno». Si hay una sola, ya viene elegida.
4. Esa persona escribe su PIN, de 4 a 6 números, en el teclado de la pantalla o en el del equipo, y toca **Autorizar**.
{: .steps}

La autorización sirve para esa sola acción y por dos minutos. En la cuenta queda quién lo hizo y quién lo autorizó: «Anulado por Mariana (autorizó Diego): Se arrepintió».

<div class="shot-phones">
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-autorizar-menu.jpg' | relative_url }}" alt="La cuenta de la mesa 1 en el teléfono de Mariana, con el menú de una línea abierto: Descontar con un candado, Mover a otra mesa sin candado, y Anular en rojo con un candado." loading="lazy" width="390" height="520">
    <figcaption>Mariana puede mover, pero no anular ni descontar.</figcaption>
  </figure>
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-autorizar-pin.jpg' | relative_url }}" alt="El diálogo Hace falta autorización: el resumen Anular 1 × Papas fritas (ronda 1) de Mesa 1, ¿Quién autoriza? con Diego elegido, cuatro círculos para el PIN y un teclado del 0 al 9." loading="lazy" width="390" height="560">
    <figcaption>Diego autoriza con su PIN.</figcaption>
  </figure>
  <figure class="shot phone">
    <img src="{{ '/assets/img/fornu/manual/salon-autorizar-hecho.jpg' | relative_url }}" alt="La cuenta después: el aviso Papas fritas: anulado, y la línea tachada con Anulado por Mariana (autorizó Diego): Se arrepintió. El total queda en 0." loading="lazy" width="390" height="660">
    <figcaption>Queda quién anuló y quién autorizó.</figcaption>
  </figure>
</div>

Pasan por PIN, cuando falta el permiso:

- **Anular** una línea.
- **Descontar…** y **Sacar el descuento** en una línea.
- **Mover la mesa entera**, **Mover ítems…**, **Mover a otra mesa…** y **Unir con otra mesa…**.
- **Pasarla a otro mozo**.
- **Anular este pago**.
- **Cancelar la mesa**.

No pasan por PIN, y sin el permiso directamente no aparecen: cobrar, el descuento a toda la cuenta al cobrar, asignar un cliente con descuento y abrir una mesa a nombre de otro. **Armar el salón** no se presta nunca.

Qué puede salir mal:

- «PIN incorrecto · quedan 4 intentos.». Con demasiados intentos, esa persona queda bloqueada unos minutos, como al entrar.
- «Diego no puede autorizar eso.» o «Diego todavía no tiene PIN: pedíselo a la administración.».
- «Nadie de este local puede autorizar esto con su PIN: se da en Personal → Configuración, en el rol de quien corresponda.».

## Cobrar {#cobrar}

La caja cobra desde la cuenta de la mesa: todo junto, lo que consumió cada uno o en partes iguales, con uno o varios medios de pago y con propina. Sin el permiso Cobrar mesas el botón no aparece, y el mozo usa **Pidió la cuenta**.

<p class="perm"><span>Quién puede:</span> <span class="tag">Cobrar mesas</span></p>

El botón **Cobrar $ …** aparece abajo cuando no queda nada sin mandar ni en espera. Si la cuenta da cero (por ejemplo, la mesa de los dueños), dice **Cerrar sin cargo**. Abre el diálogo «Cobrar Mesa 1», o «Cobrar Mesa 1 · saldo $ 7.500» si ya hay pagos.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-cobrar.jpg' | relative_url }}" alt="El diálogo Cobrar Mesa 1 en Todo: a la izquierda lo consumido, tres gaseosas y dos papas fritas por 15.000. A la derecha Aplicar un descuento, los medios de pago con Efectivo elegido, Monto 15.000, Propina 0, Paga con 30.000, los botones Justo, 20.000, 30.000 y 50.000, el Vuelto de 15.000, Otro pago, Comprobante con Facturar esta cuenta, y abajo Cobrar $ 15.000 en Efectivo." loading="lazy" width="880" height="900">
  <ol class="marks">
    <li><b>Todo</b>, <b>Por ítems</b> o <b>Partes iguales</b>: cómo se divide la cuenta.</li>
    <li><b>Aplicar un descuento</b>: a toda la cuenta, antes del primer pago.</li>
    <li><b>Medio de pago</b>: un botón por medio. Efectivo viene elegido si la cuenta lo acepta.</li>
    <li><b>Monto</b> y <b>Propina</b>.</li>
    <li><b>Paga con</b>, los billetes probables y el <b>Vuelto</b>.</li>
    <li>El botón dice cuánto se cobra y cómo.</li>
  </ol>
  <figcaption>Cobrar 15.000 en efectivo con un billete de 30.000.</figcaption>
</figure>

### Cobrar todo junto

1. Tocá **Cobrar $ …**. El diálogo abre en **Todo**, con el saldo en **Monto**.
2. Elegí el **Medio de pago**.
3. Si deja propina, escribila en **Propina**. Abajo aparece cuánto hay que pasar con la propina incluida.
4. En efectivo, tocá con cuánto paga: **Justo** o uno de los billetes que propone Fornu. El **Vuelto** aparece grande.
5. Tocá **Cobrar $ 15.000 en Efectivo** o apretá <kbd>Ctrl</kbd> + <kbd>Enter</kbd>.
{: .steps}

La mesa se cierra y Fornu avisa «Mesa cerrada.». El efectivo entra en la caja, con la propina registrada aparte.

Los billetes que propone son el total redondeado para arriba a 1.000, 10.000, 20.000, 50.000 o 100.000, los tres más chicos. Si lo que te da no alcanza, Fornu avisa «Es menos que $ 15.000.».

### Pagar con más de un medio

**Otro pago** suma una fila con lo que falta. Si no falta nada, parte la última fila en dos. Cada fila tiene su medio, su monto, su propina y una ✕ para sacarla, y su monto vuelve a la fila de arriba. Una línea avisa «Los pagos cubren la cuenta.», «Faltan $ 2.000.» o «Sobran $ 500.», y el botón pasa a decir **Cobrar 2 pagos**.

### Por ítems: cada uno paga lo suyo

1. Tocá **Por ítems**.
2. En **Qué paga esta persona**, tildá lo suyo. En las líneas de varias unidades elegí cuántas («1 de 2»).
3. Si se cobra cubierto, sumá sus **Cubiertos**.
4. Elegí el medio y la propina, y tocá **Cobrar**.
{: .steps}

El diálogo queda abierto para el siguiente, con el mismo medio de pago, y lo cobrado pasa a **Ya pagado** con su número de pago. A la derecha, **Este pago** muestra los ítems, el cubierto, el descuento en proporción si hay, y lo que paga. Cuando ese pago cierra la cuenta, dice **Lo que queda**. Si el monto pasa lo que falta, Fornu pide cobrarlo en **Todo**.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-por-items.jpg' | relative_url }}" alt="Cobrar Mesa 1 en Por ítems: tildadas 1 de 2 papas fritas, una gaseosa sin tildar, Cubiertos 1 de 3. A la derecha Este pago, 1 ítem 4.500, Cubierto × 1 500, Paga 5.000, Débito elegido y el aviso Después de este pago quedan $ 7.500: la mesa sigue abierta." loading="lazy" width="880" height="570">
  <ol class="marks">
    <li><b>Qué paga esta persona</b>: lo suyo, con cuántas unidades.</li>
    <li><b>Cubiertos</b>: los de esta persona.</li>
    <li><b>Este pago</b>: el detalle y cuánto paga.</li>
    <li>Cuánto queda después, y que la mesa sigue abierta.</li>
  </ol>
  <figcaption>Uno paga sus papas y su cubierto con débito.</figcaption>
</figure>

### Partes iguales

1. Tocá **Partes iguales**.
2. En **Entre**, poné en cuántas partes. Viene con la cantidad de comensales, o con lo que se eligió en un pago anterior.
3. Cobrá «Parte 1 de 3», después la 2, y así.
{: .steps}

Cada parte es lo que falta dividido las partes que quedan. La última se lleva los centavos que sobran. No se puede bajar de las partes ya pagadas más una, y la ayuda dice «Ya pagaron 1 de 2.». Se puede combinar: uno paga lo suyo por ítems y el resto se divide en partes iguales.

Mientras falta cobrar, la mesa dice **Pagando** en el salón y su baldosa muestra lo que queda.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-partes.jpg' | relative_url }}" alt="Cobrar Mesa 1 · saldo 7.500 en Partes iguales: a la izquierda lo consumido y un pago anterior de 5.000 en débito por 1 ítem y 1 cubierto. A la derecha Entre 2, La mesa tiene 3 comensales, Parte 1 de 2 por 3.750. En el salón, la mesa 1 dice Pagando." loading="lazy" width="1440" height="480">
  <ol class="marks">
    <li>En el salón, la mesa paga en partes.</li>
    <li><b>Partes iguales</b>.</li>
    <li><b>Entre</b>: en cuántas partes.</li>
    <li>La parte que se cobra ahora.</li>
    <li>El pago anterior, hecho por ítems.</li>
  </ol>
  <figcaption>Después de un pago por ítems, el resto entre dos.</figcaption>
</figure>

### Descuento a toda la cuenta {#descuento-cuenta}

<p class="perm"><span>Quién puede:</span> <span class="tag">Descontar e invitar</span></p>

**Aplicar un descuento** aparece antes del primer pago, solo para quien puede descontar. Muestra los motivos con su porcentaje: tocar uno con porcentaje lo aplica enseguida («Descuento aplicado.»). También se puede escribir el **Porcentaje** y tocar **Aplicar el descuento**, o **Invitar la cuenta** al 100%. **Sacar el descuento** lo quita. Si dejaste un cambio sin aplicar, Fornu avisa «Aplicá el descuento antes de cobrar.».

Si la cuenta queda en cero, el diálogo dice «No hay nada que cobrar» y el botón pasa a **Cerrar sin cargo**.

### Facturar al cobrar

Con el módulo Facturación, el pago que cierra la mesa tiene la sección **Comprobante** con **Facturar esta cuenta**. Al tildarla aparecen:

- **Condición frente al IVA**: Consumidor final, Responsable inscripto, Monotributista o Exento.
- **Documento**: Sin identificar, DNI o CUIT. Cualquier condición que no sea consumidor final pide CUIT.
- **CUIT** o **DNI**. Desde el séptimo número, Fornu muestra debajo a quién ya se le facturó con ese número, y un toque completa todo.
- **Razón social** o **Nombre**, **Domicilio**, **Teléfono** y **Email**, para mandarle el comprobante.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-facturar.jpg' | relative_url }}" alt="La sección Comprobante del cobro: Facturar esta cuenta tildado, Condición frente al IVA en Responsable inscripto y Documento fijo en CUIT. Debajo del CUIT escrito, una empresa a la que ya se le facturó con ese número, con su condición, su domicilio y la última vez. Más abajo Razón social, Domicilio, Teléfono y Email, y el aviso La facturación está apagada en esta cuenta: prendela en Facturación para emitir el comprobante." loading="lazy" width="485" height="736">
  <ol class="marks">
    <li><b>Facturar esta cuenta</b>.</li>
    <li><b>Condición frente al IVA</b> y <b>Documento</b>: un Responsable inscripto pide CUIT.</li>
    <li>El <b>CUIT</b>.</li>
    <li>A quién ya se le facturó con ese número: un toque completa los datos.</li>
    <li>Con la facturación apagada en la cuenta, Fornu avisa, y la mesa se cierra igual.</li>
  </ol>
  <figcaption>Facturar a un Responsable inscripto al cobrar.</figcaption>
</figure>

Abajo dice qué va a salir, por ejemplo «Saldrá una Factura B por $ 15.000 a consumidor final. ARCA la autoriza en unos segundos.», y el botón suma «y facturar». Al cobrar, Fornu avisa «Mesa cerrada. El comprobante se emite en unos segundos.».

Si la facturación está apagada en la cuenta o ARCA no está conectada, la mesa se cierra igual y el pedido de factura queda guardado para emitirlo después. Un Responsable inscripto sin CUIT no se puede facturar. Todo lo demás está en [Facturación electrónica]({{ '/es/projects/fornu/manual/facturacion/' | relative_url }}).

### Con la caja cerrada

Si la caja está cerrada y el pago es en efectivo, Fornu pregunta antes de cobrar:

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-caja-cerrada.jpg' | relative_url }}" alt="El aviso La caja está cerrada: Este efectivo no entra en ningún arqueo hasta que se abra la caja, en Balances → Arqueo. ¿Cobrar igual?, con los botones Volver y Cobrar igual." loading="lazy" width="480" height="224">
  <figcaption>Cobrar en efectivo con la caja cerrada.</figcaption>
</figure>

**Cobrar igual** cobra, pero ese efectivo no entra en ningún arqueo hasta que se abra la caja. Cómo se abre está en [Caja y ventas]({{ '/es/projects/fornu/manual/caja/' | relative_url }}#arqueo).

### Anular un pago {#anular-pago}

<p class="perm"><span>Quién puede:</span> <span class="tag">Cobrar mesas</span> <span class="tag">Deshacer cobros</span></p>

Los pagos se ven en la cuenta, por ejemplo «Débito · parte 1 de 2 · 12:38 · Administración», con su monto y su propina. Mientras la mesa sigue abierta:

1. Tocá la ✕ del pago (**Anular este pago**).
2. Confirmá en **Anular el pago**: «Efectivo por $ 15.000 vuelve al saldo de la mesa.».
3. Sin el permiso Deshacer cobros, Fornu pide el PIN de alguien que lo tenga.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-anular-pago.jpg' | relative_url }}" alt="La confirmación Anular el pago: Débito por $ 15.100 vuelve al saldo de la mesa, con Volver y Anular el pago" loading="lazy" width="500" height="200">
  <figcaption>Un pago en débito que vuelve al saldo.</figcaption>
</figure>

Fornu avisa «Pago anulado.» y, si era efectivo, sale de la caja.

### La mesa cobrada

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-cobrada.jpg' | relative_url }}" alt="La cuenta cobrada de la mesa 1: el estado Cobrada, la Ronda 1, el total de 12.500, tres pagos en débito (1 ítem y 1 cubierto, parte 1 de 2, parte 2 de 2), Cobrada a las 12:38 por Administración y el botón Volver a Mesas." loading="lazy" width="510" height="560">
  <ol class="marks">
    <li><b>Cobrada</b>.</li>
    <li>Cada pago, con qué se pagó, qué parte, a qué hora y quién cobró.</li>
    <li><b>Volver a Mesas</b>.</li>
  </ol>
  <figcaption>Una mesa cobrada en tres pagos.</figcaption>
</figure>

La cuenta cerrada dice cuándo y quién cobró, y la propina si hubo. **Más acciones** (⋯) sigue sirviendo para reimprimir las rondas y para **Imprimir la cuenta**. Con Facturación, aparece el comprobante con su estado (Autorizada, Esperando a ARCA, Pedida, Rechazada o Anulada) o, si todavía no tiene, el botón **Facturar**.

Si mientras cobrabas otro equipo cambió la cuenta, Fornu no cobra y avisa, por ejemplo, «La cuenta cambió: eso ahora es $ 12.500. Volvé a elegir.».

## Mostrador {#mostrador}

Para llevar o para comer en la barra. Cada venta se abre con un nombre para llamar al cliente y queda abierta hasta que se cobra, como una mesa sin silla.

<p class="perm"><span>Quién puede:</span> <span class="tag">Atender mesas</span> <span class="tag">Cobrar mesas</span></p>

1. En la pestaña **Mostrador**, tocá **Nueva venta**.
2. Si hay más de una unidad de negocio, elegí la unidad.
3. Escribí el **Nombre para llamarlo**, por ejemplo «Juan». Con Asignar quién atiende, elegí también quién atiende.
4. Tocá **Abrir**. La venta se abre al lado, lista para cargar.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-nueva-venta.jpg' | relative_url }}" alt="El diálogo Mostrador o para llevar con las unidades Doble Smash y Pizzería, el nombre Lucas y Atiende con Tomás Romero y Valentina Sosa, sin elegir" loading="lazy" width="620" height="330">
  <figcaption>Una venta nueva para Lucas. Sin elegir quién atiende, queda a tu nombre.</figcaption>
</figure>

Se carga igual que una mesa. Las diferencias:

- No hay comensales ni cubierto.
- No se mueve la venta entera ni se une con otra.
- **Mandar a la cocina** manda todo junto, sin tiempos.
- Quien cobra tiene además **Mandar y cobrar $ …**, que manda la ronda y abre el cobro de un toque. Un mozo sin Cobrar mesas ve solo **Mandar a la cocina** y **Pidió la cuenta**.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-mostrador.jpg' | relative_url }}" alt="La pestaña Mostrador con dos ventas abiertas, Camila y Lucas, el botón Nueva venta y al lado la cuenta de Lucas con la carta" loading="lazy" width="1440" height="650">
  <ol class="marks">
    <li><b>Nueva venta</b>: se abre con un nombre.</li>
    <li>La venta abierta: nombre, minutos, total y quién la atiende. La de Lucas tiene algo sin mandar.</li>
    <li>Su cuenta, al lado, como la de una mesa.</li>
  </ol>
  <figcaption>Dos ventas abiertas en el mostrador.</figcaption>
</figure>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-mandar-y-cobrar.jpg' | relative_url }}" alt="La cuenta de una venta de mostrador con un Doble cheddar sin mandar, el total de 9.800 y los botones Mandar a la cocina · 1 y Mandar y cobrar $ 9.800." loading="lazy" width="510" height="300">
  <ol class="marks">
    <li>Lo cargado, sin mandar.</li>
    <li><b>Mandar a la cocina</b>: si paga después.</li>
    <li><b>Mandar y cobrar</b>: manda y abre el cobro.</li>
  </ol>
  <figcaption>Mandar y cobrar en un toque.</figcaption>
</figure>

Si no hay nada abierto, la pestaña dice «Nada abierto en el mostrador. Una venta para llevar o para comer en la barra se abre con un nombre para llamar al cliente.».

## Mostrador express {#express}

Para la caja rápida: se carga, se manda a la cocina y se cobra de una vez. No queda nada abierto.

<p class="perm"><span>Quién puede:</span> <span class="tag">Cobrar mesas</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-express.jpg' | relative_url }}" alt="El Mostrador express: a la izquierda el buscador, las baldosas Todo, Burgers 2 y Para acompañar 2, y los productos con su color, la Gaseosa en lata con el código A7. A la derecha el Ticket con una gaseosa, el total de 2.000, los medios de pago con Efectivo elegido, Paga con y los billetes Justo, 10.000, 20.000 y 50.000, Nombre para llamarlo y el botón Cobrar $ 2.000 en Efectivo." loading="lazy" width="1440" height="710">
  <ol class="marks">
    <li><b>Buscar producto…</b>: también por código y <kbd>Enter</kbd>.</li>
    <li><b>Todo</b> y una baldosa por categoría, con su color y cuántos productos tiene.</li>
    <li>El código del producto, para cargarlo sin buscar.</li>
    <li><b>Ticket</b>: cada producto con − y +.</li>
    <li><b>Medio de pago</b> y, en efectivo, <b>Paga con</b> con los billetes probables.</li>
    <li>El botón cobra, manda a la cocina y deja todo listo para la próxima venta.</li>
  </ol>
  <figcaption>Una gaseosa cargada con su código.</figcaption>
</figure>

1. Cargá: tocá los productos, filtrá por categoría, o escribí el código y <kbd>Enter</kbd>.
2. Ajustá las cantidades con − y + en el **Ticket**.
3. Si es un cliente conocido, elegilo en **Cliente (opcional)**: su descuento se aplica solo, por ejemplo «Descuento de Dueños: 100% · Invita la casa.».
4. Elegí el **Medio de pago** y, en efectivo, con cuánto paga.
5. Si querés, poné un **Nombre para llamarlo (opcional)**. Si no, la venta sale como «Mostrador».
6. Tocá **Cobrar $ … en …**, o **Cerrar sin cargo** si el cliente trae el 100%.
{: .steps}

Fornu avisa «Cobrado $ 19.600 con Efectivo.», la ronda llega al tablero de la cocina con su nombre, y al lado queda la venta cobrada con **Nueva venta** para seguir. El color de cada categoría se elige en Carta › Categorías.

- El express no tiene propina ni pregunta por factura. Con Facturación, se factura después desde la venta cobrada, con **Facturar**.
- Si cambiás de unidad de negocio con algo cargado, Fornu pregunta «¿Vaciar el ticket y pasar a…?», porque una venta es de una sola unidad.
- Si un precio cambió desde que se abrió la carta, no cobra: «Los precios cambiaron…». La carta ya se actualizó: revisá el ticket y cobrá de nuevo.
- En el teléfono, el ticket queda debajo de la carta y abajo hay una barra con «2 ítems · $ 19.600 · Efectivo» y **Cobrar**.

## Salón › Cuentas del día {#cuentas}

Para la caja y el encargado: qué está abierto ahora y cuánto falta cobrar, y debajo lo que ya se cobró o se canceló, con quién atendió y cuántos comieron. En la barra dice **Cuentas** y el título de la página es **Cuentas del día**.

<p class="perm"><span>Quién puede:</span> <span class="tag">Cobrar mesas</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-cuentas.jpg' | relative_url }}" alt="Cuentas del día: Abiertas ahora · 2 con la Mesa V1 y la Mesa 3, su mozo, hora, total y saldo. Debajo Cobradas y canceladas con el período Hoy, el buscador, Exportar, los filtros y las tarjetas Pedidos vendidos, Ventas, Ticket promedio, Cancelados y Comensales, 2 a 12.850 por comensal." loading="lazy" width="1440" height="790">
  <ol class="marks">
    <li><b>Abiertas ahora</b>: cada cuenta con quién atiende, desde cuándo, el total y el saldo. Tocá una para abrirla.</li>
    <li>El período y el buscador («Cliente, número o código…»).</li>
    <li><b>Exportar</b>: la lista, para una planilla.</li>
    <li>Los filtros: unidad, medio de pago, quién atendió, sector, mesa, arqueo, comprobante, turno y horario.</li>
    <li><b>Comensales</b>: cuántos comieron y el promedio por comensal.</li>
  </ol>
  <figcaption>Las cuentas del día en la demo.</figcaption>
</figure>

**Abiertas ahora** incluye las ventas del mostrador y las mesas de días anteriores que siguen abiertas. Si no hay ninguna, dice «No hay mesas abiertas.». Una cuenta abierta desde acá vuelve a esta lista con la flecha **Cuentas**.

**Cobradas y canceladas** es la lista de ventas del salón, ya filtrada a las cerradas. Medio de pago tiene la opción «Todo menos efectivo», y **Desde las** y **Hasta las** se aplican a las abiertas o a las cerradas. Tocá una venta para verla al lado, y recorré la lista con <kbd>↑</kbd> <kbd>↓</kbd>. **Más info** despliega más números. En el teléfono los filtros quedan detrás de **Filtros**. Con Facturación hay una columna **Comprobante** y una acción para facturar de una vez las que quedaron sin factura, por ejemplo **Facturar 3 sin facturar**. La lista completa de ventas se explica en [Caja y ventas]({{ '/es/projects/fornu/manual/caja/' | relative_url }}).

## Salón › Sectores y mesas {#armar}

Acá se arma el salón: los sectores (Salón, Patio, Vereda), sus mesas con sus sillas, el precio del cubierto y dónde va cada mesa en el plano. En la barra dice **Mesas y sectores** y el título de la página es **Sectores y mesas**. Lo hace el dueño o el encargado, y este permiso nunca se presta con un PIN.

<p class="perm"><span>Quién puede:</span> <span class="tag">Armar el salón</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-sectores.jpg' | relative_url }}" alt="Sectores y mesas: arriba Cubierto por comensal con su botón Guardar y Nuevo sector. Las pestañas Salón y Vereda con las flechas, Editar sector y + Mesas. El editor del plano con Elegir y mover, nueve mesas ubicadas y a la derecha el catálogo Mesas." loading="lazy" width="1440" height="790">
  <ol class="marks">
    <li><b>Cubierto por comensal</b> y <b>Guardar</b>.</li>
    <li><b>Nuevo sector</b>.</li>
    <li>Un sector por pestaña.</li>
    <li>Las flechas cambian el orden del sector. <b>Editar sector</b> y <b>+ Mesas</b>.</li>
    <li><b>Elegir y mover</b>: con el Salón solo, el plano sirve para acomodar mesas.</li>
    <li>El catálogo: las mesas sin ubicar y los modelos de mesa.</li>
  </ol>
  <figcaption>El salón de la demo, armado.</figcaption>
</figure>

### El cubierto

1. Escribí el precio en **Cubierto por comensal**.
2. Tocá **Guardar**. Fornu avisa «Cubierto guardado.».
{: .steps}

Se suma por cada comensal de una mesa, nunca en el mostrador. En 0, no se cobra cubierto.

### Sectores

Al abrir la cuenta ya hay un sector llamado «Salón». **Nuevo sector** pide el **Nombre** («Salón, Patio, Vereda»). **Editar sector** cambia el nombre y tiene **Activo: sus mesas se ven en el salón**, para sacar un sector de la vista sin perderlo: su pestaña dice «Desactivado». Las flechas ← y → lo corren de lugar («Orden guardado.»).

### Crear mesas de a muchas

1. Elegí el sector y tocá **+ Mesas**.
2. **Desde el número**: Fornu propone el que sigue al más alto.
3. **Cuántas** (de 1 a 60, 10 de entrada) y **Sillas de cada una** (4 de entrada).
4. Si querés, una **Letra antes del número (opcional)**: «P» da P1, P2… para el patio.
5. Tocá **Crear de P1 a P10** (o **Crear la mesa P1** si es una).
{: .steps}

Fornu avisa «10 mesas creadas.». Si ya existe una con ese nombre: «Ya hay una mesa P1.».

### Cambiar una mesa

Elegí la mesa en el plano y tocá **Editar la mesa** en el panel de la derecha. El diálogo tiene **Número o nombre** (hasta 20 letras), **Sillas** (de 1 a 40), **Sector** (para pasarla a otro) y **Activa: se ve en el salón**. Fornu avisa «Mesa guardada.».

Una mesa que ya no se usa se desactiva, y las cuentas que se sirvieron en ella la conservan. En el teléfono no hay plano: las mesas se ven como una lista de botones, y el aviso dice «El plano se arma desde una computadora o una tablet.».

### Ubicar las mesas en el plano

Cada sector tiene su plano. Con el Salón solo, el plano es un croquis visto desde arriba donde se acomodan las mesas: no hace falta dibujar paredes.

1. Las mesas que todavía no están en el plano esperan en **Sin ubicar**, a la derecha, cada una con sus lugares.
2. Arrastrá una al plano. En una pantalla táctil, tocala y después tocá el lugar.
3. Para moverla, arrastrala. Con <kbd>R</kbd> se gira.
4. Tocá **Guardar el plano**. Fornu avisa «Plano guardado.».
{: .steps}

Cada mesa se dibuja con un modelo según sus sillas: hasta 2, Mesa de 2. Hasta 4, Mesa de 4. Hasta 6, Mesa de 6. Hasta 8, Mesa larga. Más, Redonda de 10. Una mesa arrastrada desde el catálogo **Mesas** (Mesa de 2, de 4, de 6, Mesa larga, Redonda de 4, de 6 y de 10, Mesa alta) es una mesa nueva: dice «Nueva» hasta que guardás, y entonces toma el número que sigue.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-ubicar.jpg' | relative_url }}" alt="El editor del plano con la mesa 1 elegida y su barra encima (girar a la izquierda, girar a la derecha, duplicar, menos 4 sillas más, sacar), una mesa redonda que dice Nueva, y a la derecha el panel Editar con Mesa de 4 · 1, Modelo, el giro en 0°, Sillas 4, Le entran hasta 4, 80 cm × 80 cm y Sacar del plano." loading="lazy" width="1340" height="790">
  <ol class="marks">
    <li>La barra de la mesa elegida: girar, duplicar, sillas y sacar del plano. Debajo, la manija para girarla a mano.</li>
    <li>Una mesa nueva, traída del catálogo.</li>
    <li><b>Editar</b>: el modelo, el giro, las sillas («Le entran hasta 4.») y <b>Sacar del plano</b>.</li>
  </ol>
  <figcaption>Acomodar las mesas del salón.</figcaption>
</figure>

**Sacar del plano** devuelve la mesa a **Sin ubicar**: la mesa sigue existiendo. Sin nada elegido, el panel muestra **El espacio**, con el **Ancho (m)** y el **Fondo (m)** del sector. Fornu no deja guardar si algo está mal, y dice qué: «Mesa 1 y Mesa 2 se pisan.», «Mesa 9: queda fuera del espacio.» o «Mesa 4: le entran hasta 4 sillas.». Si cambiás de sector sin guardar, pregunta antes de descartar.

Con el módulo Constructor de espacios, el mismo editor dibuja paredes, pisos, puertas y objetos: está en [Espacios: el plano del local]({{ '/es/projects/fornu/manual/espacios/' | relative_url }}).

## Las rondas en la cocina {#cocina}

Cada ronda que sale del salón es una tarjeta en **En preparación**, en el [tablero de la cocina]({{ '/es/projects/fornu/manual/pedidos/' | relative_url }}#tablero), y suena igual que un pedido nuevo. Las ventas del mostrador y del express también llegan como rondas, con su nombre.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/salon-tablero.jpg' | relative_url }}" alt="El tablero de pedidos: en En preparación la tarjeta Mesa 2 · Ronda 1 con Atiende Administración, una papa frita y el botón Lista. En Listo para entregar la tarjeta Mesa 1 · Ronda 1 con Lista a la hora, dos papas fritas con la nota Bien cocidas y el botón Se llevó a la mesa." loading="lazy" width="1024" height="580">
  <ol class="marks">
    <li>Una ronda en preparación: la mesa, el número de ronda, quién atiende y lo que lleva. <b>Lista</b> la pasa a la otra columna.</li>
    <li>Una ronda lista, esperando que el mozo la lleve.</li>
  </ol>
  <figcaption>Las rondas del salón en el tablero.</figcaption>
</figure>

La tarjeta muestra la mesa en grande, «Ronda 1», los minutos desde que salió (cambian de color pasados los 20), quién atiende, cada línea con su estación y, en **Después**, lo que espera para más tarde, por ejemplo «Principal: 2 × Bife · Postre: 1 × Flan». Al tocar **Lista**, la mesa se pone naranja en el salón. **Se llevó a la mesa** en la cocina y **La llevé** del mozo hacen lo mismo: sacan la tarjeta del tablero.

Cada ronda imprime una comanda por estación, con la mesa en grande, «RONDA 1», el mozo y los comensales, la hora y las líneas con sus notas. Las copias dicen REIMPRESIÓN y los avisos de anulación dicen ANULADO, con el motivo y quién anuló. Qué estación prepara cada categoría se elige en [Estaciones de cocina]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#estaciones).
