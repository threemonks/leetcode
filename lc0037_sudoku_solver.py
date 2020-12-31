"""
37. Sudoku Solver
Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.



Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:




Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.

"""
from typing import List

"""
dfs / recusrive
for any empty cell [i][j], try all digits (123456789), if a given digit is valid for (row, column and box), dfs/recusrive call to proceed to next cell ([i][j+1]) (note boundary case, j==9 (go to next row [i+1][0]), or i==9 (last row, done!)), if dfs call returns True, we return True, otherwise proceed to try next digit
  if all digits fails, we reset this cell to '.', and return false to go back to caller (previous cell)

"""

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(board, i, j):
            # check row
            if any([board[i][j] == board[i][k] for k in range(9) if k != j]): return False
            # check column
            if any([board[i][j] == board[k][j] for k in range(9) if k != i]): return False
            # check box
            for m in range(i // 3 * 3, i // 3 * 3 + 3):
                for n in range(j // 3 * 3, j // 3 * 3 + 3):
                    if board[m][n] == board[i][j] and not (m == i and n == j):
                        return False

            return True

        def dfs(board, i, j):
            # bounday condition, if i exceeds last row, we are done
            if i == 9:
                return True
            # boundary condition, if j exceeds boundary, go to 0 col of next row
            if j == 9:
                return dfs(board, i + 1, 0)
            if board[i][j] != '.':
                return dfs(board, i, j + 1)
            # if board[i][j] is ., then try to fill with any one of digits 123456789, and dfs/recursive call to next dfs(board, i, j+1)
            for d in list('123456789'):
                board[i][j] = d
                if is_valid(board, i, j):
                    if dfs(board, i, j + 1):
                        return True
            # if all digits fails, we reset board[i][j] back to '.', and go back to previous step
            board[i][j] = '.'
            return False

        dfs(board, 0, 0)
        return

def main():
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    sol.solveSudoku(board = board)
    assert board == [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]], 'fails'

if __name__ == '__main__':
   main()