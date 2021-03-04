"""
160. Intersection of Two Linked Lists
Easy

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.



Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.

"""

"""
LinkedList traverse

basic idea is to have pointer a, b scans list A and B in sync, when reaching end, pointer a will restart at headB, and pointer b will restart at headA, so when both pointer again meet, they will both have travelled (c3-a1+1)+c1-b1+1 = c1+c3+2-(a1+b1), thus equal and meet at intersection point, or they both be null if there's no intersection point

      p1               p2          p3
      a1 -> a2 -> a3 \
                       c1 -> c2 -> c3
b1 -> b1 -> b3 -> b3 /
p4

There are four cases of headA vs headB:

Case 1 (Have Intersection & Same Len): meet at intersection point
Case 2 (Have Intersection & Different Len): meet at intersection point
Case 3 (Have No Intersection & Same Len): both finish at end, has value null
Case 4 (Have No Intersection & Different Len): both finish at end, has value null

This works because pointer A walks through List A and List B (since once it hits null, it goes to List B's head).
Pointer B also walks through List B and List A.
Regardless of the length of the two lists, the sum of the lengths are the same (i.e. a+b = b+a), which means that the pointers sync up at the point of intersection.

If the lists never intersected, it's fine too, because they'll sync up at the end of each list, both of which are null, thus breaks out of the loop

time O(M+N)
space O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a

def main():

    sol = Solution()

    intersectNode = ListNode(8, next=ListNode(4, next=ListNode(5)))
    headA = ListNode(4, next=ListNode(1, next=intersectNode))
    headB = ListNode(5, next=ListNode(6, next=ListNode(1, next=intersectNode)))
    assert sol.getIntersectionNode(headA, headB) == intersectNode, 'fails'


if __name__ == '__main__':
   main()