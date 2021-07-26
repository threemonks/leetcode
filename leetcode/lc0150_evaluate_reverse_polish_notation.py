"""
150. Evaluate Reverse Polish Notation
Medium

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
from typing import List

"""
Eval with stack

Process Reverse Polish Notation from left to right, use stack to hold values, for each operator, we pop two values from stack and apply the operator, then push result back to stack

Infix Notation

Reverse Polish Notation
  While there are operators remaining in the list, find the left-most operator. Apply it to the 2 numbers immediately before it, and replace all 3 tokens (the operator and 2 numbers) with the result.

Note:
    python integer division does not truncate towards 0: -1//2 = -1

stack = list()
for each token in tokens:
    if token is a number:
        stack.append(token)
    else (token is operator):
        n2, n1 = stack.pop(), stack.pop()
        stack.push(apply_operator(token, n1, n2))

return stack.pop()

time O(N)
space O(N)

mistakes:
1. Reverse Polish Notation is not a "reverse" form of Polish Notation
2. Reverse Polish Notation should be processed from left to right, if number, push to stack, if operator, pop two numbers from stack and apply operator, then push result number back into stack
3. operand needs to be converted from string to int
4. needs to convert temp calculate result back to string before pushing back into stack
5. needs to set op, opa1, opa2 back to None after calculating and pushing result back into stack
6. integer division truncate towards zero - cast to int after float division int(v1/v2)
7. order of operand1 and operand2: ["12", "7", "-"] => 12 - 7 = 5

"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()

        for t in tokens:
            if t in '+-/*':
                v2, v1 = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(v1 + v2)
                elif t == '-':
                    stack.append(v1 - v2)
                elif t == '*':
                    stack.append(v1 * v2)
                elif t == '/':
                    stack.append(int(v1 / v2))
            else:
                stack.append(int(t))

        return stack[0]

def main():
    sol = Solution()
    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9, 'fails'

    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6, 'fails'


if __name__ == '__main__':
   main()