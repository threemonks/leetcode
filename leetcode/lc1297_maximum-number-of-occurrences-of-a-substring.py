"""
1297. Maximum Number of Occurrences of a Substring
Medium

432

235

Add to List

Share
Given a string s, return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.


Example 1:

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
Example 2:

Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
Example 3:

Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
Output: 3
Example 4:

Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
Output: 0


Constraints:

1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s only contains lowercase English letters.
"""
"""
Sliding Window

1. Problem description says unique, but example and test cases assumes DISTINCT
so we basically use sliding window to find max occurences of substring containing distinct chars <= maxLetters with size minSize (since any size > minSize would be appearing less often or the same)

observation:
If a string have occurrences x times, any of its substring must appear at least x times. So we only need to find substring that >= minSize, because if this substring of size minSize appears x time, any substring contains it that's larger than minSize would be appearing either x time or less. So we don't need to check for any substring that is more than minSize

note:
1. problem description says # of uniq characters, means # of chars that appear only once, but example describes and test cases assumes DISTINCT
2. right bound j increase could increase or decrease # of uniq chars within window
"""
from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        counts = defaultdict(int)
        occurences = defaultdict(int)
        i, j = 0, 0  # left and right boundary of window
        for j in range(n):
            counts[s[j]] += 1
            while i < n and j - i + 1 > minSize:  # if window is larger than minSize, try to shrink
                counts[s[i]] -= 1
                if counts[s[i]] == 0:
                    del counts[s[i]]
                i += 1
            if len(counts.keys()) <= maxLetters and j - i + 1 == minSize:
                occurences[s[i:j + 1]] += 1
            # print('i=%s j=%s counts=%s occurences=%s' % (i, j, counts, occurences))

        if occurences:
            return max(occurences.values())
        else:
            return 0


def main():
    sol = Solution()
    assert sol.maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4) == 2, 'fails'

    assert sol.maxFreq(s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3) == 2, 'fails'

    assert sol.maxFreq(s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3) == 3, 'fails'

    assert sol.maxFreq(s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3) == 0, 'fails'

if __name__ == '__main__':
   main()