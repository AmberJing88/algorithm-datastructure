#Dynamic Programming
"""188;stock buy and sell; given price array, find the best profit algorithm. you can complete
 k times transactions.sell before buy again."""
class Solution:
    def maxprofit(self,k,prices):
        if len(prices)<2: return 0
        n = len(prices)
        if k>=n/2:
            return self.solvemax(prices,k)
        maxl, maxg = [0]*(k+1), [0]*(k+1)
        for i in range(n-1):
            diff = prices[i+1] - prices[i]
            for j in range(k,0,-1):
                maxl[j] = max(maxg[j-1]+max(diff,0), maxl[j]+diff)
                maxg[j] = max(maxg[j], maxl[j])
        return maxg[k]
    def solvemax(self,prices,k):
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                maxprofit += (prices[i]- prices[i-1])
        return maxprofit

#377
"""377;given an positive integer array,no duplicates,find the number of possible combinations thant
daa up to positive integer target. """
def combinationSum(nums,target):
    if not nums or len(nums)==0 or target<min(nums):
        return 0
    dp = [0 for _ in range(target+1)]
    dp[0] = 0
    for i in range(1,target+1):
        for n in nums:
            if i>=n:
                dp[i]= dp[i]+dp[i-n]
    return dp[-1]
# optimized method
def combinationSum(nums,target):
    if not nums or len(nums)==0 or target<min(nums):
        return 0
    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    nums.sort()
    for i in range(1,target+1):
        for n in nums:
            if i>=n:
                dp[i] = dp[i]+dp[i-n]
    return dp[-1]
# dfs+memo method
def combinationSum(nums,target):
    memo = {}
    def dfs(nums,target,memo):
        if target <0: return 0
        if target==0: return 1
        if target in memo:
            return memo[targt]
        combos = 0
        for num in nums:
            combos += dfs(nums, target-num,memo)
        memo[targt] = combos
    dfs(nums,target,memo)
    return memo[target]

#518
"""518; coin change; given coins of different denomination and a total amount of money. find the
number of combinations that make up that amount. infinite number of coins"""
def change(amount, coins):
    dp = [0 for _ in range(amount+1)]
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = dp[i] +dp[i-coin]
    return dp[amount]

#322
"""322; coin change; given coins of different denomination and a total amount of money. find the
fewest number of coins that make up that amount. infinite number of coins. return -1 if no combination."""
def coinchange(coins, amount):
    if not coins or len(coins)==0 or amount ==0:
        return 0
    if min(nums)>amount:
        return -1
    dp =[float('inf') for _ in range(amount+1)]
    dp[0] = 0
    for coin in coins:
        for i in range(coin,amount+1):
            if i==coin:
                dp[i]=1
            elif dp[i]==0 and dp[i-coin] !=0:
                dp[i] = dp[i-coin]+1
            elif dp[i-coin]!=0:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return -1 if dp[amount]==float('inf') else dp[amount]

#dfs+pruning method
def coinchange(coins, amount):
    coins.sort(reverse=True)
    n, res = len(coins), 2**31-1
    def dfs(pt, ren,count):
        if not ren:
            res = min(res,count)
        for i in range(pt,n):
            if coins[i]<=ren<coins[i]*(res-count):
                dfs(i,ren-coins[i],count+1)
    for i in range(n):
        dfs(i,amount,0)
    return res if res<2**31-1 else -1

#474
"""474; given a stringarray,only contain 0 and 1, integers m,n to find the maximum number of string
that you can form with given 0s and 1s. Note: each 1 and 0 only use once."""
def findmaxform(strs,m,n):
    if not strs or len(strs)==0:
        return 0
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for s in strs:
        one, zero = 0,0
        for c in s:
            if c=='0':
                zero += 1
            else:
                one += 1
        for i in range(m,zero-1,-1):
            for j in range(n,one-1,-1):
                dp[i][j] = max(dp[i][j],dp[i-zero][j-one])
    return dp[m][n]

#494
"""494; target sum; a non-negative integer array, and target, with +, - symbles. for each integer,
you should choose one from + and - as its new symble. Find out how many ways to assign symbles to make
sum of integers."""
def findtargetsum(nums,s):
    summ = sum(nums)
    if summ <s: or (summ+s)%2!=0:
        return 0
    total = (summ+s)//2
    dp = [0 for _ in range(total+1)]
    dp[0] = 0
    for num in nums:
        for i in range(total,num-1,-1):
            dp[i] = dp[i] +dp[i-num]
    return dp[total]

#416
"""416; pattition equal subset sum; array with positive integers, find if the array can be partitioned
into 2 subsets that sum of elements in both subsets is equal."""
def canPartition(nums):
    if len(nums) <=1: return False
    if not sum(nums) %2==0:
        return False
    summ = sum(nums)//2
    dp = [False for _ in range(summ+1)]
    dp[0] = True
    for num in nums:
        for i in range(sum,num-1,-1):
            dep[i] = dp[i] or dp[i-num]
    return dp[sum]

# 2D dp method
def partition(nums):
    total = sum(nums)
    if total & 1 ==1:
        return False
    total = total //2
    n = len(nums)
    dp = [[False for _ in range(total+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(1, n+1):
        dp[i][0] =True
    for i in range(1,n+1):
        for j in range(1,total+1):
            if j >=nums[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
    return dp[n][total]
