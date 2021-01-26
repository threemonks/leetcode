"""
909. Snakes and Ladders
Medium

On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board, and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:


You start on square 1 of the board (which is always in the last row and first column).  Each move, starting from square x, consists of the following:

You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
(This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations, regardless of the size of the board.)
If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The destination of that snake or ladder is board[r][c].

Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at `3`, because you do not continue moving to `4`.)

Return the least number of moves required to reach square N*N.  If it is not possible, return -1.

Example 1:

Input: [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation:
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
Note:

2 <= board.length = board[0].length <= 20
board[i][j] is between 1 and N*N or is equal to -1.
The board square with number 1 has no snake or ladder.
The board square with number N*N has no snake or ladder.
"""
import heapq
from typing import List

"""
BFS use bfs to find shortest path with some special setup (snake/ladder)

Note: 1. we cannot mark snake or ladder entry point as visited
      2. row number starts from bottom up
      3. column number starts from left on even rows (from bottom), and alternate after, i.e., starts from right on even rows
      4. board cell numbers start from 1

time O(N^2)
space O(N^2)

"""


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        q = [(0, 1)]
        heapq.heapify(q)
        seen = {1: 0}  # nodes visited, and the cost associated

        def get_rc(s):
            # given a square number s, return its row and column in board, row starts from bottom
            # even (start at 0-th) row from bottom goes left to right
            # odd row from bottom goes from right to left

            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot  # row # starts from bottom
            col = rem if quot % 2 == 0 else n - 1 - rem  # boustrophedonically

            return row, col

        while q:
            cost, s = heapq.heappop(q)
            if s == n * n:
                return cost
            for s2 in range(s + 1, min(s + 6, n * n) + 1):
                row, col = get_rc(s2)
                if board[row][col] != -1:  # follow snake or ladder
                    s2 = board[row][col]  # board dimension is 0 index, but board cell value starts at 1
                if s2 not in seen or cost + 1 < seen[s2]:
                    seen[s2] = cost + 1
                    heapq.heappush(q, (cost + 1, s2))

        return -1

def main():
    sol = Solution()
    assert sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1], [-1,-1,-1,-1,-1,-1], [-1,-1,-1,-1,-1,-1], [-1,35,-1,-1,13,-1], [-1,-1,-1,-1,-1,-1], [-1,15,-1,-1,-1,-1]]) == 4, 'fails'

    assert sol.snakesAndLadders([[-1,4,-1],[6,2,6],[-1,3,-1]]) == 2, 'fails'

    assert sol.snakesAndLadders([[1, 1, -1], [1, 1, 1], [-1, 1, 1]]) == -1, 'fails'

    assert sol.snakesAndLadders([[-1, 7, -1], [-1, 6, 9], [-1, -1, 2]]) == 1, 'fails'



if __name__ == '__main__':
   main()