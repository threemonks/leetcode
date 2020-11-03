"""
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400

"""
from typing import List

"""
use one variable (one array can be simplified into one variable since at step i we only depends on i-1 and i-2)
dp[i] := max money after visiting house i (whether rob or not)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        n = len(nums)
        dp = [0 for _ in range(n)]

        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]


"""
use two array (can be simplified to two variable because the transition to i only requires i-1 (and i-2)
dp0[i] := max money after not robbing i-th house
dp1[i] := max money after robbing i-th house
"""


class Solution1:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp0 = [0 for _ in range(n)]  # max money after not robbing i-th
        dp1 = [0 for _ in range(n)]  # max money after robbing i-th
        dp0[0] = 0
        dp1[0] = nums[0]

        for i in range(1, n):
            dp0[i] = max(dp1[i - 1], dp0[i - 1])
            dp1[i] = max(dp1[i - 2], dp0[i - 1]) + nums[i]

        return max(dp0[n - 1], dp1[n - 1])


"""
use two array (can be simplified to two variable because the transition to i only requires i-1 (and i-2)
dp0[i] := max money after not robbing i-th house
dp1[i] := max money after robbing i-th house
transition equation:
dp0[i] = max(dp1[i-1], dp0[i-1]) # i-th not robbing is max of i-1 th not robbing and robbing, because with i-th not robbing, i-1th could be either robbing or not robbing
dp1[i] = dp0[i-1] + nums[i] # i-th robbing is i-1 th not robbing plus i-th item value, since i-th robbed, i-1 th must be not robbed, cannot be robbed
"""


class Solution2:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp0 = [0 for _ in range(n)]  # max money after not robbing i-th
        dp1 = [0 for _ in range(n)]  # max money after robbing i-th
        dp0[0] = 0
        dp1[0] = nums[0]

        for i in range(1, n):
            dp0[i] = max(dp1[i - 1], dp0[i - 1])
            dp1[i] = dp0[i - 1] + nums[i]

        return max(dp0[n - 1], dp1[n - 1])


"""
similar to Solution2 but using two variable dp0, dp1, instead of array dp0[], dp1[], since both dp0 and dp1 only depends on value of immediate preceeding dp0,1
dp0 := max money after not robbing i-th house
dp1 := max money after robbing i-th house
transition equation:
dp0[i] = max(dp1[i-1], dp0[i-1]) # i-th not robbing is max of i-1 th not robbing and robbing, because with i-th not robbing, i-1th could be either robbing or not robbing
dp1[i] = dp0[i-1] + nums[i] # i-th robbing is i-1 th not robbing plus i-th item value, since i-th robbed, i-1 th must be not robbed, cannot be robbed
"""


class Solution3:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp0 = 0
        dp1 = nums[0]

        for i in range(1, n):
            # make sure dp0 and dp1 are depending on dp0 and dp1 from previous loop
            dp0, dp1 = max(dp1, dp0), dp0 + nums[i]

        return max(dp0, dp1)


class Solution4:
    def rob(self, nums: List[int]) -> int:
        """
        dp0 := max profit after not robbing i-th house
        dp1 := max profit after robbing i-th house

        transition:
        i-1-th dp0  dp1     dp0   dp1

                |  /         |(+n)
        i-th   dp0          dp1
        """
        if not nums:
            return 0
        dp0, dp1 = 0, 0
        for n in nums:
            dp0, dp1 = max(dp0, dp1), n + dp0

        return max(dp0, dp1)

def main():
    sol = Solution4()
    nums = [1,2,3,1]
    assert sol.rob(nums) == 4, 'fails'

    nums = [2,7,9,3,1]
    assert sol.rob(nums) == 12, 'fails'

    nums = [2,1,1,2]
    assert sol.rob(nums) == 4, 'fails'

if __name__ == '__main__':
   main()