# Codex Engineering Guardrails — AI Drift Forensics

## Objective

Provide engineering constraints for building AI Drift Forensics infrastructure that remains reproducible, auditable, evidence-aware, and conservative about claims.

## 1. Evidence Before Interpretation

Every forensic observation must preserve the underlying artifact or an immutable reference to it before higher-level interpretation is generated.

```text
RAW ARTIFACT
   ↓
HASH / IDENTITY
   ↓
PROVENANCE
   ↓
NORMALIZATION
   ↓
MEASUREMENT
   ↓
INTERPRETATION
```

Never overwrite the raw artifact with a normalized or transformed representation.

## 2. Separate Fact Classes

Code and documentation must distinguish at least:

- `OBSERVED` — directly measured or recorded.
- `REPORTED` — supplied by an external party.
- `DERIVED` — computed from recorded evidence.
- `HYPOTHESIS` — proposed explanation.
- `VERIFIED` — independently reproduced or checked under a defined procedure.
- `REFUTED` — contradicted by available evidence.
- `UNRESOLVED` — insufficient evidence to select among explanations.

A hypothesis must never silently become an observed fact.

## 3. Reproducibility

A test result should record enough execution context to permit a qualified independent party to reproduce the relevant measurement, subject to lawful and security constraints.

Capture where applicable:

- model/provider/version;
- prompt or test vector identifier;
- configuration identifier;
- environment identifier;
- dependency versions;
- timestamps and clock assumptions;
- test procedure version;
- random seed or nondeterminism notes;
- output artifact identifiers.

## 4. Chain of Custody

Evidence transfers must be append-only records.

Minimum conceptual fields:

```yaml
artifact_ref: "..."
timestamp: "..."
actor: "..."
action: "ACQUIRE|COPY|TRANSFER|TRANSFORM|STORE|RELEASE"
content_hash: "..."
source_ref: "..."
destination_ref: "..."
```

A transformation must not be represented as if it were the original artifact.

## 5. Attribution Discipline

Attribution is a graph-analysis problem, not a naming exercise.

The system should preserve multiple candidate contributors and their supporting evidence.

```text
EFFECT
 ├── MODEL CHANGE
 ├── DATA CHANGE
 ├── CONFIGURATION CHANGE
 ├── DEPENDENCY CHANGE
 ├── ENVIRONMENT CHANGE
 └── UNKNOWN / ALTERNATIVE
```

Do not label a contributor as causal solely because it changed near the time of an observed effect.

## 6. Baseline Integrity

A drift measurement requires a declared comparison baseline.

Record:

- baseline identity;
- baseline creation time;
- baseline procedure;
- baseline evidence references;
- comparison window;
- measurement method;
- uncertainty/limitations.

## 7. Simulation vs. Event

Controlled tests may demonstrate that a behavior is reproducible under defined conditions. They do not establish that an equivalent event occurred in production.

Use explicit labels:

`SIMULATION`, `CONTROLLED_TEST`, `OBSERVED_PRODUCTION_EVENT`, `REPORTED_EVENT`.

## 8. Security and Privacy

Do not commit credentials, access tokens, API keys, private keys, personal data, confidential customer material, or security-sensitive operational secrets.

Public case records should use stable references, redaction, synthetic identifiers, or controlled-access storage where necessary.

## 9. Public Claims

The public website and repository must distinguish:

- research proposal from adopted standard;
- technical observation from institutional conclusion;
- evidence from interpretation;
- simulation from real-world incident;
- possible financial relevance from quantified financial loss;
- technical evidence from legal or regulatory determination.

## 10. Engineering Change Control

Every material change to forensic logic should identify:

- changed method;
- affected schema/version;
- compatibility impact;
- test coverage;
- reproducibility impact;
- migration requirement.

Prefer additive schema changes. Breaking changes require an explicit version transition.

## 11. Verification Gate

A forensic pipeline should not emit `VERIFIED` merely because an internal test passed.

The verification record must identify:

1. the proposition being tested;
2. the evidence set;
3. the procedure;
4. the expected result;
5. the observed result;
6. reproducibility status;
7. independence of the verifier, where applicable;
8. remaining limitations.

## 12. Engineering Objective

The infrastructure should make it harder to make an unsupported claim and easier to reproduce a supported one.

That is the central engineering guardrail for AI Drift Forensics.
