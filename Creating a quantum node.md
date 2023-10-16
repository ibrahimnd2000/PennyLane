# Creating a quantum node

- Together a [quantum function](./Quantum%20functions.md) and a [device](./Defining%20a%20device.md) are used to create a _quantum node_ or `QNode` object.
- It wraps the quantum function, and binds it to the device.

Can be created as:

![Quantum Node](./pennylane_example/quantum_node/creating_a_quantum_node.py)

### QNode

- compute the result of a [quantum circuit](./Quantum%20circuits.md) as if it was a standard Python function.
- Takes same arguments as the original [quantum function](./Quantum%20functions.md)

![quantum node result](./pennylane_example/quantum_node/quantum_node_result.py)

#### View quantum circuit

- To view the quantum circuit given specific paramter values, we can use the `draw()` transform.

![Draw quantum circuit](./pennylane_example/quantum_node/quantum_node_view.py)

or the `draw_mpi()` transform

![Quantum Node Matplotlib](./pennylane_example/quantum_node/quantum_node_view_mpl.py)
