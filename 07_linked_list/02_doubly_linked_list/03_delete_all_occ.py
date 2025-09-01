base = __import__("01_base")

dll = base.DoublyLL() 
 
dll.append(2)
dll.append(2)
dll.append(10)
dll.append(8)
dll.append(4) 
dll.append(2) 
dll.append(5) 
dll.append(2) 
dll.traversal() 

curr = dll.head
target = 2

while curr != None:
    prev = curr.prev
    next = curr.next
    if curr.val == target:
        if prev == None:
            next.prev = prev
            dll.head = next
        elif next == None:
            prev.next = None
        else:
            prev.next = next
            next.prev = prev
    curr = curr.next

dll.traversal() 

        