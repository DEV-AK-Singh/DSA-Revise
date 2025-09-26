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

def bottom_view(root):
    queue = deque([])
    result = {}
    ans = []
    queue.append((root, 0)) 
    while queue:
        node, line = queue.popleft() 
        result[line] = node.val
        if node.left:
            queue.append((node.left, line-1)) 
        if node.right:
            queue.append((node.right, line+1))
    for val in sorted(result.items()):
        ans.append(val[1])
    return ans

print(bottom_view(a))