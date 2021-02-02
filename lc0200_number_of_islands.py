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
"""
union find

for each "1", add it as a new island, and try to merge any of its neighbor that is also "1"
for each "1" found, we increase count by 1, and for each valid union, we decrease count by 1
the result is total number of islands

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


class Solution:
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


def main():
    sol = Solution()
    assert sol.numIslands(grid = [ ["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"] ]) == 1, 'fails'

    assert sol.numIslands(grid = [ ["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"] ]) == 3, 'fails'


if __name__ == '__main__':
   main()