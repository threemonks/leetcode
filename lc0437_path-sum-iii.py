"""
437. Path Sum III
Medium

5063

323

Add to List

Share
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).



Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3


Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 10^9
-1000 <= targetSum <= 1000
"""
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
dfs traversal

along traversal, we record the current running path sum, and the count of each path sums that have occurred by now along this path

key point:
1. we need use hashmap to store how many times a given sum has appeared along this path (because negative number could result in some section of a path sum to zero, then a given sum could appear again later)
2. need to have this count of sum specific to each dfs traverse path, since same sum from different path cannot be used to sum to k
"""


class Solution:
    def pathSum(self, root: TreeNode, t: int) -> int:
        if not root:
            return 0
        ans = 0
        counts = defaultdict(int)

        def dfs(node, curr_sum):
            nonlocal ans, counts
            if not node:
                return
            # current prefix
            curr_sum += node.val
            # this path sum to t at this node
            if curr_sum == t:
                ans += 1

            # number of times curr_sum-t already occured
            # i.e., number of times path with sum t has occurred up to current node
            if curr_sum - t in counts:
                ans += counts[curr_sum - t]

            # add current sum to hashmap to use it during child nodes processing
            counts[curr_sum] += 1

            # explore left and right subtree
            if node.left:
                dfs(node.left, curr_sum)
            if node.right:
                dfs(node.right, curr_sum)

            # backtrack, remove current sum from hashmap
            # to avoid this count being used by other parallel subtree processing
            counts[curr_sum] -= 1

        dfs(root, 0)

        return ans



