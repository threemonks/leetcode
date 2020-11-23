"""
1312. Minimum Insertion Steps to Make a String Palindrome
Hard

548

6

Add to List

Share
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.



Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we don't need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
Example 4:

Input: s = "g"
Output: 0
Example 5:

Input: s = "no"
Output: 1


Constraints:

1 <= s.length <= 500
All characters of s are lower case English letters.

"""
import collections
import math
from functools import lru_cache
from typing import List

"""
dp two strings (two pointers)
time O(n^2)
space O(n^2)
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        @lru_cache(None)
        def helper(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                i1, j1 = i, j
                while i1 < j1 and s[i1] == s[j1]:
                    i1 += 1
                    j1 -= 1
                return helper(i1, j1)
            else:
                return min(helper(i + 1, j) + 1, helper(i, j - 1) + 1)

        return helper(0, len(s) - 1)

def main():
    sol = Solution()
    assert sol.minInsertions("zzazz") == 0, 'fails'

    assert sol.minInsertions("mbadm") == 2, 'fails'

    assert sol.minInsertions("leetcode") == 5, 'fails'

    assert sol.minInsertions("g") == 0, 'fails'

    assert sol.minInsertions("no") == 1, 'fails'

if __name__ == '__main__':
   main()