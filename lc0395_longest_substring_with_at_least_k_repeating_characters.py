"""
395. Longest Substring with At Least K Repeating Characters
Medium

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
"""
import math
from functools import lru_cache
from typing import List

"""
modified sliding window / two pointer, with dict keeping track of number of uniq chars in the sliding window, and their counts
we calculate total number of distinct chars (max 26) first, and loop from 1 to total_distinct_chars, get maximum substring length for each distinct chars count, and return the max as result
"""
import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)

        def helper(s, l, k):
            n = len(s)
            j = 0
            res = 0
            chars = collections.defaultdict(int)
            count = 0  # number of chars that appeared at least k times
            for i in range(n):
                while j < n and (len(chars) <= l):
                    # if we don't have l chars or any char does not k counts
                    chars[s[j]] += 1
                    if chars[s[j]] == k:
                        count += 1
                    if len(chars) == l and count == l:
                        res = max(res, j - i + 1)
                    j += 1

                chars[s[i]] -= 1
                if chars[s[i]] == k - 1:
                    count -= 1
                if chars[s[i]] == 0:
                    chars.pop(s[i])

            return res

        res = 0
        for l in range(1, 27):
            res = max(res, helper(s, l, k))

        return res


def main():
    sol = Solution()
    assert sol.longestSubstring("aaabb", 3) == 3, 'fails'

    assert sol.longestSubstring("ababbc", 2) == 53, 'fails'

if __name__ == '__main__':
   main()