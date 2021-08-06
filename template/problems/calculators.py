# Template for calculator I, II, III
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