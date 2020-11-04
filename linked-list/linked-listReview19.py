# linked list
"""19:remove Nth mode from end of list"""
def removeNth(head, n):
    i = n
    prev = ListNode(None)
    prev.next = head
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
