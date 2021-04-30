"""
333. Largest BST Subtree
Medium

849

80

Add to List

Share
Given the root of a binary tree, find the largest subtree, which is also a Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.

A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties:

The left subtree values are less than the value of their parent (root) node's value.
The right subtree values are greater than the value of their parent (root) node's value.
Note: A subtree must include all of its descendants.

Follow up: Can you figure out ways to solve it with O(n) time complexity?



Example 1:



Input: root = [10,5,15,1,8,null,7]
Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one. The return value is the subtree's size, which is 3.
Example 2:

Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-10^4 <= Node.val <= 10^4
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math

"""
Tree

Recursively check left and right subtree, if both left and right are valid BST, and max(left sub tree )< root.val < min(right sub tree), then tree rooted at this node is also BST, with count = leftcount + rightcount + 1
"""

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 1

        def helper(node):
            # return value largest bst node counts, min node value, max node value
            nonlocal ans
            leftcount, leftmin, leftmax = 0, math.inf, -math.inf
            if node.left:
                leftcount, leftmin, leftmax = helper(node.left)
            rightcount, rightmin, rightmax = 0, math.inf, -math.inf
            if node.right:
                rightcount, rightmin, rightmax = helper(node.right)

            if (not node.left or (leftcount and leftmax < node.val)) and (
                    not node.right or (rightcount and rightmin > node.val)):
                ans = max(ans, (leftcount or 0) + (rightcount or 0) + 1)
                return (leftcount or 0) + (rightcount or 0) + 1, min(leftmin, node.val), max(rightmax, node.val)
            else:
                return 0, math.inf, -math.inf

        helper(root)
        return ans

from lc_tools import deserialize
def main():
    sol = Solution()
    assert sol.largestBSTSubtree(root = deserialize('[10,5,15,1,8,null,7]')) == 3, 'fails'

    assert sol.largestBSTSubtree(root = deserialize('[4,2,7,2,3,5,null,2,null,null,null,null,null,1]')) == 2, 'fails'


if __name__ == '__main__':
   main()
