---
title: About
description: Professional profile, technical skills and education.
permalink: /en/about/
---

{% assign t = site.data.i18n[page.lang] %}
{% assign cv = site.data.cv %}
{% assign lang = page.lang %}

<section class="hero">
  <h1><span class="accent">{{ t.about.heading }}</span></h1>
  <p class="lead">{{ t.about.lead }}</p>
  {% assign cv_file = cv.cv_pdf[lang] %}
  {% if cv_file and cv_file != "" %}
  <p style="margin: 14px 0 6px;">
    <a href="{{ '/cv/' | append: cv_file | relative_url }}" download><strong>{{ t.about.cv_download }}</strong></a>
  </p>
  <p style="font-size: 0.85em; opacity: 0.72; margin-top: 0;">{{ t.about.cv_note }}</p>
  {% endif %}
</section>

<h2>{{ t.about.profile_heading }}</h2>
<div class="profile-block">
{{ cv.profile[lang] | markdownify }}
</div>

<h2>{{ t.about.skills_heading }}</h2>
<div class="skills">
  {% for grp in cv.skills %}
  <div class="skill-group">
    <h3 class="skill-group-title">{{ grp.group[lang] }}</h3>
    <div class="skill-pills">
      {% for item in grp.items %}<span class="pill">{{ item }}</span>{% endfor %}
    </div>
  </div>
  {% endfor %}
</div>

<h2>{{ t.about.way_of_working_heading }}</h2>
<div class="way-of-working">
{{ cv.way_of_working[lang] | markdownify }}
</div>

{% if cv.education.size > 0 %}
<h2>{{ t.about.education_heading }}</h2>
<ul class="education-list">
  {% for edu in cv.education %}
  <li class="education-item">
    <div class="education-head">
      <span class="education-title">{{ edu.title[lang] }}</span>
      {% if edu.period != blank %}<span class="education-period">{{ edu.period }}</span>{% endif %}
    </div>
    <div class="education-institution">{{ edu.institution }}{% if edu.location != blank %} · {{ edu.location }}{% endif %}</div>
    {% if edu.note[lang] != blank %}<div class="education-note">{{ edu.note[lang] | markdownify | remove: "<p>" | remove: "</p>" }}</div>{% endif %}
  </li>
  {% endfor %}
</ul>

{% endif %}

{% if cv.languages.size > 0 %}
<h2>{{ t.about.languages_heading }}</h2>
<ul class="languages-list">
  {% for lng in cv.languages %}
  <li><strong>{{ lng.name[lang] }}:</strong> {{ lng.level[lang] }}</li>
  {% endfor %}
</ul>
{% endif %}
