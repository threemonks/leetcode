"""
410. Split Array Largest Sum
Hard

Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.



Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.length)

"""
from functools import lru_cache
from typing import List

"""
Binary Search / Greedy

Dividing into at most m groups, so the largest sum among the m subarrays would be at least max(nums), since that single element has to be in some group, even if it is in single element group, it will result in largest sum be max(nums). On the other end, the maximum possible value would be sum(nums). So we would do binary search between max(nums) and sum(nums), and find the maximum possible value k that would be valid (such that divide into at most group m with largest sum among the m subarrays being k)

To check if a given split is valid, we keep adding element from nums into sum, if it is greater than mid, that means we need to start a new subarray, keep counting subarray, when finishing nums, if number of subarray is equal or less than m, then it is a valid split.

time O(Nlog(sumofarray))
mistakes:
1. binary search, left close right open, if target is invalid (cannot achieve with m subarray splits), then we need to bigger target (larger largest sum of subarray)
2. to check if a target is valid for m splits, compare partial sum with target, and for each sum, we update count if sum > target, and after each count update, check if count>m
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        maxx = max(nums)
        sums = sum(nums)

        if m == 1: return sums

        def valid(target):
            nonlocal nums, m
            count = 1  # subarray count
            cursum = 0  # sum so far
            for num in nums:
                cursum = cursum + num
                if cursum > target:
                    cursum = num  # start a new partial sum
                    count += 1  # increase subarray count
                    if count > m:
                        return False

            return True

        # print('maxx=%s sums=%s' % (maxx, sums))
        left, right = maxx, sums
        while left < right:
            mid = left + (right - left) // 2
            # print('left=%s right=%s mid=%s' % (left, right, mid))
            if valid(mid):
                right = mid
            else:  # no longer valid, we need bigger largest sum for subarray to make it valid
                left = mid + 1

        # when exit loop, left==right
        return left


def main():
    sol = Solution()
    assert sol.splitArray(nums = [7,2,5,10,8], m = 2) == 18, 'fails'

    assert sol.splitArray(nums = [1,2,3,4,5], m = 2) == 9, 'fails'

    assert sol.splitArray(nums = [1,4,4], m = 3) == 4, 'fails'


if __name__ == '__main__':
   main()