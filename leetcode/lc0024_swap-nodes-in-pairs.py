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
use prev as pointer to previous node

"""


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        curr = head
        prev = curr
        count = 1
        while curr.next:
            prev = curr
            curr = curr.next
            count += 1
            if count % 2 == 0:
                # swap curr with prev
                prev.val, curr.val = curr.val, prev.val

        return head