"""
55. Jump Game
Medium

6203

424

Add to List

Share
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i] <= 10^5
"""
from functools import lru_cache
from typing import List

"""
Greedy

farthest is max index we can reach globally. We can jump to i+nums[i] if we can reach index i.

mistakes:
1. we can jump from i only if we can get to i
"""


class Solution0:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0
        for i in range(n):
            if farthest >= i:
                farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:
                return True

        return farthest >= n - 1

"""
DP

dp[i] := we can reach i

transition:
    dp[i] = true if any dp[j]+nums[j] >=i for j = 0, ..., i-1

"""


class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def dp(i):
            if i == 0:
                return True
            for j in range(i - 1, -1, -1):
                if dp(j) and j + nums[j] >= i:
                    return True

            return False

        return dp(n - 1)


"""
Greedy

from right to left, find a good index can get us to i

"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lastpos = n - 1  # last pos that can reach end
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= lastpos:  # can we move from i to lastpos (the previous good position that can reach end)
                lastpos = i

        return lastpos == 0


def main():
    sol = Solution()
    assert sol.canJump(nums = [2,3,1,1,4]) is True, 'fails'

    assert sol.canJump(nums = [3,2,1,0,4]) is False, 'fails'

if __name__ == '__main__':
   main()