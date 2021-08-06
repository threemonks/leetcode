"""
240. Search a 2D Matrix II
Medium

5325

98

Add to List

Share
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9
"""
from typing import List

"""
Brutal force search each col within each row

time O(mn)
space O(1)
"""


class Solution0:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True

        return False


"""
Search Space Reduction

steps:
1. start compare target with matrix[0][n-1],
   if smaller, then we excluded column n-1, then compare with matrix[0][n-2]
   if larger, we excluded row 0, then compare with matrix[1][n-1]
2. repeat above

time O(m+n)
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:  # check empty
            return False

        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                # prune row i, go to next row i+1
                i += 1
            elif matrix[i][j] > target:
                # prune column j, go to prev col j-1
                j -= 1

        return False

def main():
    sol = Solution()
    assert sol.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5) == True, 'fails'

    assert sol.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20) == False, 'fails'


if __name__ == '__main__':
   main()