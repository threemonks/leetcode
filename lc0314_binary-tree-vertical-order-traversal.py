"""
314. Binary Tree Vertical Order Traversal
Medium

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
Example 4:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""
# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from sortedcontainers import SortedDict

"""
DFS

DFS traversal, also keep track of offset (relative to root, -1 for left child, +1 for right child)
append each node value to the output dict identified and sorted by the offset value

how about same offset, from top to bottom, so we keep track of depth

how about same row and column, left to right (dfs traverse goes to left child first, then right child)

"""


class Solution0:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        node_list = SortedDict()

        def dfs(curr, offset=0, depth=0):
            """ node, left/right offset, depth"""
            nonlocal node_list
            if curr.left:
                if offset - 1 in node_list:
                    node_list[offset - 1].append((depth + 1, curr.left.val))  # depth, left/right, val
                else:
                    node_list[offset - 1] = [(depth + 1, curr.left.val)]  # depth, left/right, val
                dfs(curr.left, offset - 1, depth + 1)
            if curr.right:
                if offset + 1 in node_list:
                    node_list[offset + 1].append((depth + 1, curr.right.val))  # depth, left/right, val
                else:
                    node_list[offset + 1] = [(depth + 1, curr.right.val)]  # depth, left/right, val
                dfs(curr.right, offset + 1, depth + 1)

        node_list[0] = [(0, root.val)]
        dfs(root, 0, depth=0)

        result = []
        for lst in node_list.values():
            result.append([x[1] for x in sorted(lst, key=lambda x: x[0])])

        return result


"""
BFS

BFS traversal
use dict column to keep track of offset (column) position

"""


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        node_list = SortedDict()  # key is column position, value is tuple of (depth, node.val)
        column = dict()

        node_list[0] = [(0, root.val)]  # key is column, value is (depth, node.val)
        dq = collections.deque([(root, 0, 0)])  # node, depth, column

        while dq:
            curr, depth, col = dq.popleft()

            if curr.left:
                if col - 1 in node_list:
                    node_list[col - 1].append((depth + 1, curr.left.val))
                else:
                    node_list[col - 1] = [(depth + 1, curr.left.val)]
                dq.append((curr.left, depth + 1, col - 1))
            if curr.right:
                if col + 1 in node_list:
                    node_list[col + 1].append((depth + 1, curr.right.val))
                else:
                    node_list[col + 1] = [(depth + 1, curr.right.val)]
                dq.append((curr.right, depth + 1, col + 1))

        result = []
        for lst in node_list.values():
            result.append([x[1] for x in sorted(lst, key=lambda x: x[0])])

        return result

from lc_tools import deserialize
def main():
    sol = Solution()
    assert sol.verticalOrder(root = deserialize('[3,9,20,null,null,15,7]')) == [[9],[3,15],[20],[7]], 'fails'

    assert sol.verticalOrder(root = deserialize('[3,9,8,4,0,1,7]')) == [[4],[9],[3,0,1],[8],[7]], 'fails'

    assert sol.verticalOrder(root = deserialize('[3,9,8,4,0,1,7,null,null,null,2,5]')) == [[4],[9,5],[3,0,1],[8,2],[7]], 'fails'

if __name__ == '__main__':
   main()