"""
1411. Number of Ways to Paint N × 3 Grid
Hard

397

23

Add to List

Share
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown:

Example 2:

Input: n = 2
Output: 54
Example 3:

Input: n = 3
Output: 246
Example 4:

Input: n = 7
Output: 106494
Example 5:

Input: n = 5000
Output: 30228214


Constraints:

n == grid.length
grid[i].length == 3
1 <= n <= 5000

"""

"""
DP

to make sure no same color adjacent on same row, and between adjacent rows, one row could only have either two or three colors
assume

first row there could be 6 ways of painting 2 colors: RYR RGR YRY YGY GRG GYG
                similary 6 ways of painting 3 colors: RYG RGY YRG YGR GYR GRY

row i is 2 colors: ABA => row i+1 can have either two colors, BAB, BCB, CAC (3 different ways)
                      or i+1 row can have three colors BAC, CAB (2 different ways)
if row i is 3 colors: ABC => row i+1 could be three colors: BCA CAB (2 different patterns)
                                           or two colors: BAB BCB (2 ways)

i.e., color2 = 3*prev_color2 + 2*prev_color3
      color3 = 2*prev_color2 + 2*prev_color3

"""


class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        color2 = 6
        color3 = 6

        for i in range(1, n):
            prev_color2, prev_color3 = color2, color3  # keep both color2 and color3 from previous round for calculation
            color2 = (3 * prev_color2 + 2 * prev_color3) % MOD
            color3 = (2 * prev_color2 + 2 * prev_color3) % MOD

        return (color2 + color3) % MOD

def main():
    sol = Solution()
    assert sol.numOfWays(1) == 12, 'fails'

    assert sol.numOfWays(2) == 54, 'fails'

    assert sol.numOfWays(3) == 246, 'fails'

    assert sol.numOfWays(4) == 106494, 'fails'

    assert sol.numOfWays(5) == 30228214, 'fails'

if __name__ == '__main__':
   main()