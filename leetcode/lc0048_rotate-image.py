"""
48. Rotate Image
Medium

5547

362

Add to List

Share
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
Example 3:

Input: matrix = [[1]]
Output: [[1]]
Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]


Constraints:

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
from typing import List

"""
Array

1. rotate ring by ring
2. with in each ring, process for k=0...n//2
2.1. for each k value, 
     store k-th value of top row
     i) copy k-th value from left side of ring to top row of ring
     ii) copy k-th value from bottom to left
     iii) copy k-th value from right to bottom
     iv) copy k-th value from top to right

"""


class Solution0:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2 + n % 2):
            for k in range(n // 2):
                tmp = matrix[i][k]
                matrix[i][k] = matrix[n - 1 - k][i]  # copy left to top
                matrix[n - 1 - k][i] = matrix[n - 1 - i][n - 1 - k]  # copy bottom to left
                matrix[n - 1 - i][n - 1 - k] = matrix[k][n - 1 - i]  # copy right to bottom
                matrix[k][n - 1 - i] = tmp  # copy top to right


"""
Array

observation:
to rotate square aray clockwise for 90 degree, we can do this
1. flip entire array vertically, i.e., row 0 swaps with row n-1, row 1 swaps with row n-2, etc.
2. flip along diagonal swap matrix[i][j] with matrix[j][i]
"""

class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # flip vertically
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]

        # flip diagonally
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def main():
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix)
    assert matrix == [[7,4,1],[8,5,2],[9,6,3]], 'fails'

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(matrix)
    assert matrix == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]], 'fails'

    matrix = [[1]]
    sol.rotate(matrix)
    assert matrix == [[1]], 'fails'

    matrix = [[1, 2], [3, 4]]
    sol.rotate(matrix)
    assert  matrix == [[3,1],[4,2]], 'fails'


if __name__ == '__main__':
   main()