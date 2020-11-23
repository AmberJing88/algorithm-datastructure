#Dynamic Programming
"""Fibonachi problem; 母牛生产问题，一只小母牛从第三年开始生产小母牛，每年都生产一头，每只小母牛3年之后成熟，
又可以生产小牛，求n年后，母牛的数量。假设牛不死亡。"""
def numCows(n):
    if n <=3:
        return n
    dp = [0 for _ in range(n+1)]
    dp[1], dp[2],dp[3] = 1, 2, 3
    for i in range(4,n+1):
        dp[i] = dp[i-1]+dp[i-3]
    return dp[n]

# wrong letter envilope
"""有N个信和信封，被打乱，求错误装信的方式。"""
def wrongletters(n):
    if n <=1: return 0
    dp = [0 for _ in range(n+1)]
    dp[0],dp[1],dp[2] = 0,0,1
    for i in range(2,n):
        dp[i+1] = dp[i-1]*i +dp[i]*i
    return dp[-1]

#276
"""276;paint fence; n fence need to paint.we have k colors, no more than two adjacent fence postes.
have the same color,determin how many ways to paint the fence."""
def numWays(n,k):
    if n==0: return 0
    if n==1: return k
    same,diff = 0,k
    for i in range(2,n+1):
        t = diff
        diff = (same +diff)*(k-1)
        same = t
    return same+diff
# method
def numWays(n,k):
    if n==0: return 0
    if n==1: return 1
    same,diff = 0,k
    res = same +diff
    for i in range(2,n+1):
        same = diff
        diff = res *(k-1)
        res = same + diff
    return res

#198
"""198; house robber:a rray with nonnegative integers. cannot rob connected index.value.
determin the amount of most money robbed tonight."""
def rob(nums):
    if not nums or len(nums)==0:
        return 0
    if len(nums)==1: return nums[0]
    de = [0 for _ in range(len(nums)+1)]
    dp[0], dp[1] = 0, nums[0]
    for i in range(1,len(nums)):
        dp[i+1] = max(dp[i], dp[i-1]+nums[i])
    return dp[-1]
#method 2
def rob(nums):
    if not nums or len(nums)==0: return 0
    if len(nums)==1: return nums[0]
    dp = [0 for _ in range(len(nums))]
    dp[0], dp[1] = nums[0],nums[1]
    for i in range(2, len(nums)):
        temp = [dp[j]+nums[i] for j in range(i-1)] +[dp[i-1]]
        dp[i] = max(temp)
    return temp

#213
"""213: house robberII; array of circle, first and last connected, cannot rob connected house.
determin the most money."""
def rob(nums):
    if not nums or len(nums)==0:
        return 0
    if len(nums) <= 3:
        return max(nums)
    def robb(nums,i,j):
        robbed,not_robbed = 0,0
        for idx in range(i,j):
            num = nums[idx]
            robbed, not_robbed = not_robbed + num, max(robbed, not_robbed)
        return max(robbed, not_robbed)
    n = len(nums)
    return max(robb(nums,1,n), robb(nums,0,n-1))

# cut steel
"""钢条切割问题，given price-length table: 1 2 3 4 5  6  7  8  9  10
steel length                              1 2 8 9 10 17 17 20 24 30. how to cut steel to get most money"""
def cut(p,n):
    if n==0: return 0
    res = 0
    for i in range(1,n+1):
        res = max(res,p[i-1]+cut(p,n-i))
    return res

# top-down dp method
def cutmemo(p,n):
    if n==0: return 0
    memo = [-1]*(len(p)+1)
    def cut(p,n,memo):
        temp = -1
        if memo[n]>=0:
            return memo[n]
        if n==0:
            temp = 0
        else:
            for i in range(1,n+1):
                temp = max(temp, p[i-1]+cut(p,n-i),memo)
        memo[n] = temp
        return temp
    return cut(p,n,memo)

#method 3 bottom-up dp
def bottom_up_cut(p,n):
    r = [0] * (len(p)+1)
    for i in range(1, len(p)+1):
        q = -1
        for j in range(1,i+1):
            q = max(q,p[j-1]+r[i-j])
        r[i] = q
    return r[n]

#413
"""413; arithmetic sequence; given an array with intebers, count the number of sub sequence
of arithmetic sequece."""
def numArithmetic(nums):
    res, n = 0, len(nums)
    dp = [0 for _ in range(n+1)]
    for i in range(2,n):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            dp[i] = dp[i-1]+1
        res += dp[i]
    return res

# method 2
def numArithmetic(nums):
    res, cur = 0,0
    for i in range(2, len(nums)):
        if nums[i]-nums[i-1]==nums[i-1] -nums[i-2]:
            cur += 1
            res += cur
        else:
            cur = 0
    return res
