"""
515. Find Largest Value in Each Tree Row
Medium

1510

74

Add to List

Share
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).





Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,null,2]
Output: [1,2]
Example 5:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree will be in the range [0, 10^4].
-2^31 <= Node.val <= 2^31 - 1
"""
# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List

"""
BFS

level order traverse, within each level, record max, and append to answer when level is done.
"""
from collections import deque


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = deque([root])

        ans = []
        while q:
            l = len(q)
            newq = []
            level_max = -math.inf
            while l:
                cur = q.popleft()
                level_max = max(level_max, cur.val)
                if cur.left:
                    newq.append(cur.left)
                if cur.right:
                    newq.append(cur.right)
                l -= 1

            q += newq
            ans.append(level_max)

        return ans


def main():
    from leetcode.lc_tools import deserialize
    sol = Solution()
    root = deserialize("[1,3,2,5,3,null,9]")
    assert sol.largestValues(root=root) == [1,3,9], 'fails'

if __name__ == '__main__':
   main()