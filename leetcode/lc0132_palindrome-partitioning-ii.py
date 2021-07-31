"""
132. Palindrome Partitioning II
Hard

2151

63

Add to List

Share
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1


Constraints:

1 <= s.length <= 2000
s consists of lower-case English letters only.
"""
"""
区间型 DP

dp[i] := min cuts to get s[:i] into all palindrome substring

dp[i] = (i+1, dp[j]+1 for j in 1...i-1 if s[j+1:i+1] is palindrome)

note:
1. need to test if s[:i+1] is palindrome or not

"""


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        dp = [0 for _ in range(n)]

        for i in range(n):
            if s[:i + 1] == s[:i + 1][::-1]:
                dp[i] = 1
            else:
                dp[i] = i + 1
                for j in range(i):
                    if s[j + 1:i + 1] == s[j + 1:i + 1][::-1]:  # is palindrome
                        dp[i] = min(dp[i], 1 + dp[j])

        return dp[n - 1] - 1


"""
区间型 DP

dp[i] := min cuts to get s[:i] into all palindrome substring

dp[i] = (i+1, dp[j]+1 for j in 1...i-1 if s[j+1:i+1] is palindrome)

note:
1. need to test if s[:i+1] is palindrome or not
2. pre-calculate ispalindrome for all possible substring to improve performance

"""


class Solution1:
    def minCut(self, s: str) -> int:
        n = len(s)

        ispal = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                ispal[i][j] = s[i:j + 1] == s[i:j + 1][::-1]

        # print(ispal)
        dp = [0 for _ in range(n)]

        for i in range(n):
            if ispal[0][i]:
                dp[i] = 1
            else:
                dp[i] = i + 1
                for j in range(i):
                    if ispal[j + 1][i]:  # is palindrome
                        dp[i] = min(dp[i], 1 + dp[j])
                    # print('i=%s j=%s dp=%s' % (i, j, dp))

        return dp[n - 1] - 1

def main():
    sol = Solution()

    assert sol.minCut(s = "aab") == 1, 'fails'

    assert sol.minCut(s="a") == 0, 'fails'

if __name__ == '__main__':
   main()