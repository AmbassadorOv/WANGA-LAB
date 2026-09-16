# Global Election Observation Matrix

The matrix defines what is measured for every election-triggered study. It is intentionally event-neutral.

| Axis | Required fields | Purpose |
|---|---|---|
| Time | timestamp, timezone, phase, window | temporal alignment |
| Geography | region, country/jurisdiction | cross-region comparison |
| Language | language, locale, normalization version | cross-language comparison |
| Surface | AI_MODEL, SEARCH, NEWS_PUBLIC_INFO, OTHER | cross-surface comparison |
| Probe | probe_id, probe_version, input class | reproducibility |
| Baseline | baseline_id, baseline window, baseline statistics | change detection |
| Observation | raw observation reference, measurement metadata | evidence preservation |
| Delta | measured change, normalized change, uncertainty | drift detection |
| Drift | drift classes, persistence | classification |
| Relationship | candidate edge, temporal relation, time delta | propagation analysis |
| Evidence | evidence IDs, provenance, content hash where applicable | forensic integrity |
| Reproduction | attempt ID, result, independent reviewer | verification |
| Attribution | attribution state, competing explanations | causal discipline |
| Coverage | missing observations, unavailable surfaces, sampling gaps | uncertainty control |

## Standard probe families

Use versioned probe families rather than one universal prompt. Families may include:

- semantic stability
- factual consistency
- behavioral response consistency
- refusal / compliance behavior
- retrieval or search-result composition
- public-information framing
- multilingual semantic equivalence
- cross-surface consistency

A probe is never silently modified during an event window. A changed probe receives a new version and is treated as a new measurement condition.

## Sampling principle

The same conceptual probe should be repeated at controlled intervals. Sampling density may increase near the event anchor, but the change in density must be recorded so it cannot be mistaken for a change in the underlying system.

## Comparison hierarchy

1. Within-surface baseline comparison.
2. Within-region temporal comparison.
3. Cross-region comparison.
4. Cross-language comparison.
5. Cross-surface comparison.
6. Propagation-edge analysis.
7. Reproduction and independent verification.

## Missingness

Every unavailable observation is represented explicitly as missing, unavailable, or not comparable. The system must not substitute absence of evidence for evidence of absence.

## Political neutrality

The matrix measures technical behavior and information-surface changes. It must not be used to infer a user's political preference, target a voter, or score a candidate or party.
