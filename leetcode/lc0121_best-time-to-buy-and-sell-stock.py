"""
121. Best Time to Buy and Sell Stock
Easy

"""
from typing import List

"""
DP

dp[i] := max profit we sell on day i

base case:
dp0[0] = 0 # cause we don't have stock to sell

transition: because we can only transact once, max profit today, is max of
1. bought before i-1, and sold on or before i-1, the max profit on i-1 is dp[i-1], will result in profit on i is dp[i-1] + prices[i]-prices[i-1]
2. we didn't buy before i-1, so dp[i-1] = 0, but we just buy on i-1, and sell today, the profit is prices[i]-prices[i-1]

dp[i] = max(dp[i-1]+prices[i]-prices[i-1], prices[i]-prices[i-1])

ans is max(dp)

"""


class Solution0:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0 for _ in range(n)]
        dp[0] = 0

        for i in range(1, n):
            dp[i] = max(dp[i - 1] + prices[i] - prices[i - 1], prices[i] - prices[i - 1])

        return max(dp)


"""
Brutal force with improvement

We calculate minprices[i] as minprices up to index[i]
"""


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        max_profit = 0
        for i in range(n):
            for j in range(i + 1, n):
                max_profit = max(max_profit, max(0, prices[j] - prices[i]))

        return max_profit


"""
Kadane's Algorithm

Using prices, we derive diffs between adjacent days, then the max profit is to get continuous subarray that gives max sum (profit), if the profit falls below zero, we will just reset it to 0 (start a new subarray)

calculate profit if always buy on day i-1, and sell on day i, profit is prices[i]-prices[i-1] = profit[i]
then buying on day j and sell on day i, the profit is basically profit[j+1] + ... + profit[i]
i.e., the profit for buying on day j and sell on day i, is the sum of diffs of two adjacent prices during these periods

max profit during entire period is to find max consecutive subarray sum

test input prices [7,1,5,3,6,4]
diff array is [0, -6, 4, -2, 3, -2]
max subarray sum is 4+(-2)+3 = 5

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        curr_max = 0  # max sum of current subarray
        global_max = 0  # global max sum of subarray
        for i in range(1, n):
            curr_max += prices[i] - prices[i - 1]
            curr_max = max(0, curr_max)  # reset to zero to start a new subarray
            global_max = max(global_max, curr_max)

        return global_max


"""
Sliding window

scan array once, for each number, remember min value to its left, and update max profit with that current price - min price to left

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        min_price = math.inf
        max_profit = 0

        for i in range(n):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return max_profit

def main():
    sol = Solution()
    assert sol.maxProfit([7,1,5,3,6,4]) == 5, 'fails'

    assert sol.maxProfit([7,6,4,3,1]) == 0, 'fails'

if __name__ == '__main__':
   main()