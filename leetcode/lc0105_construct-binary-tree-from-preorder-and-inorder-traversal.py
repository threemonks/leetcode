"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List

"""
Tree Construct

key points:
1. preorder tells the start of root
2. root node index in inorder will split inorder list into left subtree and right subtree
3. so we keep build the tree recursively

mistakes:
1. left size could be 0
"""


class Solution0:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)

        def helper(prestart, instart, inend):
            # given start position in preorder, and start and end pos in inorder
            # build this tree/subtree
            nonlocal preorder, inorder
            if instart > inend:
                return None
            # build root
            root = TreeNode(preorder[prestart])
            # find root's index in inorder, and left subtree and right subtree size
            root_idx = 0
            for i in range(instart, inend + 1):
                if inorder[i] == preorder[prestart]:
                    root_idx = i
                    break
            left_size = root_idx - instart
            root.left = helper(prestart + 1, instart, root_idx - 1)
            root.right = helper(prestart + 1 + left_size, root_idx + 1, inend)

            return root

        return helper(0, 0, n - 1)


"""
Tree Construct

key points:
1. try to optimize from above by storing inorder value to index map into dictionary to avoid the loop lookup
"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        def helper(prestart, instart, inend):
            # given start position in preorder, and start and end pos in inorder
            # build this tree/subtree
            nonlocal preorder, inorder, inorder_map
            if instart > inend:
                return None
            # build root
            root = TreeNode(preorder[prestart])
            # find root's index in inorder, and left subtree and right subtree size
            root_idx = inorder_map[preorder[prestart]]
            left_size = root_idx - instart
            root.left = helper(prestart + 1, instart, root_idx - 1)
            root.right = helper(prestart + 1 + left_size, root_idx + 1, inend)

            return root

        return helper(0, 0, n - 1)

