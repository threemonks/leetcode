"""
865. Smallest Subtree with all the Deepest Nodes
Medium

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.

Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.
Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.


Constraints:

The number of nodes in the tree will be in the range [1, 500].
0 <= Node.val <= 500
The values of the nodes in the tree are unique.
"""

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
DFS
DFS traverse tree with depth, record ancestors list along the traverse

When DFS traverse is done, we know the maximum depth, then we can go back to the ancestors list and retrieve only the ancestors list for nodes at maximum depth

if there's one node at maximum depth, return it
if more than one node at maximum depth, return LCA of them (last common node on their ancestors list)

"""


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        parents_lists = collections.defaultdict(list)
        maxdepth = 0

        stack = [(root, 0, [root])]

        while stack:
            cur, depth, path = stack.pop()
            parents_lists[depth].append(path[:])
            maxdepth = max(maxdepth, depth)
            if cur.left:
                stack.append((cur.left, depth + 1, path + [cur.left]))
            if cur.right:
                stack.append((cur.right, depth + 1, path + [cur.right]))

        # find parent lists for leaf node at maxdepth
        parents_list = parents_lists[maxdepth]

        # find their LCA
        if len(parents_list) == 1:  # only one node at deepest level
            return parents_list[0][-1]
        else:

            minlen = min([len(pl) for pl in parents_list])
            i = 0
            while i < minlen and len(set([pl[i].val for pl in parents_list])) == 1:
                i += 1

            # when loop exits, i-1 points at last common ancestor
            return parents_list[0][i - 1]


"""
BFS

first find maximum depth, then find LCA of all nodes of that depth

to find LCA of all nodes of deepest depth:
1. if node in question has max depth, it is the answer
2. if both left and right child has descendant of deepest depth, then the answer is this node (parent)
3. otherwise, if one child has deepest descendant, then the answer is that child
4. otherwise, answer for this subtree does not exist

time O(N)
space O(N)
"""


class Solution1:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def bfs(node):
            # find maximum height of subtree at this node
            if not node:
                return 0
            else:
                return max(1 + bfs(node.left), 1 + bfs(node.right))

        max_depth = bfs(root)

        def answer(node, depth):
            # find LCA of given node recursively
            if not node:
                return None
            if depth == max_depth:
                return node
            else:
                left = answer(node.left, depth + 1)
                right = answer(node.right, depth + 1)
                if left and right:
                    return node
                elif left:
                    return left
                elif right:
                    return right
                else:
                    return None

        return answer(root, 1)