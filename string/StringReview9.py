# string
"""9:palindrome number, determin an integer is a palindrome. Note: solve it without converting
the integer to a string."""
def isPalindrome(x):
    if x <0:
        return False
    if x ==0:
        return True
    s = []
    while x >0:
        x, m = divmod(x, 10)
        s.append(m)
    left, right = 0, len(s)-1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
