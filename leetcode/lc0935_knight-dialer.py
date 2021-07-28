"""
935. Knight Dialer
Medium

973

307

Add to List

Share
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:


We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).


Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.



Example 1:

Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
Example 2:

Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
Example 3:

Input: n = 3
Output: 46
Example 4:

Input: n = 4
Output: 104
Example 5:

Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.


Constraints:

1 <= n <= 5000
"""
"""
DP

dp[i][j] := how many # of dialings can we have after dialed j-th numbers (j jumps) when landing on i

transition is sum number of different jumps a given number can come front

dp[1] = 1 => {6, 7}
dp[2] = 1 => {7, 9}
dp[3] = 1 => {4, 8}
dp[4] = 1 => {0, 3,9}
dp[5] = 1
dp[6] = 1 => {0, 1,7}
dp[7] = 1 => {2,6}
dp[8] = 1 => {1, 3}
dp[9] = 1 => {2,4}
dp[0] = 1 => {4, 6}

"""


class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0 for _ in range(10)] for _ in range(n + 1)]

        dp[1][0] = 1  # 4,6
        dp[1][1] = 1  # 6,7
        dp[1][2] = 1  # 7,9
        dp[1][3] = 1  # 4,8
        dp[1][4] = 1  # 0, 3, 9
        dp[1][5] = 1
        dp[1][6] = 1  # 0, 1, 7
        dp[1][7] = 1  # 2,6
        dp[1][8] = 1  # 1,3
        dp[1][9] = 1  # 2,4

        for j in range(2, n + 1):
            dp[j][0] = (dp[j - 1][4] + dp[j - 1][6]) % MOD
            dp[j][1] = (dp[j - 1][6] + dp[j - 1][8]) % MOD
            dp[j][2] = (dp[j - 1][7] + dp[j - 1][9]) % MOD
            dp[j][3] = (dp[j - 1][4] + dp[j - 1][8]) % MOD
            dp[j][4] = (dp[j - 1][0] + dp[j - 1][3] + dp[j - 1][9]) % MOD
            dp[j][6] = (dp[j - 1][0] + dp[j - 1][1] + dp[j - 1][7]) % MOD
            dp[j][7] = (dp[j - 1][2] + dp[j - 1][6]) % MOD
            dp[j][8] = (dp[j - 1][1] + dp[j - 1][3]) % MOD
            dp[j][9] = (dp[j - 1][2] + dp[j - 1][4]) % MOD

        return sum([dp[n][i] for i in range(10)]) % MOD

def main():
    sol = Solution()
    assert sol.knightDialer(1) == 10, 'fails'

    assert sol.knightDialer(2) == 20, 'fails'

    assert sol.knightDialer(3) == 46, 'fails'

    assert sol.knightDialer(4) == 104, 'fails'

    assert sol.knightDialer(3131) == 136006598, 'fails'

if __name__ == '__main__':
   main()