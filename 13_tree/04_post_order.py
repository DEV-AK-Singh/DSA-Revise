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



def post_order(root):
    if root == None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val, end=" ")

# pre_order(a)
# print()
# in_order(a)
# print()
# post_order(a)
# print()
 