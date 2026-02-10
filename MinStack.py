

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def push(self, val):
        self.stack.append(val)

        if self.min_stack and val > self.min_stack[-1]:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

    def top(self):
        return self.min_stack[-1]

    def get_min(self):
        return self.min_stack[-1]

m = MinStack()
m.push(4)
m.push(8)
m.push(2)
m.push(9)

print(m.get_min())

print(m.top())