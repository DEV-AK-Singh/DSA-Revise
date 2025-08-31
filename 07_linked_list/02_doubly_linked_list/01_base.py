class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)

# n1.next = n2
# n2.prev = n1
# n2.next = n3
# n3.prev = n2

class DoublyLL:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert_at(self, pos, val):
        temp = self.head
        new_node = Node(val) 
        while pos > 0:
            prev = temp
            temp = temp.next
            pos -= 1
        prev.next = new_node
        new_node.prev = prev
        new_node.next = temp
        temp.prev = new_node

    def delete_at(self, pos):
        temp = self.head
        if pos == 0:
            self.head = temp.next
            self.head.prev = None  
        else:
            while pos > 0 and temp.next != None:
                prev = temp
                temp = temp.next
                pos -= 1
            prev.next = temp.next
            temp.prev = prev

    def traversal(self):
        temp = self.head
        while temp != None:
            print(temp.val, end=" <--> ")
            temp = temp.next
        print(f"{temp}\n")

dll = DoublyLL()
dll.insert_at_head(2)
dll.insert_at_head(3)
dll.insert_at_head(4)
dll.insert_at_head(5)
dll.append(6)
dll.append(9)
dll.append(8)
dll.insert_at(3,11)
# dll.traversal()
# dll.delete_at(7) 
# dll.traversal()