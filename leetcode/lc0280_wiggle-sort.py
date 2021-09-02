"""
280. Wiggle Sort
Medium

788

69

Add to List

Share
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

You may assume the input array always has a valid answer.



Example 1:

Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.
Example 2:

Input: nums = [6,6,5,6,3,8]
Output: [6,6,5,6,3,8]


Constraints:

1 <= nums.length <= 5 * 10^4
0 <= nums[i] <= 10^4
It is guaranteed that there will be an answer for the given input nums.


Follow up: Could you do it without sorting the array?
"""
from typing import List

"""
Sort

sort and swap every adjacent pair

time O(NlogN)
"""


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)

        for i in range(1, n - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]


"""
Array / One-pass

if nums[i-1] <= nums[i], then we expect nums[i] >= nums[i+1], and if nums[i] < nums[i+1], it is always safe to swap nums[i] and nums[i+1]
because nums[i-1]<=nums[i] and nums[i] < nums[i+1] ensures nums[i-1] < nums[i+1]

similarly, if nums[i-1] >= nums[i], then we expect nums[i]<=nums[i+1], if we find nums[i] > nums[i+1] instead, then it is safe to swap nums[i] and nums[i+1], because nums[i-1] >= nums[i] and nums[i] > nums[i+1] ensurces nums[i-1] > nums[i+1].

time O(N)
"""


class Solution1:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        asc = True
        n = len(nums)

        for i in range(0, n - 1):
            if asc:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            asc = not asc
