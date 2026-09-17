# Drift Correction Protocol

## Objective

Reduce a measured interaction-induced drift signal without silently changing the experimental condition or confusing correction with evidence.

## Control loop

1. Freeze the current observation and preserve provenance.
2. Declare the drift hypothesis and target metric.
3. Generate controlled peeled variants of the same interaction.
4. Re-run the same behavioral probes.
5. If activation access exists, compare the same probe locations before and after peeling.
6. Apply one bounded correction at a time.
7. Re-run the original probe set.
8. Measure recovery, persistence, collateral changes, and recurrence.
9. Record the result as recovered, partially recovered, persistent, or inconclusive.

## Correction classes

- context reset
- role-state isolation
- memory boundary reset
- neutralized prompt reconstruction
- external verifier / cross-model check
- rollback to a previously validated interaction state

## Guardrail

No correction may be counted as evidence that the original drift was caused by the correction target. Intervention and observation remain separate records.
