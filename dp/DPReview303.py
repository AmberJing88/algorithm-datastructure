#Dynamic Programming
"""303;range sum query imutable; given an integer array uns, find the sum of the elements between
i and j,inclusive."""
class NumArray:
    def __init__(self,nums):
        self.sum = [0]
        for i in range(len(nums)):
            self.sum.append(self.sum[i]+uns[i])
    def subRange(self,i,j);
    return self.sum[j+1] -self.sum[i]
class NumArray:
    def __init__(self,nums):
        self.nums = nums
    def sumRange(self,i,j):
        return sum(self.nums[i:j+1])

#64
"""minimum path sum; find the minimum path sum form top-left to bottom-right, in a grid. only can
move to right or down at any point of time."""
def minPathSum(grid):
    m,n = len(grid), len(grid[0])
    min_path = [float('inf') for _ in range(n+1)]
    min_path[1] = 0
    for row in range(1,m+1):
        new_min_path = [float("inf") for _ in range(n+1)]
        for col in range(1,n+1):
            new_min_path[col] = grid[row-1][col-1]+min(min_path[col],new_min_path[col-1])
        min_path = new_min_path
    return minpath[-1]

def minpath(grid):
    if len(grid)==0 or len(grid[0])==0:
        return 0
    m,n = len(grid),len(grid[0])
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    dp[0][0] = grid[0][0]
    for i in range(1,m+1):
        dp[i][0] = grid[i][0]+dp[i-1][0]
    for i in range(1,n+1):
        dp[0][i] = grid[0][i]+dp[0][i-1]
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j] = grid[i][j]+min(dp[i-1][j],dp[i][j-1])
    return dp[m-1][n-1]

#300
"""300; longest sorted subsequence. given an unsorted array if integers,find the longth of longest
subsequence,increasing."""
def lenghtlis(nums):
    if not nums or len(nums)==0: return 0
    dp = [0 for _ in range(len(nums)+1)]
    dp[1] = 1
    for i in range(len(nums)):
        max_cnt = 1
        for j in range(i):
            if nums[i]>nums[j]:
                max_cnt = max(max_cnt,dp[j]+1)
        dp[i] = max_cnt
    for i in range(len(dp)):
        res = max(dp)
    return res

def lengthlis(nums):
    lis = []
    for num in nums:
        nb =binary_search(num,lis)
        if nb==len(lis)-1:
            lis.append(num)
        else:
            lis[nb+1] = min(num,lis[nb+1])
    return len(lis)
def binary_search(num,lis):
    left,right = 0,len(lis)-1
    while left <= right:
        min = (left+right)//2
        if num <=lis[mid]:
            right = mid-1
        else:
            left = mid+1
    return right

#91
"""91; decode ways; given a string of numbers, decode to letters a-z. a-1,b-2...z-26. determin
 the number of decode ways."""
def numdecode(s):
    if len(s)==0 or s[0]=='0':
        return 0
    if len(s)==0: return 1
    dp = [0 for _ in range(len(s)+1)]
    dp[0], dp[1] = 1, 1
    for i in range(1, len(s)):
        if s[i] !='0':
            dp[i+1] += dp[i]
        if (0<=int(s[i-1:i+1])<=26):
            dp[i+1] += dp[i-1]
    return dp[len(s)]

def waysdecode(s):
    if s[0]=='0' or len(s)==0:
        return 0
    prev1 = 1
    if s[0]!='0':
        curr =1
        prev2 = curr
    for i in range(1,len(s)):
        curr = 0
        if s[i] !='0':
            curr += prev2
        if 10 <=int(s[i-1:i+1])<=26:
            curr += prev1
        prev1 =prev2
        prev2=curr
    return curr

#279
"""279; perfect squares: integer n, find the least number of perfect squares 1,4,9,16,...
which sum to n"""
def numSquares(n):
    while True:
        d,m = divmod(n,4)
        if m:
            break
        else:
            n = d
    if n%8 ==7:
        return 4
    elif (n**0.5).is_integer():
        return 1
    else:
        squares = [i**2 for i in range(1,int(n**0.5))]
        i,j = 0, len(squares)-1
        while i<=j:
            s = squares[i]+squares[j]
            if s<n:
                i+=1
            elif s>n:
                j-=1
            else:
                return 2
        return 3

def numSquares(n):
    dp = [float('inf') for _ in range(n+1)]
    dp[0] = 0
    for i in range(n+1):
        j = 1
        while j*j <= (n-i):
            dp[i+j*j] = min(dp[i+j*j],dp[i]+1)
            j += 1
    return dp[-1]

#343
"""343;integer break; positive integer n, break at least two positive integers, and maximize the
product of those integer, return the maximum product.
"""
def integerbreak(n):
    dp = [1 for _ in range(n+1)]
    for i in range(3,n+1):
        for j in range(1,i):
            dp[i] = max(dp[i],max(j*(i-j),j*dp[i-j]))
    return dp[-1]

#math method
def integerbreak(n):
    d,m = divmod(n,3)
    if m==0:
        return 2 if n==3 else 3**d
    if m==1:
        return 1 if n==1 else 3**(d-1)*4
    if m==2:
        return 1 if n==2 else 3**d*2

#376
"""376; wiggle subsequence; the difference between successive numbers strictly alternate between
positive and negative. a sequence with fewer than two elements is trivially a wiggle sequence.
return the length of wiggle subsequence."""
def wiggle(nums):
    if len(nums)<2: reutrn len(nums)
    up = [1 for _ in range(len(nums))]
    down = [1 for _ in range(len(nums))]
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                up[i] = max(down[i-1]+1,up[i])
            elif nums[i]<nums[j]:
                down[i] = max(down[i], up[i-1]+1)
    return max(up[-1], down[-1])

#method 2
def wigglength(nums):
    if len(nums)<2:
        return len(nums)
    up, down = 1,1
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            up = down +1
        elif nums[i]<nums[i-1]:
            down = up+1
    return min(len(nums),max(up,down))
