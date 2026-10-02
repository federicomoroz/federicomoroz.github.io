---
title: Proyectos
description: Proyectos propios y de equipo, con write-ups tecnicos.
permalink: /es/projects/
---

{% assign t = site.data.i18n[page.lang] %}
{% assign lang = page.lang %}
{% comment %} Services (notify-router, task-queue...) live in /tools/, next to the tools. {% endcomment %}
{% assign visible_projects = site.data.projects | where: "listed", true | where_exp: "p", "p.group != 'service'" %}

<section class="hero">
  <h1>{{ t.projects.heading }}</h1>
  {% if visible_projects.size > 0 %}
  <p class="lead">{{ t.projects.lead_with_items }}</p>
  {% else %}
  <p class="lead">{{ t.projects.lead_empty }}</p>
  {% endif %}
</section>

<div class="callout">
  <p class="callout-title">{{ t.projects.capabilities_heading }}</p>
  <p>{{ t.projects.capabilities_note }}</p>
</div>

{% assign main_projects = visible_projects | where_exp: "p", "p.early != true" %}
{% assign early_projects = visible_projects | where: "early", true %}

{% if main_projects.size > 0 %}
<div class="project-grid">
  {% for proj in main_projects %}
    {% include project-card.html proj=proj lang=lang t=t i=forloop.index0 %}
  {% endfor %}
</div>
{% endif %}

{% if early_projects.size > 0 %}
<div class="section-heading">
  <h2>{{ t.projects.early_heading }}</h2>
</div>
<p class="muted">{{ t.projects.early_note }}</p>
<ul class="early-list">
  {% for proj in early_projects %}
  <li>
    <b>{% if proj.repo %}<a href="{{ proj.repo }}" target="_blank" rel="noopener">{{ proj.name }}</a>{% else %}{{ proj.name }}{% endif %}</b>
    <span>{{ proj.short[lang] | markdownify | strip_html | strip }}</span>
    <small>{{ proj.tech | join: ", " }}</small>
  </li>
  {% endfor %}
</ul>
{% endif %}
