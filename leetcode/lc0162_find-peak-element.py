"""
162. Find Peak Element
Medium

2773

2643

Add to List

Share
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.



Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


Constraints:

1 <= nums.length <= 1000
-2^31 <= nums[i] <= 2^31 - 1
nums[i] != nums[i + 1] for all valid i.


Follow up: Could you implement a solution with logarithmic complexity?
"""
from math import inf
from typing import List

"""
Binary Search

add dummy head and tail -inf, then binary search
[1, 2, 3, 1]
 1   2 3    1
if nums[m-1] < nums[m] > nums[m+1] => return m
else if nums[m-1] > nums[m], search [l, m-1]
else nums[m] < nums[m+1], search [m+1, r]

mistakes:
1. m = l+(r-l)//2
2. dummy head needs to be removed return m-1
3. edge case single element len(nums)=1
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        nums = [-inf] + nums + [-inf]
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l) // 2
            # print('l=%s r=%s m=%s' % (l, r, m))
            if nums[m - 1] < nums[m] and nums[m] > nums[m + 1]:
                return m - 1
            elif m - 1 >= 1 and nums[m - 1] > nums[m]:  # search left half
                r = m - 1
            else:  # nums[m] < nums[m+1] # search right half - but what about boundary case?
                l = m + 1

        return l - 1  # offset dummy head


def main():
    sol = Solution()
    assert sol.findPeakElement([1,2,3,1]) == 2, 'fails'

    assert sol.findPeakElement(nums = [1,2,1,3,5,6,4]) == 5, 'fails'

if __name__ == '__main__':
   main()