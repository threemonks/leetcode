"""
498. Diagonal Traverse
Medium

1467

438

Add to List

Share
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.



Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
-10^5 <= mat[i][j] <= 10^5

"""
from typing import List

"""
Array

iterate k = 0, 1, 2, ..., m+n-1, and i from min(k,m-1) to 0, and j = k-i

note:
1. needs to alternate direction of diagonal result row with each k value
2. use outloop variable line, and clear it in each k value loop

time O(M+N)
space O(min(M, N))
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])

        ans = []
        line = []
        i, j = 0, 0
        for k in range(m + n - 1):
            line.clear()
            for i in range(min(k, m - 1), -1, -1):
                j = k - i
                if j < 0 or j >= n:
                    continue
                line.append(mat[i][j])
            if k % 2 == 0:
                ans += line
            else:
                ans += line[::-1]

        return ans


def main():
    sol = Solution()
    assert sol.findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]]) == [1,2,4,7,5,3,6,8,9], 'fails'

    assert sol.findDiagonalOrder(mat = [[1,2],[3,4]]) == [1,2,3,4], 'fails'

if __name__ == '__main__':
   main()