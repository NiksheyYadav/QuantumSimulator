import sys
from quantum_state import QuantumState
from gates import CNOT, H

sys.path.insert('quantum_simulation\gates.py')
# Initialize a two-qubit state in the |00> state
qubit1 = QuantumState()
qubit2 = QuantumState()
two_qubit_state = qubit1.tensor_product(qubit2)

# Apply Hadamard gate to the first qubit
two_qubit_state.apply_gate(H, 0)

# Apply CNOT gate with the first qubit as control and the second as target
two_qubit_state.apply_gate(CNOT, [0, 1])

# Measure the qubits
measurement_results = two_qubit_state.measure()
print("Measurement results:", measurement_results)