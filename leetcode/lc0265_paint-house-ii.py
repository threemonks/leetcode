"""
265. Paint House II
Hard

647

26

Add to List

Share
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
Return the minimum cost to paint all houses.



Example 1:

Input: costs = [[1,5,3],[2,9,4]]
Output: 5
Explanation:
Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
Example 2:

Input: costs = [[1,3],[2,4]]
Output: 5


Constraints:

costs.length == n
costs[i].length == k
1 <= n <= 100
1 <= k <= 20
1 <= costs[i][j] <= 20


Follow up: Could you solve it in O(nk) runtime?
"""
from typing import List

"""
DP

dp[i][j] := cost after painting row i with color j

dp[i+1][j] = min(costs[i][j]+dp[i-1][k] for k != j)

time O(N*K^2)
space O(N*K) - can simplify into O(N) space by using 1-d array for dp

follow up:
1. optimize time: since dp[i+1][j] is only dependent on the minimum (and second minimum since the one with same j cannot be derived from the item with same column j from previous row) from previous row, thus if we keep track of these two values from previous row, we can reduce time to O(N*K).

mistakes:
1. dp[i+1][j] = min(costs[i][j]+dp[i-1][k] for k != j)

"""


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # dp[i][prev_color]
        m, n = len(costs), len(costs[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            dp[0][j] = costs[0][j]

        for i in range(1, m):
            for j in range(n):
                dp[i][j] = min([costs[i][j] + dp[i - 1][k] for k in range(n) if k != j])

        return min(dp[m - 1])


def main():
    sol = Solution()

    assert sol.minCostII(costs = [[1,5,3],[2,9,4]]) == 5, 'fails'

    assert sol.minCostII(costs = [[1,3],[2,4]]) == 5, 'fails'



if __name__ == '__main__':
   main()