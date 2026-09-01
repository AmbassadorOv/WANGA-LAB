"""
WANGA Automated Test Suite
"""

import json
import pytest
from wanga.spec import load_architecture_spec
from wanga.validation import WangaValidationPipeline
from wanga.nano import VirtualNanoProcessor
from wanga.neural import NeuralLabComponent
from wanga.quantum import QuantumInterface
from wanga.workers import WorkerRegistry, Worker
from wanga.sandbox import DockerSandbox
from wanga.provenance import ProvenanceManager
from wanga.compiler import WANGACompiler


def test_vnp_execution():
    vnp = VirtualNanoProcessor("vnp-test", registers_count=8, memory_size=128)
    vnp.load_program([
        {"op": "LOAD_CONST", "r1": 0, "val": 15},
        {"op": "LOAD_CONST", "r1": 1, "val": 25},
        {"op": "ADD", "r1": 0, "r2": 1},
        {"op": "STORE", "r1": 0, "addr": 2},
        {"op": "HALT"}
    ])
    vnp.run_until_halt()
    assert vnp.registers[0] == 40
    assert vnp.memory[2] == 40
    assert len(vnp.execution_trace) == 5


def test_neural_execution():
    nc = NeuralLabComponent("nc-test", input_dim=4, output_dim=2, seed=42)
    loss = nc.run_step([1.0, 1.0, 1.0, 1.0], [0.0, 1.0])
    assert loss >= 0.0


def test_validation_pipeline():
    pipeline = WangaValidationPipeline()
    valid_data = {
        "version": "1.0.0",
        "name": "Test",
        "agents": [{"id": "a1", "name": "A1"}],
        "virtual_nano_processors": [{"id": "vnp-1"}],
        "experiment": {"id": "e1", "seed": 42}
    }
    res = pipeline.validate(valid_data)
    assert res.is_valid

    invalid_data = {"version": "1.0.0", "name": ""}
    res_inv = pipeline.validate(invalid_data)
    assert not res_inv.is_valid


def test_determinism_replay():
    nc1 = NeuralLabComponent("nc1", seed=42)
    loss1 = nc1.run_step([0.1]*8, [1.0]*4)

    nc2 = NeuralLabComponent("nc2", seed=42)
    loss2 = nc2.run_step([0.1]*8, [1.0]*4)

    assert abs(loss1 - loss2) < 1e-6


def test_compiler_e2e():
    compiler = WANGACompiler()
    with open("examples/hello_wanga_architecture.json", "r") as f:
        arch = json.load(f)
    success, res = compiler.run_pipeline(arch, verbose=False)
    assert success
    assert res["status"] == "PASS"
    assert "artifact_sha256" in res["artifact"]
