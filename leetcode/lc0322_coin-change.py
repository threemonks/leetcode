"""
322. Coin Change
Medium

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""
import math
from functools import lru_cache
from typing import List

"""
Dynamic Programming

top down / recursive

time O(N*M) - N # of coins, M # target amount
space O(M)
mistakes:
1. early termination, only try coins that are less than target amount, and stop (return 0) if target amount <= 0
"""


class Solution0:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def helper(target):
            nonlocal coins
            if target == 0:
                return 0
            ans = math.inf
            for c in coins:
                if c > target:
                    continue
                ans = min(ans, 1 + helper(target - c))

            return ans

        res = helper(amount)

        return res if res < math.inf else -1


"""
DP

bottom up

transition
dp[i] := minimum number of coins for amount i, is the min # of coins of all possible previous target amount plus another coin in coins

dp[i] = min(math.inf, [1+dp[j] for j from 1 ... i-1 if i-j is in coins ])
"""


class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for j, c in enumerate(coins):
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])

        ans = dp[amount]
        return ans if ans < math.inf else -1


from collections import deque

"""
BFS

consider each added coin is another level, and different coin combinations on each level is the different path, we are trying to find a shortest path to destination with value amount

"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dq = deque([(0, 0)])
        visited = set([0])

        while dq:
            cur_coins, cur_val = dq.popleft()
            if cur_val == amount:
                return cur_coins
            for c in coins:
                if c + cur_val <= amount and c + cur_val not in visited:
                    dq.append((1 + cur_coins, c + cur_val))
                    visited.add(c + cur_val)

        # no valid combination found
        return -1


def main():
    sol = Solution()
    assert sol.coinChange(coins = [1,2,5], amount = 11) == 3, 'fails'

    assert sol.coinChange(coins = [2], amount = 3) == -1, 'fails'


if __name__ == '__main__':
   main()