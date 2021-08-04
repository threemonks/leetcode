"""
54. Find Minimum in Rotated Sorted Array II
Hard

1784

288

Add to List

Share
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.



Example 1:

Input: nums = [1,3,5]
Output: 1
Example 2:

Input: nums = [2,2,2,0,1]
Output: 0


Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.


Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""
from typing import List
"""
Binary Search

if nums[mi] < nums[hi]: hi = mi
elif nums[mi] > nums[hi] : lo = mi+1
else: hi -= 1  # don't know left or right, move 1 step at a time

time complexity average O(log(N)), worst case O(N)

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n-1
        while lo < hi:
            mi = lo+(hi-lo)//2
            print('lo=%s mi=%s hi=%s' % (lo, mi, hi))
            if nums[mi] < nums[hi]: # use hi = mi-1 would fail test case [3, 1, 3]
                hi = mi
            elif nums[mi] > nums[hi]: # min is to right of mid
                lo = mi+1
            else: # nums[mi] == nums[hi]
                hi -= 1

        return nums[lo]

def main():
    sol = Solution()
    assert sol.findMin(nums = [1,3,5]) == 1, 'fails'

    assert sol.findMin(nums = [2,2,2,0,1]) == 0, 'fails'

if __name__ == '__main__':
   main()