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
  <p class="callout-title">Sobre el escenario</p>
  <p>El distribuidor y su red de revendedores son un escenario construido, y en el repo está dicho. Lo escribí como se escribiría la documentación interna de ese proyecto —con los ADR, el runbook y el contrato con el ERP incluidos— porque ese era justamente el ejercicio: ver si podía sostener un sistema completo, no un endpoint de demostración. El código, las mediciones y los 343 tests son reales y se reproducen con los comandos del README.</p>
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
    eng_alt="Diagrama animado: los mismos puertos arriba y cuatro motores de base abajo turnándose, cada uno con la marca de 26 de 26 casos de contrato pasados."
    eng_ports="Puertos"
    eng_prod="producción"
    eng_demo="la demo"
    eng_pre="preproducción"
    eng_mem="En memoria"
    eng_dev="desarrollo"
    eng_foot="Los mismos 26 casos corren contra los cuatro, sin un <code>if</code> por proveedor. MySQL y PostgreSQL en contenedores reales en CI; sin Docker los casos se reportan omitidos, nunca verdes. El proveedor en memoria no usa una línea de EF Core: es el que prueba que los puertos no filtran nada."
%}

<div class="statline">
  <div class="stat"><span class="num">343</span><span class="lbl">tests en CI</span></div>
  <div class="stat"><span class="num">26<small>×4</small></span><span class="lbl">casos de contrato × motores</span></div>
  <div class="stat"><span class="num">4</span><span class="lbl">bugs que encontraron los tests</span></div>
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
| PostgreSQL | la demo desplegada | EF Core, migraciones propias |
| SQLite | preproducción | EF Core, migraciones propias |
| En memoria | desarrollo y tests | a mano, **sin una línea de EF** |

El cuarto es el que hace que la abstracción sea verificable y no declarativa: si
los puertos filtraran algo de EF, ese proyecto no compilaría.

Y encima corre `tests/Nexo.Persistence.ContractTests`, que ejecuta **los mismos
26 casos contra los cuatro proveedores**, sin un `if` por proveedor. Las clases
por motor son cuatro líneas y no definen ni un caso propio. MySQL y PostgreSQL
corren en contenedores reales en CI, con las migraciones versionadas aplicadas;
sin Docker los casos se reportan **omitidos, nunca verdes** — un test que pasa
sin haber corrido es peor que no tenerlo.

**La prueba llegó sola.** PostgreSQL se sumó cuando todo lo demás ya estaba
escrito: dos archivos de proveedor, sus migraciones, un fixture y una clase de
cuatro líneas. Los 26 casos pasaron a la primera, y no se tocó ni un caso de uso,
ni un controlador, ni el handler del WebSocket.

## Lo que la suite encontró antes de producción

No es una lista decorativa. Son bugs que estaban en el código.

**La búsqueda daba resultados distintos según el motor.** `string.Contains` se
traduce a `instr()` en SQLite, que distingue mayúsculas; MySQL con su collation
por defecto, no. En producción eso aparece como «a veces no encuentra el
artículo», y distinto según el ambiente, que es de los reportes más difíciles de
perseguir. El arreglo no fue un parche: la normalización vive en el dominio y se
guarda en columnas propias, que además son indexables —`UPPER(nombre) LIKE ...`
no lo es—.

**Las fechas se corrían tres horas.** MySQL no tiene tipo con offset y el driver
lo aplana en silencio. El mismo dato leído en una máquina argentina y en un
contenedor UTC daba dos instantes distintos.

Ninguno de los dos se habría encontrado testeando contra un solo motor.

## El benchmark refutó mi propio ADR

Escribí un ADR justificando por qué el catálogo baja por WebSocket y no por HTTP
paginado. Argumenté que ahorraba unos cien viajes de red y la mitad del payload.

Después escribí la herramienta que lo mide. Sobre 48.000 artículos, contra MySQL:

| Método | Viajes | Autenticaciones | Bytes | Tiempo |
|---|---|---|---|---|
| HTTP paginado | 96 | **96** | 9,9 MB | 1,02 s |
| WebSocket | **97** | **1** | 10,0 MB | 0,79 s |

Las dos afirmaciones eran falsas. El WebSocket hace **un viaje más**, no cien
menos —porque mi propio diseño espera confirmación por lote, así que hay un ida y
vuelta por lote igual que en la paginación—. Y el payload es el mismo.

No borré el ADR. Le agregué una sección «Corrección» que dice que la
justificación original estaba mal, puse la tabla medida, y reescribí el argumento
con lo único que la medición respalda: **96 autenticaciones contra 1**, porque
cada pedido HTTP paga el pipeline entero y el WebSocket lo paga una vez en el
handshake. Y el motivo de verdad, que no aparece en ninguna tabla de velocidad:
terminado el snapshot, la misma conexión queda escuchando los deltas.

Los tiempos están medidos en localhost y el documento lo dice con esas palabras.
No se extrapolan a un revendedor del otro lado del país.

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

### El agujero que encontró un test

La whitelist de IP depende de saber la IP real detrás del proxy, que llega en
`X-Forwarded-For`. Yo había dejado las listas de proxies vacías por defecto, con
un comentario que decía: «con la lista vacía el header se ignora, que es el
comportamiento seguro».

Escribí el test que manda un `X-Forwarded-For` falso sin proxies configurados y
espera un 403. Dio 200.

`ForwardedHeadersMiddleware` **solo controla el origen del header si hay algo** en
`KnownProxies` o `KnownNetworks`. Con las dos listas vacías —el default— le cree
a cualquiera. O sea: en la configuración por defecto, cualquiera con una
credencial válida se salteaba la whitelist con un header inventado.

Ahora, sin proxies declarados, el procesamiento del header se apaga entero. La
consecuencia buscada es ruidosa: mal configurado detrás de un proxy, toda la red
queda afuera de golpe, y es imposible no darse cuenta.

Lo que saqué de ahí no es «hay que testear todo». Es que **un comentario que dice
«esto es seguro porque X» es una hipótesis**, y esta estuvo mal durante días sin
molestar a nadie.

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

## Las cuatro deudas, y cómo se pagaron

Este apartado listaba cuatro limitaciones con la salida anotada al lado. Están
cerradas. Interesa menos el anuncio que lo que apareció al hacerlo, que en tres
de los cuatro casos no era lo previsto:

**El cupo era por proceso.** Con dos instancias detrás de un balanceador, cada
una aplicaba el suyo y el techo real se duplicaba. Ahora se comparte en Redis:
ventana deslizante sobre un *sorted set*, y las cuatro operaciones —descartar lo
viejo, contar, agregar, renovar el vencimiento— en un solo script Lua, porque
partidas en cuatro viajes dos instancias leen 119 al mismo tiempo y pasan las
dos. Con Redis caído el servicio **sigue atendiendo** contra el contador en
memoria y deja un aviso en el log: se elige atender de más antes que no atender,
y queda escrito en el ADR para que sea una decisión y no un descubrimiento.

**No había prueba de carga.** Ahora hay una herramienta que mide dos cosas: N
revendedores bajando el catálogo completo a la vez, y cuánto tarda un cambio del
ERP en llegar a N conexiones suscriptas. Contra 8.000 artículos y 40 conexiones,
en localhost: **40 de 40** completas, p50 0,30 s por conexión, y el cambio
publicado llega a las cuarenta con **p50 227 ms**.

Lo interesante no es el número. La primera corrida dio **0 de 40**, y bisecando
con la otra herramienta apareció un bug de verdad: cuando el que cerraba primero
era el cliente, el servidor nunca completaba el apretón de manos de cierre. Los
otros dos clientes del repo lo venían tapando con un `try/catch` alrededor del
cierre, que es tratar el síntoma en el lado equivocado.

**El panel se protegía con un token compartido.** Ahora, cuando hay un proveedor
de identidad cargado, pide inicio de sesión por OpenID Connect —*code flow* con
PKCE, grupo exigible por configuración— y el token deja de valer: si conviviera
sería una puerta trasera que se saltea el control de identidad, y alguien la
usaría por comodidad el primer día. Escribirlo obligó a corregir el motivo que yo
mismo había anotado: no era la exposición a internet. Un token compartido no dice
**quién** revocó una clave, no se revoca por persona, y termina pegado en un chat
interno. Las tres cosas pasan igual detrás de la VPN.

**La búsqueda no ignoraba acentos.** Ahora sí, verificado por los mismos 26 casos
contra los cuatro motores. Dos sorpresas en el camino. La primera: la forma de
libro —descomponer a `FormD` y descartar las marcas combinantes— **no hace nada**
en este servicio y tampoco falla; el proyecto declara `InvariantGlobalization`
para no depender de la versión de ICU del sistema, y eso desactiva la
normalización Unicode en silencio. La reemplaza una tabla explícita. La segunda:
la eñe no es un acento —«caña» y «cana» son dos artículos distintos en una
ferretería— y el caso que lo fija **falló solo en MySQL**, que con su collation
por defecto vuelve a planchar una columna que el código ya había dejado canónica.
El arreglo entra por una interfaz que cada motor implementa, no por un `if` sobre
el nombre del proveedor.

## Lo que sigue sin resolver

- **El flujo OIDC no está probado de punta a punta.** Acá no hay un Entra ID
  contra el cual hacerlo. Lo verificado es la decisión propia —qué modo se elige,
  qué pasa con el token, qué pasa con alguien autenticado sin el grupo—; el
  apretón de manos con el proveedor es el de ASP.NET Core y lo doy por bueno.
- **Los números de carga son de localhost.** Miden el costo del servidor en
  despachar a N conexiones, no el viaje hasta el revendedor, que se suma.
- **Con Redis caído el cupo se degrada**, no falla. Es la decisión de arriba, y
  es discutible.
- **El diario de cambios asume un solo escritor.** El ERP publica secuencial. Con
  dos fuentes de escritura la marca de agua deja de ser monótona y el mecanismo
  de reanudación se cae.

Los ocho puntos están en los ADR. Un ADR sin contras no se pensó.
