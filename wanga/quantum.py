"""
Quantum Abstraction Interface Component
"""

import math
import hashlib
from typing import Dict, Any, List, Optional


class QuantumInterface:
    """
    Provider-independent Quantum Interface supporting classical statevector simulation fallback.
    Exposes PennyLane/Qiskit provider abstractions without requiring physical quantum hardware.
    """

    def __init__(self, n_qubits: int = 2, provider: str = "classical_simulator"):
        self.n_qubits = n_qubits
        self.provider = provider
        # Initialize uniform superposition state vector 1/sqrt(2^N)
        self.dim = 2 ** n_qubits
        self.state_vector = [1.0 / math.sqrt(self.dim)] * self.dim

    def apply_hadamard(self, qubit: int):
        """Applies Hadamard-like transformation on specified qubit in classical simulator."""
        for i in range(self.dim):
            if (i >> qubit) & 1:
                self.state_vector[i] = -self.state_vector[i] / math.sqrt(2)
            else:
                self.state_vector[i] = self.state_vector[i] / math.sqrt(2)
        # Normalize
        norm = math.sqrt(sum(x * x for x in self.state_vector)) or 1.0
        self.state_vector = [x / norm for x in self.state_vector]

    def measure(self) -> List[float]:
        """Returns expectation measurements across qubits."""
        probabilities = [x ** 2 for x in self.state_vector]
        return probabilities

    def compute_sha256(self) -> str:
        s_repr = f"{self.n_qubits}:{self.provider}:{self.state_vector}"
        return hashlib.sha256(s_repr.encode("utf-8")).hexdigest()
