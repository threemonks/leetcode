"""
463. Island Perimeter
Easy

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4


Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
"""
from typing import List

"""
using BFS, for each new found 1 node, see which side of its neighbors are not in the island already, then add 1 to perimeter for that edge
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = []
        perimeter = 0
        for i in range(m):
            for j in range(n):
                # print('i=%s j=%s' % (i, j))
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 2
                    while q:
                        x, y = q.pop()
                        # print('x=%s y=%s' % (x, y))
                        for nx, ny in [(x + dx, y + dy) for dx, dy in dirs]:
                            # print('nx=%s ny=%s' % (nx, ny))
                            if nx == -1 or nx == m or ny == -1 or ny == n or (
                                    0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0):
                                perimeter += 1
                                # print('nx=%s ny=%s perimeter=%s' % (nx, ny, perimeter))
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                                q.append((nx, ny))
                                grid[nx][ny] = 2

        return perimeter

def main():
    sol = Solution()
    assert sol.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16, 'fails'

    assert sol.islandPerimeter(grid = [[1]]) == 4, 'fails'

    assert sol.islandPerimeter(grid = [[1,0]]) == 4, 'fails'

if __name__ == '__main__':
   main()