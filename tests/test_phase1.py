"""
WANGA-NANO-21 Phase 1 Unit, Integration, and Scalability Test Suite
"""

import time
import pytest
from wanga.vgpu import VirtualNanoProcessor, VNPConfig, VNPState, ExecutionPacket, VirtualNeuralProcessor
from wanga.vnp_fabric import VirtualGPU, VirtualProcessorFabric


def test_1_processor_creation():
    cfg = VNPConfig(id="VNP-001", memory_capacity_mb=128)
    vnp = VirtualNanoProcessor(cfg)
    assert vnp.id == "VNP-001"
    assert vnp.state == VNPState.READY
    assert vnp.config.memory_capacity_mb == 128


def test_2_processor_execution():
    vnp = VirtualNanoProcessor(VNPConfig(id="VNP-001"))
    pkt = ExecutionPacket(
        packet_id="pkt-1",
        source_processor="EXTERNAL",
        destination_processor="VNP-001",
        operation="DOUBLE",
        payload=21
    )
    vnp.receive_packet(pkt)
    out_pkt = vnp.execute_next()
    assert out_pkt is not None
    assert out_pkt.payload == 42
    assert vnp.state == VNPState.COMPLETED
    assert vnp.metrics["operations_executed"] == 1


def test_3_gpu_registration():
    gpu = VirtualGPU("vgpu-test")
    vnp = VirtualNanoProcessor(VNPConfig(id="VNP-001"))
    gpu.register_processor(vnp)
    assert "VNP-001" in gpu.list_processors()
    assert gpu.get_processor("VNP-001") == vnp

    gpu.unregister_processor("VNP-001")
    assert "VNP-001" not in gpu.list_processors()


def test_4_gpu_dispatch():
    gpu = VirtualGPU("vgpu-test")
    vnp = VirtualNanoProcessor(VNPConfig(id="VNP-001"))
    gpu.register_processor(vnp)

    pkt = gpu.dispatch("VNP-001", payload="hello")
    assert pkt.destination_processor == "VNP-001"
    results = gpu.synchronize()
    assert len(results) == 1
    assert results[0].payload == "processed_hello"


def test_5_fabric_connection():
    fabric = VirtualProcessorFabric()
    v1 = VirtualNanoProcessor(VNPConfig(id="VNP-001"))
    v2 = VirtualNanoProcessor(VNPConfig(id="VNP-002"))
    fabric.add_processor(v1)
    fabric.add_processor(v2)
    fabric.add_connection("VNP-001", "VNP-002")

    topo = fabric.get_topology_info()
    assert topo["node_count"] == 2
    assert topo["edge_count"] == 1
    assert ("VNP-001", "VNP-002") in topo["edges"]


def test_6_multi_processor_execution():
    gpu = VirtualGPU("vgpu-pipeline")
    v1 = VirtualNanoProcessor(VNPConfig(id="VNP-001"))
    v2 = VirtualNanoProcessor(VNPConfig(id="VNP-002"))
    v3 = VirtualNanoProcessor(VNPConfig(id="VNP-003"))

    gpu.register_processor(v1)
    gpu.register_processor(v2)
    gpu.register_processor(v3)

    # Pipeline: VNP-001 -> VNP-002 -> VNP-003
    gpu.connect_processors("VNP-001", "VNP-002")
    gpu.connect_processors("VNP-002", "VNP-003")

    gpu.dispatch("VNP-001", payload=5)
    results = gpu.synchronize()

    # VNP-001: 5 * 2 = 10
    # VNP-002: 10 * 2 = 20
    # VNP-003: 20 * 2 = 40
    assert len(results) == 3
    assert results[-1].payload == 40


def test_7_failure_isolation():
    def failing_handler(payload):
        raise ValueError("Simulated Processor Error")

    gpu = VirtualGPU("vgpu-error")
    vnp_err = VirtualNanoProcessor(VNPConfig(id="VNP-ERR"), op_handler=failing_handler)
    vnp_ok = VirtualNanoProcessor(VNPConfig(id="VNP-OK"))

    gpu.register_processor(vnp_err)
    gpu.register_processor(vnp_ok)

    gpu.dispatch("VNP-ERR", payload=100)
    with pytest.raises(ValueError, match="Simulated Processor Error"):
        gpu.synchronize()

    assert vnp_err.state == VNPState.ERROR
    assert gpu.status()["error_processors"] == 1

    # Verify OK processor remains functional
    gpu.dispatch("VNP-OK", payload=10)
    res_ok = gpu.synchronize()
    assert res_ok[0].payload == 20


@pytest.mark.parametrize("scale", [4, 8, 16, 32, 50])
def test_scalability(scale):
    gpu = VirtualGPU(f"vgpu-scale-{scale}")
    start_time = time.time()

    for i in range(1, scale + 1):
        vnp_id = f"VNP-{i:03d}"
        gpu.register_processor(VirtualNanoProcessor(VNPConfig(id=vnp_id)))

    # Connect ring topology VNP-1 -> VNP-2 ... -> VNP-N
    for i in range(1, scale):
        gpu.connect_processors(f"VNP-{i:03d}", f"VNP-{i+1:03d}")

    reg_time = time.time() - start_time
    assert len(gpu.list_processors()) == scale

    # Single dispatch flow through topology
    gpu.dispatch("VNP-001", payload=1)
    sync_start = time.time()
    results = gpu.synchronize()
    sync_time = time.time() - sync_start

    assert len(results) == scale
    assert results[-1].payload == 1 * (2 ** scale)
    print(f"\nScalability {scale} VNPs: Reg Time={reg_time*1000:.2f}ms, Sync Time={sync_time*1000:.2f}ms")


def test_virtual_neural_processor_placeholder():
    vnp_neural = VirtualNeuralProcessor("VNP-NEURAL-001")
    vnp_neural.connect_input("VNP-001")
    vnp_neural.connect_output("VNP-002")
    assert vnp_neural.input_processors == ["VNP-001"]
    assert vnp_neural.output_processors == ["VNP-002"]
