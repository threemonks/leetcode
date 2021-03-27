"""
115. Distinct Subsequences
Hard

Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.



Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag


Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""
"""
DP Two Series （双序列-动态规划）

dp[i][j] := # of distinct subsequence up to s[:i] t[:j]

dp[0][0] = 1

if s[i-1] == t[j-1]: # match, can choose to use both s[i-1] and t[j-1], thus both index advance, or ignore s[i-1]
    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
else: # don't match, can only choose to ignore s[i-1]
    dp[i][j] = dp[i-1][j]

"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = 1  # empty is subseq of empty

        for i in range(1, m):
            dp[i][0] = 1  # if t is empty, s always has distinct empty subseq

        # dp[0][i] = 0 # if s is empty, t is not empty, no subseq (default=0)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[
                    j - 1]:  # match, we can choose match and advance both index, or ignore s[i-1] thus advance i only
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:  # not match, ignore s[i-1], same # subseq
                    dp[i][j] = dp[i - 1][j]
                # print('i=%s j=%s dp[i][j]=%s' % (i, j, dp[i][j]))

        # print(dp)
        return dp[m][n]


def main():
    sol = Solution()
    assert sol.numDistinct(s = "rabbbit", t = "rabbit") == 3, 'fails'

    assert sol.numDistinct(s = "babgbag", t = "bag") == 5, 'fails'


if __name__ == '__main__':
   main()