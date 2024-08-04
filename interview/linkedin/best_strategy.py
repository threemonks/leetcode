"""
//

grid = [[X, 1, 1, 2, 2],
        [1, 0, 0, 2, 2],
        [1, 0, 1, 0, 0]]

m = # of sets O(mlogm)

// Output
[(0,0)
(0,3)
(1,1)
(2,3)
(2,2)]
"""
import math


def best_strategy(grid):
    m, n = len(grid), len(grid[0])

    def dfs(i, j, grid):
        oldval = grid[i][j]
        grid[i][j] = -1
        node_count = 1
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for ni, nj in [(i + di, j + dj) for di, dj in dirs]:
            if 0 <= ni < m and 0 <= nj < n and grid[i][j] == oldval:
                node_count += dfs(ni, nj, grid)

        return node_count

    output = []
    for i in range(m):
        for j in range(n):
            if 0 <= grid[i][j] <= 4:
                count = dfs(i, j, grid)
                output.append([count, i, j])

    ans = [(i, j) for count, i, j sorted(output, reverse=True)]

    return ans

"""
[1, 1
 1, 1]
0, 0
grid[-1, -1
     - 1, -1]

(0, 0, 4)
(0, 1, 1)
"""