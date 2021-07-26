"""
1721. Swapping Nodes in a Linked List
Medium

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Linked List - one pass

have two pointers, p1, and p2, pointer curr start from head, move k-1 steps to get to p1, at this time, start pointer p2 at head, on each step, move curr one step forward, as well as p2 one step forward, when p1 reaches end (curr.next is null), we know p3 is at k steps from end. Then we can swap p1 and p2.

time O(N)
"""

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n = 1
        curr = head
        while curr.next:
            curr = curr.next
            n += 1
            if n == k:
                break

        p1 = curr
        p2 = head
        while curr.next:
            curr = curr.next
            p2 = p2.next

        # now p1 points at k-step from head, and p2 points at k step from end
        p1.val, p2.val = p2.val, p1.val

        return head
