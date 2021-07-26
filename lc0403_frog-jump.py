"""
403. Frog Jump
Hard

1775

137

Add to List

Share
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.



Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.


Constraints:

2 <= stones.length <= 2000
0 <= stones[i] <= 231 - 1
stones[0] == 0
stones is sorted in a strictly increasing order.

"""
from typing import List

"""
DP

dp[i][k] := whether it is possible on i-th position, have jumped here with k units

base

dp[0][1] = True

transition:
dp[i][k] = dp[i-k][k-1] or dp[i-k][k] or dp[i-k][k+1]

notes:
1. stones[i] is the position of i-th stone
2. last jump is k units, next jump could be k-1, k, or k+1 units, this is units, not index count in stones
"""
from functools import lru_cache
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        pos = set(stones)
        seen = set()

        @lru_cache(None)
        def dp(i, k):
            # print('i=%s k=%s' % (i, k))
            if i == stones[-1]:
                # print('i==n-1: True')
                return True
            if i not in pos: # in water
                return False
            if (i, k) in seen: # why do we need this?
                return False
            seen.add((i, k))
            return dp(i+k-1, k-1) or dp(i+k, k) or dp(i+k+1, k+1)

        return dp(stones[0]+1, 1)


def main():
    sol = Solution()
    assert sol.canCross(stones = [0,1,3,5,6,8,12,17]) == True, 'fails'

    assert sol.canCross(stones = [0,1,2,3,4,8,9,11]) == False, 'fails'


if __name__ == '__main__':
   main()
