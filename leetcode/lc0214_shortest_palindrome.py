"""
214. Shortest Palindrome
Hard

Given a string s, you can convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"


Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
"""
"""
String Rolling Hash/Rabin-Karp
observation:
Shortest palindrome by adding minimum into front <=> find longest palindrome prefix substring, then reversing the remaining suffix and add it to the front

rolling hash / Rabin-Karp
calculate rolling hash of a given prefix from left to right decreasing power, and also from left to right with increasing power, if these two hashes equal, that is a palindrome

Note: we need to accumulatively calculate coefficients (al = base**i) for nums[i] in h2 calculation as part of the loop, instead of calculating base**i directly inside the loop in each step, as that would TLE.

"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(set(s)) == 1: return s
        n = len(s)
        nums = [ord(c) - ord('a') for c in s]
        base = 26
        MOD = 10 ** 9 + 7

        al = 1
        res = 0
        h1, h2 = 0, 0
        for i in range(n):
            h1 = (h1 * base + nums[i]) % MOD
            h2 = (h2 + nums[i] * al) % MOD
            al = (al * base) % MOD
            if h1 == h2:
                res = max(res, i)

        return s[res + 1:][::-1] + s


def main():
    sol = Solution()
    assert sol.shortestPalindrome("aacecaaa") == "aaacecaaa", 'fails'

    assert sol.shortestPalindrome("abcd") == "dcbabcd", 'fails'


if __name__ == '__main__':
   main()