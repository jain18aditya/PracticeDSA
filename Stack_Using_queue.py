from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)
        for _ in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())

    def pop(self):
        return self.stack.popleft()

    def top(self):
        return self.stack[-1]

    def print_stack(self):
        print(self.stack)

s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.top())
print(s.pop())
print(s.print_stack())