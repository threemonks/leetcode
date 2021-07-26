"""
1839. Longest Substring Of All Vowels in Order
Medium

15

3

Add to List

Share
A string is considered beautiful if it satisfies the following conditions:

Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.

A substring is a contiguous sequence of characters in a string.



Example 1:

Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13
Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
Example 2:

Input: word = "aeeeiiiioooauuuaeiou"
Output: 5
Explanation: The longest beautiful substring in word is "aeiou" of length 5.
Example 3:

Input: word = "a"
Output: 0
Explanation: There is no beautiful substring, so return 0.


Constraints:

1 <= word.length <= 5 * 10^5
word consists of characters 'a', 'e', 'i', 'o', and 'u'.
"""
"""
Hash Table
"""


class Solution0:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        idx = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        chars = 'aeiou'
        counts = [0] * 5

        ans = 0
        cur = chars[0]
        curidx = -1

        for i in range(n):
            c = word[i]
            if idx[c] == curidx or (idx[c] == curidx + 1 and counts[curidx] > 0):
                counts[idx[c]] += 1
                curidx = idx[c]
            else:
                # update answer and reset
                if counts[-1] > 0:
                    ans = max(ans, sum(counts))
                counts = [0] * 5
                # if starts with a
                if idx[c] == 0:
                    counts[idx[c]] += 1
                    curidx = idx[c]
            # print('c=%s counts=%s' % (c, counts))

        # may need to update answer after end of word
        if counts[-1] > 0:
            ans = max(ans, sum(counts))

        return ans


"""
Sliding Window / Two Pointers

keep window status must start with a, must end with u, then can keep grow with u, if encounter any other, it needs to be discarded and start a new window at next a

iterate i from 0 to n, for each i, explore j from i to right most while keeping a valid window (five sections of vowels)

"""


class Solution:
    def longestBeautifulSubstring(self, s: str) -> int:
        n = len(s)
        p = 'aeiou'

        i, ans = 0, 0
        while i < n:
            if s[i] != 'a':  # a valid sliding window always starts with 'a'
                i += 1
                continue
            j = i
            k = 0
            while j < n:
                if s[j] == p[k]:  # same char
                    j += 1
                else:
                    if k == 4:  # 5 vowels section already done, now we have a new char
                        break
                    if s[j] == p[k + 1]:  # next char
                        j += 1
                        k += 1
                    else:  # invalid next character
                        break
                if k == 4:  # we are on 5-th section of 5 section vowels, should update ans if possible
                    ans = max(ans, j - i)
                    # print('i=%s j=%s %s' % (i, j, s[i:j]))
            i = max(i + 1, j)  # i moves right 1 step, or jump to j, whichever is bigger

        return ans


def main():
    sol = Solution()

    assert sol.longestBeautifulSubstring(s = "aeiaaioaaaaeiiiiouuuooaauuaeiu") == 13, 'fails'

    assert sol.longestBeautifulSubstring(s = "aeeeiiiioooauuuaeiou") == 5, 'fails'

    assert sol.longestBeautifulSubstring(s = "a") == 0, 'fails'

if __name__ == '__main__':
   main()