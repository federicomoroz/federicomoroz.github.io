---
title: Nexo
description: "Un mayorista mandaba el catálogo por FTP una vez por día. Acá el ERP publica y la red escucha. La persistencia está detrás de puertos, y hay una suite que corre los mismos casos contra cuatro motores."
permalink: /es/projects/nexo/
---

<p class="crumbs"><a href="{{ '/es/projects/' | relative_url }}">← Volver a proyectos</a></p>

<section class="hero">
  <h1>Nexo <span class="tag active">activo</span></h1>
  <p class="lead">Un distribuidor mayorista le mandaba planillas por FTP a 40 revendedores, una vez por día, y <strong>el stock de la mañana no servía a la tarde</strong>. Acá el ERP publica, los revendedores bajan el catálogo por WebSocket y quedan en la misma conexión recibiendo los cambios.</p>
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
  <p>Los datos del repositorio son placeholder: el sistema se publica sin exponer al cliente. Lo que está acá es la documentación interna del proyecto —con los ADR, el runbook y el contrato con el ERP incluidos—, y el código, las mediciones y los 356 tests son reales y se reproducen con los comandos del README.</p>
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
    circuit_foot="Un cambio de stock publicado a las 14:03 le llega a los revendedores conectados antes de las 14:03:01. Es lo que el archivo por FTP de la mañana no podía hacer."

    bp_head="El servidor no manda el siguiente lote hasta que vuelve la confirmación del anterior."
    bp_alt="Diagrama animado de contrapresión: el servidor envía un lote de 500 artículos, espera, y recién cuando llega el ack del revendedor manda el siguiente."
    bp_server="servidor"
    bp_client="revendedor"
    bp_batch_tag="lote"
    bp_batch="500 artículos"
    bp_ack_tag="confirmación"
    bp_held="esperando · nada sale"
    bp_foot="El buffer de escritura de un WebSocket acepta mucho más de lo que la red del otro lado puede tragar. Sin esta pausa, el servidor acumula megabytes en memoria por cada revendedor con enlace lento mientras sigue leyendo la base a toda velocidad. Del lado del cliente, la regla es confirmar <b>después</b> de haber persistido el lote, no al recibirlo."

    eng_head="La capa de aplicación referencia únicamente al dominio: cero paquetes, ni una mención a Entity Framework."
    eng_alt="Diagrama animado: los mismos puertos arriba y cuatro motores de base abajo turnándose, cada uno con la marca de 27 de 27 casos de contrato pasados."
    eng_ports="Puertos"
    eng_prod="producción"
    eng_demo="la demo"
    eng_pre="preproducción"
    eng_mem="En memoria"
    eng_dev="desarrollo"
    eng_foot="Los mismos 27 casos corren contra los cuatro, sin un <code>if</code> por proveedor. MySQL y PostgreSQL en contenedores reales en CI; sin Docker los casos se reportan omitidos, nunca verdes. El proveedor en memoria no usa una línea de EF Core: es el que prueba que los puertos no filtran nada."
%}

<div class="statline">
  <div class="stat"><span class="num">356</span><span class="lbl">tests en CI</span></div>
  <div class="stat"><span class="num">27<small>×4</small></span><span class="lbl">casos de contrato × motores</span></div>
  <div class="stat"><span class="num">68<small>ms</small></span><span class="lbl">de un cambio del ERP a 40 revendedores</span></div>
</div>

## Cambiar de base de datos es cambiar una línea

Acá esa frase la sostiene una suite, no un diagrama.

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

El cuarto es el que hace que la abstracción sea verificable y no declarativa: si
los puertos filtraran algo de EF, ese proyecto no compilaría.

Y encima corre `tests/Nexo.Persistence.ContractTests`, que ejecuta **los mismos
27 casos contra los cuatro proveedores**, sin un `if` por proveedor. Las clases
por motor son cuatro líneas y no definen ni un caso propio. MySQL y PostgreSQL
corren en contenedores reales en CI, con las migraciones versionadas aplicadas;
sin Docker los casos se reportan **omitidos, nunca verdes** — un test que pasa
sin haber corrido es peor que no tenerlo.

**La prueba llegó sola.** PostgreSQL se sumó cuando todo lo demás ya estaba
escrito: dos archivos de proveedor, sus migraciones, un fixture y una clase de
cuatro líneas. Los casos de contrato pasaron a la primera, y no se tocó ni un caso de uso,
ni un controlador, ni el handler del WebSocket.

## Contrapresión: el servidor espera

El buffer de escritura de un WebSocket acepta felizmente más de lo que la red del
otro lado puede tragar. Sin confirmación por lote, el servidor acumula megabytes
en memoria por cada revendedor con enlace lento mientras sigue leyendo la base a
toda velocidad.

Por eso no sale el siguiente lote hasta que vuelve el `ack` del anterior. Del
lado del cliente eso significa confirmar **después** de haber persistido el lote,
no al recibirlo, y está escrito en la documentación del protocolo porque es el
error que va a cometer el primer integrador.

El empalme entre la foto y el flujo es lo que hace que no se pierda nada: la
marca del diario se toma **antes** de leer el primer lote y viaja en el
encabezado. Si el catálogo cambia durante el recorrido, esos cambios llegan
igual por el diario después. Tomarla al final sería el bug.

## La política de acceso, y por qué el orden importa

Siete controles, en un orden que no es casual:

```
formato → clave → vigencia → whitelist → cuenta → scope → cupo
```

Dos posiciones no son negociables y tienen test propio:

- **La whitelist de IP va después de verificar el secreto.** Al revés, alguien
  que solo conoce el prefijo —que es público, viaja en los logs— prueba desde
  distintas redes y mapea los rangos permitidos de una cuenta ajena, sin tener
  ninguna credencial válida.
- **El cupo se consume al final.** Es el único paso con efecto lateral: antes de
  autenticar, cualquiera deja sin servicio a cualquiera mandando basura con el
  prefijo de la víctima.

El handshake del WebSocket corre **exactamente el mismo pipeline** que el filtro
de MVC. Una sola implementación de la política, dos transportes.

## La vista: una consola de operaciones

Es MVC de verdad —`AddControllersWithViews`, cinco controladores, vistas Razor—,
aunque siendo preciso: cuatro de los cinco sirven JSON, porque del otro lado hay
integraciones y no navegadores. La vista es una sola pantalla, y es la correcta.

<figure class="shot">
  <img src="{{ '/assets/img/nexo-panel.jpg' | relative_url }}" alt="Consola de operaciones de Nexo: cuatro indicadores arriba —una conexión activa, 59 pedidos por minuto, 7 rechazos por minuto y 4 milisegundos de latencia p95—; debajo, la actividad por revendedor con los pedidos y rechazos de cada cuenta, los rechazos agrupados por motivo (BadSecret, UnknownKey, ScopeNotGranted) y el feed de últimos hechos con la apertura de un stream y las credenciales rechazadas." loading="lazy" width="1500" height="823">
  <figcaption>La vista, corriendo. Los números salen de tráfico real contra la instancia local: consultas que pasan, credenciales inválidas que se rechazan y un snapshot en curso. El panel se alimenta del bus de hechos, no de la base de negocio.</figcaption>
</figure>

El panel muestra conexiones activas, actividad por revendedor, rechazos por
motivo y latencia p95, en vivo. **No consulta la base de negocio**: se alimenta
del mismo bus de hechos que emite el pipeline de autorización. Si el panel se
cae, la API ni se entera, y hay un test que lo verifica.

Va por Server-Sent Events y no por SignalR, que era el candidato natural. El
motivo es de instalación y no de tecnología: el panel corre detrás de la VPN,
donde no hay salida a internet para bajar el cliente de un CDN, y no hay build de
front en el repo. `EventSource` ya viene en el navegador, reconecta solo, y para
un flujo de una sola vía alcanza.

## Cupo por clave, compartido entre instancias

Cada credencial trae su propio cupo por minuto, y el paso que lo descuenta es el
último del pipeline. La cuenta vive en Redis, en una ventana deslizante sobre un
*sorted set*, y las cuatro operaciones —descartar lo que salió de la ventana,
contar, agregar, renovar el vencimiento— van en **un solo script Lua**. Partidas
en cuatro viajes, dos instancias leen 119 al mismo tiempo y las dos pasan.

Qué hacer si Redis no contesta es una opción del operador y no una decisión de
este código: `PerProcess` sigue atendiendo con el contador de cada proceso —el
default, porque el cupo protege la base del distribuidor y una caída de Redis no
tiene por qué ser una caída del servicio— y `Reject` devuelve 429 hasta que
vuelva. Cuál corresponde depende de si el cupo es una protección o una
obligación.

## Quién entra al panel

Con un proveedor de identidad cargado, el panel pide inicio de sesión por
**OpenID Connect** —*code flow* con PKCE, cookie de sesión de ocho horas y un
grupo exigible por configuración— y el token compartido deja de valer. Si
convivieran, el token sería una puerta trasera que se saltea el control de
identidad.

El nombre del claim que trae los grupos es configuración, porque cambia según el
proveedor: Entra ID manda `roles`, Okta suele mandar `groups`. El flujo completo
—descubrimiento, PKCE, login, intercambio del code, claims y cookie— corre en la
suite contra un Keycloak en un contenedor.

## Cómo se opera

Un servicio que alguien más va a mantener necesita más que endpoints:

- **`/health/live` y `/health/ready` separados**, y el de vida no depende de la
  base a propósito: si dependiera, una caída de MySQL haría que el orquestador
  mate y reinicie contenedores sanos en bucle.
- **Un runbook por síntoma del negocio**, no por componente: «a un revendedor no
  le llegan los cambios», «todos fallan de golpe», «el ERP no está publicando».
  Cada uno con los `curl` y las consultas concretas.
- **La especificación del protocolo y una guía de integración por cada tipo de
  consumidor** —el ERP que escribe y el revendedor que lee—, con el contrato de
  errores y los tamaños de lote recomendados.
- **Once ADR** con lo que se descartó y por qué, que es la parte útil seis meses
  después, cuando alguien propone justamente lo que ya se descartó.

## Bitácora

Lo que cambió, y por qué. Está acá porque la progresión dice más que una foto
final, y corto porque el detalle vive en los ADR.

| Qué pasó | Qué salió de ahí |
|---|---|
| El benchmark que escribí para respaldar un ADR **refutó sus dos afirmaciones**. | El ADR quedó corregido con la tabla medida, no borrado. El argumento real es 1 autorización contra 96, no la velocidad. ([ADR 0001](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0001-websocket-para-la-sincronizacion-completa.md)) |
| La misma búsqueda devolvía resultados distintos según el motor, y las fechas se corrían tres horas. | Normalización en el dominio, en columnas indexables. Ninguno de los dos se veía testeando contra un solo motor. ([ADR 0008](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0008-columnas-normalizadas-para-busqueda.md)) |
| Un test mostró que la configuración de `X-Forwarded-For` que copian todos los ejemplos deja pasar el header de cualquiera. | Sin proxies declarados, el procesamiento se apaga entero. Y una regla: un comentario que dice «esto es seguro porque X» es una hipótesis. ([ADR 0009](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0009-forwarded-headers-cierra-por-defecto.md)) |
| El supuesto de «un solo escritor» no lo hacía cumplir nada: dos lotes solapados le escondían un cambio al que lee. | Los escritores se serializan con un lock de fila, y hay un caso de contrato con dos escritores y un lector. ([ADR 0004](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0004-un-solo-escritor-en-el-diario-de-cambios.md)) |
| Probar el OIDC contra un proveedor real encontró que `ForbidAsync` redirigía en vez de devolver 403, y que el rol nunca se encontraba. | El flujo completo pasó a estar verificado, y el nombre del claim a ser configuración. ([ADR 0011](https://github.com/federicomoroz/nexo/blob/main/docs/adr/0011-identidad-del-panel-interno.md)) |
| La primera prueba de carga daba 0 de 40 conexiones. | El servidor no completaba el apretón de manos de cierre cuando cerraba el cliente. Dos clientes del repo lo tapaban con un `try/catch`. |
| La medición de propagación reportaba 227 ms y yo la citaba como «el costo de despachar a cuarenta». | Con la curva completa —1, 5, 10, 20 y 40 conexiones— la latencia no se mueve: el costo está en el camino de escritura y el reparto sale casi gratis. Un punto solo no separa el costo fijo del que escala. |

## Lo que no hace

- **No está integrado con un proveedor de identidad real del distribuidor.** Hay
  OIDC verificado contra Keycloak; no hay un tenant dado de alta.
- **Las mediciones son de localhost.** Lo que se sostiene afuera es la forma de
  la curva, no los milisegundos.
- **No hay demo desplegada.** Está el descriptor de despliegue y nada corriendo.
- **Corre en una sola instancia.** El cupo ya se comparte, pero el diario y el
  despertador de cambios son de proceso: con dos instancias, un cambio publicado
  en una no despierta a las conexiones de la otra.

Cada una está en los ADR con su alternativa descartada al lado. Un ADR sin
contras no se pensó.
