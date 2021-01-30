"""
417. Pacific Atlantic Water Flow
Medium

1697

389

Add to List

Share
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.


Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

"""
import collections
from functools import lru_cache
from typing import List

"""
using DFS go from sea to inner land, with rising water, any node with higher level would then be part of this sea
eventually, we got two matrix with marked nodes representing sea Pacific, and Atlantic. We then take intersection of these two to get the nodes whose water can flow to both oceans
we need to use set to mark visited nodes in each DFS search, otherwise it will TLE

1. Two Queue and add all the Pacific border to one queue; Atlantic border to another queue.
2. Keep a visited matrix for each queue. In the end, add the cell visited by two queue to the result.

obseration / thinking:
BFS: Water flood from ocean to the cell. Since water can only flow from high/equal cell to low cell, add the neighbor cell with height larger or equal to current cell to the queue and mark as visited.

use sea water flooding into inner land, or sea water go into inner as water rsies, has the following advantage vs BFS going from any node to sea
1. there's only m+n nodes as starting point of the sea shore, vs m*n if we use BFS start from any node
2. for sea water rising flooding inner land, we add neighbor node that is higher, and skip neighbor node when is lower (this will not miss any node that is lower then this but higher than other nodes that is now part of the sea)
3. termination condition - for either BFS when queue is empty, for DFS, when no more unvisited neighbor

similar problem 
  778 - https://leetcode.com/problems/swim-in-rising-water/
  407 - https://leetcode.com/problems/trapping-rain-water-ii/
  

time O(mn)
space O(mn)
"""


class Solution0:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []

        m, n = len(matrix), len(matrix[0])

        # print('m=%s n=%s' % (m, n))

        def dfs(i, j, sea):
            nonlocal matrix
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            sea.add((i, j))
            for x, y in [(i + dx, j + dy) for dx, dy in dirs if 0 <= i + dx < m and 0 <= j + dy < n]:
                if (x, y) in sea: continue
                if matrix[x][y] >= matrix[i][j]:
                    dfs(x, y, sea)

        pac = set()
        atl = set()
        for i in range(m):
            dfs(i, 0, pac)
            dfs(i, n - 1, atl)
        for j in range(n):
            dfs(0, j, pac)
            dfs(m - 1, j, atl)

        result = []
        for i in range(m):
            for j in range(n):
                if ((i, j) in pac and (i, j) in atl):
                    result.append([i, j])

        return result


"""
BFS - similar thinking, sea water level goes up, water flood into / fill up inner land, extends sea body, until no more neighbor that is higher  

time O(mn)
space O(mn)
"""


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []

        m, n = len(matrix), len(matrix[0])
        # print('m=%s n=%s' % (m, n))

        pac = set()
        pq = collections.deque()
        atl = set()
        aq = collections.deque()
        for i in range(m):
            pq.append((i, 0))
            pac.add((i, 0))
            aq.append((i, n - 1))
            atl.add((i, n - 1))

        for j in range(n):
            pq.append((0, j))
            pac.add((0, j))
            aq.append((m - 1, j))
            atl.add((m - 1, j))

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while pq:
            i, j = pq.popleft()
            for x, y in [(i + dx, j + dy) for dx, dy in dirs if 0 <= i + dx < m and 0 <= j + dy < n]:
                if (x, y) in pac: continue
                if matrix[x][y] >= matrix[i][j]:
                    pq.append((x, y))
                    pac.add((x, y))

        while aq:
            i, j = aq.popleft()
            for x, y in [(i + dx, j + dy) for dx, dy in dirs if 0 <= i + dx < m and 0 <= j + dy < n]:
                if (x, y) in atl: continue
                if matrix[x][y] >= matrix[i][j]:
                    aq.append((x, y))
                    atl.add((x, y))

        result = []
        for i in range(m):
            for j in range(n):
                if ((i, j) in pac and (i, j) in atl):
                    result.append([i, j])

        return result


def main():
    sol = Solution()
    assert sorted(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) == sorted([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]), 'fails'

if __name__ == '__main__':
   main()