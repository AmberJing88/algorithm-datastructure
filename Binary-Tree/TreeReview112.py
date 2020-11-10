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
                self.pathSum(root, sum)
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
