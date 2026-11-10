---
layout: manual
manual: espacios
title: "Espacios: el plano del local · Manual de Fornu"
description: "El Constructor de espacios: cómo se dibuja el salón con paredes, pisos, aberturas y objetos, cómo se ve en Basic, Cenital e Isométrica, los lugares, objetos y texturas propios, calcar, imprimir y exportar, y cómo lo usan los mozos."
permalink: /es/projects/fornu/manual/espacios/
---

## Para qué sirve {#para-que}

Con el Salón, cada sector tiene un plano donde se acomodan las mesas. El Constructor de espacios convierte ese croquis en el local de verdad: paredes, pisos, puertas y ventanas, columnas, barras, plantas, sombrillas y lo que haga falta, con sus materiales, visto desde arriba o en isométrica. Se arma como un juego de construcción, y los mozos después atienden sobre ese mismo plano.

El Constructor de espacios es un módulo que se suma al Salón. Si tu cuenta no lo tiene, el plano de cada sector funciona como se explica en [Sectores y mesas]({{ '/es/projects/fornu/manual/salon/' | relative_url }}#armar), y la barra no muestra el grupo **Espacios**.

| Dónde | Para qué | Quién puede |
|---|---|---|
| **Salón › Sectores y mesas** | Dibujar el plano de cada sector y ubicar sus mesas. | Armar el salón |
| **Espacios › Lugares** | Los lugares guardados, para armar otros planos sobre ellos. | Biblioteca |
| **Espacios › Objetos propios** | Objetos armados con piezas, que se suman al catálogo. | Biblioteca |
| **Espacios › Texturas propias** | Fotos de pisos, paredes o logos, que se suman a los materiales. | Biblioteca |

El permiso **Biblioteca** («Guarda lugares, objetos y texturas propios, y arma espacios a partir de ellos.») nunca se presta con un PIN. Administración puede todo.

## Con el Salón solo y con el constructor {#dos-planos}

El mismo editor cambia según lo que tenga la cuenta:

| | Con el Salón solo | Con el Constructor de espacios |
|---|---|---|
| Un sector nuevo empieza como | un piso de 10 × 8 m | una grilla vacía de 20 × 15 m: nada viene hecho |
| Herramientas | **Elegir y mover**, deshacer, rehacer y **Grilla** | todas: habitaciones, paredes, piso, pintura, cuentagotas y mazo |
| Catálogo | las mesas sin ubicar y los modelos de mesa | también puertas, ventanas, asientos, estructura, servicio, deco, exterior, eventos y objetos propios |
| Vistas | **Basic**, un croquis desde arriba | **Basic**, **Cenital** e **Isométrica**, con texturas |
| Medidas | el ancho y el fondo del sector | además los m² de cada habitación y el largo de cada pared |
| Extras | | **Lugares**, **Calcar un plano**, **Imagen**, **Imprimir** y **Vaciar el plano** |

Con el Salón solo, tocar algo que no es una mesa avisa «Acá solo se acomodan las mesas.».

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-croquis.jpg' | relative_url }}" alt="El plano de un sector con el Salón solo: un piso liso con nueve mesas ubicadas, a la derecha El espacio con Ancho 10 y Fondo 8 y la ayuda Arrastrá al plano una mesa del catálogo, y abajo el tamaño 10,00 m × 8,00 m y los botones Descartar y Guardar el plano." loading="lazy" width="1340" height="710">
  <ol class="marks">
    <li><b>El espacio</b>: el <b>Ancho (m)</b> y el <b>Fondo (m)</b> del sector, cuando no hay nada elegido.</li>
    <li>La ayuda del editor.</li>
    <li>El tamaño del plano. Si algo está mal, acá aparece el primer error.</li>
    <li><b>Descartar</b> y <b>Guardar el plano</b>.</li>
  </ol>
  <figcaption>Con el Salón solo, el plano es un croquis para acomodar mesas.</figcaption>
</figure>

Si un día la cuenta deja de tener el constructor, los planos conservan sus paredes y sus pisos, pero solo se pueden acomodar mesas y la vista vuelve a Basic.

## El editor {#editor}

Se abre en Salón › Sectores y mesas, debajo de las pestañas de los sectores, y también en Espacios › Lugares. Se usa desde una computadora o una tablet: en el teléfono, Sectores y mesas muestra las mesas como una lista y avisa «El plano se arma desde una computadora o una tablet.».

<p class="perm"><span>Quién puede:</span> <span class="tag">Armar el salón</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-editor.jpg' | relative_url }}" alt="El editor con el constructor: arriba las herramientas Elegir y mover, Habitación, Pared, Piso, Pintura, Cuentagotas y Mazo, deshacer, rehacer y Grilla. Debajo Lugares, Calcar un plano, Imagen e Imprimir. En el plano la vista Basic, una habitación en L de 18,1 m², otra cerrada de 74,4 m² con una puerta elegida en su pared y una mesa nueva. A la derecha el catálogo con Puertas y ventanas y Mesas." loading="lazy" width="1340" height="790">
  <ol class="marks">
    <li>Las herramientas: <b>Elegir y mover</b>, <b>Habitación</b>, <b>Pared</b>, <b>Piso</b>, <b>Pintura</b>, <b>Cuentagotas</b> y <b>Mazo</b>.</li>
    <li>Deshacer, rehacer y <b>Grilla</b> (cada celda mide 25 cm).</li>
    <li><b>Lugares</b>, <b>Calcar un plano</b>, <b>Imagen</b> e <b>Imprimir</b>.</li>
    <li>La vista: <b>Basic</b>, <b>Cenital</b> o <b>Isométrica</b>.</li>
    <li>Una puerta elegida, con su barra: dar vuelta hacia dónde abre, y sacarla.</li>
    <li><b>Agregar</b> (el catálogo) y <b>Editar</b> (lo elegido).</li>
  </ol>
  <figcaption>El editor completo, con dos habitaciones y una puerta.</figcaption>
</figure>

En una esquina del plano están **Acercar**, **Alejar** y **Ver todo**. Debajo, una línea muestra el nombre de la herramienta o lo que pasa mientras dibujás: un largo («3,50 m»), una superficie («12,5 m²») o por qué algo no entra. A la derecha, **Agregar** muestra el catálogo y **Editar** lo que elegiste: al elegir algo a mano pasa a Editar, y al ubicar algo del catálogo se queda en Agregar para seguir. Abajo, el tamaño del plano («20,00 m × 15,00 m»), **Descartar** y **Guardar el plano**, que avisa «Plano guardado.».

### Las vistas {#vistas}

| Vista | Cómo se ve |
|---|---|
| **Basic** | Un croquis plano, desde arriba. Es la única vista con el Salón solo. |
| **Cenital** | Desde arriba, con los materiales y las texturas. |
| **Isométrica** | En tres dimensiones, en diagonal. |

Fuera de Basic aparece **Texturas**, para ver los materiales con su dibujo o en colores lisos. La isométrica suma cómo se ven las paredes, **Paredes altas**, **Paredes recortadas** (la de entrada) o **Paredes bajas**, y los botones ↺ ↻ que giran la vista de a un cuarto de vuelta. La elección queda guardada en ese equipo y vale para todos los planos, también para el salón en vivo.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-vistas.jpg' | relative_url }}" alt="Un salón en vista Isométrica, con Texturas tildado y Paredes recortadas: paredes de ladrillo, piso claro, tres mesas de cuatro con sus sillas, una barra oscura y el cartel 193,8 m² en el piso." loading="lazy" width="1040" height="680">
  <ol class="marks">
    <li><b>Basic</b>, <b>Cenital</b> o <b>Isométrica</b>.</li>
    <li><b>Texturas</b>: los materiales con su dibujo.</li>
    <li>Cómo se ven las paredes: altas, recortadas o bajas.</li>
    <li>↺ ↻: girar la vista.</li>
    <li>La superficie de la habitación.</li>
  </ol>
  <figcaption>El salón de la demo en isométrica.</figcaption>
</figure>

### Las herramientas {#herramientas}

| Herramienta | Qué hace |
|---|---|
| **Elegir y mover** | Tocá algo para elegirlo, con <kbd>Mayús</kbd> sumás o sacás de la selección. Arrastrá para moverlo: se ajusta a la grilla, y con <kbd>Alt</kbd> se mueve libre. Si no entra donde lo soltás, no se mueve y la línea de abajo dice por qué. Las puertas se deslizan por su pared. |
| **Habitación** | Pinta una habitación entera: piso y paredes a la vez. Pintar sobre otra las une (dos rectángulos hacen una L) y las paredes siguen el borde solas. Con Borrar o <kbd>Alt</kbd>, la recorta. |
| **Pared** | Levanta paredes. En línea, también en diagonal a 45°. De a un tramo, un toque levanta el tramo más cercano y un trazo dobla en ángulo recto. En rectángulo, arrastrá en diagonal. Con Borrar o <kbd>Alt</kbd>, las saca. |
| **Piso** | Pone baldosas: de a una, media baldosa, en línea, en rectángulo o rellenando. Con <kbd>Mayús</kbd> y un toque rellena la habitación. Con <kbd>Alt</kbd>, saca. |
| **Pintura** | Tocá una pared o un objeto para ponerle el material elegido. Con <kbd>Mayús</kbd> pinta todas las paredes unidas, o todas las partes del objeto. |
| **Cuentagotas** | Tocá una pared, un objeto o el piso para tomar su material (y el alto de la pared). Después vuelve a la herramienta de antes. |
| **Mazo** | Tocá cualquier cosa para sacarla. Arrastrando sobre una pared, saca solo ese tramo. |

Mientras arrastrás un rectángulo con Habitación podés escribir la medida, por ejemplo «4 x 3,5», y apretar <kbd>Enter</kbd>. Si está mal escrita, Fornu avisa «Escribí ancho x fondo en metros, como 4 x 3,5.». Con Pared en línea, escribí el largo («3,5») y <kbd>Enter</kbd>.

### Los pinceles

Con Habitación, Pared, Piso, Pintura o Cuentagotas aparece una segunda barra con la forma de pintar y los materiales:

- **La forma.** Piso: **De a una baldosa**, **Media baldosa**, **Línea**, **Rectángulo** y **Rellenar**. Pared: **Línea**, **De a un tramo** y **Rectángulo**. Habitación: **Rectángulo**, **De a una celda** y **Línea**. Cada herramienta recuerda la suya.
- **Media baldosa** suma ↺ ↻ para girar la media baldosa, también con <kbd>R</kbd> o <kbd>Mayús</kbd> + <kbd>R</kbd>.
- **Borrar**: «Saca en vez de poner, con la misma forma (o mantené Alt)».
- **Material**: pisos para Piso y Habitación, paredes y objetos para Pintura, todo para Cuentagotas.
- **Paredes**, con Habitación y Pared: el material de las paredes y su alto, **Completa · 2,60 m**, **Media · 2,20 m** o **Baja · 1,10 m**.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-paredes.jpg' | relative_url }}" alt="La barra de la herramienta Pared: Línea, De a un tramo elegido y Rectángulo, el botón Borrar, los materiales y el título Paredes. Debajo los materiales de pared y el alto Completa · 2,60 m. En el plano, una habitación en L de 18,1 m² y otra cerrada de 74,4 m²." loading="lazy" width="1090" height="750">
  <ol class="marks">
    <li>La forma: <b>Línea</b>, <b>De a un tramo</b> o <b>Rectángulo</b>.</li>
    <li><b>Material</b>, y a la derecha el título <b>Paredes</b> de la fila de abajo.</li>
    <li>El material de las paredes y su alto.</li>
    <li>Dos rectángulos pintados con Habitación hacen una L.</li>
    <li>Cada habitación cerrada muestra su superficie.</li>
  </ol>
  <figcaption>Levantar paredes y habitaciones.</figcaption>
</figure>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-piso.jpg' | relative_url }}" alt="La barra de la herramienta Piso: De a una baldosa, Media baldosa elegida, Línea, Rectángulo y Rellenar, los botones para girar la media baldosa, Borrar y los materiales. En el plano, un cuadrado de baldosas y tres medias baldosas en diagonal al lado." loading="lazy" width="1090" height="620">
  <ol class="marks">
    <li>Cómo se pone el piso.</li>
    <li>↺ ↻: girar la media baldosa.</li>
    <li><b>Borrar</b>: saca con la misma forma.</li>
    <li>Medias baldosas, para bordes en diagonal.</li>
    <li>Un piso puesto en rectángulo.</li>
  </ol>
  <figcaption>Poner el piso.</figcaption>
</figure>

### Armar un salón de cero

1. Sin nada elegido, poné el **Ancho (m)** y el **Fondo (m)** del lugar (de 2 a 120 m por lado).
2. Con **Habitación** en **Rectángulo**, arrastrá el salón. Mientras arrastrás, podés escribir «12 x 8» y apretar <kbd>Enter</kbd>.
3. Para una cocina o un baño, pintá otra habitación pegada: las paredes se acomodan solas.
4. En **Agregar**, arrastrá puertas y ventanas sobre las paredes.
5. Con **Piso** y **Pintura**, elegí los materiales.
6. Ubicá las mesas: las que esperan en **Sin ubicar** y las nuevas del grupo **Mesas**. Sumá la barra, la caja, las columnas y lo demás.
7. Tocá **Guardar el plano**.
{: .steps}

### El catálogo {#catalogo}

En **Agregar**, todo lo que se puede poner, dibujado como se ve desde arriba, sillas incluidas:

| Grupo | Qué trae |
|---|---|
| **Sin ubicar** | Las mesas del sector que todavía no están en el plano. |
| **Puertas y ventanas** | Puerta, Puerta doble, Ventana, Ventanal, Paso. |
| **Mesas** | Mesa de 2, Mesa de 4, Mesa de 6, Mesa larga, Redonda de 4, Redonda de 6, Redonda de 10, Mesa alta. |
| **Asientos** | Silla, Banqueta, Box, Sillón, Butaca. |
| **Estructura** | Columna redonda, Columna cuadrada, Escalera. |
| **Servicio** | Pase de cocina, Barra, Caja, Heladera exhibidora, Estación de café, Atril de recepción. |
| **Deco** | Planta, Planta alta, Cantero, Alfombra, Biombo, Cartel, Cuadro. |
| **Exterior** | Sombrilla, Estufa de exterior, Pérgola, Deck, Árbol, Banco, Valla. |
| **Eventos** | Escenario, Pista de baile, Cabina de DJ, Mesa de buffet, Mesa dulce, Living. |
| **Propios** | Los [objetos propios](#objetos) de la cuenta. |

Para ubicar algo:

- **Con el mouse o un lápiz**, arrastralo al plano. Mientras lo llevás, un borde verde o rojo dice si entra ahí, y queda donde lo soltás. Si lo soltás fuera del plano, no pasa nada.
- **Con el dedo**, tocalo: queda «en la mano». Cada toque en el plano pone uno, uno detrás de otro. Para terminar, <kbd>Esc</kbd> o tocá otra vez el objeto en el catálogo.
- **Las puertas y ventanas** van sobre una pared: arrastralas hasta una, o tocalas y después tocá la pared. Abren hacia el lado desde el que las ponés, y no van en paredes en diagonal. Si no encajan, la línea de abajo dice «Acercate a una pared.», «Las aberturas van sobre una pared.» o «La abertura tiene que quedar entera sobre la pared.».
- **Para sacar algo**, arrastralo del plano al catálogo, donde dice «Soltalo acá para sacarlo del plano».

Una mesa traída del grupo Mesas es una mesa nueva del salón: dice «Nueva» hasta que guardás, y entonces toma el número que sigue y las sillas que le pusiste (4 si no cambiaste nada).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-catalogo.jpg' | relative_url }}" alt="El editor en isométrica con un objeto propio, un barril, elegido en el plano con su barra encima. A la derecha el catálogo en los grupos Exterior, Eventos (Escenario, Pista de baile, Cabina de DJ, Mesa de buffet, Mesa dulce, Living) y Propios, con el Barril." loading="lazy" width="1340" height="790">
  <ol class="marks">
    <li><b>Agregar</b> y <b>Editar</b>.</li>
    <li>Un grupo del catálogo: <b>Eventos</b>.</li>
    <li><b>Propios</b>: un barril armado en Objetos propios.</li>
    <li>El barril en el plano, con su barra.</li>
  </ol>
  <figcaption>El catálogo, con un objeto propio.</figcaption>
</figure>

### Lo elegido: la barra, el giro y el panel Editar {#girar}

Al elegir algo aparece una barra al lado:

- **↺** y **↻**: girar a la izquierda o a la derecha (<kbd>R</kbd>).
- **Duplicar** (<kbd>Ctrl</kbd> + <kbd>D</kbd>): la copia va al lado. Si no entra, avisa «La copia no entra al lado.».
- En las mesas, **− 4 sillas +**, hasta las que le entran.
- En las puertas, **⇄**: «Dar vuelta hacia dónde abre (F)».
- **✕**: «Sacar del plano (Supr)».

Debajo del objeto hay una manija para girarlo a mano: de a 15°, con <kbd>Mayús</kbd> de a 45° y con <kbd>Alt</kbd> libre.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-girar.jpg' | relative_url }}" alt="Una mesa de seis girada en diagonal, que dice Nueva, con su barra encima (girar, girar, duplicar, menos 6 sillas más, sacar) y la manija de giro debajo." loading="lazy" width="1040" height="570">
  <ol class="marks">
    <li>La barra: girar, duplicar, sillas y sacar.</li>
    <li>La manija para girar a mano.</li>
    <li>Una mesa nueva, girada.</li>
  </ol>
  <figcaption>Girar una mesa sobre la terraza.</figcaption>
</figure>

El panel **Editar** muestra qué es lo elegido. En una mesa, «Mesa 1 · 4 sillas» y el botón **Editar la mesa** (su número, sillas y sector), el **Modelo**, el giro en grados con ↺ ↻ y **Sillas** con «Le entran hasta 6.». Los que cambian de tamaño tienen **Largo (cm)** y **Ancho (cm)**: la Mesa larga va de 120 a 600 cm. Abajo, la medida y **Sacar del plano** (en las mesas) o **Quitar** (en lo demás).

Sin nada elegido, el panel muestra **El espacio**: el **Ancho (m)** y el **Fondo (m)**, de 2 a 120 m por lado, de a 25 cm, y una ayuda: «Poné el piso baldosa por baldosa con Piso, levantá las paredes con Pared, y arrastrá lo demás del catálogo al plano.».

### Medidas

Cada habitación cerrada por paredes muestra su superficie en m², y una pared elegida muestra su largo. Mientras dibujás, la línea de abajo muestra el largo o el tamaño de lo que estás haciendo.

### Vaciar el plano

Sin nada elegido, **Vaciar el plano** borra el piso, las paredes, las puertas y lo fijo, para empezar de nuevo sobre la grilla. Pregunta antes: «Se saca el piso, las paredes, las puertas y lo fijo: queda la grilla para armarlo de nuevo. Las mesas quedan. Se puede deshacer.».

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-vaciar.jpg' | relative_url }}" alt="La confirmación Vaciar el plano: se saca el piso, las paredes, las puertas y lo fijo, queda la grilla, las mesas quedan y se puede deshacer, con Volver y Vaciar" loading="lazy" width="500" height="240">
  <figcaption>Antes de vaciar, Fornu pregunta.</figcaption>
</figure>

### Lo que no deja guardar

**Guardar el plano** no anda mientras haya un error, y el primero se lee abajo:

- «Mesa 1 y Barra se pisan.»
- «Mesa 4 atraviesa una pared.»
- «Planta tapa el paso de una puerta.»
- «Mesa 9: queda fuera del espacio.»
- «Mesa 2: le entran hasta 4 sillas.»

Si otro equipo guardó el mismo plano mientras dibujabas, Fornu avisa «Otro dispositivo guardó este plano mientras dibujabas. Descartá lo tuyo para ver el suyo.». Si salís con cambios sin guardar, pregunta antes: «El plano tiene cambios que no se guardaron.».

### Con el dedo, con el mouse y con el teclado

- **Con el dedo**: un dedo usa la herramienta, dos dedos acercan, alejan y mueven el plano. Si apoyás un segundo dedo en medio de un trazo, el trazo se cancela.
- **Con el mouse**: la rueda acerca y aleja. Para mover el plano, mantené la barra espaciadora y arrastrá, o arrastrá con el botón del medio o el derecho.
- **Con el teclado**: hacé clic en el editor primero. Las teclas no hacen nada mientras escribís en un campo.

| Tecla | Qué hace |
|---|---|
| <kbd>Ctrl</kbd> + <kbd>Z</kbd> | Deshacer |
| <kbd>Ctrl</kbd> + <kbd>Y</kbd> o <kbd>Ctrl</kbd> + <kbd>Mayús</kbd> + <kbd>Z</kbd> | Rehacer |
| <kbd>Ctrl</kbd> + <kbd>S</kbd> | Guardar el plano |
| <kbd>R</kbd> / <kbd>Mayús</kbd> + <kbd>R</kbd> | Girar 90° o 45° lo elegido o lo que tenés en la mano. Con Piso, gira la media baldosa. |
| <kbd>F</kbd> | Dar vuelta una puerta |
| <kbd>Supr</kbd> o <kbd>Retroceso</kbd> | Sacar lo elegido |
| <kbd>Ctrl</kbd> + <kbd>D</kbd> | Duplicar |
| Flechas | Mover 25 cm |
| <kbd>Alt</kbd> + flechas | Mover 1 cm |
| <kbd>Esc</kbd> | Soltar la selección, dejar de poner o cancelar un arrastre |
| Números y <kbd>Enter</kbd> mientras arrastrás | El largo o la medida exacta |

## Calcar un plano {#calcar}

Si tenés el plano del local en una foto o una imagen, ponelo debajo y dibujá encima.

1. Sin nada elegido, poné el **Ancho (m)** y el **Fondo (m)** reales del lugar. La imagen se estira sobre todo el espacio, así que las medidas tienen que coincidir.
2. Tocá **Calcar un plano** y elegí la imagen. Aparece a media transparencia, encima del piso y debajo de las paredes y lo demás.
3. Con **Calco**, hacela más clara o más oscura.
4. Dibujá encima con **Habitación** y **Pared**.
5. Cuando termines, tocá **Quitar el calco** y **Guardar el plano**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-calco.jpg' | relative_url }}" alt="Un lugar vacío de 10 por 8 metros con el plano de un local calcado encima, a media transparencia: sus paredes, la puerta y los nombres Cocina, Salón y Baño. Arriba, el control Calco y el botón Quitar el calco, y a la derecha el Ancho y el Fondo del espacio" loading="lazy" width="1440" height="780">
  <ol class="marks">
    <li><b>Ancho (m)</b> y <b>Fondo (m)</b>: las medidas reales del lugar.</li>
    <li>El plano calcado, estirado sobre todo el espacio.</li>
    <li><b>Calco</b>: más claro o más oscuro.</li>
    <li><b>Quitar el calco</b>.</li>
  </ol>
  <figcaption>Un plano de 10 × 8 m, listo para dibujar encima.</figcaption>
</figure>

El calco queda solo en esta pantalla: no se guarda con el plano.

<div class="callout tip"><p class="callout-title">Consejo</p><p>Si el plano tiene una medida escrita, una pared de 8 m por ejemplo, usala para poner el ancho y el fondo antes de calcar. Así las paredes que dibujes encima tienen el largo real.</p></div>

## Imprimir y exportar {#imprimir}

- **Imagen** descarga el plano como una imagen PNG de 2400 × 1600, tal como lo estás viendo: la misma vista, las texturas y los nombres. Fornu avisa «Imagen descargada.». Sirve para mandarlo por mensaje o pegarlo en una presentación.
- **Imprimir** imprime el plano solo, en una hoja apaisada.

La imagen sale con la vista que estás usando: una isométrica con texturas para mostrar el lugar, Basic para una hoja clara con los números de mesa.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-imagen.jpg' | relative_url }}" alt="La imagen que descarga Imagen: el salón en isométrica con seis mesas de cuatro sobre el piso" loading="lazy" width="1200" height="800">
  <figcaption>Lo que baja <b>Imagen</b>, en isométrica (achicada).</figcaption>
</figure>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-imprimir.jpg' | relative_url }}" alt="La hoja de Imprimir, apaisada: el salón visto de arriba con seis mesas y sus números" loading="lazy" width="1047" height="718">
  <figcaption>La hoja que sale con <b>Imprimir</b>.</figcaption>
</figure>

## Espacios › Lugares {#lugares}

Un lugar guarda el piso, las paredes, las aberturas y lo fijo de un espacio, para armar otros planos encima: un salón alquilado, una quinta, una carpa. Sirve para quien arma eventos en distintos lugares, o para tener el local vacío y probar disposiciones.

<p class="perm"><span>Quién puede:</span> <span class="tag">Biblioteca</span></p>

**Desde el editor**, el botón **Lugares** abre la lista de lugares guardados:

- **Usar como base** pone ese lugar debajo del plano: «El lugar del plano (piso, paredes y lo fijo) se reemplaza por este; lo acomodado queda.». Confirmá con **Usar este lugar**. Se puede deshacer, y hay que tocar **Guardar el plano** para que quede.
- **Guardar este plano como lugar**: escribí un nombre (por ejemplo «Quinta Los Álamos») y tocá **Guardar**. Fornu avisa «Lugar guardado.». Se guarda lo fijo del lugar, sin las mesas.

Si no hay ninguno, dice «Todavía no hay lugares guardados.».

**En Espacios › Lugares** están todos, uno por pestaña con su medida, y el editor completo debajo. **Nuevo lugar** crea «Lugar 1», de 10 × 8 m con piso de cemento alisado («Lugar creado.»). **Borrar el lugar** lo quita, y los espacios armados sobre él no cambian. Sin lugares, la pantalla dice «Todavía no hay lugares. Creá uno, o guardá el plano de un sector como lugar desde su editor.».

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-lugares.jpg' | relative_url }}" alt="Espacios, Lugares con un lugar nuevo de 10 por 8 metros: su pestaña, Nuevo lugar, Borrar el lugar, y el editor debajo con sus herramientas, Lugares, Calcar un plano, Imagen e Imprimir" loading="lazy" width="1440" height="838">
  <ol class="marks">
    <li>El lugar, con su medida. Hay una pestaña por lugar.</li>
    <li><b>Nuevo lugar</b>.</li>
    <li><b>Borrar el lugar</b>.</li>
    <li><b>Lugares</b>, en el editor: usar uno como base o guardar el plano como lugar.</li>
  </ol>
  <figcaption>Un lugar recién creado: 10 × 8 m de cemento alisado.</figcaption>
</figure>

## Espacios › Objetos propios {#objetos}

Si el catálogo no tiene algo que tu local sí, armalo con piezas simples: un barril, una heladera de bebidas, un mostrador con estantes. Los objetos propios se suman al catálogo del constructor, en el grupo **Propios**. En la barra dice **Objetos** y el título de la página es **Objetos propios**.

<p class="perm"><span>Quién puede:</span> <span class="tag">Biblioteca</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-objeto.jpg' | relative_url }}" alt="El armador de objetos: Nombre Barril, Va en la disposición: se mueve, Ancho 100, Fondo 60, Alto 90, Sólido tildado, Empezar de con Caja, Cilindro (elegido), Mesa con patas y Estante, Materiales con Principal, la tabla Piezas con un cilindro, y a la derecha la vista previa de un cilindro marrón. Abajo Cancelar y Guardar el objeto." loading="lazy" width="1440" height="790">
  <ol class="marks">
    <li><b>Nombre</b>, <b>Va</b> (si se mueve o queda fijo en el lugar), sus medidas en cm y <b>Sólido</b>.</li>
    <li><b>Empezar de</b>: una forma de base.</li>
    <li><b>Materiales</b>: hasta tres, con su color y su nombre.</li>
    <li><b>Piezas</b>: cada pieza con su forma, material, posición y medidas.</li>
    <li><b>Cómo se ve</b>: la vista previa, en isométrica.</li>
    <li><b>Guardar el objeto</b>.</li>
  </ol>
  <figcaption>Un barril armado con un cilindro.</figcaption>
</figure>

1. Tocá **Nuevo objeto**.
2. Escribí el **Nombre** (por ejemplo «Barril»).
3. En **Va**, elegí **En la disposición: se mueve** (como una mesa) o **Fijo en el lugar** (como una columna, que se guarda con el lugar).
4. Poné el **Ancho**, el **Fondo** y el **Alto** en centímetros. **Sólido: nada se le encima** impide que otra cosa se ponga encima.
5. En **Empezar de**, elegí una base: **Caja**, **Cilindro**, **Mesa con patas** o **Estante**.
6. En **Materiales**, poné hasta tres colores con su nombre (**+ Material**).
7. En **Piezas**, ajustá cada pieza: su forma (Caja o Cilindro), su material, **X** e **Y** (cuánto se corre desde el medio del objeto), **Desde** (a qué altura empieza), **Ancho**, **Fondo** y **Alto**. **+ Pieza** suma otra. Todo en centímetros.
8. Mirá **Cómo se ve** y tocá **Guardar el objeto**. Fornu avisa «Objeto guardado: ya está en el catálogo.».
{: .steps}

Cada objeto queda como una tarjeta con su medida y cuántas piezas tiene, con **Editar** y **Borrar**. Al borrarlo, deja de estar en el catálogo, y un plano que ya lo tiene pide sacarlo la próxima vez que se guarda.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-objetos.jpg' | relative_url }}" alt="Espacios, Objetos propios con dos tarjetas, Barril y Heladera de bebidas, cada una con su medida, sus piezas y los botones Editar y Borrar" loading="lazy" width="1440" height="340">
  <figcaption>Dos objetos propios, ya en el catálogo.</figcaption>
</figure>

## Espacios › Texturas propias {#texturas}

Fotos del piso, de las paredes o de los azulejos del local, y el logo para un cartel: se suman a los materiales del constructor, para que el plano se parezca al lugar. En la barra dice **Texturas** y el título de la página es **Texturas propias**.

<p class="perm"><span>Quién puede:</span> <span class="tag">Biblioteca</span></p>

1. Tocá **Subir una textura** y elegí la foto.
2. En **Nueva textura**, mirá en **Cómo se repite** cómo queda.
3. Escribí el **Nombre** (por ejemplo «Baldosa del patio»).
4. En **Una copia cubre (cm)**, poné cuánto mide en el local lo que se ve en la foto: una baldosa de 20 cm, un logo de 90 cm. Va de 20 a 1000, y empieza en 100.
5. En **Va en**, tildá dónde se usa: **Pisos**, **Paredes** u **Objetos**.
6. Tocá **Guardar**. Fornu avisa «Textura guardada: ya está en los pinceles.».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-textura.jpg' | relative_url }}" alt="El diálogo Nueva textura: Nombre Baldosa del patio, Una copia cubre (cm) en 100 con la ayuda Lo que mide en el local lo que se ve en la foto, y Va en con Pisos tildado y Paredes y Objetos sin tildar." loading="lazy" width="620" height="265">
  <ol class="marks">
    <li><b>Nombre</b>.</li>
    <li><b>Una copia cubre (cm)</b>: el tamaño real de lo que muestra la foto.</li>
    <li><b>Va en</b>: pisos, paredes u objetos.</li>
  </ol>
  <figcaption>Subir la baldosa del patio.</figcaption>
</figure>

Al borrar una textura, donde estaba puesta queda su color. Sin texturas propias, la pantalla dice «Todavía no hay texturas propias.».

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-texturas.jpg' | relative_url }}" alt="Espacios, Texturas propias con una tarjeta, Baldosa del patio, para pisos y de 40 cm, con el botón Borrar" loading="lazy" width="1440" height="340">
  <figcaption>Una textura propia, lista en los pinceles.</figcaption>
</figure>

Además de las propias, el constructor trae estos materiales:

| Para | Materiales |
|---|---|
| Pisos | Parquet claro, Madera oscura, Madera rústica, Damero, Calcáreo, Laja, Césped |
| Pisos y paredes | Piedra gris, Venecitas, Cemento alisado, Cemento oscuro |
| Pisos y objetos | Alfombra, Mármol blanco, Mármol negro |
| Paredes | Revoque blanco, Revoque arena, Revoque verde, Piedra, Ladrillo, Ladrillo reciclado |
| Objetos | Madera (también paredes), Acero, Tela roja, Tela gris |
| Pinturas para paredes y objetos | Blanco, Verde salvia, Azul petróleo, Terracota, Negro |

## Cómo lo ven los mozos {#en-el-salon}

El plano que armaste es el que ven los mozos en [Salón › Mesas]({{ '/es/projects/fornu/manual/salon/' | relative_url }}#mesas) con la vista **Plano**: las mismas paredes y objetos, con cada mesa pintada del color de su estado. Cada equipo elige su vista (Basic, Cenital o Isométrica) y la recuerda.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/espacios-mesas.jpg' | relative_url }}" alt="Salón › Mesas en vista Plano e Isométrica con texturas: el salón de ladrillo con tres mesas y una barra, la mesa 1 marcada en azul con 0 min, y a la derecha la cuenta de la mesa 1 abierta." loading="lazy" width="1440" height="710">
  <ol class="marks">
    <li>La vista, elegida en este equipo.</li>
    <li><b>Texturas</b>, las paredes y el giro, como en el editor.</li>
    <li>La mesa 1, ocupada, en azul. Un toque abre su cuenta.</li>
    <li>La cuenta de la mesa, al lado.</li>
  </ol>
  <figcaption>Atender sobre el plano en isométrica.</figcaption>
</figure>

En el salón en vivo el plano solo se mira y se toca: un toque en una mesa la abre (o la sienta, si está libre), y arrastrar con un dedo mueve el plano. Con el teclado, <kbd>Tab</kbd> pasa de mesa en mesa y <kbd>Enter</kbd> o la barra espaciadora la abre. Para cambiar algo del plano, se vuelve al [editor](#editor).
