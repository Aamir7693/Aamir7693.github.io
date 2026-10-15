---
layout: about
title: about
permalink: /
subtitle: PhD student in Computer Science at <a href="https://www.csee.umbc.edu/">UMBC</a> · previously Data Scientist Intern at <a href="https://www.amd.com/">AMD</a> and <a href="https://www.esri.com/">Esri</a>

profile:
  align: right
  image: aamir-portrait.jpg
  image_circular: true # crops the image to make it circular
  more_info: >
    <p>DAMS Lab · Dept. of Computer Science and Electrical Engineering</p>
    <p>University of Maryland, Baltimore County</p>
    <p>Baltimore, MD</p>

selected_papers: true # shows papers marked selected={true} in papers.bib
social: true # social icons from _data/socials.yml at the bottom of the page

announcements:
  enabled: true # news items from _news/
  scrollable: true
  limit: 5

latest_posts:
  enabled: false # no blog
---

{% include home/style.liquid %}

I am a PhD student in Computer Science at the **University of Maryland, Baltimore County (UMBC)**, advised by [Prof. Roberto Yus](https://umbc.edu/academics/faculty/roberto-yus/) in the DAMS Lab. My research sits at the intersection of **privacy, data management and generative AI**: I build and evaluate LLM-based systems that help people understand and control how their data is used — for example [GenAIPABench](https://arxiv.org/abs/2309.05138), a benchmark for generative-AI privacy assistants (PETS 2024).

Alongside the PhD I have spent three summers in industry as a data scientist — at **AMD** (2024, 2025) building forecasting models, agentic analytics and a Snowflake semantic layer for manufacturing data, and at **Esri** (2026) fine-tuning small language models for next-action prediction over ArcGIS telemetry. I like problems where research ideas have to survive contact with real data and real users.

I'm happy to talk about research, collaborations or internships — email is the best way to reach me.

{% include home/logos.liquid %}

## experience &amp; education

<p class="tl-hint" style="font-size:.85rem;opacity:.7;margin:0 0 .4rem">Click a row to see details. Full version on the <a href="{{ '/cv/' | relative_url }}">CV page</a>.</p>

{% include home/timeline.liquid %}

<div class="home-cols" markdown="1">
<div markdown="1">

## interests

{% include home/interests.liquid %}

</div>
<div markdown="1">

## skills

{% include home/skills.liquid %}

</div>
</div>
