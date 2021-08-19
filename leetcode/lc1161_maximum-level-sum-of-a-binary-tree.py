"""
1161. Maximum Level Sum of a Binary Tree
Medium

1002

46

Add to List

Share
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.



Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2


Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
"""
# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
BFS level order traverse
"""
from collections import deque


class Solution:
    def maxLevelSum(self, root: [TreeNode]) -> int:
        q = deque([root])  # node, level
        maxsum = -math.inf
        curlevel = 0
        ans = 1
        while q:
            l = len(q)
            curlevel += 1
            levelsum = 0
            newq = []
            while l > 0:
                cur = q.popleft()
                levelsum += cur.val
                if cur.left:
                    newq.append(cur.left)
                if cur.right:
                    newq.append(cur.right)
                l -= 1

            # update answer with levelsum
            if levelsum > maxsum:
                maxsum = levelsum
                ans = curlevel
            for nq in newq:
                q.append(nq)

        return ans


def main():
    from leetcode.lc_tools import deserialize
    sol = Solution()
    root = deserialize('[1,7,0,7,-8,null,null]')
    assert sol.maxLevelSum(root) == 2, 'fails'

    root = deserialize('[989,null,10250,98693,-89388,null,null,null,-32127]')
    assert sol.maxLevelSum(root) == 2, 'fails'

if __name__ == '__main__':
   main()