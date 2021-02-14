"""
784. Letter Case Permutation
Medium

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
Example 4:

Input: S = "0"
Output: ["0"]


Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

"""
from typing import List

"""
backtrack (recursion)
"""


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        n = len(S)

        result = []
        self.backtrack(S, 0, [], result)
        return [''.join(r) for r in result]

    def backtrack(self, S, cur, path, result):
        n = len(S)
        if len(path) == n:
            result.append(path)
            return
        for i in range(cur, n):
            self.backtrack(S, i + 1, path + [S[i]], result)
            if S[i].islower():
                self.backtrack(S, i + 1, path + [S[i].upper()], result)
            if S[i].isupper():
                self.backtrack(S, i + 1, path + [S[i].lower()], result)


"""
iterative - loop through index of the string, add each char in sequence with one version of the char itself, one version of different case than original
"""


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        n = len(S)

        result = []
        paths = [[]]
        for i in range(n):
            prev_paths = list(paths)
            paths = []
            for path in prev_paths:
                paths.append(path + [S[i]])
                if S[i].islower():
                    paths.append(path + [S[i].upper()])
                if S[i].isupper():
                    paths.append(path + [S[i].lower()])

            for path in paths:
                if len(path) == n:
                    result.append("".join(path))

        return result

def main():
    sol = Solution()
    assert sorted(sol.letterCasePermutation("a1b2")) == sorted(["a1b2","a1B2","A1b2","A1B2"]), 'fails'

    assert sorted(sol.letterCasePermutation("3z4")) == sorted(["3z4","3Z4"]), 'fails'

    assert sorted(sol.letterCasePermutation("12345")) == sorted(["12345"]), 'fails'

    assert sorted(sol.letterCasePermutation("0")) == sorted(["0"]), 'fails'

    assert sorted(sol.letterCasePermutation("C")) == sorted(["c", "C"]), 'fails'


if __name__ == '__main__':
   main()