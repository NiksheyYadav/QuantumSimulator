## Usage Guide for quantum_simulation

This guide dives into how to utilize the `quantum_simulation` library for simulating quantum systems. We'll explore building quantum circuits, applying gates, measuring states, and more.

### Basic Concepts

Before diving into code examples, let's revisit some key concepts:

* **Qubits:** The fundamental unit of information in quantum computing, represented as a quantum state that can be 0, 1, or a superposition of both.
* **Quantum Gates:** Operations performed on qubits to manipulate their states. Common gates include Hadamard, Pauli-X, and controlled gates.
* **Quantum Circuits:** Sequences of quantum gates applied to specific qubits, representing a computation or simulation.
* **Measurement:** Obtaining information from a quantum state, collapsing it into a classical state (0 or 1) with a specific probability.

### Building Quantum Circuits

The `quantum_simulation` library provides building blocks for constructing quantum circuits.

**1. Importing the library:**

```python
from quantum_simulation import Circuit, Qubit
```

This imports the `Circuit` class for building circuits and the `Qubit` class for representing qubits.

**2. Creating Qubits:**

```python
q0 = Qubit()  # Create a qubit in the initial state (|0>)
q1 = Qubit()  # Create another qubit
```

**3. Adding Gates:**

```python
circuit = Circuit()
circuit.add_gate(HGate(), q0)  # Apply Hadamard gate to qubit 0
circuit.add_gate(CNOTGate(control=q0, target=q1))  # Apply CNOT gate controlled by q0 on q1
```

This creates a circuit object and adds two gates:

* `HGate()` applied to `q0` (Hadamard gate)
* `CNOTGate(control=q0, target=q1)` applied with `q0` as control and `q1` as the target qubit (controlled NOT gate)

**4. Visualizing the circuit (optional):**

```python
from quantum_simulation import visualization

visualization.plot_circuit(circuit)
```

This line calls the visualization module to generate a visual representation of the circuit.

### Applying Gates and Measurements

* **Adding multiple gates:** You can chain `add_gate` calls to build complex circuits.
* **Applying measurements:**

```python
from quantum_simulation import measure

probabilities = measure(circuit)
print(probabilities)  # Prints probability of each possible outcome
```

The `measure` function takes the circuit and returns a dictionary with probabilities for each possible measurement outcome.

### Example: Bell State Circuit

Let's build a circuit representing the Bell state, a maximally entangled state:

```python
from quantum_simulation import HGate, CNOTGate

circuit = Circuit()
circuit.add_gate(HGate(), Qubit())  # Apply Hadamard on qubit 0
circuit.add_gate(CNOTGate(control=Qubit(), target=Qubit()))  # Apply CNOT on qubits 1 and 2

# Measure both qubits and print probabilities
probabilities = measure(circuit)
print(probabilities)
```

This code creates a circuit for the Bell state and prints the probabilities of possible measurement outcomes.

**Additional Resources:**

* The `quantum_simulation` API reference provides detailed information on available gates, functions, and classes.
* Explore more complex examples (e.g., Deutsch-Josz algorithm) to delve deeper into quantum simulation capabilities.

This is a starting point for using `quantum_simulation`. Experiment with different gates, circuits, and measurements to explore the fascinating world of quantum simulations!
