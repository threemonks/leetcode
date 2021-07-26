"""
140. Word Break II
Hard

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

"""
from functools import lru_cache
from typing import List
from functools import lru_cache

"""
DP / backtracking / DFS

start from beginning of string s, check the substring s[:i], see if it is a word in dict, if so, add to partial result, and run backtrack processing remaining string
and backtrack to i, we check substring s[:i+1], to

backtrack(s, path) for remaining string s, and existing partial result set path, 

"catsanddog",  []
    "sanddog", ["cat"]
        "dog", ["cat", "sand"]
        "",    ["cat", "sand", "dog"]
    "anddog",  ["cats"]
        "dog", ["cats", "and"]
        "",    ["cats", "and", "dog"]

time O(N^2+2^N+W) : N=len(s), W = len(wordDict), N character in s, there are N^2 edges (break string into a valid prefix that is a word, and remaining string to be processed by recursive call), with each recursive call, it returns 2^N result in worst case, and initial processing of wordDict takes O(W) time.
space O(2^N*N + W)

mistakes:
1. for i in range(1, len(s)): => should be for i in range(1, len(s)+1) else s[:i] does not cover till end of s
        s[:i]
2. skip recursive call if remaining string s[i:] is empty, not when self.helper(s[i:]) return None or []
3. bottom up would timeout, so we first check to make sure wordDict contains all characters in s
"""


class Solution0:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordset = set(wordDict)
        self.s = s

        result = self.helper(0)

        return [' '.join(r) for r in result]

    @lru_cache(None)
    def helper(self, start):
        n = len(self.s)
        if start == n:
            return [[]]

        ans = []
        for i in range(start + 1, n + 1):
            if self.s[start:i] in self.wordset:
                for r in self.helper(i):
                    ans.append([self.s[start:i]] + r)

        return ans


"""
DP bottom up
dp[i] := list of results words with space from prefix string ending at i

dp[i] = [dp[i-1] + s[i] if s[i] in wordset,
        , dp[i-2] + s[i-1:i+1] if s[i-1:i+1] is in wordset
        ...
        dp[0] + s[1:i+1] if s[1:i+1] is in wordset
        ]

mistakes:
1. res + ' ' + s[startindex:endindex] results in answer [" cats and dog"," cat sand dog"] instead of ["cats and dog","cat sand dog"]

"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)
        wordchars = set("".join(wordset))
        if wordchars & set(s) != set(s):  # s has character that wordDict does not contain
            return []

        n = len(s)
        dp = [[] for _ in range(n + 1)]  # dp[i] list of results words with space from prefix string ending at i
        dp[0] = ['']

        for endindex in range(1, n + 1):
            sublist = []
            for startindex in range(endindex):
                if s[startindex:endindex] in wordset:
                    for res in dp[startindex]:
                        dp[endindex].append((res + ' ' + s[startindex:endindex]).strip())  # handle case when res == ' '
            if sublist:
                dp[endindex] = sublist
                # print('endindex=%s dp=%s' % (endindex, dp[endindex]))

        return dp[n]

def main():
    sol = Solution()
    assert sol.wordBreak(s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"]) == ['cat sand dog', 'cats and dog'], 'fails'

    assert sol.wordBreak(s = "pineapplepenapple", wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]) == ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple'], 'fails'

    assert sol.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]) == [], 'fails'



if __name__ == '__main__':
   main()