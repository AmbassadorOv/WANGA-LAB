# Evaluation Lifecycle Re-entry Under Drift

**Evidence class:** PRIMARY PAPER  
**Window:** recent research identified within the 172-hour collection window.

## Abstract

A useful evaluation system should not assume that validation is a one-time gate. The recent five-phase framework for diagnostic and predictive medical AI describes evaluation across technical validation, operational robustness, controlled interaction, clinical evidence, and real-world integration. Its structure explicitly considers re-entry when systems or conditions change.

The broader architectural principle is:

**deployment is not the end of evaluation; it is a new observation environment.**

## Lifecycle

**Baseline → Technical validation → Operational validation → Controlled interaction → Real-world evidence → Monitoring → Trigger → Re-entry**

A drift trigger can arise from:

- a model version change;
- a data distribution change;
- a workflow change;
- a new population;
- a newly observed failure mode;
- a change in the operating environment.

## Why this matters

A single benchmark score compresses a trajectory into one number. A lifecycle model preserves the dependency between system state, environment, evidence, and subsequent evaluation.

For forensic work, the important object is therefore not merely the score but the evidence chain:

**which system → under which conditions → using which data → producing which behavior → evaluated by which procedure.**

## Cross-domain composition

Medicine provides one concrete instantiation. The same lifecycle can be tested in finance, insurance, cybersecurity, industrial control, and scientific computing.

The domain-specific rules change; the state-transition structure can remain comparable.

## Research questions

1. What events should automatically trigger re-evaluation?
2. Which evidence must be preserved before a new evaluation begins?
3. How can version changes be separated from environmental changes?
4. Which evaluation phases can be skipped, and under what documented conditions?

## Source

* A five-phase evaluation framework for diagnostic and predictive medical artificial intelligence*, npj Digital Medicine, 2026. citeturn0news14

**Status:** RESEARCH DRAFT; domain transfer is a proposed research composition, not a claim that the medical framework has been validated in other sectors.
