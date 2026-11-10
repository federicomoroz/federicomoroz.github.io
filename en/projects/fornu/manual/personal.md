---
layout: manual
manual: personal
title: "Staff · Fornu manual"
description: "The team with their PIN, roles and pay, permissions and which ones can be lent with a PIN, and the Personal module: attendance sheet, clock-ins, schedules, payroll and advances."
permalink: /en/projects/fornu/manual/personal/
---

## Equipo {#equipo}

**Equipo** (team) is the list of people who work at the place. Each person clocks in and gets into Fornu with their own PIN on the kitchen tablet or their phone, without your password. What they can do in Fornu comes from their roles: someone whose roles carry no permissions only clocks in and out.

<p class="perm"><span>Who can:</span> <span class="tag">Equipo</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-equipo.jpg' | relative_url }}" alt="The Equipo list with five people: their colored roles, status, what they can do in Fornu, how much they earn and whether their PIN is set" loading="lazy" width="1440" height="520">
  <ol class="marks">
    <li><b>Agregar</b> (add): adds a person to the team.</li>
    <li><b>Roles</b>: each person's roles, with their color. Someone with none shows «Sin rol» (no role).</li>
    <li><b>En Fornu</b> (in Fornu): what they can do, adding up the permissions of all their roles. Someone with no permissions shows «Solo ficha» (clocks only).</li>
    <li><b>Cobra</b> (pay): how they are paid and how much, for example «$ 4.200 por hora» (per hour). Payroll uses it.</li>
    <li><b>PIN</b>: «Cargado» (set) or «Falta» (missing). The row's <b>PIN</b> button gives them a new one.</li>
  </ol>
  <figcaption>The demo's team. The <b>Estado</b> (status) and <b>Cobra</b> columns come with the Personal module.</figcaption>
</figure>

### Add someone

1. Tap **Agregar**.
2. Type the **Nombre** (name), the way the place calls them.
3. If you already have their PIN, enter it in **PIN (opcional)** (optional): 4 to 6 digits. It can be set later.
4. Pick their **Roles**. The first one you pick is the one schedules and the attendance sheet show.
5. With the Personal module, check the **Estado** (status, it starts as **Activo**, active) and pick **Cómo cobra** (how they are paid): **Por hora** (hourly), **Por día** (daily) or **Por mes** (monthly). Type the amount in **Cuánto** (how much).
6. Tap **Guardar** (save). You see «Guardado: Lucía».
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-persona.jpg' | relative_url }}" alt="The form for adding a person, with the PIN entered, the roles to pick from, the status, the since date, and how and how much they are paid" loading="lazy" width="620" height="900">
  <ol class="marks">
    <li><b>PIN (opcional)</b>: 4 to 6 digits, to clock in and get in.</li>
    <li><b>Roles</b>: tap each one that applies. Hovering a role shows what it allows.</li>
    <li><b>Estado</b> and <b>Desde</b> (since): whether they work, and since when.</li>
    <li><b>Cómo cobra</b> and <b>Cuánto</b>: the hourly, daily or monthly amount.</li>
  </ol>
  <figcaption>A new person's form, scrolled down to the pay.</figcaption>
</figure>

What each field means:

| Field | What it is |
|---|---|
| **Estado** | Where the person stands: **Activo**, **A prueba** (on trial), **Extra**, **Inactivo** (inactive), **Baja** (left) or any you add. If the status is a non-working one, their PIN stops working. |
| **Desde** | If they stop working, their last day worked. The attendance sheet fills in the rest of the month. |
| **DNI (opcional)**, **Teléfono (opcional)**, **En caso de emergencia (opcional)** | ID number, phone and an emergency contact, to keep at hand. |
| **Cómo cobra** | **No por su tiempo** (not paid for their time, the default), **Por hora**, **Por día** or **Por mes**. |
| **Cuánto** | The hourly, daily or monthly amount. Shows when they are paid for their time. |
| **Por envío** (per delivery) | Shows if one of their roles has the **Mensajería** (delivery) permission. Added for each own-delivery order they delivered. |

To change something about a person, tap their row, make the change and tap **Guardar**. On a computer, <kbd>Ctrl</kbd> + <kbd>Enter</kbd> saves any form.

### Set or change a PIN

1. On the person's row, tap **PIN**.
2. Type the **PIN nuevo** (new PIN): 4 to 6 digits.
3. Tap **Guardar**. You see «PIN guardado» (PIN saved).
{: .steps}

<div class="callout tip"><p class="callout-title">Tip</p><p>Hand the PIN over in person, not in a message. With it they clock in and get into Fornu on any paired device at the place.</p></div>

<div class="callout"><p class="callout-title">Good to know</p><p>A person's PIN can only be changed by someone who holds every permission that person has. Nobody can give a role with permissions they don't have themselves. And your own roles and pay are changed by someone else: «Tus propios roles los cambia otra persona.» (someone else changes your own roles).</p></div>

### When someone stops working

People are never deleted, because past attendance sheets and payments still name them. With the Personal module:

1. Tap the person's row.
2. In **Estado**, pick **Inactivo** or **Baja**.
3. In **Desde**, enter their last day worked.
4. Tap **Guardar**.
{: .steps}

From then on their PIN stops working and their name leaves the device's list. With **Inactivo**, the attendance sheet fills the rest of the month with the leave code (**X**). Statuses are set up in [Configuración de personal](#estados).

How each person clocks in with their PIN is in [In the kitchen and on the road]({{ '/en/projects/fornu/manual/cocina-y-reparto/' | relative_url }}#fichar). Clocking in is part of the base: it works with or without the Personal module.

## Configuración de personal {#roles}

**Configuración de personal** (staff setup) holds the team's lists the way the place uses them: the roles and what each can do, and below them what the Personal module adds (statuses, attendance codes, named shifts and the month of the sheet). The tab reads **Configuración** and the page title **Configuración de personal**.

<p class="perm"><span>Who can:</span> <span class="tag">Equipo</span> <span class="tag">Administración</span> (roles)</p>

Only the account's Administración (admin) sees the **Roles** block. Someone with the Equipo permission sees the Personal module's lists.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-roles.jpg' | relative_url }}" alt="The Roles block with six roles: Cocina, Mensajería, Encargado/a, Mozo, Adicionista and Caja, what each can do and how many people have it" loading="lazy" width="1440" height="555">
  <ol class="marks">
    <li><b>Agregar</b>: creates a new role.</li>
    <li><b>Puede</b> (can): the role's permissions. A role with none shows «Solo ficha».</li>
    <li><b>Personas</b> (people): how many people have that role.</li>
  </ol>
  <figcaption>The demo's roles, with Salón (dining room) turned on.</figcaption>
</figure>

### Create a role

1. In **Roles**, tap **Agregar**.
2. Give it a **Nombre** the way the place says it: Parrillero (grill cook), Moza (waitress), Caja del local (front cashier). Up to 40 characters.
3. Pick the **Color**. It is the dot next to the role on the team list, schedules and attendance sheet.
4. Under **Puede**, tap the permissions it carries. **Básico** (basic) comes first, then each module that is on.
5. Tap **Guardar**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-rol-editor.jpg' | relative_url }}" alt="The new role form: name, color and the permissions grouped under Básico and under each module" loading="lazy" width="620" height="900">
  <ol class="marks">
    <li><b>Color</b>: the role's color on every team screen.</li>
    <li><b>Básico</b>: the permissions every account has.</li>
    <li>The permissions of each module that is on, grouped under its name.</li>
  </ol>
  <figcaption>Hover a permission to read what it allows.</figcaption>
</figure>

A role with no permissions is for someone who has to clock in but does not use Fornu: they tap their name, type their PIN and they are clocked in. The full list of permissions, with what each one allows, is in the [manual's index]({{ '/en/projects/fornu/manual/' | relative_url }}#permisos).

### Permissions that go together, and the ones lent with a PIN {#prestar}

Some permissions make no sense without another. If you tap **Anular lo mandado** (void what was sent), **Atender mesas** (serve tables) gets ticked too, and if you later untick **Atender mesas**, the ones that need it go with it.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-requiere.jpg' | relative_url }}" alt="The Salón permissions in the role editor: Anular lo mandado is picked and Atender mesas got ticked along with it" loading="lazy" width="620" height="270">
  <ol class="marks">
    <li><b>Anular lo mandado</b>: the permission that was tapped.</li>
    <li><b>Atender mesas</b>: ticked by itself, because the other one needs it.</li>
  </ol>
  <figcaption>Picking a permission also picks the one it needs.</figcaption>
</figure>

Some permissions can be lent on the spot. If someone lacks one of these, a person who has it types their PIN and the action goes through. It works for that one action and for two minutes, and it records who authorized it, for example «Anulado por Sofía (autorizó Lucía)» (voided by Sofía, authorized by Lucía). How to ask for it is in [Dining room: tables, counter and payment]({{ '/en/projects/fornu/manual/salon/' | relative_url }}#autorizar).

| Permission | Needs | Lent with a PIN |
|---|---|---|
| **Ver lo esperado** (see the expected cash) | Caja | No |
| **Recontar la caja** (recount the cash) | Caja | Yes |
| **Asignar quién atiende** (assign who serves) | Atender mesas | Yes |
| **Mover mesas** (move tables) | Atender mesas | Yes |
| **Anular lo mandado** | Atender mesas | Yes |
| **Descontar e invitar** (discount and comp) | Atender mesas | Yes |
| **Cobrar mesas** (take payment) | Atender mesas | No |
| **Deshacer cobros** (undo payments) | Cobrar mesas | Yes |
| **Cancelar mesas** (cancel tables) | Atender mesas | Yes |

All other permissions need nothing else and are never lent. Which table actions ask for the PIN, such as voiding a line or handing the table to another waiter, is on the same Salón page.

### The roles a new account starts with {#roles-de-entrada}

A new account comes with three roles, which can be changed like any other:

| Role | Can |
|---|---|
| **Cocina** (kitchen) | Cocina |
| **Mensajería** (delivery) | Mensajería |
| **Encargado/a** (manager) | Cocina, Pedidos, Stock, Caja, Ver lo esperado, Recontar la caja, Gastos and Dispositivos |

**Encargado/a** does not include Equipo, Ajustes or the Personal module's permissions. Add them if your manager runs the team or does payroll.

When Salón is turned on, three suggested roles arrive, unless some role already has a Salón permission:

| Role | Can |
|---|---|
| **Mozo** (waiter) | Atender mesas and Mover mesas |
| **Adicionista** (order desk) | Atender mesas, Asignar quién atiende, Mover mesas, Anular lo mandado, Descontar e invitar and Cobrar mesas |
| **Caja** (cashier) | Atender mesas, Cobrar mesas, Descontar e invitar, Anular lo mandado, Deshacer cobros and Cancelar mesas |

<div class="callout"><p class="callout-title">Good to know</p><p>Roles are never deleted. They are switched off with <b>Activo</b> (active), which shows when you edit one. A switched-off role stops granting its permissions at once. Changes to a role reach whoever is using Fornu right away, and someone left with no permissions is signed out.</p></div>

If a module is turned off, its permissions vanish from the editor but stay saved on each role, and they come back when the module is turned on again.

### The month of the sheet {#mes}

This card and the three below come with the Personal module. **El mes del presentismo** (the month of the attendance sheet) sets when each month of the sheet starts and what fills in by itself.

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-mes.jpg' | relative_url }}" alt="The El mes del presentismo card: the day the month starts, how a monthly salary is prorated and the four codes that fill in by themselves" loading="lazy" width="1440" height="275">
  <ol class="marks">
    <li><b>El mes empieza el día</b> (the month starts on day): 1 to 28. With 26, October runs from September 26 to October 25.</li>
    <li><b>El sueldo mensual se prorratea por</b> (prorate the monthly salary by): <b>Los días del mes</b> (the month's days) or <b>30 días</b>, for periods that cover part of a month.</li>
    <li><b>Fichó a horario</b> (on time), <b>Fichó tarde</b> (late), <b>Franco</b> (day off) and <b>Baja</b> (left): the code written by itself in each case, or «Nada: lo carga el encargado» (nothing, the manager enters it).</li>
    <li><b>Guardar</b>: this card saves on its own. It lights up when you change something.</li>
  </ol>
  <figcaption>A new account's settings.</figcaption>
</figure>

### Statuses {#estados}

**Estados** say where each person stands. If a status is a non-working one, the person's PIN stops working. If it also fills with leave, the attendance sheet fills the rest of the month from the day after the **Desde** date.

| Estado | Trabaja (works) | Completa con baja (fills with leave) |
|---|---|---|
| **Activo** | Yes | No |
| **A prueba** | Yes | No |
| **Extra** | Yes | No |
| **Inactivo** | No | Yes |
| **Baja** | No | No |

To add one, tap **Agregar** on the card and fill in **Nombre**, **Color**, **Trabaja** and **Completa con baja**. If people are in a status, move them to another one before changing its **Trabaja**.

### Attendance codes {#codigos}

**Códigos del presentismo** are what gets written on each day of the sheet. **Cuenta como** (counts as) decides what payroll pays, and **Suma al total de** (adds to the total of) says which column of the month it adds to.

| Code | Means | Counts as | Adds to |
|---|---|---|---|
| **P** | Presente (present) | Presente | Its own total |
| **PP** | Doble turno (double shift) | Presente | P |
| **T** | Llegó tarde (late) | Tarde | Its own total |
| **A** | Ausente (absent) | Ausente | Its own total |
| **AJ** | Ausente justificado (excused) | Ausente | A |
| **F** | Franco (day off) | No cuenta (does not count) | Its own total |
| **X** | Ya no trabaja (no longer works) | No cuenta | Its own total |

A code has up to 4 letters or digits, no spaces, and is saved in capitals. A code that fills in by itself on the sheet cannot be switched off until you pick another one in **El mes del presentismo**.

### Named shifts {#turnos}

**Turnos** are the shifts the place calls by name. With an **AM** shift from 9 to 17, typing AM in Horarios is enough, or AM, PM for a split day.

1. In **Turnos**, tap **Agregar**.
2. Give it a **Nombre** with letters only: numbers are read as hours.
3. Pick **Entra** (starts) and **Sale** (ends). If it ends before it starts, it runs past midnight: 20 to 2.
4. Tap **Guardar**.
{: .steps}

Without named shifts, schedules are written with their hours, like 9-17.

## Presentismo {#presentismo}

**Presentismo** (attendance sheet) is the month on one page: a row per person, a cell per day and the totals at the end. Clock-ins, scheduled days off and leave fill in by themselves, and what the manager writes wins, for pay too.

<p class="perm"><span>Who can:</span> <span class="tag">Presentismo</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-presentismo.jpg' | relative_url }}" alt="The November attendance sheet with five people, days filled in by themselves with P and F, and the totals column" loading="lazy" width="1440" height="510">
  <ol class="marks">
    <li>The previous month, <b>Este mes</b> (this month) and the next one. Each month is named after the month it ends in.</li>
    <li><b>Imprimir</b> (print): the month's sheet on paper.</li>
    <li>A dotted border marks what «se completó solo» (filled in by itself).</li>
    <li>A day: tap it to enter a code.</li>
    <li>The total of each code and <b>Trab.</b>, the days worked.</li>
  </ol>
  <figcaption>The demo's sheet. On a phone it scrolls sideways and opens on today.</figcaption>
</figure>

### Mark a day

1. Tap the day's cell on the person's row.
2. Tap the code. It is saved right away.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-presentismo-dia.jpg' | relative_url }}" alt="A day's window with the seven codes to pick from: Presente, Doble turno, Llegó tarde, Ausente, Ausente justificado, Franco and Ya no trabaja" loading="lazy" width="620" height="262">
  <figcaption>One tap on the code and it is entered.</figcaption>
</figure>

If the day already had a hand-written code, **Borrar lo cargado: vuelve a mostrar lo fichado** (clear it and show what was clocked) appears below.

### What fills in by itself

- A day the person clocked in shows the **Fichó a horario** code (P), or the **Fichó tarde** code (T) if they arrived after the tolerance set in [Ajustes › Configuración]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#configuracion).
- Days off in their schedule show **Franco** (F).
- After moving to a status that fills with leave, the rest of the month shows **Baja** (X).
- A hand-written code beats what was clocked.

A day marked as worked with nothing clocked counts the hours of the schedule. That way, a place that does not clock in can pay from the sheet. **PP** counts as one day worked and adds to the **P** total.

The sheet lists people with a working status, plus anyone who has something entered that month. **Imprimir** prints the month with the account name, the cells, the totals and the code legend.

<div class="callout"><p class="callout-title">Good to know</p><p>Days already paid are locked: «El 03/11 ya se le pagó: anulá ese pago en Liquidación para corregirlo.» (November 3 was already paid: void that payment in Liquidación to fix it.)</p></div>

## Asistencia {#asistencia}

**Asistencia** (clock-ins) shows who is working right now and how each person did against their schedule: hours, late arrivals and absences. This is where clock-ins get fixed and absences excused.

<p class="perm"><span>Who can:</span> <span class="tag">Presentismo</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-asistencia.jpg' | relative_url }}" alt="The Asistencia screen for today: the Exportar and Cargar turno buttons, the period, the figures for working now, hours, late arrivals and absences, and the table by person" loading="lazy" width="1440" height="600">
  <ol class="marks">
    <li><b>Exportar</b> (export) downloads the period as a spreadsheet and <b>Cargar turno</b> (add shift) adds one that was not clocked.</li>
    <li>The period: <b>Hoy</b> (today), <b>Ayer</b> (yesterday), <b>Semana pasada</b> (last week), <b>Últimos 7 días</b>, <b>Este mes</b>, <b>Mes pasado</b> (last month), or the <b>Desde</b> and <b>Hasta</b> dates.</li>
    <li><b>Trabajando ahora</b> (working now), <b>Horas trabajadas</b> (hours worked), <b>Llegadas tarde</b> (late arrivals) and <b>Faltas</b> (absences). With open shifts, <b>Sin fichar la salida</b> (not clocked out) shows too.</li>
    <li><b>Ahora</b> (now): «Desde las 21:20» (since 21:20), «No fichó hoy» (didn't clock in today), «Entra 18 h» (starts at 18), «Se fue a las 17:05» (left at 17:05) or «Franco».</li>
    <li><b>Faltas</b> in the period, against the schedule.</li>
  </ol>
  <figcaption>Today's attendance in the demo. Up to 10 minutes after the hour is not late.</figcaption>
</figure>

### See someone's days

Tap the person's row. Their days open one by one: the **Horario** (schedule), what they **Fichó** (clocked), the **Horas** and **Cómo fue** (how it went):

| Shows | Means |
|---|---|
| **Vino** | Clocked in on time on a scheduled day. |
| **Vino sin horario** | Clocked in on a day with no schedule. |
| **Tarde** | Arrived after the tolerance. Says by how many minutes. |
| **Faltó a un turno** | Had more than one shift that day and missed one. |
| **Faltó** | Did not clock in on a scheduled day. |
| **Justificado** | The absence has a reason. Says «(pago)» if it is paid. |
| **Franco** | Had no schedule. |

### Add a shift that was not clocked

1. Tap **Cargar turno**, or **Agregar** on the day inside the person's details.
2. Pick the **Persona** and the **Día** (day). It cannot be a day that has not come yet.
3. Enter the **Entrada** (in) and **Salida** (out). Leave the out time empty if they are still working.
4. Optionally add a **Nota (opcional)** such as «Se olvidó de fichar la salida» (forgot to clock out).
5. Tap **Guardar**. You see «Turno cargado» (shift added).
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-cargar-turno.jpg' | relative_url }}" alt="The Cargar turno panel with Persona on Lucía, the Día, Entrada, Salida, which can stay empty if they are still working, and the Nota" loading="lazy" width="620" height="470">
  <figcaption>Adding a shift someone forgot to clock.</figcaption>
</figure>

### Fix or delete a shift

1. In the person's details, tap the clocked times.
2. Change the in or out time and tap **Guardar**. You see «Turno corregido» (shift fixed).
{: .steps}

To delete it, tap **Borrar** (delete) in the same window and confirm. A shift never changes person: if it was entered for the wrong one, delete it and enter it for the right one. Every shift fixed by hand shows where it was clocked and who fixed it.

### Excuse an absence

1. In the person's details, tap **Justificar** (excuse) on the day they missed.
2. Type **Por qué no vino** (why they didn't come), or tap a suggestion: **Enfermedad** (sick), **Vacaciones** (vacation), **Cambio de franco** (swapped day off), **Trámite** (errand), **Estudio** (studies).
3. Turn on **Se le paga ese día** (that day is paid) if it applies. For people paid by the hour or the day, it counts as worked with the hours of their schedule.
4. Tap **Justificar**. You see «Falta justificada» (absence excused).
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-justificar.jpg' | relative_url }}" alt="The panel for Sofía Pérez's absence on Tuesday 10/11 with Por qué no vino on Turno con el médico and Se le paga ese día ticked" loading="lazy" width="620" height="260">
  <figcaption>An excused, paid absence.</figcaption>
</figure>

To undo it, open the excuse and tap **Quitar justificación** (remove excuse).

<div class="callout tip"><p class="callout-title">Tip</p><p>If someone forgets to clock out, after the hours set in <b>Un fichaje sin salida se da por olvidado a las (horas)</b> (16 unless changed) their next PIN tap starts a new shift. The forgotten one stays here marked «sin salida» (no clock-out) so the manager can enter the time. The late tolerance and those hours are set in <a href="{{ '/en/projects/fornu/manual/ajustes/' | relative_url }}#configuracion">Ajustes › Configuración</a>.</p></div>

**Exportar** downloads the chosen period as a spreadsheet with the person, the day, the schedule, the ins and outs, the hours and how it went. It opens in Excel or Google Sheets.

## Horarios {#horarios}

**Horarios** (schedules) holds each person's week, written the way the kitchen writes it. With it, Asistencia knows who was late or absent and the attendance sheet fills in the days off.

<p class="perm"><span>Who can:</span> <span class="tag">Presentismo</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-horarios.jpg' | relative_url }}" alt="The Horarios screen with five people and a box for each weekday, holding schedules like 9-17 and 18-24 and days off" loading="lazy" width="1440" height="600">
  <ol class="marks">
    <li>A day with its schedule: 9-17.</li>
    <li>An empty day is a day off.</li>
    <li><b>Horas</b>: the week's total.</li>
    <li><b>Guardar</b>: the row also saves by itself when you leave it.</li>
  </ol>
  <figcaption>Under each name it says since when their schedule applies.</figcaption>
</figure>

### Enter someone's schedule

1. Tap the day on the person's row and type the schedule.
2. Move to the next day with <kbd>Tab</kbd>. A changed row is highlighted.
3. Leaving the row, or pressing <kbd>Enter</kbd>, saves it. You see «Horario de Lucía guardado» (Lucía's schedule saved).
{: .steps}

A change applies from today: earlier days keep the schedule they had. If something can't be read, the error shows under the row and says which day to check.

| You type | It reads |
|---|---|
| 9-17, 9:30-13, 9.30-13, 9 a 17, 9-17 hs | From one hour to another. |
| 20-2 | Runs past midnight. |
| 9-13 / 19-23 | Split shift. A comma, semicolon, + or "y" (and) also work. Up to 3 shifts a day. |
| empty, franco, libre or - | Day off. |
| AM, or AM, PM | The named shifts from [Configuración de personal](#turnos). |

A shift can't be longer than 16 hours, and two shifts on the same day can't overlap.

## Liquidación {#liquidacion}

**Liquidación** (payroll) shows what each person earned in the period, according to how they are paid, minus advances, and records the payment. The payment is filed as a salary expense and, if paid in cash, leaves the cash drawer. It does not replace the accountant's payslip.

<p class="perm"><span>Who can:</span> <span class="tag">Liquidación</span></p>

At the top you pick the period: **Quincena pasada** (last fortnight: the 1st to the 15th, or the 16th to month end), **Semana pasada**, **Este mes**, **Mes pasado**, or the **Desde** and **Hasta** dates. The figures show what **Falta pagar** (is still owed) and what is **Ya pagado del período** (already paid for the period).

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-liquidacion.jpg' | relative_url }}" alt="The Liquidación table: each person with how they are paid, what they worked, what they earned, advances, what is owed and the Pagar button" loading="lazy" width="1384" height="450">
  <ol class="marks">
    <li><b>Falta cargarlo</b> (not set yet): the person has no pay set. The link goes to Equipo.</li>
    <li><b>Trabajó</b> (worked): days, hours and, for couriers, deliveries.</li>
    <li><b>A pagar</b> (to pay): what they earned minus advances.</li>
    <li><b>Pagar</b> (pay): opens that person's payment. Rows already paid show «Pagado el» (paid on) and the date.</li>
    <li><b>Últimos pagos</b> (latest payments): the last 30. Tap one to open it.</li>
  </ol>
  <figcaption>A demo fortnight, not paid yet.</figcaption>
</figure>

### Pay one person

1. Tap **Pagar** on their row.
2. Check what they earned: hours, days, the month's salary or deliveries.
3. For a bonus or a deduction, tap **+ Premio o descuento (un descuento va en negativo)** (bonus or deduction, a deduction goes negative) and type what it is and how much.
4. Each advance shows ticked, to be deducted. Untick any you want to leave for the next payment.
5. Pick the **Fecha de pago** (payment date), the **Medio de pago** (payment method) and the **Categoría del gasto** (expense category).
6. Tap **Pagar** with the amount. You see «Pago a Lucía registrado» (payment to Lucía recorded) and the payment opens.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-pagar.jpg' | relative_url }}" alt="The window for paying one person: hours worked, the link to add a bonus or deduction, what is handed over, the date, the payment method, the expense category and the Pagar button" loading="lazy" width="880" height="900">
  <ol class="marks">
    <li>What they earned, line by line.</li>
    <li><b>+ Premio o descuento</b>: adds a line. A deduction goes negative.</li>
    <li><b>Se le entrega</b> (handed over): the total, with advances already deducted.</li>
    <li><b>Medio de pago</b>: in cash, it leaves the drawer. If the drawer holds less, it says so.</li>
    <li><b>Categoría del gasto</b>: picks the salaries one by itself. That is how it counts in Rentabilidad (profitability).</li>
    <li><b>Pagar</b>, with the amount handed over.</li>
  </ol>
  <figcaption>Paying an hourly fortnight.</figcaption>
</figure>

If you pay in cash with the drawer closed, Fornu first warns «La caja está cerrada» (the drawer is closed): that money would leave a drawer nobody opened, and the cash count won't add it up. Better open the drawer first, in [Cash and sales]({{ '/en/projects/fornu/manual/caja/' | relative_url }}#arqueo), or pick another method. To go ahead anyway, tap **Pagar igual** (pay anyway). The payment is filed as an expense dated on the last day of the period, in the chosen category, and counts in [Rentabilidad]({{ '/en/projects/fornu/manual/costos-y-reportes/' | relative_url }}).

### Pay everyone {#pagar-a-todos}

When two or more people have something to collect, **Pagar a todos** (pay everyone) appears, with the headcount and the total.

1. Tap **Pagar a todos**.
2. Check the list: what each person earned, their advances and what they get.
3. Pick the **Fecha de pago**, the **Medio** and the **Categoría del gasto**. The method starts as **Transferencia** (bank transfer).
4. Tap **Pagar** with the total. You see «Pagado a 2 personas: $ 60.000.»
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-pagar-a-todos.jpg' | relative_url }}" alt="Last fortnight's payroll with the Pagar a todos button and, on the right, the panel listing six people with what each earned and what each is paid, Diego's advance deducted, the date, the method on Transferencia and the Pagar $ 1.988.322,58 button" loading="lazy" width="1440" height="900">
  <ol class="marks">
    <li><b>Pagar a todos</b> (pay everyone): shows when two or more people are due.</li>
    <li>Each person, what they earned and what they get. Diego has an advance deducted.</li>
    <li>A bonus or a deduction for someone is entered by paying that person alone.</li>
    <li><b>Medio</b> (method): starts on <b>Transferencia</b> (transfer).</li>
    <li><b>Pagar</b> (pay), with the total.</li>
  </ol>
  <figcaption>Paying a fortnight to six people.</figcaption>
</figure>

If one person's payment can't be made, Fornu says who was left unpaid, from whom on: «Se pagó a 2 personas; Martín y los que siguen quedaron sin pagar.» (2 people were paid, Martín and those after him were not).

### Print the receipt or void a payment

1. In **Últimos pagos**, tap the payment.
2. For paper, tap **Imprimir recibo** (print receipt): the «Recibo de pago» (payment receipt) prints with the total received and lines for the signature and printed name.
3. To void it, tap **Anular pago** (void payment), type **Por qué se anula** (why it is voided) and confirm with **Anular pago**.
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-recibo.jpg' | relative_url }}" alt="Carla Gómez's printed payment receipt: the period from 16 to 31 October, paid on 10/11/2026 in cash, the hours worked, the total received, Recibí de Cocina de prueba la suma de $ 299.250, and the lines for signature and printed name" loading="lazy" width="1440" height="320">
  <figcaption>The printed receipt, with room to sign.</figcaption>
</figure>

Voiding cancels its expense, puts the advances back to be deducted and, if it was in cash, returns the money to the drawer. The voided payment stays on the list, tagged «anulado» (voided).

### What stops a payment

| Message | What to do |
|---|---|
| «Lucía tiene un turno sin salida el 03/11: corregilo en Asistencia antes de pagar.» (Lucía has a shift with no clock-out) | Enter the out time in [Asistencia](#asistencia). Happens with hourly pay. |
| «Lucía sigue trabajando, desde las 9:00 del 15/11: pagale cuando salga, o liquidá hasta el día anterior.» (still working) | Wait until they clock out, or pick a period that ends yesterday. |
| «A Lucía ya se le pagó del 01/11 al 15/11: anulá ese pago para liquidarlo de nuevo.» (already paid) | Void the earlier payment first. |
| «Se paga lo ya trabajado: el período termina hoy como mucho.» (only work done is paid) | Pick a period that doesn't end in the future. |
| «Un pago cubre hasta 62 días.» (a payment covers up to 62 days) | Split the period in two. |
| «Los adelantos superan lo que cobra: destildá alguno» (advances exceed the pay) | Leave an advance for the next payment. |

<div class="callout"><p class="callout-title">Good to know</p><p>Paid days are locked. The sheet, the shifts and the excuses for those days can't be changed until the payment is voided.</p></div>

A monthly salary is prorated by the days of each month the period covers, or by 30 days, as set in [the month of the sheet](#mes).

## Adelantos {#adelantos}

**Adelantos** (advances) are money given to someone before payday. Payroll deducts it from the next payment and, if given in cash, it leaves the drawer.

<p class="perm"><span>Who can:</span> <span class="tag">Adelantos</span></p>

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-adelantos.jpg' | relative_url }}" alt="The Adelantos screen with 20,000 pesos to deduct, a cash advance with its note and the Borrar button" loading="lazy" width="1440" height="460">
  <ol class="marks">
    <li><b>Nuevo adelanto</b> (new advance): records one.</li>
    <li><b>Por descontar</b> (to deduct): the total not yet deducted, and how many advances.</li>
    <li>The note and who gave it.</li>
    <li><b>Borrar</b> (delete): removes it, if it has not been deducted yet.</li>
    <li><b>Ya descontados</b> (already deducted): those from the last two months.</li>
  </ol>
  <figcaption>One pending advance in the demo.</figcaption>
</figure>

### Record an advance

1. Tap **Nuevo adelanto**.
2. Pick the **Persona** and type **Cuánto**.
3. Check the **Día** (it can't be in the future) and the **Medio**. In **Efectivo** (cash), it leaves the drawer.
4. Optionally add a **Nota (opcional)**.
5. Tap **Guardar**. You see «Adelanto anotado» (advance recorded).
{: .steps}

<figure class="shot">
  <img src="{{ '/assets/img/fornu/manual/personal-adelanto.jpg' | relative_url }}" alt="The Nuevo adelanto panel with Persona on Martín, Cuánto 15000, the Día, Medio on Efectivo with the note Sale de la caja, and the Nota" loading="lazy" width="620" height="470">
  <figcaption>A cash advance, which leaves the drawer.</figcaption>
</figure>

With the drawer closed, Fornu asks before going on, and you can confirm with **Pagar igual**.

### Delete an advance

Tap **Borrar** on its row and confirm. If it was in cash, the money goes back to the drawer. An advance already deducted in a payment can't be deleted: void that payment in [Liquidación](#liquidacion) first.

<div class="callout tip"><p class="callout-title">Tip</p><p>On a phone, Personal sits under <b>Más</b> (more) in the bottom bar. Tables show as cards, each value with its label.</p></div>
