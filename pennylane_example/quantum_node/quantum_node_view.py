import pennylane as qml
from pennylane_example.quantum_node.creating_a_quantum_node import circuit
import numpy as np

print(qml.draw(circuit)(np.pi/4, 0.7))
