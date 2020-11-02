# Array problems
"""leetcode 697: degree of array the longest distance of the repeated numbers in an array,
find a subarry which has same degree with the original one"""
from collections import defaultdict
def findshortest(nums):
    count, position = defaultdict(int), {}
    for i num in enumerate(nums):
        count[num] += 1
        if num not in position:
            position[num] = [i, i]
        else:
            position[num][-1] = i

    max_count, max_nums = 0, []
    for num, cnt in count.item():
        if cnt == max_count:
            max_nums.append(num)
        elif cnt >max_count:
            max_count = cnt
            max_nums=[num]
    shortest = float("inf")
    for n in max_nums:
        shortest = min(shortes, position[n][-1]-position[n][0]+1)
    return shortest

# 442
"""leetcode 442: find all duplicate in an array, numbers are in range of (1, n) (size n), some
elements appear twice others appear once. """
def find_duplicate(nums):
    result = []
    for num in nums:
        num = abs(num)
        if nums[num-1] <0:
            result.append(num)
        else:
            nums[num-1] *= -1
    return result

#287
""" 287: find duplicate, array contains n+1 integers, (1, n),  one number duplicate.
do not modify the array Note:space O(1), time less than O(n^2)"""
def findduplicate(nums):
    slow = nums[0]
    fast = nums[slow]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    fast = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return fast

#667
""" given 2 integers n and k, you need to construct a list which contains n
different positive integers from 1~n and obeys the requirement.
the differential between two adjacent element has exactly k distinct integers"""

def beautiful_arrange(n, k):
    if k == 1:
        return list(range(1, n+1))
    result = [1]
    sign = 1
    for i in range(k, 0, -1):
        result.append(result[-1]+i*sign)
        sign *= -1
    return result +list(range(k+2, n+1))

def beautiful2(n, k):
    low, high = 1, k+1
    next_low = True
    result = []
    while low <= high:
        if next_low:
            result.append(low)
            low += 1
        else:
            result.append(high)
            high -= 1
        next_low = not next_low
    return result + list(range(k+2, n+1))

# 766
""" toeplitz matrix: if every diagonal from topleft to bottom right has the
same element, now given m*n matrix, return True if and only if the matrix is toeplitz"""
def isToeplitz(matrix):
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        curx = i
        cury = 0
        val = matrix[i][0]
        while curx <m and cury<n:
            if matrix[curx][cury] != val:
                return False
            curx += 1
            cury += 1
    for j in range(n):
        curx = 0
        cury = j
        val = matrix[0][j]
        while curx <m and cury < n:
            if matrix[curx][cury] != val:
                return False
            curx += 1
            cury += 1
    return True

# pythonic method
def isToeplitz(matrix):
    return all(matrix[r+1][1:] == matrix[r][:-1] for r in range(len(matrix)-1))

# 565
""" array nesting:a zzero-indexed array A with lenth n, contains all integers from 0 to
n-1, find out and return the longest length of set s, where s[i]= {A[i],A[A[i]],A[A[A[i]]],...}
suppose the first element in s starts with the selection of elemtnt A[i] of index i"""
def arrayNesting(nums):
    longest = 0
    for i, _ in enumerate(nums):
        term = nums[i]
        if term > -1:
            count = 0
            curr = term
            while nums[curr] > -1:
                count += 1
                term = nums[curr]
                nums[curr] = -1
                curr = term
            if longest < count:
                longest = count
    return longest

def arraynest(nums):
    visited = set()
    longest = 0
    for i, n in enumerate(nums):
        if n in visited:
            continue      # set terminal cache
        current = set()
        while n not in current:
            current.add(n)
            n = nums[n]
        longest = max(longest, len(current))
        if longest > len(nums) -i -1:
            break
        visited |= current
    return longest

# 769
""" 769: max chunks to make sorted, array is a permutation of [0, 1,..., array.length-1], split
the array into some numbers of chunks, and individually sort each chunk. after concatenating them,
the result equals sort most number of chunks we could have made."""
def maxChunks(arr):
    chunks = 0
    max_cnt = 0
    for i in range(len(arr)):
        max_cnt = max(max_cnt, arr[i])
        if i == max_cnt:
            chunks += 1
    return chunks
