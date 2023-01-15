"""
2536. Increment Submatrices by One
Medium
148
47
You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.

You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:

Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for for all row1i <= x <= row2i and col1i <= y <= col2i.
Return the matrix mat after performing every query.



Example 1:


Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
Output: [[1,1,0],[1,2,1],[0,1,1]]
Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).
Example 2:


Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
Explanation: The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.


Constraints:

1 <= n <= 500
1 <= queries.length <= 10^4
0 <= row1i <= row2i < n
0 <= col1i <= col2i < n
"""
# Definition for a binary tree node.
from typing import List

"""
use 2d array to simulate the +1 process
TLE

Prefix Sum

1. for each row, update (+1) at column col1, decrease (-1) at column col2+1 (if within range)
2. for each row, do prefix sum mat[i] += mat[i-1]

similar to LC370 range addition

"""


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]

        # do update for each row (increase at col1, decrease at col2+1)
        for row1, col1, row2, col2 in queries:
            for i in range(row1, row2 + 1):
                mat[i][col1] += 1
                if col2 + 1 < n:
                    mat[i][col2 + 1] -= 1

        # now do prefix sum for each row
        for i in range(n):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]

        return mat


def main():
    sol = Solution()
    assert sol.rangeAddQueries(n = 3, queries = [[1,1,2,2],[0,0,1,1]]) == [[1,1,0],[1,2,1],[0,1,1]], 'fails'

    assert sol.rangeAddQueries(n = 2, queries = [[0,0,1,1]]) == [[1,1],[1,1]], 'fails'

if __name__ == '__main__':
   main()