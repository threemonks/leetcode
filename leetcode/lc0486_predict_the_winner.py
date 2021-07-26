"""
486. Predict the Winner
Medium

Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:

Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return False.


Example 2:

Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.


Constraints:

1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.

"""

from functools import lru_cache
from typing import List

"""
DP
observation
player 1's net score gain for a given step would be the number he picks, minus what player 2 would get from remaining numbers

  dp[0] = max (nums[0] - player 2's max score for nums[1:], nums[-1] - player 2's max score for nums[0:-1])

time O(2^N) - size of recursion tree is 2^N, N is length of nums array
"""


class Solution0:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        @lru_cache(None)
        def helper(i, j):
            nonlocal nums
            if i > j:
                return 0
            if i == j:
                return nums[i]
            else:
                return max(nums[i] - helper(i + 1, j), nums[j] - helper(i, j - 1))

        res = helper(0, len(nums) - 1)

        # print(res)
        return res >= 0


"""
DP bottom up
dp[i][j] := max score with array nums[i:j+1]

dp[i][j]= max (nums[i] - dp[i-1][j], nums[j] - dp[i][j-1])

Final answer is dp[0][n-1], so we iterate i from n to 0, and j from i+1 to n-1, filling upper right half triangle only

"""


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        dp = [[0 for _ in range(n)] for _ in range(n + 1)]  # we only use dp[i][j] for j >= i

        for i in range(n, -1, -1):
            for j in range(i + 1, n):
                dp[i][i] = nums[i]
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
                print('i=%s j=%s dp[i][j]=%s' % (i, j, dp[i][j]))

        # print(dp)
        return dp[0][n - 1] >= 0

def main():
    sol = Solution()
    assert sol.PredictTheWinner([1, 5, 2]) is False, 'fails'

    assert sol.PredictTheWinner([1, 5, 233, 7]) is True, 'fails'

if __name__ == '__main__':
   main()