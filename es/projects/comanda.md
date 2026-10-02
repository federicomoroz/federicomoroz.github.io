---
title: Comanda
description: "Gestión gastronómica para un restaurante: pedidos en tablet, cocina por estación en pantalla y en papel, caja con factura electrónica, stock por receta y avisos al dueño. Corre en una PC del local y sigue funcionando sin internet."
permalink: /es/projects/comanda/
---

<p class="crumbs"><a href="{{ '/es/projects/' | relative_url }}">← Volver a proyectos</a></p>

<section class="hero">
  <h1>Comanda <span class="tag active">activo</span></h1>
  <p class="lead"><strong>Sistema de gestión gastronómica para restaurantes.</strong> Los mozos toman los pedidos en una tablet, cada estación de la cocina recibe lo suyo en pantalla y en papel, y la caja cobra y factura. Todo corre en una computadora del restaurante, así que <strong>si se corta internet, el salón sigue funcionando</strong>.</p>
  <div class="chip-row">
    <span class="tag">C#</span><span class="tag">.NET 8</span><span class="tag">ASP.NET Core MVC</span>
    <span class="tag">SignalR</span><span class="tag">EF Core</span><span class="tag">React</span>
    <span class="tag">TypeScript</span><span class="tag">PostgreSQL</span><span class="tag">Docker</span>
    <span class="tag">xUnit</span><span class="tag">Testcontainers</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/comanda-docs" target="_blank" rel="noopener">Documentación ↗</a>
    <a href="https://github.com/federicomoroz/comanda-docs/blob/main/docs/adr/0001-facturacion-como-servicio-aparte.md" target="_blank" rel="noopener">Por qué la facturación va aparte ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">Sobre los datos</p>
  <p>La carta inicial sale de la carta online pública de una parrilla real; todo lo demás (bebidas, mesas, personal, insumos, costos y datos fiscales) es simulado, y la facturación usa un ARCA simulado, así que los comprobantes salen como «sin validez fiscal». El código es privado; la documentación, las capturas y los diagramas son públicos.</p>
</div>

<figure class="shot">
  <video controls muted playsinline preload="metadata" poster="{{ '/assets/img/comanda-video-poster.jpg' | relative_url }}" width="1566" height="936">
    <source src="{{ '/assets/video/comanda.mp4' | relative_url }}" type="video/mp4">
  </video>
  <figcaption>Un pedido de punta a punta, en una sola toma y con la aplicación funcionando. A la izquierda, la tablet de la moza; a la derecha, la cocina y después la caja. La comanda aparece en la cocina en el momento en que se envía, y la factura vuelve autorizada sola.</figcaption>
</figure>

<div class="statline">
  <div class="stat"><span class="num">173</span><span class="lbl">tests, con los dos servicios sobre bases reales</span></div>
  <div class="stat"><span class="num">14<small>s</small></span><span class="lbl">para que una factura que esperaba salga sola, cuando vuelve Facturación</span></div>
  <div class="stat"><span class="num">0</span><span class="lbl">facturas perdidas con Facturación o ARCA caídas</span></div>
</div>

## Un turno, desde cada puesto

**El mozo** ve el salón entero: qué mesas están libres, cuánto lleva cada una, quién la atiende, si tiene platos listos para llevar o si ya pidió la cuenta. Carga el pedido con sus opciones (el punto de la carne, los gustos de la ensalada, el sabor de la gaseosa) y lo envía. **La cocina** tiene una pantalla por estación, con las comandas numeradas del día. Cada una se pone amarilla a los 12 minutos y roja a los 20; los dos números se cambian desde Administración.

<div class="shot-pair">
  <figure class="shot">
    <img src="{{ '/assets/img/comanda-salon.jpg' | relative_url }}" alt="El salón en la tablet del mozo: las mesas libres en blanco y las ocupadas con el total, el mozo y avisos como «5 listos», «Cuenta» o «1 sin enviar»." loading="lazy" width="834" height="1112">
    <figcaption>El salón, en la tablet.</figcaption>
  </figure>
  <figure class="shot">
    <img src="{{ '/assets/img/comanda-cocina.jpg' | relative_url }}" alt="La pantalla de cocina con todas las estaciones: comandas en verde, amarillo y rojo según la demora, con el punto de la carne y las notas destacadas, y unas papas fritas anuladas tachadas." loading="lazy" width="1440" height="1150">
    <figcaption>La cocina, con todas las estaciones. Lo anulado queda tachado y, si la estación tiene impresora, también sale un aviso en papel.</figcaption>
  </figure>
</div>

**La caja** cobra en partes, con distintos medios de pago, propina y vuelto, y emite la factura A, B o C sin hacer esperar a nadie. Muestra lo cobrado que falta facturar y cierra el turno con arqueo: lo que tendría que haber contra lo que se contó.

<figure class="shot">
  <img src="{{ '/assets/img/comanda-factura.jpg' | relative_url }}" alt="La caja con una factura B autorizada: datos del emisor, ítems, IVA contenido, CAE y el QR de ARCA, marcada como comprobante simulado." loading="lazy" width="1440" height="900">
  <figcaption>Factura B con CAE y el QR en el formato de ARCA. En esta versión el CAE viene de un simulador, y el comprobante lo dice dos veces.</figcaption>
</figure>

**El dueño** configura todo desde la pantalla, sin tocar código: la carta, los precios, las opciones de cada plato, las estaciones, las mesas, el personal y sus permisos, los medios de pago y los datos fiscales. Cada plato tiene su receta: al cobrar se descuentan los insumos y la administración muestra cuánto deja cada plato y cuáles quedaron por debajo del margen objetivo. Por Telegram, mail o Slack se entera de un insumo que llega al mínimo, de una caja que cierra con diferencia o de una anulación grande.

<figure class="shot">
  <img src="{{ '/assets/img/comanda-margenes.jpg' | relative_url }}" alt="Administración, recetas y márgenes, filtrado a los platos por debajo del objetivo del 65%: precio, precio sin IVA, costo de la receta y margen en rojo." loading="lazy" width="1440" height="610">
  <figcaption>Los platos que quedaron por debajo del margen objetivo, con el costo de su receta.</figcaption>
</figure>

## De la mesa a la factura

<figure class="shot">
  <a href="{{ '/diagramas/comanda/circuito.html' | relative_url }}"><img src="{{ '/assets/img/comanda-circuito.gif' | relative_url }}" alt="Animación en seis pasos: el mozo envía el pedido; Comanda arma una comanda por estación; la cocina marca listo y la tablet del mozo se entera; la caja cobra; Facturación pide el CAE a ARCA; la factura vuelve autorizada con su QR." loading="lazy" width="1200" height="750"></a>
  <figcaption>El recorrido completo de un pedido. Salón, cocina y caja comparten una base y una transacción; la facturación va aparte.</figcaption>
</figure>

Cobrar una cuenta descuenta el stock, cierra la mesa y suma al turno. **O pasa todo o no pasa nada**, y por eso esas partes viven juntas, en un mismo servicio con una misma base. La facturación va en un servicio aparte, con su base y su cola, porque depende de ARCA, que a veces no responde, y porque con ARCA real es la que guarda el certificado digital del local.

## Si algo se cae, no se pierde nada

<figure class="shot">
  <a href="{{ '/diagramas/comanda/facturacion.html' | relative_url }}"><img src="{{ '/assets/img/comanda-facturacion.gif' | relative_url }}" alt="Animación en seis pasos: el pedido de factura se guarda en el outbox junto con la cuenta; Facturación no responde y el pedido espera; Facturación vuelve y el pedido sale solo; ARCA no responde y la factura espera en la cola; ARCA vuelve con el CAE; el estado vuelve a Comanda con su número de versión." loading="lazy" width="1200" height="750"></a>
  <figcaption>Cada servicio guarda en su outbox lo que le debe al otro, en la misma transacción que el cambio, y reintenta hasta que llega.</figcaption>
</figure>

- **Si Facturación no responde**, la caja muestra «Esperando a Facturación» y el motivo, y el cajero sigue con la próxima mesa. El pedido queda guardado y sale solo. Medido con las imágenes de producción: salió 14 segundos después de que el servicio volvió.
- **Si ARCA no responde**, la factura espera en la cola de Facturación, en orden, para que la numeración siga correlativa. Cada reintento llega más espaciado, de 10 segundos a 5 minutos, y el dueño recibe un aviso cuando se cae y otro cuando vuelve.
- **Si se repite un envío**, no se duplica nada. Cada pedido lleva un identificador, así que el mismo pedido dos veces es una sola factura, y cada estado lleva un número de versión, así que uno viejo que llega tarde no pisa al nuevo.
- **Si Facturación rechaza el pedido** (un DNI mal cargado, por ejemplo), el cajero lo ve en el momento, con el motivo, y puede volver a facturar esa cuenta.

## Funciona sin internet

<figure class="shot">
  <a href="{{ '/diagramas/comanda/instalacion.html' | relative_url }}"><img src="{{ '/assets/img/comanda-instalacion.gif' | relative_url }}" alt="Animación en cinco pasos: tablets, pantallas de cocina, caja e impresoras hablan con la PC del local; se corta internet y el salón sigue; las facturas y los avisos esperan en cola; vuelve internet y sale todo; las dos bases se respaldan." loading="lazy" width="1200" height="750"></a>
  <figcaption>Internet solo hace falta para facturar y para avisarle al dueño, y las dos cosas esperan en cola.</figcaption>
</figure>

El sistema completo se instala con Docker Compose en una PC del restaurante, y tablets, pantallas e impresoras se conectan por el Wi‑Fi del local. Las dos bases se respaldan solas: al arrancar, si el último respaldo tiene más de un día, y después una vez por día, en un disco externo o en una carpeta que sincroniza la nube. Restaurar es un comando, y antes de restaurar se respalda el estado actual por si se eligió la carpeta equivocada.

## Para técnicos

<figure class="shot">
  <a href="{{ '/diagramas/comanda/arquitectura.html' | relative_url }}"><img src="{{ '/assets/img/comanda-arquitectura.png' | relative_url }}" alt="Mapa de la arquitectura: en el salón, tablets, pantallas de cocina, caja e impresoras; en la PC del local, el servidor (Comanda.Api, Application, Domain, Infrastructure), el servicio de facturación con su cola y su outbox, PostgreSQL con dos bases, el agente de impresión, notify-router y los respaldos; por internet, ARCA, los canales del dueño y el disco de respaldo. Cada conexión con su protocolo y su clave." loading="lazy" width="1600" height="1010"></a>
  <figcaption>El mapa completo: qué corre dónde, cómo se hablan las piezas y qué guarda cada una. La versión interactiva tiene las conexiones animadas por tipo.</figcaption>
</figure>

<div class="cards">
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/comanda/arquitectura.html' | relative_url }}">El mapa completo ↗</a></div>
    <div class="card-desc"><p>Los contenedores, los proyectos de cada servicio, el protocolo y la clave de cada conexión y las tablas de cada base.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/comanda/circuito.html' | relative_url }}">De la mesa a la factura ↗</a></div>
    <div class="card-desc"><p>Los seis pasos de un pedido, de la tablet a la factura autorizada.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/comanda/facturacion.html' | relative_url }}">Si Facturación se cae ↗</a></div>
    <div class="card-desc"><p>El outbox en los dos sentidos, la cola hacia ARCA y los estados con versión.</p></div>
  </article>
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/diagramas/comanda/instalacion.html' | relative_url }}">Funciona sin internet ↗</a></div>
    <div class="card-desc"><p>La instalación en el local: qué necesita internet, qué no, y los respaldos.</p></div>
  </article>
</div>

| Servicio | Por qué va aparte |
|---|---|
| **server** (`Comanda.Api`) | Salón, caja, cocina y stock. Van juntos porque cobrar toca a todos y tiene que quedar completo o no quedar, en una sola transacción. |
| **billing** (`Comanda.Billing`) | Depende de ARCA y, con ARCA real, guarda el certificado del local. Base, cola y outbox propios; no publica puertos. |
| **print-agent** | Tiene que correr cerca de las impresoras. Pregunta por HTTP qué imprimir y lo manda en ESC/POS por TCP 9100. |
| **notify-router** | Otro lenguaje (Python) y otro ciclo de vida. Si se cae, el salón no se entera. |
| **backup** | `pg_dump` de las dos bases, con retención y restauración. |

Las decisiones que sostienen el resto:

- **Outbox transaccional en los dos sentidos, con una fila por destino.** Que notify-router esté caído no frena los pedidos de factura, y un pedido nuevo nunca se adelanta a un mensaje más viejo para el mismo destino: así la numeración no se desordena. Un 2xx es entregado; 5xx, 408 y 429 se reintentan; cualquier otro 4xx queda apartado con el error a la vista del administrador.
- **El pedido se guarda primero y se intenta mandar en el momento.** El cajero ve un rechazo enseguida, y si Facturación no responde, el pedido queda en cola sin que nadie lo vuelva a cargar.
- **La base pone los límites.** Índices únicos parciales impiden dos cuentas abiertas en una mesa, dos cajas abiertas, dos facturas vivas para una cuenta y dos comandas con el mismo número. El número de comanda sale de un contador atómico por día. Cuentas, turnos y facturas llevan token de concurrencia.
- **Copias, no referencias.** Cada ítem guarda el nombre, el precio, el IVA y la estación del momento en que se pidió: cambiar la carta no altera las cuentas abiertas ni la historia.
- **Sesiones validadas en cada pedido.** Login por PIN con bloqueo por intentos, cookie de sesión y roles; desactivar a alguien corta su acceso al instante.
- **Una mudanza de datos sin ventanas.** Las facturas que el servidor emitía antes de que existiera Facturación pasaron al servicio nuevo con una migración que, en una sola transacción, convierte cada fila en un mensaje del outbox y borra las tablas viejas. Facturación las importa con su número y su CAE originales. La migración tiene un test que la corre sobre una base con datos.

Los 173 tests corren contra PostgreSQL real con Testcontainers, y los de Comanda levantan también el servicio de Facturación en memoria, con su propia base, hablándose por HTTP. Además, el sistema completo se probó de punta a punta con las imágenes de producción: Facturación caída, ARCA caída, el servidor caído mientras Facturación autoriza, el servidor arrancando sin Facturación, un reinicio completo y una restauración de respaldo.

## Lo que no hace

- **No factura todavía contra ARCA real.** Hace falta el certificado digital del local. Se implementa detrás de una sola interfaz (WSAA + WSFEv1) y se prueba en el entorno de homologación de ARCA; los tipos de comprobante, el IVA por alícuota, la numeración, la cola, el CAE y el QR ya están hechos.
- **No maneja varios locales en una instalación.** Cada local tiene su servidor y su base. Un servicio en la nube para muchos locales es una decisión de producto, con datos separados por local y un agente que sincronice para no depender de internet.
- **No se probó con el hardware de un restaurante.** Las impresoras se probaron contra una impresora simulada por TCP; falta una prueba con las tablets, las pantallas y una térmica reales.
