---
layout: page
title: Agentic analytics on manufacturing data
description: An LLM agent and a Snowflake semantic layer that let engineers ask questions of RMA and supply-chain data in plain English. AMD, 2024–2025.
img:
importance: 3
related_publications: false
---

Two internships at **AMD** in Austin, both about putting machine learning in front of engineers who don't write SQL.

**2025 — agentic analytics.**

- Built an **agentic RMA analytics system** (Smol Agents + Snowflake Cortex) that automates trend analysis and root-cause slicing over manufacturing data.
- Productized a **Snowflake semantic layer** across 15+ curated tables (metrics, joins, row-level access) so Cortex Analyst can answer natural-language questions — cutting recurring turnaround by ~85%.
- Developed a Cortex-based **log-triage pipeline** that extracts and summarizes errors, with prompts tuned to reduce token spend without losing extraction quality.
- Deployed production **Streamlit** apps for KPI exploration and AI-assisted insights used by leadership; standardized GenAI workflows with an internal evaluation process (safety, PII, latency) across a 20+ person team.

**2024 — supply-chain forecasting.**

- Improved forecasting accuracy by ~15% through feature engineering, validation design and model iteration on historical operational signals.
- Removed redundant features and fixed data leakage in training/validation pipelines; built automated batch-scoring pipelines (Dataiku → Snowflake) with prediction and model-health monitoring.

**Stack.** Snowflake & Cortex, Smol Agents, Dataiku, Streamlit, Python, SQL.
