"""
680. Valid Palindrome II
Easy

2706

175

Add to List

Share
Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.

"""
from functools import lru_cache

"""
Two Pointers

idea: check from left and right into middle, if letter s[i]==s[j], keep move i and j inwards, if i and j not equal, we can either drop s[i], thus check s[i+1:j+1], or drop j and check s[i:j], but we can only drop once

"""


class Solution0:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        @lru_cache(None)
        def dp(i, j, delops=0):
            if i >= j:
                return True

            if (s[i] == s[j] and dp(i + 1, j - 1, delops)) or (
                    delops > 0 and (dp(i + 1, j, delops - 1) or dp(i, j - 1, delops - 1))):
                return True

            return False

        return dp(0, n - 1, delops=1)


"""
Two Pointers

use two pointer without recursive call
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        i, j = 0, n - 1

        while i < j:
            if s[i] != s[j]:
                s1 = s[i:j]  # drop character j
                s2 = s[i + 1:j + 1]  # drop character i
                if s1 == s1[::-1] or s2 == s2[::-1]:
                    return True
                else:
                    return False
            i += 1
            j -= 1

        return True


def main():
    sol = Solution()
    assert sol.validPalindrome(s = "aba") is True, 'fails'

    assert sol.validPalindrome(s = "abca") is True, 'fails'

    assert sol.validPalindrome(s = "abc") is False, 'fails'

if __name__ == '__main__':
   main()