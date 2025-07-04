from collections import deque

#  a queue, where the first element added is the first element retrieved (“first-in, first-out”)
queue = deque(["Eric", "John", "Michael"])
print(f"queue: {queue}")
queue.append("Terry")
queue.append("Graham")
print(f"queue after adding Terry, Graham: {queue}")
x = queue.popleft()
print(f"popp left element 1: {x}")
x = queue.popleft()
print(f"popp left element 2: {x}")
print(f"queue after pop: {queue}")