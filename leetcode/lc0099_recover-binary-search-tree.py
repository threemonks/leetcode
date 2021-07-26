"""
99. Recover Binary Search Tree
Hard

You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?



Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.


Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
InOrder Traverse of BST
brutal force:

1. inorder traverse of BST results in an array
2. find the two swapped elements in an almost sorted array where only two elements are swapped.
3. swap the values of the two nodes

time O(N)
space O(N) - array
"""


class Solution0:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        array = inorder(root)

        # find the two values that are swapped in the array
        i, j = 0, len(array) - 1
        while i < len(array) and array[i] < array[i + 1]:
            i += 1
        while j >= 0 and array[j - 1] < array[j]:
            j -= 1

        # now traverse the tree again, and swap these two values array[i], array[j] in the tree
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.val == array[i]:
                cur.val = array[j]
            elif cur.val == array[j]:
                cur.val = array[i]
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)


"""
InOrder Traverse of BST

Do in order traverse, but instead of print elements, we find the ones that are not following BST property

Iterative inorder traversal is simple: go left as far as you can (and store parent into stack along), then one step right. Repeat till the end of nodes in the tree.

To find the nodes that were out of order in inorder traverse, keep track of predecessor (pred) of current node, if pred.val > curr.val, then pred is the node that needs to be swapped, and there are ONLY two such node, so we can break once two have been found

time O(N)
space O(N)
"""


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        first, second = None, None

        # iterative in order traverse
        pred = None
        curr = root
        stack = []
        while curr or stack:
            # process left child
            # move down to most bottom left node, store parents into stack along
            while curr:
                stack.append(curr)
                curr = curr.left

            # pop out parent from stack
            curr = stack.pop()
            # do something with parent
            if pred and pred.val > curr.val:
                # The first element is always larger than its next one
                # if first element is not found, then pred is the first one
                if first is None:
                    first = pred
                # the second element is always smaller than its previous one.
                # if first element is found, then curr is the seoncd element
                # note this could happen at same time as first is set,
                # as the two elements to be swapped might be next to each other
                # e.g.., [0,1]
                if first is not None:
                    second = curr

            # keep track of predecessor of curr
            pred = curr
            # now process to right child
            curr = curr.right

        # now we can swap these two nodes
        first.val, second.val = second.val, first.val

from leetcode.lc_tools import binary_tree_equal

def main():
    sol = Solution()
    root = TreeNode(1, left=TreeNode(3, right=TreeNode(2)))
    sol.recoverTree(root)
    assert binary_tree_equal(root, TreeNode(3, left=TreeNode(1, right=TreeNode(2)))), 'fails'

    root = TreeNode(3, left=TreeNode(1), right=TreeNode(4, left=TreeNode(2)))
    sol.recoverTree(root)
    assert binary_tree_equal(root, TreeNode(2, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3)))), 'fails'

if __name__ == '__main__':
   main()