import pennylane as qml


def my_quantum_function(x, y):
    qml.RZ(x, wires="q1")
    qml.CNOT(wires=["aux", "q1"])
    qml.RY(y, wires="q2")
    return qml.expval(qml.PauliZ("q2"))
