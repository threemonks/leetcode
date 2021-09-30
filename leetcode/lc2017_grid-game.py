"""
2017. Grid Game
Medium

16

1

Add to List

Share
You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.

Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).

At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.

The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.



Example 1:


Input: grid = [[2,5,4],[1,5,1]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 0 + 4 + 0 = 4 points.
Example 2:


Input: grid = [[3,3,1],[8,5,2]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 3 + 1 + 0 = 4 points.
Example 3:


Input: grid = [[1,3,1,15],[1,3,3,1]]
Output: 7
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.


Constraints:

grid.length == 2
n == grid[r].length
1 <= n <= 5 * 10^4
1 <= grid[r][c] <= 10^5
"""
import math
from typing import List

"""
Prefix Sum

since robot can only go right or down, never up, so each robot can go down only once, this restriction make the problem not suitable for DP, as robot 1 is trying to minimize robot's score, which is different from maximizing robot 1's score.

Given robot 1 can only go down once, so it will set all left end of top row to zero, until the point it goes down, then set right part of bottom row after this point to zero.

For robot 2 to maximize its point after robot 1 finishes, it has to either goes top row all the way to right, then go down,
or first go down, and go right on bottom row completely.

We can then iterate all possible turning points for robot 1, and calculate robot 2's score for each of such case.

Note:
1. if robot 1 turns at i-th cell, grid[0][i]=0 and grid[1][i] = 0, and robot 2 only get 0 from i-th column

"""


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        topsum = sum(grid[0])
        bottomsum = 0

        ans = math.inf
        for i in range(n):
            topsum -= grid[0][i]  # topsum is sum of toprow after robot 1 turns at i, which sets grid[0...i] to 0
            ans = min(ans, max(topsum, bottomsum))
            bottomsum += grid[1][i]  # bottom sum is sum of grid[1][0:i] (including grid[1][i])

        return ans


def main():
    sol = Solution()
    assert sol.gridGame(grid = [[2,5,4],[1,5,1]]) == 4, 'fails'

    assert sol.gridGame(grid = [[3,3,1],[8,5,2]]) == 4, 'fails'

    assert sol.gridGame(grid = [[1,3,1,15],[1,3,3,1]]) == 7, 'fails'

if __name__ == '__main__':
   main()