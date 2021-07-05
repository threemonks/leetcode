"""
41. First Missing Positive
Hard

6235

1050

Add to List

Share
Given an unsorted integer array nums, find the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1


Constraints:

1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""
from typing import List

"""
Array

from 1 to n, check each of i if it is in set(nums)
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)
        for i in range(1, n + 1):
            if i not in nums:
                return i

        return i + 1  # if all numbers in [1, n+1] presents, missing n+1

def main():
    sol = Solution()
    assert sol.firstMissingPositive(nums = [1,2,0]) == 3, 'fails'

    assert sol.firstMissingPositive(nums = [3,4,-1,1]) == 2, 'fails'

    assert sol.firstMissingPositive(nums = [7,8,9,11,12]) == 1, 'fails'


if __name__ == '__main__':
   main()