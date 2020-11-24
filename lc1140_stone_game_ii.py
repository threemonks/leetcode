"""
1140. Stone Game II
Medium

620

148

Add to List

Share
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.



Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger.
Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104


Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 104

"""
from functools import lru_cache
from typing import List

"""
observation

M = 1, [1, 2], X = 2
M = 2, [1, 4], X = 3
M = 3, [1, 6], X = 1
M = 3, [1, 6], X = ...

maximize: dp[state]
             ||
minimize ( maximize: dp[state'])


dp[i,M] := after first i-th piles used, how many stones Alice can have
    dp[i,] = sum(piles[i...]) - dp[i+X, max(M,X)] # effective, stones gained by Alice for taking first X remaining piles, is sum of all remaining stones, minus whatever bob can gain after Alice's turn, which is dp[i+X, max(M, X)]

"""


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # precalculate suffix sum to make it more efficient
        n = len(piles)
        sufsum = [0] * (n + 1)
        sufsum[n] = 0
        for i in range(len(piles) - 1, -1, -1):
            sufsum[i] = sufsum[i + 1] + piles[i]

        @lru_cache(None)
        def solve(i, M):
            """
            i : starting index of piles remaining
            M : parameter on how many piles current player can take
            """
            nonlocal piles, sufsum
            # print('i=%s M=%s' % (i, M))
            if i == len(piles) - 1:  # if no stones left
                return piles[i]
            elif i > len(piles) - 1:
                return 0

            return max([sufsum[i] - solve(i + X, max(M, X)) for X in range(1, 2 * M + 1)])

        return solve(0, 1)

def main():
    sol = Solution()
    assert sol.stoneGameII([2,7,9,4,4]) == 10, 'fails'

    assert sol.stoneGameII([1,2,3,4,5,100]) == 104, 'fails'

if __name__ == '__main__':
   main()