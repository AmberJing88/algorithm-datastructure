# Tree
"""501:Given BST with duplicates nodes, find all the nodes that most frequcy occured element."""
def findMode(root):
    d = {}
    maxcount = 0
    result = []
    def inorder(node):
        if not node: return None
        if node.left: inorder(node.left)
        if node.val not in d:
            d[node.val] =1
        else:
            d[node.val] += 1
        if node.right: inorder(node.right)
    inorder(root)
    for v in d:
        if d[v] > maxcount:
            maxcount = d[v]
        for v in d:
            if d[v] ==maxcount:
                result.append(v)
    return result
# iteration
def findMode(root):
    if not root: return None
    res, s, d = [],[],{}
    p = root
    max = 0
    while s or p:
        while p:
            s.append(p)
            p = p.left
        if p not in d:
            d[p] = 1
        else:
            d[p] += 1
        max = max(max, d[p])
        p = p.right
    for v in d:
        if d[v] ==max:
            result.append(v)
    return reuslt
# follow up
def findMode(root):
    if not root: return []
    result, s = [], []
    p, pre = root, None
    max, cnt = 0, 0
    while s or p:
        while p:
            s.append(p)
            p = p.left
        p = s.pop()
        if pre:
            cnt = cnt +1 if p.val==pre.val else 1
        if cnt >= max:
            if cnt>max:
                result =[]
            result.append(p.val)
            max = cnt
        pre = p
        p = root.righty
    return result

#208
"""208:implement a trie with insert, search, and startwith. prefix tree"""
class MyTrie:
    def __init__(self):
        self.trie = {}
    def insert(self, word):
        '''form as {a:{b:{c:d}}}'''
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = "#"

    def search(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False

    def startwith(self, prefix):
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True
#677
"""677: implement a mapsum class, with insert add sum method. insert key:value pairs, if the key
already existed then override original value with the new one"""
class TrieNode:
    __slots__ = 'children','score'
    def __init__(self):
        self.children = {}
        self.score = 0
class MapSum:
    def __init__(self):
        self.map = {}
        self.root = TrieNode()
        
