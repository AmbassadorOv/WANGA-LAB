# Vitruvius Work Protocol — WANGA Politeia & Copernicus Inquiry
Status: PROTOCOL SPECIFICATION
Version: 0.1.0
Scope: VITRUVIUS QUESTION INQUIRY / LINEAGE / STABILITY
Projects: WANGA Politeia, WANGA Copernicus
Branch: agent/codex-002/vitruvius-politeia-copernicus-inquiry-protocol

## 1. Purpose

This protocol defines the order in which Vitruvius investigates questions concerning WANGA Politeia and the WANGA Copernicus project.

The protocol is evidence-first. A model may generate hypotheses, classifications, or candidate relationships, but it must not promote an unsupported claim into lineage, history, stability, or governance status.

The protocol separates:
- entry assessment;
- lineage reconstruction;
- generation-by-generation stability review;
- evidence and provenance;
- unresolved questions and conflicts.

## 2. Entry Gate — ALGORITHMIC_HISTORY_OPINION

Lineage review does not begin immediately.

The first mandatory operation is an opinion/review of the algorithmic history of the entity being considered.

The purpose of this gate is to determine whether the available record supports proceeding to lineage analysis.

Minimum questions:

1. Is the entity identifiable?
2. Is its algorithmic history sufficiently documented?
3. Is there evidence of stable behavior under the applicable test scope?
4. Are there unresolved material integrity findings?
5. Are provenance and evidence sufficient to distinguish recorded history from model inference?
6. Are there material contradictions that prevent a stable preliminary determination?

Entry status:

- ACCEPTED — sufficient evidence exists to begin lineage review.
- REJECTED — the available evidence identifies a material blocking condition.
- UNKNOWN — evidence is insufficient to determine entry status.
- CONFLICT — material sources or observations conflict and require resolution.

Only ACCEPTED permits progression to the five-generation review.

## 3. Recursive Five-Generation Stability Review

After the entry gate is ACCEPTED, Vitruvius does not perform a single linear five-generation check. The check is recursive across the lineage graph.

Every accepted lineage node becomes the root of its own backward review. For each node, its parent/ancestor links are expanded and each resulting node must itself satisfy the same entry/stability condition, subject to the defined five-generation depth.

Canonical rule:

`NODE[n] → PARENTS[n-1] → PARENTS[n-2] → ... → GENERATION[n-5]`

and, recursively, every discovered parent node is itself evaluated under the same five-generation rule.

Thus, a generation does not merely contribute one record. Each discovered ancestor creates a new verification path extending five generations backward. The resulting structure is a branching lineage graph rather than a single five-row chain.

For every generation/node, record:

- identity;
- lineage relation;
- source/provenance;
- algorithmic history;
- applicable tests;
- observed stability;
- evidence references;
- validation state;
- contradictions;
- unresolved uncertainty;
- reviewer decision.

A missing link must remain UNKNOWN. It must not be filled by probability, similarity, narrative completion, or model imagination.

## 4. Stability Criterion

“Stable” is a test result, not an impression.

A generation may be marked STABLE only when the applicable predefined evaluation scope has been executed or otherwise supported by admissible evidence and no material unresolved integrity issue blocks the determination.

Generation statuses:

- STABLE
- UNSTABLE
- UNKNOWN
- CONFLICT

The exact tests and thresholds must be declared for the relevant inquiry before a final stability status is assigned.

## 5. Lineage Verification Rule

The final lineage result is:

LINEAGE_STABILITY_VERIFIED

only when all of the following are true:

1. ALGORITHMIC_HISTORY_OPINION = ACCEPTED;
2. every required parent/ancestor branch is explicitly identified, or its absence is recorded as a blocking condition;
3. every required node in the recursive five-generation scope has a STABLE result;
4. provenance exists for the lineage relations;
5. evidence is preserved and traceable;
6. no unresolved material conflict invalidates the conclusion.

Otherwise the result must remain:

NOT_VERIFIED

with the blocking status explicitly recorded.

## 6. Human/Biological Lineage Separation

Where a question concerns a human or claimed blood lineage, biological lineage and algorithmic lineage must be represented as separate evidence dimensions.

A biological relationship is not inferred from an algorithmic relationship, and an algorithmic relationship is not inferred from a biological relationship.

For biological lineage claims, each asserted link requires its own documented provenance. An absent or unverifiable link remains UNKNOWN.

No model-generated genealogy is accepted as evidence merely because it is internally coherent.

## 7. Vitruvius Question-Handling Order

For every relevant question from WANGA Politeia or WANGA Copernicus, Vitruvius must process:

1. DEFINE THE QUESTION
2. IDENTIFY THE ENTITY
3. IDENTIFY THE CLAIM TYPE
4. CHECK ENTRY GATE
5. COLLECT SOURCE / PROVENANCE
6. RECONSTRUCT LINEAGE
7. REVIEW FIVE GENERATIONS
8. TEST STABILITY
9. RECORD CONFLICTS AND UNKNOWN STATES
10. SEPARATE FACT FROM INFERENCE
11. ISSUE THE CURRENT DETERMINATION
12. PRESERVE THE EVIDENCE CHAIN

A prediction may guide the investigation but cannot substitute for an evidence record.

## 8. WANGA Politeia Interface

For WANGA Politeia, the resulting record may be consumed by the lineage/governance knowledge layer.

The protocol must preserve the distinction between:

- lineage fact;
- algorithmic-history observation;
- stability finding;
- inference;
- prediction;
- governance decision.

Vitruvius does not erase earlier lineage history when a later determination changes. It appends the new determination as a dated, traceable event.

## 9. WANGA Copernicus Interface

For WANGA Copernicus, the same protocol governs questions concerning models, software, architectures, experiments, articles, and their relationships.

Copernicus may propose or discover candidate relationships.

Vitruvius must independently classify the relationship as:

- VERIFIED
- PARTIALLY_VERIFIED
- UNKNOWN
- CONFLICT
- REJECTED

according to the evidence available for the specific claim.

The model must not promote its own proposal directly into lineage.

## 10. Failure Conditions

The following are protocol failures:

- FALSE_ANCESTRY — lineage asserted without provenance;
- SILENT_LINEAGE_LINK — relationship inserted without an explicit evidence record;
- HISTORY_COLLAPSE — algorithmic history and current behavior treated as the same claim;
- STABILITY_BY_IMPRESSION — stability assigned without a defined evidence basis;
- GENERATION_SKIP — a required generation or ancestor branch bypassed without recording the reason;
- BRANCH_COLLAPSE — multiple ancestor branches incorrectly reduced to a single representative;
- RECURSION_TRUNCATION — a required five-generation backward check stopped prematurely;
- UNKNOWN_FILLED_BY_INFERENCE — missing evidence replaced by model completion;
- CONFLICT_SUPPRESSION — contradictory evidence omitted;
- PREDICTION_AS_FACT — predicted relationship represented as verified history;
- GOVERNANCE_PROMOTION — an unverified determination promoted into governance status.

## 11. Audit Record

Every completed inquiry should preserve:

- inquiry_id;
- project;
- question;
- entity_id;
- entry_status;
- generation_results[recursive_five_generation_scope];
- lineage_graph;
- ancestor_branch_results;
- source_refs;
- evidence_refs;
- provenance_refs;
- conflicts;
- uncertainty;
- final_status;
- reviewer/action;
- timestamp;
- parent lineage reference;
- resulting lineage event.

## 12. Core Rule

The operational order is:

ALGORITHM HISTORY REVIEW
→ ENTRY DECISION
→ RECURSIVE FIVE-GENERATION LINEAGE EXPANSION
→ PER-NODE STABILITY TESTING
→ EVIDENCE VERIFICATION
→ LINEAGE DETERMINATION
→ POLITEIA / COPERNICUS KNOWLEDGE UPDATE

No step may be silently skipped.

This protocol defines a proposed research-system procedure inside WANGA-LAB. It does not by itself establish legal, regulatory, or institutional authority outside the repository.
