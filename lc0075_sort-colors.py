"""
75. Sort Colors
Medium

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.


Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?

"""
import collections
from typing import List

"""
Counting Sort

count frequency of each unique values
for values in unique values from smallest to largest:
    append this value for output for the number of times we counted

Note:
    this is unstable, means same value in output might not preserve their original order in input

time O(n+k)

mistakes:
1. since counting sort output will try to output all numbers between min and max, we need to check if the given number is actually in the array
"""


class Solution0:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        counter = collections.Counter(nums)
        counter = dict(counter)

        nummin, nummax = min(nums), max(nums)
        num = nummin
        i = 0
        while i < n and num <= nummax:
            while i < n and num in counter and counter[num] > 0:
                nums[i] = num
                i += 1
                counter[num] -= 1
            num += 1  # proceed to next unique value/color


"""

Three pointers / Dutch National Flag problem

ideas:
use three pointers, p0: right most of 0's, p2: left most of 2's, curr the current number being considered
1. init p0 = 0, p2 = n-1
2. iterate curr from 0 to n-1,
    if nums[curr] == 0, swap nums[curr] with nums[p0], move both pointers to right
    if nums[curr] == 2, swap nums[curr] and nums[p2], move pointer p2 to left
    if nums[curr] == 1, move pointer curr to right

time O(n+k)
space O(1)

"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        # for all idx < p0: nums[idx<p0] = 0
        # curr is an index of element under consideration
        # for all idx > p2: nums[idx>p2] = 2
        p0, curr, p2 = 0, 0, n - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:  # nums[curr] == 1:
                curr += 1


def main():
    sol = Solution()
    sol.sortColors(nums = [2,0,2,1,1,0])

    sol.sortColors(nums = [2,0,1])

    sol.sortColors(nums = [0])

    sol.sortColors(nums = [1])


if __name__ == '__main__':
   main()