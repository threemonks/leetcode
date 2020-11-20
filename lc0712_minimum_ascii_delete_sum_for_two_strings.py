"""
712. Minimum ASCII Delete Sum for Two Strings
Medium

1125

50

Add to List

Share
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].

"""
from functools import lru_cache

"""
DP with two string
dp bottom up
dp[i][j] := minium sum after covering s1[:i] and s2[:j]

dp[i][j] = ???
    if s[i] == s[j]:
        dp[i][j] = dp[i-1][j-1]
    else:
        # else need to delete s1[i] or s2[j]
        dp[i][j] = min(dp[i-1][j] + ord(s1[i]), dp[i][j-1] + ord(s2[j]))

time O(l1*l2)
space O(l1*l2)

"""
# import numpy

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        l1 = len(s1)
        l2 = len(s2)
        s1 = '#' + s1
        s2 = '#' + s2
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        dp[0][0] = 0

        for i in range(1, l1 + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i])
        # print(numpy.matrix(dp))

        for j in range(1, l2 + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j])
        # print(numpy.matrix(dp))

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                # print('s1[%s]=%s s2[%s]=%s' % (i, s1[i], j, s2[j]))
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                    # print(numpy.matrix(dp))
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i]), dp[i][j - 1] + ord(s2[j]))
                    # print(numpy.matrix(dp))

        # print(numpy.matrix(dp))

        return dp[l1][l2]


"""
DP top down / recursive
"""

class Solution1:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        @lru_cache(None)
        def helper(i, j):
            if i == -1 and j == -1:
                return 0
            elif i == -1 and j >= 0:
                return sum([ord(c) for c in s2[:j + 1]])
            elif i >= 0 and j == -1:
                return sum([ord(c) for c in s1[:i + 1]])
            if s1[i] == s2[j]:
                return helper(i - 1, j - 1)
            else:
                return min(helper(i - 1, j) + ord(s1[i]), helper(i, j - 1) + ord(s2[j]))

        return helper(len(s1) - 1, len(s2) - 1)


def main():
    sol = Solution1()
    assert sol.minimumDeleteSum("sea", "eat") == 231, 'fails'

    assert sol.minimumDeleteSum("delete", "leet") == 403, 'fails'

    assert sol.minimumDeleteSum("igijekdtywibepwonjbwykkqmrgmtybwhwjiqudxmnniskqjfbkpcxukrablqmwjndlhblxflgehddrvwfacarwkcpmcfqnajqfxyqwiugztocqzuikamtvmbjrypfqvzqiwooewpzcpwhdejmuahqtukistxgfafrymoaodtluaexucnndlnpeszdfsvfofdylcicrrevjggasrgdhwdgjwcchyanodmzmuqeupnpnsmdkcfszznklqjhjqaboikughrnxxggbfyjriuvdsusvmhiaszicfa"
"ikhuivqorirphlzqgcruwirpewbjgrjtugwpnkbrdfufjsmgzzjespzdcdjcoioaqybciofdzbdieegetnogoibbwfielwungehetanktjqjrddkrnsxvdmehaeyrpzxrxkhlepdgpwhgpnaatkzbxbnopecfkxoekcdntjyrmmvppcxcgquhomcsltiqzqzmkloomvfayxhawlyqxnsbyskjtzxiyrsaobbnjpgzmetpqvscyycutdkpjpzfokvi") == 41731, 'fails'

if __name__ == '__main__':
   main()