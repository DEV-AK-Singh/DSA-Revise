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

max_height_diff = 0

def balanced_bt(root):
    if root == None:
        return 0
    left_ht = balanced_bt(root.left)
    right_ht = balanced_bt(root.right) 
    global max_height_diff
    max_height_diff = max(max_height_diff, abs(left_ht - right_ht)) 
    return 1 + max(left_ht, right_ht)
     
balanced_bt(a)

print(True if max_height_diff <= 1 else False)