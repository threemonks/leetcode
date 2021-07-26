"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Medium

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.



Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
"""
import collections
import math
from functools import lru_cache
from typing import List

"""
subarray => two pointers
two pointers + brutal force
time O(N^2)
space O(1)
TLE
"""


class Solution0:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        res = 0
        j = 0
        for i in range(n):
            mx = max(nums[i:j + 1])
            mn = min(nums[i:j + 1])
            while j < n and abs(mx - mn) <= limit:
                # print('i=%s j=%s mn=%s mx=%s' % (i, j, mn, mx))
                j += 1
                if j == n:
                    break
                mx = max(nums[i:j + 1])
                mn = min(nums[i:j + 1])
            # print('i=%s j=%s mn=%s mx=%s res=%s' % (i, j, mn, mx, res))
            res = max(res, j - i)

        return res


"""
Sliding Window Max / Two Pointers
two pointers + sliding window max and min
subarray => two pointers
two pointers, iterate (fix) one pointer i, explore pointer j to see how far it can go, and record the longest valid j for each i, and keep updating this value as i iterates to end
keep a sliding window that is longest with its abs(max - min)<= limit, which we can use a deque to get max of sliding window in O(1) time
similarly use another deque to get min of sliding window in O(1) time

time O(N)
space O(N)
"""


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        qmax = collections.deque([0])  # storing index, decreasing queue to get max of sliding window in O(1) time
        qmin = collections.deque([0])  # storing index, increasing queue to get min of sliding window in O(1) time

        res = 1
        j = 0
        mn, mx = nums[0], nums[0]
        for i in range(n):
            if qmax:
                mx = nums[qmax[0]]
            if qmin:
                mn = nums[qmin[0]]
            while mx - mn <= limit:
                res = max(res, j - i+1)
                print('i=%s j=%s qmax=%s qmin=%s mx=%s mn=%s res=%s' % (i, j, qmax, qmin, mx, mn, res))
                j += 1
                if j == n: break
                while qmax and nums[j] >= nums[qmax[-1]]:
                    qmax.pop()
                qmax.append(j)
                mx = nums[qmax[0]]
                while qmin and nums[j] <= nums[qmin[-1]]:
                    qmin.pop()
                qmin.append(j)
                mn = nums[qmin[0]]
                print('added nums[j] i=%s j=%s qmax=%s qmin=%s mx=%s mn=%s' % (i, j, qmax, qmin, mx, mn))
            if j == n: break
            if qmax and qmax[0] == i:
                qmax.popleft()
                print('qmax=%s' % qmax)
            if qmin and qmin[0] == i:
                qmin.popleft()
                print('qmin=%s' % qmin)

        return res


def main():
    sol = Solution()
    assert sol.longestSubarray([8,2,4,7], 4) == 2, 'fails'

    assert sol.longestSubarray([10,1,2,4,7,2], 5) == 4, 'fails'

    assert sol.longestSubarray([4,2,2,2,4,4,2,2], 0) == 3, 'fails'

if __name__ == '__main__':
   main()