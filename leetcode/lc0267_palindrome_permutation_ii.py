"""
267. Palindrome Permutation II
Medium

https://leetcode.com/problems/palindrome-permutation-ii/
"""
from typing import List
from functools import lru_cache
from collections import Counter

"""
generate all permutations and then check palindrome and remove duplicate

factorial(12) = 10^10
TLE
"""


class Solution0:
    def generatePalindromes(self, s: str) -> List[str]:
        n = len(s)

        permutations = set()

        @lru_cache(None)
        def helper(path, s):
            # print('path=%s s=%s' % (path, s))
            if not s:
                permutations.add(path)
                return

            for i in range(len(s)):
                helper(path + s[i], s[:i] + s[i + 1:])

        helper('', s)

        result = set()
        for p in permutations:
            if p == p[::-1]:
                result.add(p)

        return list(result)


"""
Backtracking

basically generate palindrome string directly using all chars and their counts

Note:
1. filter out invalid strings (odd number of chars != 1)
2. special handling of odd count char (has to be in middle of palindrome)
"""


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        n = len(s)
        counter = Counter(s)
        odd_count = 0
        odd_count_char = ''
        for ch, cnt in counter.items():
            if cnt % 2 == 1:
                odd_count += 1
                odd_count_char = ch

        # if there's more than one char appear odd times, we cannot have palindrome perms
        if odd_count > 1:
            return []

        result = []

        def permute(sofar, counter):
            if len(sofar) == n:
                result.append(sofar)
                return

            for ch, cnt in counter.items():
                if cnt:
                    # use character ch at both front and back (palindrome required)
                    counter[ch] -= 2
                    # explore with this choice of ch
                    permute(ch + sofar + ch, counter)
                    # restore / remove char ch
                    counter[ch] += 2

        sofar = ''
        if odd_count_char:
            sofar = odd_count_char
            counter[odd_count_char] -= 1

        permute(sofar, counter)

        # print(result)

        return result

def main():
    sol = Solution()
    assert sorted(sol.generatePalindromes("aabb")) == sorted(["abba", "baab"]), 'fails'

    assert sol.generatePalindromes("abc") == [], 'fails'


if __name__ == '__main__':
   main()