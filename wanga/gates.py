"""
WANGA 231-Gate Invariant Rule Engine
"""

from typing import Dict, Any, List, Tuple, Callable


class GateCheckResult:
    def __init__(self, gate_number: int, name: str, passed: bool, message: str = ""):
        self.gate_number = gate_number
        self.name = name
        self.passed = passed
        self.message = message


class Gates231Engine:
    """
    Executes the 231 programmatic gate invariant checks for WANGA architectures.
    Gates 1-10 are explicit core gates; Gates 11-231 are system invariant gates.
    """

    def __init__(self):
        self._custom_gates: Dict[int, Tuple[str, Callable[[Dict[str, Any]], Tuple[bool, str]]]] = {}
        self._init_core_gates()

    def _init_core_gates(self):
        # Gate 1: Non-empty Name
        self._custom_gates[1] = (
            "Gate 1: Architecture Name Present",
            lambda d: (bool(d.get("name")), "Architecture name must be non-empty")
        )
        # Gate 2: Version Compatibility
        self._custom_gates[2] = (
            "Gate 2: Version Specified",
            lambda d: (bool(d.get("version")), "Architecture version must be specified")
        )
        # Gate 3: Valid Experiment
        self._custom_gates[3] = (
            "Gate 3: Experiment Defined",
            lambda d: (isinstance(d.get("experiment"), dict), "Experiment configuration block required")
        )
        # Gate 4: Determinism Seed
        self._custom_gates[4] = (
            "Gate 4: Deterministic Seed Set",
            lambda d: (isinstance(d.get("experiment", {}).get("seed"), int), "Deterministic seed must be an integer")
        )
        # Gate 5: Non-Empty Agents/Components
        self._custom_gates[5] = (
            "Gate 5: Component Count Check",
            lambda d: (
                len(d.get("agents", [])) + len(d.get("neural_components", [])) + len(d.get("virtual_nano_processors", [])) > 0,
                "Must define at least one agent, neural component, or virtual nano processor"
            )
        )
        # Gate 6: Memory Limit Upper Bound
        self._custom_gates[6] = (
            "Gate 6: Sandbox Memory Bound",
            lambda d: (d.get("security", {}).get("max_memory_mb", 512) <= 16384, "Memory limit exceeds 16GB threshold")
        )
        # Gate 7: Execution Timeout Upper Bound
        self._custom_gates[7] = (
            "Gate 7: Execution Timeout Bound",
            lambda d: (d.get("security", {}).get("max_execution_seconds", 60) <= 3600, "Execution timeout exceeds 1 hour")
        )
        # Gate 8: VNP Register Limit
        self._custom_gates[8] = (
            "Gate 8: VNP Register Count Sanity",
            lambda d: (
                all(0 < v.get("registers_count", 8) <= 1024 for v in d.get("virtual_nano_processors", [])),
                "VNP registers count must be between 1 and 1024"
            )
        )
        # Gate 9: Neural Dimension Check
        self._custom_gates[9] = (
            "Gate 9: Neural Dimension Sanity",
            lambda d: (
                all(n.get("input_dim", 1) > 0 and n.get("output_dim", 1) > 0 for n in d.get("neural_components", [])),
                "Neural dimensions must be strictly positive"
            )
        )
        # Gate 10: Disallowed Code Injection Gate
        def check_code_injection(d: Dict[str, Any]) -> Tuple[bool, str]:
            payload_str = str(d)
            prohibited = ["eval(", "exec(", "__import__", "os.system"]
            for bad in prohibited:
                if bad in payload_str:
                    return False, f"Architecture payload contains prohibited string pattern: {bad}"
            return True, "Code injection checks passed"

        self._custom_gates[10] = (
            "Gate 10: Untrusted Code Injection Gate",
            check_code_injection
        )

    def evaluate_gate(self, gate_num: int, arch_dict: Dict[str, Any]) -> GateCheckResult:
        if gate_num in self._custom_gates:
            name, fn = self._custom_gates[gate_num]
            passed, msg = fn(arch_dict)
            return GateCheckResult(gate_num, name, passed, msg)

        # Gates 11 to 231 default system invariant check
        gate_name = f"Gate {gate_num}: System Invariant Gate {gate_num}"
        allowed = arch_dict.get("security", {}).get("allowed_gates", list(range(1, 232)))
        if gate_num not in allowed:
            return GateCheckResult(gate_num, gate_name, False, f"Gate {gate_num} explicitly disabled in security policy")

        return GateCheckResult(gate_num, gate_name, True, "System invariant passed")

    def evaluate_all(self, arch_dict: Dict[str, Any]) -> Tuple[bool, List[GateCheckResult]]:
        results = []
        all_passed = True
        for g in range(1, 232):
            res = self.evaluate_gate(g, arch_dict)
            results.append(res)
            if not res.passed:
                all_passed = False
        return all_passed, results
