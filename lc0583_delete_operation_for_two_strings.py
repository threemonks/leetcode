"""
583. Delete Operation for Two Strings
Medium

1273

30

Add to List

Share
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.

"""
from functools import lru_cache

"""
dp two string

dp[i][j] := min steps required to make two string equal up to word1[:i] and word2[:j]

top down / recursive
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @lru_cache(None)
        def helper(i, j, steps):
            if i == -1 and j == -1:
                return steps
            elif i == -1 and j > -1:
                return steps + j + 1
            elif j == -1 and i > -1:
                return steps + i + 1
            else:
                if word1[i] == word2[j]:
                    return helper(i - 1, j - 1, steps)
                else:
                    return min(helper(i - 1, j, steps + 1), helper(i, j - 1, steps + 1))

        return helper(len(word1) - 1, len(word2) - 1, 0)


def main():
    sol = Solution()
    assert sol.minDistance("sea", "eat") == 2, 'fails'

if __name__ == '__main__':
   main()