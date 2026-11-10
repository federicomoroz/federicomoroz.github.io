---
layout: manual
manual: index
title: "Manual de Fornu"
heading: "Manual de uso"
description: "Cómo se usa Fornu, pantalla por pantalla: qué hace cada una, cómo se hace cada cosa, quién puede hacerla y los atajos que ahorran tiempo en el servicio."
permalink: /es/projects/fornu/manual/
---

Fornu junta en un solo lugar los pedidos del delivery, del salón y del mostrador, la cocina, el stock, la caja, las compras y el personal. Este manual recorre cada pantalla en el orden en que se usa en un local: primero entrar y moverse, después el servicio, después lo que se arma una vez y se revisa cada tanto.

Cada página dice para qué sirve la pantalla, cómo se hace cada cosa paso a paso, qué significa cada opción y qué permiso hace falta. Las capturas son de la cuenta de demo, con datos inventados. Para probar mientras leés, entrá a [fornu.onrender.com](https://fornu.onrender.com) y tocá **Probar la demo**.

## Las páginas {#paginas}

<ol class="manual-index">
{% for p in site.data.fornu_manual %}
  <li><a href="{{ '/es/projects/fornu/manual/' | append: p.id | append: '/' | relative_url }}">{{ p.title.es }}</a><p>{{ p.lead.es }}</p><small>{{ p.who.es }}</small></li>
{% endfor %}
</ol>

## Qué lee cada puesto {#por-puesto}

| Si sos… | Empezá por |
|---|---|
| Dueño o administración | [Entrar y moverse]({{ '/es/projects/fornu/manual/empezar/' | relative_url }}), [Ajustes]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}), [Carta]({{ '/es/projects/fornu/manual/carta/' | relative_url }}), [Insumos y stock]({{ '/es/projects/fornu/manual/insumos-y-stock/' | relative_url }}) y [Costos y reportes]({{ '/es/projects/fornu/manual/costos-y-reportes/' | relative_url }}) |
| Encargado o encargada | [Pedidos y delivery]({{ '/es/projects/fornu/manual/pedidos/' | relative_url }}), [Caja y ventas]({{ '/es/projects/fornu/manual/caja/' | relative_url }}), [Compras y gastos]({{ '/es/projects/fornu/manual/compras-y-gastos/' | relative_url }}) y [Personal]({{ '/es/projects/fornu/manual/personal/' | relative_url }}) |
| Cocina | [En la cocina y en la calle]({{ '/es/projects/fornu/manual/cocina-y-reparto/' | relative_url }}) y el tablero de [Pedidos y delivery]({{ '/es/projects/fornu/manual/pedidos/' | relative_url }}) |
| Mozo, adicionista o caja del salón | [Salón: mesas, mostrador y cobro]({{ '/es/projects/fornu/manual/salon/' | relative_url }}) |
| Mensajero | [En la cocina y en la calle]({{ '/es/projects/fornu/manual/cocina-y-reparto/' | relative_url }}#mensajero) |

## Dos formas de entrar {#entrar}

- **Con email y contraseña**, desde cualquier navegador. Es la entrada del dueño, la administración y el encargado: abre la pantalla completa, con todos los módulos que su rol le deja ver.
- **Con PIN, en un dispositivo vinculado.** La tablet de la cocina, el celular del mozo o del mensajero se vinculan una vez con un código, y desde ahí cada persona toca su nombre y pone su PIN. Ve solo las pestañas de su trabajo y ficha la entrada en el mismo toque.

Las dos se explican en [Entrar y moverse]({{ '/es/projects/fornu/manual/empezar/' | relative_url }}) y en [En la cocina y en la calle]({{ '/es/projects/fornu/manual/cocina-y-reparto/' | relative_url }}).

## Lo básico y los módulos {#modulos}

Toda cuenta tiene lo básico: el tablero de pedidos y el delivery propio, la carta, los insumos y el stock, la caja, los gastos, el equipo con sus dispositivos y la configuración. Encima van los módulos, que se prenden por cuenta:

| Módulo | Qué suma |
|---|---|
| **Salón** | Mesas y sectores, mozos con PIN, rondas a la cocina por tiempos, cobro en partes con propina, mostrador y mostrador express. |
| **Constructor de espacios** | El plano del local con paredes, pisos, puertas, ventanas y objetos, en vista cenital o isométrica. |
| **Delivery por plataformas** | Rappi y PedidosYa en el mismo tablero, la carta publicada en cada tienda y lo agotado que se apaga solo. |
| **Facturación electrónica** | Facturas A, B y C con CAE de ARCA, solas o a mano, sus notas de crédito y el listado para el contador. |
| **Personal** | Presentismo, fichaje con PIN, horarios, liquidación de sueldos y adelantos. |
| **Proveedores y compras** | Proveedores con su CUIT y su saldo, y compras de insumos que entran al stock. |
| **Costos y márgenes** | Lo que hay para revisar, la ficha de costo, el margen en cada canal y estadísticas. |
| **Reportes** | Resumen de ventas y rentabilidad por unidad de negocio y por canal. |

Un módulo apagado no aparece en ninguna pantalla, ni como botón gris. Lo que guardó queda para cuando se vuelva a prender. Los módulos también vienen en grupos pensados para cada tipo de local: **Dark kitchen** (plataformas, costos y reportes), **Restaurante** (salón, personal y facturación), **Cafetería** (salón y facturación) y **Salón Pro** (salón y constructor).

## Roles y permisos {#permisos}

Lo que cada persona ve y hace sale de sus roles. Los roles los arma cada cuenta con el nombre que usa el local (Parrillero, Moza, Caja) y con los permisos que elige. Cómo se arman está en [Personal]({{ '/es/projects/fornu/manual/personal/' | relative_url }}#roles). La **Administración** de la cuenta puede todo lo que la cuenta tiene prendido. Cada página del manual dice qué permiso pide cada cosa, con estos nombres:

| Permiso | Qué deja hacer |
|---|---|
| Cocina | Confirmar o cancelar los pedidos, marcarlos listos, tomar pedidos propios y cargar mermas y producción. |
| Mensajería | Llevar los pedidos propios desde el celular y ver el efectivo que tiene encima. |
| Pedidos | Ver el historial y el detalle de los pedidos y rendir el efectivo de los mensajeros. |
| Carta | Crear y cambiar productos, precios, categorías y grupos modificadores, y publicar la carta. |
| Insumos | Cargar ingredientes, elaboraciones y artículos con sus costos, recetas y categorías. |
| Stock | Ver el stock, cargar conteos, mermas y producción, y planificar la producción. |
| Caja | Abrir y cerrar la caja, cargar movimientos y ver las ventas. |
| Ver lo esperado | Ver lo que el sistema espera en la caja antes de contarla. Sin este permiso, el arqueo es a ciegas. |
| Recontar la caja | Contar de nuevo después de confirmar un conteo. |
| Gastos | Cargar, pagar y anular gastos y compras. Las categorías de gastos se arman con el permiso Ajustes. |
| Equipo | Dar de alta al personal y sus PIN. |
| Dispositivos | Vincular tablets y celulares y darlos de baja. |
| Ajustes | Unidades de negocio, estaciones, medios de pago, clientes y la configuración de la cuenta. |

Los módulos suman los suyos: el Salón trae **Atender mesas**, **Asignar quién atiende**, **Mover mesas**, **Anular lo mandado**, **Descontar e invitar**, **Cobrar mesas**, **Deshacer cobros**, **Cancelar mesas** y **Armar el salón**. Facturación trae **Facturar**, **Ver facturas** y **Configurar la facturación**. Personal trae **Presentismo**, **Adelantos** y **Liquidación**. Proveedores y compras trae **Proveedores**, Costos trae **Costos**, Reportes trae **Reportes** y el Constructor trae **Biblioteca**.

Una cuenta nueva arranca con tres roles: **Cocina**, **Mensajería** y **Encargado/a** (cocina, pedidos, stock, caja con lo esperado y el recuento, gastos y dispositivos). Con el Salón llegan tres más, sugeridos: **Mozo**, **Adicionista** y **Caja**.

## Palabras que usa la app {#palabras}

| Palabra | Qué es |
|---|---|
| Unidad de negocio | Cada marca que vende la cocina, con su carta, su color y sus canales. Todas comparten la cocina, el stock y la caja. |
| Canal | Por dónde entra la venta: **Propios** (el delivery del local), **Rappi**, **PedidosYa** o **Salón**. Cada uno con su precio y su comisión. |
| Pedido propio | Un pedido que toma el local, por teléfono o por mensaje, y reparten sus mensajeros. |
| Estación | Un lugar de la cocina que prepara una parte: parrilla, cocina, barra. Cada una recibe su comanda. |
| Comanda | Lo que la cocina tiene que preparar de un pedido o de una ronda, en pantalla o en papel. |
| Ronda | Lo que un mozo manda a la cocina de una vez desde una mesa. |
| Tiempo | Cuándo sale cada cosa en el salón: **Ya**, **Entrada**, **Principal** o **Postre**. |
| Insumo | Lo que se usa para hacer la carta: ingredientes, elaboraciones de la cocina y artículos de inventario, como el packaging. |
| Elaboración | Lo que la cocina hace por tandas con su receta, como una salsa o los medallones. |
| Adicionales | Lo que lleva cada venta además de la receta, como la caja o el sobre de salsa del delivery. |
| Arqueo | Contar la caja al abrirla y al cerrarla, y ver la diferencia con lo que dice el sistema. |
| Rendición | Cuando un mensajero entrega el efectivo que cobró en sus pedidos. |
