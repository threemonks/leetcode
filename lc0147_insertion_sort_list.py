"""
147. Insertion Sort List
Medium

769

619

Add to List

Share
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list


Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

"""


# Definition for singly-linked list.
from lc_tools import print_linked_list, deserialize_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
idea:
loop through input linked list, for each element, insert into new list in correct place (the new list is already in sorted order, so it takes O(N) to find the correct location to insert)
use two pointers, prev_node, next_node, to keep track of the node of interest, and its previous node, so that we can insert another node in front of next_node easily.
time O(N^2)
space O(1)
"""


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        pseudo_head = ListNode()
        curr = head
        while curr:
            # at each iteration, insert curr node from input list into new list at proper location
            nl_prev_node = pseudo_head
            nl_next_node = nl_prev_node.next
            while nl_next_node:
                if curr.val < nl_next_node.val:
                    break
                nl_prev_node = nl_next_node
                nl_next_node = nl_prev_node.next

            # store curr.next as we are inserting curr into new list
            next_curr = curr.next

            # insert curr into new list before nl_next_node
            curr.next = nl_next_node
            nl_prev_node.next = curr

            # moving onto next node in input list
            curr = next_curr

        return pseudo_head.next

def main():
    sol = Solution()
    head = deserialize_linked_list("4->2->1->3")
    assert print_linked_list(sol.insertionSortList(head)) == print_linked_list(deserialize_linked_list("1->2->3->4")), 'fails'

    head = deserialize_linked_list("-1->5->3->4->0")
    assert print_linked_list(sol.insertionSortList(head)) == print_linked_list(deserialize_linked_list("-1->0->3->4->5")), 'fails'

if __name__ == '__main__':
   main()