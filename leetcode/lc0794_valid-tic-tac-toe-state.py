"""
794. Valid Tic-Tac-Toe State
Medium

295

817

Add to List

Share
Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares ' '.
The first player always places 'X' characters, while the second player always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.


Example 1:


Input: board = ["O  ","   ","   "]
Output: false
Explanation: The first player always plays "X".
Example 2:


Input: board = ["XOX"," X ","   "]
Output: false
Explanation: Players take turns making moves.
Example 3:


Input: board = ["XXX","   ","OOO"]
Output: false
Example 4:


Input: board = ["XOX","O O","XOX"]
Output: true


Constraints:

board.length == 3
board[i].length == 3
board[i][j] is either 'X', 'O', or ' '.
"""
from typing import List

"""
String/Array

four invalid states:
1. more O's than X's
2. count(X) - count(O) > 1
3. X wins but count(X) == count(O)
4. O wins but count(X) > count(O)

"""


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        ocount = 0
        xcount = 0

        orows = [0 for _ in range(3)]
        ocols = [0 for _ in range(3)]
        odiag = 0
        oadiag = 0

        xrows = [0 for _ in range(3)]
        xcols = [0 for _ in range(3)]
        xdiag = 0
        xadiag = 0

        for i in range(3):
            for j in range(3):
                if board[i][j] == 'O':
                    ocount += 1
                    orows[i] += 1
                    ocols[j] += 1
                    if i == j:
                        odiag += 1
                    if i + j == 2:
                        oadiag += 1
                elif board[i][j] == 'X':
                    xcount += 1
                    xrows[i] += 1
                    xcols[j] += 1
                    if i == j:
                        xdiag += 1
                    if i + j == 2:
                        xadiag += 1

        if xcount - ocount < 0 or xcount - ocount > 1:
            # print('xcount=%s ocount=%s' % (xcount, ocount))
            return False

        # print('orows=%s ocols=%s odiag=%s oadiag=%s xrows=%s xcols=%s xdiag=%s xadiag=%s' % (orows, ocols, odiag, oadiag, xrows, xcols, xdiag, xadiag))
        if (any([x == 3 for x in orows]) or any(
                [x == 3 for x in ocols]) or odiag == 3 or oadiag == 3) and ocount < xcount:
            return False
        if (any([x == 3 for x in xrows]) or any(
                [x == 3 for x in xcols]) or xdiag == 3 or xadiag == 3) and ocount == xcount:
            return False

        return True

def main():
    sol = Solution()

    assert sol.validTicTacToe(board = ["O  ","   ","   "]) == False, 'fails'

    assert sol.validTicTacToe(board = ["XOX"," X ","   "]) == False, 'fails'

    assert sol.validTicTacToe(board = ["XXX","   ","OOO"]) == False, 'fails'

    assert sol.validTicTacToe(board = ["XOX","O O","XOX"]) == True, 'fails'

if __name__ == '__main__':
   main()

