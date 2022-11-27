"""
325. Maximum Size Subarray Sum Equals k
Medium

1838

55

Add to List

Share
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there is not one, return 0 instead.



Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.


Constraints:

1 <= nums.length <= 2 * 10^5
-104 <= nums[i] <= 10^4
"""
from typing import List

"""
Hash Map

calculate prefix sum psum, and store its index into map (always store last index of this value, to get longest subarray)
then iterate through prefixsum, if psum[i]+k in map, with index j, then j-i+1 is one such subarray (with sum value == k)

Note:
1. special case when psum[i] == k, that is an valid subarray from beginning to index i (including)


time O(N)
"""
from collections import defaultdict


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        psum = [0 for _ in range(n)]
        psum[0] = nums[0]

        for i in range(1, n):
            psum[i] = psum[i - 1] + nums[i]

        # print(f"{psum = }")

        maps = defaultdict(list)

        for i in range(n):
            maps[psum[i]] = i  # just keep the max index

        # print(f"{maps = }")

        ans = 0
        for i in range(n):
            if psum[i] == k:  # sum from first element to i-th (including)
                ans = max(ans, i + 1)
                # print(f"{i = } {psum[i] = } {ans = }")
            if psum[i] + k in maps:
                j = maps[psum[i] + k]
                ans = max(ans, j - i)
                # print(f"{i = } {j = } {psum[i] = } {ans = }")

        return ans

def main():
    sol = Solution()
    assert sol.maxSubArrayLen(nums = [1,-1,5,-2,3], k = 3) == 4, 'fails'

    assert sol.maxSubArrayLen(nums = [-2,-1,2,1], k = 1) == 2, 'fails'

if __name__ == '__main__':
   main()