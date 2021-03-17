"""
188. Best Time to Buy and Sell Stock IV
Hard

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


Constraints:

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""
from typing import List

"""
dp[i][k][0] := max profit on day i with at most k transactions, no stock at hand on i-day
dp[i][k][1] := max profit on day i with at most k transactions, with stock at hand on i-day

Note we consider transaction count increase when buy, but not when sell, since one buy and sell are considered one tx

transition
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]) # either rest, or sell on i
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]) # either rest, or buy on i
"""


class Solution:
    def maxProfit(self, K: int, prices: List[int]) -> int:
        if not prices or K <= 0:
            return 0
        n = len(prices)

        dp = [[[0 for _ in range(2)] for _ in range(K)] for _ in range(n)]

        for i in range(n):
            for k in range(K):
                if i - 1 == -1:
                    # base case
                    dp[i][k][0] = 0  # on day -1, no stock, no profit
                    dp[i][k][1] = -prices[i]  # on day -1, could not have stock
                else:
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], (dp[i - 1][k - 1][0] if k - 1 >= 0 else 0) - prices[i])
                # print('i=%s k=%s dp=%s' % (i, k, dp))

        return dp[n - 1][K - 1][0]


def main():
    sol = Solution()
    assert sol.maxProfit(k = 2, prices = [2,4,1]) == 2, 'fails'

    assert sol.maxProfit(k = 2, prices = [3,2,6,5,0,3]) == 7, 'fails'


if __name__ == '__main__':
   main()