"""
1914. Cyclically Rotating a Grid
Medium

76

151

Add to List

Share
You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:



A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:


Return the matrix after applying k cyclic rotations to it.



Example 1:


Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]
Explanation: The figures above represent the grid at every state.
Example 2:


Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
Explanation: The figures above represent the grid at every state.


Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 50
Both m and n are even integers.
1 <= grid[i][j] <= 5000
1 <= k <= 10^9
"""
from typing import List

"""
Array

1. consider each layer as an array, cycle it, process layer by layer until we hit the middle
2. for each layer, we only need to process k % (array length, or cycle perimeter) times

time: O(m*n*(k%(2*(m+n)))*min(m,n))
"""


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        grid1 = [[0 for _ in range(n)] for _ in range(m)]

        a, b = m, n  # dimension of this layer, size a*b
        c = 0  # layer count
        while a > 0 and b > 0:
            # store this layer into an array
            total = 2 * (a + b) - 4 # all 4 corners are double counted
            kc = k % total
            # print('a=%s b=%s c=%s total=%s kc=%s' % (a, b, c, total, kc))
            while kc:

                # copy grid to grid1
                for i in range(m):
                    for j in range(n):
                        grid1[i][j] = grid[i][j]
                # print(grid1)

                # top
                i = 0
                for j in range(1, b):
                    # print('i+c=%s j-1+c=%s' % (i+c, j-1+c))
                    grid1[i + c][j - 1 + c] = grid[i + c][j + c]

                # bottom
                i = a - 1
                for j in range(b - 1):
                    # print('i+c=%s j+1+c=%s' % (i+c, j+1+c))
                    grid1[i + c][j + 1 + c] = grid[i + c][j + c]

                # left
                j = 0
                for i in range(a - 1):
                    # print('i+1+c=%s j+c=%s' % (i+1+c, j+c))
                    grid1[i + 1 + c][j + c] = grid[i + c][j + c]

                # right
                j = b - 1
                for i in range(1, a):
                    # print('i-1+c=%s j+c=%s' % (i-1+c, j+c))
                    grid1[i - 1 + c][j + c] = grid[i + c][j + c]

                # print('kc=%s' % kc)

                # copy grid1 back to grid
                for i in range(m):
                    for j in range(n):
                        grid[i][j] = grid1[i][j]
                # print(grid)

                kc -= 1

            # next layer
            a -= 2
            b -= 2
            c += 1

        return grid

def main():
    sol = Solution()
    assert sol.rotateGrid(grid = [[40,10],[30,20]], k = 1) == [[10,20],[40,30]], 'fails'

    assert sol.rotateGrid(grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2) == [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]], 'fails'


if __name__ == '__main__':
   main()