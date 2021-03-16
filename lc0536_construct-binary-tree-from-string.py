"""
536. Construct Binary Tree from String
Medium

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Stack / Tree  String Deserialization

Basic idea is to reverse 

Since the input is preorder traverse of binary tree, it is intutive to reconstruct the tree using recursion, or use stack to simulate the recursion

A few different cases:
1. number string (possible - sign), find following valid part of number (digits), build a new node, peek at stack, if the stack top node has no left child, add this as its left child,
if the stack top node already has left children, then add this as its right child.
then push this node back to stack
2. if opening parenthesis, continue to process next char
3. if closing parenthesis, pop out the stack top (the last child node we added)

At the end, the stack top would have the result root node

time O(N)
"""


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        n = len(s)
        if not n:
            return None
        stack = []

        i = 0
        while i < n:
            c = s[i]
            if c.isdigit() or c == '-':
                # find the entire number
                j = i + 1
                while j < n and s[j].isdigit():
                    j += 1
                # now s[i:j] is the entire number
                node = TreeNode(int(s[i:j]))
                # append this as left child or right child to its parent (stack top element)
                if stack and stack[-1].left is None:
                    stack[-1].left = node  # add as left child
                elif stack:
                    stack[-1].right = node  # add as right child
                stack.append(node)  # add to stack (could be parent for next level nodes)
                i = j  # jump i to next char to be processed
            elif c == ')':
                # finishing up a level, pop it out
                stack.pop()
                i += 1
            else:  # c == '(' # nothing to do
                pass
                i += 1

        return stack.pop()


if __name__ == '__main__':
   main()