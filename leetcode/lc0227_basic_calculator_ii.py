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
        if op == '+': stack.append(val)
        elif op == '-': stack.append(-val)
        elif op == '*': stack.append(stack.pop()*val)
        elif op == '/': stack.append(int(stack.pop()/val))

    def calc(self, s, i):

        stack = []
        lastsign = '+'
        num = 0
        while i < len(s):
            c = s[i]
            # print(f'{i = } {c = } {num = }')
            if c.isdigit():
                num = num*10 + int(c)
            elif c == '(':
                # recursive process from here
                num, j = self.calc(s, i+1)
                i = j-1 # there is i +=1 at end of loop
            elif c == ')':
                self.update(stack, lastsign, num)
                return sum(stack), i+1
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


"""
String Stack

observation:

1. for +-*/ use stack, for */, pop out stack top, calculate with next num first, then push it back (*/ has high precedence than +/)
2. for paren () use recursive (or new stack), opening paren cause recursive calculate, closing paren cause result to be pushed back,
   note parenthesis binds tighter than plus or minus
3. space can be removed or ignored
4. test digit .isdigit or '0' <= char <= '9'
5. finally sum all numbers (with signs) in stack

use stack to hold tokens, closing parenthesis will trigger process of all tokens up till opening parenthesis, then replace all elements in stack up to opening parenthesis with the result value, and continue to process stack
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


"""
Stack

1. tokenize/parse so that multi-digits number are parsed properly
2. for number or +/-, push to stack
   for * /, grab one number from stack top, and evaluate result with next number together,
   push result back into stack

3 + 2 * 2

[3, +, 2] 

mistakes:
1. needs to skip whitespace
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

    def calculate(self, s: str) -> int:
        stack = []
        lastsign = '+'
        num = 0
        l = len(s)
        # print(f"{l = }")
        for i, token in enumerate(list(s)):
            if token == ' ':
                continue
            # print(f"{i = } {token = } {lastsign = } {num = }")
            if token.isdigit():  # number
                num = num * 10 + int(token)
            else:
                self.update(stack, lastsign, num)
                lastsign = token
                num = 0
            # print(f"{i = } {token = } {stack = } {lastsign = } {num = }")
        self.update(stack, lastsign, num)

        return sum(stack)

def main():
    sol = Solution()
    assert sol.calculate("3+2*2") == 7, 'fails'

    assert sol.calculate(" 3/2 ") == 1, 'fails'

    assert sol.calculate(" 3+5 / 2 ") == 5, 'fails'

if __name__ == '__main__':
   main()