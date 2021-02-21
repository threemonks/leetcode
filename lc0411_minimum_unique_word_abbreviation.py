"""
411. Minimum Unique Word Abbreviation
Hard

https://leetcode.com/problems/minimum-unique-word-abbreviation/

"""
import heapq
import operator
from typing import List
from functools import lru_cache

"""
Backtrack

1. Use backtrack to generate all abbreviations for target
2. sort generated abbreviation list by length(By using Priority Queue)
3. use recursive match to compare abbreviation with dictionary word, and keep shorted one that does not match any word in dictionary

observation:

find all possible abbreviations, then check against dictionary and remove invalid ones, and pick the shortest length among remaining valid ones

optimization tips:
1. any dictionary word that does not have same length as target word can be disarded
2. any dictionary word that does not match target word in any position can be discarded
3. use priority queue to keep abbreviations sorted by length obtained at time when the abbreviation is generated

"""


class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        # Throw out wrong-length words
        dictionary = [word for word in dictionary if len(word) == len(target)]

        if not dictionary:
            return str(len(target))

        # Throw out words not matching the target in any position.
        dictionary = [word for word in dictionary if any(map(operator.eq, word, target))]
        if not dictionary:
            return target if len(target) < 2 else target[0] + str(len(target) - 1)

        m = len(target)
        n = len(dictionary)

        queue = []
        heapq.heapify(queue)

        @lru_cache(None)
        def helper(idx, path, length):
            """ generate all abbreviations  """
            # print('idx=%s path=%s' % (idx, path))
            if idx == m:
                heapq.heappush(queue, (length, path))
                return

            # explore
            for i in range(idx, m):

                # choose ith
                # dot not abbreviate at i-th position
                helper(i + 1, path + target[idx:i + 1], length + i + 1 - idx)

                # abbreviate at i-th position, the following char must be not abbreviated
                if i + 1 < m:
                    helper(i + 2, path + str(i - idx + 1) + target[i + 1], length + 2)
                elif i + 1 <= m:
                    helper(i + 1, path + str(i - idx + 1), length + 1)

                # unchoose ith

        # generate all abbreviations
        helper(0, '', 0)

        @lru_cache(None)
        def match(abbrev, word):
            """ match given abbreviation with a dictionary word  """
            m, n = len(abbrev), len(word)
            if not m and not n:
                return True
            elif (not m and n) or (m and not n):
                return False

            if abbrev[0].isalpha():
                if abbrev[0] == word[0]:  # match first char
                    return match(abbrev[1:], word[1:])
                elif abbrev[0] != word[0]:
                    return False
            else:  # abbrev starts with digit
                i, num = 0, ''
                while i < m and abbrev[i].isdigit():
                    num += abbrev[i]
                    i += 1
                j = int(num) if num else 0
                if abbrev[1:] == '' and j == len(word):
                    return True
                elif j > len(word):
                    return False
                else:  # j <= len(word)
                    return match(abbrev[i:], word[j:])

        ans = (len(target), target)
        while queue:
            l, abbr = heapq.heappop(queue)
            matched = False
            for w in dictionary:
                if match(abbr, w):
                    matched = True
                    break
            if not matched:
                if l < ans[0]:
                    ans = (l, abbr)

        helper.cache_clear()
        match.cache_clear()

        return ans[1]


def main():
    sol = Solution()

    assert sol.minAbbreviation(target = "apple", dictionary = ["blade"]) == 'a4', 'fails'

    assert sol.minAbbreviation(target = "apple", dictionary = ["blade","plain","amber"]) == "1p3", 'fails'

if __name__ == '__main__':
   main()