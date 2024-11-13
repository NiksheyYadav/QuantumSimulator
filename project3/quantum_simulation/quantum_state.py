# quantum_simulation/quantum_state.py

import numpy as np


class QuantumState:
    def __init__(self, state=np.array([[1], [0]])):
        """Initialize the qubit in the |0> state by default."""
        self.state = state
    
    def apply_gate(self, gate):
        """Apply a gate (matrix) to the qubit's state vector."""
        self.state = np.dot(gate, self.state)
    
    def measure(self):
        """Measure the qubit and return 0 or 1 based on probability amplitudes."""
        probabilities = np.abs(self.state) ** 2
        result = np.random.choice([0, 1], p=[probabilities[0, 0], probabilities[1, 0]])
        print(f"Measurement result: {result}")
        return result
