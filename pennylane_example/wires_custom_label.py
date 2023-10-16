import pennylane as qml

dev_unique_wires = qml.device("default.qubit", wires=["aux", "q1", "q2"])
