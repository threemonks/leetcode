"""
224. Basic Calculator
Hard

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

"""

"""
1. parenthesis binds tighter than plus or minus
2. spaces can be ignored

use stack to hold tokens, closing parenthesis will trigger process of all tokens up till opening parenthesis, then replae all elements in stack up to opening parenthesis with the result value, and continue to process stack
"""


class Solution:
    def calculate(self, s: str) -> int:
        tokens = []
        number = ''
        for c in s:
            if c in '0123456789':
                number += c
            else:
                if number:
                    tokens.append(number)
                number = ''
                if c in '()+-':  # ignoring whitespace or other invalid characters
                    tokens.append(c)

        if number:  # remaining number char
            tokens.append(number)

        def calc_expr(sa):  # no parenthesis or whitespace
            assert '(' not in sa and ')' not in sa, 'cannot handle () in %s' % sa
            if len(sa) == 1:
                return int(sa[0])
            else:
                num, op = None, None
                for s1 in sa:
                    if s1 == '+' or s1 == '-':
                        op = s1
                    elif all([(c in '-0123456789') for c in s1]):
                        if num is not None:
                            if op == '+':
                                num = num + int(s1)
                            elif op == '-':
                                num = num - int(s1)
                        else:  # num is None
                            num = int(s1)

                return num

        stack = []
        for v in tokens:
            if v == ')':
                expr = []
                while stack and stack[-1] != '(':
                    expr.append(stack.pop())
                if stack:
                    stack.pop()
                stack.append(str(calc_expr(expr[::-1])))
            else:
                stack.append(v)

        return calc_expr(stack)


"""
observation:

1. for +-*/ use stack
2. for paren () use recursive (or new stack), opening paren cause recursive calculate, closing paren cause result to be pushed back,
   note parenthesis binds tighter than plus or minus
3. space can be removed or ignored
4. test digit .isdigit or '0' <= char <= '9'
5. finally sum all numbers (with signs) in stack

use stack to hold tokens, closing parenthesis will trigger process of all tokens up till opening parenthesis, then replae all elements in stack up to opening parenthesis with the result value, and continue to process stack
"""


class Solution1:

    def calculate(self, s: str) -> int:
        i = 0

        def calc() -> int:
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
                if c in '+-)' or i >= len(s):  # operator or closing paren or last char
                    if operator == '+':
                        stack.append(num)
                        operator = c
                    elif operator == '-':
                        stack.append(-num)
                        operator = c
                    num = 0
                    # print('i=%s stack=%s' % (i, str(stack)))
                    if c == ')':
                        break

            return sum(stack)

        return calc()

def main():
    sol = Solution1()
    assert sol.calculate("1 + 1") == 2, 'fails'

    assert sol.calculate(" 2-1 + 2 ") == 3, 'fails'

    assert sol.calculate("(1+(4+5+2)-3)+(6+8)") == 23, 'fails'

    assert sol.calculate("2-(5-6)") == 3, 'fails'

if __name__ == '__main__':
   main()