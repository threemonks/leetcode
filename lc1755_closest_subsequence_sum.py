"""
https://leetcode.com/problems/closest-subsequence-sum/

1755. Closest Subsequence Sum
Hard

You are given an integer array nums and an integer goal.

You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

Return the minimum possible value of abs(sum - goal).

Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.

Example 1:

Input: nums = [5,-7,3,5], goal = 6
Output: 0
Explanation: Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.
Example 2:

Input: nums = [7,-9,15,-2], goal = -5
Output: 1
Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.
Example 3:

Input: nums = [1,2,3], goal = -7
Output: 7

Constraints:

1 <= nums.length <= 40
-107 <= nums[i] <= 107
-109 <= goal <= 109

"""
import bisect
import math
from typing import List

"""
observation, if goal falls beyong max sum of all elements in sum, or below min sum of all elements in sum, then the best we can have is maxsum or minsum

otherwise, calculate all possible subsets in nums (nums.length < 40), calculate the sum for the subsets, sort these sums, use binary search to search the one that is closest to goal

all possible subsets have complexity of 2^40 ~ 10^9, which will TLE. So we would try to split it into two half, calculate sum of all subsets of first half array, use goal to minus this sum, search this diff in the sum of all subsets of second half array

"""


class Solution0:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        maxsum = sum([num for num in nums if num > 0])
        minsum = sum([num for num in nums if num < 0])
        if goal > maxsum: return goal - maxsum
        if goal < minsum: return minsum - goal

        res = [[]]

        def dfs(numbers, subset, res):
            res.append(subset)
            for i in range(len(numbers)):
                dfs(numbers[i + 1:], subset + [numbers[i]], res)

        n2 = n // 2  # half of n
        nums1 = []
        dfs(nums[:n2], [], nums1)
        nums2 = []
        dfs(nums[n2:], [], nums2)

        sums1 = [sum(s) for s in nums1]
        sums2 = [sum(s) for s in nums2]
        sums2 = sorted(sums2)

        remain1 = [goal - s for s in sums1]

        # now search for closest possible value to sums1-gobal
        ans = math.inf
        for r1 in remain1:
            l = bisect.bisect_left(sums2, r1)
            if l < len(sums2):
                ans = min(ans, abs(r1 - sums2[l]))
            if l > 0:
                ans = min(ans, abs(r1 - sums2[l - 1]))

        return ans


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        maxsum = sum([num for num in nums if num > 0])
        minsum = sum([num for num in nums if num < 0])
        if goal > maxsum: return goal - maxsum
        if goal < minsum: return minsum - goal

        sums = set([0])
        for i in range(len(nums)):
            t = list(sums)
            for v in t:
                sums.add(v + nums[i])

        sums = sorted(list(sums))

        l = bisect.bisect_left(sums, goal)

        ans = math.inf
        if l < len(sums):
            ans = min(ans, abs(goal - sums[l]))
        if l > 0:
            ans = min(ans, abs(goal - sums[l - 1]))

        return ans

def main():
    sol = Solution()
    assert sol.minAbsDifference(nums = [5,-7,3,5], goal = 6) == 0, 'fails'

    assert sol.minAbsDifference(nums = [7,-9,15,-2], goal = -5) == 1, 'fails'

    assert sol.minAbsDifference(nums = [1,2,3], goal = -7) == 7, 'fails'

    assert sol.minAbsDifference([3346,-3402,-9729,7432,2475,6852,5960,-7497,3229,6713,8949,9156,3945,-8686,1528,5022,-9791,-3782,-191,-9820,7720,-6067,-83,6793,340,7793,8742,8067], -20357) == 0, 'fails'



if __name__ == '__main__':
   main()