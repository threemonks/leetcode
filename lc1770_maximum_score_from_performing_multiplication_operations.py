"""
1770. Maximum Score from Performing Multiplication Operations
Medium

https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

"""
from typing import List

from functools import lru_cache

"""

DP

Use three (i, j, k) pointers to keep track of the current position
from the front of nums, from the back of nums, and on mult.

This can be simplified to two pointers because j = nums.length - 1 - k + i.

At each iteration there's two choices, add mult[k]*nums[i] to the total and
move the i pointer forward one step, or add mult[k]*nums[j] to the total and do not move pointer i.

the max of these two give max score for current step

observation:

since we can only do m operations at most, so only nums[:m] and nums[len(nums)-m:] would be impacting result, so we can reduce nums size directly.

"""


class Solution0:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # since we are only allowed at most m operations, so we would need at most m numbers from front and back of nums
        # but this does not seem to improve the total run time, maybe there's no test case with hugh nums size
        m = len(multipliers)
        # nums = nums[:m] + nums[len(nums)-m:]
        n = len(nums)

        @lru_cache(2000)  # can limit to 2000 as m < 10^3, slightly improves runtime
        def helper(i, k):
            if k == m:
                return 0

            return max(
                nums[i] * multipliers[k] + helper(i + 1, k + 1),
                nums[n - 1 - k + i] * multipliers[k] + helper(i, k + 1)
            )

        res = helper(0, 0)

        helper.cache_clear()  # this slightly improves performance

        return res


"""
DP bottom up
"""


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        # since we are only allowed at most m operations, so we would need at most m numbers from front and back of nums
        m = len(multipliers)
        nums = nums[:m + 1] + nums[len(nums) - m:]
        n = len(nums)

        dp = [[0 for _ in range(m + 1)] for _ in
              range(n + 1)]  # dp size (n+1)*(m+1) as dp[i][k] depends on dp[i+1][k+1]

        for k in range(m - 1, -1, -1):
            for i in range(k, -1, -1):  # i < k as we cannot take more numbers than # of operations performed
                dp[i][k] = max(
                    nums[i] * multipliers[k] + dp[i + 1][k + 1],
                    nums[n - 1 - k + i] * multipliers[k] + dp[i][k + 1]
                )

        res = dp[0][0]
        del dp  # does not seem to improve performance
        return res


def main():
    sol = Solution()
    assert sol.maximumScore([1,2,3], [3,2,1]) == 14, 'fails'

    assert sol.maximumScore([-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]) == 102, 'fails'


if __name__ == '__main__':
   main()