"""
https://leetcode.com/problems/word-ladder/

127. Word Ladder
Hard

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words such that:

The first word in the sequence is beginWord.
The last word in the sequence is endWord.
Only one letter is different between each adjacent pair of words in the sequence.
Every word in the sequence is in wordList.
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog" with 5 words.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no possible transformation.


Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the strings in wordList are unique.

"""

import collections
from typing import List

"""
BFS

build graph, then BFS to traverse via shortest path

Note: a graph built from wordList directly is too big, we replace one character in each word with a '*', and build a map using this modified word* as the key for adjacency list, this will significantly reduce the size of the adjacency list

"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        n = len(wordList)
        m = len(beginWord)

        adj_list = collections.defaultdict(list)
        for word in wordList:
            for i in range(m):
                w = word[:i] + '*' + word[i + 1:]
                adj_list[w].append(word)

        def get_neighbors(word):
            nonlocal adj_list
            res = set()
            for i in range(m):
                generic_word = word[:i] + '*' + word[i + 1:]
                for w in adj_list[generic_word]:
                    res.add(adj_list[w])

            return list(res)

        q = collections.deque([(beginWord, 1)])
        visited = dict()
        visited[beginWord] = 1

        while q:
            cur, steps = q.popleft()
            if cur == endWord:
                return steps
            for nei in get_neighbors(cur):
                nsteps = steps + 1
                if nei not in visited:
                    q.append((nei, nsteps))
                    visited[nei] = nsteps

        return 0


import heapq
import collections

"""
BFS

bidirectional BFS
similar to above approach, but search from beginWord and endWord at same time, if they meet in middle, then we have a solution
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        n = len(wordList)
        m = len(beginWord)

        adj_list = collections.defaultdict(list)
        for word in wordList:
            for i in range(m):
                w = word[:i] + '*' + word[i + 1:]
                adj_list[w].append(word)

        def get_neighbors(word):
            nonlocal adj_list
            res = []
            for i in range(m):
                w = word[:i] + '*' + word[i + 1:]
                res.extend(adj_list[w])

            return res

        q1 = collections.deque([(1, beginWord)])
        visited1 = {beginWord: 1}

        q2 = collections.deque([(1, endWord)])
        visited2 = {endWord: 1}

        while q1 and q2:
            level1, cur1 = q1.popleft()
            for nei in get_neighbors(cur1):
                if nei in visited2:
                    return level1 + visited2[nei]
                if nei not in visited1:
                    q1.append((level1 + 1, nei))
                    visited1[nei] = level1 + 1

            level2, cur2 = q2.popleft()
            for nei in get_neighbors(cur2):
                if nei in visited1:
                    return level2 + visited1[nei]
                if nei not in visited2:
                    q2.append((level2 + 1, nei))
                    visited2[nei] = level2 + 1

        return 0


def main():
    sol = Solution()
    assert sol.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]) == 5, 'fails'

    assert sol.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]) == 0, 'fails'


if __name__ == '__main__':
   main()