"""
695. Max Area of Island
Medium

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""

from typing import List

"""
use disjoinset union find (union by size to keep track of size and max size)

"""
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp != yp:
            if self.size[xp] > self.size[yp]:
                self.parent[yp] = xp
                self.size[xp] += self.size[yp]
            else:
                self.parent[xp] = yp
                self.size[yp] += self.size[xp]

class Solution0:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dsu = DSU(m*n)
        max_area = 0

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for nx, ny in [(i+di, j+dj) for (di, dj) in dirs if 0<=i+di<m and 0<=j+dj<n]:
                    if grid[nx][ny] == 1:
                        p = dsu.find(i*n+j)
                        np = dsu.find(nx*n+ny)
                        if p != np: # merge into one island
                            dsu.union(i*n+j, nx*n+ny)
                max_area = max(max_area, dsu.size[dsu.find(i*n+j)])

        return max_area


"""
use disjoinset union find (union by rank to keep track of size and max size)

"""
class DSUByRank:
    """
    union by rank, but keep track of size as well
    this does not have any noticable performance improvement
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp != yp:
            if self.rank[xp] > self.rank[yp]:
                self.parent[yp] = xp
                self.size[xp] += self.size[yp]
            elif self.rank[xp] < self.rank[yp]:
                self.parent[xp] = yp
                self.size[yp] += self.size[xp]
            else:  # same rank, need to update
                self.parent[yp] = xp
                self.rank[xp] += 1
                self.size[xp] += self.size[yp]


class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dsu = DSUByRank(m * n)
        max_area = 0

        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # only look to right and down for neighbors, not left and up

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for nx, ny in [(i + di, j + dj) for (di, dj) in dirs if 0 <= i + di < m and 0 <= j + dj < n]:
                    if grid[nx][ny] == 1:
                        p = dsu.find(i * n + j)
                        np = dsu.find(nx * n + ny)
                        if p != np:  # merge into one island
                            dsu.union(i * n + j, nx * n + ny)
                max_area = max(max_area, dsu.size[dsu.find(i * n + j)])

        return max_area


"""
DFS counting square

thinking: if a square ending at (r, c), we check if it connects with any of its neighbors ending at [(-1, 0), (1, 0), (0, -1), (0, 1)] and counts them all recursively
"""


class Solution2:
    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        area = 0
        grid[i][j] = 0
        area += 1
        for ni, nj in [(i + di, j + dj) for (di, dj) in dirs if 0 <= i + di < m and 0 <= j + dj < n]:
            if grid[ni][nj] == 1:
                area += self.dfs(grid, ni, nj)

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j))

        return max_area


"""
BFS counting square

thinking: if a square ending at (r, c), we check if it connects with any of its neighbors ending at [(-1, 0), (1, 0), (0, -1), (0, 1)] and counts them all recursively
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0
                    q = []
                    q.append((i, j))
                    grid[i][j] = 0
                    while q:
                        x, y = q.pop()
                        area += 1
                        for nx, ny in [(x + dx, y + dy) for (dx, dy) in dirs if 0 <= x + dx < m and 0 <= y + dy < n]:
                            if grid[nx][ny] == 1:
                                q.append((nx, ny))
                                grid[nx][ny] = 0

                    max_area = max(max_area, area)

        return max_area


def main():
    sol = Solution()
    assert sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,1,1,0,1,0,0,0,0,0,0,0,0], [0,1,0,0,1,1,0,0,1,0,1,0,0], [0,1,0,0,1,1,0,0,1,1,1,0,0], [0,0,0,0,0,0,0,0,0,0,1,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,0,0,0,0,0,0,1,1,0,0,0,0]]) == 6, 'fails'

    assert sol.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]) == 0, 'fails'

    assert sol.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]) == 4, 'fails'

    assert sol.maxAreaOfIsland([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]) == 3, 'fails'

if __name__ == '__main__':
   main()