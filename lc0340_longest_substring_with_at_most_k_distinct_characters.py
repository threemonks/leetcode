"""
340. Longest Substring with At Most K Distinct Characters
Hard

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.

"""

"""
use two pointer, iterate (fix) right index, explore left
use hashmap to store counts of each char within the current substring

time O(N*K)
spae O(K)
"""

class Solution0:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counts = dict()  # counts of each char in current substring
        i = 0  # start of current substring
        res = 0
        for j, c in enumerate(s):
            if c in counts:
                counts[c] += 1
                res = max(res, j - i + 1)
            else:  # new char
                counts[c] = 1
                while len(counts.keys()) > k:
                    counts[s[i]] -= 1
                    if counts[s[i]] == 0:
                        del counts[s[i]]
                    i += 1
                # now len(counts.keys()) <= k
                res = max(res, j - i + 1)

        return res


"""
use two pointer, iterate (fix) right index, explore left
use OrderedDict to store latest index of each char within the current sliding window

time O(N)
spae O(K)
"""
from collections import OrderedDict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        lastpos = OrderedDict()  # last position of each char in current substring
        left = 0  # start of current substring
        res = 0
        for right, c in enumerate(s):
            if c in lastpos:
                del lastpos[c]
                lastpos[c] = right  # make sure new index is updated, and stored as last one in OrderedDict
            else:
                lastpos[c] = right
                while len(lastpos) > k:
                    # delete first (most left) element of lastpos, and move left boundary of current substring i to 1+(the index pointed to by the value of this deleted key)
                    _, del_idx = lastpos.popitem(last=False)
                    # move left pointer of the sliding window
                    left = del_idx + 1
                # now len(counts.keys()) <= k
            res = max(res, right - left + 1)

        return res


def main():
    sol = Solution()
    assert sol.lengthOfLongestSubstringKDistinct("eceba", 2) == 3, 'fails'

    assert sol.lengthOfLongestSubstringKDistinct("aa", 1) == 2, 'fails'

if __name__ == '__main__':
   main()