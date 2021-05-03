"""
687. Longest Univalue Path
Medium

2284

556

Add to List

Share
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [5,4,5,1,1,5]
Output: 2
Example 2:


Input: root = [1,4,5,4,4,5]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-1000 <= Node.val <= 1000
The depth of the tree will not exceed 1000.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Tree

recursively call on left and right, returns longest path in left subtree as left, and longest path in right subtree as right, if node.left.value matches root.val, left += 1, same with right, then update global ans as max(ans, left+right), and return max(left, right) for parent to extend to longer path 

mistakes:
1. needs to recursively go to child subtree even if value does not match because there could be larger value within the subtree
"""


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0

        def helper(node):
            nonlocal ans
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            left_max, right_max = 0, 0
            if node.left and node.val == node.left.val:
                left_max = 1 + left
            if node.right and node.val == node.right.val:
                right_max = 1 + right
            ans = max(ans, left_max + right_max)

            # propagate back to parent
            return max(left_max, right_max)

        helper(root)

        return ans

from lc_tools import deserialize
def main():
    sol = Solution()
    assert sol.longestUnivaluePath(root = deserialize("[5,4,5,1,1,5]")) == 2, 'fails'

    assert sol.longestUnivaluePath(root = deserialize("[1,4,5,4,4,5]")) == 2, 'fails'


if __name__ == '__main__':
   main()