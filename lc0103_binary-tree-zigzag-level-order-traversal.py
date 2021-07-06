"""
103. Binary Tree Zigzag Level Order Traversal
Medium

3774

132

Add to List

Share
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
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
Tree / DFS

basically level order traverse, but save each level's result separately, and reverse result of a level depending on its level # level%2==1

time: O(N)
space: O(N)
"""


class Solution0:
    def recursive_level_order(self, node, level):
        if not node:
            return {}
        ans_dict = {level: [node.val]}
        left = self.recursive_level_order(node.left, level + 1)
        for k, v in left.items():
            if k in ans_dict:
                ans_dict[k].extend(v)
            else:
                ans_dict[k] = v
        right = self.recursive_level_order(node.right, level + 1)
        for k, v in right.items():
            if k in ans_dict:
                ans_dict[k].extend(v)
            else:
                ans_dict[k] = v
        return ans_dict

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        ans_dict = self.recursive_level_order(root, 0)

        ans = []
        for k, v in ans_dict.items():
            if k % 2 == 1:
                ans.append(v[::-1])
            else:
                ans.append(v)

        return ans

"""
BFS level order traverse

"""
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        level = 1
        while q:
            l = len(q)
            newq = []
            newans = []
            level += 1
            while l:
                cur = q.popleft()
                newans.append(cur.val)
                if cur.left:
                    newq.append(cur.left)
                if cur.right:
                    newq.append(cur.right)
                l -= 1

            q.extend(newq)
            if level % 2 == 1:  # odd level, reverse nodes
                ans += [newans[::-1]]
            else:
                ans += [newans[:]]

        return ans

def main():
    from lc_tools import deserialize
    sol = Solution()
    assert sol.zigzagLevelOrder(root = deserialize("[3,9,20,null,null,15,7]")) == [[3],[20,9],[15,7]], 'fails'

    assert sol.zigzagLevelOrder(root = deserialize("[1]")) == [[1]], 'fails'

    # assert sol.zigzagLevelOrder(root = deserialize("[]")) == [], 'fails'

if __name__ == '__main__':
   main()

