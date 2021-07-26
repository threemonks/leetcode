"""
1644. Lowest Common Ancestor of a Binary Tree II
Medium

Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.
Example 3:



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null
Explanation: Node 10 does not exist in the tree, so return null.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-109 <= Node.val <= 109
All Node.val are unique.
p != q


Follow up: Can you find the LCA traversing the tree, without checking nodes existence?
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


"""
DFS traverse the tree to find node p and q, also record the path to the node found
lowest common node along the paths (parents nodes) for both p and q is the LCA

"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root

        p_parents = []
        q_parents = []
        stack = [(root, [root])]
        while stack:
            cur, path = stack.pop()
            if cur.val == p.val:
                p_parents = path[:]
            if cur.val == q.val:
                q_parents = path[:]
            # explore children
            if cur.left:
                stack.append((cur.left, path + [cur.left]))
            if cur.right:
                stack.append((cur.right, path + [cur.right]))

        if not p_parents or not q_parents:
            return None
        else:
            i = 0
            while i < min(len(p_parents), len(q_parents)) and p_parents[i] == q_parents[i]:
                i += 1
            # when loop finishes, i-1 points at last common ancestor
            return p_parents[i - 1]

def main():
    sol = Solution()
    # root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    root = TreeNode(3, left=TreeNode(5, left=TreeNode(6), right=TreeNode(2, left=TreeNode(7), right=TreeNode(4))), right=TreeNode(1, left=TreeNode(0), right=TreeNode(8)))
    assert sol.lowestCommonAncestor(root = root, p = root.left, q = root.left.right.right) == root.left, 'fails'

if __name__ == '__main__':
   main()