"""
76. Minimum Window Substring
Hard

6358

429

Add to List

Share
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"


Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.


Follow up: Could you find an algorithm that runs in O(n) time?

"""
import math

"""
Sliding window

use a dict to record char:count for t
then use sliding window to calculate char:count in s, as soon as it matches with t's char count, it is a valid window, we record its length, and update answer if this valid window is shorter

time O(S+T)
space O(S+T)
"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        if len(t) > len(s):
            return ""

        tcounts = dict(Counter(t))
        scounts = dict()
        n = len(s)
        ans = ""  # max window length
        minlen = math.inf
        j = 0
        for i in range(n):
            # add letter on right side
            # print('adding i=%s %s' % (i, s[i]))
            if s[i] in scounts:
                scounts[s[i]] += 1
            else:
                scounts[s[i]] = 1

            # shrink sliding window by dropping one char from left side, while maintaining window to be valid
            # s.t. all scounts[k] > tcounts[k] for all k in tcounts
            while j < i and all([tcounts[k] <= scounts.get(k, 0) for k in tcounts]):
                # print('i=%s j=%s scounts=%s ans=%s' % (i, j, scounts, ans))
                # update answer with this valid window length (if it is valid and shorter)
                if all([tcounts[k] <= scounts.get(k, 0) for k in tcounts]):
                    if i - j + 1 < minlen:
                        ans = s[j:i + 1]
                        minlen = len(ans)
                # print('removing j=%s %s' % (j, s[j]))
                scounts[s[j]] -= 1
                if scounts[s[j]] == 0:
                    del scounts[s[j]]
                j += 1

            # update answer here again in case we didn't go into the while loop
            if all([tcounts[k] <= scounts.get(k, 0) for k in tcounts]):
                if i - j + 1 < minlen:
                    ans = s[j:i + 1]
                    minlen = len(ans)

        if minlen == math.inf:
            return ""
        else:
            return ans


def main():
    sol = Solution()
    assert sol.minWindow(s = "ADOBECODEBANC", t = "ABC") == "BANC", 'fails'

    assert sol.minWindow(s = "a", t = "a") == "a", 'fails'

if __name__ == '__main__':
   main()