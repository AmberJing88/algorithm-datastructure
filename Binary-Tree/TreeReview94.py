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
