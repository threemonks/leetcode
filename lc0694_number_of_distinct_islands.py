"""
694. Number of Distinct Islands
Medium

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""
from typing import List

"""
Hash by path signature
use BFS to find each inidividual island
two islands are the same if they have the same shape, since we use the same DFS method to traverse it, if we record the traversing path, then the two islands would be the same if only if the path representation are the same

time O(R*C) - we visit each cell exactly once
time O(R*C) - visited to store each cell visited status (if we choose to)
"""


class Solution:
    def dfs(self, grid, i, j, path, dir):
        m = len(grid)
        n = len(grid[0])
        path.append(dir)
        grid[i][j] = 2
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        di, dj = dirs[dir]
        ni, nj = i + di, j + dj
        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
            self.dfs(grid, ni, nj, path, 0)
            self.dfs(grid, ni, nj, path, 1)
            self.dfs(grid, ni, nj, path, 2)
            self.dfs(grid, ni, nj, path, 3)

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        island_paths = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    self.dfs(grid, i, j, path,
                             0)  # direction 0, 1, 2, 3 corresponding to [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    self.dfs(grid, i, j, path, 1)
                    self.dfs(grid, i, j, path, 2)
                    self.dfs(grid, i, j, path, 3)
                    if path:
                        island_paths.add(tuple(path))

        # print(grid)
        # print(island_paths)

        return len(island_paths)


def main():
    sol = Solution()
    assert sol.numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]) == 1, 'fails'

    assert sol.numDistinctIslands([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]) == 3, 'fails'


if __name__ == '__main__':
   main()