# WANGA Thinking Machine — Agent Governor

The runtime is now a governor/trainer, not merely a layer generator.

## Core rule

Agents do not receive unrestricted authority. Each agent receives an internal ONTO_CREDIT: a non-monetary ontology permit bound to agent identity, ontology scope, iteration, and a bounded credit budget.

The token is a coordination and grounding primitive, not a financial currency.

## Anti-collision rules

1. One agent = one declared ontology scope.
2. An agent cannot write another agent's state.
3. Proposed actions require provenance.
4. Scope mismatch is rejected.
5. Conflicts use lease_then_arbitrate.
6. The governor may create, modify, retire, or refuse agents.
7. Increasing agent count is not itself a success criterion.

## Training loop

observe → receive ontology credit → propose → validate → coordinate → execute later → record provenance → retain/retire

The current bootstrap still produces specifications rather than arbitrary executable code. That boundary remains intentional.

## Scale path

1 governor → 10 agents → 100 agents → 1,000 agents

Scaling occurs only after governance and provenance checks, rather than by blindly spawning agents.
