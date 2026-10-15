---
layout: page
title: Next-action prediction for ArcGIS Pro
description: Small language models over 163M telemetry events — predicting what an analyst will do next inside a desktop GIS. Esri, summer 2026.
img:
importance: 3
related_publications: false
---

**The problem.** ArcGIS Pro has thousands of tools, and users' sessions leave a trail of events. Can a model learn those sequences well enough to predict the next action — the first step toward in-app guidance and smarter defaults?

**What I built.**

- Fine-tuned **Gemma-3-1B** with LoRA/PEFT and extended its tokenizer with ~4,000 domain-specific single-token actions, so each ArcGIS event is one token rather than a phrase.
- Designed and trained a **compact decoder-only transformer from scratch**; it beat the fine-tuned 1B model on top-3 next-action accuracy (0.582 vs. 0.549) at a fraction of the parameters.
- Shipped a **Streamlit app** for interactive top-K prediction, and merged the LoRA adapter plus extended vocabulary into a single **GGUF for CPU inference with llama.cpp**.
- Mined **163.8M events across 137K sessions** into transition-probability workflow graphs to surface high-retention paths and drop-off points — large-scale process mining over real product usage.

**Stack.** PyTorch, Hugging Face, PEFT, llama.cpp, Streamlit, Python.
