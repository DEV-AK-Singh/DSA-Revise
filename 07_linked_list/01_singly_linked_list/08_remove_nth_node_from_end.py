base = __import__("01_base")

sll = base.SinglyLL()

sll.append(8)
sll.append(7)
sll.append(1)
sll.append(5)
sll.append(6)
sll.append(4)
sll.append(9)

node = 7

slow = sll.head
fast = sll.head

while node > 0 and fast != None:
    fast = fast.next
    node -= 1

if fast == None:
    sll.head = sll.head.next
    sll.traversal()
    exit()

while fast.next != None:
    fast = fast.next
    slow = slow.next

slow.next = slow.next.next

sll.traversal()

