---
layout: page
title: PrivacyLens
description: A deployed framework that finds, collects and analyzes the privacy policies of smart devices — past, present and future versions — at the scale of thousands of devices.
img: assets/img/projects/privacylens-arch.png
importance: 2
related_publications: true
---

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/img/projects/privacylens-arch.png" title="PrivacyLens architecture" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  How PrivacyLens works: policy collection finds manufacturers and their policy pages (present and past versions via the Wayback Machine) and sanitizes the text; policy analysis generates ML-based metadata — ambiguity, keywords, similarity, GDPR effects, last-update tracking.
</div>

**The problem.** Smart devices — cameras, locks, sensors, wearables — collect data continuously, and almost nobody reads the privacy policies that govern that data. For websites and apps there are tools that analyze policies automatically; for devices there wasn't even a reliable way to *find* the policies, let alone track how they change over time.

**What PrivacyLens does.** It is a deployed system that discovers manufacturers and their policy pages, collects the current policy together with past versions and watches for future ones, and runs NLP/ML analysis over the corpus: ambiguity and keyword analysis, similarity across devices, the effect of regulations such as GDPR, and when policies were last updated. On top of that corpus sit exploration tools for three audiences — consumers, policy writers and regulators.

**Scale and findings.** At the time of writing PrivacyLens had processed more than 1,200 policies covering over 7,300 devices. We used it to compare devices by category and by country of manufacture, classify policies, and measure how data-protection regulation changed company practices {% cite hamid2023privacylens %}.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/projects/privacylens-overview.png" title="PrivacyLens overview" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  The full picture from the paper: the collected corpus feeds a public website with exploration tools for consumers, regulators and policy writers — for example, comparing smart-lock policy updates across years or GDPR's effect on smart-camera policies by country.
</div>

- **Paper:** [arXiv:2308.05890](https://arxiv.org/abs/2308.05890) (2023)
- **Code:** [github.com/Aamir7693/privacy-lens](https://github.com/Aamir7693/privacy-lens)
- **Lab project page:** [DAMS Lab — PrivacyDocs](https://damslabumbc.github.io/project/privacydocs/)
- **With:** Hemanth Reddy Samidi, Tim Finin, Primal Pappachan, Roberto Yus
