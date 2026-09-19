# WANGA Neural Architecture Network

The WANGA Neural Architecture Network (NAN) is the communication fabric surrounding the WANGA architectural system. It does not replace the architecture graph; it provides the typed communication layer through which architectural nodes exchange state, events, evidence references and bounded work signals.

## Two questions

Vitruvius answers: what is connected to what?

NAN answers: how does information propagate across those connections?

## Position

VITRUVIAN SCALE -> ARCHITECTURE GRAPH -> NEURAL NETWORK -> DIGITAL ENGINE -> MODELS / AGENTS -> EVIDENCE -> VERIFICATION -> STATE UPDATE

## One-to-one communication contract

Every architecture node has a stable identity. Communication uses typed messages: STATE_UPDATE, WORK_REQUEST, CAPABILITY_SIGNAL, EVIDENCE_REFERENCE, IMPACT_SIGNAL and VERIFICATION_RESULT. Each message contains source, target, type, payload, deterministic routing weight and evidence state.

## Neural routing

For every registered relationship, the engine computes a deterministic attention-like weight. This is an executable seam where a learned attention/model component can later be attached through Model Fabric. The current implementation is therefore a neural-network communication architecture, not a claim that the network has already been trained.

## Closed loop

ARCHITECTURE CHANGE -> VITRUVIUS DISCOVERY -> NEURAL MESSAGE -> DIGITAL ENGINE -> MODEL / AGENT EXECUTION -> EVIDENCE -> VERIFICATION -> STATE UPDATE -> VITRUVIAN GRAPH UPDATE

## Boundaries

Vitruvius discovers and maps relationships. NAN transports and weights communication. Global Work Manager controls work. Digital Engine executes. Evidence and Provenance preserves events. Verification establishes state. Rational Logic remains a protected reasoning boundary.

No activation or message can promote an unverified relationship to VERIFIED.
