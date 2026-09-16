# Daily Scientific Digest

The Daily Scientific Digest converts repository changes and validated observations into a public research update.

## Pipeline

`GitHub changes → observation/analysis scan → evidence classification → quality gate → digest → publication queue → Wix`

## Public sections

1. **Observed Changes** — directly measured changes with source references.
2. **Derived Findings** — computed metrics and comparisons, explicitly marked as derived.
3. **Reproduced / Verified** — findings that passed the applicable verification gates.
4. **Unresolved Questions** — gaps, failed reproductions, and competing explanations.
5. **Research Demand** — aggregated scientist interest signals by topic.
6. **Next Research Actions** — proposed follow-up measurements.

## Rules

- A hypothesis is never presented as an observation.
- A Git commit is not itself evidence of an external event.
- Missing data remain explicit nulls.
- Public output references the source commit and relevant evidence/report IDs.
- Research-interest votes prioritize investigation; they do not alter measurements, evidence, or conclusions.
- Draft-first publication is the default. Automatic publication requires a passing quality gate.
