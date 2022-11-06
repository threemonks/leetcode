"""
2461. Maximum Sum of Distinct Subarrays With Length K
Medium

200

1

Add to List

Share
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.


Constraints:

1 <= k <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""
from typing import List

"""
Sliding window

scan through the list, add each new element into the map

use dict of {number: count} to keep track of what's in the window

if dict size < k, there's duplicate
if dict size == k, there's no duplicate, update cur_sum and global max_sum

removing last (i-k)th item from window, decreasing its count in map, remove from map if count is zero

"""


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur_sum = 0
        max_sum = 0
        maps = dict()

        for i in range(n):
            cur_sum += nums[i]
            if nums[i] in maps:
                maps[nums[i]] += 1
            else:
                maps[nums[i]] = 1
            if len(maps) == k:  # no duplicate
                max_sum = max(max_sum, cur_sum)
            else:  # there's duplicate
                pass

            # drop the one that's going out of window (i-k)th
            if i - k + 1 >= 0:
                cur_sum -= nums[i - k + 1]
                maps[nums[i - k + 1]] -= 1
                if maps[nums[i - k + 1]] == 0:
                    del maps[nums[i - k + 1]]

        return max_sum


def main():
    sol = Solution()
    assert sol.maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3) == 15, 'fails'

    assert sol.maximumSubarraySum(nums = [4,4,4], k = 3) == 0, 'fails'

if __name__ == '__main__':
   main()