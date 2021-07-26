"""
328. Odd Even Linked List
Medium

3156

344

Add to List

Share
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.



Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]


Constraints:

The number of nodes in the linked list is in the range [0, 10^4].
-10^6 <= Node.val <= 10^6


Follow up: Could you solve it in O(1) space complexity and O(nodes) time complexity?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Linked List

Traverse linked list two step at a time, take out each even ones, insert at end, so all odd ones connect together, and even ones append at end one by one

1,     2,      3,     4,     5
ep     e                     tail

               ep
1,             3       4      5,     2

time O(N)
space O(1)

mistakes:
1. needs to stop swapping once reached original odd tail

"""


class Solution0:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        tail = head
        if not head.next:
            return head
        even_prev = head
        even = head.next

        while tail.next:
            tail = tail.next

        newtail = tail
        # print('even_prev=%s even=%s newtail=%s' % (even_prev.val, even.val, newtail.val))
        # print('head=%s' % head)
        while even and even.next and even_prev != tail and even != tail:
            # extract even, attach at newtail

            # save even_prev.next.next and even.next.next
            t_prev = even_prev.next.next
            t = even.next.next

            # connect even_prev.next to even_prev.next.next
            even_prev.next = even_prev.next.next
            # attach at newtail
            newtail.next = even
            newtail = newtail.next
            newtail.next = None  # break cycle

            # move even_prev and even forward 2 steps
            even_prev = t_prev
            even = t
            # print('even_prev=%s even=%s newtail=%s' % (even_prev.val, even.val if even else None, newtail.val))
            # print('head=%s' % head)

        # handle if even is pointing at tail
        if even == tail:
            if even_prev.next.next:
                even_prev.next = even_prev.next.next
            newtail.next = even
            newtail = newtail.next
            if newtail:
                newtail.next = None  # break cycle

        return head


"""
Linked List

Use two new dummy oddheads, evenheads to hold odd index nodes list and even index nodes list, 
use one pointer to iterate through origina linked list, toggle between odd and even, and decide which list (oddheads, evenheads) to append to

After original list is done iterating, attach evenlist to end of oddlist

mistakes:
1. use dummy oddhead, evenhead to hold odd index only nodes list, and even index only nodes list
2. when attaching even list to odd list, use evenhead.next
"""


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        oddhead = ListNode(0)
        oddlist = oddhead
        evenhead = ListNode(0)
        evenlist = evenhead

        isodd = True
        while head:
            if isodd:
                oddlist.next = head
                oddlist = oddlist.next
                head = head.next
            else:
                evenlist.next = head
                evenlist = evenlist.next
                head = head.next
            isodd = not isodd

        # now connect evenhead to end of oddlist
        oddlist.next = evenhead.next
        evenlist.next = None

        return oddhead.next


def main():
    sol = Solution()
    assert sol.oddEvenList(head = [1,2,3,4,5]) == [1,3,5,2,4], 'fails'

    assert sol.oddEvenList(head = [2,1,3,5,6,4,7]) == [2,3,6,7,1,5,4], 'fails'


if __name__ == '__main__':
   main()