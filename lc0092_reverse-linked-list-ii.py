"""
92. Reverse Linked List II
Medium

3584

188

Add to List

Share
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Linked List

traverse linked list, count number of nodes traversed, when we reached i-th node, start inserting node at location left, until we visited right-th node

[1,2,3,4,5], left=2, right=4

before reverse, prev=1, cur=2
record prev=left-1 as node before reverse
node = prev
while i <= right:
    nxt = cur.next # store nxt so that after extraction of cur, we can connect to this
    cur.next = prev # insert cur in front of prev
    prev = nxt # re-position prev to newly inserted node cur, prepare for next insert
    cur = nxt # reset cur to next node to be extracted    
    i += 1

[1] [4, 3, 2] [5]
after reverse, prev=4 at location 2, cur=5
to link this reversed section back to original linked list
node.next.next = cur # connect 2 to 5
node.next = prev # connect 1 to 4

"""


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummyhead = ListNode(next=head)
        prev = dummyhead
        cur = prev.next

        i = 1
        while i < left:
            prev = cur
            cur = cur.next
            # print('i=%s head=%s prev=%s cur=%s' % (i, head, prev, cur))
            i += 1

        # now cur in at node left
        node = prev  # the noe before left, hold it to reconnect to reversed linked list section
        while i <= right:
            # print('i=%s prev=%s cur=%s' % (i, prev.val, cur.val))

            # store cur.next so that we can extract cur
            nxt = cur.next

            # extract cur and insert it in front of prev
            cur.next = prev
            # re-point prev to newly inserted node to prepare for next insert
            prev = cur

            # re-point cur to the original cur's next
            cur = nxt
            # print('i=%s head=%s prev=%s cur=%s' % (i, head, prev, cur))
            i += 1

        # now reconnect reversed linked list section back into original linked list
        node.next.next = cur
        node.next = prev

        return dummyhead.next