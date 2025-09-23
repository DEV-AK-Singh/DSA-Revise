class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f

f.left = g
f.right = h

#        a
#       / \
#      b   c
#     / \   /
#    d   e  f
#          / \
#         g   h
 
from collections import deque

# in [3,9,20,null,null,15,7]
# out [[3],[9,20],[15,7]]

def level_order(root):
    if not root:
        return []
    q = deque()
    q.append(root)
    res = []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res