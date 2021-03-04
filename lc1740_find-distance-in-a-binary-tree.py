"""
1740. Find Distance in a Binary Tree
Medium

Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and value q in the tree.

The distance between two nodes is the number of edges on the path from one to the other.



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0
Output: 3
Explanation: There are 3 edges between 5 and 0: 5-3-1-0.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7
Output: 2
Explanation: There are 2 edges between 5 and 7: 5-2-7.
Example 3:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5
Output: 0
Explanation: The distance between a node and itself is 0.


Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 109
All Node.val are unique.
p and q are values in the tree.

"""
# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""

Tree traverse

we would need to find LCA of p and q, then the distance would be p -> LCA + LCA ->q

"""


class Solution0:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        if p == q:
            return 0

        stack = [(root, [root])]
        p_ancestors = []
        q_ancestors = []

        while stack:
            cur, path = stack.pop()
            if cur.val == p:
                p_ancestors = path[:]
            if cur.val == q:
                q_ancestors = path[:]
            if cur.left:
                stack.append((cur.left, path + [cur.left]))
            if cur.right:
                stack.append((cur.right, path + [cur.right]))

        m, n = len(p_ancestors), len(q_ancestors)
        minlen = min(m, n)
        i = 0
        while i < minlen and p_ancestors[i] == q_ancestors[i]:
            i += 1

        # now i-1 points at LCA
        # the distance is m-(i-1)-1 + n-(i-1)-1 = m-i + n-i
        return m - i + n - i


"""
DFS to find LCA
then recursively calculate distance between lca to p, and lca to q

"""


class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:

        def find_lca(root, p, q):
            if not root or root.val == p or root.val == q:
                return root
            left = find_lca(root.left, p, q)
            right = find_lca(root.right, p, q)
            if left and right:
                return root
            else:
                return left or right

        lca = find_lca(root, p, q)
        print(lca.val)

        # recursively calculate distance
        def dist(node, target):
            if not node:
                return math.inf
            elif node.val == target:
                return 0
            return min(dist(node.left, target),
                       dist(node.right, target)) + 1

        return dist(lca, p) + dist(lca, q)
