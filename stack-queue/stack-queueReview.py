# stack
""" 232:implement the queue operations of a quue using stacks"""
class MyQueue:
    def __init__(self):
        self._size = 0
        self.stackin = []
        self.stackout = []
        self.top = None

    def push(self, x):
        if not self.stackin:
            self.top = x
        self.stackin.append(x)
        self._size += 1

    def pop(self):
        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.pop())
        self._size -= 1
        return self.stackout.pop()

    def peek(self):
        if self.empty():
            raise Empty('empty queue')
        if self.stackout:
            return self.stackout[-1]
        return self.top

    def empty(self):
        return self._size ==0
