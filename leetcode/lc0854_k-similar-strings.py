"""
854. K-Similar Strings
Hard

965

56

Add to List

Share
Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.



Example 1:

Input: s1 = "ab", s2 = "ba"
Output: 1
Explanation: The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".
Example 2:

Input: s1 = "abc", s2 = "bca"
Output: 2
Explanation: The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --> "bac" --> "bca".


Constraints:

1 <= s1.length <= 20
s2.length == s1.length
s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
s2 is an anagram of s1.

"""
"""
BFS

do BFS traverse to find shortest steps to visited all nodes
string is the node of graph
a swap is the edge
each string with a variation (one swap) is a new neighbor node
to get neighbor node, swap one charater with another different char in the string to obtain neighbor node

using BFS to find shortest path would be minimal swap to get to the target string

"""
from collections import defaultdict, deque
from functools import lru_cache


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        @lru_cache(None)
        def nei(X):
            n = len(X)

            # find first character in A that does not match the char in B at same index
            i = 0
            while X[i] == B[i]:
                i += 1

            for j in range(i + 1, n):
                if X[j] == B[i]:  # swap with same char at different location makes no sense
                    yield X[:i] + X[j] + X[i + 1:j] + X[i] + X[j + 1:]

        q = deque([(A, 0)])  # node, steps
        seen = {A}
        while q:
            x, d = q.popleft()
            if x == B:
                return d
            for nb in nei(x):
                if nb not in seen:
                    seen.add(nb)
                    q.append((nb, d + 1))


class Solution1:
    def kSimilarity(self, A, B):
        def nei(x):
            i = 0
            while x[i] == B[i]: i += 1
            for j in range(i + 1, len(x)):
                if x[j] == B[i]: yield x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:]

        q, seen = [(A, 0)], {A}
        for x, d in q:
            if x == B: return d
            for y in nei(x):
                if y not in seen:
                    seen.add(y), q.append((y, d + 1))


def main():
    sol = Solution()
    assert sol.kSimilarity(A = "ab", B = "ba") == 1, 'fails'

    assert sol.kSimilarity(A = "abc", B = "bca") == 2, 'fails'

if __name__ == '__main__':
   main()