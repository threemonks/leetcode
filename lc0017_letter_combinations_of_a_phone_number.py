"""
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

"""
from itertools import product
from typing import List


class Solution0:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mappings = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno',
                    7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

        # construct Cartesian product of different letters list of each digits
        n = len(digits)
        chars_lists = []
        for i in range(n):
            d = int(digits[i])
            chars = mappings[d]
            chars_lists.append(chars)

        res = product(*chars_lists)

        return [''.join(r) for r in res]


"""
backtracking
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mappings = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno',
                    7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

        n = len(digits)
        res = []

        def backtrack(ds, path):
            if len(path) == n:
                res.append(''.join(path))
            if ds:
                for c in mappings[int(ds[0])]:
                    backtrack(ds[1:], path + [c])

        backtrack(digits, [])

        return res


def main():
    sol = Solution()
    assert sol.letterCombinations(digits = "23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"], 'fails'

    assert sol.letterCombinations(digits = "") == [], 'fails'

    assert sol.letterCombinations(digits = "2") == ["a","b","c"], 'fails'

if __name__ == '__main__':
   main()