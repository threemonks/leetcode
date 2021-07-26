"""
317. Shortest Distance from All Buildings
Hard

1085

69

Add to List

Share
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.



Example 1:


Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
Example 2:

Input: grid = [[1,0]]
Output: 1
Example 3:

Input: grid = [[1]]
Output: -1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is either 0, 1, or 2.
There will be at least one building in the grid.

"""
import math
from typing import List

"""
BFS

try any empty land as house, calculate its total distance to all buildings (by avoiding obstacle)

since we don't know where the house (empty land) would be, but we do know where the buildings are, we can iterate each building, and calculate its shortest distance to all empty lands (potential house location), then we have all distances from each building to each empty lands (houses) that is accessible, which is also the distance from each empty land to each building. We then summarize the distance from each empy land to all buildings (ignoring empty lands that cannot reach all buldings), and take the one with smallest total distance to all buildings.

notes:
1. when BFS traverse, cannot pass obstacle, nor can pass building
2. if a empty land cannot reach all building (even if it can not reach just one), then this empty land cannot be for answer
"""
from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        distances = dict()  # empty land loc to building loc pair

        buildings = []
        lands = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings.append([i, j])
                elif grid[i][j] == 0:
                    lands.append([i, j])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q = deque([(i, j, 0)])
                    seen = set()

                    while q:
                        cur = q.popleft()
                        x, y, steps = cur
                        if grid[x][y] == 0:
                            if (x, y, i, j) in distances:
                                distances[(x, y, i, j)] = min(distances[(x, y, i, j)], steps)
                            else:
                                distances[(x, y, i, j)] = steps
                        # exploer all neighbors that are not wall
                        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                        for nx, ny in [(x + dx, y + dy) for dx, dy in dirs]:
                            if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] == 2 or grid[nx][
                                ny] == 1:  # out bound or wall or building
                                continue
                            if (nx, ny) not in seen:
                                q.append((nx, ny, steps + 1))
                                seen.add((nx, ny))

        # print('lands=%s' % lands)
        # print('buildings=%s' % buildings)
        # print('distances=%s' % distances)
        # now summarize across all empty lands
        ans = math.inf
        for land in lands:
            total_dist = 0
            for bld in buildings:
                if (land[0], land[1], bld[0],
                    bld[1]) not in distances:  # one building not reachable, this land cannot be answer
                    total_dist = math.inf
                else:
                    total_dist += distances[(land[0], land[1], bld[0], bld[1])]
            ans = min(ans, total_dist)

        return ans if ans < math.inf / 2 else -1


def main():
    sol = Solution()
    assert sol.shortestDistance(grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]) == 7, 'fails'

    assert sol.shortestDistance(grid = [[1,0]]) == 1, 'fails'

    assert sol.shortestDistance(grid = [[1]]) == -1, 'fails'


if __name__ == '__main__':
   main()
