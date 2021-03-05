"""
827. Making A Large Island
Hard

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.

"""
from typing import List

"""
Union-Find
use union find to find all islands, and turn all visited node to 2, then loop all node of 0, see which one can be turned to connect its neighboring islands on four sizes (could be less than four islands, since some island might join with this cell on more than one side)

time O(N^2) - loop to discover island and get sizes
space O(N^2)

"""


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # path compression
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
            else:  # same rank, merge and increase rank by 1
                self.parent[yp] = xp
                self.rank[xp] += 1
                self.size[xp] += self.size[yp]


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dsu = DSU(m * n)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for ni, nj in [(i + di, j + dj) for di, dj in dirs if 0 <= i + di < m and 0 <= j + dj < n]:
                        if grid[ni][nj] == 1:
                            if dsu.find(i * n + j) != dsu.find(ni * n + nj):
                                dsu.union(i * n + j, ni * n + nj)

        max_area = max(dsu.size)
        # loop through all nodes that is water, see if it can flip and connect its neighboring islands
        for i in range(m):
            for j in range(n):
                if grid[i][
                    j] == 0:  # find a water, if we flip it, it will connect its neighbor island on four directions (could be less than 4 islands, as some side could share island)
                    neighbor_island_areas = dict()
                    for ni, nj in [(i + di, j + dj) for di, dj in dirs if 0 <= i + di < m and 0 <= j + dj < n]:
                        if grid[ni][nj] == 1:
                            parent = dsu.find(ni * n + nj)
                            neighbor_island_areas[parent] = dsu.size[parent]
                    max_area = max(max_area, sum(neighbor_island_areas.values()) + 1)

        return max_area


def main():
    sol = Solution()
    assert sol.largestIsland(grid = [[1,0],[0,1]]) == 3, 'fails'

    assert sol.largestIsland(grid = [[1,1],[1,0]]) == 4, 'fails'

    assert sol.largestIsland(grid = [[1,1],[1,1]]) == 4, 'fails'

if __name__ == '__main__':
   main()