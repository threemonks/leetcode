"""
1597. Build Binary Expression Tree From Infix Expression
Hard

80

16

Add to List

Share
A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with 2 children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

For each internal node with operator o, the infix expression that it represents is (A o B), where A is the expression the left subtree represents and B is the expression the right subtree represents.

You are given a string s, an infix expression containing operands, the operators described above, and parentheses '(' and ')'.

Return any valid binary expression tree, which its in-order traversal reproduces s after omitting the parenthesis from it (see examples below).

Please note that order of operations applies in s. That is, expressions in parentheses are evaluated first, and multiplication and division happen before addition and subtraction.

Operands must also appear in the same order in both s and the in-order traversal of the tree.



Example 1:


Input: s = "3*4-2*5"
Output: [-,*,*,3,4,2,5]
Explanation: The tree above is the only valid tree whose inorder traversal produces s.
Example 2:


Input: s = "2-3/(5*2)+1"
Output: [+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]
Explanation: The inorder traversal of the tree above is 2-3/5*2+1 which is the same as s without the parenthesis. The tree also produces the correct result and its operands are in the same order as they appear in s.
The tree below is also a valid binary expression tree with the same inorder traversal as s, but it not a valid answer because it does not evaluate to the same value.

The third tree below is also not valid. Although it produces the same result and is equivalent to the above trees, its inorder traversal does not produce s and its operands are not in the same order as s.

Example 3:

Input: s = "1+2+3+4+5"
Output: [+,+,5,+,4,null,null,+,3,null,null,1,2]
Explanation: The tree [+,+,5,+,+,null,null,1,2,3,4] is also one of many other valid trees.


Constraints:

1 <= s.length <= 1000
s consists of digits and the characters '+', '-', '*', and '/'.
Operands in s are exactly 1 digit.
It is guaranteed that s is a valid expression.
"""

# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

observation:

use two stacks, one for operators, one for numbers

operator precedence:
*/: 2
+-: 1
(: 0

1. for digit, push node into nodes
2. for open paren (, store into ops
3. for close paren ), process (build node with two node from stack nodes) for all operator on top of stack ops until we meet with open paren (
4. for operators op, process all operators (build node with two node from nodes) on top of stack ops that is same or higher precedence than this operator op, and push result back into stack nodes
5. after we finish iterating input s, we need to process (build node with node from stack nodes) any operator in stack ops

at end, nodes[0] is the result
"""
class Solution:
    def expTree(self, s: str) -> 'Node':
        precedence = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

        def build(op, node2, node1):
            # nums is stack, with node1 at bottom, node2 above, so will pop out node2 first
            return Node(op, left=node1, right=node2)

        def helper(s):
            ops, nodes = [], []
            i = 0
            while i < len(s):
                c = s[i]
                # print('i=%s c=%s ops=%s nodes=%s' % (i, c, ops, ','.join([str(n.val) for n in nodes])))
                if c.isdigit():
                    nodes.append(Node(c))  # always single digit number
                elif c == '(':
                    ops.append(c)
                elif c == ')':
                    while ops[-1] != '(':
                        nodes.append(build(ops.pop(), nodes.pop(), nodes.pop()))
                    ops.pop()  # remove '('
                elif c in '+-/*':
                    while ops and precedence[ops[-1]] >= precedence[c]:
                        nodes.append(build(ops.pop(), nodes.pop(), nodes.pop()))
                    ops.append(c)

                i += 1

            # process remaining items in ops and nodes
            while ops:
                nodes.append(build(ops.pop(), nodes.pop(), nodes.pop()))

            # print(nodes)
            return nodes[0]

        return helper(s)


def main():
    sol = Solution()
    sol.expTree(s = "3*4-2*5")

if __name__ == '__main__':
   main()