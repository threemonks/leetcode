"""
32. Longest Valid Parentheses
Hard

5122

188

Add to List

Share
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 3 * 10^4
s[i] is '(', or ')'.
"""
"""
DP

dp[i] := longest valid parentheses ending at i

only dp[i] ending ')' will be non-zero, all dp ending at open paren '(' will be zero
and for dp[i] ending at ')'

Define P = i - dp(i-1) - 1. Then we have the following situation:
...((.....))

...P.......i

P = i - dp[i-1] - 1

String from P+1 to i - 1 indexes including is the longest valid parentheses endind with i-1 place, adding s[P] and s[i] pair, that is dp[i-1]+2, and if the substring immediately before P is also valid, it will contribute a valid length of dp[P-1]

if P >= 0 and s[P] == "(":
    return dp[i-1] + dp[P-1] + 2

if s[i] == ')'
    if s[i-1] == '(':
        dp[i] = dp[i-2]+2
    else# s[i-1] == ')':    
        if P>= 0 and s[p] == '(':  #
            # open paren ( at i-1 consumes length dp[i-1], from i-1-dp[i-1]+1 to i-1
            # and open paren at i consumes open paren at i-1-dp[i-1]
            # and we would need to carry prevous valid substring ending at i-1-dp[i-1]-1 if any
            dp[i] = dp[i-1] + dp[P-1] + 2

else:
    pass # ending ( is invalid

mistakes:
1. if s[i] == ')' and s[i-1] == ')', dp[i] = dp[i-2]+2 # s[i] matches s[i-1]
2. if s[i] == ')' and s[i-1] == ')', check where does valid substring ending at i-1 starts from: i-1-dp[i-1], and its previous valid substring could 
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        dp = [0] * n

        ans = 0
        dp[0] = 0  # single char cannot be valid

        for i in range(1, n):
            # print('i=%s' % i)
            if s[i] == ')':
                if s[i - 1] == '(':  # s[i-1] matches with s[i], add number from i-2
                    dp[i] = (dp[i - 2] if i - 2 >= 0 else 0) + 2
                else:  # s[i-1] == ')', two consecutive closing paren )
                    # check if i-1-dp[i-1] to i-1 is valid substring
                    P = i - 1 - dp[i - 1]
                    if P >= 0 and s[P] == '(':
                        dp[i] = dp[i - 1] + 2 + (dp[P - 1] if P - 1 >= 0 else 0)
                ans = max(ans, dp[i])
            else:  # '(' no valid substring would end with (
                pass
            # print('dp=%s ans=%s' % (dp, ans))

        return ans


"""
Stack

stack at any given point contains an index "after which valid substring could potentially start"

0. init stack with -1
1. for left paren '(', push its index onto stack
2. for right paren ')', pop stack top, subtract index of popped item to get length of a valid string
   if while pop, the stack become empty, push current char ')' into stack

")()())"

Key points:
1. stack stores index of char so we can calculate length of valid substring
1. open paren "(" get pushed into stack
2. close paren will consume one open paren from stack, update answer
   if there's no open paren from stack to consume, push it into stack instead
"""


class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)

        stack = []
        ans = 0
        for i in range(n):
            # print('i=%s stack=%s' % (i, stack))
            if s[i] == '(':
                stack.append(i)
            else:  # )
                if stack and s[stack[-1]] == '(':  # consume a pair, length increase 2
                    stack.pop()
                    ans = max(ans, i - (stack[-1] if stack else -1))
                else:  # ) # cannot consume (empty or not matching open paren), add into stack
                    stack.append(i)

        return ans


"""
One pass
scan left to right, keep count of left and right paren, if more right than left, reset, else when left and right being equal, mark that as an answer
also scan right to left, do the same
take max answer from two passes

Note: scan right to left as well is to handle case with more left then right, and they never equal, so didn't get to count
(((()))
mistakes:
1. check left==right on either ) or (
2. for right to left, cannot do s[::-1], also need to check right parent ) in place of left paren (
"""


class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)

        def calc(s, left_paren='('):
            ans = 0
            left, right = 0, 0
            for i in range(n):
                if s[i] == left_paren:
                    left += 1
                else:  # ')'
                    right += 1

                if right == left:
                    ans = max(ans, 2 * left)
                elif right >= left:  # reset
                    left, right = 0, 0

            return ans

        return max(calc(s), calc(s[::-1], left_paren=')'))


def main():
    sol = Solution()
    assert sol.longestValidParentheses("(()") == 2, 'fails'

    assert sol.longestValidParentheses(")()())") == 4, 'fails'

if __name__ == '__main__':
   main()