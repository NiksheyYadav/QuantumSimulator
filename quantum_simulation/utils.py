# quantum_simulation/utils.py

import numpy as np


def tensor_product(*states):
    """Compute the tensor product of multiple quantum states."""
    result = states[0]
    for state in states[1:]:
        result = np.kron(result, state)
    return result
