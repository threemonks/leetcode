"""
117. Populating Next Right Pointers in Each Node II
Medium

2631

203

Add to List

Share
Given a binary tree

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



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
DFS recursive call with extra parameter list of possible neighbors
"""


class Solution0:
    def recursive_connect(self, node, nbrs):
        if not node:
            return node
        if nbrs:
            node.next = nbrs[0]
        if node.left:
            left_nbrs = []
            if node.right:
                left_nbrs = [node.right]
            for nbr in nbrs:
                if nbr:
                    if nbr.left:
                        left_nbrs.append(nbr.left)
                    if nbr.right:
                        left_nbrs.append(nbr.right)

            node.left = self.recursive_connect(node.left, left_nbrs)
        if node.right:
            right_nbrs = []
            for nbr in nbrs:
                if nbr:
                    if nbr.left:
                        right_nbrs.append(nbr.left)
                    if nbr.right:
                        right_nbrs.append(nbr.right)

            node.right = self.recursive_connect(node.right, right_nbrs)

        return node

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        return self.recursive_connect(root, [])


"""
BFS Level order traverse
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
            while size:
                cur = q.popleft()
                if q:
                    cur.next = q[0]
                if cur.left:
                    newq.append(cur.left)
                if cur.right:
                    newq.append(cur.right)
                size -= 1

            # copy newq to q
            while newq:
                q.append(newq.popleft())

        return root