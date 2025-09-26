class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(9)
b = Node(3)
c = Node(11)
d = Node(2)
e = Node(7)
f = Node(15)
g = Node(14)
h = Node(16)

a.left = b
a.right = c

b.left = d
b.right = e

c.right = f

f.left = g
f.right = h

#            a 9
#         /       \
#       b 3        c 11
#      /   \          \
#    d 2   e 7       f 15
#                    /   \
#                   g 14   h 16

def floor_bst(node, key):
    if not node:
        return None 
    floor = -1
    while node:   
        if node.val <= key:
            floor = node.val
            node = node.right
        else: 
            node = node.left
    return floor

print(floor_bst(a, 9))