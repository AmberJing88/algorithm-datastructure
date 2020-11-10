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
        if len(large) > len(small):
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
    #return s2 in s
    i = 0
    while i < len(s) - len(s2):
        j = 0
        while j < len(s2):
            if s[i] !=s2[j]:
                i += 1
                j ==0
            else:
                i += 1
                j += 1
        if j == len(s2)-1:
            return True
    return False

#242
"""242: valid anagram, given two strings, the frequency of letters in two strings are same."""
from collections import Counter
def isAnagram(s, t):
    return Counter(s) == Counter(t)

from collections import defaultdict
def isangram(s, t):
    if len(s) != len(t):
        return False
    dict_s = defaultdict(int)
    dict_t = defaultdict(int)
    for l in s:
        if l not in t:
            return False
        dict_s[l] +=1
    for l in t:
        if l not in s:
            return False
        dict_t[l] +=1
    for l in dict_s:
        if dict_s[l] != dict_t[l]:
            return False
    return True

#409
"""409:longest parlindrome: given a string which consists of lower or uppercase letters, find the
length of the longest parlindrome that can be built those letters."""
from collections import defaultdict
def longestparlindrome(s):
    if not s or len(s)==0:
        return 0
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    res = 0
    for c in d:
        res += d[c] //2 *2
        if res %2 ==0 and d[c] %2 ==1:
            res += 1
    return res


#205
"""205: is isomorphic string: the characotors in s can be replaced to t, s and t are isomorphic."""
def isIsomorphic(s, t):
    d1, d2 = {}, {}
    for i, val in enumerate(s):
        d1[val] = d1.get(val, []) +[i]
    for i, val in enumerate(t):
        d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())

def isIsomorphic(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
def isIsomorphic(s, t):
    return [s.find(i) for i in s] == [t.find(i) for i in t]

#647
"""647: count all the parlindrome substring in a given string."""
#dp method
def countSub(s):
    n = len(s)
    dp = [[0] *n for _ in range(n)]
    res = 0
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            dp[i][j] = (s[i] ==s[j] and ((j-i+1)<3 or dp[i+1][j-1]))
            res += dp[i][j]
    return res

#manacher's algorithm is used to find longest palindromic substring in linear time complexity.
def countsubstring(s):
    def manachers(s):
        A = '@#' + '#'.join(s) + '#$'
        Z = [0] * len(A)
        center = right = 0
        for i in range(1, len(A)-1):
            if i < right:
                Z[i] = min(right-i, Z[2*center-i])
            while A[i+ Z[i]+1] == A[i-Z[i]-1]:
                Z[i] += 1
            if i + Z[i] > right:
                center, right = i, i+Z[i]
        return Z
    return sum((v+1)/2 for v in manachers(s))
