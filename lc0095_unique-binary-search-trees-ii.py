"""
95. Unique Binary Search Trees II
Medium

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.


Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 8

"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def build_trees(nums):
            if not nums:
                return [None]
            elif len(nums) == 1:
                return [TreeNode(nums[0])]
            # build all valid bsts using nums, which is strictly increasing
            res = []
            for i in range(len(nums)):
                lefts = build_trees(nums[:i])
                rights = build_trees(nums[i + 1:])

                for l in lefts:
                    for r in rights:
                        res.append(TreeNode(nums[i], left=l, right=r))

            return res

        return build_trees(range(1, n + 1))