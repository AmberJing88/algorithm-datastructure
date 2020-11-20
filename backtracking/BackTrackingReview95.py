#Back tracking
"""95; unique binary search treeII,given integer n, generate all structurally unique bst that has 1-n"""
def generatebst(n):
    if n<=0: return []
    def helper(left,right):
        if left>right: return [None]
        result = []
        for i in range(left,right+1):
            lefttree = helper(left,i-1)
            righttree = helper(i+1,right)
            for l in lefttree:
                for r in righttree:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    result.append(root)
        return result
    return helper(1,n)

#241
"""241;different ways to add parenthese; given a string of numbers, and opeators, return all possible
results from computing all the group of numbers and operators '+','-','*' """
#devide and conquer
class Solution:
    def diffwaystocompute(self,input):
        if input =='': return None
        pointer, parsed = 0, []
        for i in range(len(input)):
            if not inpu[i].isdigit():
                parsed.append(int(input[pointer:i]))
                parsed.append(input[i])
                pointer = i+1
        parsed.append(int(input[pointer:]))
        return self.diff(parsed,0,len(input)-1,{})
    def diff(self,parsed,left,right,memo):
        if left == right:
            return[parsed[left]]
        if (left,right) in memo:
            return memo[(left,right)]
        result = []
        for i in range(left+1,right,2):
            leftpart = self.diff(parsed,left,i-1,memo)
            rightpart = self.diff(parsed,i+1,right,memo)

            for l in leftpart:
                for r in rightpart:
                    if parsed[i] == '+': result.append(l+r)
                    if parsed[i] =='-': result.append(l-r)
                    if parsed[i] == '*': result.append(l*r)
        memo[(left,right)] = result
        return result

#39
"""39,combination: a set of numbers no duplicates, and a target, find all unique numbers sum to target.
the same number can be used unlimited times."""
def combination(self,candidates,target):
    result = []
    def helper(nums, target,next,partial,result):
        if target ==0:
            result.append(partial)
            return
        if next ==len(nums):
            return
        i = 0
        while target - (i*nums[next]) >=0:
            helper(nums,target-(i*nums[next]),next+1,partial+(i*nums[next]),result)
            i += 1
    helper(candidates,target,0,[],result)
    return result

#51
"""51; N Queens, NxN board, N queens, each one has one row, one col, diagnal and verse diagnal"""
class NQueens:
    def NQueens(self,n):
        res = []
        self.dfs([-1]*n,0,[],res)
        return res

    def dfs(self,nums,index,path,res):
        if index == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums,index):
                temp = '.' * len(nums)
                self.dfs(nums,index+1,path+temp[:i]+'Q'+temp[i+1:],res)

    def valid(self,nums,index):
        for i in range(index):
            if abs(nums[i] - nums[index])== index-i or nums[i]==nums[index]:
                return False
        return True

#70
"""70 climb stairs,"""
def climbstairs(n):
    memo = [0] *n
    def climb(n,i,memo):
        if i >n :return 0
        if i==n: return 1
        if memo[i] >0:
            return memo[i]
        memo[i] = climb(n,i+1,memo) +climb(n, i+2,memo)
        return memo[i]

#22
"""22 generate parenthese:"""
def generateparenthese(n):
    if n==0: return ''
    res = []
    def generaet(l,r,n,s):
        if l ==n and r==n:
            res.append(s)
        if l <n:
            generate(l+1,r,n,s+'(')
        if r <l:
            generate(l,r+1,n,s+')')
    generate(0,0,n,'')
    return res

#111
"""111 minmum depth of binary tree"""
def MindepthBT(root):
    if not root: return 0
    left = Mindepth(root.left)
    right = Mindepth(root.right)
    if not left or not right:
        return 1 + left +right
    return 1 + min(left,right)
