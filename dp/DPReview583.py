#Dynamic Programming
"""583; delete epration for two strings, find the minimum number of steps to make two given strings
same, where in each step you can delete one character in either string. (EDIT DISTANCE)"""
def minDistance(word1,word2):
    m,n = len(word1), len(word2):
    if m==0: return n
    if n==0: return m
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1,n+1):
            if word1[i-1]==word2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    return m+n-2*dp[m][n]
# dp + edit distance method
def minDistance(word1, word2):
    m,n = len(word1), lend(word2)
    dp = [[0 for _ in range(n+1)] for _ in rane(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for i in range(n+1):
        dp[0][i] = i
    for i in range(1, m+1):
        for j in range(1,n+1):
            if word1[i-1] ==word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+1
    return dp[m][n]

#72
"""72; edit distance; given two words, find the minimum number of operations required to convert
word1 to word2, you can inset, delete or replace a character once step."""
def minDistance(word1,word2):
    m,n = len(word1), len(word2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for i in range(n+1):
        dp[0][i] = i
    for i in range(1,m+1):
        for j in range(1, n+1):
            if word1[i-1]==word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+1
    return dp[m][n]
#DFS+memo method
def minDistance(word1, word2):
    def helper(i,j):
        if i<0 or j<0:
            return i+1+j+1
        if (i,j) in memo:
            return memo[(i,j)]
        if word1[i]==word2[j]:
            result = helper(i-1,j-1)
        else:
            result = 1+ min(helper(i-1,j-1),helper(i,j-1),helper(i-1j))
        memo[(i,j)] = result
        return result
    memo = {}
    return helper(len(word1)-1,len(word2)-1)

#650
"""650; two key board; initially on a motepad only one character is present, you can perform two
operations on this notepad for each step.1.copyall,2.paste the character copied last time."""
def minSteps(n):
    if n==1: return 0
    res = n
    for i in range(n-1,1, -1):
        if n%i ==0:
            res = min(res, minSteps(n//i)+i)
    return res
# dp
def minSteps(n):
    dp = [0 for _ in range(n+1)]
    h = int(math.sqrt(n))
    for i in range(2,n+1):
        dp[i] = i
        for j in range(2,h+1):
            if i%j ==0:
                dp[i] = dp[j]+dp[i//j]
                break
    return dp[n]
# mathmetics
def minSteps(n):
    if n==1: return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return i+minSteps(n//i)
    return n

#139
"""139; word break;given a string and a dict, containing words, determin if string can be segmented into
a space seperated. squence of one or more dictinary words.same word can be reused multiple times."""
def wordBreak(string, dict):
    if not dict or len(dict)==0:
        return False
    dp = [False for _ in range(len(string)+1)]
    dp[0] = True
    for i in range(1,len(string)+1):
        for word in dict:
            n = len(word)
            if n<=i and word ==s[i-n:i]:
                dp[i] = dp[i] or dp[i-n]
    return dp[len(string)]

#122
"""122;stock buy and sell; given price array, find the best profit algorithm no limit of transaction times.
sell before buy again."""
def maxprofit(prices):
    if len(prices)<2:
        return 0
    profit = 0
    for i in range(1,len(prices)):
        if prices[i] >prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

#121
"""121;stock buy and sell; given price array, find the best profit algorithm. you can only complete
 transaction.sell before buy again. """
def maxProfit(prices):
    if len(prices) <2: return 0
    buy, res = float('inf'), 0
    for price in prices:
        buy = min(buy, price)
        res = max(res, price-buy)
    return res
# kadane algorithm
def maxprofit(prices):
    if len(prices)<2: return 0
    gain = [0 for _ in range(len(prices)-1)]
    for i in range(len(gain)):
        gain[i] = prices[i+1] - prices[i]
    localmax, globalmax = 0,0
    for i in range(1,len(prices)):
        localmax = max(0, localmax+gain[i-1])
        globalmax = max(localmax,globalmax)
    return globalmax

#123
"""123; stock buy and sell; given price array, find the best profit algorithm. you can complete
 most two transactions.sell before buy again."""
 def maxprofit(prices):
     if len(prices)<2:
         return 0
    localmax = [[0]*3 for _ in range(len(prices))]
    globalmax = [[0]*3 for _ in range(len(prices))]
    for i in range(1,len(prices)):
        diff = prices[i] - prices[i-1]
        for j in range(1,3):
            localmax[i][j] = max(globalmax[i-1][j-1]+max(diff,0), localmax[i-1][j]+diff)
            globalmax[i][j] =max(globalmax[i-1][j], localmax[i][j])
    return globalmax[n-1][2]
# dp method
def maxprofit(prices):
    if len(prices) <2: return 0
    n = len(prices)
    maxl, maxg = [0] *3, [0]*3
    for i in range(n-1):
        diff = prices[i+1] - prices[i]
        for j in range(2,0,-1):
            maxl[j] = max(maxg[j-1]+max(diff,0),maxl[j]+diff)
            maxg[j] = max(maxl[j],maxg[j])
    return maxg[2]
        
