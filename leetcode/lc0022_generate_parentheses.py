"""
22. Generate Parentheses
Medium

https://leetcode.com/problems/generate-parentheses/
"""
from typing import List

"""
Backtrack

base case:
    total length == n*2 (pairs)
recursive case:
    if left < n:
        backtrack(left+1, right, curr+'(')
    if right < left and right < n:
        backtrack(left, right+1, curr+')')

restriction is number of right parenthesis cannot be more than number of left parenthesis

time catalan(n) * O(n) which is O(4^n/sqrt(n))*(n))
space catalan(n)
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(left, right, curr):
            # print('left=%s right=%s curr=%s' % (left, right, curr))
            if len(curr) == n * 2:
                result.append(curr)
                return
            if left < n:
                backtrack(left + 1, right, curr + '(')
            if right < left and right < n:
                backtrack(left, right + 1, curr + ')')

        backtrack(0, 0, '')

        # print(result)

        return result

def main():
    sol = Solution()
    assert sol.generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"], 'fails'

    assert sol.generateParenthesis(1) == ["()"], 'fails'


if __name__ == '__main__':
   main()