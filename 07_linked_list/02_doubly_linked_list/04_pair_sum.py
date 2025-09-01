base = __import__("01_base")

dll = base.DoublyLL() 
 
dll.append(1)
# dll.append(2)
# dll.append(4)
dll.append(5)
dll.append(6) 
# dll.append(8) 
# dll.append(9)  
dll.traversal() 
 
start = dll.head
end = dll.head
target = 6

res = []

while end.next != None:
    end = end.next

while start.val < end.val:
    sum = start.val + end.val
    if sum == target:
        res.append([start.val, end.val])
        start = start.next
        end = end.prev
    elif sum < target:
        start = start.next
    else:
        end = end.prev

print(res)

        