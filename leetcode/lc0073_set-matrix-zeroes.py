"""
73. Set Matrix Zeroes
Medium

4013

393

Add to List

Share
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1


Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
from typing import List

"""
Array

1. process first row and first col, check if they need to be set to zero
2. process 2nd ... m rows and 2nd ... n cols, if a cell is 0, set its first value of the row, and of the col to be 0, to indicate that this row and col needs to be set to 0.

Array: for O(1) space, we use first val of a given row / col to indicate this row or col needs to be set to zero, but what if this val was already 0? It should indicate that first row or first col needs to be set to zero, we use another variable first_row to indicate first row needs to be set to zero, and use first_col to indicate first column needs to be set to zero


note:
1. cannot use flip number to negative, because some numbers are already negative
2. before we set the first value of row/col to zero, we need to check if it is already 0, and set first_row/first_col flag
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        first_row, first_col = False, False  # do we need to set first row and first col to zero?

        # do we need to set first row to zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True

        # do we need to set first col to zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True

        # if cell is 0, set first value of its row and col to 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # set entire row to 0 if first col is 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for k in range(m):
                    matrix[k][j] = 0

        # set entire col to 0 if first row is 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for k in range(n):
                    matrix[i][k] = 0

        # now handle first row
        if first_row:
            for j in range(n):
                matrix[0][j] = 0

        # now handle first col
        if first_col:
            for i in range(m):
                matrix[i][0] = 0