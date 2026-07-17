from collections import deque

q=deque()

q.append(1)
print(q)

q.appendleft(10)
print(q)

q.extend([1,2,3])
print(q)


q.extendleft([10,20,30])
print(q)

q.pop()
print(q)

q.popleft()
print(q)