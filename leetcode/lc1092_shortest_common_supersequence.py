"""
1092. Shortest Common Supersequence
Hard

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation:
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.


Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""
"""
Dynamic Programming

Using dp 2-d to find longest common subsequence (lcs), then constructe common supersequence by iterating lcs, for each char in lcs, iterate each char in s1, if not matching lcs char, add to result, until find the matching char in s1, similar, iterate each char in s2, if not matching lcs char, add to result, then add the lcs into result, repeat until lcs is exhausted

after exhausing lcs, if there's remaining chars in s1 or s2, append to result

time O(mn) - from dp
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        def lcs(s1, s2):
            """
            longest common subsequence
            """
            m = len(s1)
            n = len(s2)

            dp = [['' for _ in range(n)] for _ in range(m)]
            # find longest common subsequence first, then?
            for i in range(m):
                for j in range(n):
                    if str1[i] == str2[j]:
                        dp[i][j] = (dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else '') + s1[i]
                    else:
                        dp[i][j] = max(dp[i - 1][j] if i - 1 >= 0 else '', dp[i][j - 1] if j - 1 >= 0 else '',
                                       key=len)  # take longer one

            return dp[m - 1][n - 1]

        res = ''
        i = 0
        j = 0
        for ch in lcs(str1, str2):
            while ch != str1[i]:
                res += str1[i]
                i += 1
            while ch != str2[j]:
                res += str2[j]
                j += 1
            res += ch
            i += 1
            j += 1

        # print('i=%s j=%s res=%s' % (i, j, res))

        return res + str1[i:] + str2[j:]

def main():
    sol = Solution()
    assert sol.shortestCommonSupersequence(str1 = "abac", str2 = "cab") == "cabac", 'fails'

if __name__ == '__main__':
   main()