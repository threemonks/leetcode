"""
45. Jump Game II
Medium

4076

177

Add to List

Share
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 10^5
"""
import math
from typing import List

"""
DP

dp[i] := min steps to move to position i
dp[0] = 0

dp[i] = min(d[i-1]+1 if nums[i-1]>= 1,
dp[i-2]+1 if nums[i-2]>=2
)

mistakes:
1. since dp = min (1+dp[j] for all j from 0, ..., i-1, where j+nums[j]>=i), we need to initialize dp to math.inf
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [math.inf] * n

        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], 1 + dp[j])

        return dp[n - 1]


def main():
    sol = Solution()
    assert sol.jump(nums = [2,3,1,1,4]) == 2, 'fails'

    assert sol.jump(nums = [2,3,0,1,4]) == 2, 'fails'


if __name__ == '__main__':
   main()