base = __import__("01_base")

dll = base.DoublyLL() 
 
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5) 
# dll.traversal()

temp = dll.head 
prev = None 
while temp != None:
    next = temp.next
    temp.next = prev
    temp.prev = next
    prev = temp
    temp = next 
dll.head = prev 

dll.traversal()