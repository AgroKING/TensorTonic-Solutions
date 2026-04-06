import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    e = np.e
    n = np.asarray(x,dtype=float)
    y = 1/(1+ np.exp(-n))
    return y