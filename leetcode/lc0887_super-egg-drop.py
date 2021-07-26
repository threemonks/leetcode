"""
887. Super Egg Drop
Hard

1668

104

Add to List

Share
You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.



Example 1:

Input: k = 1, n = 2
Output: 2
Explanation:
Drop the egg from floor 1. If it breaks, we know that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
If it does not break, then we know f = 2.
Hence, we need at minimum 2 moves to determine with certainty what the value of f is.
Example 2:

Input: k = 2, n = 6
Output: 3
Example 3:

Input: k = 3, n = 14
Output: 4


Constraints:

1 <= k <= 100
1 <= n <= 10^4
"""
"""
DP

dp[i][j] := smallest number of drop to get the optimal floor with i eggs and j floors left

base:
dp[0][j] = j # one egg
dp[i][0] = 0 # no floor
dp[i][1] = 1 # one floor

dp[i][j] = min {
  1 + max (
    #if egg breaks
    dp[i-1][k-1],
    #if egg does not break
    dp[i][j-k]
    ) for k in 1 ... j
}

This will be O(K*N^2) will TLE with N~10^5. So we need to improve it.

Since first term dp(i-1, k-1) increases with k, second term dp(i, j-k) decrease with k increase, that means there's a value of k that would minimize dp. We can use binary search to find this value.

time O(KNlog(N))
space O(1)
"""
from functools import lru_cache


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        @lru_cache(None)
        def dp(k, n):
            # print('n=%s k=%s' % (n, k))
            if k == 1 or n <= 1:
                # if only one egg left, we have to test 1 ... i-1 one by one
                return n

            lo, hi = 1, n
            while lo < hi:
                x = lo + (hi - lo) // 2
                t1 = dp(k - 1, x - 1)
                t2 = dp(k, n - x)
                if t1 < t2:
                    lo = x + 1
                elif t1 > t2:
                    hi = x
                else:
                    lo = hi = x

            ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x)) for x in (lo, hi))

            return ans

        return dp(K, N)


def main():
    sol = Solution()
    assert sol.superEggDrop(1, 2) == 2, 'fails'

    assert sol.superEggDrop(2, 6) == 3, 'fails'

    assert sol.superEggDrop(3, 14) == 4, 'fails'

if __name__ == '__main__':
   main()