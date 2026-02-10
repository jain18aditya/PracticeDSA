
class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, val):
        self.stack1.append(val)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def print_queue(self):
        print(self.stack2)

q = QueueUsingStack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.front())
q.print_queue()
print(q.dequeue())
print(q.front())
q.print_queue()
