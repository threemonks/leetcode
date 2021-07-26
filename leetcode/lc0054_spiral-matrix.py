"""
54. Spiral Matrix
Medium

4237

686

Add to List

Share
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List

"""
Array

Process one layer at a time (four sides, top, right, bottom, left), and recursively process inner layer until last layer is just one column or one row

"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        if m == 1:
            return matrix[0][:]
        if n == 1:
            return [matrix[i][0] for i in range(m)]

        ans = []
        # top
        ans += matrix[0][:]

        # right
        ans += [matrix[i][n - 1] for i in range(1, m - 1)]

        # bottom
        ans += reversed(matrix[m - 1][:])

        # left
        ans += [matrix[i][0] for i in range(m - 2, 0, -1)]

        if m - 1 > 1 and n - 1 > 1:
            ans += self.spiralOrder([matrix[i][1:n - 1] for i in range(1, m - 1)])

        return ans


def main():
    sol = Solution()
    assert sol.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5], 'fails'

    assert sol.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7], 'fails'

if __name__ == '__main__':
   main()