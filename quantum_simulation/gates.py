# quantum_simulation/gates.py

import numpy as np

# Define single-qubit gates
X = np.array([[0, 1], [1, 0]])            # Pauli-X (NOT) gate
Y = np.array([[0, -1j], [1j, 0]])          # Pauli-Y gate
Z = np.array([[1, 0], [0, -1]])            # Pauli-Z gate
H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])  # Hadamard gate

# Define two-qubit gate
CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])  # Controlled NOT gate
