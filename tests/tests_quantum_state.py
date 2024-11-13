# tests/test_quantum_state.py

import unittest

import numpy as np

from quantum_simulation.gates import H, X
from quantum_simulation.measurement import measure
from quantum_simulation.quantum_state import QuantumState


class TestQuantumState(unittest.TestCase):

    def test_initialization(self):
        state = QuantumState(np.array([[1], [0]]))
        self.assertTrue(np.allclose(state.state, np.array([[1], [0]])))
    
    def test_apply_gate(self):
        state = QuantumState(np.array([[1], [0]]))
        state.apply_gate(X)
        expected_state = np.array([[0], [1]])
        self.assertTrue(np.allclose(state.state, expected_state))
    
    def test_measurement(self):
        state = QuantumState(np.array([[1/np.sqrt(2)], [1/np.sqrt(2)]]))
        outcome, _ = state.measure()
        self.assertIn(outcome, [0, 1])

if __name__ == '__main__':
    unittest.main()
