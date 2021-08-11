"""
1382. Balance a Binary Search Tree
Medium

1001

37

Add to List

Share
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.



Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]


Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 10^5
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
DFS / BST Divide and Conquer

convert BST to an sorted array, then convert sorted array back into BST with mid point as root.

"""


class Solution:
    def nums2BST(self, nums) -> TreeNode:
        # given sorted array nums, recursively convert it to BST
        if not nums:
            return None
        n = len(nums)
        pivot = n // 2
        root = TreeNode(val=nums[pivot])
        root.left = self.nums2BST(nums[:pivot])
        root.right = self.nums2BST(nums[pivot + 1:])
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []  # sorted array to hold result of Tree to array conversion
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            nums.append(root.val)
            root = root.right

        return self.nums2BST(nums)