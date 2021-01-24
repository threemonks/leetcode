"""
1595. Minimum Cost to Connect Two Groups of Points
Hard

You are given two groups of points where the first group has size1 points, the second group has size2 points, and size1 >= size2.

The cost of the connection between any two points are given in an size1 x size2 matrix where cost[i][j] is the cost of connecting point i of the first group and point j of the second group. The groups are connected if each point in both groups is connected to one or more points in the opposite group. In other words, each point in the first group must be connected to at least one point in the second group, and each point in the second group must be connected to at least one point in the first group.

Return the minimum cost it takes to connect the two groups.



Example 1:


Input: cost = [[15, 96], [36, 2]]
Output: 17
Explanation: The optimal way of connecting the groups is:
1--A
2--B
This results in a total cost of 17.
Example 2:


Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
Output: 4
Explanation: The optimal way of connecting the groups is:
1--A
2--B
2--C
3--A
This results in a total cost of 4.
Note that there are multiple points connected to point 2 in the first group and point A in the second group. This does not matter as there is no limit to the number of points that can be connected. We only care about the minimum total cost.
Example 3:

Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
Output: 10


Constraints:

size1 == cost.length
size2 == cost[i].length
1 <= size1, size2 <= 12
size1 >= size2
0 <= cost[i][j] <= 100
"""
import math
from functools import lru_cache
from typing import List

"""
Use DP + bitmask - bitmask to represents the state of point in right group, whether it has been used by given node i in group 1 or not
Two steps:
    1. connect all group 1 nodes to group2 nodes, each group1 node have one edge going out to group 2, but each group 2 node might have more than one incoming
    2. for any group2 node that have no connection yet, connect them to group 1 node with least cost
"""


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        # print('m=%s n=%s' % (m, n))

        # get minimum cost to any point in group 1 for any point in group 2

        min_cost = [min(c) for c in list(zip(*cost))]

        @lru_cache(None)
        def dp(i, mask):
            if i == m:
                # if there's any points in right group still not connected, connect back to point in left group with minimum cost
                # for any bit in mask that is not set, connect that back to group 1 with min cost
                ans = 0
                for j in range(n):
                    if mask & (1 << j) == 0:  # 0110 & 1000 == 0 > jth bit not set
                        ans += min_cost[j]

                return ans

            ans = math.inf
            for j in range(n):
                # print('i=%s j=%s' % (i, j))
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))

            return ans

        return dp(0, 0)


def main():
    sol = Solution()
    assert sol.connectTwoGroups([[15, 96], [36, 2]]) == 17, 'fails'

    assert sol.connectTwoGroups([[1, 3, 5], [4, 1, 1], [1, 5, 3]]) == 4, 'fails'

    assert sol.connectTwoGroups([[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]) == 10, 'fails'

if __name__ == '__main__':
   main()