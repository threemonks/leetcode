"""
283. Move Zeroes
Easy

5431

170

Add to List

Share
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?

"""
from typing import List

"""
Two Pointers

i iterate entire array from n-1 to 0, j points at first non-zero from right
if nums[i] is zero, insert nums[i] to right of nums[j], and move nums[i+1:j+1] one step to left

time O(N^2)
space O(1)
"""


class Solution0:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        i, j = n - 1, n - 1
        for i in range(n - 1, -1, -1):
            if nums[i] == 0:
                # insert nums[i] to right of nums[j]
                # and shift all elements betwee i+1...j to left by one
                tmp = nums[i]
                for k in range(i + 1, j + 1):
                    nums[k - 1] = nums[k]
                nums[j] = tmp
                j -= 1


"""
Two Pointers

pointer j counts index of non-zero element found so far
pointer i iterate the array, from 0 to n-1, if nums[i] is non-zero, replace nums[j] with nums[i], then set nums[i] to zero

once the above loop is done, we need to set all elements from j to n-1 to zero (these are all the zeros to right)

time O(N)
space O(1)

mistakes:
1. nums[i] could be negative
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n == 1:
            return

        j = 0  # index after last non-zero elements stored
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]  # this would be no op if j==i (all beginning non-zero elements)
                j += 1

        # set all elements from j to n-1 to zero
        for i in range(j, n):
            nums[i] = 0