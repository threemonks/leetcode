"""
1102. Path With Maximum Minimum Value
Medium

1133

115

Add to List

Share
Given an m x n integer matrix grid, return the maximum score of a path starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4 cardinal directions.

The score of a path is the minimum value in that path.

For example, the score of the path 8 → 4 → 5 → 9 is 4.


Example 1:


Input: grid = [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: The path with the maximum score is highlighted in yellow.
Example 2:


Input: grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:


Input: grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
0 <= grid[i][j] <= 10^9

"""
from typing import List

"""
BFS shortest path - Dijkstra's Algorithm

typical Dijkstra's algo keeps track of shortest path (with weight), here we keep track minimum of path element value
And in Dijkstra's algo, the path can have weight, here the weight is 1

Note:
1. ending condition is reaching grid[m-1][n-1], not grid[m][n]
"""
import heapq


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = [(-grid[0][0], 0, 0)]  # start at (0, 0)
        heapq.heapify(q)

        # keep track of nodes we have already visited so we don't visit them again
        visited = [[0 for x in range(n)] for y in range(m)]
        visited[0][0] = 1

        while q:
            score, x, y = heapq.heappop(q)
            # print(f"{q = } {score = } {x = } {y = }")
            if x == m - 1 and y == n - 1:
                return -score
            # add all non-visited nodes into queue
            dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for nx, ny in [(x + dx, y + dy) for dx, dy in dirs]:
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:  # out of boundary
                    visited[nx][ny] = 1
                    heapq.heappush(q, (max(score, -grid[nx][ny]), nx, ny))

        return -1

def main():
    sol = Solution()
    assert sol.maximumMinimumPath(grid = [[5,4,5],[1,2,6],[7,4,6]]) == 4, 'fails'

    assert sol.maximumMinimumPath(grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]) == 2, 'fails'

    assert sol.maximumMinimumPath([[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]) == 3, 'fails'

if __name__ == '__main__':
   main()