---
title: Tools
description: Tools and libraries shipped as standalone repos.
permalink: /en/tools/
---

{% assign t = site.data.i18n[page.lang] %}
{% assign lang = page.lang %}
{% assign visible_tools = site.data.tools | where: "visibility", "public" %}

<section class="hero">
  <h1><span class="accent">{{ t.tools.heading }}</span></h1>
  <p class="lead">{{ t.tools.lead }}</p>
</section>

{% if visible_tools.size > 0 %}
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

<h2>{{ t.tools.notes_heading }}</h2>
<ul>
  <li>{{ t.tools.notes_semver }}</li>
  <li>{{ t.tools.notes_changelog }}</li>
</ul>
{% else %}
<p class="muted">{{ t.tools.empty }}</p>
<p class="muted">{{ t.tools.empty_long }}</p>
{% endif %}
