"""
1091. Shortest Path in Binary Matrix
Medium

1191

78

Add to List

Share
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.



Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1

"""
from typing import List
from collections import deque

"""
BFS
"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        dirs = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]

        dq = deque([(1, 0, 0)])  # cost, node
        visited = set((0, 0))
        while dq:
            step, x, y = dq.popleft()
            if x == n - 1 and y == n - 1:
                return step
            for nx, ny in [(x + dx, y + dy) for dx, dy in dirs if 0 <= x + dx < n and 0 <= y + dy < n]:
                if (nx, ny) not in visited and grid[nx][ny] == 0:
                    dq.append((step + 1, nx, ny))
                    visited.add((nx, ny))

        return -1


def main():
    sol = Solution()
    assert sol.shortestPathBinaryMatrix(grid = [[0,1],[1,0]]) == 2, 'fails'

    assert sol.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]]) == 4, 'fails'

    assert sol.shortestPathBinaryMatrix(grid = [[1,0,0],[1,1,0],[1,1,0]]) == -1, 'fails'

if __name__ == '__main__':
   main()