"""
Problem: Producer–Consumer Using Threads and Queue

Implement the Producer–Consumer problem using multithreading in Python.

- A Producer thread generates items and puts them into a shared bounded queue.
- A Consumer thread removes items from the queue and processes them.
- The queue has a fixed maximum capacity, so the Producer must wait if the queue is full.
- The Consumer must wait if the queue is empty.
- Synchronization must be handled safely using a thread-safe queue.

Requirements:
- Use Python's threading module.
- Use queue.Queue for thread-safe communication.
- Implement one producer and one consumer.
- Ensure all produced items are eventually consumed.
- Prevent race conditions and ensure proper thread coordination.

Example Behavior:
Produced 0
Consumed 0
Produced 1
Produced 2
Consumed 1
...

Approach:
- Use queue.Queue(maxsize=N) to create a bounded buffer.
- Producer uses q.put() to add items (blocks if queue is full).
- Consumer uses q.get() to retrieve items (blocks if queue is empty).
- Use q.task_done() to signal completion of processing.
- Use thread.join() to wait for threads to finish execution.
"""

import threading
import queue
import time

q = queue.Queue(maxsize=5)
def producer():
    for i in range(10):
        q.put(i)
        print(f"Produced {i}")
        time.sleep(1)

def consumer():
    for i in range(10):
        item = q.get()
        print(f"Consumed {item}")
        q.task_done()
        time.sleep(2)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()

