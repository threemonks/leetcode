"""
666. Path Sum IV
Medium

225

304

Add to List

Share
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:

The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.

It's guaranteed that the given list represents a valid connected binary tree.

Example 1:

Input: [113, 215, 221]
Output: 12
Explanation:
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.


Example 2:

Input: [113, 221]
Output: 4
Explanation:
The tree that the list represents is:
    3
     \
      1

The path sum is (3 + 1) = 4.

"""
from typing import List

"""
the array gives level order traverse
so we need to build tree from level order traverse, then sum all paths
We need to construct the tree from input array

For node xy? its left child is (x+1)(y*2-1)? and right child is (x+1)(y*2)?
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        root = TreeNode(val=nums[0] % 10)
        cur = None

        for i in range(1, len(nums)):
            num = nums[i]
            depth, pos, val = num // 100, (num % 100) // 10, num % 10
            pos -= 1  # pos needs to be 0 indexed
            # print('i=%s num=%s depth=%s pos=%s val=%s' % (i, num, depth, pos, val))
            node = TreeNode(val=val)
            # complete binary tree, last level (d) has 2**(d-1) nodes
            # with 0-index pos
            # pos < (2**(d-1))/2 => left
            cur = root
            for d in range(depth - 2, -1, -1):
                if pos < 2 ** d:  # left tree
                    if not cur.left:
                        cur.left = node
                    cur = cur.left
                else:  # right
                    if not cur.right:
                        cur.right = node
                    cur = cur.right
                pos %= 2 ** d  # unchanged if it is on left half, but subtract 2**d (half of last level's length) if it is on right half

        # print(root)

        # now we have the tree, dfs traverse to sum all paths
        ans = 0

        def dfs(node, sums):
            nonlocal ans
            sums += node.val
            if not node.left and not node.right:  # this is leaf node
                ans += sums
            if node.left:
                dfs(node.left, sums)
            if node.right:
                dfs(node.right, sums)

        dfs(root, 0)

        return ans

def main():
    sol = Solution()
    assert sol.pathSum([113, 215, 221]) == 12, 'fails'

    assert sol.pathSum([113, 221]) == 4, 'fails'

if __name__ == '__main__':
   main()