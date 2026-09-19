import json
import tempfile
import unittest
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("chatgpt_bridge", ROOT / "scripts" / "chatgpt_bridge.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class ChatGPTBridgeTests(unittest.TestCase):
    def test_no_change_is_not_significant(self):
        state = {"architecture": {"core_flow": ["A"]}, "model_fabric": {"connected_slots": 0, "verified_slots": 0}, "autonomy": {}, "wix": {}, "source_history_policy": {}}
        self.assertEqual(mod.classify(state, state), (None, []))

    def test_foundational_change_is_s3(self):
        old = {"architecture": {"core_flow": ["A"]}, "model_fabric": {}, "autonomy": {}, "wix": {}, "source_history_policy": {}}
        new = {"architecture": {"core_flow": ["A","B"]}, "model_fabric": {}, "autonomy": {}, "wix": {}, "source_history_policy": {}}
        sig, changed = mod.classify(old, new)
        self.assertEqual(sig, "S3")
        self.assertIn("architecture", changed)

    def test_model_verification_change_is_s1(self):
        old = {"architecture": {}, "model_fabric": {"connected_slots": 0, "verified_slots": 0}, "autonomy": {}, "wix": {}, "source_history_policy": {}}
        new = {"architecture": {}, "model_fabric": {"connected_slots": 1, "verified_slots": 1}, "autonomy": {}, "wix": {}, "source_history_policy": {}}
        sig, changed = mod.classify(old, new)
        self.assertEqual(sig, "S1")
        self.assertIn("model_fabric.connected_slots", changed)

if __name__ == "__main__":
    unittest.main()
