"""
289. Game of Life
Medium

2797

352

Add to List

Share
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.



Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.


Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

"""
"""
Array
use a hash map to store value from current round

optimize O(1) space: use -1 indicates 1=>0, 2 indicates 0=>1, after updated all cells, then replace all <=0 with 0, replace >0 with 1

follow up inifinite boards:
  the boards are read from file, only three rows in memory, process and discard unneeded rows, then read new rows to process

time: O(m*n)
space: O(m*n)
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        status = {}

        for i in range(m):
            for j in range(n):
                status[(i, j)] = board[i][j]

        for i in range(m):
            for j in range(n):
                dirs = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]

                liveneighbors = sum(
                    [status[(i + dx, j + dy)] for dx, dy in dirs if 0 <= i + dx < m and 0 <= j + dy < n])
                if liveneighbors < 2:
                    board[i][j] = 0
                # elif 2 <= liveneighbors <= 3:
                #     pass
                elif liveneighbors > 3:
                    board[i][j] = 0
                elif liveneighbors == 3:
                    board[i][j] = 1


def main():
    sol = Solution()
    assert sol.gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]) == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]], 'fails'

    assert sol.gameOfLife(board = [[1,1],[1,0]]) == [[1,1],[1,1]], 'fails'

if __name__ == '__main__':
   main()