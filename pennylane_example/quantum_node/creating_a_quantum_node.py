import pennylane as qml
from pennylane_example.wires_quantum_function_with_label import my_quantum_function
from pennylane_example.wires_custom_label import dev_unique_wires

circuit = qml.QNode(my_quantum_function, dev_unique_wires)
