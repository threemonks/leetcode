"""
494. Target Sum
Medium

https://leetcode.com/problems/target-sum/
"""
from functools import lru_cache
from typing import List
from collections import defaultdict
from functools import lru_cache

"""
DFS / Recursion with memoization

Note:
    base case index = len(nums)
    recursive 
        backtrack(index+1, target-nums[index]) # + sign
        backtrack(index+1, target+nums[index]) # - minus sign

time O(2^N)
space O(1)
"""


class Solution0:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def backtrack(index, target):
            nonlocal count
            # base case
            if index == n:
                if target == 0:
                    return 1
                return 0

            # use current elment

            # explore with current element
            # +
            count1 = backtrack(index + 1, target - nums[index])
            # -
            count2 = backtrack(index + 1, target + nums[index])

            # unchoose current element

            return count1 + count2

        count = backtrack(0, S)

        return count


"""
DP

sum of elements in the given array will not exceed 1000 => sum can use as dp index

dp[i][j] := the number of assignments which can lead to a sum of j upto the i-th index

dp[i][j+nums[i]] = dp[i][j+nums[i]] + dp[i-1][j] <= with sum of j at i-1th element, we assign plus(+) sign, achieve j+nums[i] at i-th element
dp[i][j-nums[i]] = dp[i][j-nums[i]] + dp[i-1][j] <= with sum of j at i-1th element, we assign minus(-) sign, achieve j-nums[i] at i-th element

dp[n-1][S+1000] is the answer

Note:
    sum can range from -1000 to +1000, needs to offset 1000 to use sum as index

"""


class Solution1:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)

        dp = [[0 for _ in range(2001)] for _ in range(n)]

        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1

        for i in range(1, n):
            for sums in range(-1000, 1001):
                if dp[i - 1][sums + 1000] > 0:
                    dp[i][sums + nums[i] + 1000] += dp[i - 1][sums + 1000]
                    dp[i][sums - nums[i] + 1000] += dp[i - 1][sums + 1000]

        if S > 1000:
            return 0
        else:
            return dp[n - 1][S + 1000]


"""
DP

similar to above, but use dict to store number of ways of assignments to sum j, at each step (element i)
use hashtable to visit valid states only

"""


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        counts = defaultdict(int)
        counts[0] = 1  # initial value for not picking any assignment yet, there's 1 way

        for i in range(n):
            ith_counts = defaultdict(int)
            for sums in counts:
                ith_counts[sums + nums[i]] += counts[sums]
                ith_counts[sums - nums[i]] += counts[sums]

            counts = ith_counts

        return counts[S]


def main():
    sol = Solution()
    assert sol.findTargetSumWays([1, 1, 1, 1, 1]) == 5, 'fails'

if __name__ == '__main__':
   main()