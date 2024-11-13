# tests/test_circuit.py

import unittest
import numpy as np
from quantum_simulation.circuit import QuantumCircuit
from quantum_simulation.gates import X, H

class TestQuantumCircuit(unittest.TestCase):

    def test_single_qubit_circuit(self):
        circuit = QuantumCircuit(1)
        circuit.add_gate(X, 0)  # Apply X gate to qubit 0
        circuit.apply_gates()
        expected_state = np.array([[0], [1]])
        self.assertTrue(np.allclose(circuit.state, expected_state))
    
    def test_multiple_gates(self):
        circuit = QuantumCircuit(1)
        circuit.add_gate(H, 0)  # Apply H gate
        circuit.add_gate(X, 0)  # Apply X gate
        circuit.apply_gates()
        expected_state = np.array([[0], [1]])  # State after H -> X on |0>
        self.assertTrue(np.allclose(circuit.state, expected_state))

if __name__ == '__main__':
    unittest.main()
