""" Reshape the rows and columns of given matrix at same row-traversing order."""
def ReshapeMatrix(nums):
    temp = []
    r, c = 0, 0
    for n in nums:
        temp += n
    reshape = []
    if r * c == len(temp):
        for j in range(0, len(temp),c):
            reshape.append(temp[j:j+c])
        return reshape

def reshapematrix(nums):
    row, col = len(nums), len(nums[0])
    r, c = 0, 0
    temp = []
    reshape = [[]]
    for n in nums:
        temp += n
    if row * col != r *c:
        return nums
    else:
        for i in range(row):
            for j in range(col):
                if len(reshape[-1]) ==c:
                    reshape.append([])
                reshape[-1].append(nums[i][j])
        return reshape
