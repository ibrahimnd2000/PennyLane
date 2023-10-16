import matplotlib.pyplot as plt
import pennylane as qml
from pennylane_example.quantum_node.creating_a_quantum_node import circuit
import numpy as np

qml.drawer.use_style("black_white")

fig, ax = qml.draw_mpl(circuit)(np.pi/4, 0.7)
plt.show()
