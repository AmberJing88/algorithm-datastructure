# Tree
"""94:inorder traversal return nodes in the inorder sequence"""
class Solution:
    def inorderTravesal(self,root):
        if not root: return []
        self.ans = []
        def helper(node):
            if not node: return
            if node.left: helper(node.left)
            self.ans.append(node.val)
            if node.right: helper(node.right)
        helper(root)
        return self.ans
# iteration method
    def inorder(root):
        if not root: return []
        result = []
        s, head = [], root
        while s or head:
            if head:
                s.append(head)
                head = head.left
            else:
                head = s.pop()
                result.append(head.val)
                head = head.right
        return result
# Morris order traversal
class MorrisTraversal:
    def MorrisInorder(self,root):
        if not root: return []
        result = []
        curr, pre = root, TreeNode(None)
        while curr:
            if not root.left:
                result.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                if not pre.right:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    result.append(curr.val)
                    curr = curr.right
        return result

#Back tracking
"""44:wild card match: given an input string and a pattern,inplement wildcard. pattern matching wiht
support for "?" for a single charactor and "*" for any sequence of charactors."""
def isMatch(s,p):
    i,j,star = 0,0,-1
    while i < len(s):
        if j >= len(p) or p[j] not in {'*','?'} and p[j] != s[i]:
            if star == -1:
                return False
            j = star +1
            star_i += 1
            i = star_i
        elif p[j] =='*':
            star = j
            star_i = i
            j += 1
        else:
            i += 1
            j += 1
    while j < len(p):
        if p[j] != '*':
            return False
        j += 1
    return True
# DP method
def isMatch(s, p):
    dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
    for i in range(len(s)+1):
        for j in range(len(p)+1):
            start_s, start_p = i-1,j-1
            if i==0 and j==0:
                dp[i][j] = True
            elif i==0:
                dp[i][j] = p[start_p] =='*' and dp[i][j-1]
            elif j==0:
                dp[i][j] = False
            elif p[start_p]=='*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            elif s[start_s]==p[start_p] or p[start_p]=='?':
                dp[i][j] = dp[i-1][j-1]
    return dp[len(s)][len(p)]

#17
"""17: given a string containing digits from 2-9 include, return all possible letter combinations that
the number could represent."""
def letterCombine(digit):
    res = []
    mapp = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    def backtrack(sub,start,mapp):
        if len(sub)==len(digits):
            res.append(sub[:])
        for i in range(start, len(digits)):
            for j in mapp[digits[i]]:
                backtrack(sub+j,j+1,mapp)
    backtrack('',0,mapp)
    return res
# backtrack method
def lettercombine(digits):
    res = []
    keys = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    if not digits or len(digits)==0:
        return []
    def DFS(sub, index, keys):
        if len(sub)==len(digits):
            res.append(sub[:])
            return
        curdigit = int(digits[index])
        letters = keys[curdigit]
        for i in letters:
            sub += i
            DFS(sub,index+1,keys)
            sub = sub[-1]
    DFS('',0,keys)
    return res

#93
"""93: given a string containing only digits restore it by returning all possible valid IP
address combinations. Note IP: four exactly integers all between 0~255."""
def IPaddress(s):
    addresses = []
    if len(s)==0 or len(s)>12:
        return []
    def dorestore(k,temp,s):
        if k==4 or len(s)==0:
            addresses.append(temp[:])
            return
        for i in range(len(s)):
            if i<=2:
                if i !=0 and s[0]=='0':
                    break
                part = s[:i+1]
                if int[part] <=255:
                    if len(temp)!=0:
                        part='.' +part
                    temp += part
                    dorestore(k+1,temp,s[i+1:])
                    temp = temp[:(len(temp)-len(part))]
    dorestore(0,'',s)
    return addresses

#79
"""79:word search; given 2D board and a word, find if the word exists in the grid, the word can
be constructed from letters of sequentially adjacent cell, where adjacent cells are those
horizontally or vertically neibouring. the same letter cell may not be used more than once."""
def exist(board,word):
    if not board: return False
    def DFS(board, i, j, word):
        if len(word)==0:
            return True
        if i<0 or i>=len(board) or j<0 or j>len(board[0]) or word[0]!=board[i][j]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        res = DFS(board,i+1,j, word[1:]) or DFS(board, i-1,j,word[1:]) or
            DFS(board,i,j+1,word[1:]) or DFS(board,i,j-1,word[1:])
        board[i][j] = temp
        return res
    for i in range(len(board)):
        for j in range(len(board[0])):
            if DFS(board,i,j,word):
                return True
    return False

#257
"""257 given a binary tree, return all root-leaf path."""
def binarytree(root):
    if not root: return []
    def DFS(node, temp):
        if not node.left and not node.right:
            res.append(tem+str(node.val))
        temp += str(node.val) +'->'
        if node.left:
            DFS(node.left,temp)
        if node.right:
            DFS(node.right,temp)
    res = []
    DFS(root,'')
    return res
# iteration stack
def binarytree(root):
    if not root: return []
    while stack:
        node,ls = stack.pop()
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.right:
            stack.append((node.right,ls+str(node.val)+'->'))
        if node.left:
            stack.append((node.left,ls+str(node.val)+'->'))
    return res

#131
"""131: given a string s, partition s such that every substring of partition is a palindrome
return all palindrome partitions of s"""
class Solution:
    def partition(self,s):
        if not s: return []
        self.res = []
        self.doPart(s,[])

    def doPart(self,s, temp):
        if len(s) ==0:
            self.res.append(temp[:])
            return
        def ispalindrome(s,start,end):
            while start<end:
                if s[start] != s[end]:
                    return False
            return True
        for i in range(0,len(s)):
            if ispalindrome(s,0,i):
                temp.append(s[:i+1])
                self.doPart(temp,s[i+1:])
                remp.pop()
