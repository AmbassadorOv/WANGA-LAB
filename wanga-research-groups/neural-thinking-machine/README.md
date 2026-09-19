# Neural Thinking Machine — Initial Architecture

Status: INITIAL / EXPERIMENTAL

The Neural Thinking Machine (NTM) is the primary cognitive CPU of WANGA. It is the high-level reasoning layer that receives bounded system state, evidence, version history, structural relations, drift findings, and formally represented research hypotheses; performs higher-order logical analysis; and returns verified findings, repair candidates, architecture candidates, or escalation requests.

## Core role

- High-level logical reasoning across research groups.
- Cross-version comparison and architectural change analysis.
- Historical intent recovery when the current architecture is unclear or blocked.
- Formalization of human research discoveries into testable hypotheses.
- Derivation and exploration of required neural computations under WANGA-X.
- Exploration of candidate computational architectures.
- Coordination of specialized drift analysis.
- Detection of logical conflicts and structural inconsistencies.
- Return of findings with provenance.

## Human discovery boundary

A researcher can introduce a **Discovery Trigger**. This may originate during ordinary work, reflection, sleep, or a dream.

The NTM does not need to explain or validate the origin. It must:

`DISCOVERY -> HYPOTHESIS -> REQUIREMENT -> REQUIRED NEURAL COMPUTATION -> ARCHITECTURE CANDIDATE -> BLUEPRINT -> EXPERIMENT -> EVIDENCE -> VERIFY`

A discovery is therefore an input to reasoning, not evidence of the resulting claim.

## WANGA-X core route

The NTM participates in the central causal chain:

`USER QUERY / SYSTEM REQUEST -> REQUIREMENT -> REQUIRED NEURAL COMPUTATION -> NTM ARCHITECTURE REASONING -> BLUEPRINT / IR -> MATERIALIZER -> NEURAL COMPUTER -> EXECUTION -> EVIDENCE -> VERIFICATION`

The NTM does not replace the materializer. Its role is to reason about what neural computation is required and what computational structures can implement it.

## System position

`WANGA OS -> Neural Thinking Machine -> Research / Runtime / Network subsystems -> Evidence -> Neural Thinking Machine`

## Operating principle

`OBSERVE -> REPRESENT -> COMPARE -> REASON -> DETECT CONFLICT -> DERIVE REQUIRED COMPUTATION -> PROPOSE ARCHITECTURE / BLUEPRINT -> VERIFY -> RETURN`

A proposed repair or architecture is not automatically authoritative. Facts, observations, historical artifacts, hypotheses, and proposed changes remain distinct.

## Initial-version rule

This architecture is an initial version. It must preserve earlier designs and research artifacts. When the current state is ambiguous or a research path becomes blocked:

`LOCATE_ORIGINAL -> READ_ORIGINAL -> COMPARE_WITH_CURRENT -> RECOVER_INTENT -> TEST -> VERIFY`

## Planned internal components

- `high_logic_engine`
- `version_intelligence`
- `semantic_diff_engine`
- `architecture_diff_engine`
- `intent_recovery_engine`
- `discovery_formalizer`
- `requirement_deriver`
- `neural_computation_deriver`
- `blueprint_reasoner`
- `architecture_candidate_engine`
- `letter_token_state`
- `word_sequence_state`
- `drift_orchestrator`
- `conflict_detector`
- `logic_repair_engine`
- `verification_gate`
- `architect_review_interface`

## Dynamic architecture research foundation

NTM architecture reasoning is connected to WANGA-X research foundations including HLS, specialized accelerator synthesis, requirement-to-architecture synthesis, dynamic neural networks, neural architecture search, generated parameters, structural neural transformation, conditional computation, hardware-aware neural design, and runtime/adaptive architecture.

The central WANGA-X distinction is:

**Existing dynamic-neural direction:** an existing neural system adapts its structure or parameters.

**WANGA-X research direction:** the user's query determines the required neural computation; the required neural computation determines the Blueprint; the Blueprint determines the neural computer.

When requirements change:

`CHANGED REQUIREMENT -> NEW REQUIRED NEURAL COMPUTATION -> NEW BLUEPRINT -> RECOMPOSE / REBUILD / REPLACE`

The research foundations and prototype boundary are documented in `docs/WANGA_X_NEURAL_COMPUTATION_PARADIGM.md` and `docs/WANGA_X_RESEARCH_FOUNDATIONS.md`.
