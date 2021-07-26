"""
16. 3Sum Closest
Medium

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

"""
import math
from typing import List


"""

Two Pointers + Binary Search

observation:
brutal force would be O(N^3), so we can sort it using O(Nlog(N)) to speed up inner loop/twosum without increasing overall time complexity

time O(N^2)
space O(N)

"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)

        diff = math.inf
        ans = sum(nums[:3])
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicates
                continue
            # print('i=%s nums[i]=%s' % (i, nums[i]))
            l, r = i + 1, n - 1
            while l < r:
                sums = nums[i] + nums[l] + nums[r]
                # print('i=%s l=%s r=%s diff=%s sums=%s' % (i, l, r, diff, sums))
                if target - sums < 0:
                    r -= 1
                elif target - sums > 0:
                    l += 1
                else:  # nums[l]+nums[r] - rem <= 0
                    return sums
                if abs(target - sums) < abs(target - ans):
                    ans = sums

        return ans


def main():
    sol = Solution()

    assert sol.threeSumClosest(nums = [-1,2,1,-4], target = 1) == 2, 'fails'

if __name__ == '__main__':
   main()