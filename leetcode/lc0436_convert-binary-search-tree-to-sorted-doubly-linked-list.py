"""
426. Convert Binary Search Tree to Sorted Doubly Linked List
Medium
"""
"""
# Definition for a Node.

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Tree

Need to do an inorder traverse and setup doubly links 
1. inorder traverse, left, root, right
2. needs to use global head and prev to keep track of linked list head, and prev node of current (root) node, to setup double link

"""


class Solution0:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        head = None  # linked list head (smallest element in BST)
        prev = None  # prev node of current node, to setup doubly linked list

        def inorder(root):
            nonlocal head, prev
            # inorder traverse, process left, then root, then right
            if not root:
                return

            inorder(root.left)  # left

            # process root
            # setup head
            if not head:
                head = root

            # setup double link
            if prev:
                prev.right = root
            root.left = prev
            prev = root

            inorder(root.right)  # right

            return head

        inorder(root)

        # connect head and tail
        head.left = prev
        prev.right = head

        return head


"""
Tree

Inorder traverse using iterative and stack

"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        head = None  # linked list head (smallest element in BST)
        prev = None  # prev node of current node, to setup doubly linked list
        stack = []

        while root or stack:
            while root:  # traverse to left most node, push all passing nodes to stack
                stack.append(root)
                root = root.left

            # process element from stack
            root = stack.pop()
            if not head:  # setup head
                head = root

            # double link
            if prev:
                prev.right = root
                root.left = prev

            # go to process next node (root.right), also keep root in prev
            prev = root
            root = root.right

        # link head and tail (circular link)
        prev.right = head
        head.left = prev

        return head


