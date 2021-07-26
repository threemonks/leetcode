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
import operator
from typing import List
from functools import lru_cache

"""
divide and conquer 
recursively solve each half, and generate all possible combinations using each result from left, and each result from right, with the operator in between
base case is pure digits (number)

time complexity O(P(N)) - Catalan number P(N) = sum(p1*p_n-1+p2*p_n-2+ ... + p_n-1*p1)
"""
class Solution0:
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


"""
Divide & Conquer - by operator

divide and conquer, always split at operator, recursively solve left and right, get all possible values from left, and all possible values from right, pair each possible value in left with each possible value in right, to get all possible final values

base case is pure digit

divide and conquer

time O(P(N)) where P(N) is Catalan number P(N) = C(2n, n) - C(2n, n+1)

"""

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}

        def helper(s):
            n = len(s)
            if s.isdigit():
                return [int(s)]
            ans = []
            for i in range(1, n - 1):
                c = s[i]
                if c in '+-*':
                    left_result = helper(s[:i])
                    right_result = helper(s[i + 1:])
                    for l in left_result:
                        for r in right_result:
                            ans.append(ops[c](l, r))

            return ans

        return helper(expression)


def main():
    sol = Solution()
    assert sorted(sol.diffWaysToCompute("2-1-1")) == sorted([2, 0]), 'fails'

    assert sorted(sol.diffWaysToCompute("2*3-4*5")) == sorted([-34, -10, -14, -10, 10]), 'fails'

if __name__ == '__main__':
   main()