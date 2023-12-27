import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=1, shots=100000)

@qml.qnode(dev)
def circuit():
    qml.RX(np.pi/4, wires=0)
    qml.Hadamard(wires=0)
    qml.PauliZ(wires=0)

    return qml.sample(qml.PauliY(wires=0))
    


def compute_expval_from_samples(samples):
    """Compute the expectation value of an observable given a set of 
    sample outputs. You can assume that there are two possible outcomes,
    1 and -1. 
    
    Args: 
        samples (array[float]): 100000 samples representing the results of
            running the above circuit.
        
    Returns:
        float: the expectation value computed based on samples.
    """

    # RETURN THE MEASUREMENT SAMPLES OF THE CORRECT OBSERVABLE
    

    # USE THE SAMPLES TO ESTIMATE THE EXPECTATION VALUE

    return np.mean(samples)


samples = circuit()
print(compute_expval_from_samples(samples))
