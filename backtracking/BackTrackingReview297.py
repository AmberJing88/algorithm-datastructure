#Back tracking
"""297; serialize and deserialize binary tree. serialize: convert a BT to a string,
deserialize: string to BT. Note donot use class member, global/static variables to store states."""
def serialize(root):
    vals = []
    def flat(node):
        if not node:
            vals.append('#')
        else:
            vals.append(str(node.val))
            flat(node.left)
            flat(node.right)
    flat(root)
    return ' '.join(vals)

def deserialize(data):
    vals = iter(data.split())
    def build():
        vals = next(vals)
        if val =='#':
            return None
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node
    return build()

# bfs method
def serialize(root):
    if not root: return ''
    q  = [root]
    res = []
    while q:
        node = q.pop(0)
        if node:
            q.append(node.left)
            q.append(node.right)
            res.append(str(node.val) if node else "#")
    return ' '.join(res)
def deserialize(data):
    if not node: return None
    nodes = data.split()
    root = TreeNode(int(nodes[0]))
    q, i = [root], 1
    while q:
        node = q.pop(0)
        if nodes[i] != '#':
            node.left = TreeNode(int(nodes[i]))
            q.append(node.left)
        i += 1
        if nodes[i] !='#':
            node.right = TreeNode(int(nodes[i]))
            q.append(node.right)
        i+= 1
    return root

#236
"""236; longest common ancestors of nodes p and q in a BT."""
def LCA(root,p,q):
    if not root or root==p or root==q:
        return root
    left = LCA(root.left,p,q)
    right = LCA(root.right,p,q)
    if left and right:
        return root
    return left or right

#77
"""77; combination, n, k return all possible combinations of k numbers out of 1,2,...n"""
def combination(n,k):
    res = []
    row = []
    if k==n or k==0:
        row = []
        for i in range(1,k+1):
            row.append(i)
        return [row]
    res += combination(n-1,k-1)
    return res
# python built in function
def combination(n,k):
    return itertools.combination(list(range(1,n+1)),k)

#226
"""226; invert a binary tree"""
def invertTree(root):
    if not root:
        return None
    temp = root.left
    root.left = invertTree(root.right)
    root.right = invertTree(temp)
    return root
# iteration
def inverttree(root):
    if not root: rturn None
    q = [root]
    while q:
        node = q.pop(0)
        if node:
            node.left,node.right = node.right,node.left
        q.append(node.left)
        q.append(node.right)
    return root

#98
"""98; validate a bst"""
def validbst(root):
    if not root: return True
    def bst(node,floor,ceiling):
        if not node: return True
        if node.val >=ceiling or node.val<= floor:
            return False
        if not bst(node.left,floor,node.val):
            return False
        if not bst(node.right,node.val, ceiling):
            return False
        return True
    return bst(root,float('-inf'),float('inf'))

#104
"""104; max depth of binary tree"""
def maxdepth(root):
    if not root: return 0
    left = maxdepth(root.left)
    right = maxdepth(root.right)
    return 1 + max(left,right)

#105
"""105; construct a binary tree, from its preorder and inorder traversal"""
def buildtree(preorder, inorder):
    if inorder:
        i = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[i])
        if i==0:
            root.left = None
        if i ==len(inorder)-1:
            root.right = None
        root.left = buildtree(preorder, inorder[:i])
        root.right = buildtree(preorder,inorder[i+1:])
        return root
# inorder recursion
def buildtree(preorder, inorder):
    def build(stop):
        if inorder and inorder[0] != stop:
            root = TreeNode(preorder.pop(0))
            root.left = build(root.val)
            inorder.pop(0)
            root.right = build(stop)
            return root
    return build(None)    
