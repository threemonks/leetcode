"""
772. Basic Calculator III
Hard

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Follow up: Could you solve the problem without using built-in library functions.



Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 6-4 / 2 "
Output: 4
Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
Example 4:

Input: s = "(2+6* 3+5- (3*14/7+2)*5)+3"
Output: -12
Example 5:

Input: s = "0"
Output: 0


Constraints:

1 <= s <= 104
s consists of digits, '+', '-', '*', '/', '(', ')' and ' '.
s is a valid expression.

"""

"""
use recursive to handle parenthesis precedence
combine minus sign to number into negative number
*/ has higher binding priority than +-, i.e., if there is operator */, pop out stack top element, calculate */ result, push the result back into stack
both */ and +- follows left to right association order

time O(N)
space O(N)
"""


class Solution:
    def calculate(self, s: str) -> int:
        i = 0

        def calc():
            nonlocal i, s
            stack = []
            operator = '+'
            num = 0
            while i < len(s):
                c = s[i]
                i += 1
                if c in '0123456789':
                    num = num * 10 + int(c)
                elif c == '(':
                    num = calc()
                if c in '+-*/)' or i >= len(s):  # operator, closing paren or end of string
                    if operator == '+':
                        stack.append(num)
                        print('after + %s' % str(stack))
                    elif operator == '-':
                        stack.append(-num)
                        print('after - %s' % str(stack))
                    elif operator == '*':
                        t = stack.pop()
                        stack.append(t * num)
                        print('after * %s' % str(stack))
                    elif operator == '/':
                        numerate = stack.pop()
                        print('numerate=%s num=%s' % (numerate, num))
                        stack.append(-(-numerate // num) if numerate < 0 else numerate // num)  # round towards zero
                        print('after / %s' % str(stack))
                    operator = c
                    if c == ')':
                        break
                    num = 0
                print(stack)

            return sum(stack)

        return calc()

def main():
    sol = Solution()
    assert sol.calculate("1 + 1") == 2, 'fails'

    assert sol.calculate(" 6-4 / 2 ") == 4, 'fails'

    assert sol.calculate("2*(5+5*2)/3+(6/2+8)") == 21, 'fails'

    assert sol.calculate("(2+6* 3+5- (3*14/7+2)*5)+3") == -12, 'fails'

    assert sol.calculate("0") == 0, 'fails'

if __name__ == '__main__':
   main()