"""
366. Find Leaves of Binary Tree
Medium

1517

23

Add to List

Share
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.


Example 1:


Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]


Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
DFS

note:
return value list of subtree, along with height of each sublist from leaves
"""
from collections import deque


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:

        def dfs(node):
            if not node:
                return {}
            elif node and not node.left and not node.right:
                return {0: [node.val]}
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                height = 1 + max(max(list(left.keys())) if left else 0, max(list(right.keys())) if right else 0)
                res = {height: [node.val]}
                for k, v in left.items():
                    if k in res:
                        res[k].extend(v)
                    else:
                        res[k] = v
                for k, v in right.items():
                    if k in res:
                        res[k].extend(v)
                    else:
                        res[k] = v
                return res

        res = dfs(root)
        ans = []
        for k in sorted(res.keys()):
            ans.append(res[k])

        return ans


def main():
    from leetcode.lc_tools import deserialize
    sol = Solution()
    assert sol.findLeaves(root = deserialize('[1,2,3,4,5]')) == [[4,5,3],[2],[1]], 'fails'

    assert sol.findLeaves(root = deserialize('[1]')) == [[1]], 'fails'

if __name__ == '__main__':
   main()