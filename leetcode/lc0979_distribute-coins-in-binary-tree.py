"""
979. Distribute Coins in Binary Tree
Medium

2350

80

Add to List

Share
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins and there are n coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another. (A move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.



Example 1:


Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:


Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
Example 3:


Input: root = [1,0,2]
Output: 2
Example 4:


Input: root = [1,0,0,null,3]
Output: 4


Constraints:

The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of Node.val is n.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


"""
DFS post order traverse, each child will return its extra coins that it will give to parent, left, and right, negative means it needs this many coins, and the parent would need to transfer parent.val+left+right-1 coins back to its parent, so the total moves, to move from left to parent, from parent to right, and remainings from parent to parent's parent are:

abs(left)+abs(right) + abs(parent.val+left+right-1) moves

"""


class Solution0:
    def distributeCoins(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)

            # total moves needed to move extra coins in left subtree to current node
            # extra coins in right subtree to current node
            ans += abs(left) + abs(right)

            # keep 1 coin for this node, return rest balance to upper parent
            return node.val + left + right - 1

        dfs(root)

        return ans


"""
DFS post order traverse with extra parameter pointer to parent

"""


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:

        ans = 0

        def dfs(node, p=None):
            nonlocal ans
            if not node: return 0
            dfs(node.left, p=node)
            dfs(node.right, p=node)

            # keep 1 coin for this node, return rest balance to upper parent
            if p:
                p.val += node.val - 1
            ans += abs(node.val - 1)

        dfs(root, p=None)

        return ans


from leetcode.lc_tools import deserialize
def main():
    sol = Solution()
    assert sol.distributeCoins(root = deserialize("[3,0,0]")) == 2, 'fails'

    assert sol.distributeCoins(root = deserialize("[0,3,0]")) == 3, 'fails'

    assert sol.distributeCoins(root = deserialize("[1,0,2]")) == 2, 'fails'

    assert sol.distributeCoins(root = deserialize("[1,0,0,null,3]")) == 4, 'fails'

if __name__ == '__main__':
   main()