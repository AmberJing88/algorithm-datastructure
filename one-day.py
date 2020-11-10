#295
from heapq import *
class MedianFinder:
    def __init__(self):
        self.heaps = [], []
    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, - heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) >len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0

#215
form heapq import *
def findkthlargest(nums):
    if not nums or not k or k >len(nums):
        return None
    h = []
    for i in range(k):
        heapq.heappush(h, nums[i])
    for num in nums[k:]:
        if num > h[0]:
            heapq.heappushpop(h, num)
    return h[0]
#703
class KthLargest:
    def __init__(self, k, nums):
        heapq.heapify(nums)
        while len(nums) >k:
            heapq.heappopo(nums)
        self.k = k
        self.nums = nums
    def add(self, val):
        if len(self.nums) == self.k and val<= self.nums[0]:
            return self.nums[0]
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

#9
def isPalindrome(x):
    if x <0:
        return False
    if x ==0: return True
    s = []
    while x >0:
        x, m = divmod(x, 10)
        s.append(m)
    left, right = 0, len(s)-1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right += 1
    return True
#1
def twosum(nums, target):
    d = {}
    for i, e in enumerate(nums):
        if target -e in d:
            return [ i, d[target-e]]
        d[e] = i
    return []
#217
def findduplicate(nums):
    d = {}
    for i, e in enumerate(nums):
        if e in d:
            return True
        d[e] = i
    return False
def find(nums);
return len(set(nums)) != len(nums)
#594
from collections import Counter
def findHs(nums):
    frequence = Counter(nums)
    max_f = 0
    for num, cnt in frequence.items():
        if num - 1 in frequence:
            max_f = max(max_f, cnt + frequence[num-1])
    return max_f
