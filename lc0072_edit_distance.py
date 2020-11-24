"""
72. Edit Distance
Hard

4743

64

Add to List

Share
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

"""
import math
from functools import lru_cache
from typing import List

"""
dp with two series

dp[i][j] := minmum operation required to convert word1[:i] to word2[:j]

if word1[i] == word2[j]:
    dp[i][j] = dp[i-1][j-1]
elif word1[i] != word2[j]:
    dp[i][j] = min(dp[i-1][j-1]+1, # replace
            dp[i-1][j], # insert
            dp[i][j+1], # delete
            )

time O(m*n)
space O(m*n)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[math.inf for _ in range(n+1)] for _ in range(m+1)]

        word1 = '#' + word1
        word2 = '#' + word2
        dp[0][0] = 0

        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
                print('i=%s j=%s word1[i]=%s word2[j]=%s dp[i][j]=%s' %(i, j, word1[i], word2[j], dp[i][j]))

        return dp[m][n]

def main():
    sol = Solution()
    assert sol.minDistance("horse", "ros") == 3, 'fails'

    assert sol.minDistance("intention", "execution") == 5, 'fails'

    assert sol.minDistance("a", "ab") == 1, 'fails'

if __name__ == '__main__':
   main()