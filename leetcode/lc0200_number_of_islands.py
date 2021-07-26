"""
200. Number of Islands
Medium

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""
from typing import List

"""
union find

for each "1", add it as a new island, and try to merge any of its neighbor that is also "1"
for each "1" found, we increase count by 1, and for each valid union, we decrease count by 1
the result is total number of islands

time O(m*n)

mistakes:
1. in DSU class method find: if self.parent[x] != x: self.parent[x] = self.find(self.parent[x]), it is not while, since find is calling itself recursively
2. in DSU class method union, self.parent[xp] = yp
3. 2D to 1D [i][j] => i*n+j, where n is # of columns
"""


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)
        if xp != yp:
            self.parent[xp] = yp


class Solution0:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        count = 0

        dsu = DSU(m * n)

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                count += 1
                for ni, nj in [(i + di, j + dj) for di, dj in dirs if 0 <= i + di < m and 0 <= j + dj < n]:
                    if grid[ni][nj] == "1":
                        p1, p2 = i * n + j, ni * n + nj  # convert 2-d index to 1-d index for DSU
                        island1 = dsu.find(p1)
                        island2 = dsu.find(p2)
                        if island1 != island2:
                            dsu.union(p1, p2)
                            count -= 1

        return count


"""
BFS
loop through all nodes
    for a node with value "1"
    increase island_count by 1
    add to queue

    while q
        pop from queue
        mark it as visited (or set to 0 if allowed, as it is faster)
        find its valid neighbors that is also 1, add into queue

return island count
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        num_island = 0
        q = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] == '0'
                    num_island += 1
                    q.append((i, j))
                    while q:
                        x, y = q.pop()
                        grid[x][y] = '0'
                        for nx, ny in [(x + dx, y + dy) for dx, dy in dirs if 0 <= x + dx < m and 0 <= y + dy < n]:
                            if grid[nx][ny] == '1':
                                q.append((nx, ny))

        return num_island


"""
DFS/recursive

Note: instead of mark as visited, we set value of grid[i][j] from "1" to "0" after visited
"""


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            grid[x][y] = '0'
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for nx, ny in [(x + dx, y + dy) for dx, dy in dirs if 0 <= x + dx < m and 0 <= y + dy < n]:
                if grid[nx][ny] == '1':
                    dfs(nx, ny)

        num_island = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_island += 1
                    dfs(i, j)

        return num_island


"""
DFS

use DFS to count number of islands return 1 for entire island (dfs recursively mark entire islands as 0)
"""


class Solution:
    def numIslands(self, A: List[List[str]]) -> int:
        m, n = len(A), len(A[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j):
            A[i][j] = "0"
            for ni, nj in [[i + di, j + dj] for di, dj in dirs if 0 <= i + di < m and 0 <= j + dj < n]:
                if A[ni][nj] == "1":
                    dfs(ni, nj)

            return 1

        count = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == "1":
                    count += dfs(i, j)

        return count

def main():
    sol = Solution()
    assert sol.numIslands(grid = [ ["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"] ]) == 1, 'fails'

    assert sol.numIslands(grid = [ ["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"] ]) == 3, 'fails'


if __name__ == '__main__':
   main()