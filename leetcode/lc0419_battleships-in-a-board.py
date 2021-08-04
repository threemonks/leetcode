"""
419. Battleships in a Board
Medium

1073

653

Add to List

Share
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).



Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.


Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
"""
from typing import List

"""
DFS count # of islands

DFS recursively visit all nodes of an island, and mark them as empty
"""
from collections import deque


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j):
            board[i][j] = '.'
            for ni, nj in [(i + di, j + dj) for di, dj in dirs]:
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'X':
                    dfs(ni, nj)

        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    ans += 1
                    dfs(i, j)

        return ans


def main():
    sol = Solution()
    assert sol.countBattleships(board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]) == 2, 'fails'

if __name__ == '__main__':
   main()