"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Tree construct

similar to 105 construct tree from preorder+inorder
1. postorder tells root node, and inorder tells left and right subtree relaative to root

"""


class Solution0:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(inorder)

        def helper(poststart, instart, inend):
            # start/end index in inorder list, start index in postorder list
            nonlocal inorder, postorder
            if instart > inend:
                return None
            root = TreeNode(postorder[poststart])
            root_idx = 0
            for i in range(len(inorder)):
                if inorder[i] == postorder[poststart]:
                    root_idx = i
            right_size = inend - root_idx
            root.left = helper(poststart - 1 - right_size, instart, root_idx - 1)
            root.right = helper(poststart - 1, root_idx + 1, inend)

            return root

        return helper(n - 1, 0, n - 1)


"""
Tree construct

similar to 105 construct tree from preorder+inorder
1. postorder tells root node, and inorder tells left and right subtree relaative to root

Note: optimize root index lookup in inorder with hashmap
"""


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(inorder)
        inorder_map = dict()
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        def helper(poststart, instart, inend):
            # start/end index in inorder list, start index in postorder list
            nonlocal inorder, postorder, inorder_map
            if instart > inend:
                return None
            root = TreeNode(postorder[poststart])
            root_idx = inorder_map[postorder[poststart]]
            right_size = inend - root_idx
            root.left = helper(poststart - 1 - right_size, instart, root_idx - 1)
            root.right = helper(poststart - 1, root_idx + 1, inend)

            return root

        return helper(n - 1, 0, n - 1)

