"""
Virtual Nano-Processor (VNP) Software Simulator
"""

import hashlib
from typing import Dict, Any, List, Optional


class Opcode:
    NOP = 0x00
    LOAD_CONST = 0x01
    ADD = 0x02
    SUB = 0x03
    MUL = 0x04
    STORE = 0x05
    FETCH = 0x06
    SEND = 0x07
    HALT = 0xFF


class VirtualNanoProcessor:
    """
    Software simulator for a configurable Virtual Nano-Processor (VNP).
    Provides registers, memory, opcode execution, routing, execution trace, metrics, state serialization, and determinism.
    """

    def __init__(self, vnp_id: str, registers_count: int = 8, memory_size: int = 256, router_id: Optional[str] = None):
        self.vnp_id = vnp_id
        self.registers_count = registers_count
        self.memory_size = memory_size
        self.router_id = router_id or f"router-{vnp_id}"

        self.registers: List[int] = [0] * registers_count
        self.memory: List[int] = [0] * memory_size
        self.pc: int = 0
        self.halted: bool = False
        self.cycle_count: int = 0
        self.execution_trace: List[Dict[str, Any]] = []
        self.outbox: List[Dict[str, Any]] = []

    def load_program(self, instructions: List[Dict[str, Any]]):
        """Loads list of instruction dicts into processor memory."""
        self.instructions = instructions
        self.pc = 0
        self.halted = False
        self.cycle_count = 0
        self.execution_trace.clear()

    def step(self) -> bool:
        if self.halted or self.pc >= len(self.instructions):
            self.halted = True
            return False

        inst = self.instructions[self.pc]
        op = inst.get("op", "NOP")
        r1 = inst.get("r1", 0)
        r2 = inst.get("r2", 0)
        val = inst.get("val", 0)
        addr = inst.get("addr", 0)
        target = inst.get("target")

        prev_pc = self.pc

        if op in ("NOP", Opcode.NOP):
            pass
        elif op in ("LOAD_CONST", Opcode.LOAD_CONST):
            if 0 <= r1 < self.registers_count:
                self.registers[r1] = val
        elif op in ("ADD", Opcode.ADD):
            if 0 <= r1 < self.registers_count and 0 <= r2 < self.registers_count:
                self.registers[r1] = (self.registers[r1] + self.registers[r2]) & 0xFFFFFFFF
        elif op in ("SUB", Opcode.SUB):
            if 0 <= r1 < self.registers_count and 0 <= r2 < self.registers_count:
                self.registers[r1] = (self.registers[r1] - self.registers[r2]) & 0xFFFFFFFF
        elif op in ("MUL", Opcode.MUL):
            if 0 <= r1 < self.registers_count and 0 <= r2 < self.registers_count:
                self.registers[r1] = (self.registers[r1] * self.registers[r2]) & 0xFFFFFFFF
        elif op in ("STORE", Opcode.STORE):
            if 0 <= r1 < self.registers_count and 0 <= addr < self.memory_size:
                self.memory[addr] = self.registers[r1]
        elif op in ("FETCH", Opcode.FETCH):
            if 0 <= r1 < self.registers_count and 0 <= addr < self.memory_size:
                self.registers[r1] = self.memory[addr]
        elif op in ("SEND", Opcode.SEND):
            if 0 <= r1 < self.registers_count:
                self.outbox.append({
                    "src": self.vnp_id,
                    "target": target,
                    "payload": self.registers[r1]
                })
        elif op in ("HALT", Opcode.HALT):
            self.halted = True

        self.cycle_count += 1
        self.pc += 1

        self.execution_trace.append({
            "cycle": self.cycle_count,
            "pc": prev_pc,
            "op": op,
            "registers": list(self.registers),
            "halted": self.halted
        })

        if self.pc >= len(self.instructions):
            self.halted = True

        return not self.halted

    def run_until_halt(self, max_cycles: int = 1000) -> int:
        cycles = 0
        while not self.halted and cycles < max_cycles:
            self.step()
            cycles += 1
        return cycles

    def get_state(self) -> Dict[str, Any]:
        return {
            "vnp_id": self.vnp_id,
            "registers": list(self.registers),
            "memory": list(self.memory),
            "pc": self.pc,
            "halted": self.halted,
            "cycle_count": self.cycle_count
        }

    def compute_sha256(self) -> str:
        state_repr = str(self.get_state())
        return hashlib.sha256(state_repr.encode("utf-8")).hexdigest()
