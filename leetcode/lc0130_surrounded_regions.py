"""
130. Surrounded Regions
Medium

5726

1340

Add to List

Share
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""
from typing import List

"""
DFS

search for connected O from any of the side cells, turn them to *
then turn all remaining O (not connected with O's from side) to X
then turn * back to O

"""
class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        # print(f"{m=} {n=}")

        def dfs(i, j):
            m, n = len(board), len(board[0])
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for nx, ny in [(i+dx, j+dy) for (dx, dy) in dirs]:
                if (0 <= nx < m and 0 <= ny < n) and board[nx][ny] == 'O':
                    board[nx][ny] = '*'
                    dfs(nx, ny)


        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = '*'
                    # dfs
                    dfs(i, j)
                # print(f"1 {i=} {j=} {board=} {board[i][j]=}")

        for j in [0, n-1]:
            for i in range(m):
                if board[i][j] == 'O':
                    board[i][j] = '*'
                    # dfs
                    dfs( i, j)
                # print(f"2 {i=} {j=} {board=} {board[i][j]=}")

        # print(f"after dfs {board=}")

        # change all remaining O to X
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        # print(f"after capturing {board=}")

        # change all * to O
        for i in range(m):
            for j in range(n):
                if board[i][j] == '*':
                    board[i][j] = 'O'

        # print(f"after reset * to O {board=}")


def main():
    sol = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sol.solve(board)
    assert board == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]], 'fails'

    board = [["X"]]
    sol.solve(board)
    assert board == [["X"]], 'fails'

if __name__ == '__main__':
   main()