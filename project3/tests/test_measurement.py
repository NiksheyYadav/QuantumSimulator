# tests/test_measurement.py

import unittest
import sys
from quantum_simulation.measurement import simulate_measurement
import numpy as np
sys.path.insert('quantum_simulation/measurement.py')

class TestMeasurement(unittest.TestCase):

    def test_measurement(self):
        state = np.array([[1/np.sqrt(2)], [1/np.sqrt(2)]])  # |+> state
        outcome, post_state = simulate_measurement(state)
        self.assertIn(outcome, [0, 1])  # Measurement should return 0 or 1
        self.assertTrue(np.allclose(post_state, state))  # Post-measurement state should match initial state for ideal case

if __name__ == '__main__':
    unittest.main()
