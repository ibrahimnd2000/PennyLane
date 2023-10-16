#### Hashable

- An object is hashable if it has a hash value that does not change during its entire lifetime.

# Device options

- options can be passed as keyword arguments, and can differ based on the device.

### Most important device options

- `wires` - number of wires
- `shots` - how many times the circuit should be evaluated (or "sampled") to estimate statistical quantities.

##### Wires:

- `int`
- defines the _number of wires_ that you can address by consecutive integer labels `0, 1, 2, ...`

![wires](./pennylane_example/wires.py)

###### Alternatively,

- you can use custom labels by passing an iterable that contains unique labels for the subsystems

![alternative wires](./pennylane_example/wires_custom_label.py)

In [quantum function](./Quantum%20functions.md), you can now use your own label to address wires:

![Quantum function with label](./pennylane_example/wires_quantum_function_with_label.py)

- Allowed wire labels can be any type that is [_hashable_](#hashable), which allows two wires to be uniquely distinguished

> 💡 Some devices, such as hardware chips, may have a fixed number of wires. The iterable of labels passed to the device's `wires` argument must match this expected number of wires.

> ❗️ In order to support wire labels of any hashable type, integers and 0-d arrays are considered different. For example, running `qml.RX(1.1, qml.numpy.array(0))` on a device initialized with `wires=[0]` will fail because `qml.numpy.array(0)` does not exist in the device's wire map.

##### Shots:

- `int`
- defines how many times the circuit should be evaluated (or "sampled") to estimate statistical quantities.
- On some supported simulator devices, `shots=None` computes measurement statistics exactly.

> 💡 This argument can be temporarily overwritten when a QNode is called. For example, `my_qnode(shots=3)` wille temporarily evaluate `my_qnode` using three shots. This is a feature of QNode and it is not necessary to manually implement the `shots` keyword argument of the [quantum function](./Quantum%20functions.md)

###### Shot Batching

- It is sometimes useful to retrieve the result of computation for different shot numbers without evaluating a QNode several times.
- Batches of shots can be specified by passing `int[]`, allowing measurement statistics to be course-grained with a single QNode evaluation.

Consider,

![shot batching](./pennylane_example/shot_batching.py)

- When QNodes are executed on this device, a single execution of 1015 shots will be submitted.
- However, three sets of measurement statistics will be returned; using the first 5 shots, second set of 10 shots, and final 1000 shots, separately.

For example:

![Shot Batching Example 1](./pennylane_example/shot_batching_example1.py)

Executing this, we will get an output of shape (3, 2):

![Shot Batching Result](./pennylane_example/shot_batching_result.py)

We can index into this tuple and retrieve the results computed with only 5 shots:
![Shot batching indexing](./pennylane_example/shot_batching_indexing.py)
