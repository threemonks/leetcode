"""
1771. Maximize Palindrome Length From Subsequences
Hard

https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/

"""
from functools import lru_cache

"""
concat word1 and word2, find longest palindrome subsequence, and then filter to keep only valid ones

how to check if we have at least one char from each word?
the counts in dp[i][sz1+j] are the ones counting at least one char from word1, and at least one char from word2

time O((M+N)^2)
space O((M+N)^2
"""


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        word = word1 + word2
        n = len(word)

        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for i in range(n, -1, -1):
            for j in range(i + 1, n):
                if word[i] == word[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        ans = 0
        sz1, sz2 = len(word1), len(word2)
        for i in range(sz1):
            for j in range(sz2):
                if word1[i] == word2[j]:  # make sure we have at least one char from each word
                    ans = max(ans, dp[i][sz1 + j])

        return ans

def main():
    sol = Solution()
    assert sol.longestPalindrome(word1 = "cacb", word2 = "cbba") == 5, 'fails'

    assert sol.longestPalindrome(word1 = "ab", word2 = "ab") == 3, 'fails'

    assert sol.longestPalindrome(word1 = "aa", word2 = "bb") == 0, 'fails'

if __name__ == '__main__':
   main()