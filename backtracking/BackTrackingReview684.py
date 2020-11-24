#Back tracking
"""684 redundant connection: find the circle """
def findRedundant(edges):
    parent = [0]*len(edges)
    def find(x):
        if parent[x] ==0:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    def union(x,y):
        rootx,rooty = find(x), find(y)
        if rootx ==rooty:
            return False
        parent[rootx]=rooty
        return True
    for x, y in edges:
        if not union(x,y):
            return[x,y]
    raise(ValueError)
#dfs method
def findRedundant(edges):
    graph = collecions.defaultdict(set)
    def dfs(source,targt):
        if source==target:
            return True
        return any(dfs(neigh,target) for neigh in graph[source])
    for u,v in edges:
        seen = set()
        if u in graph and v in graph and dfs(u,v):
            return [u,v]
        graph[u].add(v)
        graph[v].add(u)

#261
"""261; graph valid tree, no cycle in the graph"""
def validTree(n,edges):
    parents= [0 for _ in range(n+1)]
    def find(x):
        if parent[x]==0: return x
        parents[x]= find(parent[x])
        return parent[x]
    for i,j in edges:
        rooti, rootj = find(i),find(j)
        if rooti ==rootj:
            return False
        parent[rooti]=rootj
    return len(edges)==n-1
#method 2
def validTree(n,edges):
    graph = {i:[] for i in range(n)}
    def dfs(node):
        neighs = graph.pop(node,[])
        for nei in neighs:
            dfs(nei)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    dfs(0)
    return not graph and len(edges)==n-1

#78
"""78; subset, integer set, return all possible subsets no duplicate"""
def subset(nums):
    def dfs(start,sub):
        if len(sub)==k:
            res.append(sub[:])
        for i in range(start,len(nums)):
            sub.append(nums[i])
            dfs(i+1,sub)
            sub.pop()
    res = []
    for k in range(len(nums)+1):
        dfs(0,[])
    return res
# methd2
def subset(nums):
    n = len(nums)
    res = [[]]
    for num in nums:
        res += [cur +[num] for cur in res]

#90
"""integers collections may have duplicate, return all possible subsets, no duplicate."""
def subsetwithDu(nums):
    nums = sorted(nums)
    def dfs(start,sub):
        res.append(s[:])
        for i in range(start,len(nums)):
            if i > start and nums[i]==nums[i-1]:
                continue
            sub.append(nums[i])
            dfs(i+1,sub)
            sub.pop()
    res  =[]
    dfs(0,[])
    return res

#77
"""77; combination, given two integers n and k return all possible combinations of k numbers out of 1-n"""
def combine(n,k):
    def dfs(start,sub):
        if len(sub)==k:
            res.append(sub[:])
        for i in range(start,n+1):
            sub.append(i)
            dfs(i+1, sub)
            sub.pop()
    res = []
    dfs(1,[])
    return res

# method 2
def combine(n,k):
    comb =[[]]
    for _ in range(k):
        combs = [[i]+c for c in combs for i in range(1,c[0] if c else n+1)]
    return combs

# 39
"""39 combination summation, given a set of candidates numbers and a target, return all the possible
combinations that candidates summation to equal to target, canbe repeated use multi times"""
def combination(nums,target):
    res = []
    n = len(nums)
    def helper(target,curr,start):
        if target < 0: return
        if target ==0:
            res.append(curr[:])
        else:
            for i in range(start,n):
                curr.append(nums[i])
                helper(target-nums[i],curr,i)
                curr.pop()
    helper(target,[],0)
    return res

#40
"""40; combinationIII, given a set of candidates numbers and a target, return all the possible
combinations that candidates summation to equal to target, each candidate can only be used once"""
def combination(nums,target):
    def backtrack(start,sub,left):
        if left <0: return
        if left==0:
            res.append(sub[:])
        else:
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                sub.append(nums[i])
                backtrack(i+1,sub,left-nums[i])
                sub.pop()
    res = []
    nums.sort()
    backtrack(0,[],target)
    return res        



    return
