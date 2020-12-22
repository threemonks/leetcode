"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""
"""
use a hashmap to store last occurence and last las occurence of each character
so longest substring determined would be from minimum of previous previous occurence of this letter to the current index i, for all possible characters
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        lastlastpos = dict()
        lastpos = dict()
        res = 1
        for i, c in enumerate(s):
            if c in lastpos:
                lastlastpos[c] = lastpos[c]
            lastpos[c] = i
            if lastlastpos:
                res = max(res, min([i - v for k, v in lastlastpos.items()]))
            else:
                res = max(res, i + 1)
            # print('i=%s c=%s lastpos=%s lastlastpos=%s' % (i, c, str(lastpos), str(lastlastpos)))

        return res


"""
use two pointers denote start (i) and end (j) of substring investigating, also store last seen position of each character to identify duplicate, update start(i) is char seen already and last seen index is within the substring we are evaluating checking, if char not seen, or last seen outside start, then add this new char into current substring, and update ans (max length)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        lastpos = dict()
        ans = 0
        i = 0
        for j in range(n):
            c = s[j]
            if c in lastpos and i <= lastpos[
                c]:  # only care about lastpos within [i,j], characters seen before i does not impact current substring
                i = lastpos[c] + 1
            else:
                ans = max(ans, j - i + 1)
            lastpos[c] = j
            # print('i=%s j=%s c=%s lastpos=%s ans=%s' % (i, j, c, str(lastpos), ans))

        return ans


def main():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3, 'fails'

    assert sol.lengthOfLongestSubstring("bbbbb") == 1, 'fails'

    assert sol.lengthOfLongestSubstring("pwwkew") == 3, 'fails'

    assert sol.lengthOfLongestSubstring("") == 0, 'fails'

    assert sol.lengthOfLongestSubstring("au") == 2, 'fails'

if __name__ == '__main__':
   main()