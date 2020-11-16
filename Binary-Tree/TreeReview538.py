# Tree
"""538:convert BST to greater as every key of the original bst is changed to the original key plus
 sum of all keys """
class Solution:
    def convertBST(self, root):
        head = root
        self.summ = 0
        def traversal(node):
            if not node: return
            if node.right:
                traversal(node.right)
            self.summ += node.val
            node.val = self.summ
            if node.left:
                traversal(node.left)
        traversal(head)
        return root
    # iteration
    def convertbst(root):
        total = 0
        node = root
        s = []
        while s or node:
            if node:
                s.append(node)
                node = node.right
            else:
                node = s.pop()
                total += node.val
                node.val = total
                node = node.left
        return root
#235
"""235 lowest common ancestor BST; find the lowest common ancestor of two node in a BST
Note: a node to be a descendant of itself."""
def lowestCommonAncestor(root, p, q):
    if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
        return root
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    else:
        return lowestCommonAncestor(root.right, p, q)
#optimized method
def lowestca(root, p, q):
    if q.val > root.val and p.val>root.val:
        return lowestca(root.right, p, q)
    if q.val < root.val and p.val < root.val:
        return lowestca(root.left, p, q)
    else:
        return root
#iteration
def LCA(root, p, q):
    node = root
    while node:
        if p.val > node.val and q.val>node.val:
            node = node.right
        if p.val < node.val and q.val < node.val:
            node = node.left
        else:
            return node
#236
"""236: find the LCA of two nodes in a binary tree.Note: two nodes exist in the tree,
and tree nodes are unique."""
def lowestca(self, root, p, q):
    if not root or root==p or root ==q:
        return root
    left = self.lowestca(root.left, p, q)
    right = self.lowestca(root.right, p, q)
    if left and right:
        return root
    return left or right
# iteration method
def LCA(root, p, q):
    stack = [root]
    parent = {root:None}
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q
#108
"""convert sorted array to a height banlanced BST"""
class Solution:
    def ArraytoBST(self, nums):
        if not nums:
            return None
        mid = len(nums) //2
        root = TreeNode(nums[mid])
        root.left = self.ArraytoBST(nums[:mid])
        root.right = self.ArraytoBST(nums[mid+1:])
        return root

#109
"""convert a sorted linked list to a height banlanced BST"""
class Solution:
    def listtoBST(self, head):
        if not head: return None
        slow, fast, pre = head, head, None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if pre:
            pre.next = None
        else:
            head = None
        root = TreeNode(slow.val)
        root.left = self.listtoBST(head)
        root.right = self.listtoBST(slow.next)
        return root

#653
"""653: given a BST, and target, return true if there exist two elements in BST such that their
sum is equal to target."""
def findTarget(root, k):
    if not root: return False
    self.result = []
    def inorder(node):
        if not node:
            return
        if node.left:
            inorder(node.left)
        self.result.append(node.val)
        if node.right:
            inorder(node.right)
    inorder(root)
    low, hi = 0, len(self.result)-1
    while low < hi:
        if self.result[low] + self.[h] == k:
            return True
        if self.result[low] +self.result[hi] <k:
            low += 1
        else:
            hi -= 1
    return False

# optimized recursion
def findTarget(root, k):
    s = set()
    def helper(root, k):
        if not root: return False
        if k - root.val in s:
            return True
        s.add(root.val)
        return helper(root.left,k) or helper(root.right, k)
    return helper(root, k)

#530
"""minimum abslute difference in BST, with non-negative values, find the minimum absolute difference between
values of any two nodes"""
class Solution:
    def getMinimumDiff(self, root):
        self.min = float('inf')
        self.pre = None

        def getmin(node):
            if not node: return
            if node.left:
                getmin(node.left)
            if self.pre:
                self.min = min(self.min, abs(node.val-self.pre.val))
            self.pre = node
            if node.right:
                getmin(node.right)
            return self.min
        return getmin(root)
        
