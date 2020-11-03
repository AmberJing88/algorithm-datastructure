# linked list
""" 160 intersection of two linked list: find out the mode at which the intersection
of two single linked list."""
import gc
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def gerIntersection(self, headA, headB):
        if not headA or not headB:
            return None
        savedA, savedB = headA, headB
        while headA != headB:
            headA = savedB if not headA else headA.next
            headB = savedA if not headB else headB.next

        gc.collect()
        return headA

#206
"""206 reverse a single linked list"""
def reverselist(head):
    new = None
    while head:
        next = head.next
        head.next = new
        new = head
        head = next
    return new

# recursion method
def verselist2(head):
    if head ==None or head.next ==None:
        return head
    reverse = reverselist2(head.next)
    head.next.next = head
    head.next = None
    return reverse

#92
""" reverse linked list II: reverse a linked list from position m to n.Do it in one pass"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverselist(self,head, m, n):
        if n==m:
            return head
        psedo = ListNode(None)
        psedo.next = head
        node = psedo
        count = 1
        while count <m:
            node = node.next
            count += 1
        start = None
        next_reverse = node.next
        while count <= n:
            tail = next_reverse.next
            next_reverse.next = start
            start = next_reverse
            next_reverse = tail
            count += 1
        node.next.next = tail
        node.next = start
        return psedo.next

#21
"""21: merge two sorted list and return it as a new list."""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergelist(head1, head2):
        if head1 is None: return head2
        if head2 is None: return head1
        curr = dummy = ListNode(None)
        while head1 and head2:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        curr.next = head1 or head2
        return dummy.next

#88
"""merge two sorted array nums1, nums2 into nums1 as one sorted array"""
def merge(nums1, nums2, m, n):
    i, j, k = m-1, n-1, m+n-1
    while i >=0 and j>=0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    if j >=0:
        nums1[:j+1] = nums2[:j+1]
    return nums1

#83
"""83: remove duplicate from sorted list: given a sorted liked list, delete all duplicates such that
each element appear only once."""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicate(self, head):
        if head is None or head.next is None:
            return head
        prev = head
        while prev.next:
            if prev.val != prev.next.val:
                prev = prev.next
            else:
                prev.next = prev.next.next
        return head

    # recursion method
    def deleteduplicate(self, head):
        if head is None:
            return
        if head.next not None:
            if head.val == head.next.val:
                temp = head.next.next
                head.next = None
                head.next = temp
                self.deleteduplicate(head)
            else:
                self.deleteduplicate(head.next)
        return head
