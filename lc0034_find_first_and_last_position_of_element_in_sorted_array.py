"""
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

"""
import bisect
from typing import List


class Solution0:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == right:  # target not in nums
            return -1, -1
        else:
            return left, right - 1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return -1, -1
        elif n == 1:
            if nums[0] == target:
                return 0, 0
            else:
                return -1, -1

        lo, hi = 0, n  # left close, right open [)
        mi = lo
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if nums[mi] == target:
                break
            elif nums[mi] > target:
                hi = mi
            else:
                lo = mi + 1

        # when exit, either nums[mi] == target, or lo>=hi, and target should be inserted at nums[lo] location
        if nums[mi] == target:
            left = mi
            while left >= 0 and nums[left] == target:  # find left most position of target value
                left -= 1
            right = mi
            while right < n and nums[right] == target:  # find right most position of target value
                right += 1
            return left + 1, right - 1
        else:  # not found
            return -1, -1


def main():
    sol = Solution()
    assert sol.searchRange([5,7,7,8,8,10], 8) == (3, 4), 'fails'

    assert sol.searchRange([5,7,7,8,8,10], 6) == (-1, -1), 'fails'

    assert sol.searchRange([], 0) == (-1, -1), 'fails'

    assert sol.searchRange([1], 1) == (0, 0), 'fails'

if __name__ == '__main__':
   main()