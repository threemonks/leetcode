"""
131. Palindrome Partitioning
Medium

https://leetcode.com/problems/palindrome-partitioning/
"""
from typing import List

"""
Backtrack w/ exhaustive search (loop through all possible length prefix substring)

use backtrack exhaustive search to find all sublists, and prune that exploration path as soon as any one of the sublist if found to be not palindrome

mistakes:
1. this is exhaustive search, so we need to keep the partial sublists found so far
2. s == s[::-1] for testing palindrome
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def backtrack(s, path):
            # print('s=%s path=%s' % (s, path))
            # base case
            if not s:
                result.append(path)
                return

            # exhaustive search for sublists with all possible length
            # choose prefix substring s[:i]
            # recursive exploration
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    backtrack(s[i:], path+[s[:i]])
            # unchoose prefix substring s[:i]

        backtrack(s, [])

        return result


def main():
    sol = Solution()
    assert sol.partition(s = "aab") ==[["a","a","b"],["aa","b"]], 'fails'

    assert sol.partition(s = "a") == [["a"]], 'fails'



if __name__ == '__main__':
   main()