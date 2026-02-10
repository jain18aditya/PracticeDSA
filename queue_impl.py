from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return "Queue is empty"

    def enqueue(self, val):
        self.queue.append(val)

    def front(self):
        return self.queue[0] if self.queue else "Queue is empty"

q = Queue()
q.enqueue("apple")
q.enqueue("banana")
print(q.front())
print(q.dequeue())
print(q.front())


