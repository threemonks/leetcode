"""
445. Add Two Numbers II
Medium

2322

199

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.


Follow up: Could you solve it without reversing the input lists?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Linked List

reverse linked list, then add digit by digit, with some carry, store result into linked list
and reverse final result linked list reslist

mistakes:
1. l1 or l2 could have leftover
2. even if l1 and l2 does not have leftover, carry itself could have left over that needs to be handled after loop
"""


class Solution0:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def reverse(head):
            newhead = None
            cur = head
            while cur:
                t = cur.next
                cur.next = newhead
                newhead = cur
                cur = t
            return newhead

        l1 = reverse(l1)
        l2 = reverse(l2)
        carry = 0
        dummyhead = ListNode()
        reslist = dummyhead
        while l1 and l2:
            val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            reslist.next = ListNode(val)
            reslist = reslist.next
            l1 = l1.next
            l2 = l2.next

        # add whichever one left over (l1 or l2) into reslist
        if l1:
            while l1:
                val = (l1.val + carry) % 10
                carry = (l1.val + carry) // 10
                reslist.next = ListNode(val)
                reslist = reslist.next
                l1 = l1.next

        if l2:
            while l2:
                val = (l2.val + carry) % 10
                carry = (l2.val + carry) // 10
                reslist.next = ListNode(val)
                reslist = reslist.next
                l2 = l2.next

        if carry:
            reslist.next = ListNode(carry)

        return reverse(dummyhead.next)


"""
Linked List

solving without reversing the linked list - use stack

"""


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        res = []
        while stack1 or stack2 or carry != 0:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            sums = v1 + v2 + carry
            val = sums % 10
            carry = sums // 10
            res.append(val)

        print(res)
        # build output linked list
        dummyhead = ListNode()
        cur = dummyhead
        while res:
            cur.next = ListNode(res.pop())
            cur = cur.next

        return dummyhead.next
