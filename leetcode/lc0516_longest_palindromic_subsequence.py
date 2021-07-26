"""
516. Longest Palindromic Subsequence
Medium

https://leetcode.com/problems/longest-palindromic-subsequence/
"""

from functools import lru_cache
from functools import lru_cache

"""
DP top down with memoization
"""

class Solution0:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def helper(i, j):

            if i >= n or j < 0 or i > j:
                return 0
            if i == j:
                return 1
            elif s[i] == s[j]:
                return 2 + helper(i + 1, j - 1)
            else:
                return max(helper(i + 1, j), helper(i, j - 1))

        return helper(0, n - 1)


"""
DP bottom up

dp[i][j] := max length of palindrome subsequence for substring s[i:j] (including i and j)

so the goal is find dp[0][n-1]

base case:

dp[i][i] = 1

transition equation:
 if s[i] == s[j] and i != j:
    dp[i][j] = 2 + dp[i+1][j-1]
else:
    dp[i][j] = max(dp[i+1][j], dp[i][j-1]) # s[i] != s[j]


"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


def main():
    sol = Solution()
    assert sol.longestPalindromeSubseq("bbbab") == 4, 'fails'

    assert sol.longestPalindromeSubseq("cbbd") == 2, 'fails'


if __name__ == '__main__':
   main()