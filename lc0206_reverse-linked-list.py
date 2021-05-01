"""
206. Reverse Linked List
Easy

6859

129

Add to List

Share
Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
create a dummy new head, append each node to end of new head
"""


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        newhead = None
        cur = head
        while cur:
            # remove cur from its current location
            t = cur.next

            # insert cur before newhead
            cur.next = newhead
            newhead = cur  # set new newhead

            cur = t

        return newhead