"""
1255. Maximum Score Words Formed by Letters
Hard

https://leetcode.com/problems/maximum-score-words-formed-by-letters/
"""
from typing import List
from collections import Counter
from functools import lru_cache

"""
Backtrack recursion with memoization

We need to check each of the word (index=i) in words, to decide whether we should include it or not, so we use backtrack, each time for the current word, we have two choices:
1. we use this word if possible, add its score to current score result
2. we don't use this word, keep current score result
then recursive call to next level with index=i+1, and the new current score

Each time we got a new score, we would compare it with global ans and keep the max score.

Note:
1. this needs to cache call to dfs, but it has remaining words (list) as input, so we need to convert it into tuple then add memoization  -- No longer needed after we clean up redundant processing and pass only current word index into recursive call
2. needs to convert words to tuple, and letters to string to use memoization -- no longer necessary

"""


class Solution0:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters = ''.join(letters)  # convert to string so we can cache recursive call result
        m, n = len(words), len(letters)
        wordscore = dict()
        for word in words:
            wordscore[word] = sum([score[ord(w) - ord('a')] for w in word])

        @lru_cache(None)
        def check_word(word, letters):
            # can this word be constructed from these letters
            wordcount = Counter(word)
            lettercount = Counter(letters)
            for w, c in wordcount.items():
                if w not in lettercount or c > lettercount[w]:
                    return False
            return True

        ans = 0

        @lru_cache(None)
        def dfs(words, letters, res):
            nonlocal ans
            # print('words=%s letters=%s res=%s' % (words, letters, res))
            # loop each words, and try recursive call with remaining
            for i in range(len(words)):  # the loop embeded the base case (when len(words) == 0, do nothing)
                if check_word(words[i], letters):
                    remain_letters = ''.join((Counter(letters) - Counter(words[i])).elements())
                    dfs(tuple(words[:i] + words[i + 1:]), remain_letters, res + wordscore[words[i]])
            ans = max(ans, res)
            return

        dfs(tuple(sorted(words)), letters, 0)

        return ans


"""
Backtrack with memoization

We need to check each of the word (index=i) in words, to decide whether we should include it or not, so we use backtrack, each time for the current word, we have two choices:
1. we use this word if possible, add its score to current score result
2. we don't use this word, keep current score result
then recursive call to next level with index=i+1, and the new current score

Each time we got a new score, we would compare it with global ans and keep the max score.

"""


class Solution1:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters = ''.join(letters)  # convert to string so we can cache recursive call result
        m, n = len(words), len(letters)
        wordscore = dict()
        for word in words:
            wordscore[word] = sum([score[ord(w) - ord('a')] for w in word])

        @lru_cache(None)
        def check_word(word, letters):
            # can this word be constructed from these letters
            wordcount = Counter(word)
            lettercount = Counter(letters)
            for w, c in wordcount.items():
                if w not in lettercount or c > lettercount[w]:
                    return False
            return True

        ans = 0

        @lru_cache(None)
        def dfs(idx, letters, res):
            nonlocal ans
            # print('words=%s letters=%s res=%s' % (words, letters, res))
            # base case
            if idx >= m:
                ans = max(ans, res)
                return

            # choose words[idx]
            word = words[idx]
            if check_word(word, letters):
                remain_letters = ''.join((Counter(letters) - Counter(word)).elements())
                dfs(idx + 1, remain_letters, res + wordscore[word])

            # do not choose words[idx]
            dfs(idx + 1, letters, res)
            return

        dfs(0, letters, 0)

        return ans


"""
Backtrack

At each current word (of words), we can choose to
1. use it (if it fits with remaining letters), and add the word score, and recursive call into next index
2. or not use it, then recursive call into next index

With this, we don't need to cache call to dfs since it will just run once for idx from 0 to m, and remaining letters would always be different between each call 

"""


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters = ''.join(letters)  # convert to string so we can cache recursive call result
        m, n = len(words), len(letters)
        wordscore = dict()
        for word in words:
            wordscore[word] = sum([score[ord(w) - ord('a')] for w in word])

        @lru_cache(None)
        def check_word(word, letters):
            # can this word be constructed from these letters
            wordcount = Counter(word)
            lettercount = Counter(letters)
            for w, c in wordcount.items():
                if w not in lettercount or c > lettercount[w]:
                    return False
            return True

        def dfs(idx, letters):
            # print('idx=%s letters=%s' % (idx, letters))
            # base case
            if idx >= m:
                return 0
            res = 0
            # use word[idx] and its score
            if check_word(words[idx], letters):
                remain_letters = ''.join((Counter(letters) - Counter(words[idx])).elements())
                res += wordscore[words[idx]] + dfs(idx + 1, remain_letters)

            # do not use word[i] and its score
            return max(res, dfs(idx + 1, letters))

        return dfs(0, letters)


def main():
    sol = Solution()
    assert sol.maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]) == 23, 'fails'

    assert sol.maxScoreWords(words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]) == 27, 'fails'

    assert sol.maxScoreWords(words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]) == 0, 'fails'

if __name__ == '__main__':
   main()