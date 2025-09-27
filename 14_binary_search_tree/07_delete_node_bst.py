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

def delete_node(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)
    return root

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def pre_order(root):
    if root == None:
        return
    print(root.val, end=" ")
    pre_order(root.left)
    pre_order(root.right)

pre_order(a)    
print()
root = delete_node(a, 9)
pre_order(root)