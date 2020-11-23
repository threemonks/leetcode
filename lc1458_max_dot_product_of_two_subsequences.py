"""
1458. Max Dot Product of Two Subsequences
Hard

364

9

Add to List

Share
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).



Example 1:

Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.
Example 2:

Input: nums1 = [3,-2], nums2 = [2,-6,7]
Output: 21
Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.
Example 3:

Input: nums1 = [-1,-1], nums2 = [1,1]
Output: -1
Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.


Constraints:

1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 1000

"""
import collections
import math
from functools import lru_cache
from typing import List

"""
dp two arrays

dp[i][j] : maximum dot product after checking nums1[:i] and nums2[:j]

if nums1[i] nums2[j] of same sign:
    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j-1]+nums1[i]*nums2[j], dp[i-1][j] + ??, dp[i][j-1] + ?? )

time O(m*n)
space O(m*n)

"""

import numpy

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        nums1 = nums1
        nums2 = nums2
        dp = [[-math.inf/2 for _ in range(l2)] for _ in range(l1)] # init to -math.inf/2 as we are calculating max, and to avoid overflow when using math.inf directly
        dp[0][0] = nums1[0]*nums2[0]
        for i in range(1, l1):
            dp[i][0] = max(dp[i-1][0], nums1[i]*nums2[0])

        for j in range(1, l2):
            dp[0][j] = max(dp[0][j-1], nums1[0]*nums2[j])

        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = max(dp[i - 1][j - 1] + nums1[i] * nums2[j], # update dp[i-1][j-1] with new dot product result
                               dp[i - 1][j],
                               dp[i][j - 1],
                               nums1[i] * nums2[j] # ignore previous F(.., ..) because it might be better to not add it at all (i.e. if it is negative).
                               )
                print(numpy.matrix(dp))

        return dp[-1][-1]


"""
dp topdown recursive
"""


class Solution1:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def helper(i, j):
            nonlocal nums1, nums2
            if i == -1 or j == -1:
                return -math.inf/2
            if i == 0 and j == 0:
                return nums1[i] * nums2[j]
            return max(helper(i - 1, j - 1)+nums1[i] * nums2[j], helper(i - 1, j), helper(i, j - 1), nums1[i] * nums2[j])

        return helper(len(nums1) - 1, len(nums2) - 1)


def main():
    sol = Solution1()
    assert sol.maxDotProduct([2,1,-2,5], [3,0,-6]) == 18, 'fails'

    assert sol.maxDotProduct([3,-2], [2,-6,7]) == 21, 'fails'

    assert sol.maxDotProduct([-1,-1], [1,1]) == -1, 'fails'

if __name__ == '__main__':
   main()