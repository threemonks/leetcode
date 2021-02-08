"""
52. N-Queens II
Hard

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 9
"""

"""
backtrack strategy
use backtrack/recusrive call to loop all rows:
   for j in all cols:
        if queen can be placed here at (i, j):
            place_queen(i, j), update attacked (horizontally, vertically, diagonally)
            if last row: solution count ++
            else: continue to next row backtrack(row+1, count)
            remove_queen(i, j) # backtracking
        else:
            go to next column
time O(N^3)
space O(N^2)
"""


class Solution0:
    def totalNQueens(self, n: int) -> int:

        queens = []
        attacked = [[0] * n for _ in range(n)]

        def not_under_attack(row, col):
            nonlocal attacked
            return attacked[row][col] == 0

        def place_queen(row, col):
            nonlocal n, queens, attacked
            queens.append((row, col))
            for i in range(n):
                for j in range(n):
                    if i == row or j == col or i - row == j - col or i - row == -(j - col):
                        attacked[i][j] += 1

        def remove_queen(row, col):
            nonlocal n, queens, attacked
            queens.remove((row, col))
            for i in range(n):
                for j in range(n):
                    if i == row or j == col or i - row == j - col or i - row == -(j - col):
                        attacked[i][j] -= 1

        def backtrack(row, count):
            nonlocal n
            for col in range(n):
                if not_under_attack(row, col):
                    place_queen(row, col)
                    # print('row=%s col=%s count=%s queens=%s attacked=%s' % (row, col, count, queens, attacked))
                    if row == n - 1:  # final row, a successful placement
                        count += 1
                    else:
                        count = backtrack(row + 1, count)  # backtrack and move to next row
                    remove_queen(row, col)
            return count

        return backtrack(0, 0)


"""
use backtrack to find all n-queens solution

-- a queen is in check if it is on same row or col, or diagonal (x-i==y-j or x-i=-(y-j) with another queen

"""


class Solution:
    def totalNQueens(self, n: int) -> int:

        def checkok(x, y, path):
            for i, j in path:
                if i == x or j == y or x - i == y - j or x - i == -(y - j):
                    return False
            return True

        queens = []

        def backtrack(row, path):
            if row == n:
                queens.append(path)
            for col in range(n):
                if checkok(row, col, path):
                    backtrack(row + 1, path + [(row, col)])

        queens = []
        backtrack(0, [])

        return len(queens)

def main():
    sol = Solution()
    assert sol.totalNQueens(4) == 2, 'fails'

    assert sol.totalNQueens(1) == 1, 'fails'


if __name__ == '__main__':
   main()