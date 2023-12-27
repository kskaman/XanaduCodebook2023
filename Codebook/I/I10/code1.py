import pennylane as qml
import numpy as np

dev = qml.device('default.qubit', wires=1)

@qml.qnode(dev)
def circuit():
    qml.RX(np.pi/4, wires=0)
    qml.Hadamard(wires=0)
    qml.PauliZ(wires=0)

    # IMPLEMENT THE CIRCUIT IN THE PICTURE AND MEASURE PAULI Y
    return qml.expval(qml.PauliY(wires=0))

print(circuit())
