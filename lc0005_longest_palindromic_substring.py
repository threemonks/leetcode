"""
5. Longest Palindromic Substring
Medium

https://leetcode.com/problems/longest-palindromic-substring/
"""
"""
brutal force
TLE
"""


class Solution0:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        ans = ''
        for i in range(n):
            for j in range(i + 1, n + 1):
                if s[i:j] == s[i:j][::-1]:
                    if j - i > len(ans):
                        ans = s[i:j]

        return ans


"""
DP bottom up

dp[i][j] := whether s[i:j+1] is palindrome

base case:
    dp[i][i] = True # one char
    dp[i][i+1] = s[i] == s[i+1] # its palindrome if s[i] == s[i+1]

transition
    dp[i][j] = dp[i+1][j-1] and s[i]==s[j] # base on this transition, i needs to iterate from n-1 to 0, j from i+1 to n-1

Time Complexity - O(N^2)
Space Complexity - O(N^2) (caching all substring)

https://leetcode.com/problems/longest-palindromic-substring/discuss/900639/Python-Solution-%3A-with-detailed-explanation-%3A-using-DP
* because dp[i][j] depends on dp[i+1][j-1], so i needs to iterate from n-1 to 0, and j is ending index of palindrome substring, so j>i, so j iterates from i+1 to n-1

Bottom up DP note
https://leetcode.com/problems/longest-palindromic-substring/discuss/151144/Bottom-up-DP-Logical-Thinking

mistakes:
1. dp[i][j] represents substring i to j (both inclusive), the length of this substring is j-i+1
"""


class Solution1:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[False for _ in range(n)] for _ in range(n)]

        ans = ''
        for i in range(n):
            dp[i][i] = True
            ans = s[i]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if dp[i][j] and j - i + 1 > len(ans):
                            ans = s[i:j + 1]

        return ans


"""
Recursive / Expand from middle / grow palindrome substring from middle to outer

https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).

time O(N^2)
space O(1)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def helper(l, r):
            # return longest substring palindrome growing from i to left, and j to right
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            # returns s[l+1:r] instead of s[l:r+1] because the last l,r value does not satisfy s[l] == s[r] when the loop exits
            return s[l + 1:r]

        ans = ''
        for i in range(n):
            # odd case, like "aba"
            tmp = helper(i, i)
            if len(tmp) > len(ans):
                ans = tmp
            # even case, like "cbbd"
            tmp = helper(i, i + 1)
            if len(tmp) > len(ans):
                ans = tmp

        return ans


def main():
    sol = Solution()
    assert sol.longestPalindrome("babad") in ["bab", "aba"], 'fails'

    assert sol.longestPalindrome("cbbd") in ["bb"], 'fails'

    assert sol.longestPalindrome("a") in ["a"], 'fails'

    assert sol.longestPalindrome("ac") in ["a", "c"], 'fails'

if __name__ == '__main__':
   main()