"""
778. Swim in Rising Water
Hard

On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].

"""

from typing import List
import heapq
"""
Dijkstra's algorithm where the distance between two vertices is the maximum of the two vertices' values.

time O(N^2*log(N))
space O(N^2)
"""

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        q = [(grid[0][0], (0, 0))]  # node, and elevation of this node
        heapq.heapify(q)
        visited = set()
        visited.add((0, 0))

        res = 0

        while q:
            # print('q=%s' % q)
            t, cur = heapq.heappop(q)
            res = max(res, t)
            if cur == (N - 1, N - 1):
                return res
            # print('cur=%s t=%s res=%s' % (cur, t, res))
            i, j = cur
            neighbors = []
            if i - 1 >= 0: neighbors.append((i - 1, j))
            if i + 1 < N: neighbors.append((i + 1, j))
            if j - 1 >= 0: neighbors.append((i, j - 1))
            if j + 1 < N: neighbors.append((i, j + 1))
            for nei in neighbors:
                ni, nj = nei
                if nei not in visited:
                    heapq.heappush(q, (grid[ni][nj], (ni, nj)))
                    visited.add(nei)

        return res


def main():
    sol = Solution()
    assert sol.swimInWater([[0,2],[1,3]]) == 3, 'fails'

    assert sol.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]) == 16, 'fails'


if __name__ == '__main__':
   main()