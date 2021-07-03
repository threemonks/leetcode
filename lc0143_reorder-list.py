"""
143. Reorder List
Medium

3416

154

Add to List

Share
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:

The number of nodes in the list is in the range [1, 5 * 10^4].
1 <= Node.val <= 1000
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
LinkedList

if length n is even, iterate to n//2 +1
 for n//2 + 2-th (index=n//2+1), build a linked list in reverse order
 then merge two lists

time: O(N)
space: O(1)

mistakes:
1. reverse linked list was done incorrectly
2. needs to handle single node specially
"""


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:  # single node, do nothing
            return

        p1, p2 = head, head

        while p1 and p2:
            p1 = p1.next
            if p2.next:
                p2 = p2.next.next
            else:
                break

        # now p1 points at index=n//2+1
        # break p1 from original linked list
        p = head
        prev = head
        while p != p1:
            prev = p
            p = p.next

        # now break prev->p into two lists
        prev.next = None

        # reverse p1 to end, call the new head head2
        head2 = p1
        while p1.next:
            t = p1.next
            p1.next = t.next  # extract p1.next
            t.next = head2  # insert p1 in front of head2
            head2 = t  # repoint head2 at p1

        # now merge two lists head and head2
        tail = ListNode()
        ans = tail
        while head or head2:
            if head:
                tail.next = head
                head = head.next
                tail = tail.next

            if head2:
                tail.next = head2
                head2 = head2.next
                tail = tail.next

        return ans

def main():
    sol = Solution()

    assert sol.reorderList(head = ListNode(1, next=ListNode(2, next=ListNode(3,next=ListNode(4))))), 'fails'

    assert sol.reorderList(head = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))), 'fails'

    assert sol.reorderList(head = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5, next=ListNode(6, next=ListNode(7)))))))), 'fails'



if __name__ == '__main__':
   main()