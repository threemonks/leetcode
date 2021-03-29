"""
647. Palindromic Substrings
Medium

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:

The input string length won't exceed 1000.

"""
"""
DP String Two Pointers

brutal force
time O(N^3)
"""


class Solution0:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        ans = 0
        for i in range(n):
            for j in range(i, n):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    ans += 1

        return ans


"""
DP String Two Pointers

dp[i][j] := is string s[i:j] (inclusive) a valid palindrome?

base case:
1. single letter is valid palindrome: dp[i][i] = True
2. double letter is valid palin if chars same: dp[i][i+1] = (s[i]==s[i+1])

transition:
    if s[i] == s[j]:
        if i+1<j-1:
            dp[i][j] = dp[i+1][j-1]
        else: # empty between s[i] and s[j]
            dp[i][j] = True
    else:
        dp[i][j] = False

mistakes:
1. i needs to iterate backwards because dp[i][j] depends on dp[i+1][j-1]
2. for 2 chars or less, dp[i][j] = (s[i]==s[j]), special handling
   dp[i + 1][j - 1] implies that i+1<=j-1, i.e., j-i>=2, so we are left with empty (nothing) for j-i <2
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        # base case 1: single letter is always valid palindrome
        for i in range(n):
            dp[i][i] = True

        # base case 2: double letter is palin if chars are same
        for i in range(1, n):
            if s[i] == s[i - 1]:
                dp[i - 1][i] = True

        for i in range(n - 1, -1, -1):  # i needs to iterate backwards since dp[i][j] depends on dp[i+1][j-1]
            for j in range(i, n):
                if s[i] == s[j]:
                    if i + 1 < j - 1:
                        dp[i][j] = dp[i + 1][j - 1]  # needs to handle 2 chars or less specially
                    else:
                        dp[i][j] = True  # no substring between i and j (after s[i] == s[j])
                else:
                    dp[i][j] = False

        # print(dp)
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += dp[i][j]

        return ans


def main():
    sol = Solution()
    assert sol.countSubstrings("abc") == 3, 'fails'

    assert sol.countSubstrings("aaa") == 6, 'fails'


if __name__ == '__main__':
   main()