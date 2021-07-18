"""
387. First Unique Character in a String
Easy

3231

157

Add to List

Share
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 10^5
s consists of only lowercase English letters.
"""
"""
Hash Map
time O(N)
space O(26)=O(1) (lowercase english letters only)
"""
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        positions = defaultdict(int)
        for i, c in enumerate(s):
            if c not in positions:
                positions[c] = i+1 # shift by 1
            elif positions[c] > 0:
                positions[c] = -1
            elif positions[c] == -1: # appear more than once
                pass
            else: # should not need this
                positions[c] = i+1

        ps = [p for p in positions.values() if p > 0]
        if ps:
            return min(ps) - 1
        else: # not found
            return -1

def main():
    sol = Solution()

    assert sol.firstUniqChar(s = "leetcode") == 0, 'fails'

if __name__ == '__main__':
   main()

