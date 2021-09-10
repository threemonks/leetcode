"""
562. Longest Line of Consecutive One in Matrix
Medium

561

91

Add to List

Share
Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

The line could be horizontal, vertical, diagonal, or anti-diagonal.



Example 1:


Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3
Example 2:


Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
Output: 4


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
"""
from collections import defaultdict
from typing import List

"""
Hash Map

use hash map to store longest line of consecutive one in four directions: horizontal, vertical, diagonal, anti-diagonal

time O(M*N)
space O(M*N)
"""


class Solution0:
    def longestLine(self, mat: List[List[int]]) -> int:
        counts_h = defaultdict(int)
        counts_v = defaultdict(int)
        counts_d = defaultdict(int)
        counts_ad = defaultdict(int)

        for r, row in enumerate(mat):
            for c, col in enumerate(row):
                if mat[r][c] == 1:
                    # horizontal
                    counts_h[(r, c)] = max(1, 1 + counts_h[(r, c - 1)])
                    # vertical
                    counts_v[(r, c)] = max(1, 1 + counts_v[(r - 1, c)])
                    # diagonal
                    counts_d[(r, c)] = max(1, 1 + counts_d[(r - 1, c - 1)])
                    # anti-diagonal
                    counts_ad[(r, c)] = max(1, 1 + counts_ad[(r - 1, c + 1)])

        ans = 0
        if counts_h.values():
            ans = max(ans, max(counts_h.values()))
        if counts_v.values():
            ans = max(ans, max(counts_v.values()))
        if counts_d.values():
            ans = max(ans, max(counts_d.values()))
        if counts_ad.values():
            ans = max(ans, max(counts_ad.values()))

        return ans


"""
DP

use 3D dp to represent longest consecutive ones to current cell

dp[i][j][d] := longest consecutive ones to current cell [i][j] (with current cell value being 1)
where d is direction:
0 - horizontal
1 - diagonal (\)
2 - vertical
3 - anti-digonal (/)

note:
1. need to take max among entire 3D dp array
2. only need one row of dp from previous row => can simplify to 2D dp array

time O(M*N)
space O(M*N) => can simplify into O(4*N)
"""


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(m)]

        for j in range(n):
            if mat[0][j] == 1:
                dp[0][j][0] = max(1, (1 + dp[0][j - 1][0]) if j - 1 >= 0 else 0)

                # diagonal
                dp[0][j][1] = 1

                # vertical
                dp[0][j][2] = 1

                # anti-diagonal
                dp[0][j][3] = 1

        for i in range(1, m):
            for j in range(n):
                if mat[i][j] == 1:
                    # horizontal
                    dp[i][j][0] = max(1, (1 + dp[i][j - 1][0]) if j - 1 >= 0 else 0)

                    # diagonal
                    dp[i][j][1] = max(1, (1 + dp[i - 1][j - 1][1]) if j - 1 >= 0 else 0)

                    # vertical
                    dp[i][j][2] = max(1, 1 + dp[i - 1][j][2])

                    # anti-diagonal
                    dp[i][j][3] = max(1, (1 + dp[i - 1][j + 1][3]) if j + 1 < n else 0)

        # take max among entire 3D array
        return max([dp[i][j][k] for i in range(m) for j in range(n) for k in range(4)])

def main():
    sol = Solution()
    assert sol.longestLine(mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]) == 3, 'fails'

    assert sol.longestLine(mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]) == 4, 'fails'

if __name__ == '__main__':
   main()