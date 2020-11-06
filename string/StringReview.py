# string
"""295: find the median from data stream, median is the middle value in an ordered integerlist.
if the size is even, there is no middle value, return the median of the middle values."""
from heapq import *
class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large,num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(larget) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0

#programming 3.1
"""programming 3.1: move the elements in a string for k steps."""
def movesteps(s,k):
    def reversestring(s):
        n = len(s)
        res = ''
        for i in range(n):
            res += s[n-1-i]
        return res

    sub1 = reversestring(s[:k+1])
    sub2 = reversestring(s[k+1:])
    return reversestring(sub1+sub2)

# programming 2.7
"""programming 2.7: compare to strings s1 and s2 check is s2 is substring of s1"""
def substring(s1, s2):
    if not s1:
        return False
    if not s2:
        return True
    s = s1 +s1
    i = 0
    while i < len(s) - len(s2):
        for i

    #return s2 in s
