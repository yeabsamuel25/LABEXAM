import numpy as np

def compute_cross_product(array1, array2):
    
    Compute, the cross product of two arrays.

    Parameters:
    array1 (numpy.ndarray): First input array.
    array2 (numpy.ndarray): Second input array.

    Returns:
    numpy.ndarray: The cross product of the two arrays.
    
    return np.cross(array1, array2)