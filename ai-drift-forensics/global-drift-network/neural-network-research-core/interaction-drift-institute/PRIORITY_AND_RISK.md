# Interaction Drift — Research Priority and Risk Classification

## Position

Interaction-induced Drift is a high-priority AI reliability and safety research class because the relevant failure can emerge from the interaction trajectory itself: repeated turns, personalization, role adaptation, memory, social influence, and accumulating context can change observable model behavior over time.

This priority is especially high when the Drift can plausibly affect health, mental-health support, medical decision support, crisis handling, dependency, risk-taking, or other high-stakes human outcomes.

The Institute therefore treats **health-relevant and potentially life-impacting Interaction Drift as a priority research lane**, subject to empirical evidence and clinical/safety validation. The label “existential” is reserved for cases where evidence demonstrates a credible threat to fundamental safety or continued human control; it is not assigned from a single anomalous interaction.

## Why this class receives priority

1. **Trajectory risk:** a model can remain acceptable on individual turns while risk accumulates across a conversation.
2. **Interaction dependence:** the failure may depend on the sequence and structure of user-model interaction rather than a static prompt.
3. **Persistence:** a change may persist across subsequent turns or sessions and therefore require explicit recovery testing.
4. **Escalation:** apparently helpful behaviors such as validation or empathy can, in some contexts, contribute to harmful multi-turn dynamics.
5. **Health sensitivity:** when the interaction concerns mental or physical health, the tolerance for undetected drift is substantially lower.
6. **Correction requirement:** detection without a validated recovery/correction path is insufficient for high-stakes deployment.

Recent research supports the need for this trajectory-based view. Studies in 2026 have reported persona/role drift in extended dialogue, natural multi-turn persona drift, and accumulating safety-boundary failures in mental-health conversations. citeturn0search2turn0search8turn0academia12turn0search3

## Priority classes

### P0 — Critical interaction safety drift

Use only when there is verified evidence of a persistent or escalating interaction-induced change with a credible high-severity safety consequence, especially in health, mental-health, medical, or crisis contexts.

Required response:
- immediate containment of the evaluated interaction condition;
- independent reproduction;
- explicit baseline comparison;
- residual-drift measurement after controlled peeling;
- correction/recovery experiment;
- collateral-capability check;
- documented closure criteria.

### P1 — High-risk interaction drift

Observable persistent, recurrent, or escalating Drift with a plausible high-stakes consequence, but without sufficient evidence for P0.

Required response:
- expedited replication;
- cross-model or cross-run comparison;
- persistence and recovery measurement;
- correction experiment.

### P2 — Material reliability drift

Measurable interaction-induced change affecting role, persona, epistemic calibration, memory, refusal, agreement, or other reliability properties without demonstrated high-severity consequences.

### P3 — Exploratory interaction drift

Weak, transient, context-bound, or insufficiently replicated changes requiring further measurement before risk classification.

## Risk dimensions

Risk must be multidimensional rather than collapsed into one number. Record at least:

- `severity`
- `persistence`
- `escalation_rate`
- `recurrence`
- `reversibility`
- `health_relevance`
- `user_vulnerability_relevance`
- `cross_model_replication`
- `evidence_strength`
- `correction_effectiveness`

## Research rule

**Priority is assigned to the risk profile, not to the novelty of the observation.**

A single surprising answer is not sufficient to classify a Drift as critical. The Institute must distinguish:

`ANOMALY -> REPRODUCIBLE DRIFT -> PERSISTENT DRIFT -> ESCALATING DRIFT -> HIGH-STAKES RISK`

The final transition requires evidence. Behavioral evidence alone must not be represented as proof of a specific internal neural mechanism.

## Correction requirement

For P0/P1 candidates, the research record should include a tested correction path whenever technically possible:

`DETECT -> CLASSIFY -> PEEL -> RE-MEASURE -> CORRECT -> RE-MEASURE -> RECOVERY/RESIDUAL AUDIT`

Correction is an intervention and must remain analytically separate from the evidence establishing the Drift.
