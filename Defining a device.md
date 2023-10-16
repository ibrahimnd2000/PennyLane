# Defining a device

- To run- and later optimize- a quantum circuit, one needs to first specify a _computational device_.
- instance of `Device` class, and either represent
- can be instantiated using the `device` loader.

![Defining a devce](./pennylane_example/defining_a_device.py)

### Devices

- `default.qubit`
- `default.mixed`
- `lightning.qubit`
- `default.gaussian`
- addtitional devices can be installed as plugins ([available plugins](https://pennylane.ai/plugins/))

> 💡 choice of a device significantly determines the speed of your computation, as well as the available options that can be passed to the device loader.
