# Preventive AI Forensic Intervention Record

## Purpose

This document records the transition from research and observation into a preventive forensic intervention concerning potential AI-related exposure in financial and insurance environments.

It does not establish that a catastrophe occurred, that a particular institution suffered loss, or that a particular anomaly was systemic. It records an evidentiary posture: potentially material technical changes should be identified, preserved, reconstructable, and independently examinable before the relevant evidence disappears.

## Operational Principle

> Do not wait for the incident to become the evidence.

Evidence should exist before the incident. Baselines should exist before drift. Version history should exist before a dispute. Dependency records should exist before failure. Verification should exist after remediation.

## Intervention Lifecycle

```text
RESEARCH
  -> OBSERVATION
  -> DRIFT IDENTIFICATION
  -> EVIDENCE PRESERVATION
  -> RISK ANALYSIS
  -> INSTITUTIONAL NOTIFICATION
  -> INDEPENDENT REVIEW
  -> CORRECTIVE INTERVENTION
  -> VERIFICATION
```

## Financial-System Evidence Question

For a critical AI-dependent process, an investigator should be able to determine, to the extent supported by available evidence:

- what system was operating;
- which model/version was active;
- which dependencies were involved;
- what changed;
- when the change occurred;
- what evidence establishes the change;
- whether the change is temporally or causally associated with an observed outcome; and
- whether the relevant state can be independently reconstructed.

## Evidence Preservation

Potentially relevant evidence may include model identifiers, deployment records, configuration state, prompts or policies where appropriate, dependency versions, API metadata, data-provenance records, logs, hashes, timestamps, measurements, test outputs, and reconstructed environment state.

The preservation rule is:

**Preserve first. Interpret second.**

Preservation does not imply a conclusion. It protects the ability to reach a conclusion later.

## Forensic Card Set

Each intervention case may be represented as a structured collection of evidence cards:

1. **System Card** — system identity and scope.
2. **Model Card** — model, version, deployment identity and relevant configuration.
3. **Environment Card** — runtime, infrastructure and dependencies.
4. **Data Card** — relevant data provenance and distribution observations.
5. **Configuration Card** — prompts, policies, thresholds, routing, tools and deployment settings.
6. **Event Card** — anomaly, material change, incident or controlled intervention.
7. **Timeline Card** — ordered technical and operational events.
8. **Evidence Card** — preserved artifacts, measurements, hashes and provenance.
9. **Attribution Card** — candidate contributors, dependency paths and alternative explanations.
10. **Intervention Card** — action taken and intended effect.
11. **Verification Card** — post-intervention evidence and reproducibility result.

## Financial Risk Window

The research focus is the interval between technical change and institutional recognition:

```text
AI / MODEL CHANGE
      |
      v
OPERATIONAL BEHAVIOUR CHANGE
      |
      v
RISK PROFILE CHANGE
      |
      v
INCOMPLETE DETECTION
      |
      v
INCOMPLETE EVIDENCE
      |
      v
UNCERTAIN ATTRIBUTION
      |
      v
FINANCIAL / INSURANCE UNCERTAINTY
```

This interval is treated as a potential AI Evidence Gap. The objective is to determine whether that gap can be measured and reduced.

## Institutional Communication

The transition from quiet research to broader notification is documented as a change in communication scope:

```text
DIRECT TECHNICAL RESEARCH
      -> STRUCTURED EVIDENCE
      -> INSTITUTIONAL WARNING
      -> FINANCIAL / INSURANCE ANALYSIS
      -> GOVERNMENT / PUBLIC COMMUNICATION
      -> PUBLIC DOCUMENTATION
```

Communication should distinguish observation, evidence, interpretation, and unresolved questions. No warning should be phrased as proof of an event that has not been independently established.

## Insurance and Risk-Transfer Interface

For insurance and reinsurance analysis, the relevant technical question is whether the insured AI-dependent environment can be reconstructed sufficiently to establish how it changed over time.

Potentially relevant evidence includes deployment history, model versions, material configuration changes, dependencies, drift measurements, incident timelines, and reconstructed system states.

This framework does not determine coverage, liability, claims outcomes, underwriting decisions, or actuarial conclusions. It provides a technical evidence layer that may support those independent decisions.

## Status

This record is part of an active research and development program. The IOADC framework is proposed technical research and is not represented as an adopted statutory, regulatory, or accredited international standard.

## Case Integrity Rules

- Separate observed facts from hypotheses.
- Preserve original artifacts before transformation.
- Record timestamps and provenance.
- Hash preserved artifacts where appropriate.
- Record tool/model/version context when relevant.
- Maintain a chain of custody for evidence transferred between systems.
- Record alternative explanations rather than prematurely selecting one.
- Make reproducibility a separate verification step.
- Never convert a simulation into a claim that a real-world event occurred.
- Never convert a provider declaration into independent verification.
