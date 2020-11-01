# Array problems
"""leetcode 485: max consecutive ones, find the longest consecutive 1s in given array"""
def MaxConseOnes(nums):
    maxx, curr = 0, 0
    for n in nums:
        if n == 1:
            curr += 1
            if curr > maxx:
                maxx = curr
        else:
            curr = 0
    return maxx

def ConseMax(nums):
    maxn = []
    curr =0
    for i in nums:
        if i == 1:
            curr += 1
        else:
            maxn.append(curr)
    return max(maxn)
