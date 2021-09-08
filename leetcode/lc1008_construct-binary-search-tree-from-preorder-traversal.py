"""
1008. Construct Binary Search Tree from Preorder Traversal
Medium

2380

52

Add to List

Share
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.



Example 1:


Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
Example 2:

Input: preorder = [1,3]
Output: [1,null,3]


Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
All the values of preorder are unique.
"""
import math
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Divide and Conquer

preorder[0] is root, firt value after preorder[0] is the right child

time: O(N^2)
space: O(log(N))
"""


class Solution0:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])

        idx = 1
        while idx < len(preorder) and preorder[idx] < preorder[0]:
            idx += 1
        # print('idx=%s' % idx)
        # now idx points at right child
        if idx <= len(preorder):
            if idx < len(preorder) and preorder[idx] < preorder[0]:  # idx is left child
                root.left = self.bstFromPreorder(preorder[1:])
            else:  # idx is right child
                root.left = self.bstFromPreorder(preorder[1:idx])
                root.right = self.bstFromPreorder(preorder[idx:])

        return root


"""
Sort

sorted array is BST inorder traverse, then we can construct from preorder and inorder
root element splits inorder list into left and right subtrees

preorder = [8,5,1,7,10,12]
inorder = [1,5,7,8,10,12]

time: O(Nlog(N))
space: O(log(N))
"""


class Solution1:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)

        # build inorder val to idx map
        in_idx_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(in_left, in_right, pre_left, pre_right):
            # left and right boundary of inorder/preorder
            nonlocal preorder, inorder
            if in_left > in_right:  # empty
                return None

            # root splits inorder list into left and right subtrees
            root_val = preorder[pre_left]
            in_root_idx = in_idx_map[root_val]
            left_len = in_root_idx - in_left
            root = TreeNode(root_val)
            if in_left == in_right:
                return root

            # recursive
            root.left = helper(in_left, in_root_idx - 1, pre_left + 1, pre_left + 1 + left_len - 1)
            root.right = helper(in_root_idx + 1, in_right, pre_left + 1 + left_len, pre_right)

            return root

        return helper(0, len(inorder) - 1, 0, len(preorder) - 1)


"""
Recursive

use a recursive helper function that processes remaining elements with an upper bound
left recursion (creates left subtree) will process elements < node.val
right recursion (creates right subtree) will process remaining elements < bound (elements < node.val have already been processed and removed from A)

time: O(N)
space: O(H)
"""
from collections import deque


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        A = deque(preorder)  # use deque allows remove A[0] at O(1) time

        def helper(A, bound):
            if not A or A[0] > bound:
                return None
            node = TreeNode(A.popleft())
            # print('node=%s A=%s' % (node.val, A))
            node.left = helper(A, node.val)
            node.right = helper(A, bound)

            return node

        return helper(A, math.inf)

def main():
    from leetcode.lc_tools import deserialize
    sol = Solution()
    assert sol.bstFromPreorder(preorder = [8,5,1,7,10,12]) == deserialize("[8,5,10,1,7,null,12]"), 'fails'

    assert sol.bstFromPreorder(preorder = [1,3]) == deserialize("[1,null,3]"), 'fails'

if __name__ == '__main__':
   main()