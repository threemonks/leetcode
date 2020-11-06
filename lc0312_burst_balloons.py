"""
312. Burst Balloons
Hard

2842

73

Add to List

Share
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

"""
from functools import lru_cache
from typing import List

"""
idea:
    if we consider bursting a balloon i, and ramaining balloons [0, i-1] and [i+1, n), then maxCoins from left subarray and right subarray depend on each other as they are now adjacent
    so we do reverse thinking, if we divide the array into two subarrays using the last balloons to pop, i, then its coin is maxCoins(0, i) + nums[0]*nums[i]*nums[n+1]+maxCoins(i+1,n+1) <- recursive

    dp:
        dp[i][j]: coins obtained from bursting all the balloons between index i and j (not including i or j)
        dp[i][j] = max(nums[i]*nums[k]*nums[j] + dp[i][k]+dp[k][j]) for k in [i+1,j-1] (k is any number between i and j, but excluding i, and j)
        if k is the last balloon burst between i and j, the coins from bursting k is nums[i]*nums[k]*nums[j], and to calculate dp[i][j], we also need to add coins from bursting balloons from i to k, which is dp[i][k] and from k to j, which is dp[k][j]
    note:
        1. we need to pad nums with index nums[-1]=1 and nums[n]=1 to make boundary case easier
        2. pop all 0s first as they don't add value
        3. base case is i+1==j, as there's no balloon to pop
"""


class Solution:
    def maxCoins(self, input_nums: List[int]) -> int:
        # edge case
        if not input_nums:
            return 0
        elif len(input_nums) == 1:
            return input_nums[0]

        # pop all zeros and padd with imagnary boundary value 1 to ease boundary handling (no impact on result)
        nums = [v for v in input_nums if v > 0]
        nums = [1] + nums + [1]

        n = len(nums)

        @lru_cache(None)
        def dp(i, j):
            nonlocal nums
            if i + 1 == j:
                return 0
            return max([(nums[i] * nums[k] * nums[j] + dp(i, k) + dp(k, j)) for k in range(i + 1, j)])

        return dp(0, n - 1)

def main():
    sol = Solution()
    assert sol.maxCoins([3,1,5,8]) == 167, 'fails'

if __name__ == '__main__':
   main()