"""
1799. Maximize Score After N Operations
Hard

"""
import math
from functools import lru_cache
from typing import List

"""
brutal force DFS

TLE (after memoization)

mistakes:
1. gcd implementation
2. could use tuple instead of list as function parameter, so that we can use memoization

"""


class Solution0:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) // 2

        @lru_cache(None)
        def gcd(x, y):
            while y > 0:
                x, y = y, x % y
            return x

        @lru_cache(None)
        def dfs(ns, partial):
            # print('ns=%s partial=%s' % (ns, partial))
            if not ns:
                return partial
            m = len(ns) // 2
            idx = n - m
            ans = -math.inf
            for i in range(2 * m):
                for j in range(i + 1, 2 * m):
                    ans = max(ans,
                              dfs(tuple(ns[:i] + ns[i + 1:j] + ns[j + 1:]), partial + (idx + 1) * gcd(ns[i], ns[j])))

            return ans

        return dfs(tuple(nums), 0)


"""
DP

use bitmask to represent the two number chosen to get gcd on i-th op

time O(N*fullmask*(2N)^2) = O(N^3*2^N) - fullmask=2^(2N)
space O(2^N)
"""


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        fullmask = (1 << n) - 1

        @lru_cache(None)
        def gcd(x, y):
            while y > 0:
                x, y = y, x % y
            return x

        @lru_cache(None)
        def dfs(op, bitmask):
            # print('op=%s bitmask=%s' % (op, bin(bitmask)))
            # reach n-th operation, already used nums indicated by bitmask (1 means used)
            if op == n // 2 + 1:
                # print('op=%s bitmask=%s return 0' % (op, bin(bitmask)))
                return 0
            if bitmask == fullmask:
                # print('op=%s bitmask=%s return 0' % (op, bin(bitmask)))
                return 0

            ans = -math.inf
            for i in range(n):
                if bitmask & (1 << i):
                    continue
                for j in range(i + 1, n):
                    if bitmask & (1 << j):
                        continue
                    ans = max(ans, op * gcd(nums[i], nums[j]) + dfs(op + 1, bitmask | (1 << i) | (1 << j)))

            # print('op=%s bitmask=%s ans=%s' % (op, bin(bitmask), ans))
            return ans

        return dfs(1, 0)

def main():
    sol = Solution()
    assert sol.maxScore(nums = [1,2]) == 1, 'fails'

    assert sol.maxScore(nums = [3,4,6,8]) == 11, 'fails'

    assert sol.maxScore(nums = [1,2,3,4,5,6]) == 14, 'fails'


if __name__ == '__main__':
   main()