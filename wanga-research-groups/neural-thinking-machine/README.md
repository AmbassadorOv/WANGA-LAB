# Neural Thinking Machine — Initial Architecture

Status: INITIAL / EXPERIMENTAL

The Neural Thinking Machine (NTM) is the primary cognitive CPU of WANGA. It is not an ordinary research group, model runtime, or autonomous authority. It is the anchored high-level reasoning layer that receives bounded system state, evidence, version history, structural relations, and drift findings; performs higher-order logical analysis; and returns verified findings, repair candidates, or escalation requests.

## Core role

- High-level logical reasoning across research groups.
- Cross-version comparison and architectural change analysis.
- Historical intent recovery when the current architecture is unclear or blocked.
- Coordination of specialized drift analysis.
- Detection of logical conflicts, structural inconsistencies, and unresolved transitions.
- Return of findings to the originating subsystem with provenance.

## System position

`WANGA OS -> Neural Thinking Machine -> Research / Runtime / Network subsystems -> Evidence -> Neural Thinking Machine`

The network distributes computation. The Neural Thinking Machine anchors high-level reasoning. It does not require the whole network to become one shared brain.

## Operating principle

`OBSERVE -> REPRESENT -> COMPARE -> REASON -> DETECT CONFLICT -> PROPOSE REPAIR -> VERIFY -> RETURN`

A proposed repair is not automatically authoritative. Facts, observations, and historical artifacts remain distinct from inference and proposed changes.

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
- `letter_token_state`
- `word_sequence_state`
- `drift_orchestrator`
- `conflict_detector`
- `logic_repair_engine`
- `verification_gate`
- `architect_review_interface`

The 620-position/token structure and other symbolic matrices are intentionally treated as research inputs to be recovered and verified from the historical corpus before being frozen as implementation constants.
