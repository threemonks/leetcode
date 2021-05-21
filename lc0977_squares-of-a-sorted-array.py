"""
977. Squares of a Sorted Array
Easy

2422

117

Add to List

Share
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.

"""
from typing import List

"""
Sort

Two Pointers merge sorted array

time O(N)
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums1, nums2 = [], []

        for num in nums:
            if num < 0:
                nums1.append(num * num)
            else:
                nums2.append(num * num)

        nums1 = nums1[::-1]

        ans = []
        # merge nums1 and nums2
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1

        # append remaining of nums1 or nums2
        while i < len(nums1):
            ans.append(nums1[i])
            i += 1

        while j < len(nums2):
            ans.append(nums2[j])
            j += 1

        return ans


def main():
    sol = Solution()
    assert sol.sortedSquares(nums = [-4,-1,0,3,10]) == [0,1,9,16,100], 'fails'

    assert sol.sortedSquares(nums = [-7,-3,2,3,11]) == [4,9,9,49,121], 'fails'

if __name__ == '__main__':
   main()