# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        def dfs(node, path, sums):
            if not node.left and not node.right:
                if sums == targetSum:
                    ans.append(path)
                return
            if node.left:
                dfs(node.left, path+[node.left.val], sums+node.left.val)
            if node.right:
                dfs(node.right, path+[node.right.val], sums+node.right.val)
            
        dfs(root, [root.val], root.val)
        
        return ans