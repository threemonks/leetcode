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
calculator or expression with paren/brace eval

双栈，分别存数字，和，符号
1. 遇到数字，入数字栈
2. 遇到开括号(，入符号栈
3. 遇到闭括号，将符号栈顶所有非开括号(的符号都弹出，和数字栈顶元素结合处理，结果重新入数字栈，直到遇到开括号(
4. 遇到其他符号+-/*，将符号栈顶所有优先级不低于这个符号的符号都弹出，和数字栈顶元素结合处理，结果重新入数字栈
5. 依次弹出并处理所有符号栈顶的符号

结束时，数字栈顶就是结果nums[0]

treat open paren ( as an operator with lowest precedence
close paren ) will trigger processing until find matching open paren (
operator precedence: '*/' > '+-' > '('
*/: 2
+-: 1
(: 0

when encounter closing paren ')', we process all operators from ops stack top (with num from stack nums) until the matching open paren (

Note: (but not applicable here as we don't have such test case)
To deal with "-1+4*3/3/3": add 0 to num stack if the first char is '-';
To deal with "1-(-7)": add 0 to num stack if the first char after '(' is '-'.
"""


class Solution0:
    def calculate(self, s: str) -> int:
        # operator precedence
        precedence = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

        def calc(op, num2, num1):
            # when we pop num from stack nums, we get num2, then num1
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
            elif op == '/':
                return num1 // num2 if num1 > 0 else -((-num1) // num2)

        def helper(s):
            ops, nums = [], []
            num = ''
            i = 0
            while i < len(s):
                c = s[i]
                # print('i=%s c=%s ops=%s nums=%s num=%s' % (i, c, ops, nums, num))
                if c == ' ':  # skip whitespace
                    continue
                elif c.isdigit():
                    while c.isdigit():  # get entire number
                        num += c
                        i += 1
                        if i < len(s):
                            c = s[i]
                        else:
                            c = ''
                    nums.append(int(num))
                    num = ''
                    if i < len(s):
                        # put back this none-digit
                        i -= 1
                elif c == '(':
                    ops.append(c)
                elif c == ')':
                    # if we encounter ), do math until (
                    while ops[-1] != '(':
                        nums.append(calc(ops.pop(), nums.pop(), nums.pop()))
                    # remove (
                    ops.pop()
                elif c in '+-/*':
                    while ops and precedence[ops[-1]] >= precedence[c]:
                        nums.append(calc(ops.pop(), nums.pop(), nums.pop()))
                    ops.append(c)

                i += 1

            # process all remaining items in ops and nums
            while ops:
                # print('ops=%s nums=%s' % (ops, nums))
                nums.append(calc(ops.pop(), nums.pop(), nums.pop()))

            return nums.pop()

        return helper(s)


"""
calculator or expression with paren/brace eval

use stack
( => push into stack, clear cusStr
) => eval curStr, concatenate with stack.pop()
else:
  curStr + s[i]

func eval needs to handle (no paren, but number could have sign)
*/ has higher precedence, needs to pop one from stack, eval with next val, then push back result
+5--433+3*-210-2-3-+3+-5
+5, --433, +3*(-210), -2, -3, -+3, -5,
"""


class Solution1:
    def calculate(self, s: str) -> int:

        # remove white space
        s = ''.join([c for c in s if c != ' '])

        def calc(s):
            """
            evaludate string expression with +-*/ without parenthesis
            """
            if (s[0] != '+' and s[0] != '-'):
                s = '+' + s
            stack = []
            num = ''
            i = 0
            while i < len(s):
                c = s[i]
                print('i=%s c=%s' % (i, c))
                if c == '+' or c == '-':
                    j = i + 1
                    if s[j] == '+' or s[j] == '-':  # this is sign of number
                        j += 1
                    while j < len(s) and s[j].isdigit():
                        j += 1
                    num = s[i + 1:j]
                    i = j - 1
                    if c == '-':
                        stack.append(-int(num))
                    else:
                        stack.append(int(num))
                    num = ''
                elif c == '*' or c == '/':
                    j = i + 1
                    if s[j] == '+' or s[j] == '-':  # this is sign of number
                        j += 1
                    while j < len(s) and s[j].isdigit():
                        j += 1
                    num = s[i + 1:j]
                    i = j - 1
                    prev_num = stack.pop()
                    if c == '*':
                        stack.append(prev_num * int(num))
                    else:  # /
                        stack.append(-(-prev_num // int(num)) if prev_num < 0 else prev_num // int(num))
                    num = ''

                print('stack=%s' % str(stack))
                i += 1

            if num:  # last number
                stack.append(int(num))

            return sum(stack)

        cur_str = ''
        stack = []  # holding string elements with parenthesis evaluated first
        for c in s:
            if c == '(':
                stack.append(cur_str)
                cur_str = ''
            elif c == ')':
                cur_res = calc(cur_str)
                cur_str = stack.pop() + str(cur_res)
            else:
                cur_str += c
        print('cur_str=%s' % cur_str)
        return calc(cur_str)


"""
use recursive to handle parenthesis precedence
combine minus sign to number into negative number
*/ has higher binding priority than +-, i.e., if there is operator */, pop out stack top element, calculate */ result, push the result back into stack
both */ and +- follows left to right association order

time O(N)
space O(N)
"""


class Solution2:
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
                        # print('after + %s' % str(stack))
                    elif operator == '-':
                        stack.append(-num)
                        # print('after - %s' % str(stack))
                    elif operator == '*':
                        t = stack.pop()
                        stack.append(t * num)
                        # print('after * %s' % str(stack))
                    elif operator == '/':
                        numerate = stack.pop()
                        print('numerate=%s num=%s' % (numerate, num))
                        stack.append(-(-numerate // num) if numerate < 0 else numerate // num)  # round towards zero
                        # print('after / %s' % str(stack))
                    operator = c
                    if c == ')':
                        break
                    num = 0
                # print(stack)

            return sum(stack)

        return calc()


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
    sol = Solution()
    assert sol.calculate("1 + 1") == 2, 'fails'

    assert sol.calculate(" 6-4 / 2 ") == 4, 'fails'

    assert sol.calculate("2*(5+5*2)/3+(6/2+8)") == 21, 'fails'

    assert sol.calculate("(2+6* 3+5- (3*14/7+2)*5)+3") == -12, 'fails'

    assert sol.calculate("2-(5-6)") == 3, 'fails'

    assert sol.calculate("0") == 0, 'fails'

if __name__ == '__main__':
   main()