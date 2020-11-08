# Hash table
"""1. given an array of integers return indices of the two numbers such that they add up to
specific target."""
def twosum(nums, target):
    d = {}
    for i, e in enumerate(nums):
        if target -e in d:
            return[i, d[target-e]]
        d[e] = i
    return []

#217
"""217: contain duplicate: find out if an array contains any duplicate. return True if has.
False if elements are distinct."""
def findDuplicate(nums):
    d = {}
    for i, e in enumerate(nums):
        if e in d:
            return True
        d[e] = i
    return False
def findduplicate(nums):
    return len(set(nums)) != len(nums)

#594
"""594: define a harmonious array the difference between the maximum value and minimum value is 1."""
from collections import Counter
def findHs(nums):
    frequence = Counter(nums)
    max_f = 0
    for num, cnt in frequence.items():
        if num-1 in frequence:
            max_f = max(max_f, cnt+frequece[num-1])
    return max_f
