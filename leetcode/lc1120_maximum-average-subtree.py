"""
1120. Maximum Average Subtree
Medium

477

15

Add to List

Share
Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)



Example 1:



Input: [5,6,1]
Output: 6.00000
Explanation:
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.


Note:

The number of nodes in the tree is between 1 and 5000.
Each node will have a value between 0 and 100000.
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Tree
post order traverse and return sums, node counts, and max avg within the give subtree
than aggregate as we traverse back to tree top

time O(log(N)) - log(N) is tree height
"""


class Solution:
    def recursive_ma(self, node):
        sums, count = node.val, 1
        left_sum, left_count, left_ma = 0, 0, 0
        if node.left:
            left_sum, left_count, left_ma = self.recursive_ma(node.left)
        right_sum, right_count, right_ma = 0, 0, 0
        if node.right:
            right_sum, right_count, right_ma = self.recursive_ma(node.right)

        ma = (sums + left_sum + right_sum) / (count + left_count + right_count)
        return sums + left_sum + right_sum, count + left_count + right_count, max(ma, left_ma, right_ma)

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        sums, count, ma = self.recursive_ma(root)

        return ma

def main():
    from leetcode.lc_tools import deserialize
    sol = Solution()
    assert sol.maximumAverageSubtree(deserialize("[5,6,1]")) == 6.000, 'fails'

if __name__ == '__main__':
   main()