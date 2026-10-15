---
layout: page
permalink: /people/
title: people
description: The people I work with and learn from. Edit <code>_data/people.yml</code> or use the dashboard to add someone.
nav: true
nav_order: 6
---

<style>
  .people-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 1rem; margin: 0.5rem 0 2rem; }
  .person-card { display: flex; gap: 0.85rem; align-items: flex-start; padding: 0.9rem; border: 1px solid rgba(128,128,128,0.3); border-radius: 10px; background: rgba(128,128,128,0.06); }
  .person-avatar { flex: 0 0 56px; width: 56px; height: 56px; border-radius: 50%; object-fit: cover; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 1.1rem; background: rgba(128,128,128,0.25); }
  .person-name { font-weight: 600; margin: 0 0 0.15rem; }
  .person-meta { font-size: 0.9rem; opacity: 0.8; line-height: 1.35; margin: 0; }
  .person-note { font-size: 0.85rem; opacity: 0.75; margin: 0.35rem 0 0; }
</style>

{% assign roles = "Advisor|Mentor|Collaborator|Student" | split: "|" %}
{% for role in roles %}
  {% assign group = site.data.people | where: "role", role %}
  {% if group.size > 0 %}
    {% case role %}
      {% when "Advisor" %}{% assign heading = "Advisor" %}
      {% when "Mentor" %}{% assign heading = "Mentors" %}
      {% when "Collaborator" %}{% assign heading = "Collaborators" %}
      {% else %}{% assign heading = "Students" %}
    {% endcase %}

## {{ heading }}

<div class="people-grid">
{% for person in group %}
  {% assign parts = person.name | split: " " %}
  <div class="person-card">
    {% if person.image %}
      {% if person.image contains "://" %}{% assign src = person.image %}{% else %}{% assign src = person.image | relative_url %}{% endif %}
      <img class="person-avatar" src="{{ src }}" alt="{{ person.name }}">
    {% else %}
      <div class="person-avatar" aria-hidden="true">{{ parts.first | slice: 0 }}{{ parts.last | slice: 0 }}</div>
    {% endif %}
    <div>
      <p class="person-name">{% if person.url %}<a href="{{ person.url }}">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}</p>
      <p class="person-meta">{% if person.title %}{{ person.title }}<br>{% endif %}{{ person.affiliation }}</p>
      {% if person.note %}<p class="person-note">{{ person.note }}</p>{% endif %}
    </div>
  </div>
{% endfor %}
</div>
  {% endif %}
{% endfor %}
