"""
1676. Lowest Common Ancestor of a Binary Tree IV
Medium

Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.

Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
Output: 2
Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
Output: 1
Explanation: The lowest common ancestor of a single node is the node itself.

Example 3:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
Output: 5
Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.
Example 4:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [0,1,2,3,4,5,6,7,8]
Output: 3
Explanation: The lowest common ancestor of all the nodes is the root node.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-109 <= Node.val <= 109
All Node.val are unique.
All nodes[i] will exist in the tree.
All nodes[i] are distinct.
"""
# Definition for a binary tree node.
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
Tree traverse DFS

DFS tree traverse, and recording ancestor list from root to current node, if the node is one of nodes, store its parent lists

When tree traverse is done, check the last common elements among all the parents lists, that would be LCA

"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        n = len(nodes)

        parent_lists = collections.defaultdict(list)

        nodes_set = set([node.val for node in nodes])

        stack = [(root, [root])]

        while stack:
            cur, path = stack.pop()
            if cur.val in nodes_set:
                parent_lists[cur.val] = path[:]
            if cur.left:
                stack.append((cur.left, path + [cur.left]))
            if cur.right:
                stack.append((cur.right, path + [cur.right]))

        # now find the last common elements in all of parent_lists
        i = 0
        minlen = min([len(pl) for pl in parent_lists.values()])
        while i < minlen and len(set([pl[i].val for pl in parent_lists.values()])) == 1:
            i += 1

        # when loop exits, i-1 points at last common parent node
        return list(parent_lists.values())[0][i - 1]

