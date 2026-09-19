# WANGA-X — Neural Computation-Driven Blueprint Paradigm

Status: RESEARCH FOUNDATION / CORE ARCHITECTURAL THESIS

## Core thesis

WANGA-X starts from the user's query or system request, not from a fixed neural architecture.

The query establishes the requirement. The requirement determines what neural computation is required. The required neural computation determines the computational structure from which the Blueprint of the neural computer is derived.

The central causal chain is:

```
USER QUERY / SYSTEM REQUEST
            ↓
      REQUIREMENT
            ↓
REQUIRED NEURAL COMPUTATION
            ↓
NEURAL COMPUTATIONAL STRUCTURE
            ↓
         BLUEPRINT
            ↓
     NEURAL COMPUTER
            ↓
        EXECUTION
```

The key proposition is therefore not simply that a neural network can adapt its architecture. The proposition is that **the required neural computation is the intermediate determinant between the user's requirement and the Blueprint of the neural computer**.

## Architecture paradigm

The conventional direction is:

```
FIXED ARCHITECTURE → COMPUTATION / QUERY
```

The WANGA-X direction is:

```
QUERY → REQUIRED NEURAL COMPUTATION → BLUEPRINT → NEURAL COMPUTER
```

When the requirement changes, the computational requirement is reconsidered and the Blueprint may change accordingly:

```
NEW QUERY / CHANGED REQUIREMENT
            ↓
NEW REQUIRED NEURAL COMPUTATION
            ↓
NEW / CHANGED COMPUTATIONAL STRUCTURE
            ↓
NEW BLUEPRINT
            ↓
EVOLVED NEURAL COMPUTER
```

## What changes

The evolving object is not limited to topology. Depending on the requirement, the generated neural computational system may determine:

- architecture and topology;
- computational modules;
- connections and routing;
- parameters and weights;
- allocation of computational resources;
- state representation and execution structure.

The research question is whether these elements can be derived and materialized from the required neural computation through a persistent Blueprint representation.

## Relation to existing dynamic-neural research

Dynamic Neural Network research has established mechanisms for changing network structures or parameters. WANGA-X uses that foundation but changes the architectural starting point:

**Dynamic neural research:** an existing neural system adapts its structure or parameters.

**WANGA-X hypothesis:** the required neural computation is first derived from the query/requirement, and that computation then determines the Blueprint of the neural computer.

This distinction is the core conceptual contribution under investigation.

## Position of Rational Logic and NTM

Rational Logic determines and constrains what computation is required by the user's request.

The Neural Thinking Machine reasons over candidate neural computational structures.

The Blueprint represents the selected computational structure.

The materializer constructs the neural computer represented by the Blueprint.

```
USER QUERY
    ↓
RATIONAL LOGIC
    ↓
REQUIRED NEURAL COMPUTATION
    ↓
NTM ARCHITECTURE REASONING
    ↓
BLUEPRINT / IR
    ↓
MATERIALIZATION
    ↓
NEURAL COMPUTER
    ↓
EXECUTION
    ↓
EVIDENCE / VERIFICATION
```

## Research boundary

This document records the core paradigm and research hypothesis. It does not claim that the complete mechanism has already been implemented or experimentally validated.

The purpose of the first prototype is to determine whether the proposed causal chain can be implemented as an executable system and whether different requirements can produce materially different neural computational structures and Blueprints while preserving explicit verification and provenance.
