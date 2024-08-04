"""
33. Search in Rotated Sorted Array
Medium

7307

642

Add to List

Share
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104

"""
from typing import List

"""
Binary Search

1. use binary search to find the rotation index (smallest item) index pivot, which divides the array into two parts, both are sorted in itself
2. compare target with nums[0] and nums[pivot] to see which part the target should be in
    if nums[pivot] <= target <= nums[n-1]: target is on right side between pivot and n-1
    else target is on left side between 0 and pivot-1
3. in that part, use binary search to find the target

Observation: since the array is rotated at one pivot once, one part of the array (to one side of the pivot index) is not rotated.


time O(log(N))
"""


class Solution0:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n == 1:
            return 0 if nums[0] == target else -1

        lo, hi = 0, n - 1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if nums[mi] > nums[hi]:
                # this is not correct order, so smallest value is between mi and hi
                lo = mi + 1
            else:  # nums[pivot] > nums[lo] since all nums unique
                hi = mi

        # when search finishes, lo is the smallest value index
        pivot = lo
        # print('lo=%s hi=%s pivot=%s' % (lo, hi, pivot))

        # now we found pivot, we know nums[0...pivot] and nums[pivot...n] are both sorted
        # we search in [lo, hi) (left close, right open)
        if nums[pivot] <= target <= nums[n - 1]:  # if target is in right part, then search in right part
            lo, hi = pivot, n
        else:  # target >= nums[pivot], then search in left part
            lo, hi = 0, pivot

        # print('lo=%s hi=%s' % (lo, hi))
        while lo < hi:
            mi = lo + (hi - lo) // 2
            # print('lo=%s hi=%s mi=%s' % (lo, hi, mi))
            if nums[mi] == target:
                return mi
            elif nums[mi] > target:
                hi = mi
            else:
                lo = mi + 1

        return -1


"""
Binary Search

One pass

idea is to add some additional check during the normal binary search in order to better narrow down the scope of the search

revised binary search:
mid = start + (end - start)//2

if nums[mid] == target: return mid
elif nums[start] < nums[mid]: # first half is ordered
    # if target in first half
    if nums[start]<=target<=nums[mid]:
        # go left
        end = mid-1
    else:
        # go right
        start = mid+1
elif nums[start] > nums[mid]: # second half is ordered
    # if target in second half
    if nums[mid] <= target <= nums[end]:
        # go right
        start = mid+1
    else:
        # go left
        end = mid-1

time O(log(N))
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n == 1:
            return 0 if nums[0] == target else -1

        left, right = 0, n - 1
        while left <= right:
            mi = left + (right - left) // 2
            if nums[mi] == target:
                return mi
            elif nums[left] > nums[mi]:  # second half is sorted
                if nums[mi] < target <= nums[right]:
                    # target in second half
                    # move to right
                    left = mi + 1
                else:
                    # move to left
                    right = mi - 1
            else:  # first half is sorted
                if nums[left] < target <= nums[mi]:
                    # target in first half
                    # move to left
                    right = mi - 1
                else:
                    # move to right
                    left = mi + 1

        return -1

def main():
    sol = Solution()
    assert sol.search(nums = [4,5,6,7,0,1,2], target = 0) == 4, 'fails'

    assert sol.search(nums = [4,5,6,7,0,1,2], target = 3) == -1, 'fails'

    assert sol.search(nums = [1], target = 0) == -1, 'fails'

    assert sol.search([5,1,3], 1) == 1, 'fails'


if __name__ == '__main__':
   main()