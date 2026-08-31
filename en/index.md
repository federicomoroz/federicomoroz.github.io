---
title: Home
description: Federico Moroz's portfolio. Backend, API integrations and distributed systems.
permalink: /en/
---

{% assign t = site.data.i18n[page.lang] %}
{% assign lang = page.lang %}
{% assign visible_projects = site.data.projects | where: "listed", true %}
{% assign visible_tools = site.data.tools | where: "visibility", "public" %}

<section class="hero">
  <h1>{{ t.hero.welcome_prefix }} <span class="accent">{{ site.author.name }}</span>.</h1>
  <p class="lead">{{ t.home.profile_short }}</p>
  <p style="margin-top: 14px;"><a href="{{ '/' | append: lang | append: '/about/' | relative_url }}">{{ t.home.profile_link }}</a></p>
</section>

<h2>{{ t.home.purpose_heading }}</h2>
<p>{{ t.home.purpose_body }}</p>

<hr>

<div class="section-heading">
  <h2>{{ t.home.projects_heading }}</h2>
  {% if visible_projects.size > 0 %}<a class="section-action" href="{{ '/' | append: lang | append: '/projects/' | relative_url }}">{{ t.home.view_all }}</a>{% endif %}
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
  {% if visible_tools.size > 0 %}<a class="section-action" href="{{ '/' | append: lang | append: '/tools/' | relative_url }}">{{ t.home.view_all }}</a>{% endif %}
</div>

{% if visible_tools.size > 0 %}
<p class="muted">{{ visible_tools.size }} {{ t.home.tools_intro_count }}</p>

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
