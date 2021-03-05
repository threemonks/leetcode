"""
1568. Minimum Number of Days to Disconnect Island
Hard

Given a 2D grid consisting of 1s (land) and 0s (water).  An island is a maximal 4-directionally (horizontal or vertical) connected group of 1s.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

Example 1:

Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:

Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
Example 3:

Input: grid = [[1,0,1,0]]
Output: 0
Example 4:

Input: grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,0,1,1]]
Output: 1
Example 5:

Input: grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,1,1,1]]
Output: 2


Constraints:

1 <= grid.length, grid[i].length <= 30
grid[i][j] is 0 or 1.
"""
import collections
from itertools import product
from typing import List
from itertools import product

"""
Graph DFS SCC Tarjan's

note that we should only need to flip either 0, or 1, or 2 (at most 2) cells, because we can always find a corner piece and flip its two neighbors to make it a new island
so the answer should be 0, 1, or 2
with the above knowledge, we do this
1. count number of islands, if there's 0 or 2 or more islands, we don't need to do anything, return 0
2. if there's exactly 1 island, we need to consider
2.1 if there's exactly 1 cell with value 1, we flip it to get 0 island => 1
2.2 if there's exactly 2 cell with value 1, they must be next to each other (per above we have just one island), we need to flip them both to get to 0 island => 2
2.3 otherwise, we need to use tarjan's algorithm to find if there's a bridge, if there is a bridge, we need to cut that bridge (flip 1 cell) => 1
2.4 if there's no bridge, we need to flip 2 cell to cut into two islands
"""


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        islands, count, critical_edge_found = 0, 0, False
        root = -1
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            nonlocal grid, visited, dirs, count
            visited.add((i, j))
            count += 1
            for ni, nj in [(i + di, j + dj) for di, dj in dirs if 0 <= i + di < m and 0 <= j + dj < n]:
                if grid[ni][nj] == 1 and (ni, nj) not in visited:
                    dfs(ni, nj)

        def number_of_islands():
            nonlocal grid, visited, islands, root
            for i, j in product(range(m), range(n)):
                if grid[i][j] == 1 and (i, j) not in visited:
                    if root == -1: root = i * n + j
                    islands += 1
                    dfs(i, j)

        number_of_islands()

        if islands != 1:
            return 0
        if count == 1:
            return 1
        elif count == 2:
            return 2

        # now we know there's one island, we need to find out if there's at least one critical edge
        # construct graph
        adj_list = collections.defaultdict(list)
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                for ni, nj in [(i + di, j + dj) for di, dj in dirs if 0 <= i + di < m and 0 <= j + dj < n]:
                    if grid[ni][nj] == 1:
                        if ni * n + nj not in adj_list[(i * n + j)]:
                            adj_list[(i * n + j)].append(ni * n + nj)
                        if i * n + j not in adj_list[(ni * n + nj)]:
                            adj_list[(ni * n + nj)].append(i * n + j)

        seen = set()  # visited set for tarjan's algorithm to find critical edge
        lowest = dict()  # keep lowest time for each vertex
        critical_edges = []

        def tarjan(parent, cur, curtime, seen):
            nonlocal critical_edge_found, lowest, critical_edges
            seen.add(cur)
            lowest[cur] = curtime
            for nei in adj_list[cur]:
                if nei == parent: continue
                if nei not in seen: tarjan(cur, nei, curtime + 1, seen)
                if curtime < lowest[nei]:
                    critical_edge_found = True
                    critical_edges.append((cur, nei))
                lowest[cur] = min(lowest[cur], lowest[nei])

        tarjan(-1, root, 0, seen)

        if critical_edge_found:
            return 1
        else:
            return 2


def main():
    sol = Solution()
    assert sol.minDays([[0,1,1,0],[0,1,1,0],[0,0,0,0]]) == 2, 'fails'

    assert sol.minDays([[1,1]]) == 2, 'fails'

    assert sol.minDays([[1,0,1,0]]) == 0, 'fails'

    assert sol.minDays([[1,1,0,1,1], [1,1,1,1,1], [1,1,0,1,1], [1,1,0,1,1]]) == 1, 'fails'

    assert sol.minDays([[1,1,0,1,1], [1,1,1,1,1], [1,1,0,1,1], [1,1,1,1,1]]) == 2, 'fails'

    assert sol.minDays([[0,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,0]]) == 1, 'fails'

if __name__ == '__main__':
   main()