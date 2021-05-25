"""
678. Valid Parenthesis String
Medium

2413

68

Add to List

Share
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true


Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""
from functools import lru_cache

"""
DP DFS with memoization

dp/dfs recursive call to check each index, and tracking all open paren count (not mateched yet) along the path

( => stack
) => pop one from stack
? try it as (, '', or ')'

time O(3^N)
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        @lru_cache(None)
        def helper(i, c):
            # current index being checked, count of open parenthesis not matched yet
            if i == n:
                return not c
            if s[i] == '(':
                return helper(i+1, c+1)
            elif s[i] == ')':
                if c:
                    return helper(i+1, c-1)
                else:
                    return False
            else: # *
                # treat it as (, '', or )
                if helper(i+1, c+1) or helper(i+1, c) or (c>0 and helper(i+1, c-1)):
                    return True
                else:
                    return False

        return helper(0, 0)

"""
Greedy counting open parenthesis, since * have three possibilities, so it could lead to three possible open parenthesis, we use minopen and maxopen to keep track of possible open parenthesis.

Note that the minopen and maxopen specifies the range of possible open parentheis, and since each character (include *) only change minopen and maxopen by exactly 1, the possible states are continuous range of the entire range of minopen and maxopen

( => open += 1
) => open -= 1
* => three possibilities, so we have minopen -=1, maxopen +=1

Q: we are just counting balances, could we be balancing opening paren to closing paren that happens before it? No because we ensure maxopen >=0 all the time, and we reset minopen if it falls below zero (would be borrowing open paren from future)
"""
class Solution1:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        minopen, maxopen = 0, 0
        for c in s:
            if c == '(':
                minopen += 1
                maxopen += 1
            elif c == ')':
                minopen -= 1
                maxopen -= 1
                if maxopen < 0: # too many closing paren before enough open paren
                    return False
            else: # *
                minopen -= 1 # treat as )
                maxopen += 1 # treat as (

            if minopen < 0: # reset minopen if minopen < 0, so that we don't match open paren to closing paren to its left.
                minopen = 0

        return minopen <= 0


def main():
    sol = Solution()
    assert sol.checkValidString("()") is True, 'fails'

    assert sol.checkValidString("(*)") is True, 'fails'

    assert sol.checkValidString("(*))") is True, 'fails'

if __name__ == '__main__':
   main()