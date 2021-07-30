"""
256. Paint House
Medium

1432

108

Add to List

Share
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Return the minimum cost to paint all houses.



Example 1:

Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
Example 2:

Input: costs = [[7,6,2]]
Output: 2


Constraints:

costs.length == n
costs[i].length == 3
1 <= n <= 100
1 <= costs[i][j] <= 20
"""
from typing import List

"""
DP

dp[i][j] := min accumulated cost for paiting house i with color j

base
dp[0][j] = costs[0][j] for j = 0, 1, 2

dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])+costs[i][j]

time O(3*N) = O(N)
space O(3*N) = O(N)
"""


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0 for _ in range(3)] for _ in range(n)]

        for j in range(3):
            dp[0][j] = costs[0][j]

        for i in range(1, n):
            for j in range(3):
                dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + costs[i][j]
                # print('i=%s j=%s dp=%s' % (i, j, dp))

        return min(dp[n - 1][:])

def main():
    sol = Solution()
    assert sol.minCost(costs = [[17,2,17],[16,16,5],[14,3,19]]) == 10, 'fails'

    assert sol.minCost(costs = [[7,6,2]]) == 2, 'fails'

if __name__ == '__main__':
   main()