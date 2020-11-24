"""
877. Stone Game
Medium

898

1169

Add to List

Share
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.



Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.


Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.

"""
from functools import lru_cache
from typing import List

"""
observation: let Lee's move deduct the score amount from Alex score points
dp(i, j) : maximum score Alex can get more then Lee with remaining piles [i, .., j]

time O(n^2)
space O(n^2)

"""


class Solution1:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def helper(i, j, score):
            """
            parity = 1 means first player, -1 means second player (first play lose this score point)
            """
            if i > j:
                return 0
            elif i == j:
                return piles[i] * score
            return max(helper(i + 1, j, score=(-1) * score) + piles[i] * score,
                       helper(i, j - 1, score=(-1) * score) + piles[j] * score)

        return helper(0, len(piles) - 1, score=1) > 0


"""
dp bottom up
2-d dp
time O(n^2)
space O(n^2)
"""


class Solution2:
    def stoneGame(self, piles: List[int]) -> bool:
        l = len(piles)
        dp = [[0 for _ in range(l)] for _ in range(l)]

        for i in range(l):
            for j in range(l - 1, -1, -1):  # from l-1 to 0
                parity = (j + 1 - i) % 2  # parity = 0 is first player
                if parity == 0:
                    dp[i][j] = max(dp[i - 1][j] + piles[i], dp[i][j - 1] + piles[j])
                else:  # Alex's minimize score on this step means Lee's optimal move for max score
                    dp[i][j] = min(dp[i - 1][j] + piles[i], dp[i][j - 1] + piles[j])

        return dp[-1][0] > 0


"""
dp bottom up

1-d dp
time O(n^2)
space O(n)
"""


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l = len(piles)
        dp = [0 for _ in range(l)]

        for i in range(l):
            prev_dp = dp[:]
            for j in range(l - 1, -1, -1):  # from l-1 to 0
                parity = (j + 1 - i) % 2  # parity = 0 is first player
                if parity == 0:
                    dp[j] = max(prev_dp[j] + piles[i], dp[j - 1] + piles[j])
                else:  # Alex's minimize score on this step means Lee's optimal move for max score
                    dp[j] = min(prev_dp[j] + piles[i], dp[j - 1] + piles[j])

        return dp[0]


def main():
    sol = Solution()
    assert sol.stoneGame([5,3,4,5]) is True, 'fails'

if __name__ == '__main__':
   main()