"""
81. Search in Rotated Sorted Array II
Medium

2045

576

Add to List

Share
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.



Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 10^4
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 10^4


Follow up: This problem is the same as Search in Rotated Sorted Array, where nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""
from typing import List

"""
Binary Search

One pass

"""


class Solution0:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n <= 1:
            return target in nums

        left, right = 0, n - 1
        while left <= right:  # we use left close, right close, and left <= right as condition, then we always move left to mid+1, or right to mid-1
            mid = left + (right - left) // 2
            # print('left=%s right=%s mid=%s' % (left, right, mid))
            if nums[mid] == target:
                return True
            elif nums[left] == nums[mid] and nums[mid] == nums[right]:
                # if both end are the same, we don't know which side is rotated, which side is not
                # so we shrink both to check further
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                # left part is sorted, check if target is in left
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                # right part is sorted, check if target is in right part
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


"""
Binary Search

different way to check which part to check target

"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n <= 1:
            return target in nums

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            # print('left=%s right=%s mid=%s' % (left, right, mid))
            if nums[mid] == target:
                return True
            elif nums[left] == nums[mid]:  # duplicate number left, not target, exclude it
                left += 1
            elif nums[left] <= target < nums[mid]:  # target in left
                right = mid - 1
            elif nums[mid] < target <= nums[right]:  # target in right
                left = mid + 1
            elif nums[left] < nums[mid]:  # target not in left, shrink left
                left = mid + 1
            else:
                right = mid - 1

        return False

def main():
    sol = Solution()
    assert sol.search(nums = [2,5,6,0,0,1,2], target = 0) is True, 'fails'

    assert sol.search(nums = [2,5,6,0,0,1,2], target = 3) is False, 'fails'


if __name__ == '__main__':
   main()