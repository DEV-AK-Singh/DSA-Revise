class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
  
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

    def delete_at_last(self):
        temp = self.head
        if temp == None:
            return -1
        if temp.next == None:
            self.head = None
            return temp.val
        while temp.next != None:
            prev = temp
            temp = temp.next 
        temp_data = temp.val
        prev.next = temp.next
        temp.prev = prev
        return temp_data

    def traversal(self):
        temp = self.head
        while temp != None:
            print(temp.val, end=" <--> ")
            temp = temp.next
        print(f"{temp}\n")
 
class Stack:
    def __init__(self):
        self.stack = DoublyLL()

    def push(self, data):
        self.stack.append(data)

    def pop(self): 
        return self.stack.delete_at_last()
    
    def print_ll(self):
        return self.stack.traversal()

mystack = Stack()
mystack.push(1)
print(mystack.pop()) 
print(mystack.pop()) 
