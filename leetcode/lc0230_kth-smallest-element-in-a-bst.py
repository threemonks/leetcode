"""
230. Kth Smallest Element in a BST
Medium

Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.



Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104


Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Recursive DFS / Preorder
preorder traverse will give proper increasing array, get its k-th element
"""


class Solution0:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        res = []

        def preorder(node):
            nonlocal res
            if node.left:
                preorder(node.left)
            res.append(node.val)
            if node.right:
                preorder(node.right)

        preorder(root)
        # print(res)
        return res[k - 1]


"""
Iterative DFS / Preorder
"""


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            # now we are at left most (smallest) node
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        # print(res)
        return res[k - 1]

from leetcode.lc_tools import deserialize
def main():
    sol = Solution()
    assert sol.kthSmallest(deserialize("[3,1,4,null,2]"), k = 1) == 1, 'fails'

    assert sol.kthSmallest(deserialize("[5,3,6,2,4,null,null,1]"), k = 3) == 3, 'fails'


if __name__ == '__main__':
   main()