"""
https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/qi-ta-suan-fa-wen-ti/tuan-mie-gu-piao-wen-ti

https://labuladong.gitbook.io/algo-en/i.-dynamic-programming/besttimetobuyandsellstock

for state1 in all values of state1：
    for state2 in in all values of state2：
        for ...
            dp[state1][state2][...] = best_choice(choice1, choice2 ...)

"""
import math
from typing import List

"""
* States

dp[i][k][0 or 1]
0 <= i <= n-1, 1 <= k <= K
(n means the number of days, the uppercase K means the maximum number of allowed transactions)
This problem has a total of n × K × 2 states, and we can solve it all by exhausting them.

for 0 <= i < n:
    for 1 <= k <= K:
        for s in {0, 1}:
            dp[i][k][s] = max(buy, sell, rest)
            
* State transition

dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
              max( choose rest  ,          choose sell      )

Explanation: I don’t hold stocks today. There are two possibilities:
1) Either I didn’t hold stocks yesterday, and then choose to rest today, so I still don’t hold stocks today.
2) Either I held stocks yesterday, but today I chose to sell, so I don't hold stocks today.

dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
              max( choose rest  ,            choose buy         )

Explanation: Today I hold stocks. There are two possibilities:
1) Either I held stocks yesterday and chose to rest today, so I still hold stocks today.
2) Either I didn't hold stocks yesterday, but today I chose to buy, so today I hold stocks.

* Base case

dp[-1][k][0] = 0
Explanation: Because i starts at 0, i = -1 means it hasn't started yet, and the profit at this time is of course 0.

dp[-1][k][1] = -infinity
Explanation: Before the beginning, it was impossible to hold stocks, which is expressed as negative infinity.

dp[i][0][0] = 0
Explanation: Because k starts from 1, k = 0 means that trading is not allowed at all, and profit is of course 0 at this time.

dp[i][0][1] = -infinity
Explanation: It is impossible to hold stocks when trading is not allowed. This possibility is expressed by negative infinity.


base case：
dp[-1][k][0] = dp[i][0][0] = 0
dp[-1][k][1] = dp[i][0][1] = -infinity

state transition equation：
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
"""

"""
First Problem: k = 1

dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i]) 
            = max(dp[i-1][1][1], -prices[i])
Explanation：Base case of k = 0，so dp[i-1][0][0] = 0

Now we find that k is 1 and will not change, that is, k has no effect on the state transition. We can further simplify it with removing all k:
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], -prices[i])

"""

class Solution:
    # k == 1
    def maxProfit_k_1(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(n)] for _ in range(2)]

        for i in range(n):
            if i -1 == -1: # handle boundary i=-1
                dp[i][0] = 0
                dp[i][1] = -prices[0]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], -prices[i])

        return dp[n - 1][0]

    # observing that dp[i] only depends on dp[i-1], we can simplify the above to use one variable instead of array
    # and simplify the boundary condition
    # k == 1
    def maxProfit_k_1_1(self, prices: List[int]) -> int:
        n = len(prices)
        # base case: dp[-1][0] = 0, dp[-1][1] = -infinity
        dp_i_0, dp_i_1 = 0, -math.inf
        for i in range(n):
            # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            # dp[i][1] = max(dp[i-1][1], -prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])

        return dp_i_0

    """
Second Problem: k = +infinity

If k is positive infinity, then k and k-1 can be considered the same. The framework can be rewritten like this:

dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
            = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])

We find that k in the array has not changed, which means that we do not need to record the state of k:
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
"""

    def maxProfit_k_inf(self, prices: List[int]) -> int:
        n = len(prices)
        # base case: dp[-1][0] = 0, dp[-1][1] = -infinity
        dp_i_0, dp_i_1 = 0, -math.inf
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            # dp[i][1] = max(dp[i-1][1], -prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])

        return dp_i_0

    """    

Third Problem: k = +infinity with cooldown

dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
Explanation: When we choose to buy on day i, the state of i-2 should be transferred instead of i-1.

"""

    def maxProfit_w_cool(self, prices: List[int]) -> int:
        n = len(prices)
        # base case: dp[-1][0] = 0, dp[-1][1] = -infinity
        dp_i_0, dp_i_1 = 0, -math.inf
        dp_pre_0 = 0 # variable representing dp[i-2][0]
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            # dp[i][1] = max(dp[i-1][1], -prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp

        return dp_i_0

    """
Fourth Problem: k = +infinity with fee

dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
Explanation: That means that the price of buying stocks has risen.
It's the same case that we substract it in the first formula, which is equivalent to reducing the price of the stock sold.

"""
    def maxProfit_w_fee(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # base case: dp[-1][0] = 0, dp[-1][1] = -infinity
        dp_i_0, dp_i_1 = 0, -math.inf
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            # dp[i][1] = max(dp[i-1][1], -prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i] - fee)

        return dp_i_0


    """
Fifth Problem: k = 2

The original state transition equation, where there is no simplification
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

For k = 2 or other positive integer (not infinity), we must exhaust all states, i.e., 
iterate through all possible values of k to complete transition from all possible states, to all other possible states in next stage

int max_k = 2;
int[][][] dp = new int[n][max_k + 1][2];
for (int i = 0; i < n; i++) {
    for (int k = max_k; k >= 1; k--) {
        if (i - 1 == -1) { /* Deal with the base case */ }
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]);
    }
}
// Exhaust n × max_k × 2 states, correct!
return dp[n - 1][max_k][0];

For k = 2, we explicitly write cases for k == 1 and k ==2 
dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
dp[i][1][1] = max(dp[i-1][1][1], -prices[i])

"""

    def maxProfit_k_2(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i10, dp_i11 = 0, -math.inf
        dp_i20, dp_i21 = 0, -math.fin
        for i in range(n):
            dp_i20 = max(dp_i20, dp_i21 + prices[i])
            dp_i21 = max(dp_i21, dp_i10 - prices[i])
            dp_i10 = max(dp_i10, dp_i11 + prices[i])
            dp_i11 = max(dp_i11, - prices[i])

        return dp_i20

    """

Sixth Problem: k = any integer

We can reuse the code above for k == 2 cases, but if k is very large, the dp array might overflow
since we know that if k > len(prices)/2, then there is basically no limit, because it takes two days to complete a buy and sell
so we could treat it as no limit if k > len(prices)/2
"""


    def maxProfit_k_2(self, max_k: int, prices: List[int]) -> int:
        n = len(prices)
        if max_k > n/2:
            return self.maxProfit_k_inf(prices)
        dp = [[[0 for _ in range(2)] for _ in range(max_k+1)] for _ in range(n)]
        for i in range(n):
            for k in range(max_k, 0, -1):
                if (i-1==-1):
                    # handle boundary case
                    pass
                else:
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return dp[n-1][max_k][0]

"""
int maxProfit_k_any(int max_k, int[] prices) {
    int n = prices.length;
    if (max_k > n / 2) 
        return maxProfit_k_inf(prices);

    int[][][] dp = new int[n][max_k + 1][2];
    for (int i = 0; i < n; i++) 
        for (int k = max_k; k >= 1; k--) {
            if (i - 1 == -1) { /* Deal with the base case */ }
            dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
            dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]);     
        }
    return dp[n - 1][max_k][0];
}
"""