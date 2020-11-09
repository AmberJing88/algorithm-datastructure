#128
"""longest consecutive sequence:given an unsorted array of integers find the length of the
longest consecutive elements sequence."""
def longestconsecutive(nums):
    nums = set(nums)
    longest = 0
    for num in nums:
        if num -1 not in nums:
            current = num
            curr_cnt = 1
            while current +1 in nums:
                current += 1
                curr_cnt += 1
            longest = max(longest, curr_cnt)
    return longest

def longest(nums):
    nums = set(nums)
    longest = 0
    while nums:
        first = last +nums.pop()
        while first -1 in nums:
            first -= 1
            nums.remove(first)
        while last+1 in nums:
            last += 1
            nums.remove(last)
        longest = max(longest, last - first+1)
    return longest

#696
"""696: count binary substring, count the number of substring which contain the same number
of 0' and 1' and all 0 and 1 are grouped consecutively"""
def countbinary(s):
    res , pre, cur = 0,0,1
    n = len(s)
    for i in range(1,n):
        if s[i]==s[i-1]:
            cur += 1
        else:
            pre = cur
            cur = 1
        if pre >= cur:
            res += 1
    return res

#104
"""maximum depth of dinary tree: given a binary tree find its maimum depth longest path from root to a leaf."""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def maxDepth(self, root):
        if root is None:
            return 0
        if not root.left and not root.right:
            return 1
        while root.left or root.right:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#110
"""110:balanced binary tree: given a binary tree, determin if it is height-banlanced. the binary tree in
which the left and right subtrees of every node difference in height no more than 1."""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def isBalanced(self,root):
        def balance(node):
            if not node:
                return 0
            lef_balance = balance(node.left)
            right_balance = balance(node.right)
            if left_balance == -1 or right_balance ==-1:
                return -1
            if abs(left_balance - right_balance) >1:
                return -1
            return max(left_balance, right_balance) +1
        return balance(root) != -1

#543
"""543:diameter of binary tree: given a binary tree, you need to compute the length of the diameter of
the tree. the diameter is the length of the longest path between any two nodes in a tree. this path may
not pass through the root."""
def diameterofbinarytree(root):
    result = 0
    def maxdepth(node):
        if not node:
            return 0
        left = maxdepth(node.left)
        right = maxdepth(node.right)
        result =max(result, left +right)
        return 1 + max(left, right)
    maxdepth(root)
    return result
#226
"""226: invert binary tree: left to right and viseversa."""
def inVertTree(root):
    if not root:
        return None
    root.left, root.right = inVertTree(root.right), inVertTree(root.left)
    return root

from queue import Queue
def inverttree(root):
    if not root:
        return None
    q = Queue()
    q.put(root)
    while q:
        node = q.get()
        temp = node.left
        node.left = node.right
        node.right = temp
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return root
#617
"""617: merge two binary tree: given two binary trees, put one of them to cover the other, some nodes are
overlaped while others are not. merge them into a new binary tree. the merge rule is that if two nodes overlap,
sum the them as the value of the merge node."""
def mergeTrees(t1, t2):
    if not t1: return t2
    if not t2: return t1

    new = TreeNode(t1.val+t2.val)
    new.left = mergeTrees(t1.left, t2.left)
    mew.right = mergeTrees(t1.right, t2.right)
    return new
