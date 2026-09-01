---
title: Home
description: Portfolio de Federico Moroz. Backend, integraciones de APIs y sistemas distribuidos.
permalink: /es/
---

{% assign t = site.data.i18n[page.lang] %}
{% assign lang = page.lang %}
{% assign visible_projects = site.data.projects | where: "listed", true %}
{% assign visible_tools = site.data.tools | where: "visibility", "public" %}

<section class="hero">
  <p class="hero-eyebrow">{{ site.author.name }}</p>
  <h1>{{ t.hero.headline }}</h1>
  <p class="lead">{{ t.hero.lead }}</p>
  <p class="hero-metric">{{ t.hero.metric }}</p>
  {% assign cv_file = site.data.cv.cv_pdf[lang] %}
  <div class="hero-actions">
    <a class="primary" href="{{ '/' | append: lang | append: '/projects/' | relative_url }}">{{ t.hero.cta_projects }}</a>
    {% if cv_file and cv_file != "" %}<a href="{{ '/cv/' | append: cv_file | relative_url }}" download>{{ t.hero.cta_cv }}</a>{% endif %}
    <a href="{{ '/' | append: lang | append: '/about/' | relative_url }}">{{ t.nav.about }}</a>
  </div>
</section>

<hr>

<div class="section-heading">
  <h2>{{ t.home.projects_heading }}</h2>
  {% if visible_projects.size > 4 %}<a class="section-action" href="{{ '/' | append: lang | append: '/projects/' | relative_url }}">{{ t.home.view_all }}</a>{% endif %}
</div>

{% if visible_projects.size > 0 %}
<div class="project-list">
  {% for proj in visible_projects limit:4 %}
    {% include project-row.html proj=proj lang=lang t=t %}
  {% endfor %}
</div>
{% else %}
<p class="muted">{{ t.home.projects_empty }}</p>
{% endif %}

<div class="section-heading">
  <h2>{{ t.home.tools_heading }}</h2>
  {% if visible_tools.size > 3 %}<a class="section-action" href="{{ '/' | append: lang | append: '/tools/' | relative_url }}">{{ t.home.view_all }}</a>{% endif %}
</div>

{% if visible_tools.size > 0 %}
<p class="muted">{{ visible_tools.size }} {% if visible_tools.size == 1 %}{{ t.home.tools_intro_one }}{% else %}{{ t.home.tools_intro_count }}{% endif %}</p>

<div class="cards">
  {% for tool in visible_tools limit:3 %}
  <article class="card">
    <div class="card-header">
      <a class="card-title" href="{{ tool.repo }}" target="_blank" rel="noopener">{{ tool.name }}</a>
      {% if tool.version %}<span class="card-version">v{{ tool.version }}</span>{% endif %}
    </div>
    <div class="card-id">{{ tool.kind }}</div>
    <p class="card-desc">{{ tool.description[lang] | markdownify | strip_html | truncate: 160 }}</p>
    <div class="card-meta">
      {% for tech in tool.tech %}<span>{{ tech }}</span>{% endfor %}
    </div>
  </article>
  {% endfor %}
</div>
{% else %}
<p class="muted">{{ t.home.tools_empty }}</p>
{% endif %}
