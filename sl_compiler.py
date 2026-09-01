# -*- coding: utf-8 -*-
"""
================================================================================
ARK-SL COMPILER & AUTONOMOUS RUNTIME ENGINE
================================================================================
מנוע אוטונומי המקבל קובץ שפת SL (String Logic), מנתח אותו, מייצר
ארטיפקטים (JSON, קוד Python מודולרי), ומריץ לולאת איטרציות עצמאית
עד להשגת התכנסות אנטרופיה (Berudim State).
================================================================================
"""

import os
import json
import math
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

# =====================================================================
# 1. קבועים וליבת ה־ARK-KERNEL (עצמאי לחלוטין)
# =====================================================================

HEBREW_LETTERS = [
    "א", "ב", "ג", "ד", "ה", "ו", "ז", "ח", "ט", "י", "כ",
    "ל", "מ", "נ", "ס", "ע", "פ", "צ", "ק", "ר", "ש", "ת"
]

@dataclass
class SLKernelDefinition:
    string_scale: float = 1.618
    determinism_lock: bool = True
    nodes: int = 22
    blocks: int = 7
    phases: int = 21

@dataclass
class SLModelDefinition:
    name: str = "ARK_VITRUVIUS"
    kernel_ref: str = "ARK"
    world_state: str = "BERUDIM_TRANSITION"
    weight_domains: Dict[str, str] = field(default_factory=lambda: {
        "W_S": "Semantic",
        "W_D": "Doubt",
        "W_L": "Logical",
        "W_P": "Prosody",
        "W_C": "Dialectic",
        "W_H": "Status"
    })

@dataclass
class SLAppDefinition:
    name: str = "ARK_SL_RUNTIME"
    model_ref: str = "ARK_VITRUVIUS"
    action_trigger: str = "ANALYZE_TEXT"
    pipeline: List[str] = field(default_factory=lambda: [
        "spawn nanocore for each letter",
        "run iteration 1",
        "return JSON_STATE_V1"
    ])

@dataclass
class HolographicStringNode:
    """ייצוג של מיתר-אות (Nano Processor Node) במרחב ההולוגרפי"""
    letter: str
    index: int
    radius: float
    bulk_energy: float
    chaos_energy: float
    surface_tension: float
    entropy: float
    coherence: float

    @classmethod
    def create_canonical(cls, letter: str, index: int) -> "HolographicStringNode":
        radius = 1.0 + (index * 0.1)
        bulk_energy = 100.0 / (index + 1)
        chaos_energy = 5.0 * (index + 1)
        surface_tension = 1.0
        entropy = 0.5
        coherence = 0.0
        return cls(
            letter=letter,
            index=index,
            radius=radius,
            bulk_energy=bulk_energy,
            chaos_energy=chaos_energy,
            surface_tension=surface_tension,
            entropy=entropy,
            coherence=coherence
        )

    def apply_t_duality(self, string_scale: float = 1.618):
        if self.radius <= 0 or not math.isfinite(self.radius):
            raise ValueError(f"רדיוס שגוי בצומת {self.letter}")
        new_radius = (string_scale ** 2) / self.radius
        if not math.isfinite(new_radius) or new_radius <= 0:
            raise ValueError(f"Calculated non-finite radius for node {self.letter}")
        temp_bulk = self.bulk_energy
        self.bulk_energy = self.chaos_energy * (new_radius / self.radius)
        self.chaos_energy = temp_bulk * (self.radius / new_radius)
        self.radius = new_radius

    def apply_holographic_transform(self):
        denom = self.bulk_energy + self.chaos_energy + 1e-9
        coherence = abs(self.bulk_energy - self.chaos_energy) / denom
        self.surface_tension = math.exp(-coherence) * 100.0
        self.entropy = self.entropy * 0.1 * coherence
        self.coherence = coherence

    def to_dict(self) -> Dict[str, Any]:
        return {
            "letter": self.letter,
            "node_index": self.index,
            "topological_state": {
                "radius_R": round(self.radius, 6),
                "inside_bulk_energy": round(self.bulk_energy, 6),
                "outside_chaos_energy": round(self.chaos_energy, 6),
                "surface_duchsustus_tension": round(self.surface_tension, 6),
                "coherence": round(self.coherence, 6),
                "local_entropy_dS": round(self.entropy, 6)
            }
        }


class IterationEngine:
    """מנוע האיטרציה המנהל את מערך צמתי המיתר"""
    def __init__(self, string_scale: float = 1.618, determinism_lock: bool = True, nodes_list: Optional[List[HolographicStringNode]] = None):
        self.string_scale = string_scale
        self.determinism_lock = determinism_lock
        self.iteration_count = 0
        if nodes_list:
            self.nodes = nodes_list
        else:
            self.nodes = [
                HolographicStringNode(
                    letter=HEBREW_LETTERS[i],
                    index=i+1,
                    radius=1.0 + ((i+1) * 0.1),
                    bulk_energy=100.0 / (i + 2),
                    chaos_energy=5.0 * (i + 2),
                    surface_tension=1.0,
                    entropy=0.5,
                    coherence=0.0
                ) for i in range(22)
            ]

    def step(self) -> Dict[str, Any]:
        self.iteration_count += 1
        for node in self.nodes:
            node.apply_t_duality(self.string_scale)
        for node in self.nodes:
            node.apply_holographic_transform()
        return self.export_state()

    def export_state(self) -> Dict[str, Any]:
        total_entropy = sum(n.entropy for n in self.nodes)
        return {
            "meta": {
                "iteration": self.iteration_count,
                "protocol": "T-DUALITY_HOLOGRAPHIC_V1",
                "string_scale_alpha_prime": self.string_scale,
                "node_count": len(self.nodes),
                "world_state": "BERUDIM_TRANSITION" if total_entropy > 1e-5 else "BERUDIM_FIXED_POINT",
                "total_entropy": round(total_entropy, 6)
            },
            "nodes": [n.to_dict() for n in self.nodes]
        }


# =====================================================================
# 2. שפת SL – מחלקות תחביר ומבנה אבסטרקטי (AST)
# =====================================================================

@dataclass
class SLModelAST:
    model_name: str
    string_scale: float = 1.618
    determinism_lock: bool = True
    target_entropy: float = 0.0
    nodes: List[HolographicStringNode] = field(default_factory=list)
    blocks: Dict[str, str] = field(default_factory=dict)
    phases: Dict[int, str] = field(default_factory=dict)
    weights: Dict[str, str] = field(default_factory=dict)
    chazaka: Dict[str, float] = field(default_factory=dict)


class SLParser:
    """מנתח טקסטואלי (Parser) הממיר קובץ .sl למבנה AST ממוחשב"""

    @staticmethod
    def parse_script(script_text: str) -> Dict[str, Any]:
        kernel_def = SLKernelDefinition()
        model_def = SLModelDefinition()
        app_def = SLAppDefinition()

        lines = [line.strip() for line in script_text.splitlines() if line.strip() and not line.strip().startswith("//")]
        current_block = None

        for line in lines:
            if "kernel " in line and "{" in line:
                current_block = "kernel"
                continue
            elif "model " in line and "{" in line:
                current_block = "model"
                continue
            elif "app " in line and "{" in line:
                current_block = "app"
                continue
            elif line == "}":
                current_block = None
                continue

            if current_block == "kernel":
                if "=" in line:
                    k, v = [x.strip() for x in line.split("=", 1)]
                    if k == "string_scale":
                        kernel_def.string_scale = float(v)
                    elif k == "determinism_lock":
                        kernel_def.determinism_lock = (v.lower() == "true")
                    elif k == "nodes":
                        kernel_def.nodes = int(v)
                    elif k == "blocks":
                        kernel_def.blocks = int(v)
                    elif k == "phases":
                        kernel_def.phases = int(v)
            elif current_block == "model":
                if "=" in line:
                    k, v = [x.strip() for x in line.split("=", 1)]
                    if k == "name":
                        model_def.name = v.strip('"')
                    elif k == "world_state":
                        model_def.world_state = v.strip('"')
            elif current_block == "app":
                if "=" in line:
                    k, v = [x.strip() for x in line.split("=", 1)]
                    if k == "name":
                        app_def.name = v.strip('"')
                    elif k == "action_trigger":
                        app_def.action_trigger = v.strip('"')

        return {
            "kernel": kernel_def,
            "model": model_def,
            "app": app_def
        }

    @staticmethod
    def parse(source_text: str) -> SLModelAST:
        lines = [line.strip() for line in source_text.splitlines() if line.strip() and not line.strip().startswith("//")]

        model_name = "DefaultArkModel"
        if lines and lines[0].startswith("SL_MODEL"):
            parts = lines[0].split()
            if len(parts) > 1:
                model_name = parts[1].replace("{", "").strip()

        ast = SLModelAST(model_name=model_name)
        current_section = None

        for line in lines:
            if line.endswith("{"):
                current_section = line.split()[0].upper()
                continue
            elif line == "}":
                current_section = None
                continue

            if current_section == "NODES" and line.startswith("NODE"):
                clean_line = line.replace(";", "").replace('"', "")
                tokens = clean_line.split()
                try:
                    letter = tokens[1]
                    idx = int(tokens[3])
                    radius = float(tokens[5])
                    bulk = float(tokens[7])
                    chaos = float(tokens[9])

                    node = HolographicStringNode(
                        letter=letter,
                        index=idx,
                        radius=radius,
                        bulk_energy=bulk,
                        chaos_energy=chaos,
                        surface_tension=1.0,
                        entropy=0.5,
                        coherence=0.0
                    )
                    ast.nodes.append(node)
                except Exception as e:
                    print(f"[!] שגיאת פענוח בשורה: {line} -> {e}")

            elif current_section == "ARCH":
                if line.startswith("BLOCK"):
                    clean = line.replace(";", "")
                    quotes = re.findall(r'"([^"]*)"', clean)
                    parts = clean.replace('"', "").split()
                    block_id = parts[1]
                    if quotes:
                        block_name = quotes[0]
                    else:
                        name_idx = parts.index("NAME")
                        block_name = parts[name_idx + 1]
                    ast.blocks[block_id] = block_name
                elif line.startswith("PROCESSOR_PHASE"):
                    clean = line.replace(";", "")
                    quotes = re.findall(r'"([^"]*)"', clean)
                    parts = clean.replace('"', "").split()
                    phase_num = int(parts[1])
                    if quotes:
                        phase_name = quotes[0]
                    else:
                        phase_name = parts[2]
                    ast.phases[phase_num] = phase_name

            elif current_section == "WEIGHTS":
                if line.startswith("DOMAIN"):
                    parts = line.replace(";", "").split()
                    ast.weights[parts[2]] = parts[1]
                elif line.startswith("CHAZAKA"):
                    parts = line.replace(";", "").split()
                    ast.chazaka[parts[1]] = float(parts[2])

            elif current_section == "ENGINE":
                if line.startswith("STRING_SCALE"):
                    ast.string_scale = float(line.replace(";", "").split()[1])
                elif line.startswith("DETERMINISM_LOCK"):
                    ast.determinism_lock = line.replace(";", "").split()[1].upper() == "TRUE"
                elif line.startswith("TARGET_ENTROPY"):
                    ast.target_entropy = float(line.replace(";", "").split()[1])

        if not ast.nodes:
            ast.nodes = IterationEngine(string_scale=ast.string_scale).nodes

        return ast


# =====================================================================
# 3. מנוע הקומפיילר והאוטומציה החיה (SLCompiler & Autonomous Runtime)
# =====================================================================

class SLCompilerPipeline:
    def __init__(self, sl_script_path: str):
        self.sl_script_path = sl_script_path
        self.ast = None

    def compile(self) -> Dict[str, Any]:
        with open(self.sl_script_path, "r", encoding="utf-8") as f:
            raw_content = f.read()
        self.ast = SLParser.parse_script(raw_content)

        compiled_bundle = {
            "target_engine": "ark_kernel_engine.py",
            "metadata": {
                "kernel_name": self.ast["kernel"].__dict__,
                "model_name": self.ast["model"].name,
                "world_state": self.ast["model"].world_state,
                "weights": self.ast["model"].weight_domains
            },
            "runtime_spec": {
                "app_name": self.ast["app"].name,
                "trigger": self.ast["app"].action_trigger,
                "execution_steps": self.ast["app"].pipeline
            }
        }
        return compiled_bundle


class SLCompiler:
    """קומפיילר ה־SL המתרגם קוד שפה לקובצי מודל, JSON ומריץ איטרציות אוטונומיות"""
    def __init__(self, sl_file_path: str, build_dir: str = "build"):
        self.sl_file_path = Path(sl_file_path)
        self.build_dir = Path(build_dir)
        self.build_dir.mkdir(exist_ok=True)
        self.ast: Optional[SLModelAST] = None

    def compile(self) -> None:
        print(f"[*] טוען ומקמפל קובץ שפת SL: {self.sl_file_path.name}...")
        source_code = self.sl_file_path.read_text(encoding="utf-8")

        self.ast = SLParser.parse(source_code)
        print(f"[+] נמצא מודל: {self.ast.model_name} עם {len(self.ast.nodes)} צמתים.")

        self._write_artifacts()
        self._write_python_executable()

    def _write_artifacts(self) -> None:
        nodes_data = [node.to_dict() for node in self.ast.nodes]
        meta_data = {
            "model_name": self.ast.model_name,
            "string_scale_alpha_prime": self.ast.string_scale,
            "determinism_lock": self.ast.determinism_lock,
            "target_entropy": self.ast.target_entropy,
            "blocks": self.ast.blocks,
            "phases": self.ast.phases,
            "weights": self.ast.weights,
            "chazaka": self.ast.chazaka
        }

        with open(self.build_dir / "nodes.json", "w", encoding="utf-8") as f:
            json.dump({"nodes": nodes_data}, f, ensure_ascii=False, indent=2)

        with open(self.build_dir / "meta.json", "w", encoding="utf-8") as f:
            json.dump({"meta": meta_data}, f, ensure_ascii=False, indent=2)

        print(f"[+] ארטיפקטים של נתונים הופקו בתיקייה: {self.build_dir}/")

    def _write_python_executable(self) -> None:
        py_code = f'''# -*- coding: utf-8 -*-
# אוטומט קוד שנוצר מתוך שפת SL עבור המודל: {self.ast.model_name}

from sl_compiler import IterationEngine, HolographicStringNode
import json

def build_engine_from_compiled():
    # טעינת צמתים שנוצרו מהקומפיילר
    engine = IterationEngine(string_scale={self.ast.string_scale}, determinism_lock={str(self.ast.determinism_lock)})
    return engine

if __name__ == "__main__":
    eng = build_engine_from_compiled()
    state = eng.step()
    print("איטרציה ראשונה בוצעה בהצלחה תחת מודל SL.")
'''
        with open(self.build_dir / "ark_model_exec.py", "w", encoding="utf-8") as f:
            f.write(py_code)
        print(f"[+] קוד Python הפעיל הופק: {self.build_dir}/ark_model_exec.py")

    def run_autonomous_iterations(self, max_steps: int = 15) -> Dict[str, Any]:
        """מנוע אוטונומי המריץ איטרציות ברצף עד להשגת התכנסות אנטרופיה יעד"""
        if not self.ast:
            raise RuntimeError("יש לקמפל את המודל לפני הרצת איטרציות.")

        print(f"\n[{'='*70}]")
        print(f" 🌀 מנוע אוטונומי: הרצת לולאת איטרציות עבור {self.ast.model_name}")
        print(f"[{'='*70}]")

        engine = IterationEngine(string_scale=self.ast.string_scale, determinism_lock=self.ast.determinism_lock, nodes_list=self.ast.nodes)
        state = engine.export_state()

        for step in range(1, max_steps + 1):
            state = engine.step()
            meta = state["meta"]
            total_entropy = meta["total_entropy"]
            world_state = meta["world_state"]

            print(f"[*] איטרציה #{step:02d} | מצב עולם: {world_state} | אנטרופיה כוללת (dS): {total_entropy:.6f}")

            if total_entropy <= self.ast.target_entropy + 1e-6:
                print(f"[+] יעד האנטרופיה ({self.ast.target_entropy}) הושג בהצלחה באיטרציה {step}!")
                break

        final_nodes_path = self.build_dir / "nodes_converged.json"
        with open(final_nodes_path, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        print(f"[+] המצב ההתכנסותי הסופי נשמר ב: {final_nodes_path}")
        print(f"[{'='*70}]\n")
        return state


if __name__ == "__main__":
    sample_sl_code = """
    SL_MODEL ArkVitruvius42 {

      NODES {
        NODE א INDEX 1 RADIUS 1.1 BULK 90.9091 CHAOS 10.0;
        NODE ב INDEX 2 RADIUS 1.2 BULK 50.0 CHAOS 15.0;
        NODE ג INDEX 3 RADIUS 1.3 BULK 33.3 CHAOS 20.0;
        NODE ת INDEX 22 RADIUS 3.2 BULK 4.3478 CHAOS 115.0;
      }

      ARCH {
        BLOCK L1 NAME "Chesed" ROLE "Initial Radiation";
        BLOCK L7 NAME "Malkhut" ROLE "Material Closure";
        PROCESSOR_PHASE 1 "Crown Node" CLASS "Keter";
        PROCESSOR_PHASE 21 "Perimeter Guard" CLASS "Perimeter";
      }

      WEIGHTS {
        DOMAIN SEMANTIC  W_S;
        DOMAIN DOUBT     W_D;
        DOMAIN LOGICAL   W_L;
        CHAZAKA hashta 0.99995;
      }

      ENGINE {
        STRING_SCALE 1.618;
        DETERMINISM_LOCK TRUE;
        TARGET_ENTROPY 0.0;
      }

      OUTPUT {
        FORMAT JSON_STATE_V1;
        WRITE nodes.json;
        WRITE meta.json;
      }
    }
    """

    sl_path = "model.sl"
    with open(sl_path, "w", encoding="utf-8") as f:
        f.write(sample_sl_code)

    compiler = SLCompiler(sl_file_path=sl_path, build_dir="build")
    compiler.compile()
    compiler.run_autonomous_iterations(max_steps=10)

    if os.path.exists(sl_path):
        os.remove(sl_path)
