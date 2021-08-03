"""
523. Continuous Subarray Sum
Medium

560

95

Add to List

Share
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.



Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false


Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= sum(nums[i]) <= 2^31 - 1
1 <= k <= 2^31 - 1
"""
from typing import List

"""
Prefix sum Mod + Hash Table

check prefix sum % K

if presum[i]%k exists in map, and current index - map[presum[i]%k]>=2, return True
if not exist in map, add it to map

note:
1. to add dummy value {0: -1} to simplify edge case

time O(N)
"""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        presum = [0 for _ in range(n)]

        presum[0] = nums[0]

        for i in range(1, n):
            presum[i] = presum[i - 1] + nums[i]

        presum = [0] + presum  # add a dummy value 0
        maps = {0: -1}

        for i in range(n):
            presum_remainder = presum[i + 1] % k
            if presum_remainder in maps:
                if i - maps[presum_remainder] >= 2:
                    # print('i=%s presum_remainder=%s maps=%s' % (i, presum_remainder, maps))
                    return True
            else:
                maps[presum_remainder] = i

        return False

def main():
    sol = Solution()
    assert sol.checkSubarraySum(nums = [23,2,4,6,7], k = 6) is True, 'fails'

    assert sol.checkSubarraySum(nums = [23, 2, 6, 4, 7], k = 6) is True, 'fails'

    assert sol.checkSubarraySum(nums = [23, 2, 6, 4, 7], k = 13) is False, 'fails'

    assert sol.checkSubarraySum([1,0], 2) is False, 'fails'

    assert sol.checkSubarraySum([5,0,0,0], 3) is True, 'fails'

if __name__ == '__main__':
   main()