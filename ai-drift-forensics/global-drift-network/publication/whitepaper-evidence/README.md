# White Paper Evidence Infrastructure

This directory is the evidence-control layer for the Global Drift Network government White Paper.

## Purpose

Maintain a reproducible separation between:

- raw observations;
- measured drift signals;
- external sources;
- claims made in the White Paper;
- verification status;
- analysis and limitations;
- publication-ready material.

No unverified result should be presented as an established finding.

## Evidence status

- `OBSERVED` — measured by the Global Drift Network dataset.
- `SUPPORTED` — supported by an identified external source.
- `HYPOTHESIS` — proposed but not yet sufficiently tested.
- `REFUTED` — tested and not supported under the documented method.

## Structure

```text
whitepaper-evidence/
├── README.md
├── CLAIMS.md
├── evidence-registry.json
├── daily-runs/
├── snapshots/
├── sources/
├── analysis/
└── draft/
```

## Control rule

Every substantive White Paper claim should resolve to one or more evidence IDs. Each evidence item should preserve provenance, timestamp, method/version information, and enough metadata to reproduce or independently inspect the observation where permitted.

The evidence repository is a research record, not a substitute for legal or regulatory review.
