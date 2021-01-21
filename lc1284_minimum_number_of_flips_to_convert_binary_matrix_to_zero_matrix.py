"""
1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
Hard

Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbours of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighboors if they share one edge.

Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.

Binary matrix is a matrix with all cells equal to 0 or 1 only.

Zero matrix is a matrix with all cells equal to 0.



Example 1:


Input: mat = [[0,0],[0,1]]
Output: 3
Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.
Example 2:

Input: mat = [[0]]
Output: 0
Explanation: Given matrix is a zero matrix. We don't need to change it.
Example 3:

Input: mat = [[1,1,1],[1,0,1],[0,0,0]]
Output: 6
Example 4:

Input: mat = [[1,0,0],[1,0,0]]
Output: -1
Explanation: Given matrix can't be a zero matrix


Constraints:

m == mat.length
n == mat[0].length
1 <= m <= 3
1 <= n <= 3
mat[i][j] is 0 or 1.

"""

import heapq
from typing import List

"""
modified BFS/dijsktra's algorithm with bitmask compression

use number of steps as metrics to pick which next state to explore first

we need to keep track of visisted state of matrix, use bitmask to represent each state of matrix

for each state, we explore every node on array and flipping it (along with its neighbor nodes), and enque the new state (if not visited yet) for further exploration

termination condition is state == 0 (all elements are 0)

time O(2^(m*n)*m*n)
space O(m*n)
"""


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        visited = set()
        state = 0  # convert 2-d array mat to a integer of bitmask
        for i in range(m):
            for j in range(n):
                state |= (mat[i][j] << i * n + j)  # add all 1 bits into state
        if state == 0:
            return 0
        q = [(0, state)]  # steps, initial state of matrix
        heapq.heapify(q)
        # print('state=%s' % state)
        visited.add(state)

        while q:
            # print('q=%s' % (q))
            steps, state = heapq.heappop(q)
            if state == 0:
                return steps
            for i in range(m):  # try all nodes in the array
                for j in range(n):
                    tmp_state = state
                    # flip this node and its valid neighbors
                    for (ni, nj) in [(i, j), (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if (ni >= 0 and ni < m and nj >= 0 and nj < n):
                            tmp_state ^= (
                                        1 << ni * n + nj)  # flip ni*n+nj bit, corresponding to (ni, nj) in original array
                    if tmp_state not in visited:  # new state found, enque it for further exploration
                        heapq.heappush(q, (steps + 1, tmp_state))
                        visited.add(tmp_state)

        return -1


def main():
    sol = Solution()
    assert sol.minFlips([[0,0],[0,1]]) == 3, 'fails'

    assert sol.minFlips([[0]]) == 0, 'fails'

    assert sol.minFlips([[1,1,1],[1,0,1],[0,0,0]]) == 6, 'fails'

    assert sol.minFlips([[1,0,0],[1,0,0]]) == -1, 'fails'


if __name__ == '__main__':
   main()