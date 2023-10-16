# Quantum circuits

- Quantum computations, which involve the execution of one or more quantum circuits, are represented as _quantum node_ objects.
- Quantum node is used to declare the quantum circuit, and also ties the computation to a specific device that executes it.
- Can interface with any of the supported numerical and machine learning libraries-NumPy, PyTorch, TensorFlow, and JAX-indicated by providing an optional interface argument when creating a QNode.
- Each interface allows the quantum circuit to integrate seamlessly with library-specific data structures (e.g., NumPy and JAX arrays or Pytorch/TensorFlow tensors) and optimizers.
  ![PennyLane](https://docs.pennylane.ai/en/stable/_images/qnode.png)
