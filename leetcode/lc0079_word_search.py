"""
79. Word Search
Medium

Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 200
1 <= word.length <= 103
board and word consists only of lowercase and uppercase English letters.

"""
from typing import List

"""
DFS / backtracking

brutal force traversing and remember entire path and compare the word from path to compare with target word

this AC, but pretty slow

time O(M*N*3^L) - (M, N) is board size, L is len(word), 3^L comes from for each cell, there's four directions, but one is the one we come front, so there's 3 directions to expore on each cell
space O(L)

"""
class Solution0:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, path):
            # print('i=%s j=%s path=%s' % (i, j, path))
            if len(path) == len(word):
                return True
            elif len(path) > len(word):
                return False
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            pathset = set(path)
            for ni, nj in [(i+di, j+dj) for di, dj in dirs if 0<=i+di<m and 0<=j+dj<n]:
                if (ni, nj) not in pathset and board[ni][nj] == word[len(path)]:
                    if dfs(ni, nj, path + [(ni, nj)]):
                        return True

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, [(i, j)]):
                    return True

        return False

"""
DFS / backtracking

start from any cell, try all four directions, to see if the next cell match with next character in word (early pruning), if it does, recursive call with that neighbor, and word[1:] as remaining word


mistakes:
1. initial call to dfs with (0, 0, remaining=word), terminating condition for recursive call is remaining==''

"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])
        if m == 1 and n == 1 and board[0][0] == word[0] and len(word) == 1:
            return True

        def dfs(i, j, remaining):
            # print('i=%s j=%s remaining=%s' % (i, j, remaining))
            if not remaining:
                return True

            # check current status before exploring neighbors
            if i < 0 or i == m or j < 0 or j == n or board[i][j] != remaining[0]:
                return False

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            ret = False
            # mark the cell as visited in this path by modifying its content as '#'
            # we need special handling for single char board, since we won't enter this block with single char board
            board[i][j] = '#'
            for ni, nj in [(i+di, j+dj) for di, dj in dirs if 0<=i+di<m and 0<=j+dj<n]:
                if dfs(ni, nj, remaining[1:]):
                    return True

            board[i][j] = remaining[0]

            return ret

        for i in range(m):
            for j in range(n):
                # print('i=%s j=%s board[i][j]=%s word[0]=%s' % (i, j, board[i][j], word[0]))
                if board[i][j] == word[0]:
                    if dfs(i, j, word):
                        return True

        return False


def main():
    sol = Solution()
    assert sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED") is True, 'fails'

    assert sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE") is True, 'fails'

    assert sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB") is False, 'fails'

if __name__ == '__main__':
   main()