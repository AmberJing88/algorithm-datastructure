# Tree
"""687:longest univalue path: fien the longest length of each node in the path has the
same value. this path may or may not pass through the root."""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def longestUnivalue(self, root):
        self.longest = 0
        def helper(node):
            if not node:
                return 0,0
            max_left = max(helper(node.left))
            max_right = max(helper(node.right))
            if node.val == node.left.val:
                left = max_left+1
            else:
                left = 0
            if node.val = node.right.val:
                right = max_right+1
            else:
                right = 0
            self.longest = max(left+right, self.longest)
            return left, right
        return self.longest
# iteration method
def longestUnivalue(root):
    postorder = [(0, root, None)]
    count = 0
    d = {None:0}
    while postorder:
        see, node, parent = postorder.pop()
        if node is None: continue
        if not seen:
            postorder.append((1, node, parent))
            postorder.append((0, node.right, node.val))
            postorder.append((0, node.left, node.val))
        else:
            if node.val == parent:
                d[node] = max(d[node.left], d[node.right])+1
            else:
                d[node] = 0
            count = max(count, d[node.left]+d[node.right])
    return count
#337
"""337: house robber: there is only one entrance in this area, called root, besides the root, each house has
one and only one parent house. after a tour, all houses in this place forms a binary tree. it will automaticly
contact the police if two directly-linked houses were broken into on the same night."""
def rob(root):
    if not root:
        return 0
    def helper(node):
        if not node: return 0, 0
        left_with, left_without = helper(node.left)
        right_with, right_without = helper(node.right)
        node_with = node.val + left_without + right_without
        node_without = max(left_with, left_without) + max(right_with, right_without)
        return node_with, node_without
    return max(helper(root))

#671
"""671: second minimum node in BT:a binary tree consisting non-negative nodes, where each nodes
in this tree has exactly two or zero sub-nodes, if a node has two children, the value of node is
the smaller among its two sub-nodes. return -1 if no such smallest value."""
class Solution:
    def findSecondMin(self, root):
        min_val = root.val
        self.ans = float('inf')

        def helper(node):
            if not node: return
            if node.val == min_val:
                helper(node.left)
                helper(node.right)
            else:
                self.ans = min(self.ans, node.val)
        helper(root)
        return -1 if self.ans ==float('inf') else self.ans
#70
"""70: climb stairs: tack n steps from bottom to top, each time you can either climb 1 or 2 steps.
in how many distinct ways can you reach the top:"""
def climbstair(n):
    if n==0: return 0
    if n==1: return 1
    memo = [0] * (n+2)
    def climb(i, n, memo):
        if i >n:
            return 0
        if i==n:
            return 1
        if memo[i] >0:
            return memo[i]
        memo[i] = climb(i+1, n, memo)+ climb(i+2, n, memo)
        return memo[i]
    return climb(0, n, memo)

# 22
"""22: generae parentheses: given n pairs ofparenthese, write a function to generate all combinations
of well-formed parentheses."""
def generateparenthese(n):
    if n==0:
        return ''
    res = []
    def parenthese(n, l, r, s):
        if l==n and r==n:
            res.append(s)
        if l<n:
            parenthese(n, l+1, r, s+'(')
        if r <l:
            parenthese(n, l, r+1, s+')')
    parenthese(n, 0, 0, "")
    return res

#669
"""669: trim a bst: given a BST, and lowest and highest boundaries as L and R. trim the tree
so that all its elements lies in [L, R], you might need to change the root of the tree. so that
the result return the new root of trimed BST."""
class Solution:
    def trimBST(self, root, l, r):
        if not root:
            return None
        if root.val > r:
            return self.trimBST(root.left, l, r)
        if root.val < l:
            return self.trimBST(root.right, l, r)
        else:
            root.left = self.trimBST(root.left, l, r)
            root.right = self.trimBST(root.right, l,r)
        return root

#230
"""230: find the Kth smallest element in a BST."""
class Solution:
    def KthSmallestBST(self, root, k):
        self.k_l = []
        def inorder(root):
            if not root: return
            if root.left:
                inorder(root.left)
            self.k_l.append(roo.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        return self.k_l[k-1]  # inorder is the increment direction in BST

    #method iteration
    def Kthsmallest(self, root, k):
        s = []
        while True:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            k -= 1
            if not k:
                reurn root.val
            root = root.right

#98
"""98: validate BST: determin if a BST is valid, left subtree nodes less than root, right subtree nodes
larger than root, all subtrees are BST."""
class Solution:
    def isValidBST(self, root):
        if not root: return True
        self.res = []
        def inorder(node):
            if not node: return
            if node.left:
                inorder(node.left)
            self.res.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        for i in range(len(self.res)-1):
            if self.res[i] >= self.res[i+1]:
                return False
        return True

    #optimized method
def isValidBST(root):
    if not root:
        return True
    def valid(root, floor = float('-inf'), ceiling=float('inf')):
        if not root:
            return True
        if root.val >= ceiling or root.val <= floor:
            return False
        return valid(root.left, floor, root.val) and valid(root.right, root.val, ceiling)
    return valid(root, float('-inf'), float('inf'))

# iteration method
def isValidBST(root):
    s = []
    curr, pre = root, TreeNode(None)
    while s or curr:
        if curr:
            s.append(curr)
            curr = curr.left
        else:
            curr = s.pop()
            if pre and curr.val <= pre.val:
                return False
            pre = curr
            curr = curr.right
    return True

# opimized iteration method
def isvalidbst(root):
    if not root: return True
    stack = [(root, float('-inf'), float('inf'))]
    while stack:
        root, floor, ceiling = stack.pop()
        if not root:
            continue
        val = root.val
        if val <= floor or val >= ceiling:
            return False
        stack.append((root.right, val, ceiling))
        stack.append((root.left, floor, val))
    return True
