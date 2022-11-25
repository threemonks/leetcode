## Template for calculator I, II, III

# One template for calculator I, II, III
"""
https://leetcode.com/problems/basic-calculator-ii/discuss/658480/Python-Basic-Calculator-I-II-III-easy-solution-detailed-explanation

"""
"""
Stack

this solution works for basic calculator (add, substract, parenthesis, space), basic calculator II (add, substract, multiple, divide), basic calculator III (add, substract, multiply, divide, parenthesis)

iterating each char (ignore space), and keep track of last sign (operator), and last number found

c=(: recursively process remaining string
c=): return processed result and index of last processed
c is digit: update variable num
c is operator: update stack by doing
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


"""
Two Stack approach
https://blog.csdn.net/shenjian58/article/details/89849281

输入长度为n的字符串，例如：1+2+3*4*5

输出表达式的值，即：63

“表达式求值”问题，两个核心关键点：

（1）双栈，一个操作数栈，一个运算符栈；

（2）运算符优先级，栈顶运算符，和，即将入栈的运算符的优先级比较：

如果栈顶的运算符优先级低，新运算符直接入栈

如果栈顶的运算符优先级高，先出栈计算，计算结果入栈，新运算符再入栈

如果新运算符和栈顶运算符同级别，栈顶级别算高，先出栈计算，计算结果入栈，新运算符再入栈


这个方法的时间复杂度为O(n)，整个字符串只需要扫描一遍。
————————————————
版权声明：本文为CSDN博主「58沈剑」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/shenjian58/article/details/89849281

"""
""""
Recursive with Stack
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

"""
Stack with recursive call

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