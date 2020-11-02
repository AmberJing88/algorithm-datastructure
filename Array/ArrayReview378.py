# Array problems
"""leetcode 378: sorted matrix in ascending order, find the kth smallest element in the matrix"""
def KthSmallest(matrix, k):
    m,n = len(matrix), len(matrix[0])
    low, high = matrix[0][0], matrix[m-1][n-1]
    while low <= high:
        cnt = 0
        mid = low + (high - low)//2
        for i in range(m):
            for j in range(n):
                if matrix[i][j] <= mid:
                    cnt += 1

        if cnt < k:
            low = mid +1
        else:
            high = mid -1
    return low

# method 2 heap queue method
import heapq
def kthsmallest(matrix, k):
    rows, cols = len(matrix), len(matrix[0])
    if k > (rows *cols)//2:
        back = True
        k = row *cols -k+1
        frontier = [(-matrix[rows-1][cols-1],rows-1,cols-1)]
    else:
        back = False
        frontier = [(matrix[0][0],0,0)]
    while k:
        val, r, c = heapq.heappop(frontier)
        k -= 1
        if not back:
            if c != len(matrix[0]-1):
                heapq.heappush(frontier,(matrix[r][c+1],r, c+1))
            if c ==0 and r != len(matrix)-1:
                heapq.heappush(frontier,(matrix[r+1][c],r+1,c))
        else:
            if c != 0:
                heapq.heappush(frontier, (matrix[r][c-1], r, c-1))
            if c == cols-1 and r != 0:
                heapq.heappush(frontier, (-matrix[r-1][c], r-1, c))
    return -val, if back else val


"""array 645: set s contains number from 1 to n, but one of numbers gotcopied to
 another number in the set, which result in repetation, and loss of another number.
 find out the two errors."""
 def FindErrorNums(nums):

     for num in nums:
         if nums[abs(num)-1] < 0:
             duplicate = abs(num)
         else:
             nums[abs(num)-1] *= -1
     for i, n in enumerate(nums):
         if n >0:
             missing = i+1
             break
     return duplicate, missing

""" array 448: array of integers 1 <= a[i] <= n (size n), some elements appear twice, and
others appear once. find all dispeeared number."""
def FindMissing(nums):
    for n in nums:
        n = abs(n)
        nums[n-1] = -abs(nums[n-1])
    return [i+1 for i, n in enumerate(nums) if n>0]

Note: do not use brute force to solve, because nums unsorted, time O(N) >O(n).
