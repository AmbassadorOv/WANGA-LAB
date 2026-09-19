# Architectural Candidate Discovery System

## Purpose

Define a candidate-discovery system for identifying people who may contribute primarily through architectural reasoning, problem formulation, cross-domain composition, and system redesign.

This is a research specification, not a ranking of people and not a claim that any individual has a fixed level of ability.

## Core principle

The system must detect architectural evidence rather than optimize for conventional productivity signals.

Primary distinction:

- Execution profile: performs defined tasks reliably within an existing structure.
- Architectural profile: can redefine the problem, alter the structure, compose across domains, expose hidden assumptions, and produce a testable new system.

A candidate may have both profiles.

## Discovery pipeline

Candidate signal
→ Public/consented evidence collection
→ Evidence normalization
→ Architectural-signal extraction
→ Contradiction and assumption analysis
→ Cross-domain composition analysis
→ Small open-ended challenge
→ Human review
→ Research Site invitation
→ Evidence graph
→ Verification
→ Ongoing reassessment

## Evidence sources

Allowed sources should be public, voluntarily submitted, or explicitly consented:

- research papers and preprints
- patents and technical disclosures
- open-source repositories
- documented experiments
- talks and lectures
- technical essays
- portfolios
- research proposals
- demonstrated prototypes
- candidate-submitted work samples

Do not infer architectural potential from protected or sensitive personal attributes.

## Signal families

### 1. Problem formation

Can the candidate identify a problem that is not already expressed in the task description?

### 2. Structural recomposition

Can the candidate change the architecture of a proposed solution rather than merely optimize its parameters?

### 3. Cross-domain composition

Can the candidate construct a defensible connection between otherwise separate fields?

### 4. Assumption detection

Can the candidate identify assumptions that the existing system treats as fixed?

### 5. Interface creation

Can the candidate define a useful interface between people, models, data, institutions, or disciplines?

### 6. Failure reconstruction

Can the candidate trace a failure from observed output back through dependencies and assumptions?

### 7. Experimental discrimination

Can the candidate propose an experiment that distinguishes competing explanations?

### 8. Independent artifact production

Can the candidate produce an artifact that another person can inspect, reproduce, or challenge?

### 9. Uncertainty preservation

Can the candidate distinguish evidence, hypothesis, interpretation, and unknowns?

## Candidate record

Each candidate record should contain:

- candidate_id
- evidence_items
- source_provenance
- domains
- problem_formation_examples
- recomposition_examples
- cross_domain_examples
- assumption_challenges
- interface_examples
- failure_reconstruction_examples
- experimental_design_examples
- independent_artifacts
- uncertainty_handling
- candidate_consent_status
- reviewer_notes
- verification_status
- research_site_status

No single scalar score should determine placement.

## Open challenge

The candidate should receive a problem with:

- incomplete specification
- conflicting constraints
- no predefined solution menu
- permission to redefine the problem
- requirement to state assumptions
- requirement to propose at least one discriminating test

The system records the process and resulting artifact, not only the final answer.

## Architectural Capacity Preservation Test

A candidate is provisionally identified as architecturally promising when the evidence demonstrates some combination of:

1. redefining the problem;
2. changing the structure of the solution;
3. connecting domains through an explicit mechanism;
4. challenging a supplied assumption;
5. creating an interface not present in the prompt;
6. proposing a verification method for the new structure.

The test is diagnostic, not a permanent label.

## Human review gate

Automated extraction must not make the final placement decision.

Human reviewers inspect:

- evidence quality
- provenance
- alternative explanations
- domain context
- candidate intent
- reproducibility
- possible evaluator bias

## Research Site pathway

When evidence warrants further exploration:

Candidate
→ dedicated research site
→ candidate-controlled research portfolio
→ evidence and version history
→ cross-domain composition index
→ open challenge workspace
→ collaborators
→ prototype
→ verification

The site is an environment for architectural work, not a public ranking page.

## Protection against the execution trap

The system must explicitly test whether a candidate is being redirected into repetitive micro-task execution after discovery.

Monitor:

- proportion of work that is predefined vs self-defined
- opportunity to redesign tasks
- access to long-form research space
- ability to publish artifacts
- ability to challenge system assumptions
- time available for architectural exploration

A high-throughput task profile must never be treated as proof that execution is the appropriate destination.

## Output classes

- DISCOVERED_SIGNAL
- EVIDENCE_PENDING
- OPEN_CHALLENGE_REQUIRED
- HUMAN_REVIEW
- RESEARCH_SITE_CANDIDATE
- RESEARCH_SITE_ACTIVE
- VERIFICATION_PENDING
- INSUFFICIENT_EVIDENCE

These are workflow states, not human-value labels.

## Verification requirements

Before a candidate is routed into the research-site pathway, preserve:

- source URLs or artifact identifiers
- timestamps
- version/hash where available
- reviewer identity
- evaluation protocol
- challenge prompt version
- candidate response artifact
- verification outcome
- unresolved uncertainty

## Non-goals

- ranking human worth
- predicting career success
- inferring intelligence from demographics
- making employment decisions automatically
- assigning permanent labels
- replacing human judgment
- treating one benchmark as proof of architectural capacity

## Integration with WANGA-LAB

The system interfaces with:

Architectural Capacity Preservation Test
→ Evidence/Provenance
→ Research Composition Fractal Map
→ Research Site layer
→ Global Work Manager
→ Rational Logic verification
→ Drift Forensics

The central question is:

> Did the system discover and preserve the candidate's ability to formulate and redesign systems, or did it merely measure their ability to execute predefined tasks?

## Implementation status

SPECIFIED — research architecture only.

No empirical candidate classification is asserted by this document.
