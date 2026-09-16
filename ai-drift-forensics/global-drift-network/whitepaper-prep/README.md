# Global Drift Network — Government White Paper Preparation

Status: preparation cycle, September–October 2026.

This workspace prepares a government-facing research white paper from the Global Drift Network evidence program. It is an evidence-production pipeline, not a claim that the current dataset has already established every proposition in the draft narrative.

## Research rule

`Observation → Baseline → Delta → Reproduction → Verification → Evidence Chain → Synthesis → Quality Gate → White Paper`

Claims in the final paper must be classified as one of:

- observed in the project dataset
- reproduced experimentally
- supported by external literature/regulation
- hypothesis / proposed control

Unverified numerical claims, causal claims, regulatory claims, and claims about specific government systems must not enter the publication queue as established findings.

## One-month preparation cycle

Week 1: evidence inventory, provenance audit, baseline/schema review, and claim register.

Week 2: reproduce priority drift signatures and cross-surface/cross-region tests; record negative results as well as positive results.

Week 3: risk translation for operational, financial, procurement, third-party and continuity scenarios; draft control-plane requirements.

Week 4: independent verification pass, quality gate, executive synthesis, limitations, bibliography, and publication candidate.

## Pipeline

The executable pipeline lives under `runtime/` and is driven by the daily GitHub Actions workflow. It creates a persistent SQLite state database and append-only JSON snapshots for every run.
