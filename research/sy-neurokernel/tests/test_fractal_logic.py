import unittest

from sy_neurokernel.fractal_logic import (
    CrystalSymmetricLogic,
    FractalRationalLogic,
    LetterContractionExpansionLogic,
    Provenance,
)


class FractalLogicTests(unittest.TestCase):
    def test_crystal_has_231_symmetric_gates(self):
        logic = CrystalSymmetricLogic()
        self.assertEqual(len(logic.gates), 231)
        state = tuple(range(22))
        scores = logic.evaluate(state)
        reverse = logic.evaluate(tuple(reversed(state)))
        self.assertEqual(len(scores), 231)
        self.assertNotEqual(scores, reverse)

        # Endpoint order within a gate is symmetric.
        a, b = logic.gates[0]
        self.assertEqual((state[a] + state[b]) / 2.0,
                         (state[b] + state[a]) / 2.0)

    def test_contraction_reduces_deviation_from_center(self):
        logic = LetterContractionExpansionLogic()
        state = tuple(float(i) for i in range(22))
        center = sum(state) / 22.0
        out = logic.transform(state, contraction=0.5, expansion=0.0)
        self.assertEqual(len(out), 22)
        self.assertLess(
            sum(abs(x - center) for x in out),
            sum(abs(x - center) for x in state),
        )

    def test_fractal_layer_emits_message(self):
        logic = FractalRationalLogic()
        state = tuple((i % 5) - 2 for i in range(22))
        msg = logic.speak(state, contraction=0.2, expansion=0.3, depth=2)
        self.assertEqual(msg.kind, "NEURAL_DIALOGUE_STATE")
        self.assertEqual(msg.depth, 2)
        self.assertEqual(len(msg.payload), 22)
        self.assertEqual(msg.provenance, Provenance.GENERATED_MESSAGE)

    def test_invalid_state_is_rejected(self):
        logic = FractalRationalLogic()
        with self.assertRaises(ValueError):
            logic.speak((0.0,) * 21, 0.1, 0.1)


if __name__ == "__main__":
    unittest.main()
