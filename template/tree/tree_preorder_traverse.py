"""
preorder Traverse of Tree

recursive
"""

class Solution:
    def preorder(self, root):
        print(root.val)
        self.preorder(root.left)  # left
        self.preorder(root.right)  # right

"""
iterative
"""

class Solution1:
    def preorder(self, root):
        stack =[root]

        while stack:
            # now process
            root = stack.pop()
            print(root.val)
            # push right into stack first, so that when popout and process, left child gets processed first
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
