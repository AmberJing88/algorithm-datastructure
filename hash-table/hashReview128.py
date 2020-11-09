#128
"""longest consecutive sequence:given an unsorted array of integers find the length of the
longest consecutive elements sequence."""
def longestconsecutive(nums):
    nums = set(nums)
    longest = 0
    for num in nums:
        if num -1 not in nums:
            current = num
            curr_cnt = 1
            while current +1 in nums:
                current += 1
                curr_cnt += 1
            longest = max(longest, curr_cnt)
    return longest

def longest(nums):
    nums = set(nums)
    longest = 0
    while nums:
        first = last +nums.pop()
        while first -1 in nums:
            first -= 1
            nums.remove(first)
        while last+1 in nums:
            last += 1
            nums.remove(last)
        longest = max(longest, last - first+1)
    return longest

#696
"""696: count binary substring, count the number of substring which contain the same number
of 0' and 1' and all 0 and 1 are grouped consecutively"""
def countbinary(s):
    res , pre, cur = 0,0,1
    n = len(s)
    for i in range(1,n):
        if s[i]==s[i-1]:
            cur += 1
        else:
            pre = cur
            cur = 1
        if pre >= cur:
            res += 1
    return res
