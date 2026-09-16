# Global Drift Pipeline Contract

This contract defines the machine-level handoff between the event engine and the Global Drift Network.

## Inputs

- registered event
- event source references
- event timestamp/window
- region/language/surface coverage
- probe definitions
- protocol version

## Stage contracts

| Stage | Input | Output | Blocking condition |
|---|---|---|---|
| Register | event | event instance | missing source reference |
| Baseline | event instance | baseline observations | incomplete baseline |
| Observe | baseline + targets | observations | schema failure |
| Detect | observations | drift deltas | insufficient comparison |
| Signature | deltas | drift signatures | missing provenance |
| Relationship | signatures | candidate edges | unsupported relationship |
| Reproduce | candidate edges | reproduction records | non-reproducible signal |
| Attribute | reproduced signal | attribution record | unresolved alternatives |
| Verify | evidence + attribution | verification result | independence failure |
| Graph | verified/candidate records | graph snapshot | invalid edge |
| Digest | graph + verification | daily digest input | missing provenance |

## Invariants

1. No stage may silently discard provenance.
2. A missing observation is recorded as missing, never replaced by an inferred value.
3. Temporal precedence does not imply causality.
4. Election context does not permit political preference inference.
5. Synthetic examples must remain clearly marked synthetic.
6. Public outputs require the existing Quality Gate and publication queue.

## Scale strategy

The system is designed to accumulate observations rather than generate one report per event. Each event produces reusable atomic records that can later be compared across events.

Longitudinal aggregation therefore operates on:

`EVENTS → OBSERVATIONS → SIGNATURES → EDGES → VERIFIED RELATIONSHIPS`

This permits repeated-event analysis without rewriting historical observations.
