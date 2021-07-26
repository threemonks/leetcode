"""
305. Number of Islands II
Hard

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?

"""
from typing import List

"""
disjoinset / union find
"""


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp != yp:
            self.parent[yp] = xp


"""
disjoinset / union find
"""


class DSUByRank:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1 for _ in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp != yp:
            if self.rank[xp] > self.rank[yp]:
                self.parent[yp] = xp
            elif self.rank[xp] < self.rank[yp]:
                self.parent[xp] = yp
            else:  # same rank, increase by 1
                self.parent[yp] = xp
                self.rank[xp] += 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        res = []
        count = 0

        dsu = DSUByRank(m * n)

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        grid = [[0 for _ in range(n)] for _ in range(m)]

        for x, y in positions:
            if grid[x][y] == 0:
                count += 1
                grid[x][y] = 1
            # merge it with any potential neighbor island, if successfully merged, count -=1
            for nx, ny in [(x + dx, y + dy) for dx, dy in dirs if 0 <= x + dx < m and 0 <= y + dy < n]:
                if grid[nx][ny] == 1:
                    p1, p2 = x * n + y, nx * n + ny
                    if dsu.find(p1) != dsu.find(p2):
                        dsu.union(p1, p2)
                        count -= 1
            res.append(count)

        return res


def main():
    sol = Solution()
    assert sol.numIslands2(m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]) == [1,1,2,3], 'fails'

    assert sol.numIslands2(3, 3, [[0,0],[0,1],[1,2],[1,2]]) == [1,1,2,2], 'fails'

    assert sol.numIslands2(8, 4, [[0,0],[7,1],[6,1],[3,3],[4,1]]) == [1, 2, 2, 3, 4], 'fails'

if __name__ == '__main__':
   main()