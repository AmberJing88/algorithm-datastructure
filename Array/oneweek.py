#283
def movezeros(nums):
    i = 0
    for n in nums:
        if n != 0:
            nums[i] = n
            i += 1
    nums[i:] = [0]*(len(nums)-i)
#566
def reshapematrix(matrix, r, c):
    temp = []
    for n in matrix:
        temp += n
    reshape = []
    if r *c == len(temp):
        for j in range(0, len(temp), c):
            reshape.append(temp[j:j+c])
    return reshape
def reshapem(matrix, r, c):
    row, col = len(matrix), len(matrix[0])
    temp = []
    reshape = [[]]
    for n in nums:
        temp += n
    if row * col != r *c:
        return matrix
    else:
        for i in range(row):
            for j in range(col):
                if len(reshape[-1]==c):
                    reshape.append([])
                reshpae[-1].append(matrix[i][j])
    return reshape

#485
def maxconsecutiveones(nums):
    maxx, curr = 0, 0
    for n in nums:
        if n==1:
            curr += 1
            if curr > maxx:
                maxx = curr
        else:
            curr = 0
    return maxx
def maxconse(nums):
    maxx= []
    curr = 0
    for n in nums:
        if i == 1:
            curr += 1
        maxx. append(curr)
    return max(maxx)
#240
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    row, col = len(matrix), len(matrix[0])
    r, c = 0, col-1
    while r < row and c >= 0:
        if matrix[r][c] == target:
            return True
        if target > matrix[r][c]:
            r += 1
        else:
            c -= 1
    return False
#378
def KthSmallest(nums,k):
    m,n = len(matrix), len(matrix[0])
    low, high = matrix[0][0], matrix[m-1][n-1]
    while low <= high:
        cnt = 0
        mid = low + (high - low) // 2
        for i in range(m):
            for j in range(n):
                if matrix[i][j] <= mid:
                    cnt += 1
        if cnt < k:
            low = mid +1
        else:
            high = mid -1
    return low
from heapq import *
def kthsmallest(matrix, k):
    row, col = len(matrix), len(matrix[0])
    if k > (row * col) //2:
        back = True
        k = row * col -k +1
        frontier = [(-matrix[row-1][col-1], row-1, col-1)]
    else:
        back = False
        frontier = [(matrix[0][0],0,0)]
    while k:
        val, r, c = heapq.heappop(frontier)
        k -= 1
        if not back:
            if c != len(matrix[0]-1):
                heapq.heappush(frontier, (matrix[r][c+1],r, c+1))
            if c == col-1 and r != 0:
                heapq.heappush(frontier, (-matrix[r-1][c], r-1, c))
    return -val, if back else val

#645
def findErrors(nums):
    for num in nums:
        if nums[abs(num)-1] <0:
            duplicate = abs(num)
        else:
            nums[abs(num)-1] *= -1
    for i, n in enumerate(nums):
        if n >0:
            missing = i+1
            break
    return[duplicate, missing]

#448
def findmissing(nums):
    for n in nums:
        n = abs(n)
        nums[n-1] = -abs(nums[n-1])
    return [i+1 for i, n in enumerate(nums) if n >0]
