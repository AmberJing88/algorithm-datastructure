# linked list
"""19:remove Nth mode from end of list"""
def removeNth(head, n):
    i = n
    #prev = ListNode(None)
    #prev.next = head
    slow = fast = head
    while i >0:
        fast = fast.next
        i -= 1
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

#24
"""24: swap ajacent nodes in a single linkedlist in pairs"""
def SwapPairs(head):
    if not head or not head.next:
        return head
    prev = dummy = ListNode(None)
    #prev.next = head
    while head and head.next:
        temp = head.next.next
        prev.next = head.next
        head.next.next = head
        prev = head
        head = temp
    prev.next = head
    return dummy.next

#25
"""25: reverse linked list nodes in k-group"""
def reverseKgroup(head, k):
    if k <2:
        return head
    for i in range(k):
        if not node:
            return head
        node = node.next
    prev = reverseKgroup(node,k)
    for _ in range(k):
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev

#445
"""445: add two numbers: two linkedlist prepresenting digits of two numbers, add the two
do not modify the original lists."""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def AddTwo(self, l1, l2):
        num1, num2 = 0, 0
        node = l1
        while node:
            num1 = num1 *10 + node.val
            node = node.next
        node = l2
        while node:
            num2 = num2 *10 + node.val
            node = node.next
        summ = num1 +num2
        if summ ==0:
            return ListNode(0)
        result = None
        while summ !=0:
            summ, digit = divmod(summ, 10)
            new_node = ListNode(digit)
            new_node.next = result
            result = new_node
        return result

#234
"""234: palindrome linked list a single linked list, determin if it is a palindrome
Note: need to solve in O(n) time and O(1) space."""
def Palindrome(head):
    slow, fast = head, head
    reverse = None
    while fast and fast.next:
        fast = fast.next.next # count to the middle
        temp = slow.next      # reverse first half of list
        slow.next = reverse
        reverse = slow
        slow = temp
    if fast:
        slow = slow.next  # when list has odd number nodes, skip the center node
    while slow:
        if reverse.val != slow.val:
            return False
        reverse = reverse.next
        slow = slow.next
    return True

#725
""" 725 split singly linked list in parts: length of each part as equal as possible."""
def splitListNode(root, k):
    n = 0
    node = root
    result = []
    while node:
        n += 1
        node = node.next
    length, extent = divmod(n, k)
    pre, curr = None, root
    for _ in range(k):
        length = size
        if extent >0:
            extent -= 1
            size += 1
        result.append(curr)
        for _ in range(length):
            pre, curr = curr, curr.next
        if pre:
            pre.next = None
    return result

#328
"""328: odd even linked list: single linked list group all nodes together, followed by even nodes.
Note: time O(n), space O(1)"""
def OddEven(head):
    if head is None or head.next is None:
        return head
    odd, even = head, head.next
    evenhead = even
    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next
    odd.next = evenhead
    return head
