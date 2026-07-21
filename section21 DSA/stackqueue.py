# Queue Implementation
class Queue:
  def __init__(self):
    self.items=[]

  def push(self,e):
    self.items.append(e)

  def pop(self):
    head= self.items[0]
    self.items=self.items[1:]
    return head

q=Queue()
q.push(1)
q.push(2)
q.push(3)
print(q.pop())
print(q.pop())
print(q.pop())

#Stack Implementation
class Stack:
  def __init__(self):
    self.items=[]

  def push(self,e):
    self.items=[e]+ self.items

  def pop(self):
    return self.items.pop(0)

s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())