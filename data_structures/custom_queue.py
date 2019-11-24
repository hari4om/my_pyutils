from collections import deque

class my_queue:
    def __init__(self):
        self.item = deque()

    def enqueue(self, value):
        self.item.append(value)

    def dequeue(self):
        return self.item.popleft()

    def is_empty(self):
        return len(self.item) == 0

    def show(self):
        print(self.item)