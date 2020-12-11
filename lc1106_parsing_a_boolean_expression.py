"""
1106. Parsing A Boolean Expression
Hard

Return the result of evaluating a given boolean expression, represented as a string.

An expression can either be:

"t", evaluating to True;
"f", evaluating to False;
"!(expr)", evaluating to the logical NOT of the inner expression expr;
"&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...;
"|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...


Example 1:

Input: expression = "!(f)"
Output: true
Example 2:

Input: expression = "|(f,t)"
Output: true
Example 3:

Input: expression = "&(t,f)"
Output: false
Example 4:

Input: expression = "|(&(t,f,t),!(t))"
Output: false


Constraints:

1 <= expression.length <= 20000
expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f', ','}.
expression is a valid expression representing a boolean, as given in the description.

"""

"""
operator precedence: () > ! > &|
logic

if ( recursive into call with paren_operator (& or |)
if ) evaluate entire stack and return from recursive call
if t or f, append to stack, apply local operator if necessary
if ,!&| store operator, clear value

"""

class Solution:
    def parseBoolExpr(self, s: str) -> bool:
        i = 0
        def calc(paren_operator=None):
            nonlocal i, s
            stack = [] # holds all boolean values inside a paren
            v = None
            operator = None
            while i != ')' and i < len(s):
                c = s[i]
                i += 1
                print('i=%s c=%s operator=%s stack=%s' % (i, c, operator, str(stack)))
                if c == '(':
                    if operator in '&|':
                        v = calc(paren_operator=operator)
                    elif operator == '!':
                        v = not calc()
                    stack.append(v)
                elif c == 't':
                    v = False if operator == '!' else True
                    stack.append(v)
                elif c == 'f':
                    v = True if operator == '!' else False
                    stack.append(v)
                if c in ',!&|':
                    operator = c
                    v = None
                print(stack)
                if c == ')':
                    break
            if paren_operator == '&':
                return all(stack)
            elif paren_operator == '|':
                return any(stack)
            else: # None
                return stack[0]

        return calc()

def main():
    sol = Solution()
    assert sol.parseBoolExpr("!(f)") is True, 'fails'

    assert sol.parseBoolExpr("|(f,t)") is True, 'fails'

    assert sol.parseBoolExpr("&(t,f)") is False, 'fails'

    assert sol.parseBoolExpr("|(&(t,f,t),!(t))") is False, 'fails'

    assert sol.parseBoolExpr("!(&(!(&(f)),&(t),|(f,f,t)))") is False, 'fails'

    assert sol.parseBoolExpr("!(&(&(!(&(f)),&(t),|(f,f,t)),&(t),&(t,t,f)))") is True, 'fails'

if __name__ == '__main__':
   main()