"""
122. Best Time to Buy and Sell Stock II
Easy

"""
from typing import List

"""
DP

dp0[i] := max profit on i-th day with no stock
dp1[i] := max profit on i-th day with stock at hand

base case
dp0[0] = 0
dp1[0] = -prices[0] (bought stock using money, so profit is -price)

transition:
dp0[i] = max(dp0[i-1], dp1[i-1]+prices[i])
dp1[i] = max(dp1[i-1], dp0[i-1]-prices[i])

ans is dp0[n-1]

time O(N)
space O(N) - can reduce to O(1) since dp{0,1}[i] only depends on dp{0,1}[i-1]
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp0 = [0 for _ in range(n)]
        dp1 = [0 for _ in range(n)]

        dp0[0] = 0
        dp1[0] = -prices[0]

        for i in range(1, n):
            dp0[i] = max(dp0[i - 1], dp1[i - 1] + prices[i])
            dp1[i] = max(dp1[i - 1], dp0[i - 1] - prices[i])

        return max(dp0[n - 1], dp1[n - 1])

def main():
    sol = Solution()
    assert sol.maxProfit([7,1,5,3,6,4]) == 7, 'fails'

    assert sol.maxProfit([1,2,3,4,5]) == 4, 'fails'

    assert sol.maxProfit([7,6,4,3,1]) == 0, 'fails'

if __name__ == '__main__':
   main()