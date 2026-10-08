---
title: ArcaSim
description: "Los web services de ARCA para desarrollar y probar sin ARCA: 52 de los 53 vigentes, con sus WSDL, sus errores con los textos reales y sus reglas, y fallas a pedido. Para pasar a producción se cambian dos direcciones y el certificado."
permalink: /es/projects/arcasim/
---

<p class="crumbs"><a href="{{ '/es/tools/' | relative_url }}">{{ site.data.i18n[page.lang].services.back }}</a></p>

<section class="hero">
  <h1>ArcaSim <span class="tag active">activo</span></h1>
  <p class="lead"><strong>Los web services de ARCA, para desarrollar y probar sin ARCA.</strong> Una aplicación que factura usa su cliente real de ARCA contra ArcaSim mientras se desarrolla, en los tests y en las demos. Para pasar a producción <strong>se cambian dos direcciones y el certificado, no el código</strong>.</p>
  <div class="chip-row">
    <span class="tag">C#</span><span class="tag">.NET 8</span><span class="tag">ASP.NET Core</span>
    <span class="tag">SOAP</span><span class="tag">PostgreSQL</span><span class="tag">Docker</span>
    <span class="tag">xUnit</span><span class="tag">Testcontainers</span>
  </div>
  <p class="row-links">
    <a href="https://github.com/federicomoroz/arcasim" target="_blank" rel="noopener">Repo ↗</a>
    <a href="https://github.com/federicomoroz/arcasim/blob/main/docs/api.md" target="_blank" rel="noopener">Referencia de la API ↗</a>
    <a href="https://github.com/federicomoroz/arcasim/tree/main/docs/arca" target="_blank" rel="noopener">El estudio de la API de ARCA ↗</a>
  </p>
</section>

<div class="callout">
  <p class="callout-title">Sobre ARCA</p>
  <p>ArcaSim no tiene relación con ARCA. Los contribuyentes son ficticios, los CAE que otorga no tienen validez fiscal y sus tickets de acceso solo sirven contra ArcaSim. Lo que sí es de ARCA son los WSDL, los códigos de error y los textos, tomados de su documentación pública y de respuestas reales.</p>
</div>

<figure class="shot">
  <img src="{{ '/assets/img/arcasim-panel.jpg' | relative_url }}" alt="El panel de ArcaSim: ambiente, versión del manual y reloj; contribuyentes ficticios con sus puntos de venta; emisión de certificados y autorizaciones; fallas a pedido; cotizaciones, y la tabla de comprobantes emitidos con su CAE." loading="lazy" width="1425" height="1443">
  <figcaption>El panel. Lo que en ARCA hace WSASS (certificados y autorizaciones) lo hace ArcaSim, y además permite mover el reloj y provocar fallas.</figcaption>
</figure>

<div class="statline">
  <div class="stat"><span class="num">52</span><span class="lbl">de los 53 web services vigentes de ARCA, con sus WSDL oficiales</span></div>
  <div class="stat"><span class="num">byte a byte</span><span class="lbl">igual a una respuesta real de ARCA, salvo el número de CAE</span></div>
  <div class="stat"><span class="num">789</span><span class="lbl">tests, con el cliente generado del WSDL oficial, cada servicio contra su WSDL y PostgreSQL real</span></div>
</div>

## Para qué sirve

Facturar en Argentina pasa por ARCA: cada factura necesita su CAE, y para pedirlo la aplicación firma un pedido con un certificado digital, obtiene un ticket de acceso y recién ahí llama al servicio de factura electrónica. Probar eso contra ARCA exige tramitar un certificado de prueba con clave fiscal, y aun así no se puede provocar lo que más importa probar: que ARCA no responda, que rechace con un código concreto o que la respuesta se pierda después de otorgar el CAE.

La salida habitual es un simulador escrito dentro de cada aplicación, que devuelve un CAE inventado y nunca se parece del todo al protocolo real. ArcaSim hace lo contrario: **la aplicación usa desde el primer día el mismo cliente con el que va a facturar en producción**, y del otro lado responde un servicio que habla exactamente como ARCA.

## Solo con los endpoints

ArcaSim se usa como se usa ARCA: con dos URL y un certificado. No hay que cargar nada antes. Acepta cualquier certificado que tenga el CUIT en el DN, ya sea el que WSASS emitió para homologación o uno autofirmado con openssl, y el contribuyente y el punto de venta se crean la primera vez que se usan. Por eso funciona desde cualquier lenguaje y con cualquier cliente de ARCA: el repositorio trae un ejemplo que pide un CAE solo con openssl y curl, y una [referencia completa](https://github.com/federicomoroz/arcasim/blob/main/docs/api.md) de las operaciones, los errores y los escenarios de prueba.

```bash
docker run -d -p 7080:8080 -v arcasim-data:/data ghcr.io/federicomoroz/arcasim
```

Quien necesite reproducir los errores de registro de ARCA (certificado no autorizado, punto de venta que no es de web services) lo pasa a modo estricto.

## Cambiar ArcaSim por ARCA

<figure class="shot">
  <a href="{{ '/diagramas/arcasim/modulo.html' | relative_url }}"><img src="{{ '/assets/img/arcasim-modulo.gif' | relative_url }}" alt="Animación en cinco pasos: la aplicación firma el pedido y obtiene el ticket de acceso de ArcaSim; pide el CAE de una factura B; el panel provoca fallas; el reloj vence el ticket o cruza el 01/12/2026; para producción, las mismas llamadas van a ARCA cambiando dos direcciones y el certificado." loading="lazy" width="1200" height="750"></a>
  <figcaption>Del lado de la aplicación no cambia nada: el cliente, las llamadas y el manejo de errores son los mismos contra ArcaSim y contra ARCA.</figcaption>
</figure>

Para facturar, una aplicación necesita dos servicios:

- **WSAA**, el que entrega el ticket de acceso. Valida el pedido firmado en el mismo orden que ARCA, entrega el ticket con el formato exacto y una vida de 12 horas, y responde con los mismos errores, incluida la ventana que impide pedir otro ticket mientras el anterior sigue vigente.
- **WSFEv1**, el de factura electrónica, con sus 22 operaciones: el CAE de un comprobante o de un lote, el último número autorizado, la consulta de un comprobante emitido, las tablas de parámetros y el régimen de contingencia CAEA. Las validaciones del manual devuelven el código y el texto que devuelve ARCA, con sus faltas de tildes y sus dobles espacios.

El repositorio trae además **Arca.Client**, el cliente que usan las aplicaciones. No sabe nada de ArcaSim: firma el pedido, guarda el ticket hasta que vence, arma los comprobantes y distingue un rechazo, que se corrige y se reenvía, de una falla que conviene reintentar.

## No solo la factura electrónica

ARCA tiene más de cincuenta web services, y una empresa pocas veces usa solo WSFEv1: una exportadora pide sus CAE por WSFEXv1, un acopio de granos emite cartas de porte por WSCPE y liquida por WSLPG, un banco consulta deudas por SUD, un depósito fiscal informa sus movimientos a la aduana. **ArcaSim responde 52 de los 53 servicios vigentes**; el que falta no tiene contrato publicado.

Cada uno en su ruta, con su WSDL oficial y en el dialecto de su servidor: ASMX de .NET, Apache Axis2, CXF, JAX-WS o Spring-WS. Rechazan un ticket con sus propios códigos y textos, y no devuelven datos de muestra: aplican las reglas de su manual sobre lo que ArcaSim guarda.

- **Facturación**: factura con ítems, de exportación, bonos fiscales, turismo y seguros de caución, con su numeración, su CAE o CAEA y sus validaciones. Lo que autoriza cualquiera de ellos se puede constatar con WSCDC, como en ARCA.
- **Factura de Crédito MiPyME**: la cuenta corriente entre emisor y receptor (aceptar, rechazar, cancelar, ajustar) y, encima, los agentes de depósito y el sistema de circulación abierta.
- **Agro**: la carta de porte de punta a punta (autorizar, arribo, descarga, desvío, anulación), las liquidaciones de granos, hacienda, leche, tabaco y caña, el régimen tabacalero y los remitos de harina, carne y azúcar.
- **Organismos**: Ventanilla Electrónica, deuda de proveedores, apócrifos, juegos de azar, certificados de retención, declaraciones juradas, transferencias de automotores y el pago de VEPs, el único REST.
- **Aduana**: diez servicios de la DIA, de los precintos y los depósitos fiscales a las tiendas libres.

Los registros que ARCA llena por fuera de sus web services, como las deudas, los apócrifos o los despachos, arrancan con datos ficticios, y se reemplazan desde la API de administración antes de un test.

## La respuesta que se pierde

<figure class="shot">
  <a href="{{ '/diagramas/arcasim/recuperacion.html' | relative_url }}"><img src="{{ '/assets/img/arcasim-recuperacion.gif' | relative_url }}" alt="Animación en seis pasos: el cliente pregunta el último número y pide el CAE del 42; ARCA lo otorga y lo guarda pero la conexión se corta; reenviar a ciegas daría 10016; el cliente consulta el 42 con FECompConsultar y recupera el CAE sin duplicar nada." loading="lazy" width="1200" height="750"></a>
  <figcaption>El procedimiento que indica el manual de ARCA para los errores de comunicación, provocado a pedido desde el panel.</figcaption>
</figure>

ARCA no es idempotente: si la respuesta a un pedido de CAE se pierde y la aplicación reenvía el mismo comprobante, ARCA lo rechaza porque ese número ya figura como emitido. Con ARCA real esta situación casi no se puede provocar. **ArcaSim la produce a pedido**: otorga el CAE, lo guarda y corta la conexión antes de responder. Arca.Client la resuelve como indica el manual, consultando el comprobante antes de reintentar.

Desde el panel también se tira el servicio, se le agrega una demora, se rechaza el próximo comprobante con el código que se elija y se mueve el reloj: vencer el ticket, salirse del rango de fechas permitido o cruzar el 01/12/2026, cuando la condición frente al IVA del receptor pasa a ser obligatoria.

## Saturación y cuellos de botella

<figure class="shot">
  <img src="{{ '/assets/img/arcasim-trafico.jpg' | relative_url }}" alt="La sección de tráfico del panel: dos medidores de saturación, uno por servicio. El de WSFEv1 marca 58,3 %: de 12 pedidos en el último minuto, 7 rechazados, con 805 ms de promedio y 1.281 ms de p95, con dos atendidos a la vez, 400 ms cada uno y tres lugares en la cola." loading="lazy" width="1245" height="384">
  <figcaption>Doce pedidos al mismo tiempo, con dos atendidos a la vez y tres lugares en la cola: cinco salen, siete reciben 503, y el medidor lo marca.</figcaption>
</figure>

Un servicio saturado tarda o deja de atender. ArcaSim lo reproduce sobre sus mismas URL, con un límite de pedidos por minuto, una capacidad (cuántos atiende a la vez y cuánto tarda cada uno) y una cola. Lo que no entra recibe HTTP 503, como un balanceador saturado, y el cliente tiene que reintentar. El medidor, portado del de [Rate Guardian]({{ '/es/tools/#rate-guardian' | relative_url }}), marca qué parte de los pedidos del último minuto quedó afuera, y un registro en vivo muestra cada ticket, cada CAE y cada rechazo.

## Igual que ARCA, verificado

| Nivel | Qué coincide | Cómo se verifica |
|---|---|---|
| Contrato | Rutas, WSDL oficiales, operaciones, namespaces, SOAP 1.1 y 1.2 | El cliente que genera `dotnet-svcutil` a partir del WSDL de ARCA, sin tocarlo, pide un CAE contra ArcaSim en SOAP 1.1 y 1.2 |
| Bytes | Una sola línea con el encabezado `FEHeaderInfo`, `<CAE />` vacío, importes sin ceros de relleno, el literal `NULL` en fechas vacías; los faults de Apache Axis en WSAA | Un CAE aprobado y un reenvío rechazado coinciden byte a byte con respuestas grabadas de ARCA, salvo el número de CAE |
| Errores | Los códigos del manual y los textos reales donde se conocen | Una tabla de cobertura que sale del código |
| Comportamiento | Numeración correlativa por CUIT, punto de venta y tipo; un lote se corta en el primer rechazo; ticket de 12 horas | Tests de escenarios |
| Los demás servicios | Cada respuesta, válida contra el WSDL de ARCA; el ticket rechazado con los códigos y textos de cada servicio | Un test por operación de cada servicio, además de los flujos principales de cada uno |

## Lo usa

<div class="cards">
  <article class="card">
    <div class="card-header"><a class="card-title" href="{{ '/es/projects/comanda/' | relative_url }}">Comanda</a></div>
    <div class="card-desc"><p>La facturación de Comanda pide los CAE con Arca.Client. En modo homologación habla con ArcaSim, y sus tests recorren el camino real: CAE otorgado, rechazo de ARCA con su motivo en la caja y ARCA caída con la factura esperando en la cola.</p></div>
    <p class="row-links"><a href="{{ '/es/projects/comanda/' | relative_url }}">Case study</a></p>
  </article>
</div>

## Para técnicos

- **Una capa SOAP propia en lugar de CoreWCF.** Los servicios de ARCA corren en seis servidores distintos: ASMX de .NET, Apache Axis y Axis2, CXF, JAX-WS y Spring-WS, cada uno con sus rarezas, y un framework genérico las normaliza. WSFEv1 lee y escribe con `XmlSerializer`, el mismo serializador que usa ASMX: acepta los elementos en cualquier orden, ignora los desconocidos y responde con el mismo formato.
- **Un motor que lee los WSDL de ARCA.** Fuera de WSAA y WSFEv1, ningún servicio tiene un contrato escrito a mano: el motor lee el WSDL y los XSD oficiales, valida el ticket y responde en el dialecto del servicio. Un catálogo dice cómo rechaza cada uno un ticket y qué valores fijos manda; las reglas de un servicio son una clase que se registra sola, y su estado va a un almacén de documentos, en memoria o en PostgreSQL.
- **Reglas como datos.** Cada validación es una regla con el código que lleva al pedir un CAE y el que lleva al informar un comprobante de contingencia, donde muchas observan en lugar de rechazar. Si rechaza u observa, y el texto, salen de la tabla del manual, extraída del estudio a un archivo de datos.
- **Perfiles.** El ambiente (homologación o producción) cambia los textos del encabezado y la ventana del ticket; la versión del manual (4.7 o 4.8) sigue por defecto la fecha del reloj de ArcaSim.
- **Un bus de eventos entre las partes.** El control de tráfico, WSAA y WSFEv1 publican lo que pasa: pedido atendido o rechazado, ticket emitido, comprobante autorizado o rechazado. El medidor y el registro en vivo solo escuchan; nadie sabe que existen. La API de administración son controllers MVC, uno por recurso.
- **Almacenamiento detrás de puertos.** En memoria para los tests de una aplicación, que arranca en milisegundos, o PostgreSQL para un equipo o una CI. La misma suite de contrato corre contra los dos.
- **Claves que sobreviven a un reinicio.** La autoridad certificante propia y la clave que firma los tickets se guardan en disco: una aplicación guarda su ticket 12 horas y no tiene por qué perderlo si ArcaSim se reinicia.

Antes de escribir código se estudió la API pública de ARCA completa: WSAA, WSFEv1 y sus 496 validaciones, cada uno de los demás servicios con sus códigos, el catálogo y la normativa vigente, con los WSDL oficiales y respuestas reales. Está en el repositorio, en [`docs/arca/`](https://github.com/federicomoroz/arcasim/tree/main/docs/arca).

```bash
docker run -d -p 7080:8080 ghcr.io/federicomoroz/arcasim   # la imagen publicada, en memoria
docker compose up -d                                       # desde el repositorio, con PostgreSQL
dotnet test
```
