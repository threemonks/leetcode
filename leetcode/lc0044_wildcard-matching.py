"""
44. Wildcard Matching
Hard

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input: s = "acdcb", p = "a*c?b"
Output: false


Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.

"""

from functools import lru_cache

"""
DP Recursive 动态规划

Note: * match empty or any chars (match any chars first seems faster)

time O(SP)
space O(SP)
"""


class Solution0:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def helper(s, p):
            # print('s=%s p=%s' % (s, p))
            if not s:
                if not p or (p[0] == '*' and len(set(p)) == 1):  # if s is empty, only match empty p or 1 or more *
                    return True
                else:
                    return False
            # s not empty
            if not p:
                return False
            # both s and p not empty
            if s[0] == p[0] or p[0] == '?':  # single char match or ?
                i, j = 0, 0
                while i < len(s) and j < len(p) and (s[i] == p[j] or p[j] == '?'):
                    i += 1
                    j += 1
                return helper(s[i:], p[i:])
            elif p[0] == '*':
                # * match any char or empty
                return helper(s[1:], p) or helper(s, p[1:])
            else:  # no wild char, and s[0] != p[0]
                return False

        return helper(s, p)


"""
DP Two Series 双序列动态规划 bottom up

dp[i][j] := up to s[i-1] [j-1], is it match or not?

base case
dp[0][0] = True # empty matches empty
dp[0][j] = dp[0][j-1]|p[j-1]=='*' # * matches anything, including empty

transition:

if s[i-1] == p[j-1] or p[j-1] == '?':
    dp[i][j] = dp[i-1][j-1]
elif p[j-1] == '*':
    dp[i][j] = dp[i-1][j] # * matches anything
              or dp[i][j-1] # * matches empty


time O(SP)
space O(SP)
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        # base case
        dp[0][0] = True  # empty matches empty
        for j in range(1, n + 1):
            if p[j - 1] == '*':  # * matches anything
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]

        # print(dp)
        return dp[m][n]


def main():
    sol = Solution()
    assert sol.isMatch(s = "aa", p = "a") is False, 'fails'

    assert sol.isMatch(s = "aa", p = "*") is True, 'fails'

    assert sol.isMatch(s = "cb", p = "?a") is False, 'fails'

    assert sol.isMatch(s = "adceb", p = "*a*b") is True, 'fails'

    assert sol.isMatch(s = "acdcb", p = "a*c?b") is False, 'fails'

if __name__ == '__main__':
   main()