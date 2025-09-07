from collections import deque

items = deque([])
items.appendleft(1)
items.appendleft(2)
items.append(4)
items.append(3)
items.extend([2,3,4])
print(items)