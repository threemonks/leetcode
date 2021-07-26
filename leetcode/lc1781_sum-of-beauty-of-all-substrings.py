"""
1781. Sum of Beauty of All Substrings
Medium

The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.



Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17


Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters.

"""
from collections import defaultdict

"""
Hash Table
"""


class Solution0:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            counts = defaultdict(int)
            counts[s[i]] += 1
            for j in range(i + 1, n):
                counts[s[j]] += 1

                if counts:
                    beauty = max(counts.values()) - min(counts.values())
                    ans += beauty

        return ans


"""
Hash Table / Array

Use array to store character counter

mistakes:
1. we need a new counts array for each new i, because for a new i, j restarts from 0, all counts for j>i+1 in previous i are no longer relavant.
2. j needs to start at i+1, otherwise we are double counting s[i]
"""


class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            counts = [0 for _ in range(26)]
            counts[ord(s[i]) - ord('a')] += 1
            for j in range(i + 1, n):
                counts[ord(s[j]) - ord('a')] += 1
                nonzero_counts = [c for c in counts if c > 0]
                if nonzero_counts:
                    beauty = max(nonzero_counts) - min(nonzero_counts)
                    ans += beauty

        return ans


def main():
    sol = Solution()
    assert sol.beautySum(s = "aabcb") == 5, 'fails'

    assert sol.beautySum(s = "aabcbaa") == 17, 'fails'

if __name__ == '__main__':
   main()