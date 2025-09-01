base = __import__("01_base")

dll = base.DoublyLL() 
 
dll.append(1)
dll.append(1)
dll.append(1)
dll.append(2)
dll.append(2)
dll.append(3) 
dll.append(4)  
dll.append(4)  
dll.traversal() 
  
curr = dll.head
while curr != None:
    prev = curr.prev
    next = curr.next   
    if prev != None and prev.val == curr.val:
        if next != None:
            prev.next = next
            next.prev = prev
        else:
            prev.next = None
    curr = next

dll.traversal() 
