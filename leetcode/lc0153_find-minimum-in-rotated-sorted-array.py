"""
153. Find Minimum in Rotated Sorted Array
Medium

4025

320

Add to List

Share
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.


Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

"""
from typing import List

"""
Binary Search

rotated means one side is not in correct order, i.e., 
without ratation
lo < mi < hi
nums[lo] < nums[mi] < nums[hi]
after rotation
we might have nums[mi] < nums[lo] or nums[mi] > nums[hi]
if nums[mi] > nums[hi], that means pivot/min is to right of mi
if nums[mi] <= nums[hi], that means pivot/min is to left of mi

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n-1
        while lo < hi:
            mi = lo + (hi-lo)//2
            # print('lo=%s mi=%s hi=%s' % (lo, mi, hi))
            if nums[mi] > nums[hi]: # pivot/min is to right
                lo = mi + 1
            else:
                hi = mi

        return nums[lo]


def main():
    sol = Solution()
    assert sol.findMin(nums = [3,4,5,1,2]) == 1, 'fails'

    assert sol.findMin(nums = [4,5,6,7,0,1,2]) == 0, 'fails'

    assert sol.findMin(nums = [11,13,15,17]) == 11, 'fails'

if __name__ == '__main__':
   main()