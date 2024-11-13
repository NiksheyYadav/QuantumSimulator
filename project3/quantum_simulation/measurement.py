# quantum_simulation/measurement.py

import numpy as np


def measure(state):
    """Measure a quantum state and return a binary result for each qubit."""
    probabilities = np.abs(state) ** 2
    outcome = np.random.choice([0, 1], p=[probabilities[0, 0], probabilities[1, 0]])
    print(f"Measurement result: {outcome}")
    return outcome
