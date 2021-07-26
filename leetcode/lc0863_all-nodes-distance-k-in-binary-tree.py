"""
863. All Nodes Distance K in Binary Tree
Medium

3533

73

Add to List

Share
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque, defaultdict

"""
Tree

Convert to graph and do BFS

"""


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        adj_list = defaultdict(list)

        def dfs(node):
            nonlocal adj_list
            if not node:
                return
            if node.left:
                adj_list[node.val].append(node.left.val)
                adj_list[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                adj_list[node.val].append(node.right.val)
                adj_list[node.right.val].append(node.val)
                dfs(node.right)

        # convert tree to graph in adj_list form
        dfs(root)

        # BFS traverse from target node for K steps
        q = deque([(target.val, K)])
        visited = set([target.val])

        ans = []
        while q:
            cur, step = q.popleft()
            if step == 0:
                ans.append(cur)
            elif step > 0:
                for nxt in adj_list[cur]:
                    if nxt not in visited:
                        q.append((nxt, step - 1))
                        visited.add(nxt)

        return ans


from leetcode.lc_tools import deserialize
def main():
    sol = Solution()
    assert set(sol.distanceK(root = deserialize("[3,5,1,6,2,0,8,null,null,7,4]"), target = TreeNode(5), K = 2)) == set([1, 7, 4]), 'fails'


if __name__ == '__main__':
   main()