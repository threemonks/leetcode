"""
1373. Maximum Sum BST in Binary Tree
Hard

Given a binary tree root, the task is to return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:



Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
Example 2:



Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
Example 3:

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.
Example 4:

Input: root = [2,1,3]
Output: 6
Example 5:

Input: root = [5,4,8,3,null,6,3]
Output: 7


Constraints:

The given binary tree will have between 1 and 40000 nodes.
Each node's value is between [-4 * 10^4 , 4 * 10^4].

"""


# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
BST

basic idea
postorder traverse, and for each subtree, return four values, sum of all its nodes value, whether it is BST, min and max of all of its node values
at each node, if it is determined it is BST, then we update the global max sum

time O(N)
space O(log(N))
"""


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:

        ans = 0

        # postorder traverse
        def postorder(node):
            nonlocal ans
            if not node:
                return 0, True, math.inf, -math.inf
            left_sum, left_isbst, left_min, left_max = postorder(node.left)
            right_sum, right_isbst, right_min, right_max = postorder(node.right)

            # print(node.val)

            node_sum = node.val + left_sum + right_sum
            node_min = min(left_min, node.val, right_min)
            node_max = max(left_max, node.val, right_max)

            node_isbst = True
            if (node.left and (not left_isbst or left_max >= node.val)) or (
                    node.right and (not right_isbst or right_min <= node.val)):
                node_isbst = False

            if node_isbst:
                ans = max(ans, node_sum)
                # print('BST: %s sum=%s min=%s max=%s' % (node.val, node_sum, node_min, node_max))

            return node_sum, node_isbst, node_min, node_max

        postorder(root)

        return ans

from leetcode.lc_tools import deserialize
def main():
    sol = Solution()
    assert sol.maxSumBST(root = deserialize('[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]')) == 20, 'fails'

    assert sol.maxSumBST(root = deserialize('[4,3,null,1,2]')) == 2, 'fails'

    assert sol.maxSumBST(root=deserialize('[-4,-2,-5]')) == 0, 'fails'

    assert sol.maxSumBST(root=deserialize('[2, 1, 3]')) == 6, 'fails'

    assert sol.maxSumBST(root=deserialize('[5,4,8,3,null,6,3]')) == 7, 'fails'


if __name__ == '__main__':
   main()