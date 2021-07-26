"""
1028. Recover a Tree From Preorder Traversal
Hard

We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.



Example 1:


Input: S = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:


Input: S = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
Example 3:


Input: S = "1-401--349---90--88"
Output: [1,401,null,349,88,90]


Constraints:

The number of nodes in the original tree is in the range [1, 1000].
1 <= Node.val <= 10^9

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
[(1, 0), (2, 1), (3, 2), (4, 2), (5, 1), (6, 2), (7, 2)]
[(1, 0), (2, 1), (3, 2), (4, 2)]
5,1 => 1< stack[-1][1]= 2, so we need to pop out 3,2 and 4,2 attach them back to 2,1 and

stack should hold tree nodes in DFS traverse order
1. if current node depth is lower than node at stack top, add to the stack top node as left children (if none yet), or right children
   then add current node to stack for further processing
2. if current node depth is higher than node at stack top, that means there's no more children for the node at stack top, we can pop it out from stack, until we find parent of current node (identified by depth), then we attach current node as left (or right) child, and push current node into stack

result is stack[0]

"""


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack, num, depth, i = [], None, 0, 0
        while i < len(S):
            if S[i] == '-':
                while i < len(S) and S[i] == '-':
                    depth += 1
                    i += 1
            else:  # digits
                digits = ''
                while i < len(S) and S[i] != '-':
                    digits += S[i]
                    i += 1
                num = int(digits)
                # if lower level node at top of stack, pop it
                while stack and len(stack) > depth:
                    stack.pop()

                node = TreeNode(num)
                if stack and stack[-1].left is None:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node

                # now stack top node is same level or higher than this node
                # push this node to stack, so we might continue processing its children (if any)
                stack.append(node)
                depth = 0

        # only root remains in stack
        return stack[0]
