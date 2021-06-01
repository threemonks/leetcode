"""
1590. Make Sum Divisible by P
Medium

543

24

Add to List

Share
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.



Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
Example 4:

Input: nums = [1,2,3], p = 7
Output: -1
Explanation: There is no way to remove a subarray in order to get a sum divisible by 7.
Example 5:

Input: nums = [1000000000,1000000000,1000000000], p = 3
Output: 0


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= p <= 10^9
"""
import math
from typing import List

"""
Hash Table + Prefix sum

For remaining arry after removing subarray to be divisible by p, then the remainder of total sum divided by p should be same as remainder of sum of removed subarray divided by p.

let total_remainder = sum(nums) % p, we want to remove min length subarray whose sum(subarray) %p == total_remainder
if we calculate prefix sum of nums, then calculate remainder of the presum % p, then we are looking for two element in remainder of presum that has difference of total_remainder, i.e., 

iterate through remainder of presum % p, for current index i, with remainder of presum % p as cur_remainder, we look for last found cur_remainder - total_remainder, elements within this subarray can be removed for remaining array to have sum divisible by p.

"""


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total_remainder = sum(nums) % p
        if total_remainder == 0:  # no need to remove anything
            return 0

        presum = 0
        seen = {0: -1}  # dummy presum mod sentinel index
        remove_len = math.inf
        for i in range(n):
            presum += nums[i]
            cur_remainder = presum % p
            prev_remainder = cur_remainder - total_remainder if cur_remainder - total_remainder >= 0 else (
                        cur_remainder - total_remainder + p)
            if prev_remainder in seen:  # remove subarray i-seen[prev_remainder] would be valid
                remove_len = min(remove_len, i - seen[prev_remainder])
            seen[cur_remainder] = i

        if remove_len == n:  # cannot remove entire array
            return -1
        else:
            return remove_len

def main():
    sol = Solution()

    assert sol.minSubarray(nums = [3,1,4,2], p = 6) == 1, 'fails'

    assert sol.minSubarray(nums = [6,3,5,2], p = 9) == 2, 'fails'

    assert sol.minSubarray(nums = [1,2,3], p = 3) == 0, 'fails'

    assert sol.minSubarray(nums = [1, 2, 3], p = 7) == -1, 'fails'

if __name__ == '__main__':
   main()