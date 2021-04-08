"""
30. Substring with Concatenation of All Words
Hard

1210

1454

Add to List

Share
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.



Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]


Constraints:

1 <= s.length <= 10^4
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.

"""
from typing import List

"""
Hash Table / Sliding Window

since all words have same length, so we can jump one word length at a time, keep a sliding window of n words length, and check if a new word from right boundary of window is added, and if so, increase its count, also decreas the count for the word that drops out of left boundary of window. At each such step, we verify if the window content (words and their counts) matches with given words (as dict of word count), if so, record window left boundary

m, n = len(s), len(words)
wl = wordlength
for i in range(wl):
    counts[i] = dict()
    for j in range(i, i+m+1, wl):
        # add new word
        if s[j-wl:j] in wordsdct:
            counts[i][s[j-wl:j]] += 1
        # remove old word dropping outside of left window boundary
        if s[j-wl-wl*n:j-wl*n] in wordsdct:
            counts[i][s[j-wl-wl*n:j-wl*n]] -= 1

        if counts[i] has same words and word counts as given words
            add left boundary of window (j-wl*n) into result

time O(N*M) - N=len(words), M=len(s)
space O(N*wl) - wl=word length (len(words[0]))

mistakes:
1. words can have duplicates
2. j needs to reach m since it is an exclusive upper word bound
"""

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m, n = len(s), len(words)
        wl = len(words[0])  # word length

        # print('m=%s n=%s wl=%s' % (m, n, wl))

        wordsdct = dict()
        for word in words:
            if word in wordsdct:
                wordsdct[word] += 1
            else:
                wordsdct[word] = 1

        counts = [dict() for _ in range(wl)]

        result = []
        for i in range(wl):  # move one char at a step
            for j in range(i, i + m + 1,
                           wl):  # jump wl at each step, note j needs to reach m, since it is used as exclusive word upper bound (not including upper bound)
                # add new word from right side if it is in dict
                if j - wl >= 0 and s[j - wl:j] in wordsdct:
                    word = s[j - wl:j]
                    if word in counts[i]:
                        counts[i][word] += 1
                    else:
                        counts[i][word] = 1
                # remove word dropping out of left boundary of window
                if j - wl - wl * n >= 0 and s[j - wl - wl * n:j - wl * n] in wordsdct:
                    word = s[j - wl - wl * n:j - wl * n]
                    if word in counts[i]:
                        counts[i][word] -= 1
                        if counts[i][word] == 0:
                            del counts[i][word]
                    else:
                        counts[i][word] = 1

                # check if counts[i] has all different words, and only once for each
                # print('i=%s j=%s counts[i]=%s' % (i, j, counts[i]))
                if counts[i] == wordsdct:
                    result.append(j - wl * n)  # start of first word in window
                # print('i=%s j=%s result=%s' % (i, j, result))

        # print(result)
        return result

def main():
    sol = Solution()
    assert sorted(sol.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"])) == [0, 9], 'fails'

    assert sorted(sol.findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"])) == [], 'fails'

    assert sorted(sol.findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"])) == [6, 9, 12], 'fails'


if __name__ == '__main__':
   main()