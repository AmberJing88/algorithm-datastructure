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

#225
"""225: implement stack operations using queues"""
from queue import Queue
class MyStack:
    def __init__(self):
        self.stack = Queue()
        self._size = 0

    def push(self, x):
        reverse = Queue()
        while not self.stack.empty():
            reverse.put(self.stack.get())
        self.stack.put(x)
        while not reverse.empty():
            self.stack.put(reverse.get())
        self._size += 1

    def pop(self):
        if not self.empty():
            self._size -= 1
            return self.stack.get()

    def top(self):
        top = self.stack.get()
        self.push(top)
        return top
    def empty(self):
        return self.stack.empty()

#155
"""155: min stack design a stach that supports push, pop, top and retrieving the minimum
element in constant time."""
class MinStack:
    def __init__(self):
        self.minstack = []
        self._size = 0

    def push(self, x):
        self.minstack.append(x)
        self._size += 1

    def pop(self):
        self.minstack.pop()
        self._size -= 1

    def top(self):
        if self._size ==0:
            return False
        else:
            return self.minstack[-1]

    def getMin(self):
        if self._size != 0:
            return min(self.minstack)
