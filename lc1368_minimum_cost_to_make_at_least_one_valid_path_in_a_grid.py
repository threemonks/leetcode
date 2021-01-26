"""
1368. Minimum Cost to Make at Least One Valid Path in a Grid
Hard

Given a m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some invalid signs on the cells of the grid which points outside the grid.

You will initially start at the upper left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path doesn't have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.



Example 1:


Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.
Example 2:


Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).
Example 3:


Input: grid = [[1,2],[4,3]]
Output: 1
Example 4:

Input: grid = [[2,2,2],[2,2,2]]
Output: 3
Example 5:

Input: grid = [[4]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100

"""
import collections
import heapq
from typing import List

import heapq
"""
BFS

build a graph from any point to any other neighboring points, with correct direction as weight 0, incorrect direct as weight 1

now BFS search shortest path (weighted) from start point to end point

note visited records smallest cost we visit a node, and we may revisit a node if now comes with a smaller cost.

time O(mn)
space O(mn)
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        adj_list = collections.defaultdict(list)
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        for i in range(m):
            for j in range(n):
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        if ((grid[i][j] == 1 and di == 0 and dj == 1) \
                                or (grid[i][j] == 2 and di == 0 and dj == -1) \
                                or (grid[i][j] == 3 and di == 1 and dj == 0) \
                                or (grid[i][j] == 4 and di == -1 and dj == 0)):
                            adj_list[(i, j)].append((ni, nj, 0))
                        else:
                            adj_list[(i, j)].append((ni, nj, 1))

        q = [(0, 0, 0)]
        heapq.heapify(q)

        visited = dict()
        visited[(0, 0)] = 0

        while q:
            costs, i, j = heapq.heappop(q)
            if i == m - 1 and j == n - 1:
                return costs

            for ni, nj, ncost in adj_list[(i, j)]:
                if (ni, nj) not in visited or costs + ncost < visited[(ni, nj)]:
                    heapq.heappush(q, (costs + ncost, ni, nj))
                    visited[(ni, nj)] = costs + ncost

        return -1

def main():
    sol = Solution()
    assert sol.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]) == 3, 'fails'

    assert sol.minCost([[1,1,3],[3,2,2],[1,1,4]]) == 0, 'fails'

    assert sol.minCost([[1,2],[4,3]]) == 1, 'fails'

    assert sol.minCost([[2,2,2],[2,2,2]]) == 3, 'fails'

    assert sol.minCost([[4]]) == 0, 'fails'

if __name__ == '__main__':
   main()