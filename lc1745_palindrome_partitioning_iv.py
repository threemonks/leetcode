"""
https://leetcode.com/problems/palindrome-partitioning-iv/

1745. Palindrome Partitioning IV
Hard

Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​

A string is said to be palindrome if it the same string when reversed.



Example 1:

Input: s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.
Example 2:

Input: s = "bcbddxy"
Output: false
Explanation: s cannot be split into 3 palindromes.


Constraints:

3 <= s.length <= 2000
s​​​​​​ consists only of lowercase English letters.
"""

from functools import lru_cache

"""
DP String
use dp to break this into check for one regular string palindrome checking (varying all possible string lengths), and another palindrome partitioning problem of 2 partitions
and recursively break the palindrome partitioning of 2 partitions into two regular palindrome checking problems

transition:

def dp(s, k):
    loop i from 0 to len(s):
        if s[:i+1] is palindrome and dp(s[i+1:], k-1) is true:
            return true
        else:
            return False

"""


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)

        @lru_cache(None)
        def helper(ns, k):
            if k == 1:
                return ns == ns[::-1]
            for i in range(len(ns) - 1):
                if ns[:i + 1] == ns[:i + 1][::-1] and helper(ns[i + 1:], k - 1):
                    return True

            return False

        return helper(s, 3)


def main():
    sol = Solution()
    assert sol.checkPartitioning("abcbdd") == True, 'fails'

    assert sol.checkPartitioning("bcbddxy") == False, 'fails'


if __name__ == '__main__':
   main()