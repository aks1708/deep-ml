def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    m, n = len(a), len(a[0])
    result = [[0]*m for i in range(n)]
    
    for i, el in enumerate(a):
        for j in range(n):
            result[j][i] = el[j]
    
    return result
    