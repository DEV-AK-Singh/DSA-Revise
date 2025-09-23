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

# def count_level(root):
#     count = 0
#     if not root:
#         return 0
#     q = deque()
#     q.append(root) 
#     while q: 
#         for _ in range(len(q)):
#             node = q.popleft() 
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#         count += 1
#     return count

# print(count_level(a))

def count_level(root):
    if root == None:
        return 0
    left_ht = count_level(root.left)
    right_ht = count_level(root.right)
    return 1 + max(left_ht, right_ht)

print(count_level(a))