"""
730. Count Different Palindromic Subsequences
Hard

953

54

Add to List

Share
Given a string s, return the number of different non-empty palindromic subsequences in s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is obtained by deleting zero or more characters from the string.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences a1, a2, ... and b1, b2, ... are different if there is some i for which ai != bi.



Example 1:

Input: s = "bccb"
Output: 6
Explanation: The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
Example 2:

Input: s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
Output: 104860361
Explanation: There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 109 + 7.


Constraints:

1 <= s.length <= 1000
s[i] is either 'a', 'b', 'c', or 'd'.
"""
"""
DP

only four chars, so it could be
a, b, c, d
aa, bb, cc, dd
aaa, aba, aca, ada, bbb, bab, bcb, bdb, ccc, cac, cbc, cdc, dad, dbd, dcd, ddd

dp[i][j] := counts non-empty palindromic subsequcen within string s[i:j+1] (including i and j)

base dp[i][i] = 1 # "a", "b", "c", "d"

if s[i] != s[j]:
    dp[i][j][k] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1] 
if s[i] == s[j]:
    a [xxx] a
    i       j
    we wuold have a, aa, [xxx], a[xxx]a, so
    if a not inside s[i+1:j]:
        dp[i][j] = dp[i+1][j-1]*2 + 2
    elif a appear once in s[i+1:j]: # we have aa, [xxx], a[xxx]a
        dp[i][j] = dp[i+1][j-1]*2 + 1
    elif a appear twice or more inside s[i+1:j], # then we need to exclude inner double counting all palindromic subseq within the
         inner layer, which starts at first char from left != s[i], and first char from right != s[j] (same as s[i])
         i.e., we remove all s[i]'s' from both end of dp[i+1][j-1], the remaining part would be low+1...high-1, 
         that part needs to be excluded as it is double counted
        dp[i][j] = dp[i+1][j-1]*2 - dp[low+1][high-1]

"""
from collections import defaultdict


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 1000000007
        n = len(s)

        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1  # base case 'a', 'b', 'c'

        for dist in range(1, n): # the range of the subsequence range being checked
            for i in range(n - dist): # left boundary
                j = i + dist # right boundary
                dp[i][i] = 1
                low = i + 1
                high = j - 1

                while low <= high and s[low] != s[j]:
                    low += 1

                while low <= high and s[i] != s[high]:
                    high -= 1

                if s[i] != s[j]:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                elif s[i] == s[j]:
                    if low > high:
                        dp[i][j] = dp[i + 1][
                                       j - 1] * 2 + 2  # count for 'a', 'aa', assuming s[i]=a, this low>high tells us 'a' does not exist in s[i+1:j] # excluding j
                    elif low == high:
                        dp[i][j] = dp[i + 1][
                                       j - 1] * 2 + 1  # count for 'a', assuming s[i]=a, this low>high tells us 'a' exists in s[i+1:j] exactly once # excluding j
                    elif low < high:
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[low + 1][
                            high - 1]  # this is when s[i+1:j] has outer layer 'a*a' (assuming s[i]='a'), low+1:high-1 is the first layer that is not enclosed with s[i] (e.g, 'a*a')

                if dp[i][j] < 0:
                    dp[i][j] += MOD
                else:
                    dp[i][j] = dp[i][j] % MOD

        return dp[0][n - 1]


def main():
    sol = Solution()
    assert sol.countPalindromicSubsequences(s = "bccb") == 6, 'fails'

    assert sol.countPalindromicSubsequences(s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba") == 104860361, 'fails'


if __name__ == '__main__':
   main()