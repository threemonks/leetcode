"""
222. Count Complete Tree Nodes
Medium

2881

258

Add to List

Share
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 5 * 10^4].
0 <= Node.val <= 5 * 10^4
The tree is guaranteed to be complete.


Follow up: Traversing the tree to count the number of nodes in the tree is an easy solution but with O(n) complexity. Could you find a faster algorithm?
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
brutal force
"""


class Solution0:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


"""
Binary Search

Since it is complete binary tree, with height d, the last level would have 1 to 2^d nodes. 
1. there's 2^d leaf nodes on last level, but we don't need to check all, we could do binary search and only check log(2^d)=d leaf nodes only
2. To check if a specific leaf node exist or not, we again use O(d) time to determine its' search path from root.
   within index range [0, 2**d-1] of last level, if the leaf node index idx is to left half, first move to root is to left
   i.e.
   left, right = 0, 2**d-1
   while d:
        m = left + (right-left)//2
        if idx <= m: # continue search left half
            node = node.left
            right = m
        else:
            node = node.right
            left = m+1

    return node is not None      

time O(log(N))
"""


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = 0  # root is at d=0 level
        cur = root
        while cur.left:
            d += 1
            cur = cur.left

        if d == 0:
            return 1

        def exists(idx, d, node):
            # check if m-th node (0-based) on last level (d) exists or not
            left, right = 0, 2 ** d - 1
            while d:
                m = left + (right - left) // 2
                if idx <= m:  # go left, continue search left half tree
                    node = node.left
                    right = m
                else:
                    node = node.right
                    left = m + 1
                d -= 1

            return node is not None

        # last level has 0 to 2^d-1, we binary search idx within [0, 2^d],
        # and for each such idx, we explore from root to it to verify if it exists or not
        last_idx = 0  # last_idx on last level
        l, r = 0, 2 ** d - 1
        while l <= r:
            m = l + (r - l) // 2
            if exists(m, d, root):  # exists
                last_idx = m
                l = m + 1
            else:  # not exists, shrink right side
                r = m - 1

        # the tree contains 2**d-1 nodes on the first (d-1) levels
        # and 0, ..., last_idx nodes on the last level
        return 2 ** d - 1 + last_idx + 1

from lc_tools import deserialize
def main():
    sol = Solution()
    assert sol.countNodes(root = deserialize('[1,2,3,4,5,6]')) == 6, 'fails'

    assert sol.countNodes(root=deserialize('[1]')) == 1, 'fails'


if __name__ == '__main__':
   main()