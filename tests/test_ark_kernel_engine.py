# -*- coding: utf-8 -*-
"""
Tests for ark_kernel_engine module.
"""

import pytest
from ark_kernel_engine import ARKKernelEngine, execute_sl_bundle
from sl_compiler import SLCompilerPipeline


def test_ark_kernel_engine_execution():
    engine = ARKKernelEngine(string_scale=1.618, determinism_lock=True)

    dummy_bundle = {
        "target_engine": "ark_kernel_engine.py",
        "metadata": {
            "kernel_name": {"string_scale": 1.618, "determinism_lock": True},
            "model_name": "TEST_MODEL"
        },
        "runtime_spec": {
            "app_name": "TEST_APP"
        }
    }

    result = engine.execute_bundle(dummy_bundle, steps=2)
    assert result["engine"] == "ark_kernel_engine.py"
    assert result["app_name"] == "TEST_APP"
    assert result["executed_steps"] == 2
    assert result["state"]["meta"]["iteration"] == 2
    assert len(result["state"]["nodes"]) == 22


def test_execute_sl_bundle_convenience():
    dummy_bundle = {
        "target_engine": "ark_kernel_engine.py",
        "metadata": {
            "kernel_name": {"string_scale": 1.618, "determinism_lock": True},
            "model_name": "CONVENIENCE_TEST"
        },
        "runtime_spec": {
            "app_name": "CONVENIENCE_APP"
        }
    }

    result = execute_sl_bundle(dummy_bundle, steps=1)
    assert result["app_name"] == "CONVENIENCE_APP"
    assert result["state"]["meta"]["iteration"] == 1
