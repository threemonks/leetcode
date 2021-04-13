"""
968. Binary Tree Cameras
Hard

1256

19

Add to List

Share
Given a binary tree, we install cameras on the nodes of the tree.

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.



Example 1:


Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:


Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""

DP DFS / topdown

use recursive / dfs dp, we define dfs(node) be the num of cameras needed to cover the subtree rooted at node, then there are three states:

state=0: all nodes below are covered, but node not covered (still need cover)
state=1: all nodes below are covered, including this node, but no camera at this node (covered, no camera)
state=2: all nodes below are covered, including this node, and a camera is on this node (covered, with camera)

then we can recursively calculate dfs(node) using result from dfs call to its children
* dp0: to cover a strict subtree children of current node must be in state 1
* dp1: cover a normal subtree without placing camera here, the children of this node must be in state1 or state 2, and at least one of those children must be in state 2 (has camera)
* dp2: to cover the subtree while placing a camera at this node, the children can be in any state
"""
class Solution0:
    def minCameraCover(self, root: TreeNode) -> int:

        def dfs(node):
            # returns three values, dp0, dp1, dp2
            # 0 means this node not covered
            # 1 means covered, but no camera at this node
            # 2 means covered, and has camera at this node
            if not node: # cannot have camera
                return 0, 0, math.inf

            left = dfs(node.left)
            right = dfs(node.right)

            dp0 = left[1] + right[1]
            dp1 = min(min(left[1:]) + right[2], left[2] + min(right[1:]))
            dp2 = 1+ min(left) + min(right) # add camera at this node

            # print('node=%s dp0=%s dp1=%s dp2=%s' % (node.val, dp0, dp1, dp2))
            return dp0, dp1, dp2

        return min(dfs(root)[1:]) # root must be in state 1 or 2

"""
Greedy / Bottom up

observation:
Noting that leaf node covered by its parent is always better solution then placing camera at the leaf node itself, as placing camera at leaf node just cover itself and its parent, but placing camera at its parent would cover leaf, leaf's parent and leaf's parent's parent.

still we need to realize that there are three states for each node
0: this node has no camera, not covered
1: this node has no comera, but covered by camera from below
2: this node has a camera

we recursively call dfs on nodes's left and right children, based on result from left and right, we decide whether we need a camera at current node or not, and how it affect overall camera counts

"""
class Solution1:
    def minCameraCover(self, root: TreeNode) -> int:

        ans = 0
        def dfs(node):
            # return 0, 1, 2
            # 0 means node is not covered, not camera at it
            # 1 means node is covered, but no cmaera at it
            # 2 means node is covered, and has camera at it
            nonlocal ans

            if not node:
                return 1 # no camera, and covered (no node, don't need to cover)
            need_camera, covered = False, False
            if node.left:
                left = dfs(node.left)
                if left == 0:
                    need_camera = True
                    covered = True
                elif left == 1:
                    pass
                else: # left == 2:
                    covered = True
            if node.right:
                right = dfs(node.right)
                if right == 0:
                    need_camera = True
                    covered = True
                elif right == 1:
                    pass
                else: # left == 2:
                    covered = True

            if need_camera:
                covered = True
                ans += 1
                return 2

            if not covered:
                return 0

            return 1

        state = dfs(root)

        if state == 0: # root still needs a camera to cover it
            ans += 1

        return ans

"""
Greedy / Bottom up

Using hashmap to store covered nodes

Note there are three states for each node on how it is covered or not
0: this node has no camera, not covered
1: this node has no comera, but covered by camera from below
2: this node has a camera

we recursively call dfs on nodes's left and right children, based on result from left and right, we decide whether we need a camera at current node or not, and how it affect overall camera counts

"""
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:

        ans = 0
        covered = set([None])
        def dfs(node, parent=None):
            nonlocal ans, covered
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                if (parent is None and node not in covered) or node.left not in covered or node.right not in covered:
                        # if child needs cover, or this is root and not covered
                        ans += 1
                        covered.add(parent)
                        covered.add(node)
                        covered.add(node.left)
                        covered.add(node.right)

        dfs(root)

        return ans

from lc_tools import deserialize
def main():
    sol = Solution()
    assert sol.minCameraCover(deserialize("[0,0,null,0,0]")) == 1, 'fails'

    assert sol.minCameraCover(deserialize("[0,0,null,0,null,0,null,null,0]")) == 2, 'fails'

if __name__ == '__main__':
   main()