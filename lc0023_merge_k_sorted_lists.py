"""
23. Merge k Sorted Lists
Hard

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

"""
import heapq

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
use heapq minheap to keep head node of each list, pop the smallest node val and idx from queue, and store it into result, also retrieve its next in that Linked List and push into queue

Note: use dummy head for result Linked List so that we can keep pointer pointing to end of Linked List for adding next value, and still has pointer to head for return result
"""


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)

        q = [(l.val, idx) for idx, l in enumerate(lists) if l]

        heapq.heapify(q)

        head = cur = ListNode(None)
        while q:
            val, idx = heapq.heappop(q)
            cur.next = ListNode(val)
            cur = cur.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(q, (lists[idx].val, idx))

        return head.next
