class Stack:
    def __init__(self):
        self.__stack = []
        self.size = 0

    def push(self, item):
        self.__stack.append(item)
        self.size += 1

    def pop(self):
        self.size -= 1
        last_item = self.__stack[-1]
        self.__stack.pop()
        return last_item
    
    def top(self):
        return self.__stack[-1]
    
stack = Stack()
stack.push("x")
stack.push("y")
stack.push("z")
print(stack.top())
stack.pop()
print(stack.top())  