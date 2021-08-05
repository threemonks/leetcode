"""
361. Bomb Enemy
Medium

636

82

Add to List

Share
Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E' or empty '0', return the maximum enemies you can kill using one bomb. You can only place the bomb in an empty cell.

The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.



Example 1:


Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3
Example 2:


Input: grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
Output: 1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 'W', 'E', or '0'.
"""
from typing import List

"""
Matrix

try all empty cell, iterate from the empty cell to both ends of row or col, one by one gather all enemies on its row or col without wall blocking

time O(m*n*(m+n))
space O(m*n)
"""
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        hits = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    for k in range(i+1, m):
                        if grid[k][j] == 'E':
                            hits[i][j] += 1
                        elif grid[k][j] == 'W':
                            break
                    for k in range(i-1, -1, -1):
                        if grid[k][j] == 'E':
                            hits[i][j] += 1
                        elif grid[k][j] == 'W':
                            break
                    for l in range(j+1, n):
                        if grid[i][l] == 'E':
                            hits[i][j] += 1
                        elif grid[i][l] == 'W':
                            break
                    for l in range(j-1, -1, -1):
                        if grid[i][l] == 'E':
                            hits[i][j] += 1
                        elif grid[i][l] == 'W':
                            break

        # print(hits)
        return max(map(max, hits))


def main():
    sol = Solution()
    assert sol.maxKilledEnemies(grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]) == 3, 'fails'

    assert sol.maxKilledEnemies(grid = [["W","W","W"],["0","0","0"],["E","E","E"]]) == 1, 'fails'


if __name__ == '__main__':
   main()