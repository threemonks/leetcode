"""
921. Minimum Add to Make Parentheses Valid
Medium

1462

90

Add to List

Share
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.



Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
Example 3:

Input: s = "()"
Output: 0
Example 4:

Input: s = "()))(("
Output: 4


Constraints:

1 <= s.length <= 1000
s[i] is either '(' or ')'.
"""
"""
Stack

Use stack to keep track of not closed open parens, and use unmatched_close to keep track of extra closing paren that has no corresponding open ones

note:
1. when finish iterating s, there might be unmatched open parens in stack
"""


class Solution0:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        unmatched_close = 0
        ans = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    unmatched_close += 1
                    ans = max(ans, unmatched_close)

        # if stack, that's extra unmatched open
        if stack:
            ans += len(stack)

        return ans


"""
Greedy

count unmatched close and unmatched open (closing paren cancels unmatched open first, if no more unmatched open, then it increase unmatched close)

note:
1. when finish iterating s, there might be left unbalanced open parens
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unmatched_open = 0
        unmatched_close = 0
        ans = 0
        for c in s:
            if c == '(':
                unmatched_open += 1
            elif c == ')':
                if unmatched_open > 0:
                    unmatched_open -= 1
                else:
                    unmatched_close += 1

        return unmatched_open + unmatched_close


def main():
    sol = Solution()
    assert sol.minAddToMakeValid(s = "())") == 1, 'fails'

    assert sol.minAddToMakeValid(s = "(((") == 3, 'fails'

    assert sol.minAddToMakeValid(s = "()") == 0, 'fails'

    assert sol.minAddToMakeValid(s = "()))((") == 4, 'fails'

if __name__ == '__main__':
   main()