# tests/test_gates.py

import unittest
import numpy as np
from quantum_simulation.gates import X, H

class TestGates(unittest.TestCase):

    def test_x_gate(self):
        state = np.array([[1], [0]])
        result = np.dot(X, state)
        expected_result = np.array([[0], [1]])
        self.assertTrue(np.allclose(result, expected_result))

    def test_h_gate(self):
        state = np.array([[1], [0]])
        result = np.dot(H, state)
        expected_result = np.array([[1/np.sqrt(2)], [1/np.sqrt(2)]])
        self.assertTrue(np.allclose(result, expected_result))

if __name__ == '__main__':
    unittest.main()
