"""
994. Rotting Oranges
Medium

3539

217

Add to List

Share
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

"""
from typing import List

"""
BFS

start queue all rotten ones with step 0, add it to seen, if any of its neighbor is fresh, turn it to rotten, add to queue with step+1, mark it as seen

time O(V+E)
"""
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = deque()

        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append(([i, j], 0))  # cell, steps
                    seen.add((i, j))

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        ans = 0
        while q:
            cur, steps = q.popleft()
            ans = max(ans, steps)
            x, y = cur
            for nx, ny in [(x + dx, y + dy) for dx, dy in dirs if 0 <= x + dx < m and 0 <= y + dy < n]:
                if grid[nx][ny] == 1 and (nx, ny) not in seen:
                    grid[nx][ny] = 2
                    q.append(([nx, ny], steps + 1))
                    seen.add((nx, ny))

        # check if any fresh left
        # print('steps=%s' % steps)
        # print(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # print('i=%s j=%s still fresh' % (i, j))
                    return -1

        # if all rotten:
        return ans

def main():
    sol = Solution()
    assert sol.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]) == 4, 'fails'

    assert sol.orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]) == -1, 'fails'

    assert sol.orangesRotting(grid = [[0,2]]) == 0, 'fails'


if __name__ == '__main__':
   main()