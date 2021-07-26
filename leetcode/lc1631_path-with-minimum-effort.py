"""
1631. Path With Minimum Effort
Medium

1375

68

Add to List

Share
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.



Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.


Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 10^6
"""
import math
from typing import List

"""
Single Source Shortest Path - Dijkstra's algo : BFS + PriorityQueue

Shortest path with positive weight => dijkstra


time O(E*log(V)) - where E is number of edge, V is number of vertices
     O(M*N(log(M*N))) - m row, n col, number of edge and path are both m*n
mistakes:
1. route's effort is maximum absolute difference in heights between two consecutive cells of the route
"""
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        hq = [(0, 0, 0)]  # effort, x, y

        mincost = [[math.inf for _ in range(n)] for _ in range(m)]
        mincost[0][0] = 0

        while hq:
            cost, x, y = heapq.heappop(hq)
            if cost > mincost[x][y]:  # already have mincost, skip
                continue
            if x == m - 1 and y == n - 1:  # destination reached
                return cost
            for nx, ny in [(x + dx, y + dy) for dx, dy in dirs if 0 <= x + dx < m and 0 <= y + dy < n]:
                ncost = max(cost, abs(heights[nx][ny] - heights[x][y]))
                if ncost < mincost[nx][ny]:  # if better mincost found, then enqueue it and process
                    mincost[nx][ny] = ncost
                    heapq.heappush(hq, (ncost, nx, ny))

def main():
    sol = Solution()
    assert sol.minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]]) == 2, 'fails'

    assert sol.minimumEffortPath(heights = [[1,2,3],[3,8,4],[5,3,5]]) == 1, 'fails'

    assert sol.minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]) == 0, 'fails'


if __name__ == '__main__':
   main()