"""
856. Score of Parentheses
Medium

2232

70

Add to List

Share
Given a balanced parentheses string s, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
Example 4:

Input: s = "(()(()))"
Output: 6


Note:

s is a balanced parentheses string, containing only ( and ).
2 <= s.length <= 50

"""
"""
Stack

key idea is to observe each parenthesis has a depth (layer), we should always be calculating score for current level
stack top always has current score of current level
'(' => open new layer with score 0, and push value 0 into stack
')' => pop current value from stack
       if popped value is 0, means this is inner most (), it has value 1, we push 1 back to top of stack
       if popped value is > 0, we double it, and add result back into top of stack

mistakes:
1. need to keep track of layer/depth, and open paren ( opens new layer with score 0
2. stack top hold current score of current layer
3. closing paren would result in new value of 2*stack.pop() or 1, and this result value should be added to stack[-1] after previous pop
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # score of current frame
        for c in s:
            if c == '(':
                stack.append(0)
            else:  # c == ')'
                cur = stack.pop()
                stack[-1] += 2 * cur or 1  # add 2*cur or 1 onto stack top after popped cur

        return stack[-1]


def main():
    sol = Solution()
    assert sol.scoreOfParentheses(s = "()") == 1, 'fails'

    assert sol.scoreOfParentheses(s = "(())") == 2, 'fails'

    assert sol.scoreOfParentheses(s = "()()") == 2, 'fails'

    assert sol.scoreOfParentheses(s = "(()(()))") == 6, 'fails'

if __name__ == '__main__':
   main()