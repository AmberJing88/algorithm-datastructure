# Tree
"""112:path sum: given a vinary tree and a sum, determin if the tree has a root to leaf path
such that add up all the values along the path equals the given sum. """
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and root.val ==sum:
            return True
        lefty = self.hasPathSum(root.left, sum-root.val)
        righty = self.hasPathSum(root.right, sum- root.val)
        return lefty or righty
#445
"""445:add two II: given two non-empty linked lists representing two non-negative integers. the most
significant digit comes first and each of their nodes contain a single digit. add the two numbers
and return it as a linked list."""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwo(head1, head2):
        num1, num2 = 0, 0
        node = head1
        while node:
            num1 = num1 * 10 + node.val
            node = node.next
        node = head2
        while node:
            num2 = num2 * 10 + node.val
            node = node.next
        summ = num1 + num2
        if summ ==0:
            return ListNode(0)
        result = None
        while summ !=0:
            summ, digit = divmod(summ, 10)
            new_node = ListNode(digit)
            new_node.next = result
            result = new_node
        return result
#437
"""437: path sum III: given a tree, nodes with integer value, afind the number of path that
sum to a given value. the path no need to start or end at the root or a leaf, but it must go
downwards."""
class Solution:
    def pathSum(self, root, sum):
        if not root:
            return 0
        def pathSumStartnode(root, sum):
            if not root:
                return 0
            count = 0
            if root.val == sum:
                count += 1
            count += pathSumStartnode(root.left, sum-root.val) +
                pathSumStartnode(root.right, sum-root.val)
            return count
        result = self.pathSum(root.left, sum) +
                self.pathSum(root.right, sum) +
                pathSumStartnode(root, sum)
        return result

# dictionary method
from collections import defaultdict
def pathsum(root, sum):
    paths = defaultdict(int)
    paths[0] = 1

    def helper(node, partial):
        if not node: return 0
        partial += node.val
        count = paths[partial-sum]
        paths[partial] += 1
        count += helper(node.left, partial)
        count += helper(node.right, partial)
        paths[partial] -= 1
        return count
    return helper(root, 0)

#572
"""given two non empty binary trees s and t, check whether tree t has exactly the same structure and
node value with a subtree of s. a subtree of s is a tree consists of a node in s and all of its nodes
detendents. the tree s could also be considered as a subtree of tiself."""
class Solution:
    def isSubtree(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        return self.isSameTree(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        if s.val != t.val: return False
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
# iteration method
class Solution:
    def isSubtree(self, s, t):
        serial = []

        def serialize(node):
            if not node:
                serial.append("#")
                return
            serial.append(",")
            setial.append(str(node.val))
            serialize(node.left)
            serialize(node.right)

        serialize(s)
        s_serial = ''.join(serial)
        serial = []
        serialize(t)
        t_serial = ''.join(setial)
        return t_setial in s_setial

#101
"""101: symmetric tree: check whether a binary tree is a mirror of itself."""
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.Symmetric(root.left, root.right)

    def Symmetric(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        return self.Symmetric(node1.left, node2.right) and self.Symmetric(node1.right, node2.left)

    # method2 iteration
    from queue import Queue
    def isSymmetric(root):
        q = Queue()
        q.put(root)
        q.put(root)
        while not q.empty():
            t1, t2 = q.get(), q.get()
            if not t1 and t2:
                continue
            if not t1 or t2:
                return False
            if t1.val != t2.val:
                return False
            q.put(t1.left)
            q.put(t2.right)
            q.put(t1.right)
            q.put(t2.left)
        return True

#111
"""111: minimum depth of Binary tree, find the path root to nearest leaf number."""
class Solution:
    def minDepth(self, root):
        if not root: return 0
        lefty = self.minDepth(root.left)
        righty = self.minDepth(root.right)
        if not lefy or not righty:
            return 1 + lefy + righty
        return 1 + min(lefty, righty)

    # DFS method2
    def mindepth(self, root):
        if not root: return 0
        if None in [root.left, root.right]:
            return 1+ max(self.mindepth(root.left), self.mindepth(root.right))
        else:
            return 1 +min(self.mindepth(root.left), self.mindepth(root.right))

    #BFS method
    def mindepth(self, root):
        if not root: return 0
        queue  =[(root, 1)]
        while queue:
            node.level = queue.pop(0)
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))

#404
"""404:sum of left leaves: find the sum of left leaves in a binary tree."""
class Solution:
    def sumLeftLeaves(self, root):
        if not root: return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumLeftLeaves(root.right)
        return self.sumleftLeaves(root.left) + self.sumLeftLeaves(root.right)
