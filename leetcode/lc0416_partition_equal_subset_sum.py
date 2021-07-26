"""
416. Partition Equal Subset Sum
Medium

https://leetcode.com/problems/partition-equal-subset-sum/
"""
from typing import List
from functools import lru_cache

"""
Backtrack

* keep track of two sums
* remove one value from remaining numbers, until there's no more to use (use index to keep track when index ==len(nums)) (base case)
* search each possible path (add this number to left, add this number to right)

"""
from functools import lru_cache


class Solution0:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2 != 0:  # total sum is odd, then not partitionable
            return False

        @lru_cache(None)
        def partition(index, left, right):
            # base case
            if index == n:
                return left == right
            # choose first element
            #
            # explore
            return partition(index + 1, left + nums[index], right) or partition(index + 1, left, right + nums[index])
            # unchoose first element
            #

        return partition(0, 0, 0)


"""
DP (or variant of 0/1 knapsack problem with target weight is sums/2, and weight is 1)

For each number, we can pick it or not. let dp[i][j] be the specific sum j we can achieve with first i-th items, dp[i][j] is true if we can pick items from first 1...i items such that the sum is j, otherwise it is false

Base case is dp[0][0] = true

Transition function:
for dp[i][j], for item i, if we don't pick it, then dp[i][j] = dp[i-1][j], means if first i-1 items can sum to j, then first i items can also sum to j, because we can just not use item i
if we do use item i, then dp[i][j] = dp[i][j-nums[i]], which means if first i-1 items sum to j-nums[i], then adding item i will now sum to j-nums[i]+nums[i] = j
so dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

"""


class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sums = sum(nums)
        if sums % 2 != 0:  # total sum is odd, then not partitionable
            return False

        sums //= 2

        dp = [[False for _ in range(sums + 1)] for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n):
            dp[i][0] = True

        for j in range(1, sums):
            dp[0][j] = False

        for i in range(1, n + 1):
            for j in range(1, sums + 1):
                dp[i][j] = dp[i - 1][j]
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][sums]


"""
DP knapsack subset problem with state compression using 1-D dp array

Note: we need to iterate j backwards, as we don't want dp[j] with smaller j being impacted by dp[j] of larger j from previous i-1 th run
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sums = sum(nums)
        if sums % 2 != 0:
            return False

        sums //= 2
        dp = [False for _ in range(sums + 1)]

        # base case
        dp[0] = True  # use no number, sum to 0

        for i in range(1, n + 1):
            for j in range(sums, -1, -1):
                if j - nums[i - 1] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i - 1]]

        return dp[sums]


def main():
    sol = Solution()
    assert sol.canPartition(nums = [1,5,11,5]) is True, 'fails'

    assert sol.canPartition(nums = [1,2,3,5]) is False, 'fails'

if __name__ == '__main__':
   main()