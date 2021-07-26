"""
174. Dungeon Game
Hard

2540

53

Add to List

Share
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.



Example 1:


Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
Example 2:

Input: dungeon = [[0]]
Output: 1


Constraints:

m == dungeon.length
n == dungeon[i].length
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000
"""
from typing import List

"""
DP

dp[i][j] := minimum health to reach cell (i, j) with positive health and keep positive health after dungeon[i][j]

base
dp[m-1][n-1] = max(1, 1-dungeon[m-1][n-1])

transition
dp[i][j] = min(max(1, dp[i][j+1] - dungeon[i][j]),
               max(1, dp[i+1][j] - dungeon[i][j])
               )

-2 -3   4
-5 -10  1
10 30  -5

(7,21)   (4,18) (1)
(19,20)   15    (5)
1        1      6

2,2: dp+(-5)>=1 => dp >= 1 - (-5) => dp = 6
2,1: dp[2][1]+dungeon[2][1](30) >= max(1, dp[2][2])
     dp[2][1] = max(1, dp[2][2] - dungeon[2][1])

time O(M*N)
space O(M*N)

"""


class Solution0:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        dp = [[1 for _ in range(n)] for _ in range(m)]
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])
        # print(dp)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue  # init condition
                else:
                    if i + 1 < m and j + 1 < n:
                        dp[i][j] = max(1, min(dp[i][j + 1] - dungeon[i][j], dp[i + 1][j] - dungeon[i][j]))
                    elif j + 1 < n:
                        dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j])
                    elif i + 1 < m:
                        dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j])
                # print('i=%s j=%s dp[i][j]=%s' % (i, j, dp[i][j]))

        # print(dp)
        return dp[0][0]


"""
DP Recursive / top down
"""


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        def get_min_hp(i, j, d, memo):
            if i > m - 1 or j > n - 1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if i == m - 1 and j == n - 1:
                ans = max(1, 1 - d[i][j])
                memo[(i, j)] = ans
                return ans
            if i < m - 1 and j < n - 1:
                ans = max(1, min(get_min_hp(i + 1, j, d, memo) - d[i][j],
                                 get_min_hp(i, j + 1, d, memo) - d[i][j]),
                          )
                memo[(i, j)] = ans
                return ans
            elif i < m - 1:
                ans = max(1, get_min_hp(i + 1, j, d, memo) - d[i][j])
                memo[(i, j)] = ans
                return ans
            elif j < n - 1:
                ans = max(1, get_min_hp(i, j + 1, d, memo) - d[i][j])
                memo[(i, j)] = ans
                return ans

        memo = {}
        ans = get_min_hp(0, 0, dungeon, memo)

        return ans


def main():
    sol = Solution()

    assert sol.calculateMinimumHP(dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]) == 7, 'fails'

    assert sol.calculateMinimumHP(dungeon = [[0]]) == 1, 'fails'


if __name__ == '__main__':
   main()