"""
241. Different Ways to Add Parentheses
Medium

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
"""

from typing import List
from functools import lru_cache

"""
divide and conquer 
recursively solve each half, and generate all possible combinations using each result from left, and each result from right, with the operator in between
base case is pure digits (number)

time complexity O(P(N)) - Catalan number P(N) = sum(p1*p_n-1+p2*p_n-2+ ... + p_n-1*p1)
"""
class Solution:
    @lru_cache(None)
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        result = []
        for i, c in enumerate(input):
            if c in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                if c == '+':
                    result.extend([l+r for l in left for r in right])
                elif c == '-':
                    result.extend([l-r for l in left for r in right])
                elif c == '*':
                    result.extend([l*r for l in left for r in right])
        return result


def main():
    sol = Solution()
    assert sorted(sol.diffWaysToCompute("2-1-1")) == sorted([2, 0]), 'fails'

    assert sorted(sol.diffWaysToCompute("2*3-4*5")) == sorted([-34, -10, -14, -10, 10]), 'fails'

if __name__ == '__main__':
   main()