import pennylane as qml
import numpy as np

dev = qml.device('default.qubit', wires=3)

@qml.qnode(dev)
def make_basis_state(basis_id):
    """Produce the 3-qubit basis state corresponding to |basis_id>.
    
    Note that the system starts in |000>.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.
        
    Returns:
        array[complex]: The computational basis state |basis_id>.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # CREATE THE BASIS STATE
    str = np.binary_repr(basis_id, width=3)
    print(str)
    for i in range(3):
        if (int(str[i])):
            qml.PauliX(wires=i)

    return qml.state()


basis_id = 3
print(f"Output state = {make_basis_state(basis_id)}")