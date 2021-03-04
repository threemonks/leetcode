"""
1650. Lowest Common Ancestor of a Binary Tree III
Medium

92

5

Add to List

Share
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q exist in the tree.
"""

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

"""

Tree traverse

traverse tree upwards to parent, and keep track of list of ancestors, and check if current parent node of current node is in the parent node list of the other node, if so, return the node as answer

"""


class Solution0:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if p.val == q.val:
            return p

        p_parents = set()
        q_parents = set()

        while p and q and p.val != q.val:
            p_parents.add(p.val)
            if p.val in q_parents:
                return p
            if p.parent:
                p = p.parent
            q_parents.add(q.val)
            if q.val in p_parents:
                return q
            if q.parent:
                q = q.parent

        return p


"""
Tree traverse - Two Pointers

similar to intersection point of two linked lists (lc0160), traverse along parents list, when reaching root, set the pointer to start node of the other node's (path) starting point, when they eventually meet, it will be at the lowest common ancestor

time O(M+N)
space O(1)
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if p.val == q.val:
            return p
        p0, q0 = p, q  # keep starting node of p and q

        while p != q:
            # when p.parent is None p is at root, we restart p at q0
            p = p.parent if p.parent is not None else q0
            q = q.parent if q.parent is not None else p0

        # when exist loop, p and q would be pointing at lowest common ancestor
        return p
