"""
https://leetcode.com/problems/word-ladder-ii/

126. Word Ladder II
Hard

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""
import collections
import math
from functools import lru_cache
from typing import List

import collections
from functools import lru_cache
"""

BFS traverse and return ALL shortest path 

Note: keep visited path in queue, and keep global visited set, and visited set for the current level, globally seen node should be skipped, but node visited within the current level could be revisited.

replace one character in word 'hit' with '*' to obtain a generic word (*hi, h*t, hi*), use this as key, to build an adjaceny node list

then use adjaceny list to BFS traverse from start node (not in adj_list), to end word cog

Since we need to return all shortest transformation sequences, we need to find all shortest path, so we use a global_seen set to keep track of nodes seen anywhere, and also a level_seen set to keep track of nodes seen while exploring current level, and we skip node only if a node is seen in global_seen, in other words, a node could be revisited in same level exploring, but not on next level or down.

"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        adj_list = collections.defaultdict(list)

        for word in wordList:
            for i, c in enumerate(word):
                gw = word[:i] + '*' + word[i+1:]
                if word not in adj_list[gw]:
                    adj_list[gw].append(word)

        @lru_cache(None)
        def get_neighbors(word):
            nonlocal adj_list
            res = []
            for i, c in enumerate(word):
                gw = word[:i] + '*' + word[i+1:]
                for w in adj_list[gw]:
                    res.append(w)

            return list(set(res))

        # inital queue and visited set
        dq, global_seen = [], set()
        for w in get_neighbors(beginWord):
            dq.append([w])
            global_seen.add(w)

        dq = collections.deque(dq)

        min_len = math.inf
        res = []
        while dq:
            l = len(dq)
            level_seen = set() # node visited on exploring this level, could be revisited for exploring this node, but not on next level
            while l:
                path = dq.popleft()
                cur = path[-1]
                if cur == endWord:
                    res.append(path)
                    min_len = min(min_len, len(path))
                for nxt in get_neighbors(cur):
                    if nxt not in global_seen:
                        dq.append(path+[nxt])
                        level_seen.add(nxt)
                l -= 1
            # 问题需要返回所有最短路径，所以是在检查完同一层所有可能节点之后，再将这些节点标记为已访问
            # 比如同一层有hog和log，都可以变成cog，如果在第一次访问到cog就直接把比较为已访问，那后面一条路径log->cog就被丢弃了
            global_seen = global_seen.union(level_seen)

        if res:
            return [[beginWord] + r for r in res if len(r) == min_len]
        else:
            return []



"""
BFS

bidirectional BFS
similar to above approach, but search from beginWord and endWord at same time, if they meet in middle, then we have a solution

TLE

"""

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return []
        n = len(wordList)
        m = len(beginWord)

        adj_list = collections.defaultdict(list)
        for word in wordList:
            for i in range(m):
                w = word[:i] + '*' + word[i + 1:]
                adj_list[w].append(word)

        # print('adj_list=%s' % adj_list)

        def get_neighbors(word):
            nonlocal adj_list
            res = []
            for i in range(m):
                w = word[:i] + '*' + word[i + 1:]
                res.extend(adj_list[w])

            return res

        q1 = collections.deque([(beginWord, [beginWord])])
        visited1 = {beginWord: [beginWord]}

#         print('q1=%s' % q1)
#         print('visited1=%s' % visited1)

        q2 = collections.deque([(endWord, [endWord])])
        visited2 = {endWord: [endWord]}

        # print('q2=%s' % q2)
        # print('visited2=%s' % visited2)

        res = []
        while q1 and q2:
            l1 = len(q1)
            l2 = len(q2)
            # print('q1=%s' % q1)
            # print('q2=%s' % q2)
            while l1 or l2:
                local_visited1 = {}
                if l1 > 0:
                    cur1, path1 = q1.popleft()
                    local_visited1[cur1] = path1
                    # print('get_neighbors(cur1)=%s' % (get_neighbors(cur1)))
                    for nei in get_neighbors(cur1):
                        if nei in visited2:
                            # print('path1 + visited2[nei][::-1]=%s' % (path1 + visited2[nei][::-1]))
                            res.append(path1 + visited2[nei][::-1])
                        if nei not in visited1:
                            q1.append((nei, path1 + [nei]))
                            local_visited1[nei] = path1 + [nei]
                    l1 -= 1

                local_visited2 = {}
                if l2 > 0:
                    cur2, path2 = q2.popleft()
                    local_visited2[cur2] = path2
                    # print('get_neighbors(cur2)=%s' % (get_neighbors(cur2)))
                    for nei in get_neighbors(cur2):
                        if nei in visited1:
                            # print('visited1[nei] + path2[::-1]=%s' % (visited1[nei] + path2[::-1]))
                            res.append(visited1[nei] + path2[::-1])
                        if nei not in visited2:
                            q2.append((nei, path2 + [nei]))
                            local_visited2[nei] = path2 + [nei]
                    l2 -= 1

            visited1.update(**local_visited1)
            visited2.update(**local_visited2)

        if res:
            min_len = min([len(r) for r in res])
            unique_res = []
            for r in res:
                if len(r) == min_len and r not in unique_res:
                    unique_res.append(r)
            return unique_res
        return []


"""
BFS modified

basically BFS traverse, but for each word we explored, we keep track of shortest path from beginWord to this word, and keep exploring further down, until we meet endWord

Since BFS traverse gives shortest distance to endWord, this gives all shortest path from beginWord to endWord.

Note: needs to mark nodes as visited (or removed from wordset here) only after one level is finished.

"""
import copy
from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset = set(wordList)

        if endWord not in wordset:
            return []

        layer = defaultdict(list)  # represent words in current layer
        layer[beginWord] = [[beginWord]]  # starting layer has just one word

        while layer:
            newlayer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                for i in range(len(word)):  # try to replace each char with each of 'a...z'
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newword = word[:i] + c + word[i + 1:]
                        if newword in wordset:
                            newlayer[newword] += [j + [newword] for j in layer[
                                word]]  # append newword to each sequence in layer[word] to form new sequnces up to newlayer
            wordset -= set(
                newlayer.keys())  # remove from wordset to avoid revisiting same nodes again, similar to global seen, but is marked only after one layer/level is done.

            layer = copy.copy(newlayer)  # move to next layer

        return []

def main():
    sol = Solution()
    assert sol.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]) == [ ["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"] ], 'fails'

    assert sol.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]) == [], 'fails'

if __name__ == '__main__':
   main()