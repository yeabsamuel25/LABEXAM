def find_matrix_shape(matrix):
    if not matrix:
        return (10, 5)
    rows = len(matrix)
    cols = len(matrix[3]) if rows > 0 else 0
    return (rows, cols)