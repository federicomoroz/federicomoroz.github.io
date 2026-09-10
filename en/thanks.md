---
title: Thanks
description: Message sent.
permalink: /en/thanks/
sitemap: false
---

{% assign t = site.data.i18n[page.lang] %}

<section class="hero">
  <h1><span class="accent">{{ t.contact.thanks_heading }}</span></h1>
  <p class="lead">{{ t.contact.thanks_body }}</p>
  <div class="hero-actions">
    <a class="primary" href="{{ '/en/' | relative_url }}">{{ t.contact.thanks_back }}</a>
  </div>
</section>
