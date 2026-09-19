# GitHub Fractal Neural Network

The recursive layer extends Vitruvius from architecture discovery to a **family-of-families network**.

For every discovered repository and integration branch, the engine recursively decomposes:

`Repository → Branch → Family → Subfamily → Artifact → Architecture`

Each level becomes a node. Parent-child relations become edges. The resulting local branch networks are folded into one global topology.

The important property is recursion: a family can contain smaller families, and the same classification rule is applied again until the available repository structure or declared artifact boundary is exhausted.

The neural network then operates over the combined topology. Vitruvius determines structural relationships; the neural communication layer carries typed state and impact signals.

## Global model

```
GitHub
  ├── Repository A
  │    ├── Branch
  │    │    ├── Family
  │    │    │    ├── Subfamily
  │    │    │    └── Artifact
  │    │    └── Family
  │    └── Branch
  ├── Repository B
  │    └── ...
  └── ...
          ↓
   Vitruvian Recursive Extraction
          ↓
 Family-of-Families Graph
          ↓
 Neural Communication Fabric
          ↓
 One Global WANGA Neural Topology
```

This is an architecture for building a connected computational map of accessible GitHub material. It does not imply that every public GitHub repository is automatically copied, trusted, or merged. Discovery, authorization, integration, testing and verification remain separate stages.
