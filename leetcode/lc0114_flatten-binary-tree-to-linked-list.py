"""
114. Flatten Binary Tree to Linked List
Medium

4994

424

Add to List

Share
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


Follow up: Can you flatten the tree in-place (with O(1) extra space)?

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Tree Linked List

do inorder traverse iteratively, append each node to current tail as right child

space: O(N)
"""


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return

        stack = [root]
        tail = TreeNode(val=0, right=root)
        while stack:
            node = stack.pop()
            # print('node%s' % node.val)
            node_right = node.right
            node_left = node.left
            node.left = None  # break links within original list
            node.right = None
            tail.right = node
            tail = tail.right
            if node_right:
                stack.append(node_right)
                # print('appending %s to stack=%s' % (node.right.val, stack))
            if node_left:
                stack.append(node_left)
                # print('appending %s to stack=%s' % (node.left.val, stack))

        # don't return, as root is in place