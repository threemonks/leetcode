"""
2. Add Two Numbers
Medium

https://leetcode.com/problems/add-two-numbers/
"""

"""
needs to carry some extra

mistakes:
1. l1 or l2 could be longer and needs to be handled after while loop finishes
2. carry could be non-zero, needs to be added after both l1 and l2 finishes
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def equal(self, other):
        while self and other and self.val == other.val:
            self = self.next
            other = other.next
        if not self and not other:
            return True
        return False

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        h1, h2 = l1, l2
        dummy_res = ListNode()
        res = dummy_res
        while l1 and l2:
            sums = l1.val + l2.val + carry
            val = sums % 10
            carry = sums // 10
            res.next = ListNode(val=val)
            l1 = l1.next
            l2 = l2.next
            res = res.next

        while l1:
            val = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            res.next = ListNode(val)
            l1 = l1.next
            res = res.next

        while l2:
            val = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            res.next = ListNode(val)
            l2 = l2.next
            res = res.next

        if carry:
            res.next = ListNode(carry)

        return dummy_res.next


def main():
    sol = Solution()
    assert sol.addTwoNumbers(l1 = ListNode(2, next=ListNode(4, next=ListNode(3))), l2 = ListNode(5, next=ListNode(6, next=ListNode(4)))).equal(ListNode(7, next=ListNode(0, next=ListNode(8)))), 'fails'

    assert sol.addTwoNumbers(l1 = ListNode(2, next=ListNode(4, next=ListNode(3))), l2 = ListNode(5, next=ListNode(6, next=ListNode(4)))).equal(ListNode(7, next=ListNode(0, next=ListNode(8)))), 'fails'


    assert sol.addTwoNumbers(l1=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9))))))),
                             l2=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9))))).equal(
           ListNode(8, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(0, next=ListNode(0, next=ListNode(0, next=ListNode(1))))))))), 'fails'

if __name__ == '__main__':
   main()