# -*- coding: utf-8 -*-
"""
Tests for sl_compiler module.
"""

import os
import json
import tempfile
import pytest
from pathlib import Path

from sl_compiler import (
    SLParser,
    SLModelAST,
    SLCompilerPipeline,
    SLCompiler,
    IterationEngine,
    HolographicStringNode,
    HEBREW_LETTERS,
    SLKernelDefinition,
    SLModelDefinition,
    SLAppDefinition
)


def test_sl_parser_parse_script():
    script_text = """
    kernel ARK {
      string_scale      = 1.618
      determinism_lock  = true
      nodes             = 22
      blocks            = 7
      phases            = 21
    }
    model ARK_VITRUVIUS {
      name = "ARK_VITRUVIUS"
      world_state = "BERUDIM_TRANSITION"
    }
    app ARK_SL_RUNTIME {
      name = "ARK_SL_RUNTIME"
      action_trigger = "ANALYZE_TEXT"
    }
    """
    ast = SLParser.parse_script(script_text)
    assert isinstance(ast["kernel"], SLKernelDefinition)
    assert ast["kernel"].string_scale == 1.618
    assert ast["kernel"].nodes == 22
    assert isinstance(ast["model"], SLModelDefinition)
    assert ast["model"].name == "ARK_VITRUVIUS"
    assert isinstance(ast["app"], SLAppDefinition)
    assert ast["app"].name == "ARK_SL_RUNTIME"


def test_sl_compiler_pipeline():
    with tempfile.NamedTemporaryFile("w", suffix=".sl", delete=False, encoding="utf-8") as tmp:
        tmp.write("""
        kernel ARK {
          string_scale = 1.618
          determinism_lock = true
        }
        """)
        tmp_path = tmp.name

    try:
        pipeline = SLCompilerPipeline(tmp_path)
        bundle = pipeline.compile()

        assert bundle["target_engine"] == "ark_kernel_engine.py"
        assert "metadata" in bundle
        assert "runtime_spec" in bundle
        assert bundle["metadata"]["kernel_name"]["string_scale"] == 1.618
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)


def test_sl_parser_parse_dsl_model():
    sample_sl_code = """
    SL_MODEL ArkVitruvius42 {

      NODES {
        NODE א INDEX 1 RADIUS 1.1 BULK 90.9091 CHAOS 10.0;
        NODE ב INDEX 2 RADIUS 1.2 BULK 50.0 CHAOS 15.0;
      }

      ARCH {
        BLOCK L1 NAME "Chesed" ROLE "Initial Radiation";
        BLOCK L7 NAME "Malkhut" ROLE "Material Closure";
        PROCESSOR_PHASE 1 "Crown Node" CLASS "Keter";
      }

      WEIGHTS {
        DOMAIN SEMANTIC  W_S;
        CHAZAKA hashta 0.99995;
      }

      ENGINE {
        STRING_SCALE 1.618;
        DETERMINISM_LOCK TRUE;
        TARGET_ENTROPY 0.0;
      }
    }
    """
    ast = SLParser.parse(sample_sl_code)
    assert isinstance(ast, SLModelAST)
    assert ast.model_name == "ArkVitruvius42"
    assert len(ast.nodes) == 2
    assert ast.nodes[0].letter == "א"
    assert ast.blocks["L1"] == "Chesed"
    assert ast.phases[1] == "Crown Node"
    assert ast.weights["W_S"] == "SEMANTIC"
    assert ast.chazaka["hashta"] == 0.99995


def test_sl_compiler_compilation_and_artifacts():
    sample_sl_code = """
    SL_MODEL TestModel {
      ENGINE {
        STRING_SCALE 1.618;
        DETERMINISM_LOCK TRUE;
        TARGET_ENTROPY 0.0;
      }
    }
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        sl_file = Path(tmpdir) / "test_model.sl"
        sl_file.write_text(sample_sl_code, encoding="utf-8")

        build_dir = Path(tmpdir) / "build"
        compiler = SLCompiler(sl_file_path=str(sl_file), build_dir=str(build_dir))
        compiler.compile()

        assert (build_dir / "nodes.json").exists()
        assert (build_dir / "meta.json").exists()
        assert (build_dir / "ark_model_exec.py").exists()

        with open(build_dir / "meta.json", "r", encoding="utf-8") as f:
            meta = json.load(f)
            assert meta["meta"]["model_name"] == "TestModel"

        state = compiler.run_autonomous_iterations(max_steps=10)
        assert state["meta"]["total_entropy"] <= 1e-5
        assert (build_dir / "nodes_converged.json").exists()


def test_iteration_engine_entropy_reduction():
    engine = IterationEngine(string_scale=1.618)
    initial_entropy = sum(n.entropy for n in engine.nodes)
    step1 = engine.step()
    entropy1 = step1["meta"]["total_entropy"]
    assert entropy1 < initial_entropy
