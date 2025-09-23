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

max_dia = 0

def bt_dia(root):
    if root == None:
        return 0
    left_ht = bt_dia(root.left)
    right_ht = bt_dia(root.right) 
    global max_dia
    max_dia = max(max_dia, left_ht + right_ht) 
    return 1 + max(left_ht, right_ht)
     
print(bt_dia(a))
 