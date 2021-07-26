"""
348. Design Tic-Tac-Toe
Medium

1097

74

Add to List

Share
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.
Follow up:
Could you do better than O(n2) per move() operation?



Example 1:

Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]

Explanation
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|


Constraints:

2 <= n <= 100
player is 1 or 2.
1 <= row, col <= n
(row, col) are unique for each different call to move.
At most n2 calls will be made to move.
"""
"""
Design

use an nxn 2D array init to 0 to present board
player 1 would place 1 in a cell if it is empty
player 2 would place 2 in a cell if it is empty

if anytime there's n of same number in one row, one column, or one diagonal, then he wins, then the game finishes, no more move it s allowed
diagonal: row == col
anti-diagonal row = n-1-col, or row+col == n-1

time O(N) for move
space O(N^2)
"""


class TicTacToe0:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        n = len(self.board)
        self.board[row][col] = player
        # entire column
        if all([self.board[r][col] == player for r in range(n)]):
            self.board[row][col] = player
            return player
        # entire row
        if all([self.board[row][c] == player for c in range(n)]):
            return player
        # entire diagonal
        if all([self.board[i][i] == player for i in range(n)]):
            return player
        # entire anti-diagonal
        if all([self.board[i][n - 1 - i] == player for i in range(n)]):
            return player

        # other wise no one wins yet
        return 0


"""
Design

because the problem description guarantees all moves are valid, so we don't need the entire move history, we only need to check win condition, which is if a given player has played n tile on any row, or column, or diagonal or anti-diagonal

Thus, we only need to keep track each player's count on each column, row, diagonal, and anit-diagonal

if at any move, the current player's current row, or col, or diag or anti-diag counts to n, he/she wins

time O(1) for move
space O(N)

mistakes:
1. check self.p1row[row] == n or self.p1col[col] == n for win
"""


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.p1row = [0 for _ in range(n)]
        self.p1col = [0 for _ in range(n)]
        self.p1diag = 0
        self.p1antidiag = 0

        self.p2row = [0 for _ in range(n)]
        self.p2col = [0 for _ in range(n)]
        self.p2diag = 0
        self.p2antidiag = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        n = len(self.p1row)
        if player == 1:
            self.p1row[row] += 1
            self.p1col[col] += 1
            if row == col:
                self.p1diag += 1
            if row + col == n - 1:  # anti-diagonal
                self.p1antidiag += 1
            if self.p1row[row] == n or self.p1col[col] == n or self.p1diag == n or self.p1antidiag == n:
                return 1
        elif player == 2:
            self.p2row[row] += 1
            self.p2col[col] += 1
            if row == col:
                self.p2diag += 1
            if row + col == n - 1:  # anti-diagonal
                self.p2antidiag += 1
            if self.p2row[row] == n or self.p2col[col] == n or self.p2diag == n or self.p2antidiag == n:
                return 2

        # nobody wins yet
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
"""
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]
"""

def main():

    obj = TicTacToe(3)
    obj.move(0, 0, 1)
    obj.move(0, 2, 2)
    obj.move(2, 2, 1)
    obj.move(1, 1, 2)
    obj.move(2, 0, 1)
    obj.move(1, 0, 2)
    assert obj.move(2, 1, 1) == 1, 'fails'

if __name__ == '__main__':
   main()