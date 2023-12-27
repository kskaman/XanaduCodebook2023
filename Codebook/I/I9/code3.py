import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=1)

def prepare_psi():
    qml.RX(-2*np.pi/3, wires=0)

@qml.qnode(dev)
def measure_in_y_basis():
    ##################
    # YOUR CODE HERE #
    ##################
    
    # PREPARE THE STATE
    prepare_psi()
    # PERFORM THE ROTATION BACK TO COMPUTATIONAL BASIS
    qml.adjoint(qml.S(wires=0))
    qml.Hadamard(wires=0)
    # RETURN THE MEASUREMENT OUTCOME PROBABILITIES

    return qml.probs(wires=0)

print(measure_in_y_basis())
