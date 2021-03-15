"""
19. Remove Nth Node From End of List
Medium
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Linked List - one pass - traverse n-th node from end

use one pointer curr to traverse from head to end (.next is null), when curr moves n steps, then start another pointer p1 at head, to move lock step with curr, when curr reaches end, p1 will be at n steps from end

We keep prev at each step we move p1, then we can remove p1 by
prev.next = p1.next

time O(N)

mistakes:
1 need to handle case when we are asked to remove head
"""


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head

        for i in range(1, n):
            curr = curr.next

        p1 = head
        prev = p1
        while curr.next:
            curr = curr.next
            prev = p1
            p1 = p1.next

        if p1 == head:
            # removing head
            return head.next
        else:
            # now remove p1
            prev.next = p1.next

            return head