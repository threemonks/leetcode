"""
1216. Valid Palindrome III
Hard

202

5

Add to List

Share
Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.



Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.


Constraints:

1 <= s.length <= 1000
s has only lowercase English letters.
1 <= k <= s.length

"""
import collections
import math
from functools import lru_cache
from typing import List

"""
dp two string s and s[::-1] / two pointers

dp topdown recursive w/ memoization

time O(m^2)
space O(m^2)
"""


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @lru_cache(None)
        def helper(i, j, removes):
            if removes > k:
                return False
            if i >= j:
                return removes <= k
            if s[i] == s[j]:
                i1 = i
                j1 = j
                while i1 < j1 and s[i1] == s[j1]:
                    i1 += 1
                    j1 -= 1
                return helper(i1, j1, removes)
            else:
                return helper(i, j - 1, removes + 1) or helper(i + 1, j, removes + 1)

        return helper(0, len(s) - 1, 0)

def main():
    sol = Solution()
    assert sol.isValidPalindrome("abcdeca", 2) is True, 'fails'

if __name__ == '__main__':
   main()