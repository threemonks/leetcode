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
Stack / Math

1. parenthesis binds tighter than plus or minus
2. spaces can be ignored

use stack to hold tokens, closing parenthesis will trigger process of all tokens up till opening parenthesis, then replace all elements in stack up to opening parenthesis with the result value, and continue to process stack
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

use stack to hold tokens, closing parenthesis will trigger process of all tokens up till opening parenthesis, then replace all elements in stack up to opening parenthesis with the result value, and continue to process stack
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


"""
Stack - to hold temporary values that need to hold until sub-expressions are evaluated

Use stack without recursive call

1. itreate the expression one char at a time, if we encounter digit, we continue to get the entire number
2. if char is + or -, we first evaluate the expression to left, and then save this sign for the next evaluation
3. if char is opening paren '(', we push both result so far and sign onto stack, and start a fresh as if we are calculating a new expression
4. if char is closing paren ')', we first calculate the expression to the left, the result would be result of expression within parenthesis that just concluded. This result is then multiplied with the sign, if there is one on top of stack, because a sign is always applied to the operand to its right, and we push the sign to stack if a parenthesis (sub-expression) follows the sign. The result of this mulitplication is then added to the next element on top of stack.

Note in this approach most expression are evaluated on-the-go, operands and signs are pushed to stack when sub-expression needs to be evaled first 

"""


class Solution:

    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        i = 0
        operand = 0
        sign = 1
        res = 0  # on-going result
        while i < n:
            c = s[i]
            # print('i=%s c=%s sign=%s operand=%s stack=%s res=%s' % (i, c, sign, operand, stack, res))
            # skip whitespace
            if c == ' ':
                i += 1
                continue
            if c.isdigit():
                # get the entire number
                j = i
                while j < n and s[j].isdigit():
                    j += 1
                # now s[i:j] is the entire number
                operand = int(s[i:j])
                i = j
            elif c == '+':
                # evaludate expression to the left, with result, sign operand
                res += sign * operand
                sign = 1  # save sign for next
                operand = 0  # reset operand
                i += 1
            elif c == '-':
                # evaludate expression to the left, with result, sign operand
                res += sign * operand
                sign = -1  # save sign for next
                operand = 0  # reset operand
                i += 1
            elif c == '(':
                # push result and sign onto stack, for later
                # push result first, then sign
                stack.append(res)
                stack.append(sign)

                # then reset sign and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0
                i += 1
            elif c == ')':
                # evaluate expression to left, with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of paren
                # its result is multiplied with sign on top of stack
                res *= stack.pop()  # stack pop 1, which is the sign to apply to the result of this paren

                # then add the result to next operand on top of stack
                res += stack.pop()  # stack pop 2, operand to add with result

                # reset operand
                sign = 1
                operand = 0
                i += 1

            # print('*** i=%s c=%s sign=%s operand=%s stack=%s res=%s' % (i, c, sign, operand, stack, res))

        return res + sign * operand


"""
Stack

this solution works for basic calculator (add, substract, parenthesis, space), basic calculator II (add, substract, multiple, divide), basic calculator III (add, substract, multiply, divide, parenthesis) 

iterating each char (ignore space), and keep track of last sign (operator), and last number found

c=(: recursively process remaining string
c=): return processed result and index of last processed
c is digit: update variable num
c is operator: update stack
  +: add num into stack
  -: add -num into stack
  *: pop stack top, multiply with num, push result back into stack
  /: pop stack top, divide by num, push result back into stack

"""


class Solution:
    def update(self, stack, op, val):
        if op == '+':
            stack.append(val)
        elif op == '-':
            stack.append(-val)
        elif op == '*':
            stack.append(stack.pop() * val)
        elif op == '/':
            stack.append(int(stack.pop() / val))

    def calc(self, s, i):

        stack = []
        lastsign = '+'
        num = 0
        while i < len(s):
            c = s[i]
            # print(f'{i = } {c = } {num = }')
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '(':
                # recursive process from here
                num, j = self.calc(s, i + 1)
                i = j - 1  # there is i +=1 at end of loop
            elif c == ')':
                self.update(stack, lastsign, num)
                return sum(stack), i + 1
            elif c in '+-*/':
                self.update(stack, lastsign, num)
                lastsign = c
                num = 0
            # elif c == ' ':
            #     pass
            i += 1
            # print(f'{i = } {c = } {stack = } {num = }')

        self.update(stack, lastsign, num)

        return sum(stack), i

    def calculate(self, s: str) -> int:
        return self.calc(s, 0)[0]


def main():
    sol = Solution1()
    assert sol.calculate("1 + 1") == 2, 'fails'

    assert sol.calculate(" 2-1 + 2 ") == 3, 'fails'

    assert sol.calculate("(1+(4+5+2)-3)+(6+8)") == 23, 'fails'

    assert sol.calculate("2-(5-6)") == 3, 'fails'

if __name__ == '__main__':
   main()