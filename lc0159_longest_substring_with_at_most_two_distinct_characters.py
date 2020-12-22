"""
159. Longest Substring with At Most Two Distinct Characters
Medium

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

"""
"""
two pointers, iterate right pointer, keep track of all characters inside current substring, and last seen position of each char
if new char is in seen chars inside substring, just add it to right end of substring
if new char is not seen, move left index of substring until it drops out one char (min(chars.values())+1) completely, then add new char into it
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        chars = {}  # store lastest index of each char
        ans = 0
        i = 0
        for j, c in enumerate(s):
            if c not in chars and len(chars.keys()) == 2:
                # retrieve char with lowest index from chars and drop it
                min_char, min_pos = [(k, v) for k, v in sorted(chars.items(), key=lambda x: x[1])][0]
                del chars[min_char]
                # and move left index i just pass it
                i = min_pos + 1
            ans = max(ans, j - i + 1)
            chars[c] = j
            # print('i=%s j=%s c=%s chars=%s ans=%s' % (i, j, c, str(chars), ans))

        return ans

def main():

    sol = Solution()

    sol.lengthOfLongestSubstringTwoDistinct("eceba") == 3, 'fails'

    sol.lengthOfLongestSubstringTwoDistinct("ccaabbb") == 5, 'fails'

if __name__ == '__main__':
   main()