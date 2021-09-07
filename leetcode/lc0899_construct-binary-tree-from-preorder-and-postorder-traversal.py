"""
889. Construct Binary Tree from Preorder and Postorder Traversal
Medium

1491

70

Add to List

Share
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.



Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]


Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.

"""
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Divide and Conquer

preorder tells root and left child
postorder tells root and right child

use a hashmap to store value to indices for preorder, with postorder gives right child, find its location in preorder array, then we know exactly the start and end of left child subarray and right child subarray within preorder

time O(N) - build hashmap
     divide & conquer part is O(log(N))
"""


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        preorder_map = dict()
        for i, num in enumerate(preorder):
            preorder_map[num] = i

        def build(pre_start, pre_end, post_start, post_end):
            nonlocal preorder_map
            if pre_start == pre_end:  # single value
                return TreeNode(preorder[pre_start])
            elif pre_end < pre_start or post_end < post_start:  # empty range
                return None

            root = TreeNode(preorder[pre_start])

            left_pre_start = pre_start + 1
            right_pre_start = preorder_map[postorder[post_end - 1]]
            left_len = right_pre_start - left_pre_start
            right_len = pre_end - right_pre_start + 1

            left = build(left_pre_start, right_pre_start - 1, post_start, post_start + left_len - 1)
            right = build(right_pre_start, pre_end, post_start + left_len, post_start + left_len + right_len - 1)
            root.left = left
            root.right = right

            return root

        pre_start, pre_end = 0, len(preorder) - 1
        post_start, post_end = 0, len(postorder) - 1

        node = build(pre_start, pre_end, post_start, post_end)

        return node
