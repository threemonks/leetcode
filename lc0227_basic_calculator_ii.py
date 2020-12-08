"""
227. Basic Calculator II
Medium

Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.

"""
"""
observation:

1. for +-*/ use stack, for */, pop out stack top, calculate with next num first, then push it back (*/ has high precedence than +/)
2. for paren () use recursive (or new stack), opening paren cause recursive calculate, closing paren cause result to be pushed back,
   note parenthesis binds tighter than plus or minus
3. space can be removed or ignored
4. test digit .isdigit or '0' <= char <= '9'
5. finally sum all numbers (with signs) in stack

use stack to hold tokens, closing parenthesis will trigger process of all tokens up till opening parenthesis, then replae all elements in stack up to opening parenthesis with the result value, and continue to process stack
"""


class Solution:
    def calculate(self, s: str) -> int:
        i = 0

        def calc():
            nonlocal s, i
            stack = []
            num = 0
            operator = '+'

            while i < len(s):
                c = s[i]
                i += 1
                if c in '0123456789':
                    num = num * 10 + int(c)
                elif c == '(':
                    num = calc()
                if c in '+-*/)' or i >= len(s):  # operator, closing paren or last char
                    if operator == '+':
                        stack.append(num)
                        operator = c
                    elif operator == '-':
                        stack.append(-num)
                        operator = c
                    elif operator == '*':
                        stack.append(stack.pop() * num)
                        operator = c
                    elif operator == '/':
                        numerate = stack.pop()
                        stack.append(-(
                                    -numerate // num) if numerate < 0 else numerate // num)  # handles negative integer divison round towards zero
                        operator = c
                    num = 0

                    if c == ')':
                        break  # return from recursive

            return sum(stack)

        return calc()

def main():
    sol = Solution()
    assert sol.calculate("3+2*2") == 7, 'fails'

    assert sol.calculate(" 3/2 ") == 1, 'fails'

    assert sol.calculate(" 3+5 / 2 ") == 5, 'fails'

if __name__ == '__main__':
   main()