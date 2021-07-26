"""
438. Find All Anagrams in a String
Medium

4504

207

Add to List

Share
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.



Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:

1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.
"""
from typing import List

"""
String
anagram - use dict to hold each char's count

use sliding window to scan through s to find matching count dict

"""
from collections import defaultdict

"""
Sliding Window

anagram - use dict to hold the count of each char in string p

use sliding window to scan through string s to find a window with matching count dict as p

time O(Ns+Np) - Ns=len(s) Np=len(p)
space O(1) - 26 character
"""
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countp = defaultdict(int)
        for c in p:
            countp[c] += 1

        n = len(s)
        ans = []
        counts = defaultdict(int)
        j = 0
        for i, c in enumerate(s):
            # print('i=%s' % i)
            counts[c] += 1
            while j < n and counts[s[j]] > countp[s[j]]:
                counts[s[j]] -= 1
                j += 1

            # is this a valid window?
            if counts.keys() == countp.keys() and all([counts[k] == countp[k] for k in countp.keys()]):
                # print('j=%s i=%s' % (j, i))
                ans.append(j)

        return ans


def main():
    sol = Solution()
    assert sol.findAnagrams(s = "cbaebabacd", p = "abc") == [0, 6], 'fails'

    assert sol.findAnagrams(s = "abab", p = "ab") == [0, 1, 2], 'fails'


if __name__ == '__main__':
   main()