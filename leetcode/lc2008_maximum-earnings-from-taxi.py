"""
2008. Maximum Earnings From Taxi
Medium

850

16

Add to List

Share
There are n points on a road you are driving your taxi on. The n points on the road are labeled from 1 to n in the direction you are going, and you want to drive from point 1 to point n to make money by picking up passengers. You cannot change the direction of the taxi.

The passengers are represented by a 0-indexed 2D integer array rides, where rides[i] = [starti, endi, tipi] denotes the ith passenger requesting a ride from point starti to point endi who is willing to give a tipi dollar tip.

For each passenger i you pick up, you earn endi - starti + tipi dollars. You may only drive at most one passenger at a time.

Given n and rides, return the maximum number of dollars you can earn by picking up the passengers optimally.

Note: You may drop off a passenger and pick up a different passenger at the same point.



Example 1:

Input: n = 5, rides = [[2,5,4],[1,5,1]]
Output: 7
Explanation: We can pick up passenger 0 to earn 5 - 2 + 4 = 7 dollars.
Example 2:

Input: n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
Output: 20
Explanation: We will pick up the following passengers:
- Drive passenger 1 from point 3 to point 10 for a profit of 10 - 3 + 2 = 9 dollars.
- Drive passenger 2 from point 10 to point 12 for a profit of 12 - 10 + 3 = 5 dollars.
- Drive passenger 5 from point 13 to point 18 for a profit of 18 - 13 + 1 = 6 dollars.
We earn 9 + 5 + 6 = 20 dollars in total.


Constraints:

1 <= n <= 10^5
1 <= rides.length <= 3 * 10^4
rides[i].length == 3
1 <= starti < endi <= n
1 <= tipi <= 10^5
"""

"""
DP

n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
dp[i] : max $ we get when arriving at i (which is end of each route)
dp[i] = max(
            max(dp[j] + ride profit for each ride ending at j), # pick a ride
            dp[i-1] # don't pick a ride
            )

time O(N*log(N))
"""
from typing import List
from collections import defaultdict


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0 for _ in range(n + 1)]
        rides = sorted(rides, key=lambda r: r[1])
        ridesEndAt = defaultdict(list)

        for start, end, dollar in rides:
            ridesEndAt[end].append((start, end - start + dollar))

        # print(f"{ridesEndAt = }")

        for i in range(1, n + 1):
            for start, earnings in ridesEndAt[i]:
                dp[i] = max(dp[i], earnings + dp[start])
            dp[i] = max(dp[i], dp[i - 1])
            # print(f"{i = } {dp = }")

        return dp[-1]

def main():
    sol = Solution()
    assert sol.maxTaxiEarnings(n = 5, rides = [[2,5,4],[1,5,1]]) == 7, 'fails'

    assert sol.maxTaxiEarnings(n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]) == 20, 'fails'


if __name__ == '__main__':
   main()