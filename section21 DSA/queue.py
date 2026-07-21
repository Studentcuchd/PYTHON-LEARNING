from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if not self.items:
            return "Queue is empty"
        return self.items.popleft()

    def peek(self):
        if not self.items:
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


queue = Queue()

queue.push(10)
queue.push(20)
queue.push(30)

print(queue.pop())   # 10
print(queue.peek())  # 20