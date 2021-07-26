"""
199. Binary Tree Right Side View
Medium

3825

204

Add to List

Share
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

"""
we do level order traverse, and output nodes with its level/depth
only last value of each level output is added to final ans
"""


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ansdict = defaultdict(int)
        dq = deque([(1, root)])
        maxlevel = 1
        while dq:
            level, cur = dq.popleft()
            maxlevel = max(maxlevel, level)
            ansdict[level] = cur.val
            if cur.left:
                dq.append((level + 1, cur.left))
            if cur.right:
                dq.append((level + 1, cur.right))

        ans = []
        for i in range(1, maxlevel + 1):
            ans.append(ansdict[i])

        return ans