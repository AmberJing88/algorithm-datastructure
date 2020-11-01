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

# method 2, binary search method
class Solution:
    def helper(self, matrix, target, start_x, start_y, rows, cols):
        if not matrix: return False
        if rows <=0 or col <=0:
            return False
        mid_x = start_x +rows // 2
        mid_y = start_y + cols// 2
        if matrix[mid_x][mid_y] == target:
            return True
        elif rows == 1 and cols ==1:
            return False
        elif matrix[mid_x][mid_y] < target:
            if self.helper(matrix, target, start_x,strat_y, rows//2, cols-cols//2):
                return True
            if self.helper(matrix, target, start_x,strat_y, rows-rows//2, cols//2):
                return True
            if self.helper(matrix, target, start_x,strat_y, rows-rows//2, cols-cols//2):
                return True
        else:
            if self.helper(matrix, target, start_x,strat_y, rows//2, cols-cols//2):
                return True
            if self.helper(matrix, target, start_x,strat_y, rows-rows//2, cols//2):
                return True
            if self.helper(matrix, target, start_x,strat_y, rows//2, cols//2):
                return True
        return False
    
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        start_x, start_y = 0, 0
        rows, cols = len(matrix), len(matrix[0])
        return self.helper(matrix, target, start_x, start_y, rows, cols)
        
        
