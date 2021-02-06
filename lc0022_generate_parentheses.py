"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8

"""
from typing import List

"""
backtrack

time (4^n/sqrt(n))
space (4^n/sqrt(n)) 
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(res, left=0, right=0):
            nonlocal result
            if len(res) == n * 2:
                result.append(res)
            if left >= n and right >= n:
                return
            if left < n:
                helper(res + '(', left + 1, right)
            if right < left:
                helper(res + ')', left, right + 1)

        helper('', left=0, right=0)

        return result


def main():
    sol = Solution()
    assert sol.generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"], 'fails'

    assert sol.generateParenthesis(1) == ["()"], 'fails'


if __name__ == '__main__':
   main()