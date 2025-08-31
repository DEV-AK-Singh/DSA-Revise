base = __import__("01_base")

sll = base.SinglyLL()

sll.append(8)
sll.append(7)
sll.append(1)
sll.append(5)
sll.append(6)
sll.append(4)
sll.append(9)

# sll.traversal()
odd = sll.head
even_head = sll.head.next
even = sll.head.next
while even != None and even.next != None:
    o_temp = odd.next.next
    e_temp = even.next.next
    odd.next = o_temp
    even.next = e_temp
    odd = o_temp 
    even = e_temp
odd.next = even_head
sll.traversal()
