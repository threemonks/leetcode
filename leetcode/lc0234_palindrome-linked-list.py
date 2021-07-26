"""
234. Palindrome Linked List
Easy

5349

440

Add to List

Share
Given the head of a singly linked list, return true if it is a palindrome.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Two Pointers 快慢指针

fast  two nodes at a time
slow one node at a time, and push slow element into stack
when fast gets to end, slow is in middle
if odd number of elements, slow move one more step (to skip the odd number element in middle), then break
then slow continue while stack is not empty, each time compare slow pointer value with stack end, and pop stack after it. If not match, return False

finally return True

time O(N)
space O(N)

mistakes:
1. needs to handle odd number of elements
"""


class Solution0:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            stack.append(slow.val)
            slow = slow.next

        if fast:  # odd number of nodes
            slow = slow.next

        # now fast is at end, slow is in middle
        # now fast repoint to head, and run as slow, and compare it with stack
        # print(stack)
        while stack:
            if slow.val != stack[-1]:
                # print('slow.val=%s stack[-1]=%s' % (slow.val, stack[-1]))
                return False
            stack.pop()
            slow = slow.next

        return True


"""
Two Pointers

To achieve O(N) time and O(1) space, we can reverse first half while traversing fast and slow pointers
after fast reaches end, first half is already reversed, then we can just compare first half with second half.

"""


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # rev is the head of left half
        # while traversing, slow pointer, we also reverse the left half of the linked list
        rev = None
        fast, slow = head, head
        while fast and fast.next:
            # fast moves 2 step at a time, will be passing end if length is even
            # fast will be at last element if length is odd
            fast = fast.next.next

            # insert node pointed by slow to front of rev (head of reversed first half)
            # then move slow pointer to slow.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:  # odd number of nodes
            slow = slow.next

        # now fast is at end, slow is in middle
        # we re-position fast pointer to head, slow points at node next to middle
        # we now move fast and slow both at slow pace, and compare each value, if any mismatch, not palindrome
        fast = rev
        while slow and slow.val == fast.val:
            slow = slow.next
            fast = fast.next

        # if fast is None, that means we have palindrome
        return not fast


def main():
    sol = Solution()
    assert sol.isPalindrome(head = [1,2,2,1]) == True, 'fails'

    assert sol.isPalindrome(head = [1,2]) == False, 'fails'


if __name__ == '__main__':
   main()