"""
792. Number of Matching Subsequences
Medium

2140

120

Add to List

Share
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".


Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2


Constraints:

1 <= s.length <= 5 * 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
"""
from typing import List

"""
String / Hash Map

for each word, try to match it with each char in the string s, if not advance s to next char, if we finished s, but have not yet matched all chars in word, then this word is not in s

note:
1. words might have repeat word, better to count word freq, and only check whether uniq word occurs in string, then multiple their freq to get final total counts

time O(len(words)*len(s))

"""
from collections import Counter


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_counts = Counter(words)
        words = set(words)
        n = len(s)
        ans = 0
        for word in words:
            i, j = 0, 0
            while i < len(word) and j < n:
                if word[i] == s[j]:
                    i += 1
                    j += 1
                else:  # word[i] != s[j]:
                    j += 1

            if i == len(word):
                ans += word_counts[word]

        return ans


"""
Hash Map

while iterating through s, if current head char of word matches s[i], move word into bucket for its next char. If word has no next char, it is done and found.

use iterator to represent words and their progress.


time O(len(s)*len(words))

"""
from collections import Counter, defaultdict


class Solution1:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        heads = defaultdict(list)

        for word in words:
            heads[word[0]].append(iter(word[1:]))

        ans = 0
        for c in s:
            old_bucket = heads.pop(c, [])
            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    heads[nxt].append(it)
                else:  # this word is done
                    ans += 1

        return ans


"""
Hash Map

while iterating through s, if current head char of word matches s[i], move word into bucket for its next char. If word has no next char, it is done and found.

use an index i within word to indicate next char within word to match against


time O(len(s)*len(words))

"""
from collections import Counter, defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        heads = defaultdict(list)

        for word in words:
            heads[word[0]].append([word, 1])

        ans = 0
        for c in s:
            old_bucket = heads.pop(c, [])
            while old_bucket:
                word, idx = old_bucket.pop()
                if idx < len(word):
                    nxt_c = word[idx]
                    heads[nxt_c].append([word, idx + 1])
                else:  # this word is done
                    ans += 1

        return ans

def main():
    sol = Solution()
    assert sol.numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]) == 3, 'fails'

    assert sol.numMatchingSubseq(s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]) == 2, 'fails'

if __name__ == '__main__':
   main()