"""
1522. Diameter of N-Ary Tree
Medium

219

3

Add to List

Share
Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

(Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)



Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Explanation: Diameter is shown in red color.
Example 2:



Input: root = [1,null,2,null,3,4,null,5,null,6]
Output: 4
Example 3:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 7


Constraints:

The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [1, 10^4].
"""
# Definition for a Node.
class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
DFS

1. dfs visit each node, for each node, calculate all its children's max depth, return max depth of this node, also calculate diameter that passes this node and update global max diameter
"""


class Solution:

    def diameter(self, root: 'TreeNode') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        maxdiameter = 0

        def dfs_height(node):
            nonlocal maxdiameter
            # calculate height via dfs, and update global max diameter with new result from this node at same time
            h1, h2 = 0, 0  # max height1 height2
            for child in node.children:
                ch = dfs_height(child)
                ch += 1  # to include current node
                if ch > h1:
                    h1, h2 = ch, h1
                elif ch > h2:
                    h2 = ch
            maxdiameter = max(maxdiameter, h1 + h2)  # sum top two heights

            return h1

        dfs_height(root)

        return maxdiameter


def main():
    from leetcode.lc_tools import deserialize
    sol = Solution()
    root = deserialize("[1,null,3,2,4,null,5,6]")
    assert sol.diameter(root=root) == 3, 'fails'

    root = deserialize("[1,null,2,null,3,4,null,5,null,6]")
    assert sol.diameter(root=root) == 4, 'fails'

if __name__ == '__main__':
   main()
