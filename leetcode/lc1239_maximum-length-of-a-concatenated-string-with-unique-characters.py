"""
1239. Maximum Length of a Concatenated String with Unique Characters
Medium

1174

112

Add to List

Share
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26


Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""
from typing import List

"""
Backtrack

for each element in arr, we can choose to use or not to use

Note:
1. arr[i] itself could contain duplicate chars, then it needs to be skipped.
"""
from functools import lru_cache


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        # drop any word with duplicate chars
        arr = [word for word in arr if len(word) == len(set(word))]

        n = len(arr)
        ans = 0

        @lru_cache(None)
        def bt(idx, path):
            nonlocal ans
            ans = max(ans, len(path))
            if idx == n:
                return

            for j in range(idx, n):
                # if arr[j] has any duplicate chars with existing path
                if any([c in path for c in arr[j]]):
                    continue
                # valid arr[j] that can add into result
                bt(j + 1, path + arr[j])

        bt(0, '')

        return ans

def main():
    sol = Solution()
    assert sol.maxLength(arr = ["un","iq","ue"]) == 4, 'fails'

    assert sol.maxLength(arr = ["cha","r","act","ers"]) == 6, 'fails'

    assert sol.maxLength(arr = ["abcdefghijklmnopqrstuvwxyz"]) == 26, 'fails'

if __name__ == '__main__':
   main()