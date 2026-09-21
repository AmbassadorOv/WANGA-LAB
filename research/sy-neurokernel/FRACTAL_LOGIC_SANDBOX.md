# SY-NeuroKernel — Fractal Logic Sandbox

This sandbox isolates the proposed three-layer interaction without exposing the protected Rational Logic implementation.

## Layers

```
K22 / 231 symmetric gates
          │
          ▼
CrystalSymmetricLogic
          │
          ├──────────────┐
          ▼              │
LetterContractionExpansionLogic
          │
          ▼
FractalRationalLogic
          │
          ▼
structured neural dialogue message
```

### 1. Crystal-symmetric logic

A fixed 22-address space produces:

- 22 addresses
- C(22,2) = 231 unordered gates

The topology is structural. The sandbox does not allow the neural layer to invent a new edge.

### 2. Letter contraction/expansion logic

A 22-value state is transformed around its deterministic center.

- contraction reduces deviation from the center;
- expansion increases contrast around the same center;
- neither operation changes the address set or gate topology.

### 3. Fractal rational layer

The third layer composes the two views and emits a typed `LogicMessage`.

The word "fractal" is used here as an architectural label for recursive/compositional reuse. This sandbox does not claim that it has implemented the protected Rational Logic mechanism itself.

## Verification boundary

Current status: **PROTOTYPED**.

The implementation is intentionally dependency-free. Run:

```bash
python -m unittest discover -s tests
```

Passing these tests demonstrates only the local invariants covered by the tests. It does not establish semantic correctness, historical interpretation, cloud deployment, or independent verification.

Cloud components named in the broader architecture — Anthropic, GCP Pub/Sub, Supabase, GitHub Actions — remain integration boundaries and are not activated by this sandbox.
