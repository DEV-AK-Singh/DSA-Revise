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

# brute
# from collections import deque
# def right_view(root):
#     queue = deque([])
#     result = {}
#     ans = []
#     line = 0 
#     queue.append((root, 0))
#     while queue:
#         node, line = queue.popleft()  
#         result[line] = node.val
#         if node.left:
#             queue.append((node.left, line + 1)) 
#         if node.right:
#             queue.append((node.right, line + 1)) 
#     for values in sorted(result.items()):
#         ans.append(values[1])
#     return ans
# print(right_view(a))

# optimal
ans = []
def reverse_post_order(node, level, ans): 
    if node == None:
        return
    if len(ans) == level:
        ans.append(node.val)
    if node.right:
        reverse_post_order(node.right, level+1, ans)
    if node.left:
        reverse_post_order(node.left, level+1, ans)
reverse_post_order(a, 0, ans)
print(ans)