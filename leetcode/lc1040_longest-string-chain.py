"""
1048. Longest String Chain
Medium

1960

109

Add to List

Share
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.



Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chain is "a","ba","bda","bdca".
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5


Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.

"""
from collections import defaultdict, deque
from functools import lru_cache
from typing import List

"""
DFS

time O(n*L*L)
space O(N*L*L)
mistakes:
1. instead of add character to get next word and check if it is in known words, better to remove character from longer word, and see if resulting word is in known set
2. for BFS, we need to find longest path by traverse starting from any node
"""


class Solution0:
    def longestStrChain(self, words: List[str]) -> int:
        wordset = set(words)

        g = defaultdict(list)

        for word in words:
            l = len(word)
            for j in range(l):
                if word[:j] + word[j + 1:] in wordset:
                    g[word].append(word[:j] + word[j + 1:])

        maxlen = max([len(w) for w in words])

        ans = 0
        longest = {}  # longest word chain we can form when ending at given word, might be updated later

        q = deque()
        for w in words:
            q.append((w, 1))
            longest[w] = 1

        while q:
            cur, step = q.popleft()
            ans = max(ans, step)
            for nxt in g[cur]:
                if nxt not in longest or step + 1 > longest[nxt]:
                    q.append((nxt, step + 1))
                    longest[nxt] = step + 1

        return ans


"""
DP

transition:
dp(word) := longest word chain starting with word
dp(word_i) = max([dp(word_i[:j]+word_i[j+1:])+1 for j in range(len(word_i)) if word_i[:j]+word_i[j+1:] in known sets])

time O(n*L*L) # n is len(words), L is average word lenegth
space O(n*L*L)
"""


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = set(words)

        @lru_cache(None)
        def dp(word):
            if word not in words:
                return 0
            return max(dp(word[:i] + word[i + 1:]) for i in range(len(word))) + 1

        return max(dp(word) for word in words)

def main():
    sol = Solution()
    assert sol.longestStrChain(words = ["a","b","ba","bca","bda","bdca"]) == 4, 'fails'

    assert sol.longestStrChain(words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]) == 5, 'fails'

if __name__ == '__main__':
   main()