class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# temp = node1
# while temp != None:
#     print(temp.val)
#     temp = temp.next

class SinglyLL:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def append(self, val):
        new_node = Node(val)
        self.length += 1
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node

    def traversal(self):
        if self.head == None:
            print("List is empty")
        else:
            curr = self.head
            while curr != None:
                print(curr.val)
                curr = curr.next
        
    def insert(self, position, value):
        if position > self.length:
            print("Insertion at giving position not possible")
        else:
            new_node = Node(value)
            if position == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                curr = self.head
                while position > 0:
                    prev = curr
                    curr = curr.next
                    position -= 1  
                prev.next = new_node
                new_node.next = curr
    
    def delete(self, value):
        temp = self.head
        if temp.val == value:
            self.head = temp.next
            del temp
        else:
            curr = self.head
            while curr.val != value: 
                prev = curr
                curr = curr.next
            prev.next = curr.next
            del curr

sll = SinglyLL() 
sll.append(1)
sll.append(3) 
sll.append(4)
sll.append(5)
sll.insert(4, 10)
sll.delete(4)
sll.traversal()