"""
Sliding window max + Monotonic decreasing deque

keep a sliding window size of K (indices) (or less if not enough items yet), storing indices of monotonic decreasing nums as deque
so the max of the sliding window is always dq[0]

time O(N)
mistakes:
1. start to output at i=k-1
2. when left side item drop out of window size k, call dq.popleft()
"""
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dq = deque()
        ans = []
        for i in range(n):
            # add item nums[i] (index) into dq, while maintaining monotonic decreasing deque (value decreasing)
            # i.e., if dq right end nums[dq[-1]] < nums[i], drop nums[dq[-1]]
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            # now either dq is empty, or nums[dq[-1]] >= nums[i]
            dq.append(i)
            # drop items that are out of window k (index)
            while dq and dq[0] <= i - k:
                dq.popleft()
            # now all items in dq are valid within i-k to i-1, dq[0] is the max
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans