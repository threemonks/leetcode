"""
Recursive/DFS
1. start traversing the tree from root
2. if current node is p or q, return current node, else we search both left and right child tree
3. if either left or right subtree search returns some result (not None), that means at least one of p or q is in that subtree
4. if both left and right subtree returns node, that means p and q are in different subtree, so the current node is the LCA
5. if only one side returns a node, that would be the LCA

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: # if both left and right returns, means p and q are on separate branch (one in left, one in right)
            return root
        else: # only one side has return value, means both p and q are on one side of root
            return left or right