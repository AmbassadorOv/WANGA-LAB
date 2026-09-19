# Candidate Discovery Tier Topology

## Objective

Define a bounded discovery topology for identifying people who may contribute through architectural reasoning, problem formation, cross-domain composition, and system redesign.

This is a discovery architecture, not a ranking of human worth or a claim that any candidate is inherently superior.

## Target scale

The operational target is approximately:

- **Tier 1 — 8–10 anchor candidates**
  - Strongest currently evidenced architectural signals.
  - Each anchor can serve as a node around which a research cluster is formed.
  - Target: 8–10, not a mandatory fixed count.

- **Tier 2 — ~100 cluster candidates**
  - Approximately 10 candidates associated with each Tier-1 anchor.
  - Selection is evidence-based and domain-diverse where possible.
  - A candidate may remain unassigned until evidence supports a cluster relationship.

- **Tier 3 — ~1,000 candidates**
  - Approximately 10 candidates per Tier-2 node.
  - Broader discovery layer for researchers, engineers, founders, scientists, designers, and other contributors whose artifacts show relevant architectural signals.

- **Tier 4+ — bounded expansion**
  - Do not expand automatically merely to increase the database.
  - Expansion requires a demonstrated research or infrastructure need.
  - The default stopping point is therefore approximately **1,000 additional candidates beyond the first 100**, subject to evidence quality and operational capacity.

## Topology

Tier 1 (8–10)
→ each anchor: ~10 Tier-2 candidates
→ each Tier-2 node: ~10 Tier-3 candidates

Nominal 10 × 10 × 10 structure:
**10 anchors → 100 cluster candidates → 1,000 broader candidates**

The topology is a discovery network, not a leaderboard.

## Selection rule

Candidates enter a tier only when supported by traceable evidence such as:

- published research or preprints;
- technical artifacts or open-source work;
- documented experiments;
- patents or technical disclosures;
- substantial technical essays;
- talks/lectures with inspectable claims;
- candidate-submitted work;
- open-ended challenge artifacts.

The system should preserve evidence provenance and uncertainty rather than collapse candidates into one scalar score.

## Cluster formation

Clusters should be formed around demonstrated intellectual/technical relationships, for example:

- shared problem architecture;
- complementary domains;
- compatible research methods;
- a common unresolved system problem;
- complementary evidence or implementation capabilities;
- a useful contradiction or alternative hypothesis.

The system must not manufacture relationships solely to fill a quota.

## Saturation / efficiency rule

Once the target topology has sufficient evidence coverage, additional discovery is lower priority unless it produces:

1. a materially new domain;
2. a materially new architectural pattern;
3. a missing capability;
4. a strong alternative hypothesis;
5. a verification or reconstruction capability;
6. a candidate who materially changes the architecture of the research network.

This keeps discovery bounded by information value rather than database size.

## Human review

Automated discovery may propose candidates and clusters. Human review is required before:

- Tier-1 placement;
- invitations to a research site;
- public association of a person with the network;
- any consequential opportunity allocation.

## Privacy and fairness

The system must use public, voluntarily submitted, or explicitly consented evidence. It must not infer architectural potential from protected or sensitive personal attributes, and it must not be used as an automated employment or admissions decision system.

## Implementation status

**SPECIFIED — research architecture.**

No candidate has been classified by this document alone.
