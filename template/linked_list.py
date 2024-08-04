"""
Linked List
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Two Pointers to detect cycle
"""
# Initialize slow & fast pointers
def has_cycle(head):
    fast, slow = head, head

    # Change this condition to fit specific problem.
    # Attention: remember to avoid null-pointer error
    while slow and fast and fast.next:
        slow = slow.next # move slow pointer one step each time
        fast = fast.next.next # move fast pointer two steps each time
        if slow == fast: # change this condition to fit specific problem
            return True

    return False # change return value to fit specific problem


"""
Revese Linked List

one by one insert into head of new list

step0      1,      2,     3,     4
        newhead
           cur

=>     newhead, newhead.next, cur = cur, newhead, cur.next

step1      1,      2,     3,     4
        newhead   cur

=>     newhead, newhead.next, cur = cur, newhead, cur.next

step2      2,      1,     3,     4   
        newhead          cur   

=>     newhead, newhead.next, cur = cur, newhead, cur.next

step3:     3,      2,     1,     4
        newhead                  cur     

"""

"""
Below reverse list is from leetcode explcore card at
https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1206/
"""
def reverseList(head: ListNode) -> ListNode:
    if not head:
        return head

    curhead = head # the current head
    while head.next:
        p = head.next
        head.next = p.next # extract p (head.next)
        p.next = curhead # insert p in front of curhead
        curhead = p # reset p as curhead

    return curhead

"""
use example
[1, 2, 3, 4, 5], left=2, right=4
before reverse
prev = 1, cur = 2, create node=prev=1 to hold node before reversed section
after reverse
[1], [4, 3, 2], [5]
prev=4 (we always keep it here as next insertion point), cur = 5 (next node to extract if we are going to)
to reconnect this reversed section back
node.next.next = cur # connects 2 to 5
node.next = prev # connects 1 to 4
"""
def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    # left, right are 1-indexed
    # create dummy head
    dummyhead = ListNode(next=head)
    prev = dummyhead
    cur = prev.next

    # get to node at index m
    i = 1
    while i < left:
        prev = cur
        cur = cur.next
        i += 1

    # now prev points at left-1, we need to record it so we can reconnect to reversed linked list section later
    node = prev
    while i <= right:
        nxt = cur.next # record cur node's next, so we can reconnect to it after we extract cur node
        cur.next = prev # extract cur node and insert in front of prev
        prev = cur # re-point prev at newly inserted node cur
        cur = nxt # reset cur to next node to be extracted
        i += 1

    # after reverse
    # prev points at head of reversed section, cur points at node after tail of reversed section
    # connect reversed section back to original linked list
    node.next.next = cur # node.next is the tail of reversed section, connect it to node after revered part
    node.next = prev # node is the one before reversed part, connect it to head of reversed part
"""
Reverse Linked List

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode()
        dummy.next = head

        prev = head
        cur = head.next
        while cur:
            # connect prev and cur.next
            temp = cur
            prev.next = cur.next
            cur = prev.next

            # insert cur between dummy and its next
            temp.next = dummy.next
            dummy.next = temp

        return dummy.next

"""
Remove node in Linked List
"""
## Linked List remove node

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        cur = head
        while cur:
            if cur.val == val:
                # remove cur
                prev.next = cur.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next

        return dummy.next