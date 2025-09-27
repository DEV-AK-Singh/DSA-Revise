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

def insert_node_bst(node, key):
    temp = node
    if node == None:
        node = Node(key) 
    while temp != None:
        if temp.val > key:
            if temp.left == None:
                temp.left = Node(key)
                break
            temp = temp.left
        else:
            if temp.right == None:
                temp.right = Node(key)
                break
            temp = temp.right
    return node
 
def pre_order(root):
    if root == None:
        return
    print(root.val, end=" ")
    pre_order(root.left)
    pre_order(root.right)

insert_node_bst(a, 12)
pre_order(a)