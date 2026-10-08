---
title: Articles
description: "Technical notes with measured numbers: what changes, by how much and how to reproduce it."
permalink: /en/articles/
---

{% assign t = site.data.i18n[page.lang] %}
{% assign lang = page.lang %}
{% assign articles = site.data.articles | where: "listed", true | sort: "date" | reverse %}

<section class="hero">
  <h1>{{ t.articles.heading }}</h1>
  <p class="lead">{{ t.articles.lead }}</p>
</section>

{% if articles.size > 0 %}
<div class="project-grid">
  {% for a in articles %}
    {% include article-card.html a=a lang=lang t=t %}
  {% endfor %}
</div>
{% else %}
<p class="muted">{{ t.articles.empty }}</p>
{% endif %}
