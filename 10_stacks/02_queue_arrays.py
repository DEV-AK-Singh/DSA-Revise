class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0
    
    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0)
    
    def front(self):
        return self.__items[0]

    def rear(self):
        return self.__items[-1]
    
    def size(self):
        return len(self.__items)
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.front())
print(q.rear())
print(q.size())