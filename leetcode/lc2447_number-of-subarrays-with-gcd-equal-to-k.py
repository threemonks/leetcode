"""
2447. Number of Subarrays With GCD Equal to K
Medium

81

31

Add to List

Share
Given an integer array nums and an integer k, return the number of subarrays of nums where the greatest common divisor of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The greatest common divisor of an array is the largest integer that evenly divides all the array elements.



Example 1:

Input: nums = [9,3,1,2,6,3], k = 3
Output: 4
Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
Example 2:

Input: nums = [4], k = 7
Output: 0
Explanation: There are no subarrays of nums where 7 is the greatest common divisor of all the subarray's elements.


Constraints:

1 <= nums.length <= 1000
1 <= nums[i], k <= 10^9

"""
import math
from typing import List

"""
double loop with optimization

with some optimization
1. gcd(gcd([a, b, c, d]) = gcd(gcd([a, b, c]), d)
2. if curr_gcd < k or curr_gcd % k != 0, no need to proceed further
"""


class Solution:

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ans = 0

        for i in range(n):
            if nums[i] < k or nums[i] % k != 0:
                continue
            cur_gcd = 0
            for j in range(i, n):
                cur_gcd = math.gcd(cur_gcd, nums[j])
                if cur_gcd == k:
                    ans += 1
                if cur_gcd < k or cur_gcd % k != 0:
                    break

        return ans


def main():
    sol = Solution()
    assert sol.subarrayGCD([9,3,1,2,6,3], 3) == 4, 'fails'

    assert sol.subarrayGCD([4], 7) == 0, 'fails'

if __name__ == '__main__':
   main()