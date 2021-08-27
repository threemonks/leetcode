"""
1293. Shortest Path in a Grid with Obstacles Elimination
Hard

1011

18

Add to List

Share
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.



Example 1:

Input:
grid =
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:

Input:
grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1
Output: -1
Explanation:
We need to eliminate at least two obstacles to find such a walk.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] == 0 or 1
grid[0][0] == grid[m - 1][n - 1] == 0

"""
from typing import List

"""
BFS

BFS to find shortest path on (i, j, r) where (i, j) is the grid cell, r is remaining obstacles we can eliminate

time O(V) V=m*n
"""
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        q = deque([[0, 0, k, 0]])  # node, eliminated obstacle
        visited = set([(0, 0, k)])

        while q:
            i, j, remains, steps = q.popleft()
            # print('i=%s j=%s remains=%s steps=%s q=%s' % (i, j, remains, steps, q))
            if i == m - 1 and j == n - 1:
                return steps

            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for ni, nj in [[i + di, j + dj] for di, dj in dirs]:
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                if grid[ni][nj] == 0 and (ni, nj, remains) not in visited:
                    q.append([ni, nj, remains, steps + 1])
                    visited.add((ni, nj, remains))
                if grid[ni][nj] == 1 and remains > 0 and (ni, nj, remains - 1) not in visited:
                    q.append([ni, nj, remains - 1, steps + 1])
                    visited.add((ni, nj, remains - 1))

        return -1


def main():
    sol = Solution()
    assert sol.shortestPath(grid = [[0,0,0], [1,1,0], [0,0,0], [0,1,1], [0,0,0]], k = 1) == 6, 'fails'

    assert sol.shortestPath(grid = [[0,1,1], [1,1,1], [1,0,0]], k = 1) == -1, 'fails'


if __name__ == '__main__':
   main()