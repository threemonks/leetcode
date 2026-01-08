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


class Solution0:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        color2 = 6
        color3 = 6

        for i in range(1, n):
            prev_color2, prev_color3 = color2, color3  # keep both color2 and color3 from previous round for calculation
            color2 = (3 * prev_color2 + 2 * prev_color3) % MOD
            color3 = (2 * prev_color2 + 2 * prev_color3) % MOD

        return (color2 + color3) % MOD

"""
dp (dynamic programming)

a row could have these valid states
ABA: RYR RGR YRY YGY GRG GYG
ABC: RYG RGY GRY GYR YRG YGR

transitions (moving from row i to row i+1)
RYR
-> YRY YGY GRG
-> YRG GRY

RYG
-> YGY YRY
-> YGR GRY

ABA_(n+1) = 3*ABA_(n) + 2 * ABC_(n)

ABC_(n+1) = 2 * ABA_(n) + 2 * ABC_(n)

complexity:
time O(N)
space O(1)

"""
class Solution:
    # solution for 3 colors only
    # def numOfWays(self, n: int) -> int:
    #     MOD = 10**9 + 7

    #     # initial state for n = 1
    #     aba = 6
    #     abc = 6

    #     for i in range(2, n+1):
    #         # calculate next values based on transactions
    #         next_aba = (3*aba + 2 * abc) % MOD
    #         next_abc = (2*aba + 2 * abc) % MOD

    #         #update current value for next iteration
    #         aba, abc = next_aba, next_abc

    #     return (aba + abc) % MOD

    # solution for any number of colors
    # Universal solution
    """
Pre-calculate Transitions
For every pair of valid states (let's call them row1 and row2), check if they can be neighbors. They are compatible if:

row1[0] != row2[0]

row1[1] != row2[1]

row1[2] != row2[2]    
    """    
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        colors = [0, 1, 2]
        
        # 1. Find all valid states for one row
        states = []
        for a in colors:
            for b in colors:
                for c in colors:
                    if a != b and b != c:
                        states.append((a, b, c))
        
        # 2. Initialize DP: Each state has 1 way to exist in the first row
        dp = {state: 1 for state in states}
        
        # 3. Transition row by row
        for _ in range(n - 1):
            new_dp = {state: 0 for state in states}
            for curr_state in states:
                for prev_state in states:
                    # Check vertical compatibility
                    if all(curr_state[i] != prev_state[i] for i in range(3)):
                        new_dp[curr_state] = (new_dp[curr_state] + dp[prev_state]) % MOD
            dp = new_dp
            
        return sum(dp.values()) % MOD    

def main():
    sol = Solution()
    assert sol.numOfWays(1) == 12, 'fails'

    assert sol.numOfWays(2) == 54, 'fails'

    assert sol.numOfWays(3) == 246, 'fails'

    assert sol.numOfWays(4) == 106494, 'fails'

    assert sol.numOfWays(5) == 30228214, 'fails'

if __name__ == '__main__':
   main()