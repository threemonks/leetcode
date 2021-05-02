"""
36. Valid Sudoku
Medium

2527

563

Add to List

Share
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.

"""
from collections import Counter, defaultdict
from typing import List

"""
Hash Table

1. check row
2. check column
3. check 3x3 small square

mistakes:
1. skip dot
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        def isvalid(s):
            if any([v > 1 for v in Counter([c for c in s if c != '.']).values()]):
                return False
            return True

        # check row
        for i in range(n):
            if not isvalid(board[i]):
                # print('failing row %s' % i)
                return False

        # check column
        for i in range(n):
            if not isvalid([board[j][i] for j in range(n)]):
                # print('failing column %s' % i)
                return False

        # check smaller 3x3 square
        counts = defaultdict(set)
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                x = i // 3
                y = j // 3
                if board[i][j] in counts[(x, y)]:
                    # print('failing box %s %s %s %s' % (x, y, i, j))
                    return False
                else:
                    counts[(x, y)].add(board[i][j])

        return True


def main():
    sol = Solution()
    assert sol.isValidSudoku(board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]) == False, 'fails'


if __name__ == '__main__':
   main()