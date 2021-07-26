"""
308. Range Sum Query 2D - Mutable
Hard

508

66

Add to List

Share
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:

NumMatrix(int[][] matrix) initializes the object with the integer matrix matrix.
void update(int row, int col, int val) updates the value of matrix[row][col] to be val.
int sumRegion(int row1, int col1, int row2, int col2) returns the sum of the elements of the matrix array inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).


Example 1:


Input
["NumMatrix", "sumRegion", "update", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]
Output
[null, 8, null, 10]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8
numMatrix.update(3, 2, 2);
numMatrix.sumRegion(2, 1, 4, 3); // return 10


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-10^5 <= matrix[i][j] <= 10^5
0 <= row < m
0 <= col < n
-10^5 <= val <= 10^5
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 10^4 calls will be made to sumRegion and update.
"""
from typing import List

"""
Segement Tree

Best solution would be 2D segment tree to get O(log(M)*log(N)) on both update and sumRegion

However, we can pre-calculate prefix sum within 1d array to get O(MN) time complexity on both update and sumRegion

time: O(M*N)
"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # convert each row to presum
        self.matrix = matrix
        self.maxrow = len(matrix)
        self.maxcol = len(matrix[0])
        for r in range(self.maxrow):
            for c in range(self.maxcol):
                self.matrix[r][c] += self.matrix[r][c - 1] if c - 1 >= 0 else 0

    def update(self, row: int, col: int, val: int) -> None:
        # to update, calculate diff with orig value (orig = val[r][c]-val[r]c-1)
        # then apply this diff to all cols from col to end of row
        orig = self.matrix[row][col] - (self.matrix[row][col - 1] if col - 1 >= 0 else 0)
        diff = val - orig
        for c in range(col, self.maxcol):
            self.matrix[row][c] += diff

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for r in range(row1, row2 + 1):
            ans += self.matrix[r][col2] - (self.matrix[r][col1 - 1] if col1 - 1 >= 0 else 0)

        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

"""
Input
["NumMatrix", "sumRegion", "update", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]
Output
[null, 8, null, 10]
"""
def main():

    obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    assert obj.sumRegion([2, 1, 4, 3]) == 8, 'fails'
    obj.update([3, 2, 2])
    assert obj.sumRegion([2, 1, 4, 3]) == 10, 'fails'

if __name__ == '__main__':
   main()