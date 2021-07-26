"""
329. Longest Increasing Path in a Matrix
Hard

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""
import collections

from functools import lru_cache
from typing import List

"""
only increasing neighbors are valid edges, use BFS to find longest path
mark node as visited with longest increasing path to it so far, can revisit if a longer increasing path found
"""


class Solution0:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])

        q = collections.deque()

        visited = dict()
        for i in range(m):
            for j in range(n):
                q.append((i, j, 1))
                visited[(i, j)] = 1

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        res = 0
        while q:
            # print('q=%s' % q)
            i, j, pathlen = q.popleft()
            # print('i=%s j=%s pathlen=%s' % (i, j, pathlen))
            res = max(res, pathlen)
            for ni, nj in ([(i + di, j + dj) for di, dj in dirs if 0 <= i + di < m and 0 <= j + dj < n]):
                if matrix[ni][nj] > matrix[i][j] and ((ni, nj) not in visited or pathlen + 1 > visited[(ni, nj)]):
                    q.append((ni, nj, pathlen + 1))
                    visited[(ni, nj)] = pathlen + 1

        return res


"""
DFS with memoization

Note can be either longest increasing path or longest decreasing path
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(i, j):

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            neighbors = [dfs(ni, nj) for ni, nj in
                         [(i + di, j + dj) for di, dj in dirs if 0 <= i + di < m and 0 <= j + dj < n]
                         if matrix[ni][nj] < matrix[i][j]]
            return 1 + (max(neighbors) if neighbors else 0)

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res


def main():
    sol = Solution()
    assert sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]) == 4, 'fails'

    assert sol.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]) == 4, 'fails'

    assert sol.longestIncreasingPath([[1]]) == 1, 'fails'

if __name__ == '__main__':
   main()
