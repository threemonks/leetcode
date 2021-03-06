"""
116. Populating Next Right Pointers in Each Node
Medium

3768

174

Add to List

Share
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


"""
DFS

dfs recursive call with extra parameter neighbor, to explore left child with right child as neighbor, and to expore right child with nbr.left if an parameter nbr was passed in, else no nbr to pass when exploring right child

"""


class Solution0:
    def recursive_connect(self, node, nbr):
        if not node:
            return node
        if node.left:
            node.left.next = node.right
            self.recursive_connect(node.left, node.right)
        if node.right:
            if nbr:
                node.right.next = nbr.left
            self.recursive_connect(node.right, None if not nbr else nbr.left)

        return node

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        return self.recursive_connect(root, None)


"""
Tree Level Order traverse
"""
from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])

        while q:
            size = len(q)
            newq = deque([])
            while size:  # finish exploring one level
                cur = q.popleft()
                if q:
                    cur.next = q[0]
                if cur.left:
                    newq.append(cur.left)
                if cur.right:
                    newq.append(cur.right)
                size -= 1

            while newq:  # copy newq into q for this level
                q.append(newq.popleft())

        return root