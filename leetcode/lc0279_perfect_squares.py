"""
279. Perfect Squares
Medium

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""
import math

"""
dfs with memo
"""
from functools import lru_cache
class Solution:
    def numSquares(self, n: int) -> int:
        memo = {0: 0, 1: 1}
        @lru_cache(None)
        def helper(num):
            if num in memo:
                return memo[num]
            else:
                res = num
                nsqrt = int(math.floor(math.sqrt(num)))
                for i in range(1, nsqrt+1):
                    res = min(res, 1 + helper(num-i**2))
                memo[num] = res
                return res

        return helper(n)

"""
dp[n] : min number of squares required to sum to n
dp[n] = min (
    for i in range(1, floor(sqrt_of_n)):
        1+dp[n-i**2]
)
"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        n_sqrt = math.floor(math.sqrt(n))
        squares = list([ns**2 for ns in range(1, n_sqrt+1)])

        for i in range(2, n+1):
            dp[i] = i
            i_sqrt = math.floor(math.sqrt(i))
            for k in range(1, i_sqrt+1):
                dp[i] = min(dp[i], 1+dp[i-k**2])

        return dp[n]

def main():
    sol = Solution()
    assert sol.numSquares(12) == 3, 'fails'

    assert sol.numSquares(13) == 2, 'fails'

if __name__ == '__main__':
   main()