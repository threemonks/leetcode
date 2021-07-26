"""
53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647


Constraints:

1 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""
from typing import List
import math

"""
DP (dynamic programming) using Kadane's algorithm

    cur_sum[i] = max(nums[i], nums[i]+cur_sum[i-1])
                 ^                   ^
        don't use cur_sum[i-1]     use cur_sum[i-1]

time O(N)
space O(1)

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -math.inf
        cur_sum = -math.inf
        for num in nums:
            cur_sum = max(num, cur_sum + num)
            best_sum = max(best_sum, cur_sum)

        return best_sum

def main():
    sol = Solution()
    assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6, 'fails'

    assert sol.maxSubArray([1]) == 1, 'fails'

    assert sol.maxSubArray([0]) == 0, 'fails'

    assert sol.maxSubArray([-1]) == -1, 'fails'

    assert sol.maxSubArray([-2147483647]) == -2147483647, 'fails'


if __name__ == '__main__':
   main()