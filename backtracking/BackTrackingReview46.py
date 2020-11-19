#Back tracking
"""46; permutation: a collection of distinct integers, return all possible permutations."""
def permute(nums):
    def backtrack(sub):
        if len(sub)==n:
            res.append(sub[:])
        for i in range(n):
            if nums[i] in sub:
                continue
            sub.append(nums[i])
            backtrack(sub)
            sub.pop()
    res, n = [], len(nums)
    backtrack([])
    return res

# method2
def permute(nums):
    def dfs(start,end):
        if start==end:
            res.append(nums[:])
        for i in range(start,end):
            nums[start], nums[i] = nums[i],nums[start]
            dfs(start+1, end)
            nums[start], nume[i] = nums[i], nums[start]
    res = []
    dfs(0,len(nums))
    return res

#216
"""216;find all possible combinations of k numbers that add up to n, given that only number from 1-9
can be used and each combiantion should be unique.set of numbers."""
def combine(n,k):
    def backtrack(sub,k,n,start):
        if n<0:return
        if len(sub)==k and n==0:
            res.append(sub[:])
        for i in range(start,10):
            if i in sub: continue
            if i>n: break
            sub.append(i)
            backtrack(sub,k,n-i,i+1)
            sub.pop()
    res = []
    backtrack([],k,n,1)
    return res

#47
"""47;permutation,a collection of numbers may duplicate, return all possible permutations no duplicate"""
def permute(nums):
    def backtrack(nums,start):
        if start ==n-1:
            res.append(nums[:])
            return
        for i in range(start,n):
            if i >start and nums[i]==nums[start]:
                continue
            nums[start],nums[i] =nums[i],nums[start]
            backtrack(nums[:],start+1)
    res,n = [], len(nums)
    nums.sort()
    backtrack(nums,0)
    return res

#91
"""91 decode ways, message contain A-Z decode with A-1,B-2...Z-26, given non-empty string only containing
digits, determin the total number of decode."""
def numDecode(s):
    if s[0]=='0':return 0
    n = len(s)
    return ways(s,n-1)
def ways(s,n):
    if n <= 0: return 1
    count = 0
    if s[n]>'0':
        count += ways(s,n-1)
    if s[n-1]=='1' or (s[n-1]=='2' and s[n]<='6'):
        count += ways(s,n-2)
    return count

# dp method2
def numDecode(s):
    if s[0]=='0': return 0
    prev1 = 1
    if s[0] != 0:
        curr = 1
        prev2 = curr
    for i in range(1, len(s)):
        curr = 0
        if s[i]!='0':
            curr += prev2
        if 10 <= int(s[i-1:i+1]) <=26:
            curr += prev1
        prev1 = prev2
        prev2 = curr
    return curr

#247
"""247; strobogrammatic number;is a number that looks the same when rotate 180 degrees. find all strobogrammatic
numbers that length of n"""
def findStrobo(n):
    return find(n,n)
def find(m,n):
    if m==0: return ['']
    if m==1: return ['0','1','8']
    result = []
    centre = find(m-2,n)
    for c in centre:
        if m!=n:
            result.append('0'+c+'0')
        result.append('1'+c+'1')
        result.append('6'+c+'9')
        result.append('8'+c+'8')
        result.append('9'+c+'6')
    return result

# method2
def findStrobo(n):
    if n <= 0:
        return ['']
    if n%2==1:
        result = ['0','1''8']
    else:
        result = ['']
    strobo = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
    for i in range(n//2):
        result = [h+res+strobo[h] for res in result for h in strobo]
    return [res for res in result if (res[0]!='0' or n==1)]

#96
"""96 unique binary search tree,given n how many structurally unique bst's store value 1....n"""
def numTrees(n):
    memo = [-1]*(n+1)
    def helper(n,memo):
        if n<=1: return 1
        if memo[n]!=-1:
            return memo[n]
        count = 0
        for i in range(1,n+1):
            count += helper(i-1,memo) * helper(n-i,memo)
        memo[n] = count
        return count
    return helper(n,memo)









    return
