"""
518. Coin Change 2
Medium

"""
from typing import List

from functools import lru_cache

"""
Dynamic Programming / Unbounded Knapsack problem

observation:
The problem asks for # combinations => means order we pick coins do not matter, need to be careful not to duplicate count coins in different order

DP state definition:
dp[i][j] : the number of combinations to make up amount j by using the first i types of coins coins[0:i]

State transition:

1. not using the i-th coin, only using the first i-1 coins to make up amount j, then we have dp[i-1][j] ways.
2. using the ith coin, since we can use unlimited same coin, we need to know how many ways to make up amount j - coins[i-1] by using first i coins(including ith), which is dp[i][j-coins[i-1]], here coins[i-1] means i-th coin, means we use firth i-th coins to make up amount j-coins[i-1], and then explicitly uses i-th coin once again (whose cost is coins[i-1])

    dp[i][j] =  dp[i-1][j]
              + dp[i-1][j] + dp[i][j-coins[i-1]]
              + dp[i-1][j] + dp[i][j-2*coins[i-1]]
              + dp[i-1][j] + dp[i][j-3*coins[i-1]]
              ...
              for all j such that j-k*coins[i-1] >=0
    dp[i][j] = sum(dp[i-1][j] + dp[i][j-k*coins[i-1]]) for 0<=k<=j//coins[i-1]

Initialization: dp[i][0] = 1 # to make amount 0, we have only one way, use no coins

time O(N*M^2)

TLE

mistakes:
1. used amount as outer loop, and coins as inner loop (via recursive implementation), this results in duplicate count as we are looking for # of combinations, not # of permutations

"""


class Solution0:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        # dp[0][j] = 0 for j > 0, since using no coin, cannot get to any non-zero amount

        for i in range(1, n + 1):
            for j in range(0, amount + 1):
                for k in range(j // coins[i - 1] + 1):
                    dp[i][j] += dp[i - 1][j - k * coins[i - 1]] if j - k * coins[i - 1] >= 0 else 0
                # print('i=%s j=%s dp=%s'  %(i, j, dp))

        return dp[-1][-1]


"""
Dynamic Programming

dp[i][j] := number of ways to achieve combination for amount j using only first i-th coins (coins[i-1])
Observing 

    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]] if j >= coins[i-1] else 0

we can improve by removing the inner loop on k

filling the dp table for example with amount = 5, coins = [1, 2, 5]

      amount  0  1  2  3  4  5
coins 0       1  0  0  0  0  0  
      1       1  1  1  1  1  1
      1,2     1  1  2  2  3  3
      1,2,5   1  1  2  2  3  4

for example, for coins=1,2 amount=5, 
if we do not use coin 2, there's 1 way dp[i-1][j] (from row above)
if we do use coin 2, then there's 2 ways dp[i][j-coin] (from 2 columns to left (amount==3))
so dp[2][5] = dp[1][5] + dp[2][5-2]

time O(N*M)

mistakes:
1 dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]] needs to handle negative amount correctly
    if j-coins[i-1] >= 0:
        dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
    else:
        dp[i][j] = dp[i-1][j]

  when write this in one line, there's needs to be parenthesis around the if else expression:
    dp[i][j] = dp[i-1][j] + (dp[i][j-coins[i-1]] if j-coins[i-1]>=0 else 0)

"""


class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                # 1. do not use coins[i]
                # 2. do use coins[i] at least once
                dp[i][j] = dp[i - 1][j] + (dp[i][j - coins[i - 1]] if j - coins[i - 1] >= 0 else 0)
                # print('i=%s j=%s' % (i, j))

        return dp[-1][-1]


"""
Dynamic Programming

since dp[i][j] only depends on dp[i-1][j] or dp[i][j...], we can reduce this 2D dp into 1D

alternative way of thinking about this dp implementation
1. add coins one-by-one, start from base case with "no coins"
2. for each added coin, compute recursively the number of combinations for each amoun of money from 0 to amount
"""


class Solution:
    def change(self, amount, coins):
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = dp[j] + dp[j - coin]

        return dp[amount]


def main():
    sol = Solution()
    assert sol.change(amount = 5, coins = [1, 2, 5]) == 4, 'fails'

    assert sol.change(amount = 3, coins = [2]) == 0, 'fails'

    assert sol.change(amount = 10, coins = [10]) == 1, 'fails'

if __name__ == '__main__':
   main()