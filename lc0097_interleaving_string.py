"""
97. Interleaving String
Hard

1719

97

Add to List

Share
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.



Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true


Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lower-case English letters.

"""
import math
from functools import lru_cache
from typing import List

"""
dp with two strings

dp[i][j] := interleaving or not for s1[:i], s2[:j] to interleave and get s3[:i+j]


dp[i][j] = dp[i-1][j] is True && s1[i] == s3[i+j]
           or dp[i][j-1] is True && s2[j] == s3[i+j]

# define dp as (m+1)*(n+1) and add leading dummy char to both string to avoid special handling edge case

time O(m*n)
space O(m*n)
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m + n != len(s3):
            return False

        # define dp to be (m+1)*(n+1)
        # and add leading character to s1, s2, and s3 to avoid having to deal with special edge case
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        s1 = "#" + s1
        s2 = "#" + s2
        s3 = "#" + s3

        # when s1, s2 and s3 all empty, result is True
        dp[0][0] = True

        # we need to deal boundary case i=0 and j=0 first
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i] == s3[i]

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j] == s3[j]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i] == s3[i + j] and dp[i - 1][j]:
                    dp[i][j] = True
                elif s2[j] == s3[i + j] and dp[i][j - 1]:
                    dp[i][j] = True

        return dp[-1][-1]

"""
DFS recursive with memoization
"""
class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l = len(s1)
        m = len(s2)
        n = len(s3)

        @lru_cache(None)
        def helper(i, j, k):
            """
            i: the index we are checking in s1
            j: the index we are checking in s2
            k: the index we are checking in s3
            """
            if i == l and j == m and k == n:
                return True
            if k == n and not (i == l and j == m):
                return False
            if i < l and j < m and k < n and s1[i] == s3[k] and s2[j] == s3[k]:
                return helper(i + 1, j, k + 1) or helper(i, j + 1, k + 1)
            elif i < l and k < n and s1[i] == s3[k]:
                return helper(i + 1, j, k + 1)
            elif j < m and k < n and s2[j] == s3[k]:
                return helper(i, j + 1, k + 1)

        return bool(helper(0, 0, 0))

def main():
    sol = Solution1()
    assert sol.isInterleave("aabcc", "dbbca", "aadbbcbcac") is True, 'fails'

    assert sol.isInterleave("aabcc", "dbbca", "aadbbbaccc") is False, 'fails'

    assert sol.isInterleave("", "", "") is True, 'fails'

if __name__ == '__main__':
   main()