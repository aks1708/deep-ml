import numpy as np

def cholesky_decomposition(A):
    """
    Perform Cholesky decomposition on a symmetric positive-definite matrix.

    Args:
        A: A symmetric positive-definite matrix (2D list or numpy array)

    Returns:
        L: Lower triangular matrix such that A = L @ L.T as a 2D list,
           or -1 if decomposition is not possible
    """
    A = np.array(A, dtype=float)
    n = A.shape[0]
    if A.shape[0] != A.shape[1]:
        return -1

    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):
            s = L[i, :j] @ L[j, :j]
            if i == j:
                diag = A[i, i] - s
                if diag <= 0:          # not positive-definite
                    return -1
                L[i, j] = np.sqrt(diag)
            else:
                L[i, j] = (A[i, j] - s) / L[j, j]

    return L.tolist()