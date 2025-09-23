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

def dfs(node):
    result = []
    queue = deque([])
    queue.append(node)
    while len(queue) != 0:
        e = queue.popleft()
        result.append(e.val)
        if e.left is not None:
            queue.append(e.left)
        if e.right is not None:
            queue.append(e.right)
    return result
     
print(dfs(a))