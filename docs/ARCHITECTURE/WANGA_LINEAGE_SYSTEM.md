# WANGA Lineage System — Universal Registry

This registry generalizes lineage tracking across every architectural layer.

## Scope

A lineage may be maintained for any first-class entity in WANGA, including:
- researchers and contributors
- research questions
- studies and research programs
- methods
- sources and datasets
- findings and claims
- ideas and concepts
- models
- architectures and architectural families
- components and interfaces
- software artifacts
- experiments and validations
- integrations ("marriages") between lineages
- descendants produced by any of the above

## Universal rule

Every entity has:
1. provenance — where it came from
2. lineage — what it developed from
3. descendants — what it produced
4. state — what happened to it
5. destination — where it currently participates
6. future — what it may produce next

A descendant is a first-class entity. It receives its own lineage record and can become a parent of another lineage.

## Lineage families

Different entity types can maintain their own family trees:
- Researcher Lineage
- Research Lineage
- Method Lineage
- Evidence Lineage
- Idea Lineage
- Architecture Lineage
- Artifact Lineage
- Experiment Lineage
- Integration Lineage

These are not isolated trees. They form a connected lineage graph.

## The marriage layer

When two or more lineages combine to produce a new architectural result, record an explicit INTEGRATION_EVENT.

An integration event records:
- participating lineage IDs
- reason for combination
- inherited elements from each lineage
- newly created elements
- resulting descendant IDs
- architectural destination
- evidence and source references
- decision/provenance references
- timestamp
- current state

An integration is itself a lineage node and may generate descendants.

## Recursive development

parent → descendant → new family → descendants

and:

lineage A + lineage B → integration lineage → descendant architecture → new lineage branches

There is no fixed maximum depth.

## Researcher lineage

Researcher records describe documented contribution history and relationships to projects, questions, methods, findings, and artifacts. This is a provenance record, not a judgment of researchers.

## Research lineage

Research programs and studies record their origins, questions, methods, evidence, findings, revisions, and descendants.

## Architectural integration

Every mature lineage should be connected to the architecture through explicit edges such as:
- CONTRIBUTES_TO
- INTEGRATES_INTO
- IMPLEMENTS
- REPRESENTS
- SUPPORTS
- DERIVES_FROM
- GENERATES
- VALIDATES

## Universal provenance rule

Never infer ancestry from similarity alone. Every lineage edge should have a source, artifact, decision, dated record, or explicit derivation. Unknown provenance remains explicitly unknown.

## Result

The WANGA Lineage System is intended to make the whole project traceable in both directions:

origin → development → integration → architecture → descendants

and:

current architecture → integrated lineage → ancestors → original source

This registry is the umbrella methodology. Specialized lineage registries may define domain-specific fields while remaining linked to this universal model.
