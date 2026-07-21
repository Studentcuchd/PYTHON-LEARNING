class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if not self.items:
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if not self.items:
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())   # 30
print(stack.peek())  # 20