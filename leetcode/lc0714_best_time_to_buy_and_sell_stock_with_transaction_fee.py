"""
714. Best Time to Buy and Sell Stock with Transaction Fee
Medium

Share
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""
from typing import List

"""
DP

dp0[i] := value on day i, with no stock at hand
dp1[i] := value on day i, with stock at hand

dp1[i] = max(dp1[i-1], dp0[i-1]-prices[i])
dp0[i] = max(dp0[i-1], dp1[i-1]-fee+prices[i])

time O(n)
space O(n) - can simplify to O(1) since each dp uses only the immediate previous value
"""


class Solution0:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        dp0 = [0 for _ in range(n)]
        dp1 = [0 for _ in range(n)]
        dp0[0] = 0
        dp1[0] = -prices[0]

        for i in range(1, n):
            dp1[i] = max(dp1[i - 1], dp0[i - 1] - prices[i])
            dp0[i] = max(dp0[i - 1], dp1[i - 1] - fee + prices[i])

        return max(dp0[-1], dp1[-1])


"""
let dp0[i] := max profit on day i without stock
    dp1[i] := max profit on day i with stock

goal is dp0[n-1]

transition on day i from day i-1
dp0[i] = max(dp0[i-1], dp1[i-1] + prices[i] - fee) # transaction fee on sell only
dp1[i] = max(dp1[i-1], dp0[i-1] - prices[i])

mistakes:
1. dp1[i] = max(dp1[i-1], dp0[i-1] - prices[i]) since it is purchased on day i, so the price is prices[i]
"""


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp0 = [0 for _ in range(n)]
        dp1 = [0 for _ in range(n)]
        dp0[0] = 0
        dp1[0] = -prices[0]

        for i in range(1, n):
            dp0[i] = max(dp0[i - 1], dp1[i - 1] + prices[i] - fee)
            dp1[i] = max(dp1[i - 1], dp0[i - 1] - prices[i])
            # print('i=%s dp0[i]=%s dp1[i]=%s' % (i, dp0[i], dp1[i]))

        return max(dp0[n - 1], dp1[n - 1])


def main():
    sol = Solution()
    assert sol.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2) == 8, 'fails'

if __name__ == '__main__':
   main()