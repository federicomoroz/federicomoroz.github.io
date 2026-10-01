---
title: Home
description: "Federico Palatnik Moroz: AI Engineer, backend e integraciones y Forward Deployed Engineer. Sistemas con IA donde el modelo propone y el código decide."
permalink: /es/
---

{% assign t = site.data.i18n[page.lang] %}
{% assign lang = page.lang %}
{% assign visible_projects = site.data.projects | where: "listed", true | where_exp: "p", "p.early != true" %}
{% assign cv_file = site.data.cv.cv_pdf[lang] %}

<section class="intro">
  <div>
    <h1 class="hero-name">{{ site.author.name }}</h1>
    <p class="claim">{{ t.hero.headline }}</p>
    <p class="roles">{% for r in t.hero.roles_list %}<span>{{ r }}</span>{% endfor %}</p>
  </div>
  <div class="intro-side">
    <div class="hero-actions">
      <a class="primary" href="{{ '/' | append: lang | append: '/projects/' | relative_url }}">{{ t.hero.cta_projects }}</a>
      {% if cv_file and cv_file != "" %}<a href="{{ '/cv/' | append: cv_file | relative_url }}" download>{{ t.hero.cta_cv }}</a>{% endif %}
    </div>
    {% include hero-contact.html t=t %}
  </div>
</section>

{% include lab.html lang=lang %}

<div class="section-heading">
  <h2>{{ t.home.projects_heading }}</h2>
  {% if visible_projects.size > 4 %}<a class="section-action" href="{{ '/' | append: lang | append: '/projects/' | relative_url }}">{{ t.home.view_all }}</a>{% endif %}
</div>

{% if visible_projects.size > 0 %}
<div class="project-grid">
  {% for proj in visible_projects limit:4 %}
    {% include project-card.html proj=proj lang=lang t=t i=forloop.index0 %}
  {% endfor %}
</div>
{% else %}
<p class="muted">{{ t.home.projects_empty }}</p>
{% endif %}

<div class="section-heading">
  <h2>{{ t.home.journey_heading }}</h2>
</div>

<section class="journey">
  <figure class="portrait"><img src="{{ '/assets/img/portrait.webp' | relative_url }}" alt="{{ t.home.portrait_alt }}" width="896" height="1088" loading="lazy" decoding="async"></figure>
  <div class="journey-text">
    <p class="journey-intro">{{ t.home.journey_intro }}</p>
    <p>{{ t.home.journey_origin }}</p>
    {% include journey.html lang=lang %}
    <a class="more" href="{{ '/' | append: lang | append: '/about/' | relative_url }}">{{ t.home.journey_more }}</a>
  </div>
</section>

{% include contact-section.html t=t lang=lang %}
