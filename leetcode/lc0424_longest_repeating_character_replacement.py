"""
424. Longest Repeating Character Replacement
Medium

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.


Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
import collections

"""
two pointers sliding window
for each new char, add to the sliding window, update counter of each chars
while operations required to get all char to be the same within the window > k, remove one char from left, until we can make all chars within sliding window the same with no more than k operations
once window is valid again, calculate window length and update result if necessary
"""

import collections

"""
two pointers sliding window
for each new char, add to the sliding window, update counter of each chars
while operations required to get all char to be the same within the window > k, remove one char from left, until we can make all chars within sliding window the same with no more than k operations
once window is valid again, calculate window length and update result if necessary
"""

import collections

"""
two pointers sliding window
for each new char, add to the sliding window, update counter of each chars
while operations required to get all char to be the same within the window > k, remove one char from left, until we can make all chars within sliding window the same with no more than k operations
once window is valid again, calculate window length and update result if necessary
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.defaultdict(int)
        maxf = 0
        left = 0
        res = 0
        for i, c in enumerate(s):
            counter[c] += 1  # adding new character, update counter
            maxf = max(maxf, counter[c])
            # counter.most_common(1)[0][1] # count of most often char in the counter
            while i - left + 1 - maxf > k:  # total operations required to make all chars the same within the window
                counter[s[left]] -= 1
                left += 1

            res = max(res, i - left + 1)

        return res


def main():
    sol = Solution()
    assert sol.characterReplacement(s = "ABAB", k = 2) == 4, 'fails'

    assert sol.characterReplacement(s = "AABABBA", k = 1) == 4, 'fails'

if __name__ == '__main__':
   main()