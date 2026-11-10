---
layout: manual
manual: personal
title: "Personal · Manual de Fornu"
description: "El equipo con su PIN, sus roles y su paga, los permisos y cuáles se prestan con PIN, y el módulo Personal: presentismo, asistencia, horarios, liquidación y adelantos."
permalink: /es/projects/fornu/manual/personal/
---

## Equipo {#equipo}

Es la lista de la gente que trabaja en el local. Cada persona entra y ficha con su PIN en la tablet de la cocina o en su celular, sin usar tu contraseña. Lo que puede hacer en Fornu lo dicen sus roles: alguien con un rol sin permisos solo ficha la entrada y la salida.

<p class="perm"><span>Quién puede:</span> <span class="tag">Equipo</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-equipo.jpg' | relative_url }}" alt="La lista Equipo con cinco personas: sus roles con color, el estado, lo que pueden hacer en Fornu, cuánto cobran y si tienen PIN cargado" loading="lazy" width="1440" height="520">
  <ol class="marks">
    <li><b>Agregar</b>: suma una persona al equipo.</li>
    <li><b>Roles</b>: los roles de cada uno, con su color. Si no tiene ninguno dice «Sin rol».</li>
    <li><b>En Fornu</b>: lo que puede hacer, sumando los permisos de todos sus roles. Quien no tiene permisos dice «Solo ficha».</li>
    <li><b>Cobra</b>: cómo y cuánto cobra, por ejemplo «$ 4.200 por hora». Lo usa la liquidación.</li>
    <li><b>PIN</b>: «Cargado» o «Falta». El botón <b>PIN</b> de la fila le pone uno nuevo.</li>
  </ol>
  <figcaption>El equipo de la demo. Las columnas <b>Estado</b> y <b>Cobra</b> aparecen con el módulo Personal.</figcaption>
</figure>

### Sumar a alguien

1. Tocá **Agregar**.
2. Escribí el **Nombre**, como lo llaman en el local.
3. Si ya tenés su PIN, cargalo en **PIN (opcional)**: entre 4 y 6 números. Se puede cargar después.
4. Elegí sus **Roles**. El primero que elijas es el que muestran los horarios y el presentismo.
5. Con el módulo Personal, fijate el **Estado** (arranca en **Activo**) y elegí **Cómo cobra**: **Por hora**, **Por día** o **Por mes**. Escribí el monto en **Cuánto**.
6. Tocá **Guardar**. Aparece «Guardado: Lucía».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-persona.jpg' | relative_url }}" alt="El formulario para sumar a una persona, con el PIN cargado, los roles para elegir, el estado, la fecha desde, y cómo y cuánto cobra" loading="lazy" width="620" height="900">
  <ol class="marks">
    <li><b>PIN (opcional)</b>: de 4 a 6 números, para fichar y entrar.</li>
    <li><b>Roles</b>: tocá cada uno que corresponda. Pasando el mouse se ve qué permite cada rol.</li>
    <li><b>Estado</b> y <b>Desde</b>: si trabaja o no, y desde cuándo.</li>
    <li><b>Cómo cobra</b> y <b>Cuánto</b>: la hora, el día o el mes, según cómo cobra.</li>
  </ol>
  <figcaption>El formulario de una persona nueva, ya bajando hasta la paga.</figcaption>
</figure>

Lo que significa cada campo:

| Campo | Qué es |
|---|---|
| **Estado** | Dónde está parada la persona: **Activo**, **A prueba**, **Extra**, **Inactivo**, **Baja** o los que armes. Si el estado es de los que no trabajan, su PIN deja de andar. |
| **Desde** | Si deja de trabajar, el último día que trabajó. El presentismo completa el resto del mes. |
| **DNI (opcional)**, **Teléfono (opcional)**, **En caso de emergencia (opcional)** | Datos para tener a mano. |
| **Cómo cobra** | **No por su tiempo** (el que viene elegido), **Por hora**, **Por día** o **Por mes**. |
| **Cuánto** | La hora, el día o el mes, según cómo cobra. Aparece cuando cobra por su tiempo. |
| **Por envío** | Aparece si alguno de sus roles tiene el permiso **Mensajería**. Se le suma por cada pedido propio que entregó. |

Para cambiar algo de una persona, tocá su fila, cambiá lo que haga falta y tocá **Guardar**. En la compu, <kbd>Ctrl</kbd> + <kbd>Enter</kbd> guarda cualquier formulario.

### Ponerle o cambiarle el PIN

1. En la fila de la persona, tocá **PIN**.
2. Escribí el **PIN nuevo**: entre 4 y 6 números.
3. Tocá **Guardar**. Aparece «PIN guardado».
{: .steps}

<div class="callout tip"><p class="callout-title">Consejo</p><p>Dale el PIN en persona, no por mensaje. Con ese PIN ficha y entra a Fornu en cualquier dispositivo vinculado del local.</p></div>

<div class="callout"><p class="callout-title">Importante</p><p>El PIN de alguien lo cambia quien tiene todos los permisos que tiene esa persona. Tampoco se puede dar un rol con permisos que uno no tiene. Y los roles y la paga propios los cambia otra persona: «Tus propios roles los cambia otra persona.»</p></div>

### Cuando alguien deja de trabajar

Las personas no se borran, porque el presentismo y los pagos de meses anteriores las siguen nombrando. Con el módulo Personal:

1. Tocá la fila de la persona.
2. En **Estado**, elegí **Inactivo** o **Baja**.
3. En **Desde**, poné el último día que trabajó.
4. Tocá **Guardar**.
{: .steps}

Desde ese momento su PIN deja de andar y su nombre sale de la lista de los dispositivos. Con **Inactivo**, el presentismo completa el resto del mes con el código de baja (**X**). Los estados se arman en [Configuración de personal](#estados).

Cómo ficha cada uno con su PIN está en [En la cocina y en la calle]({{ '/es/projects/fornu/manual/cocina-y-reparto/' | relative_url }}#fichar). Fichar es parte de lo básico: anda con o sin el módulo Personal.

## Configuración de personal {#roles}

Acá se arman las listas del equipo como las usa el local: los roles y lo que puede hacer cada uno, y debajo lo que suma el módulo Personal (estados, códigos del presentismo, turnos y el mes de la planilla). La pestaña dice **Configuración** y el título de la página, **Configuración de personal**.

<p class="perm"><span>Quién puede:</span> <span class="tag">Equipo</span> <span class="tag">Administración</span> (los roles)</p>

El bloque **Roles** lo ve solo la Administración de la cuenta. Quien tiene el permiso Equipo ve las listas del módulo Personal.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-roles.jpg' | relative_url }}" alt="El bloque Roles con seis roles: Cocina, Mensajería, Encargado/a, Mozo, Adicionista y Caja, lo que puede cada uno y cuántas personas lo tienen" loading="lazy" width="1440" height="555">
  <ol class="marks">
    <li><b>Agregar</b>: arma un rol nuevo.</li>
    <li><b>Puede</b>: los permisos del rol. Un rol sin permisos dice «Solo ficha».</li>
    <li><b>Personas</b>: cuántas personas tienen ese rol.</li>
  </ol>
  <figcaption>Los roles de la demo, con el Salón prendido.</figcaption>
</figure>

### Armar un rol

1. En **Roles**, tocá **Agregar**.
2. Poné el **Nombre** como lo dicen en el local: Parrillero, Moza, Caja del local. Hasta 40 letras.
3. Elegí el **Color**. Es el punto que acompaña al rol en el equipo, los horarios y el presentismo.
4. En **Puede**, tocá los permisos que lleva. Arriba están los de **Básico** y debajo los de cada módulo prendido.
5. Tocá **Guardar**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-rol-editor.jpg' | relative_url }}" alt="El formulario de un rol nuevo: nombre, color y los permisos agrupados en Básico y en cada módulo" loading="lazy" width="620" height="900">
  <ol class="marks">
    <li><b>Color</b>: el del rol en todas las pantallas del equipo.</li>
    <li><b>Básico</b>: los permisos que tiene toda cuenta.</li>
    <li>Los permisos de cada módulo prendido, cada grupo con su nombre.</li>
  </ol>
  <figcaption>Pasando el mouse por un permiso se lee qué deja hacer.</figcaption>
</figure>

Un rol sin ningún permiso sirve para quien tiene que fichar pero no usa Fornu: toca su nombre, pone el PIN y queda fichado. La lista completa de permisos, con lo que deja hacer cada uno, está en el [índice del manual]({{ '/es/projects/fornu/manual/' | relative_url }}#permisos).

### Permisos que van juntos y los que se prestan con PIN {#prestar}

Algunos permisos no tienen sentido sin otro. Si tocás **Anular lo mandado**, se marca solo **Atender mesas**, y si después sacás **Atender mesas**, se van con él los que lo necesitan.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-requiere.jpg' | relative_url }}" alt="Los permisos del Salón en el editor de roles: Anular lo mandado está elegido y Atender mesas se marcó con él" loading="lazy" width="620" height="270">
  <ol class="marks">
    <li><b>Anular lo mandado</b>: el permiso que se tocó.</li>
    <li><b>Atender mesas</b>: se marcó solo, porque el otro va con él.</li>
  </ol>
  <figcaption>Elegir un permiso marca también el que necesita.</figcaption>
</figure>

Algunos permisos se pueden prestar en el momento. Si a alguien le falta uno de estos, otra persona que lo tiene pone su PIN y la acción sale. Vale para esa sola acción y por dos minutos, y queda anotado quién autorizó, por ejemplo «Anulado por Sofía (autorizó Lucía)». Cómo se pide está en [Salón: mesas, mostrador y cobro]({{ '/es/projects/fornu/manual/salon/' | relative_url }}#autorizar).

| Permiso | Va con | Se presta con PIN |
|---|---|---|
| **Ver lo esperado** | Caja | No |
| **Recontar la caja** | Caja | Sí |
| **Asignar quién atiende** | Atender mesas | Sí |
| **Mover mesas** | Atender mesas | Sí |
| **Anular lo mandado** | Atender mesas | Sí |
| **Descontar e invitar** | Atender mesas | Sí |
| **Cobrar mesas** | Atender mesas | No |
| **Deshacer cobros** | Cobrar mesas | Sí |
| **Cancelar mesas** | Atender mesas | Sí |

Los demás permisos no piden otro y no se prestan. Qué acción de la mesa pide el PIN, por ejemplo anular una línea o pasar la mesa a otro mozo, está en la misma página del Salón.

### Los roles con los que arranca la cuenta {#roles-de-entrada}

Una cuenta nueva trae tres roles, que se pueden cambiar como cualquier otro:

| Rol | Puede |
|---|---|
| **Cocina** | Cocina |
| **Mensajería** | Mensajería |
| **Encargado/a** | Cocina, Pedidos, Stock, Caja, Ver lo esperado, Recontar la caja, Gastos y Dispositivos |

**Encargado/a** no trae Equipo, Ajustes ni los permisos del módulo Personal: dáselos si el encargado arma el equipo o liquida sueldos.

Cuando se prende el Salón llegan tres roles sugeridos, salvo que algún rol ya tenga un permiso del Salón:

| Rol | Puede |
|---|---|
| **Mozo** | Atender mesas y Mover mesas |
| **Adicionista** | Atender mesas, Asignar quién atiende, Mover mesas, Anular lo mandado, Descontar e invitar y Cobrar mesas |
| **Caja** | Atender mesas, Cobrar mesas, Descontar e invitar, Anular lo mandado, Deshacer cobros y Cancelar mesas |

<div class="callout"><p class="callout-title">Importante</p><p>Los roles no se borran: se apagan con <b>Activo</b>, que aparece al editarlos. Un rol apagado deja de dar sus permisos en el acto. Los cambios en un rol llegan enseguida a quien está usando Fornu, y quien se queda sin permisos sale de la sesión.</p></div>

Si se apaga un módulo, sus permisos desaparecen del editor pero quedan guardados en cada rol, y vuelven cuando el módulo se prende de nuevo.

### El mes del presentismo {#mes}

Esta tarjeta y las tres que siguen las trae el módulo Personal. Acá se dice cuándo empieza cada mes de la planilla y qué se completa solo.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-mes.jpg' | relative_url }}" alt="La tarjeta El mes del presentismo: el día en que empieza el mes, cómo se prorratea el sueldo y los cuatro códigos que se completan solos" loading="lazy" width="1440" height="275">
  <ol class="marks">
    <li><b>El mes empieza el día</b>: del 1 al 28. Con 26, octubre va del 26 de septiembre al 25 de octubre.</li>
    <li><b>El sueldo mensual se prorratea por</b>: <b>Los días del mes</b> o <b>30 días</b>, para los períodos que toman parte de un mes.</li>
    <li><b>Fichó a horario</b>, <b>Fichó tarde</b>, <b>Franco</b> y <b>Baja</b>: el código que se escribe solo en cada caso, o «Nada: lo carga el encargado».</li>
    <li><b>Guardar</b>: esta tarjeta guarda aparte. Se enciende cuando cambiás algo.</li>
  </ol>
  <figcaption>Los valores con los que arranca una cuenta.</figcaption>
</figure>

### Estados {#estados}

Dicen dónde está parada cada persona. Si el estado no trabaja, su PIN deja de andar. Si además completa con baja, el presentismo llena el resto del mes desde el día siguiente a la fecha **Desde**.

| Estado | Trabaja | Completa con baja |
|---|---|---|
| **Activo** | Sí | No |
| **A prueba** | Sí | No |
| **Extra** | Sí | No |
| **Inactivo** | No | Sí |
| **Baja** | No | No |

Para sumar uno, tocá **Agregar** en la tarjeta y completá **Nombre**, **Color**, **Trabaja** y **Completa con baja**. Si hay personas en un estado, primero pasalas a otro para cambiarle **Trabaja**.

### Códigos del presentismo {#codigos}

Son lo que se escribe en cada día de la planilla. **Cuenta como** decide qué paga la liquidación, y **Suma al total de** dice en qué columna del mes suma.

| Código | Significa | Cuenta como | Suma a |
|---|---|---|---|
| **P** | Presente | Presente | Su propio total |
| **PP** | Doble turno | Presente | P |
| **T** | Llegó tarde | Tarde | Su propio total |
| **A** | Ausente | Ausente | Su propio total |
| **AJ** | Ausente justificado | Ausente | A |
| **F** | Franco | No cuenta (franco, baja) | Su propio total |
| **X** | Ya no trabaja | No cuenta (franco, baja) | Su propio total |

Un código lleva hasta 4 letras o números, sin espacios, y se guarda en mayúsculas. Un código que se completa solo en la planilla no se puede apagar hasta elegir otro en **El mes del presentismo**.

### Turnos {#turnos}

Son los turnos que el local llama por su nombre. Con un turno **AM** de 9 a 17, en Horarios alcanza con escribir AM, o AM, PM para un turno cortado.

1. En **Turnos**, tocá **Agregar**.
2. Poné el **Nombre**, solo con letras: los números se leen como horas.
3. Elegí **Entra** y **Sale**. Si la salida es antes que la entrada, el turno pasa la medianoche: de 20 a 2.
4. Tocá **Guardar**.
{: .steps}

Sin turnos con nombre, los horarios se escriben con sus horas, como 9-17.

## Presentismo {#presentismo}

Es la planilla del mes: una fila por persona, un casillero por día y los totales al final. Lo que se fichó, los francos del horario y las bajas se completan solos, y lo que escribe el encargado manda, también para la paga.

<p class="perm"><span>Quién puede:</span> <span class="tag">Presentismo</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-presentismo.jpg' | relative_url }}" alt="La planilla de presentismo de noviembre con cinco personas, días completados solos con P y F, y la columna de totales" loading="lazy" width="1440" height="510">
  <ol class="marks">
    <li>El mes anterior, <b>Este mes</b> y el siguiente. El mes lleva el nombre del mes en que termina.</li>
    <li><b>Imprimir</b>: la planilla del mes en papel.</li>
    <li>El borde punteado marca lo que «se completó solo».</li>
    <li>Un día: tocalo para cargarle un código.</li>
    <li>Los totales de cada código y <b>Trab.</b>, los días trabajados.</li>
  </ol>
  <figcaption>La planilla de la demo. En el teléfono se desliza de costado y abre en el día de hoy.</figcaption>
</figure>

### Marcar un día

1. Tocá el casillero del día en la fila de la persona.
2. Tocá el código. Se guarda en el momento.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-presentismo-dia.jpg' | relative_url }}" alt="La ventana de un día con los siete códigos para elegir: Presente, Doble turno, Llegó tarde, Ausente, Ausente justificado, Franco y Ya no trabaja" loading="lazy" width="620" height="262">
  <figcaption>Un toque en el código y queda cargado.</figcaption>
</figure>

Si el día ya tenía un código escrito a mano, abajo aparece **Borrar lo cargado: vuelve a mostrar lo fichado**.

### Qué se completa solo

- Un día que la persona fichó muestra el código de **Fichó a horario** (P), o el de **Fichó tarde** (T) si llegó después de la tolerancia de [Ajustes › Configuración]({{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#configuracion).
- Los días libres de su horario muestran **Franco** (F).
- Después de pasar a un estado que completa con baja, el resto del mes muestra **Baja** (X).
- Lo escrito a mano le gana a lo fichado.

Un día marcado como trabajado sin nada fichado cuenta las horas de su horario. Así, un local que no ficha puede pagar desde la planilla. **PP** cuenta como un día trabajado y suma al total de **P**.

En la planilla aparecen las personas con un estado que trabaja, y cualquiera que tenga algo cargado en ese mes. **Imprimir** saca el mes con el nombre de la cuenta, los casilleros, los totales y la lista de códigos.

<div class="callout"><p class="callout-title">Importante</p><p>Los días que ya se pagaron quedan cerrados: «El 03/11 ya se le pagó: anulá ese pago en Liquidación para corregirlo.»</p></div>

## Asistencia {#asistencia}

Muestra quién está trabajando ahora y lo que hizo cada uno contra su horario: horas, llegadas tarde y faltas. Desde acá se corrigen las fichadas y se justifican las faltas.

<p class="perm"><span>Quién puede:</span> <span class="tag">Presentismo</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-asistencia.jpg' | relative_url }}" alt="La pantalla Asistencia del día: los botones Exportar y Cargar turno, el período, las cifras de trabajando ahora, horas, tardes y faltas, y la tabla por persona" loading="lazy" width="1440" height="600">
  <ol class="marks">
    <li><b>Exportar</b> baja una planilla del período y <b>Cargar turno</b> suma uno que no se fichó.</li>
    <li>El período: <b>Hoy</b>, <b>Ayer</b>, <b>Semana pasada</b>, <b>Últimos 7 días</b>, <b>Este mes</b>, <b>Mes pasado</b>, o las fechas <b>Desde</b> y <b>Hasta</b>.</li>
    <li><b>Trabajando ahora</b>, <b>Horas trabajadas</b>, <b>Llegadas tarde</b> y <b>Faltas</b>. Si hay turnos abiertos, aparece también <b>Sin fichar la salida</b>.</li>
    <li><b>Ahora</b>: «Desde las 21:20», «No fichó hoy», «Entra 18 h», «Se fue a las 17:05» o «Franco».</li>
    <li><b>Faltas</b> del período, contra su horario.</li>
  </ol>
  <figcaption>La asistencia de hoy en la demo. Llegar hasta 10 minutos después de la hora no es tarde.</figcaption>
</figure>

### Ver los días de alguien

Tocá la fila de la persona. Se abre su detalle día por día: el **Horario**, lo que **Fichó**, las **Horas** y **Cómo fue**:

| Dice | Significa |
|---|---|
| **Vino** | Fichó a tiempo un día con horario. |
| **Vino sin horario** | Fichó un día que no tenía horario. |
| **Tarde** | Llegó después de la tolerancia. Dice cuántos minutos. |
| **Faltó a un turno** | Tenía más de un turno ese día y faltó a alguno. |
| **Faltó** | No fichó en un día con horario. |
| **Justificado** | La falta tiene motivo. Dice «(pago)» si se le paga. |
| **Franco** | No tenía horario. |

### Cargar un turno que no se fichó

1. Tocá **Cargar turno**, o **Agregar** en el día, dentro del detalle de la persona.
2. Elegí la **Persona** y el **Día**. No puede ser un día que todavía no llegó.
3. Poné la **Entrada** y la **Salida**. Dejá la salida vacía si todavía está trabajando.
4. Si querés, dejá una **Nota (opcional)**, como «Se olvidó de fichar la salida».
5. Tocá **Guardar**. Aparece «Turno cargado».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-cargar-turno.jpg' | relative_url }}" alt="El panel Cargar turno con Persona en Lucía, el Día, Entrada, Salida, que puede quedar vacía si todavía está trabajando, y la Nota" loading="lazy" width="620" height="470">
  <figcaption>Cargar un turno que alguien se olvidó de fichar.</figcaption>
</figure>

### Corregir o borrar un turno

1. En el detalle de la persona, tocá el horario fichado.
2. Cambiá la entrada o la salida y tocá **Guardar**. Aparece «Turno corregido».
{: .steps}

Para borrarlo, tocá **Borrar** en la misma ventana y confirmá. Un turno no cambia de persona: si se cargó a otra, borralo y cargalo en la que corresponde. Cada turno corregido a mano dice dónde se fichó y quién lo corrigió.

### Justificar una falta

1. En el detalle de la persona, tocá **Justificar** en el día que faltó.
2. Escribí **Por qué no vino**, o tocá una sugerencia: **Enfermedad**, **Vacaciones**, **Cambio de franco**, **Trámite**, **Estudio**.
3. Prendé **Se le paga ese día** si corresponde. Para quien cobra por hora o por día, cuenta como trabajado con las horas de su horario.
4. Tocá **Justificar**. Aparece «Falta justificada».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-justificar.jpg' | relative_url }}" alt="El panel de la falta de Sofía Pérez del martes 10/11 con Por qué no vino en Turno con el médico y Se le paga ese día tildado" loading="lazy" width="620" height="260">
  <figcaption>Una falta justificada y paga.</figcaption>
</figure>

Para deshacerla, abrí la justificación y tocá **Quitar justificación**.

<div class="callout tip"><p class="callout-title">Consejo</p><p>Si alguien se olvida de fichar la salida, pasadas las horas de <b>Un fichaje sin salida se da por olvidado a las (horas)</b> (16, si no se cambió) su próximo toque del PIN empieza un turno nuevo. El turno olvidado queda acá, marcado «sin salida», para que el encargado le ponga la hora. La tolerancia para llegar y esas horas se cambian en <a href="{{ '/es/projects/fornu/manual/ajustes/' | relative_url }}#configuracion">Ajustes › Configuración</a>.</p></div>

**Exportar** baja una planilla del período elegido, con la persona, el día, el horario, las entradas y salidas, las horas y cómo fue. Se abre con Excel o Google Sheets.

## Horarios {#horarios}

Es el horario de la semana de cada persona, escrito como se escribe en la cocina. Con él la asistencia sabe quién llegó tarde o faltó y el presentismo completa los francos.

<p class="perm"><span>Quién puede:</span> <span class="tag">Presentismo</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-horarios.jpg' | relative_url }}" alt="La pantalla Horarios con cinco personas y un casillero por día de la semana, con horarios como 9-17 y 18-24 y francos" loading="lazy" width="1440" height="600">
  <ol class="marks">
    <li>Un día con su horario: 9-17.</li>
    <li>Un día vacío es franco.</li>
    <li><b>Horas</b>: el total de la semana.</li>
    <li><b>Guardar</b>: la fila también se guarda sola al salir de ella.</li>
  </ol>
  <figcaption>Debajo de cada nombre dice desde cuándo vale su horario.</figcaption>
</figure>

### Cargar el horario de alguien

1. Tocá el día en la fila de la persona y escribí el horario.
2. Pasá al día siguiente con <kbd>Tab</kbd>. La fila cambiada se resalta.
3. Al salir de la fila, o con <kbd>Enter</kbd>, se guarda sola. Aparece «Horario de Lucía guardado».
{: .steps}

Un cambio vale desde hoy: los días anteriores quedan con el horario que tenían. Si algo no se entiende, el error aparece debajo de la fila y dice qué día revisar.

| Escribís | Se lee |
|---|---|
| 9-17, 9:30-13, 9.30-13, 9 a 17, 9-17 hs | De tal hora a tal hora. |
| 20-2 | Pasa la medianoche. |
| 9-13 / 19-23 | Turno cortado. También sirven la coma, el punto y coma, el + o la y. Hasta 3 turnos por día. |
| vacío, franco, libre o - | Franco. |
| AM, o AM, PM | Los turnos con nombre de [Configuración de personal](#turnos). |

Un turno no puede durar más de 16 horas, y dos turnos del mismo día no se pueden pisar.

## Liquidación {#liquidacion}

Muestra lo que ganó cada persona en el período, según cómo cobra, menos los adelantos, y anota el pago. El pago queda como gasto de sueldos y, si es en efectivo, sale de la caja. No reemplaza el recibo de sueldo del contador.

<p class="perm"><span>Quién puede:</span> <span class="tag">Liquidación</span></p>

Arriba se elige el período: **Quincena pasada** (del 1 al 15, o del 16 a fin de mes), **Semana pasada**, **Este mes**, **Mes pasado**, o las fechas **Desde** y **Hasta**. Las cifras dicen cuánto **Falta pagar** y cuánto está **Ya pagado del período**.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-liquidacion.jpg' | relative_url }}" alt="La tabla de Liquidación: cada persona con cómo cobra, lo que trabajó, lo que ganó, los adelantos, lo que hay que pagarle y el botón Pagar" loading="lazy" width="1384" height="450">
  <ol class="marks">
    <li><b>Falta cargarlo</b>: la persona no tiene cargado cómo cobra. El link lleva a Equipo.</li>
    <li><b>Trabajó</b>: días, horas y, para los mensajeros, envíos.</li>
    <li><b>A pagar</b>: lo que ganó menos los adelantos.</li>
    <li><b>Pagar</b>: abre el pago de esa persona. Las filas ya pagadas dicen «Pagado el» y la fecha.</li>
    <li><b>Últimos pagos</b>: los 30 últimos. Tocá uno para abrirlo.</li>
  </ol>
  <figcaption>Una quincena de la demo, todavía sin pagar.</figcaption>
</figure>

### Pagarle a una persona

1. Tocá **Pagar** en su fila.
2. Revisá lo que ganó: horas, días, el sueldo del mes o los envíos.
3. Si hay un premio o un descuento, tocá **+ Premio o descuento (un descuento va en negativo)**, escribí qué es y cuánto.
4. Cada adelanto aparece tildado para descontarlo. Destildá el que quieras dejar para el próximo pago.
5. Elegí la **Fecha de pago**, el **Medio de pago** y la **Categoría del gasto**.
6. Tocá **Pagar** con el monto. Aparece «Pago a Lucía registrado» y se abre el pago.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-pagar.jpg' | relative_url }}" alt="La ventana para pagarle a una persona: las horas trabajadas, el link para sumar un premio o descuento, lo que se le entrega, la fecha, el medio de pago, la categoría del gasto y el botón Pagar" loading="lazy" width="880" height="900">
  <ol class="marks">
    <li>Lo que ganó, línea por línea.</li>
    <li><b>+ Premio o descuento</b>: suma una línea. Un descuento va en negativo.</li>
    <li><b>Se le entrega</b>: el total, con los adelantos ya descontados.</li>
    <li><b>Medio de pago</b>: en efectivo, sale de la caja. Si en la caja hay menos, lo avisa.</li>
    <li><b>Categoría del gasto</b>: elige sola la de sueldos. Así cuenta en Rentabilidad.</li>
    <li><b>Pagar</b>, con el monto que se entrega.</li>
  </ol>
  <figcaption>El pago de una quincena por hora.</figcaption>
</figure>

Si se paga en efectivo con la caja cerrada, Fornu avisa antes «La caja está cerrada»: esa plata saldría de una caja que nadie abrió y el arqueo no la cuadra. Conviene abrir la caja primero, en [Caja y ventas]({{ '/es/projects/fornu/manual/caja/' | relative_url }}#arqueo), o elegir otro medio. Para seguir igual, tocá **Pagar igual**. El pago queda como gasto con fecha del último día del período, en la categoría elegida, y suma en [Rentabilidad]({{ '/es/projects/fornu/manual/costos-y-reportes/' | relative_url }}).

### Pagar a todos {#pagar-a-todos}

Cuando dos o más personas tienen algo para cobrar, aparece **Pagar a todos**, con la cantidad y el total.

1. Tocá **Pagar a todos**.
2. Revisá la lista: lo que ganó cada uno, los adelantos y lo que se le entrega.
3. Elegí la **Fecha de pago**, el **Medio** y la **Categoría del gasto**. El medio viene en **Transferencia**.
4. Tocá **Pagar** con el total. Aparece «Pagado a 2 personas: $ 60.000.»
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-pagar-a-todos.jpg' | relative_url }}" alt="La liquidación de la quincena pasada con el botón Pagar a todos y, a la derecha, el panel que lista a seis personas con lo que ganó cada una y lo que se le paga, el adelanto descontado a Diego, la fecha, el medio en Transferencia y el botón Pagar $ 1.988.322,58" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li><b>Pagar a todos</b>: aparece con dos o más personas para pagar.</li>
    <li>Cada persona, lo que ganó y lo que se le entrega. A Diego se le descuenta un adelanto.</li>
    <li>Un premio o un descuento de alguien se carga pagándole solo a esa persona.</li>
    <li><b>Medio</b>: viene en <b>Transferencia</b>.</li>
    <li><b>Pagar</b>, con el total.</li>
  </ol>
  <figcaption>El pago de una quincena a seis personas.</figcaption>
</figure>

Si el pago de alguien no se puede hacer, Fornu avisa quién quedó sin pagar y desde quién: «Se pagó a 2 personas; Martín y los que siguen quedaron sin pagar.»

### Imprimir el recibo o anular un pago

1. En **Últimos pagos**, tocá el pago.
2. Para el papel, tocá **Imprimir recibo**: sale el «Recibo de pago» con el total recibido y lugar para la firma y la aclaración.
3. Para anularlo, tocá **Anular pago**, escribí **Por qué se anula** y confirmá con **Anular pago**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-recibo.jpg' | relative_url }}" alt="El recibo de pago impreso de Carla Gómez: el período del 16 al 31 de octubre, pagado el 10/11/2026 en efectivo, las horas trabajadas, el total recibido, Recibí de Cocina de prueba la suma de $ 299.250, y las líneas para la firma y la aclaración" loading="lazy" width="1440" height="320">
  <figcaption>El recibo impreso, con lugar para la firma.</figcaption>
</figure>

Al anular, se anula su gasto, los adelantos vuelven a quedar por descontar y, si fue en efectivo, la plata vuelve a la caja. El pago anulado sigue en la lista con la marca «anulado».

### Lo que frena un pago

| Mensaje | Qué hacer |
|---|---|
| «Lucía tiene un turno sin salida el 03/11: corregilo en Asistencia antes de pagar.» | Ponerle la salida en [Asistencia](#asistencia). Pasa con quien cobra por hora. |
| «Lucía sigue trabajando, desde las 9:00 del 15/11: pagale cuando salga, o liquidá hasta el día anterior.» | Esperar a que fiche la salida, o elegir un período que termine ayer. |
| «A Lucía ya se le pagó del 01/11 al 15/11: anulá ese pago para liquidarlo de nuevo.» | Anular el pago anterior primero. |
| «Se paga lo ya trabajado: el período termina hoy como mucho.» | Elegir un período que no termine en el futuro. |
| «Un pago cubre hasta 62 días.» | Partir el período en dos. |
| «Los adelantos superan lo que cobra: destildá alguno» | Dejar un adelanto para el próximo pago. |

<div class="callout"><p class="callout-title">Importante</p><p>Los días pagados quedan cerrados. La planilla, los turnos y las justificaciones de esos días no se pueden cambiar hasta anular el pago.</p></div>

Un sueldo mensual se prorratea por los días de cada mes que toma el período, o por 30 días, según lo elegido en [El mes del presentismo](#mes).

## Adelantos {#adelantos}

Es la plata que se le da a alguien antes del día de pago. La liquidación la descuenta del próximo pago y, si se da en efectivo, sale de la caja.

<p class="perm"><span>Quién puede:</span> <span class="tag">Adelantos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-adelantos.jpg' | relative_url }}" alt="La pantalla Adelantos con 20.000 pesos por descontar, un adelanto en efectivo con su nota y el botón Borrar" loading="lazy" width="1440" height="460">
  <ol class="marks">
    <li><b>Nuevo adelanto</b>: anota uno.</li>
    <li><b>Por descontar</b>: el total que todavía no se descontó, y cuántos adelantos son.</li>
    <li>La nota y quién lo dio.</li>
    <li><b>Borrar</b>: lo saca, si todavía no se descontó.</li>
    <li><b>Ya descontados</b>: los de los últimos dos meses.</li>
  </ol>
  <figcaption>Un adelanto pendiente en la demo.</figcaption>
</figure>

### Anotar un adelanto

1. Tocá **Nuevo adelanto**.
2. Elegí la **Persona** y escribí **Cuánto**.
3. Revisá el **Día** (no puede ser futuro) y el **Medio**. En **Efectivo**, sale de la caja.
4. Si querés, dejá una **Nota (opcional)**.
5. Tocá **Guardar**. Aparece «Adelanto anotado».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-adelanto.jpg' | relative_url }}" alt="El panel Nuevo adelanto con Persona en Martín, Cuánto 15000, el Día, Medio en Efectivo con el aviso Sale de la caja, y la Nota" loading="lazy" width="620" height="470">
  <figcaption>Un adelanto en efectivo, que sale de la caja.</figcaption>
</figure>

Con la caja cerrada, Fornu pregunta antes de seguir y se puede confirmar con **Pagar igual**.

### Borrar un adelanto

Tocá **Borrar** en su fila y confirmá. Si fue en efectivo, la plata vuelve a la caja. Un adelanto que ya se descontó en un pago no se borra: primero hay que anular ese pago en [Liquidación](#liquidacion).

<div class="callout tip"><p class="callout-title">Consejo</p><p>En el teléfono, Personal está dentro de <b>Más</b>, en la barra de abajo. Las tablas se ven como tarjetas, cada dato con su nombre.</p></div>
