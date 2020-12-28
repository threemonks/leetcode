"""
377. Combination Sum IV
Medium

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.


Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""
from typing import List
from functools import lru_cache

"""
dp topdown/recursive

time O(N^2)
space O(1)
"""

class Solution0:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        @lru_cache(None)
        def dfs(target):
            nonlocal nums
            if target == 0:
                return 1
            res = 0
            for num in nums:
                if num <= target:
                    res += dfs(target - num)
            return res

        return dfs(target)


"""
dp bototm up
dp[i] : number of combinations (or rather, permutations) for target i
"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1  # empty set

        for i in range(1, target + 1):
            for j in range(len(nums)):
                if i - nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]
                # print('i=%s j=%s nums[%s]=%s dp[%s]=%s' % (i, j, j, nums[j], dp[i], i))

        return dp[-1]


def main():
    sol = Solution()
    assert sol.combinationSum4([1, 2, 3], 4) == 7, 'fails'

    assert sol.combinationSum4([4,2,1], 32) == 39882198, 'fails'

if __name__ == '__main__':
   main()