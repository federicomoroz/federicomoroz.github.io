---
title: Services & tools
description: Services that plug into other systems (notifications, queues, gateways, webhooks) and small tools shipped as standalone repos.
permalink: /en/tools/
---

{% assign t = site.data.i18n[page.lang] %}
{% assign lang = page.lang %}
{% assign services = site.data.projects | where: "listed", true | where: "group", "service" %}
{% assign visible_tools = site.data.tools | where: "visibility", "public" %}

<section class="hero">
  <h1><span class="accent">{{ t.tools.heading }}</span></h1>
  <p class="lead">{{ t.tools.lead }}</p>
</section>

{% comment %}
  Services are entries of _data/projects.yml with `group: service`: they get the
  same card as the projects (cover, live preview, links), because they are the
  same kind of work, only smaller and meant to be plugged into something else.
{% endcomment %}
{% if services.size > 0 %}
<div class="section-heading">
  <h2>{{ t.services.heading }}</h2>
</div>
<p class="muted">{{ t.services.lead }}</p>
<div class="project-grid">
  {% for proj in services %}
    {% include project-card.html proj=proj lang=lang t=t i=forloop.index0 %}
  {% endfor %}
</div>
{% endif %}

<div class="section-heading">
  <h2>{{ t.tools.tools_heading }}</h2>
</div>
{% if visible_tools.size > 0 %}
<p class="muted">{{ t.tools.tools_lead }}</p>
<div class="cards">
  {% for tool in visible_tools %}
  <article class="card">
    <div class="card-header">
      <a class="card-title" href="{{ tool.repo }}" target="_blank" rel="noopener">{{ tool.name }} ↗</a>
      {% if tool.version %}<span class="card-version">v{{ tool.version }}</span>{% endif %}
    </div>
    <div class="card-id">{{ tool.kind }}</div>
    <div class="card-desc">{{ tool.description[lang] | markdownify }}</div>
    {% if tool.install %}
    <div class="install-block">
      <span class="install-label">{{ t.tools.install_label }}</span>
      <pre><code>{{ tool.install }}</code></pre>
    </div>
    {% endif %}
    <div class="card-meta">
      {% for tech in tool.tech %}<span>{{ tech }}</span>{% endfor %}
    </div>
  </article>
  {% endfor %}
</div>
{% else %}
<p class="muted">{{ t.tools.empty }}</p>
{% endif %}
