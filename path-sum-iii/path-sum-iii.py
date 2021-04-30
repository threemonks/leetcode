from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
dfs traversal

along traversal, we record the current running path sum, and the count of each path sums that have occurred by now along this path

key point:
1. we need use hashmap to store how many times a given sum has appeared along this path (because negative number could result in some section of a path sum to zero, then a given sum could appear again later)
2. need to have this count of sum specific to each dfs traverse path, since same sum from different path cannot be used to sum to k
"""
class Solution:
    def pathSum(self, root: TreeNode, t: int) -> int:
        if not root:
            return 0
        ans = 0
        counts = defaultdict(int)

        def dfs(node, curr_sum):
            nonlocal ans, counts
            if not node:
                return
            # current prefix
            curr_sum += node.val
            # this path sum to t at this node
            if curr_sum == t:
                ans += 1

            # number of times curr_sum-t already occured
            # i.e., number of times path with sum t has occurred up to current node
            if curr_sum-t in counts:
                ans += counts[curr_sum-t]
                
            # add current sum to hashmap to use it during child nodes processing
            counts[curr_sum] += 1
            
            # explore left and right subtree
            if node.left:
                dfs(node.left, curr_sum)
            if node.right:
                dfs(node.right, curr_sum)
                
            # backtrack, remove current sum from hashmap
            # to avoid this count being used by other parallel subtree processing
            counts[curr_sum] -= 1
                
        
        dfs(root, 0)
        
        return ans
        