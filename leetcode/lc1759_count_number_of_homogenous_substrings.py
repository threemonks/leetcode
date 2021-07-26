"""
1759. Count Number of Homogenous Substrings
Medium

Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
Example 2:

Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".
Example 3:

Input: s = "zzzzz"
Output: 15


Constraints:

1 <= s.length <= 105
s consists of lowercase letters.

"""
"""
Greedy String
a continuous substring of n # of 'a's contribute sum(1+...+n) = n*(n+1)/2 homogenous substrings

time O(N)
space O(1)
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        n = len(s)
        MOD = 10 ** 9 + 7

        total = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            # now s[j] != s[i]
            # and wehave j-i of s[i]'s
            if j == n or s[j] != s[i]:
                total = (total + int((j - i) * (j - i + 1) / 2) % MOD) % MOD
            else:  # j>n or s[j] == s[i]
                total = (total + 1) % MOD
            i = j

        return total


def main():
    sol = Solution()
    assert sol.countHomogenous(s = "abbcccaa") == 13, 'fails'

    assert sol.countHomogenous(s = "xy") == 2, 'fails'

    assert sol.countHomogenous(s = "zzzzz") == 15, 'fails'


if __name__ == '__main__':
   main()