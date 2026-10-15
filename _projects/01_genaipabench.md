---
layout: page
title: GenAIPABench
description: A benchmark for generative-AI privacy assistants — can an LLM answer questions about a privacy policy accurately, clearly and with the right citations?
img: assets/img/projects/genaipabench.png
importance: 1
related_publications: true
---

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/img/projects/genaipabench.png" title="Figure 1: a high-level overview of GenAIPABench" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  Figure 1 from the paper: the evaluator passes a privacy document and a bank of questions to a generative-AI privacy assistant through its API, stores the answers, and an analyst scores them on relevance, accuracy, clarity, completeness and references.
</div>

Privacy policies are long and hard to read, so people increasingly ask chatbots about them. **GenAIPABench** measures how well generative-AI assistants do at that job. An evaluator feeds an assistant real privacy policies and a graded set of questions, then scores the answers and summaries on relevance, accuracy, clarity, completeness, and whether they cite the right section of the policy.

In our PETS 2024 study {% cite hamid2024genaipabench %}, ChatGPT-4 and Bing AI generally did better than Bard; Bard was clear and relevant but struggled with citations, and all three degraded as the questions got harder — which is exactly where a privacy assistant matters most.

- **Paper:** [Privacy Enhancing Technologies 2024](https://doi.org/10.56553/popets-2024-0081) · [arXiv](https://arxiv.org/abs/2309.05138)
- **Code & data:** [github.com/DAMSlabUMBC/GenAIPABench](https://github.com/DAMSlabUMBC/GenAIPABench)
- **With:** Hemanth Reddy Samidi, Tim Finin, Primal Pappachan, Roberto Yus
