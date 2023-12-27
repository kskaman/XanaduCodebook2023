import numpy as np
import pennylane as qml

# CREATE A DEVICE
dev = qml.device("default.qubit", wires=1)
# CREATE A QNODE CALLED apply_hxh THAT APPLIES THE CIRCUIT ABOVE
@qml.qnode(dev)
def apply_hxh(state):
    
    if (state):
        qml.PauliX(wires=0)
    qml.Hadamard(wires=0)
    qml.PauliX(wires=0)
    qml.Hadamard(wires=0)
    
    return qml.state()
    
# Print your results
print(apply_hxh(0))
print(apply_hxh(1))
