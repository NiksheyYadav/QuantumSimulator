# quantum_simulation/circuit.py

import sys

import numpy as np

from .quantum_state import QuantumState

sys.path.insert('C:/Users/IQBAL SINGH/OneDrive/Desktop/project3/quantum_simulation/quantum_state.py')

class QuantumCircuit:
    def __init__(self, num_qubits):
        """Initialize a quantum circuit with a specified number of qubits."""
        self.num_qubits = num_qubits
        self.state = np.kron(*[np.array([[1], [0]])] * num_qubits)  # Initial |0...0> state
        self.gates = []

    def add_gate(self, gate, qubit_index):
        """Add a gate to the circuit, to be applied to a specified qubit."""
        self.gates.append((gate, qubit_index))

    def apply_gates(self):
        """Apply all gates in sequence."""
        for gate, qubit_index in self.gates:
            if self.num_qubits == 1:
                self.state = np.dot(gate, self.state)
            else:
                # Extend to handle multi-qubit cases with tensor products as needed
                pass  # Placeholder for handling multi-qubit gate applications
