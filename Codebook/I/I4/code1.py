import numpy as np
import pennylane as qml

dev = qml.device("default.qubit", wires=1)

U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

@qml.qnode(dev)
def varied_initial_state(state):
    """Complete the function such that we can apply the operation U to
    either |0> or |1> depending on the input argument flag.
    
    Args:
        state (int): Either 0 or 1. If 1, prepare the qubit in state |1>,
            otherwise, leave it in state 0.
  
    Returns:
        array[complex]: The state of the qubit after the operations.
    """
    ##################
    if (state):
        qml.PauliX(wires=0)

    ##################

    # KEEP THE QUBIT IN |0> OR CHANGE IT TO |1> DEPENDING ON THE state PARAMETER

    # APPLY U TO THE STATE
    qml.QubitUnitary(U, wires=0)

    return qml.state()
