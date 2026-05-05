# Queue implementation using deque

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    # Method to add element to queue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} enqueued into queue")

    # Method to safely dequeue element
    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty, cannot dequeue.")
            return None
        else:
            return self.queue.popleft()

    # Method to display queue
    def display(self):
        print("Queue:", list(self.queue))


# Driver code
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Dequeued element:", q.safe_dequeue())
print("Dequeued element:", q.safe_dequeue())
print("Dequeued element:", q.safe_dequeue())

# Attempt to dequeue from empty queue
print("Dequeued element:", q.safe_dequeue())