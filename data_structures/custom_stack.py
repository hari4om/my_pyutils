from collections import deque

class my_stack:
    def __init__(self):
        self.item = deque()

    def push(self, value):
        self.item.append(value)

    def pop(self):
        return self.item.pop()

    def is_empty(self):
        return len(self.item) == 0

    def show(self):
        print(self.item)