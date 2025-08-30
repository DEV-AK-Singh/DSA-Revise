from base import SinglyLL

sll = SinglyLL()

sll.append(6)
sll.append(8) 
sll.append(9)
sll.append(11) 
sll.append(22)  

temp = sll.head
prev = None

while temp != None:
    front = temp.next
    temp.next = prev
    prev = temp 
    temp = front

sll.head = prev

sll.traversal()