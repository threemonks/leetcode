"""
254. Factor Combinations
Medium

740

33

Add to List

Share
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].



Example 1:

Input: n = 1
Output: []
Example 2:

Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
Example 3:

Input: n = 37
Output: []
Example 4:

Input: n = 32
Output: [[2,16],[4,8],[2,2,8],[2,4,4],[2,2,2,4],[2,2,2,2,2]]


Constraints:

1 <= n <= 10^7
"""
from typing import List

"""
Backtrack

steps:
0. in each recursive dfs(n, start, factors) call
1. for i from 2...sqrt(n)
2. add factors + [i, n//i] as new result list
3. recursively call dfs(n//i, start=i, factors + [i])
4. backtrack by removing i from factors # done at step 3

time O(sqrt(N)*logN)
"""

import math
from functools import lru_cache


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        ans = []

        def dfs(k, start, factors, result):
            i = start
            while i * i <= k:
                if k % i == 0:
                    result.append(factors + [i, k // i])  # adding factors list [..., i, k//i]
                    dfs(k // i, i, factors + [i], result)
                i += 1

        dfs(n, 2, [], ans)

        return ans

def main():
    sol = Solution()
    assert sol.getFactors(12) == [[2,6],[3,4],[2,2,3]], 'fails'

    # assert sol.getFactors(32) == [[2,16],[4,8],[2,2,8],[2,4,4],[2,2,2,4],[2,2,2,2,2]], 'fails'

if __name__ == '__main__':
   main()