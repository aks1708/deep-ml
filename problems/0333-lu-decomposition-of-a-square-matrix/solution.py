import numpy as np

def lu_decomposition(A: list) -> tuple:
    """
    Perform LU decomposition on a square matrix using Doolittle's method.

    Args:
        A: Square matrix as a list of lists

    Returns:
        tuple: (L, U) where L is lower triangular with 1s on diagonal,
               U is upper triangular, and A = L @ U
    """
    A = np.array(A, dtype=float)
    n = A.shape[0]
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square")

    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n):
        # Upper triangular: row i of U
        for j in range(i, n):
            U[i, j] = A[i, j] - L[i, :i] @ U[:i, j]

        # Lower triangular: column i of L
        for j in range(i + 1, n):
            if U[i, i] == 0:
                raise ValueError("Zero pivot encountered; decomposition without pivoting fails")
            L[j, i] = (A[j, i] - L[j, :i] @ U[:i, i]) / U[i, i]

    return L, U
