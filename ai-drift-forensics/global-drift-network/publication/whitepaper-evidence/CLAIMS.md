# White Paper Claim Ledger

Use this ledger before a claim enters the government-facing White Paper.

| Claim ID | Claim | Status | Evidence IDs | Method / Source | Verified | Section |
|---|---|---|---|---|---|---|
| DRIFT-CLAIM-001 | Behavioral change between a documented baseline and a later measurement period | HYPOTHESIS | — | Repeated measurement | false | Findings |
| DRIFT-CLAIM-002 | Drift may differ by surface, language, geography, or retrieval environment | HYPOTHESIS | — | Stratified comparison | false | Findings |
| DRIFT-CLAIM-003 | Changes observed during a high-salience political/economic period require controls for ordinary temporal variation | HYPOTHESIS | — | Stress-test design | false | Methodology |

## Rules

1. Do not convert `HYPOTHESIS` to `OBSERVED` without a corresponding measurement record.
2. Do not convert an observation into a causal claim without a design that supports causal inference.
3. External regulatory or research statements must cite their original source and publication date.
4. Every reported percentage must have a denominator, population/scope, measurement window, and calculation method.
5. Every drift result must state relevant alternative explanations, including provider changes, data/retrieval changes, prompt/context effects, and random variation.
