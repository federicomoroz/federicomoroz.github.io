---
title: Projects
description: Personal and team projects, with technical write-ups.
permalink: /en/projects/
---

{% assign t = site.data.i18n[page.lang] %}
{% assign lang = page.lang %}
{% assign visible_projects = site.data.projects | where: "listed", true %}

<section class="hero">
  <h1><span class="accent">{{ t.projects.heading }}</span></h1>
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

{% if visible_projects.size > 0 %}
<div class="project-list">
  {% for proj in visible_projects %}
    {% include project-row.html proj=proj lang=lang t=t %}
  {% endfor %}
</div>
{% endif %}
