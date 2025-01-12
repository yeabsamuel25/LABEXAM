import numpy as np

def reconstruct_matrix(U, S, V):
    """
    Reconstruct the original matrix from its SVD components.

    Parameters:
    U (numpy.ndarray): Left singular vectors.
    S (numpy.ndarray): Singular values.
    V (numpy.ndarray): Right singular vectors.

    Returns:
    numpy.ndarray: The reconstructed original matrix.
    """
    # Convert S to a diagonal matrix
    S_matrix = np.diag(S)
    # Reconstruct the original matrix
    original_matrix = np.dot(U, np.dot(S_matrix, V))
    return original_matrix