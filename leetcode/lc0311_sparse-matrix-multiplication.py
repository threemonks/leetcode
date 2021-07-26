"""
311. Sparse Matrix Multiplication
Medium

674

256

Add to List

Share
Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.



Example 1:


Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
Output: [[7,0,0],[-7,0,3]]
Example 2:

Input: mat1 = [[0]], mat2 = [[0]]
Output: [[0]]


Constraints:

m == mat1.length
k == mat1[i].length == mat2.length
n == mat2[i].length
1 <= m, n, k <= 100
-100 <= mat1[i][j], mat2[i][j] <= 100

"""
from typing import List

"""
Hash Table

use hash table to store non-zero element, only do multiplication on non-zero elements if r2==c1, and add result to ans[r1][c2]

"""


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        dict1 = {}
        m, n = len(mat1), len(mat1[0])
        for i in range(m):
            for j in range(n):
                if mat1[i][j] != 0:
                    dict1[(i, j)] = mat1[i][j]

        dict2 = {}
        x, y = len(mat2), len(mat2[0])
        for i in range(x):
            for j in range(y):
                if mat2[i][j] != 0:
                    dict2[(i, j)] = mat2[i][j]

        ans = [[0 for _ in range(y)] for _ in range(m)]
        for r1, c1 in dict1.keys():
            for r2, c2 in dict2.keys():
                if c1 == r2:
                    ans[r1][c2] += dict1[(r1, c1)] * dict2[(r2, c2)]

        return ans


def main():
    sol = Solution()
    assert sol.multiply(mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]) == [[7,0,0],[-7,0,3]], 'fails'

    assert sol.multiply(mat1 = [[0]], mat2 = [[0]]) == [[0]], 'fails'


if __name__ == '__main__':
   main()
