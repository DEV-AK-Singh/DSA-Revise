class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node3 # cycle
# node9.next = None # no-cycle
 
# # brute 
# s1 = set()
# temp = node1
# cycle = False
# while temp != None:
#     if temp not in s1:
#         s1.add(temp)
#     else:
#         cycle = True
#         break
#     temp = temp.next
# print(cycle)

# # optimal
# slow = node1
# fast = node1
# cycle = False
# while fast != None and fast.next != None:
#     slow = slow.next
#     fast = fast.next.next
#     if slow == fast:
#         cycle = True
#         break 
# print(cycle)