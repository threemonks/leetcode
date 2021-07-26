"""
464. Can I Win
Medium

In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise return false. Assume both players play optimally.

Example 1:

Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
Example 2:

Input: maxChoosableInteger = 10, desiredTotal = 0
Output: true
Example 3:

Input: maxChoosableInteger = 10, desiredTotal = 1
Output: true


Constraints:

1 <= maxChoosableInteger <= 20
0 <= desiredTotal <= 300

"""


"""
DP Minmax

idea: if A can choose a number and force B to lose, than A is sure to win, otherwise A cannot force B to lose, than A has no sure win, so return False

special case: 
  1. if largest available number exceeding target, than A can just pick it and win
  2. if all available numbers sum together is less than target, than A cannot win, so return False

time O(N*2^N) - DP break down problem to 2^N subproblem with caching, and each subproblem does work with O(N)
"""
from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        @lru_cache(None)
        def helper(total, nums):
            # not enough number to win, so no guarante to win
            if sum(nums) < total:
                return False

            # if A can win by pick the biggest available number, then A can win for sure
            if nums and total <= max(nums):
                return True

            # pick any of nums, if any of its recursive call (B's turn) return True, then we return False
            # i.e., if A cannot choose one number and force B to lose, than A lose
            for i, num in enumerate(nums):
                if not helper(total - num, tuple(nums[:i] + nums[i + 1:])):
                    return True

            # if A has no strategy to force B to lose, than A lose
            return False

        return helper(desiredTotal, tuple(range(1, maxChoosableInteger + 1)))


def main():
    sol = Solution()
    assert sol.canIWin(maxChoosableInteger = 10, desiredTotal = 11) is False, 'fails'

    assert sol.canIWin(maxChoosableInteger = 10, desiredTotal = 0) is True, 'fails'

    assert sol.canIWin(maxChoosableInteger = 10, desiredTotal = 1) is True, 'fails'

if __name__ == '__main__':
   main()