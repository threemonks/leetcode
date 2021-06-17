"""
1019. Next Greater Node In Linked List
Medium

1481

77

Add to List

Share
We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.



Example 1:

Input: [2,1,5]
Output: [5,5,0]
Example 2:

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
Example 3:

Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]


Note:

1 <= node.val <= 10^9 for each node in the linked list.
The given list has length in the range [0, 10000].
"""
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Stack - Monotonic Stack

Use monotonic decreasing stack to hold node value with its index in linked list
each larger linkedlist node value would pop smaller node value at top of stack, and update its next larger value with current linkedlist node value

Store the next larger into dict with index as key, final result is output of dict value sorted by key

time O(N)
"""
from collections import defaultdict

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:

        # stock holds node val with index with monotonic decreasing value,
        # so any new node_j with larger value would pop and update the next larger of all smaller nodes in the stack
        stack = []
        ans = defaultdict(int)
        pos = 0
        while head:
            while stack and head.val > stack[-1][0]:
                _, idx = stack.pop()
                ans[idx] = head.val
            stack.append([head.val, pos])
            pos += 1
            head = head.next

        while stack:
            _, idx = stack.pop()
            ans[idx] = 0

        return [ans[k] for k in sorted(ans.keys())]
