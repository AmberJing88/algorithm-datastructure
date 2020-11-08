# priority Queue
"""295: find median from data stream. find the middle value in an ordered integer list.
if the size of the list is even, so the median is the mean of the two middle value."""
from heapq import *
class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heapushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0

#215
"""215: find the kth largest element in an unsorted array"""
from heapq import *
def findkthlargest(nums):
    if not nums or not k or k >len(nums):
        return None
    h =[]
    for i in range(k):
        heapq.heappush(h, nums[i])
    for num in nums[k:]:
        if num > h[0]:
            heapq.heappushpop(h, num)
    return h[0]

#703
"""kth largest element in a stream, design a class to find the kth largest element in a stream"""
class KthLargest:
    def __init__(self, k, nums):
        heapq.heapify(nums)
        while len(nums)> k:
            heapq.heappop(nums)
        self.k = k
        self.nums = nums

    def add(self, val):
        if len(self.nums)== self.k and val <= self.nums[0]:
            reutrn self.nums[0]
        heapq.heappush(slef.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
