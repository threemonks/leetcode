"""
1143. Longest Common Subsequence
Medium

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.



If there is no common subsequence, return 0.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

"""
import math
from functools import lru_cache
from typing import List

"""
make dp 1+n, i.e., add dp[0][0] as sentinel point to avoid handling boundary case
dp[i][j] := longest common subsequence covering string text1[:i] and text2[:j]

dp[i][j] = dp[i-1][j-1]+1 if text1[i-1]==text2[j-1] # can extend one to left
else max(dp[i-1][j], dp[i][j-1]) # cannot extend, keep length from previous check point

"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

def main():
    sol = Solution()
    assert sol.longestCommonSubsequence("abcde", "ace") == 3, 'fails'

    assert sol.longestCommonSubsequence("abc", "abc") == 3, 'fails'

    assert sol.longestCommonSubsequence("abc", "def") == 0, 'fails'

if __name__ == '__main__':
   main()