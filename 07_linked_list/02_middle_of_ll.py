base = __import__("01_base")

sll = base.SinglyLL()

sll.append(6)
sll.append(8) 
sll.append(9)
sll.append(11) 
sll.append(22)  

slow = sll.head
fast = sll.head

while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

print(slow.val)