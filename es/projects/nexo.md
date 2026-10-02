---
title: Nexo
description: "Un mayorista mandaba el catálogo por FTP una vez por día. Acá el ERP publica y la red escucha. La persistencia está detrás de puertos, y hay una suite que corre los mismos casos contra cuatro motores."
permalink: /es/projects/nexo/
---

<p class="crumbs"><a href="{{ '/es/projects/' | relative_url }}">← Volver a proyectos</a></p>

<section class="hero">
  <h1>Nexo <span class="tag active">activo</span></h1>
  <p class="lead">Un distribuidor mayorista le mandaba planillas por FTP a 40 revendedores, una vez por día, y <strong>el stock de la mañana no servía a la tarde</strong>. Con Nexo, el ERP publica los cambios y los revendedores bajan el catálogo por WebSocket. Después quedan en esa misma conexión, recibiendo cada cambio a medida que se publica.</p>
  <div class="chip-row">
    <span class="tag">C#</span><span class="tag">.NET 8</span><span class="tag">ASP.NET Core MVC</span>
    <span class="tag">WebSocket</span><span class="tag">SSE</span><span class="tag">EF Core</span>
    <span class="tag">MySQL</span><span class="tag">PostgreSQL</span><span class="tag">Testcontainers</span>
    <span class="tag">xUnit</span><span class="tag">Docker</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/nexo" target="_blank" rel="noopener">Repo ↗</a>
    <a href="https://github.com/federicomoroz/nexo/tree/main/docs/adr" target="_blank" rel="noopener">Los once ADR ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">Sobre los datos</p>
  <p>Los datos del repositorio son placeholder, para publicar el sistema sin exponer al cliente. La documentación es la interna del proyecto, incluidos los ADR, el runbook y el contrato con el ERP. El código, las mediciones y los 356 tests son reales y se reproducen con los comandos del README.</p>
</div>

{% include nexo-diagramas.html
    circuit_head="El ERP publica; la red consulta y escucha. El diario de cambios lleva un número correlativo y cada revendedor guarda hasta dónde leyó."
    circuit_alt="Diagrama animado del circuito: el ERP escribe hacia Nexo, los revendedores consultan, y Nexo les empuja los cambios de vuelta. Debajo, la marca del diario de cambios."
    erp_sub="catálogo · precios<br>existencias"
    pipe_write="el ERP escribe"
    pipe_read="la red consulta"
    pipe_push="Nexo empuja los cambios"
    peer_1="Sanitarios Sur"
    peer_2="Ferretera Norte"
    peer_3="Casa Grande"
    peer_more="+ 37 revendedores"
    watermark_label="marca del diario"
    circuit_foot="Un cambio de stock publicado a las 14:03 le llega a los revendedores conectados antes de las 14:03:01."

    bp_head="El servidor no manda el siguiente lote hasta que vuelve la confirmación del anterior."
    bp_alt="Diagrama animado de contrapresión: el servidor envía un lote de 500 artículos, espera, y recién cuando llega el ack del revendedor manda el siguiente."
    bp_server="servidor"
    bp_client="revendedor"
    bp_batch_tag="lote"
    bp_batch="500 artículos"
    bp_ack_tag="confirmación"
    bp_held="esperando · nada sale"
    bp_foot="El buffer de escritura de un WebSocket acepta mucho más de lo que la red del otro lado puede tragar. Sin esta pausa, el servidor acumula megabytes en memoria por cada revendedor con enlace lento mientras sigue leyendo la base a toda velocidad. Del lado del cliente, la regla es confirmar el lote <b>después</b> de persistirlo."

    eng_head="La capa de aplicación referencia únicamente al dominio: cero paquetes, ni una mención a Entity Framework."
    eng_alt="Diagrama animado: los mismos puertos arriba y cuatro motores de base abajo turnándose, cada uno con la marca de 27 de 27 casos de contrato pasados."
    eng_ports="Puertos"
    eng_prod="producción"
    eng_demo="la demo"
    eng_pre="preproducción"
    eng_mem="En memoria"
    eng_dev="desarrollo"
    eng_foot="Los mismos 27 casos corren contra los cuatro, sin un <code>if</code> por proveedor. MySQL y PostgreSQL en contenedores reales en CI; sin Docker esos casos se reportan como omitidos. El proveedor en memoria está escrito sin EF Core, así que si los puertos filtraran algo de EF no compilaría."
%}

<div class="statline">
  <div class="stat"><span class="num">356</span><span class="lbl">tests en CI</span></div>
  <div class="stat"><span class="num">27<small>×4</small></span><span class="lbl">casos de contrato × motores</span></div>
  <div class="stat"><span class="num">68<small>ms</small></span><span class="lbl">de un cambio del ERP a 40 revendedores</span></div>
</div>

## Cambiar de base de datos es cambiar una línea

Toda la persistencia pasa por puertos declarados en la capa de aplicación, que
**referencia únicamente al dominio: cero paquetes, ni una mención a Entity
Framework**. Hay cuatro implementaciones y se elige por configuración:

```json
"Nexo": { "Persistence": { "Provider": "MySql" } }
```

| Proveedor | Dónde corre | Cómo está hecho |
|---|---|---|
| MySQL | producción | EF Core, migraciones propias |
| PostgreSQL | la configuración de despliegue | EF Core, migraciones propias |
| SQLite | preproducción | EF Core, migraciones propias |
| En memoria | desarrollo y tests | a mano, **sin una línea de EF** |

El proveedor en memoria está escrito sin EF, así que si los puertos filtraran
algo de EF, ese proyecto no compilaría. Con eso la abstracción se puede
verificar.

Además, `tests/Nexo.Persistence.ContractTests` ejecuta **los mismos 27 casos
contra los cuatro proveedores**, sin un `if` por proveedor. Las clases por motor
son cuatro líneas y no definen ni un caso propio. MySQL y PostgreSQL corren en
contenedores reales en CI, con las migraciones versionadas aplicadas. Sin
Docker, esos casos se reportan como **omitidos**, para que un test que no corrió
nunca figure en verde.

PostgreSQL se sumó cuando todo lo demás ya estaba escrito. Hicieron falta dos
archivos de proveedor, sus migraciones, un fixture y una clase de cuatro líneas.
Los casos de contrato pasaron a la primera, sin tocar casos de uso,
controladores ni el handler del WebSocket.

## Contrapresión: el servidor espera

El buffer de escritura de un WebSocket acepta más datos de los que la red del
otro lado puede tragar. Sin confirmación por lote, el servidor acumula megabytes
en memoria por cada revendedor con enlace lento mientras sigue leyendo la base a
toda velocidad.

Por eso el servidor no manda el siguiente lote hasta recibir el `ack` del
anterior. El cliente tiene que confirmar recién **después** de persistir el
lote. La documentación del protocolo lo pide de forma explícita, porque
confirmar al recibir es el error más probable de un integrador.

Para empalmar la foto con el flujo sin perder nada, la marca del diario se toma
**antes** de leer el primer lote y viaja en el encabezado. Si el catálogo cambia
durante el recorrido, esos cambios llegan igual por el diario después. Si la
marca se tomara al final, se perderían.

## La política de acceso y el orden de los controles

Cada pedido pasa por siete controles, en este orden:

```
formato → clave → vigencia → whitelist → cuenta → scope → cupo
```

Dos de esas posiciones tienen un test propio que las fija:

- **La whitelist de IP va después de verificar el secreto.** Al revés, alguien
  que solo conoce el prefijo (es público y aparece en los logs) podría probar
  desde distintas redes y mapear los rangos permitidos de una cuenta ajena, sin
  tener ninguna credencial válida.
- **El cupo se consume al final.** Es el único paso con efecto lateral. Si se
  descontara antes de autenticar, cualquiera podría dejar sin servicio a otra
  cuenta mandando basura con el prefijo de la víctima.

El handshake del WebSocket corre **exactamente el mismo pipeline** que el filtro
de MVC, así que la política está implementada una sola vez para los dos
transportes.

## La vista: una consola de operaciones

La aplicación es MVC (`AddControllersWithViews`, cinco controladores, vistas
Razor), pero cuatro de los cinco controladores sirven JSON, porque quienes
consumen la API son integraciones. La vista es una sola pantalla.

<figure class="shot">
  <img src="{{ '/assets/img/nexo-panel.jpg' | relative_url }}" alt="Consola de operaciones de Nexo: cuatro indicadores arriba —una conexión activa, 59 pedidos por minuto, 7 rechazos por minuto y 4 milisegundos de latencia p95—; debajo, la actividad por revendedor con los pedidos y rechazos de cada cuenta, los rechazos agrupados por motivo (BadSecret, UnknownKey, ScopeNotGranted) y el feed de últimos hechos con la apertura de un stream y las credenciales rechazadas." loading="lazy" width="1500" height="823">
  <figcaption>La vista, corriendo. Los números salen de tráfico real contra la instancia local: consultas que pasan, credenciales inválidas que se rechazan y un snapshot en curso. El panel lee del bus de hechos.</figcaption>
</figure>

El panel muestra en vivo las conexiones activas, la actividad por revendedor,
los rechazos por motivo y la latencia p95. Se alimenta del mismo bus de hechos
que emite el pipeline de autorización, **sin consultar la base de negocio**. Si
el panel se cae, la API ni se entera, y hay un test que lo verifica.

Los datos llegan por Server-Sent Events. SignalR era el candidato natural, pero
el panel corre detrás de la VPN, sin salida a internet para bajar el cliente de
un CDN, y el repo no tiene build de front. `EventSource` ya viene en el
navegador y reconecta solo. Para un flujo de una sola vía, alcanza.

## Cupo por clave, compartido entre instancias

Cada credencial trae su propio cupo por minuto, y el paso que lo descuenta es el
último del pipeline. La cuenta vive en Redis, en una ventana deslizante sobre un
*sorted set*. Las cuatro operaciones (descartar lo que salió de la ventana,
contar, agregar y renovar el vencimiento) van en **un solo script Lua**. Si
fueran cuatro viajes separados, dos instancias podrían leer 119 al mismo tiempo
y dejar pasar las dos.

Si Redis no contesta, qué hacer lo elige el operador.
`PerProcess` sigue atendiendo con el contador de cada proceso. Es el default,
porque el cupo protege la base del distribuidor y una caída de Redis no tiene
por qué ser una caída del servicio. `Reject` devuelve 429 hasta que Redis
vuelva. Cuál corresponde depende de si el cupo es una protección o una
obligación.

## Quién entra al panel

Con un proveedor de identidad cargado, el panel pide inicio de sesión por
**OpenID Connect** (*code flow* con PKCE, cookie de sesión de ocho horas y un
grupo exigible por configuración), y el token compartido deja de valer. Si los
dos convivieran, el token permitiría saltearse el control de identidad.

El nombre del claim que trae los grupos es configuración, porque cambia según el
proveedor: Entra ID manda `roles`, Okta suele mandar `groups`. La suite corre el
flujo completo contra un Keycloak en un contenedor: descubrimiento, PKCE, login,
intercambio del code, claims y cookie.

## Cómo se opera

Para que lo pueda operar y mantener otra persona, el repo trae:

- **`/health/live` y `/health/ready` separados**, y el de vida no depende de la
  base a propósito: si dependiera, una caída de MySQL haría que el orquestador
  mate y reinicie contenedores sanos en bucle.
- **Un runbook organizado por síntoma del negocio**, como «a un revendedor no le
  llegan los cambios», «todos fallan de golpe» o «el ERP no está publicando».
  Cada uno con los `curl` y las consultas concretas.
- **La especificación del protocolo y una guía de integración por cada tipo de
  consumidor** (el ERP que escribe y el revendedor que lee), con el contrato de
  errores y los tamaños de lote recomendados.
- **Once ADR** que registran lo que se descartó y por qué, para cuando, seis
  meses después, alguien vuelva a proponer una de esas alternativas.

## Bitácora

Lo que cambió en el camino y por qué. El detalle de cada punto está en su ADR.

| Qué pasó | Qué salió de ahí |
|---|---|
| El benchmark que escribí para respaldar un ADR **refutó sus dos afirmaciones**. | El ADR se corrigió con la tabla medida y sigue publicado. La decisión se sostiene en 1 autorización contra 96. La velocidad dejó de ser argumento. ([ADR 0001](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0001-websocket-para-la-sincronizacion-completa.md)) |
| La misma búsqueda devolvía resultados distintos según el motor, y las fechas se corrían tres horas. | Normalización en el dominio, en columnas indexables. Ninguno de los dos se veía testeando contra un solo motor. ([ADR 0008](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0008-columnas-normalizadas-para-busqueda.md)) |
| Un test mostró que la configuración de `X-Forwarded-For` que aparece en los ejemplos deja pasar el header de cualquiera. | Sin proxies declarados, el procesamiento del header se apaga por completo. Quedó además una regla: un comentario del tipo «esto es seguro porque X» se trata como una hipótesis. ([ADR 0009](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0009-forwarded-headers-cierra-por-defecto.md)) |
| El supuesto de «un solo escritor» no lo hacía cumplir nada: dos lotes solapados le escondían un cambio al que lee. | Los escritores se serializan con un lock de fila, y hay un caso de contrato con dos escritores y un lector. ([ADR 0004](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0004-un-solo-escritor-en-el-diario-de-cambios.md)) |
| Probar el OIDC contra un proveedor real encontró que `ForbidAsync` redirigía en vez de devolver 403, y que el rol nunca se encontraba. | El flujo completo pasó a estar verificado, y el nombre del claim a ser configuración. ([ADR 0011](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0011-identidad-del-panel-interno.md)) |
| La primera prueba de carga daba 0 de 40 conexiones. | El servidor no completaba el apretón de manos de cierre cuando cerraba el cliente. Dos clientes del repo lo tapaban con un `try/catch`. |
| La medición de propagación daba 227 ms, y ese número se leía como «el costo de despachar a cuarenta». | Con la curva completa (1, 5, 10, 20 y 40 conexiones), la latencia no se mueve: el costo está en el camino de escritura y el reparto sale casi gratis. Con un solo punto no se puede separar el costo fijo del que escala. |
