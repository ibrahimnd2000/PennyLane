# Quantum functions

- Quantum ciruit as a special Python function

![Quantum function](./pennylane_example/quantum_circuit.py)

> 💡 Wires refer to a quantum subsystem-for most devices, this corresponds to a qubit. For continous-variable devices, it corresponds to a quantum mode.

### Constraints:

- Accepts classical input, consists of quantum operators or sequences of operators called Templates.
- Contain classical flow control structures, such as `for` loops or `if` statements.
- Return a single or tuple of _measurement values_, by applying a `measurement function` to the qubit register.

> 💡 Quantum functions are evaluated on a device from within a QNode.
