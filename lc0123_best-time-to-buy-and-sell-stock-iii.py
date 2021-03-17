"""
123. Best Time to Buy and Sell Stock III
Hard

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Example 4:

Input: prices = [1]
Output: 0


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
"""
from typing import List

"""
DP

dp[i][k][0] := max profit on i-th day, with at most k-transactions, with no stock at hand
dp[i][k][1] := max profit on i-th day, with at most k-transactions, with 1 stock at hand

buy and sell is considered one transaction, so we only increase transaction count at buy time

base case:
dp[i][0][0] = 0 for i from 0 to n # on any day, if no trsaction allowed, no profit
dp[0][0][1] = -math.inf # on day 0, no transaction, cannot have stock

transition: the choices on any day i, is buy (if still allowed), rest, or sell (if has stock)
    # no stock on i-th day, could be from no stock on i-1 day, or have stock on i-1 th day, but sold on i-th day
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i]
    # has stock on i-th day, could be from has stock on i-1 day and rest, or no stock on i-1 day, and buy stock on i-day
    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])

time O(N)
space O(k*N)
"""


class Solution0:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(n)]

        for i in range(n):
            for k in range(2):
                if i - 1 == -1:
                    dp[i][k][0] = 0  # before we start, no stock, no profit
                    dp[i][k][1] = - prices[i]
                else:
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], (dp[i - 1][k - 1][0] if k - 1 >= 0 else 0) - prices[i])
                # print('i=%s k=%s dp=%s' % (i, k, dp))

        return dp[n - 1][1][0]


"""
DP

reduce dp table dimension

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0 for _ in range(2)] for _ in range(2)]
        prev_dp = [[0 for _ in range(2)] for _ in range(2)]

        for i in range(n):
            prev_dp = dp[:]
            for k in range(2):
                if i - 1 == -1:
                    dp[k][0] = 0  # before we start, no stock, no profit
                    dp[k][1] = - prices[i]
                else:
                    dp[k][0] = max(prev_dp[k][0], prev_dp[k][1] + prices[i])
                    dp[k][1] = max(prev_dp[k][1], (prev_dp[k - 1][0] if k - 1 >= 0 else 0) - prices[i])
                # print('i=%s k=%s dp=%s' % (i, k, dp))

        return dp[1][0]

def main():
    sol = Solution()
    assert sol.maxProfit(prices = [3,3,5,0,0,3,1,4]) == 6, 'fails'

    assert sol.maxProfit(prices = [1,2,3,4,5]) == 4, 'fails'

    assert sol.maxProfit(prices = [7,6,4,3,1]) == 0, 'fails'

if __name__ == '__main__':
   main()