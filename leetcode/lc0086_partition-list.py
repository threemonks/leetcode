"""
86. Partition List
Medium

4975

591

Add to List

Share
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]


Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200

"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution0:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head

        small_tail = dummy

        prev = dummy
        cur = head
        while cur and cur.val < x:
            # initally skip all val < x
            small_tail = cur
            prev = cur
            cur = cur.next

        while cur:
            if cur.val < x:
                temp = cur
                # remove cur
                prev.next = cur.next
                cur = prev.next

                # insert cur after small_tail
                temp.next = small_tail.next
                small_tail.next = temp
                small_tail = temp  # repoint small_tail
            else:
                # don't extract node, just move to next
                prev = cur
                cur = cur.next

            # print(f"{cur = } {small_tail = } {dummy = }")

        # print(f"{dummy = }")
        return dummy.next


"""

Linked List / Merge sort

"""


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        p1 = ListNode()
        p2 = ListNode()

        p1_dummy = p1

        p2_dummy = p2

        dummy = ListNode()
        dummy.next = head

        prev = dummy
        cur = head
        while cur:
            if cur.val < x:
                temp = cur
                prev.next = cur.next
                cur = cur.next

                temp.next = p1.next
                p1.next = temp
                p1 = p1.next

            else:
                temp = cur
                prev.next = cur.next
                cur = cur.next

                temp.next = p2.next
                p2.next = temp
                p2 = p2.next

        p1.next = p2_dummy.next
        p2.next = None  # to avoid cycle

        return p1_dummy.next


def main():
    sol = Solution()
    head = ListNode(1, next=ListNode(4, next=ListNode(3, next=ListNode(2, next=ListNode(5, next=ListNode(2))))))
    result = ListNode(1,next=ListNode(2, next=ListNode(2, next=ListNode(4, next=ListNode(3, next=ListNode(5))))))
    assert sol.partition(head = head, x = 3) == result, 'fails'


if __name__ == '__main__':
   main()