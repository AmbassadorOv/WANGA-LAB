# Ontology Communication Protocol v0.1

## Purpose

A Thinking Machine exposes a governed communication boundary to an external AI.
The external AI does not inherit the internal ontology by default.

It must obtain an ONTO_CREDIT for a declared scope.

### Handshake

1. External AI requests a scope.
2. Gateway checks the requested scope.
3. Gateway checks provenance.
4. Gateway evaluates structural-weight requirements.
5. Gateway accepts or rejects the communication lease.
6. Accepted traffic remains scoped; the external AI cannot silently redefine the internal names.

### Token meaning

ONTO_CREDIT is currently a non-monetary access/coordination credential.
Commercial licensing can later map to credits, but no payment or financial token is implemented here.

### Structural-weight principle

Weights are not truth probabilities.
They regulate investigation and communication priority.

The first implementation uses configurable signals:

- source
- dependency
- contradiction
- depth
- evidence
- resolution

A structural contradiction can therefore receive more operational weight than many isolated local inconsistencies.

### Type-lock principle

The protocol keeps explicit distinctions between:

- NAME
- THING
- RELATION
- PROPOSITION
- INFERENCE

An external participant cannot silently change a name's role in the protocol and continue as though no transition occurred.

### Boundary

The gateway is a sandbox for the external AI that wants to communicate with the governed network. It is not merely a sandbox for an internal agent.
