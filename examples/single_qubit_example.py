import sys
from quantum_state import QuantumState
from gates import H

sys.path.insert(0, 'C:/Users/IQBAL SINGH/OneDrive/Desktop/project3/quantum_simulation/quantum_state.py')

# Initialize a qubit in the |0> state
qubit = QuantumState()

# Apply Hadamard gate
qubit.apply_gate(H)

# Measure the qubit
measurement_result = qubit.measure()
print("Measurement result:", measurement_result)