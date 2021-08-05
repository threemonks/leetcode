"""
272. Closest Binary Search Tree Value II
Hard

824

26

Add to List

Share
Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that are closest to the target.



Example 1:


Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
Example 2:

Input: root = [1], target = 0.000000, k = 1
Output: [1]


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 10^4.
0 <= Node.val <= 10^9
-10^9 <= target <= 10^9


Follow up: Assume that the BST is balanced. Could you solve it in less than O(n) runtime (where n = total nodes)?
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
inorder DFS + Heap

1. in order DFS to convert BST to sorted nums, as we traverse, push node into pq, and keep pq size at k, pop extra
2. return pq

time: O(Nlog(k)) - tree traverse, heapq time O(Nlog(k))
"""
import heapq


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        nums = []

        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            num = root.val
            heapq.heappush(nums, [-abs(num - target), num])
            if len(nums) > k:
                heapq.heappop(nums)
            root = root.right

        return [num[1] for num in nums]
