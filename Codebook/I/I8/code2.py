import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def prepare_state():
    qml.RX(np.pi/3, wires=0)

    # APPLY OPERATIONS TO PREPARE THE TARGET STATE

    return qml.state()
