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
        self.stack.push(top)
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

#20
"""20: implement the parentheses match with stack."""
def isMatch(s):
    if len(s) % 2 !=0:
        return False
    else:
        left = '({['
        right = ')}]'
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            elif c in right:
                if stack == []:
                    return False
                if right.index(c) != left.index(stack.pop()):
                    return False
    return len(stack)==0

#739
"""739: daily temperature: a list of temperature, return a list of days such that for
each day input, you need to tells how many days to wait until a warmer temperature."""
def dailytemprature(T):
    stack = []
    result = [0]* len(T)
    for i, t in enumerate(T):
        while stack and stack[-1][0] < t:
            _, prev_i = stack.pop()
            result[prev_i] = i - prev_i
        stack.append((t,i))
    return result

#503
"""503:next greater element : circular array, print the next preater number for every element.
if it doesn't exist, output -1 for this number."""
def nextGreaterElement(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(2*n):
        while stack and stack[-1][0] < nums[i%n]:
            _, prev = stack.pop()
            result[prev] = nums[i%n]
        stack.append((nums[i%n], i%n))
    return result

#556
"""556: next greater element: given a positive 32-bit integer n , find out the smallest
32-bit integer which has exactly the same digets existing in the integer n and is greater
in value than n. return -1 if not found."""
def nextGreater(n):
    l = [c for c in str(n)]
    i = len(l) -1
    while i >0 and l[i] <= l[i-1]:
        i -= 1
    if i ==0:
        return -1
    j = len(l) -1
    while j >= i and l[j] <= l[j-1]:
        j -= 1
    l[i-1], l[j] = l[j], l[i-1]
    result = l[:i]+sorted(l[i:])
    answer= int(''.join(result))
    return -1 if answer >= 2** 31 else answer
