"""
1000. Minimum Cost to Merge Stones
Hard
"""
from functools import lru_cache
from math import inf
from typing import List

"""
DP top down / recursive

Observation:
1. The number of piles reduces K - 1 after merging K piles (each K piles merge into 1 pile)
If (len(stones) - 1) % (K - 1) != 0, it is impossible to merge them into 1 pile.
2. If less than K piles and no more merger happens.
3. let dp[i][j][m] means the minimum cost needed to merge stones[i] ~ stones[j] to m piles
note that when deriving transition function for dp[i][j], it can only be obtained by those steps that result in 1 pile, K piles (which can then become 1 pile), 1+(K-1)*x piles, but not other number of piles, so we have
dp[i][j][m] := minimum cost to merge stones[i] ... stones[j] into m piles

dp[i][j][1] = dp[i][j][K] + sum(stones[i:j+1]) # this is one merge
dp[i][j][m] = min(dp[i][mid][1] + dp[mid+1][j][m-1]) for all mid = i+(K-1)*x # this divides into two subproblems, but no merging happens

init condition:
dp[i][i][1] = 0
dp[i][i][m] = inf for 1<m

note all valid mid points must be K-1 piles away from i, i.e., 
mid = i+(K-1)*x

time O(N^3/K) - iterate for i, j, m, and each time the index move at step K
space (N^2) - stack, i, j
mistakes:
1. merged pile is a choice for remaining steps
2. need to add early termination condition if (j-i+1-m)%(K-1) != 0: return inf
3. need two transitions:
    dp[i][j][1] <= dp[i][j][K] + sum(stones[i:j+1])
    dp[i][j][m] = min(dp[i][mid][1] + dp[mid+1][j][m-1])
"""


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if n == 1:
            return 0
        if (n - 1) % (
                K - 1) != 0:  # if total piles-1 is not multiples of K-1, not possible, since each merge reduce # piles by K-1
            return -1

        # calculate prefix sum to speed up sum
        presum = [0 for _ in range(len(stones))]
        presum[0] = stones[0]
        for i in range(1, n):
            presum[i] = presum[i - 1] + stones[i]

        @lru_cache(None)
        def dp(i, j, m):
            # min cost to merge stones[i:j+1] into m piles
            # print('i=%s j=%s m=%s' % (i, j, m))
            if (j - i + 1 - m) % (K - 1) != 0:
                return inf
            if i == j:
                return 0 if m == 1 else inf
            if m == 1:
                # return dp(i, j, K) + sum(stones[i:j+1])
                return dp(i, j, K) + presum[j] - (presum[i - 1] if i - 1 >= 0 else 0)

            cost = inf
            # only jump at step K-1 since only those are valid possible mid way # of piles that can contribute to possible new costs
            # for mid in range(i, j):
            #     cost = min(cost, dp(i, mid, 1) + dp(mid+1, j, m-1))
            for mid in range(i, j, K - 1):
                cost = min(cost, dp(i, mid, 1) + dp(mid + 1, j, m - 1))

            return cost

        ans = dp(0, n - 1, 1)

        return ans if ans < inf else -1


def main():
    sol = Solution()
    assert sol.mergeStones(stones = [3,2,4,1], K = 2) == 20, 'fails'

    assert sol.mergeStones(stones = [3,2,4,1], K = 3) == -1, 'fails'

    assert sol.mergeStones(stones = [3,5,1,2,6], K = 3) == 25, 'fails'

if __name__ == '__main__':
   main()