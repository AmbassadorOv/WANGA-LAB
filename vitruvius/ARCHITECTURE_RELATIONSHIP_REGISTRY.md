# Vitruvius Architecture Relationship Registry

This registry is the control-plane contract for connecting WANGA architectures, work branches, research assets, and verification boundaries.

## Rule

Vitruvius discovers, normalizes, classifies and proposes relationships. It does not make a relationship scientifically true merely by placing it in the graph.

Relationship lifecycle: DISCOVERED → CANDIDATE → MAPPED → IMPLEMENTED → TESTED → VERIFIED

When an architecture changes, Vitruvius resolves direct and transitive relationships, resolves matching work-branch patterns, and emits an affected-work set for the Global Work Manager.

## Branch rule

A Git branch is a work location, not an architecture. Branches are linked to architecture nodes through declared branch patterns and canonical branch mappings.

## Safety boundaries

- No automatic merge.
- No automatic promotion to VERIFIED.
- No protected Rational Logic implementation disclosure.
- No model or agent becomes its own verification authority.
- No branch is deleted as part of graph reconciliation.
