"""
1542. Find Longest Awesome Substring
Hard

353

8

Add to List

Share
Given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it palindrome.

Return the length of the maximum length awesome substring of s.



Example 1:

Input: s = "3242415"
Output: 5
Explanation: "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.
Example 2:

Input: s = "12345678"
Output: 1
Example 3:

Input: s = "213123"
Output: 6
Explanation: "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.
Example 4:

Input: s = "00"
Output: 2


Constraints:

1 <= s.length <= 10^5
s consists only of digits.
"""
from collections import defaultdict

"""
Bit Manipulation

any number of swaps to make palindrome => at most one odd count

mistakes:
1. needs to have maps value default to a large value (>=n), so that maps[mask] = min(maps[mask], i) will always pick i if maps[mask] has not been set yet

"""


class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        maps = defaultdict(lambda: n)
        # maps[0] = -1
        mask, fullmask = 0, (1 << 10) - 1
        ans = 1  # a single char is always palindrome
        for i in range(n):
            mask ^= (1 << (ord(s[i]) - ord('0')))
            # print('i=%s mask=%s s[i]=%s' % (i, bin(mask), s[i]))
            for j in range(11):
                mask1 = fullmask & (mask ^ (1 << j))
                # print('--j=%s mask1=%s' % (j, bin(mask1)))
                ans = max(ans, i - maps[mask1])
                # print('--j=%s mask1=%s ans=%s' % (j, bin(mask1), ans))
            maps[mask] = min(maps[mask], i)
            # print('i=%s mask=%s maps=%s' % (i, mask, maps))

        return ans

def main():
    sol = Solution()

    # assert sol.longestAwesome(s = "3242415") == 5, 'fails'
    #
    # assert sol.longestAwesome(s = "12345678") == 1, 'fails'

    assert sol.longestAwesome(s = "213123") == 6, 'fails'

    assert sol.longestAwesome(s = "00") == 2, 'fails'

if __name__ == '__main__':
   main()