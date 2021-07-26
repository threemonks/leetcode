"""
236. Lowest Common Ancestor of a Binary Tree
Medium

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""
"""
Lowest Common Ancestor (LCA) of Binary Tree

find path from root to p, and path from root to q, take the common prefix of the two paths, the last node in the common prefix is the LCA
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution0:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        def find_path(root, p):
            if not root:
                return []
            elif root == p:
                return [root]
            else:
                left_path = find_path(root.left, p)
                if left_path:
                    return [root] + left_path
                right_path = find_path(root.right, p)
                if right_path:
                    return [root] + right_path

                # not found
                return []


        path_p = find_path(root, p)
        path_q = find_path(root, q)
        i = 0
        while i < min(len(path_p), len(path_q)) and path_p[i] == path_q[i]:
            i += 1

        return path_p[i-1]

"""
Lowest Common Ancestor (LCA) of Binary Tree

Recursive/DFS
1. start traversing the tree from root
2. if current node is p or q, return current node, else we search both left and right child tree
3. if either left or right subtree search returns some result (not None), that means at least one of p or q is in that subtree
4. if both left and right subtree returns node, that means p and q are in different subtree, so the current node is the LCA
5. if only one side returns a node, that would be the LCA

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: # if both left and right returns, means p and q are on separate branch (one in left, one in right)
            return root
        else: # only one side has return value, means both p and q are on one side of root
            return left or right

"""
Lowest Common Ancestor (LCA) of Binary Tree

DFS/Iterative with stack to traverse the tree until we see p or q, and when one node is found, the path from root to this node is its ancenstors list.

Compare ancenstors list for p and q, the lowest common ancestor is LCA.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        p_parents = []
        q_parents = []

        stack = [(root, [root])]

        while stack:
            node, path = stack.pop()
            if node == p:
                p_parents = path[:]
            if node ==  q:
                q_parents = path[:]
            if node.left:
                stack.append((node.left, path+[node.left]))
            if node.right:
                stack.append((node.right, path+[node.right]))

        # when done, we should have p_parents and q_parents
        i = 0
        while i < min(len(p_parents), len(q_parents)) and p_parents[i] == q_parents[i]:
            i += 1

        return p_parents[i-1]

def main():
    sol = Solution()
    root = TreeNode(3, left=TreeNode(5, left=TreeNode(6), right=TreeNode(2, left=TreeNode(7), right=TreeNode(4))), right=TreeNode(1, left=TreeNode(0), right=TreeNode(8)))
    assert sol.lowestCommonAncestor(root = root, p = root.left, q = root.right) == root, 'fails'


if __name__ == '__main__':
   main()