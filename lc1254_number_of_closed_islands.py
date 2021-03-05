"""
1254. Number of Closed Islands
Medium

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2


Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1

"""
from typing import List

"""
Union-Find
use DFS to find all islands, and identify if each of the island touches boundary, if so, it is not closed, we only count closed islands

time O(R*C)
space O(R*C)
"""

class Solution:
    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        grid[i][j] = 2
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            closed = False
        else:
            closed = True
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for ni, nj in [(i + di, j + dj) for di, dj in dirs if 0 <= i + di < m and 0 <= j + dj < n]:
            if grid[ni][nj] == 0:
                if not self.dfs(grid, ni, nj):
                    closed = False
        return closed

    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        closed = 0

        for i in range(m):
            for j in range(n):
                # print('i=%s j=%s ' % (i, j))
                if grid[i][j] == 0:
                    if self.dfs(grid, i, j):
                        closed += 1

        return closed


def main():
    sol = Solution()
    assert sol.closedIsland(grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]) == 2, 'fails'

    assert sol.closedIsland(grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]) == 1, 'fails'

    assert sol.closedIsland(grid = [[1,1,1,1,1,1,1], [1,0,0,0,0,0,1], [1,0,1,1,1,0,1], [1,0,1,0,1,0,1], [1,0,1,1,1,0,1], [1,0,0,0,0,0,1], [1,1,1,1,1,1,1]]) == 2, 'fails'

if __name__ == '__main__':
   main()