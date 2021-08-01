"""
59. Spiral Matrix II
Medium

1863

137

Add to List

Share
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20
"""
from typing import List

"""
Array

fill layer by layer
within each layer, fill top (left to right), right (top to bottom), bottom (right to left), and left (bottom to top)

1  2  3   4
12 13 14  5
11 16 15  6
10  9  8  7
time O(N^2)
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0 for _ in range(n)] for _ in range(n)]

        layer = 0
        num = 1

        while num <= n * n:
            # top
            i = layer + 0
            for j in range(layer, n - layer):
                grid[i][j] = num
                num += 1

            # print('after top grid=%s' % grid)

            # right
            j = n - 1 - layer
            for i in range(layer + 1, n - layer):
                grid[i][j] = num
                num += 1

            # print('after right grid=%s' % grid)

            # bottom
            i = n - 1 - layer
            for j in range(n - 2 - layer, layer - 1, -1):
                grid[i][j] = num
                num += 1

            # print('after bottom grid=%s' % grid)

            # left
            j = 0 + layer
            for i in range(n - 1 - layer - 1, layer, -1):
                grid[i][j] = num
                num += 1

            # print('after left grid=%s' % grid)

            # to next layer
            layer += 1

        return grid


def main():
    sol = Solution()
    assert sol.generateMatrix(3) == [[1,2,3],[8,9,4],[7,6,5]], 'fails'

    assert sol.generateMatrix(1) == [[1]], 'fails'

if __name__ == '__main__':
   main()