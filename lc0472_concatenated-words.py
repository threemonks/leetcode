"""
472. Concatenated Words
Hard

1340

162

Add to List

Share
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.



Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]


Constraints:

1 <= words.length <= 104
0 <= words[i].length <= 1000
words[i] consists of only lowercase English letters.
0 <= sum(words[i].length) <= 105
"""
from typing import List

"""
DFS/Recursion

1. convert words list to wordset
2. for each word, check any prefix if in wordset, then recursively check its remaining suffix, if exhaust the word (no remaining suffix), and accumulated word count (through recursion) >= 2, return True
3. if the word recursive check returns True, add to output

time O(N*2^L)

time complexity:
T(n) = 1; n is 0
     = 2*T(n-1); otherwise
=> O(2^n)

"""


class Solution:
    def recursive_check(self, s, count, wordset):
        if not s and count >= 2:
            return True
        for j in range(1, len(s) + 1):
            if s[:j] in wordset and self.recursive_check(s[j:], count + 1, wordset):
                # print('s=%s s[:j]=%s, count=%s' % (s, s[:j], count))
                return True

        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        wordset = set(words)

        ans = []

        for word in words:
            if self.recursive_check(word, 0, wordset):
                ans.append(word)

        return ans

def main():
    sol = Solution()
    assert sol.findAllConcatenatedWordsInADict(words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]) == ["catsdogcats","dogcatsdog","ratcatdogcat"], 'fails'

    assert sol.findAllConcatenatedWordsInADict(words = ["cat","dog","catdog"]) == ["catdog"], 'fails'

if __name__ == '__main__':
   main()