"""
250. Count Univalue Subtrees
Medium

720

195

Add to List

Share
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.



Example 1:


Input: root = [5,1,5,5,5,null,5]
Output: 4
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6


Constraints:

The numbrt of the node in the tree will be in the range [0, 1000].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
DFS

Post traverse tree, process child and pass result (count of univalue tree, and boolean whether tree ends at current node) back to parent node, all the way to root.

time O(N)
space O(H) - call stack
"""


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0, True
            left_count, right_count = 0, 0
            left, right, isunival = False, False, False
            if node.left:
                left_count, left = helper(node.left)
            if node.right:
                right_count, right = helper(node.right)
            if not node.left and not node.right:
                return 1, True  # one uni-value tree, and ending at root
            res = left_count + right_count
            if (not node.left or (left and node.left.val == node.val)) and (
                    not node.right or (right and node.right.val == node.val)):
                res += 1
                isunival = True
            return res, isunival

        res, isunival = helper(root)

        return res


def main():
    from leetcode.lc_tools import deserialize
    sol = Solution()
    assert sol.countUnivalSubtrees(root = deserialize('[5,1,5,5,5,null,5]')) == 4, 'fails'

    assert sol.countUnivalSubtrees(root = deserialize('[null]')) == 0, 'fails'

    assert sol.countUnivalSubtrees(root = deserialize('[5,5,5,5,5,null,5]')) == 6, 'fails'


if __name__ == '__main__':
   main()