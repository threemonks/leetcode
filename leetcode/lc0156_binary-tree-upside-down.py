"""
156. Binary Tree Upside Down
Medium

10

27

Add to List

Share
Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.


The mentioned steps are done level by level, it is guaranteed that every node in the given tree has either 0 or 2 children.



Example 1:


Input: root = [1,2,3,4,5]
Output: [4,5,2,null,null,3,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree will be in the range [0, 10].
1 <= Node.val <= 10
Every right node in the tree has a sibling (a left node that shares the same parent).
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
DFS

recursively process as this:
set root as new right of root.left
set right as new left of root.left
set recursively processed left as the new root
return new root
"""
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root or not root.left:
            return root
        newroot = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right # attach root.right to the left of original left of root
        root.left.right = root # attach root to right of original left or root
        root.right = None
        root.left = None
        return newroot
