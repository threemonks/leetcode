"""
1884. Egg Drop With 2 Eggs and N Floors
Medium

261

20

Add to List

Share
You are given two identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

In each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.



Example 1:

Input: n = 2
Output: 2
Explanation: We can drop the first egg from floor 1 and the second egg from floor 2.
If the first egg breaks, we know that f = 0.
If the second egg breaks but the first egg didn't, we know that f = 1.
Otherwise, if both eggs survive, we know that f = 2.
Example 2:

Input: n = 100
Output: 14
Explanation: One optimal strategy is:
- Drop the 1st egg at floor 9. If it breaks, we know f is between 0 and 8. Drop the 2nd egg starting
  from floor 1 and going up one at a time to find f within 7 more drops. Total drops is 1 + 7 = 8.
- If the 1st egg does not break, drop the 1st egg again at floor 22. If it breaks, we know f is between 9
  and 21. Drop the 2nd egg starting from floor 10 and going up one at a time to find f within 12 more
  drops. Total drops is 2 + 12 = 14.
- If the 1st egg does not break again, follow a similar process dropping the 1st egg from floors 34, 45,
  55, 64, 72, 79, 85, 90, 94, 97, 99, and 100.
Regardless of the outcome, it takes at most 14 drops to determine f.
"""
"""
DP

dp[i][j] := use i eggs (i-1 eggs, as index is 0 based), we can determine j is the critical floor, with a total floors n

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

time O(2*N^2)
space O(1)
"""
from functools import lru_cache
class Solution:
    def twoEggDrop(self, n: int) -> int:
        eggs = 2

        @lru_cache(None)
        def dp(eggs, floors):
            # print('floors=%s eggs=%s' % (floors, eggs))
            if eggs == 1 or floors <= 1:
                # if only one egg left, we have to test 1 ... i-1 one by one
                return floors

            ans = n
            # try all k from 1 to floors, use best (min) result
            # take the worst case of the two situations
            for k in range(1, floors+1): # start with drop eggs at k-th floor
                ans = min(ans,
                          1+ max(
                            dp(eggs-1, k-1), # if egg broke, we have one less egg, and k-1 floors to test
                            dp(eggs, floors-k) # if egg not broke, we have e egg to test n-k floor.
                                 )
                         )

            return ans

        return dp(eggs, n)


def main():
    sol = Solution()
    assert sol.twoEggDrop(2) == 2, 'fails'

    assert sol.twoEggDrop(100) == 14, 'fails'

if __name__ == '__main__':
   main()