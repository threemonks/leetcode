"""
426. Convert Binary Search Tree to Sorted Doubly Linked List
Medium

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.



Example 1:



Input: root = [4,2,5,1,3]


Output: [1,2,3,4,5]

Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

Example 2:

Input: root = [2,1,3]
Output: [1,2,3]
Example 3:

Input: root = []
Output: []
Explanation: Input is an empty tree. Output is also an empty Linked List.
Example 4:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
All the values of the tree are unique.

"""

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Tree

Need to do an inorder traverse and setup doubly links 
1. inorder traverse, left, root, right
2. needs to use global head and prev to keep track of linked list head, and prev node of current (root) node, to setup double linked list

"""


class Solution:
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


class Solution1:
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


def main():
    sol = Solution()
    sol.treeToDoublyList(Node(4, left=Node(2, left=Node(1), right=Node(3)), right=Node(5)))

if __name__ == '__main__':
   main()