"""
Inorder Traverse of Tree

recursive
"""

class Solution:
    def inorder(self, root):
        self.inorder(root.left)  # left
        print(root.val)
        self.inorder(root.right)  # right

"""
iterative
"""

class Solution1:
    def inorder(self, root):
        stack =[]

        while root or stack:
            # go to left most leaf
            while root:
                stack.append(root)
                root = root.left
            # now process
            root = stack.pop()
            print(root.val)
            # process right
            root = root.right
