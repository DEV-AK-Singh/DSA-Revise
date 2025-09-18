from collections import deque

class MyStack:

    def __init__(self):
        self.stack = deque([])

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()        

    def top(self) -> int:
        return self.stack[-1] if len(self.stack) > 0 else -1

    def empty(self) -> bool:
        return False if len(self.stack) > 0 else True