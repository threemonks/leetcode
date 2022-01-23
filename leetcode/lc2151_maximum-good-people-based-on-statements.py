"""
2135. Count Words Obtained After Adding a Letter
Medium

168

45

Add to List

Share
You are given two 0-indexed arrays of strings startWords and targetWords. Each string consists of lowercase English letters only.

For each string in targetWords, check if it is possible to choose a string from startWords and perform a conversion operation on it to be equal to that from targetWords.

The conversion operation is described in the following two steps:

Append any lowercase letter that is not present in the string to its end.
For example, if the string is "abc", the letters 'd', 'e', or 'y' can be added to it, but not 'a'. If 'd' is added, the resulting string will be "abcd".
Rearrange the letters of the new string in any arbitrary order.
For example, "abcd" can be rearranged to "acbd", "bacd", "cbda", and so on. Note that it can also be rearranged to "abcd" itself.
Return the number of strings in targetWords that can be obtained by performing the operations on any string of startWords.

Note that you will only be verifying if the string in targetWords can be obtained from a string in startWords by performing the operations. The strings in startWords do not actually change during this process.



Example 1:

Input: startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]
Output: 2
Explanation:
- In order to form targetWords[0] = "tack", we use startWords[1] = "act", append 'k' to it, and rearrange "actk" to "tack".
- There is no string in startWords that can be used to obtain targetWords[1] = "act".
  Note that "act" does exist in startWords, but we must append one letter to the string before rearranging it.
- In order to form targetWords[2] = "acti", we use startWords[1] = "act", append 'i' to it, and rearrange "acti" to "acti" itself.
Example 2:

Input: startWords = ["ab","a"], targetWords = ["abc","abcd"]
Output: 1
Explanation:
- In order to form targetWords[0] = "abc", we use startWords[0] = "ab", add 'c' to it, and rearrange it to "abc".
- There is no string in startWords that can be used to obtain targetWords[1] = "abcd".


Constraints:

1 <= startWords.length, targetWords.length <= 5 * 10^4
1 <= startWords[i].length, targetWords[j].length <= 26
Each string of startWords and targetWords consists of lowercase English letters only.
No letter occurs more than once in any string of startWords or targetWords.
"""
from typing import List

"""
Bit Manipulation

time: (2^n)*(n^2)
      - 2^n - iterate all possible states
      - n^2 - to check all pairs of said statements for a given state to determinte if there's confliction
"""


class Solution:
    def maximumGood(self, g: List[List[int]]) -> int:
        n = len(g)

        ans = 0

        for i in range(1 << n):  # all possible combinations
            valid = True
            for j in range(n):
                for k in range(n):
                    if g[j][k] != 2:  # if something was said
                        if (i >> j & 1):  # j is good
                            # if j is good, what he said about k must match with g[j][k]
                            # i.e., if j says k is good, then g[j][k]==1, and (i>>k)&1==1
                            # or if j says k is bad, then g[j][k]==0, and (i>>k)&1==0
                            if (i >> k & 1) != g[j][
                                k]:  # don't use i & (1<<k) as it might result in value 2 instead of 1, since we need a value either 0 or 1 here to compare g[j][k]
                                valid = False
                                break
                if valid is False:
                    break

            if valid:
                ans = max(ans, bin(i).count('1'))

        return ans


def main():
    sol = Solution()
    assert sol.maximumGood(statements = [[2,1,2],[1,2,2],[2,0,2]]) == 2, 'fails'

    assert sol.maximumGood(statements = [[2,0],[0,2]]) == 1, 'fails'

if __name__ == '__main__':
   main()