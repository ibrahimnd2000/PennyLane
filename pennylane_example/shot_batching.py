import pennylane as qml

shots_list = [5, 10, 1000]

dev = qml.device("default.qubit", wires=2, shots=shots_list)
