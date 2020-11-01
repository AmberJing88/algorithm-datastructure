""" search 2D matrix,search for a value in m*n matrix."""
def SearchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    row, col = len(matrix), len(matrix[0])
    r, c = 0, col -1
    while r < row and c >= 0:
        if matrix[r][c] == target:
            return True
        if target > matrix[r][c]:
            r += 1
        else:
            c -= 1
    return False
