# Neural Thinking Machine — Initial Architecture

Status: INITIAL / EXPERIMENTAL

The Neural Thinking Machine (NTM) is the primary cognitive CPU of WANGA. It is not an ordinary research group, model runtime, or autonomous authority. It is the anchored high-level reasoning layer that receives bounded system state, evidence, version history, structural relations, drift findings, and formally represented research hypotheses; performs higher-order logical analysis; and returns verified findings, repair candidates, architecture candidates, or escalation requests.

## Core role

- High-level logical reasoning across research groups.
- Cross-version comparison and architectural change analysis.
- Historical intent recovery when the current architecture is unclear or blocked.
- Formalization of human research discoveries into testable hypotheses.
- Exploration of candidate computational architectures under WANGA-X.
- Coordination of specialized drift analysis.
- Detection of logical conflicts, structural inconsistencies, and unresolved transitions.
- Return of findings to the originating subsystem with provenance.

## Human discovery boundary

A researcher can introduce a **Discovery Trigger**. This may originate during ordinary work, reflection, sleep, or a dream.

The NTM does not need to explain or validate the origin. It must:

`DISCOVERY -> HYPOTHESIS -> REQUIREMENT -> ARCHITECTURE CANDIDATE -> EXPERIMENT -> EVIDENCE -> VERIFY`

A discovery is therefore an input to reasoning, not evidence of the resulting claim.

## System position

`WANGA OS -> Neural Thinking Machine -> Research / Runtime / Network subsystems -> Evidence -> Neural Thinking Machine`

Under WANGA-X, the architectural path may become:

`DISCOVERY/REQUIREMENT -> NTM -> BLUEPRINT -> MATERIALIZER -> EXECUTION -> EVIDENCE -> VERIFICATION -> NTM`

## Operating principle

`OBSERVE -> REPRESENT -> COMPARE -> REASON -> DETECT CONFLICT -> PROPOSE REPAIR/ARCHITECTURE -> VERIFY -> RETURN`

A proposed repair or architecture is not automatically authoritative. Facts, observations, historical artifacts, hypotheses, and proposed changes remain distinct.

## Initial-version rule

This architecture is an initial version. It must preserve earlier designs and research artifacts. When the current state is ambiguous or a research path becomes blocked:

`LOCATE_ORIGINAL -> READ_ORIGINAL -> COMPARE_WITH_CURRENT -> RECOVER_INTENT -> TEST -> VERIFY`

An older version is a historical reference point, not automatically the current truth and not disposable merely because a newer version exists.

## Planned internal components

- `high_logic_engine`
- `version_intelligence`
- `semantic_diff_engine`
- `architecture_diff_engine`
- `intent_recovery_engine`
- `discovery_formalizer`
- `requirement_deriver`
- `blueprint_reasoner`
- `architecture_candidate_engine`
- `letter_token_state`
- `word_sequence_state`
- `drift_orchestrator`
- `conflict_detector`
- `logic_repair_engine`
- `verification_gate`
- `architect_review_interface`
