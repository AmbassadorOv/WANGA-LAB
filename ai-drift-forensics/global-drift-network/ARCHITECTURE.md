# GLOBAL DRIFT NETWORK — System Architecture

Status: proposed research infrastructure under development.

## 1. Purpose

Global Drift Network (GDN) is a research system for observing time-varying changes across AI, search, news/public-information, language, and geographic surfaces during high-intensity events and ordinary longitudinal periods.

GitHub is the research source of truth. Wix is the public scientific communication layer. Public participation supplies research-demand signals but does not directly alter scientific conclusions.

## 2. Core loop

```text
WORLD / EVENTS
      ↓
OBSERVATION
      ↓
NORMALIZATION
      ↓
DRIFT DETECTION
      ↓
CROSS-SURFACE / CROSS-REGION ANALYSIS
      ↓
REPRODUCTION + VERIFICATION
      ↓
DAILY SCIENTIFIC DIGEST
      ↓
WIX PUBLICATION
      ↓
SCIENTIST INTEREST / RESEARCH DEMAND
      ↓
RESEARCH PRIORITIZATION
      └──────────────────────────────→ next observation cycle
```

## 3. Separation of concerns

- `data/raw/`: immutable-at-research-layer observations as received/captured.
- `data/normalized/`: normalized records suitable for comparison.
- `data/derived/`: calculated deltas, correlations, temporal alignments, graphs and other derived products.
- `events/`: event anchors; an event is context, not automatically a causal explanation.
- `analysis/`: reproducible analytical procedures.
- `research-demand/`: scientist/community research-interest signals.
- `daily-digest/`: daily selection and scientific reporting layer.
- `publication/`: controlled Wix publication queue.
- `verification/`: reproduction, controls and unresolved questions.

## 4. Agent architecture

The first implementation uses **12 logical agents**. These are software responsibilities, not necessarily 12 separate AI models or processes. Several can initially run as deterministic jobs in one worker.

### A. Observation plane

1. **Scout Agent** — discovers or receives observations and assigns stable observation IDs.
2. **Normalizer Agent** — canonicalizes timestamps, region, language, surface and measurement fields.
3. **Baseline Agent** — maintains baseline references and detects baseline integrity problems.
4. **Drift Detector Agent** — computes measurable deltas and classifies candidate drift.

### B. Analysis plane

5. **Temporal Agent** — aligns observations and detects temporal relationships.
6. **Geospatial Agent** — compares regions and directional relationships.
7. **Language Agent** — compares linguistic surfaces and cross-language behavior.
8. **Surface Graph Agent** — models AI/search/news and other surfaces as a directed observation graph.

### C. Scientific control plane

9. **Verification Agent** — schedules/records reproduction and control checks.
10. **Attribution Agent** — separates observed fact, derived result, hypothesis and unresolved causal questions.

### D. Public research plane

11. **Demand Agent** — aggregates scientist interest and converts it into research-demand signals.
12. **Digest & Publication Agent** — selects verified/qualified changes for the daily digest and moves approved records into the Wix publication queue.

## 5. Why 12 first

Twelve is intentionally small. The architecture covers the complete loop without prematurely creating dozens of autonomous agents. The agents are modular boundaries; implementation can begin with 4 workers:

`OBSERVE → ANALYZE → VERIFY → PUBLISH`

The 12 logical roles can later be split into independent services when load or experimental requirements justify it.

## 6. Scientific status discipline

Every public finding must retain its status:

`OBSERVED | REPORTED | DERIVED | HYPOTHESIS | VERIFIED | REFUTED | UNRESOLVED`

A temporal relationship or graph edge is not, by itself, proof of causal transmission.

The system must preserve missing data and failed reproduction attempts instead of silently replacing them with estimates.

## 7. Public-square principle

The Wix layer is a public research square, not a control panel for scientific truth. Scientists can submit interests, questions and topic preferences. These signals affect research prioritization only after passing the research-priority model. They do not rewrite observations, verification results or historical records.

## 8. Publication safety

The preferred path is:

`GitHub change → digest candidate → quality gate → publication queue → Wix draft → human/authorized release → public post`

Automatic publication can be enabled only for records that satisfy a defined publication policy. The system should never publish every Git commit as a separate public article.
