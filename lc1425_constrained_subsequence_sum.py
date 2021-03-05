"""
1425. Constrained Subsequence Sum
Hard

Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.



Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

"""
import collections
import math
from functools import lru_cache
from typing import List

"""
DP Sliding Window/Two Pointers
two pointers - brutal force to get max sum
dp[i] := max sum of valid subsequence with element ending at i
dp[i] = nums[i] + max([0, dp[i-k], dp[i-k+1], dp[i-1]])
use sliding window max for dp
what defines the sliding window size? j-i<=k
what do we store in dq? index of numbers that could be next largest?
"""


class Solution0:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dp = [-math.inf] * n  # store max sum of valid subsequence ending at i
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, n):
            dp[i] = nums[i] + max([0] + [dp[i - j] if i - j + 1 >= 0 else 0 for j in range(1, k + 1)])
            print('i=%s dp=%s' % (i, dp))
            res = max(res, dp[i])

        return res


"""
DP Sliding Window/Two Pointers
two pointers
dp[i] := max sum of valid subsequence with element ending at i
dp[i] = nums[i] + max([0, dp[i-k], dp[i-k+1], dp[i-1]])
use sliding window max to obtain max dp out of all dps within the sliding window
what defines the sliding window size? j-i<=k
what do we store in queue? index of dps that could be max for future, but still satify j-i<=k
we keep deque decreasing so q[0] is always the max within the window, to do that, we pop out any element in end of queue with smaller dp[q[-1]] < dp[i]
and at end of each iteration on index i, we popleft front of queue when it is no longer valid q[0]+k<=i
time O(N)
space O(N)
"""


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dp = [
                 -math.inf] * n  # store max sum of valid subsequence ending at i (valid means all its element has distance <= k)
        q = collections.deque()
        q.append(0)
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, n):
            # calculate dp[i]
            dp[i] = nums[i] + max(0, dp[q[0]] if q else 0)
            # pop out dp from q end that is smaller, as we want a decreasing queue
            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            q.append(i)
            # print('i=%s dp=%s q=%s' % (i, dp, q))
            res = max(res, dp[i])
            if q and q[
                0] + k <= i:  # if queue front element is too far from i (q[0]+k<i), we cannot include it further down, drop it
                q.popleft()

        return res


def main():
    sol = Solution()
    assert sol.constrainedSubsetSum([10,2,-10,5,20], 2) == 37, 'fails'

    assert sol.constrainedSubsetSum([-1,-2,-3], 1) == -1, 'fails'

    assert sol.constrainedSubsetSum([10,-2,-10,-5,20], 2) == 23, 'fails'


if __name__ == '__main__':
   main()