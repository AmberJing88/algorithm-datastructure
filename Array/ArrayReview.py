# Array problems
"""leetcode 283: move all 0s in list to the end."""

def MoveZeros(nums):
    n = len(nums)
    A = [0] *n
    i =0
    for num in nums:
        if num != 0:
            A[i] = num
            i += 1
    return A

a = MoveZeros([1,0,2,0,3,5,0,6,0])
print(a)
