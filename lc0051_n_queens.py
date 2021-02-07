"""
51. N-Queens
Hard

2611

96

Add to List

Share
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.



Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]


Constraints:

1 <= n <= 9
"""
from typing import List

"""
1. put one queen on any one of the cells in first row
2. mark all cells it checks (same x, same y, or diagonally straigh line (for (x,y) and (i,j), the check condition is x-i==y-j)) as checked
3. repeat the above step for all following rows
4. repeat the above to find different solutions

time O(N!) N possibilities for first queen, not more than N(N-2) to put the second one, and not more than N(N-2)(N-4) for thrid one etc, so total is O(N!) time
space O(N)

"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def checkok(path, i, j):
            for x, y in path:
                if x == i or y == j or x - i == y - j or x - i == -(y - j):
                    return False
            return True

        result = []

        def helper(i, path):
            nonlocal result
            if i == n:
                result.append(path)
                return
            for j in range(n):
                if checkok(path, i, j):
                    helper(i + 1, path + [(i, j)])

        helper(0, [])
        output = []
        for res in result:
            res1 = []
            for i in range(n):
                res1.append(''.join(['Q' if (i, j) in res else '.' for j in range(n)]))

            output.append(res1)

        return output

def main():
    sol = Solution()
    assert sol.solveNQueens(4) == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]], 'fails'

    assert sol.solveNQueens(1) == [["Q"]], 'fails'


if __name__ == '__main__':
   main()