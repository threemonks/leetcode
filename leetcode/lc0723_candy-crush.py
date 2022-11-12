"""
723. Candy Crush
Medium

881

422

Add to List

Share
This question is about implementing a basic elimination algorithm for Candy Crush.

Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy. A value of board[i][j] == 0 represents that the cell is empty.

The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the stable board.



Example 1:


Input: board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
Output: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
Example 2:

Input: board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
Output: [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]
"""
from typing import List

"""
Matrix
"""


class Solution:
    def crush(self, board, coords):
        """
        return list of coordinations that can be crushed
        """
        m, n = len(board), len(board[0])

        # print(f"to crush {coords = } {board = }")
        # replace with 0
        for x, y in coords:
            board[x][y] = 0

        # drop to first non-zero
        # for each column
        # drop all items if bottom element is zero
        for j in range(n):
            new_col = [board[i][j] for i in range(m - 1, -1, -1) if board[i][j] > 0]  # take all non-zero values
            for i in range(m):
                board[m - 1 - i][j] = new_col[i] if i < len(new_col) else 0  # assign to board[:][j] from bottom to top

        # print(f"after crush {coords = } {board = }")

    def can_crush(self, board):
        """
        return list of coordinations that can be crushed
        """
        m, n = len(board), len(board[0])

        res = set()

        for i in range(m):
            for j in range(n - 2):
                if board[i][j] > 0 and board[i][j] == board[i][j + 1] and board[i][j + 1] == board[i][j + 2]:
                    res.add((i, j))
                    res.add((i, j + 1))
                    res.add((i, j + 2))

        for j in range(n):
            for i in range(m - 2):
                if board[i][j] > 0 and board[i][j] == board[i + 1][j] and board[i + 1][j] == board[i + 2][j]:
                    res.add((i, j))
                    res.add((i + 1, j))
                    res.add((i + 2, j))

        return res

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        coords = self.can_crush(board)
        while coords:
            # print(f"to crush {coords = }")
            self.crush(board, coords)
            coords = self.can_crush(board)

        return board

def main():

    sol = Solution()

    assert sol.candyCrush(board = [[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414],
                    [5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2],
                    [4, 1, 4, 4, 1014]]) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [110, 0, 0, 0, 114], [210, 0, 0, 0, 214],
             [310, 0, 0, 113, 314], [410, 0, 0, 213, 414], [610, 211, 112, 313, 614], [710, 311, 412, 613, 714],
             [810, 411, 512, 713, 1014]], 'fails'

    assert sol.candyCrush(board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]) == [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]], 'fails'


if __name__ == '__main__':
   main()