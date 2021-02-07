"""
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

1752. Check if Array Is Sorted and Rotated
Easy

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.



Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
Example 4:

Input: nums = [1,1,1]
Output: true
Explanation: [1,1,1] is the original sorted array.
You can rotate any number of positions to make nums.
Example 5:

Input: nums = [2,1]
Output: true
Explanation: [1,2] is the original sorted array.
You can rotate the array by x = 5 positions to begin on the element of value 2: [2,1].


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
from typing import List

"""
brutal force
1. sort nums, then compare with nums, and nums[::-1], if equal, return true
2. shift nums by 1: nums = nums[1:] + nums[:1], repeat above step
3. repeat step 2 from 1 to n
4. if not returned yet, return False (no way to match)

"""


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0 or n == 1: return True

        nums_sorted = sorted(nums)
        for i in range(n + 1):
            nums1 = nums[i:] + nums[:i]
            if nums1 == nums_sorted or nums1 == nums_sorted[::-1]:
                return True

        return False


def main():
    sol = Solution()
    assert sol.check([3,4,5,1,2]) is True, 'fails'

    assert sol.check([2,1,3,4]) is False, 'fails'

    assert sol.check([1,2,3]) is True, 'fails'

    assert sol.check([1,1,1]) is True, 'fails'

    assert sol.check([2,1]) is True, 'fails'


if __name__ == '__main__':
   main()