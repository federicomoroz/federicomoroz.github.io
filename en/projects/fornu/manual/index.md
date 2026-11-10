---
layout: manual
manual: index
title: "Fornu user manual"
heading: "User manual"
description: "How to use Fornu, screen by screen: what each one does, how to do each thing, who can do it, and the shortcuts that save time during service."
permalink: /en/projects/fornu/manual/
---

Fornu brings together, in one place, the orders from delivery, the dining room and the counter, the kitchen, the stock, the cash drawer, purchases and staff. This manual goes through every screen in the order a restaurant uses them: first getting in and around, then service, then what gets set up once and reviewed now and then.

Each page says what the screen is for, how to do each thing step by step, what each option means and which permission it takes. The app is in Spanish, so its buttons and messages are quoted exactly as they appear, with a short English gloss the first time. The screenshots come from the demo account, with made-up data. To try things while you read, go to [fornu.onrender.com](https://fornu.onrender.com) and tap **Probar la demo** (try the demo).

## The pages {#paginas}

<ol class="manual-index">
{% for p in site.data.fornu_manual %}
  <li><a href="{{ '/en/projects/fornu/manual/' | append: p.id | append: '/' | relative_url }}">{{ p.title.en }}</a><p>{{ p.lead.en }}</p><small>{{ p.who.en }}</small></li>
{% endfor %}
</ol>

## Where each role starts {#por-puesto}

| If you are… | Start with |
|---|---|
| The owner or the back office | [Getting in and around]({{ '/en/projects/fornu/manual/empezar/' | relative_url }}), [Settings]({{ '/en/projects/fornu/manual/ajustes/' | relative_url }}), [Menu]({{ '/en/projects/fornu/manual/carta/' | relative_url }}), [Stock items and stock]({{ '/en/projects/fornu/manual/insumos-y-stock/' | relative_url }}) and [Costs and reports]({{ '/en/projects/fornu/manual/costos-y-reportes/' | relative_url }}) |
| The manager | [Orders and delivery]({{ '/en/projects/fornu/manual/pedidos/' | relative_url }}), [Cash and sales]({{ '/en/projects/fornu/manual/caja/' | relative_url }}), [Purchases and expenses]({{ '/en/projects/fornu/manual/compras-y-gastos/' | relative_url }}) and [Staff]({{ '/en/projects/fornu/manual/personal/' | relative_url }}) |
| The kitchen | [In the kitchen and on the road]({{ '/en/projects/fornu/manual/cocina-y-reparto/' | relative_url }}) and the board in [Orders and delivery]({{ '/en/projects/fornu/manual/pedidos/' | relative_url }}) |
| A waiter, the order desk or the dining room's cashier | [Dining room: tables, counter and payment]({{ '/en/projects/fornu/manual/salon/' | relative_url }}) |
| A courier | [In the kitchen and on the road]({{ '/en/projects/fornu/manual/cocina-y-reparto/' | relative_url }}#mensajero) |

## Two ways in {#entrar}

- **With an email and a password**, from any browser. This is how the owner, the back office and the manager come in: it opens the full screen, with every module their role lets them see.
- **With a PIN, on a paired device.** The kitchen tablet, or a waiter's or courier's phone, is paired once with a code. From then on each person taps their name and types their PIN. They see only the tabs for their job, and clock in with the same tap.

Both are explained in [Getting in and around]({{ '/en/projects/fornu/manual/empezar/' | relative_url }}) and in [In the kitchen and on the road]({{ '/en/projects/fornu/manual/cocina-y-reparto/' | relative_url }}).

## The base and the modules {#modulos}

Every account has the base: the orders board and its own delivery, the menu, stock items and stock, the cash drawer, expenses, the team with its devices, and the settings. Modules go on top, switched on per account:

| Module | What it adds |
|---|---|
| **Salón** (dining room) | Tables and sections, waiters with a PIN, rounds to the kitchen by course, split payments with tips, the counter and the express counter. |
| **Constructor de espacios** (space builder) | The floor plan with walls, floors, doors, windows and objects, seen from above or in isometric view. |
| **Delivery por plataformas** (platform delivery) | Rappi and PedidosYa on the same board, the menu published to each store, and sold-out items switched off by themselves. |
| **Facturación electrónica** (electronic invoicing) | Type A, B and C invoices with an ARCA CAE, automatic or by hand, their credit notes and the list for the accountant. |
| **Personal** (staff) | Attendance, PIN clock-in, schedules, payroll and advances. |
| **Proveedores y compras** (suppliers and purchases) | Suppliers with their tax ID and balance, and stock purchases that go into stock. |
| **Costos y márgenes** (costs and margins) | What needs reviewing, the cost sheet, the margin on each channel, and statistics. |
| **Reportes** (reports) | Sales summary and profitability by business unit and by channel. |

A module that is off does not appear on any screen, not even as a greyed-out button. What it saved is kept for when it is switched on again. Modules also come in groups meant for each kind of place: **Dark kitchen** (platforms, costs and reports), **Restaurante** (dining room, staff and invoicing), **Cafetería** (dining room and invoicing) and **Salón Pro** (dining room and builder).

## Roles and permissions {#permisos}

What each person sees and does comes from their roles. Each account builds its roles with the names the place uses (Parrillero, Moza, Caja) and with the permissions it chooses. How to build them is in [Staff]({{ '/en/projects/fornu/manual/personal/' | relative_url }}#roles). The account's **Administración** (administrator) can do everything the account has switched on. Every page of the manual says which permission each action needs, using these names:

| Permission | What it allows |
|---|---|
| Cocina (kitchen) | Confirming or cancelling orders, marking them ready, taking orders of your own, and logging waste and batches. |
| Mensajería (courier) | Taking your own orders out from a phone and seeing the cash on hand. |
| Pedidos (orders) | Seeing the history and detail of orders, and taking in the couriers' cash. |
| Carta (menu) | Creating and changing products, prices, categories and modifier groups, and publishing the menu. |
| Insumos (stock items) | Setting up ingredients, prepared items and supplies with their costs, recipes and categories. |
| Stock | Seeing the stock, logging counts, waste and batches, and planning production. |
| Caja (cash) | Opening and closing the drawer, recording movements and seeing sales. |
| Ver lo esperado (see expected) | Seeing what the system expects in the drawer before counting it. Without it, the count is blind. |
| Recontar la caja (recount) | Counting again after a count was confirmed. |
| Gastos (expenses) | Recording, paying and voiding expenses and purchases. Expense categories are set up with the Ajustes permission. |
| Equipo (team) | Adding staff and their PINs. |
| Dispositivos (devices) | Pairing tablets and phones and removing them. |
| Ajustes (settings) | Business units, stations, payment methods, customers and the account's configuration. |

Modules bring their own. The dining room brings **Atender mesas**, **Asignar quién atiende**, **Mover mesas**, **Anular lo mandado**, **Descontar e invitar**, **Cobrar mesas**, **Deshacer cobros**, **Cancelar mesas** and **Armar el salón**. Invoicing brings **Facturar**, **Ver facturas** and **Configurar la facturación**. Staff brings **Presentismo**, **Adelantos** and **Liquidación**. Suppliers and purchases brings **Proveedores**, Costs brings **Costos**, Reports brings **Reportes** and the builder brings **Biblioteca**.

A new account starts with three roles: **Cocina**, **Mensajería** and **Encargado/a** (manager: kitchen, orders, stock, cash with the expected amount and recounts, expenses and devices). The dining room adds three suggested ones: **Mozo** (waiter), **Adicionista** (order desk) and **Caja** (cashier).

## Words the app uses {#palabras}

| Word | What it means |
|---|---|
| Unidad de negocio (business unit) | Each brand the kitchen sells, with its menu, colour and channels. They all share the kitchen, the stock and the cash drawer. |
| Canal (channel) | Where a sale comes from: **Propios** (the place's own delivery), **Rappi**, **PedidosYa** or **Salón** (dining room). Each with its own price and commission. |
| Pedido propio (own order) | An order the place takes by phone or message and delivers with its own couriers. |
| Estación (station) | A part of the kitchen that makes part of the order: grill, kitchen, bar. Each gets its own ticket. |
| Comanda (ticket) | What the kitchen has to make for an order or a round, on screen or on paper. |
| Ronda (round) | What a waiter sends to the kitchen in one go from a table. |
| Tiempo (course) | When each thing goes out in the dining room: **Ya** (now), **Entrada** (starter), **Principal** (main) or **Postre** (dessert). |
| Insumo (stock item) | What goes into the menu: ingredients, items the kitchen prepares, and supplies such as packaging. |
| Elaboración (prepared item) | What the kitchen makes in batches with its own recipe, such as a sauce or burger patties. |
| Adicionales (extras) | What each sale carries besides the recipe, such as the delivery box or a sauce sachet. |
| Arqueo (cash count) | Counting the drawer when opening and closing it, and seeing the difference from what the system expects. |
| Rendición (handover) | When a courier hands in the cash collected on their orders. |
