# Interaction Drift Institute

Research program for interaction-induced drift in language models: drift that emerges through the model's ongoing interaction with a user, conversation history, relational framing, personalization, role assignment, and repeated feedback loops.

## Scope

This institute is distinct from model-weight drift and deployment/configuration drift. It studies the interaction trajectory itself as a potential state-transition mechanism.

Core research questions:

1. What changes across turns even when the underlying model weights are unchanged?
2. Which changes are ordinary contextual adaptation versus measurable structural/behavioral drift?
3. Can user-induced interaction patterns predict later drift?
4. Which signals persist after stylistic and affective components are removed?
5. Can drift be detected early enough to trigger a bounded correction or rollback?

## Evidence boundary

Use public, reproducible, timestamped evidence wherever possible. Separate observation from hypothesis and causal interpretation. Never infer private communications or private individual activity.

## Primary model

`USER INTERACTION -> CONTEXT ACCUMULATION -> STATE/REPRESENTATION SHIFT -> BEHAVIORAL DRIFT -> DETECTION -> PEELING -> RESIDUAL AUDIT -> CORRECTION/ROLLBACK -> RECHECK`

## Research status

This is a research architecture, not a claim that every interaction change represents internal neural change. Internal activation claims require direct measurement access; black-box systems should be labeled behavioral/proxy evidence.
