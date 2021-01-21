"""
956. Tallest Billboard
Hard

You are installing a billboard and want it to have the largest height.  The billboard will have two steel supports, one on each side.  Each steel support must be an equal height.

You have a collection of rods which can be welded together.  For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation.  If you cannot support the billboard, return 0.

Example 1:

Input: [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
Example 2:

Input: [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
Example 3:

Input: [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.


Note:

0 <= rods.length <= 20
1 <= rods[i] <= 1000
The sum of rods is at most 5000.

"""
from typing import List

"""
first impression would be a 2D knapsack problem, then it would be dp[left][right], but left right height range is 0 ~ 5000, dp[5000][5000] would be too big

1 <= rods[i] <= 1000
and sum(rods) <= 5000 => indicates that we would like dp dimension on value (index being diff between left and right rod height)

define dp[diff] := max left height for diff = left height - right height

target is to find max diff[0] with all rods used to update it

each time, a rod can be added to either left, or right, or don't use, so with one rod being considered, the transition equation of dp[diff] from one value to next would be
for l in rods:
    for all possible differences [-5000, 5000+1]
        if we don't use it:
            dp[diff] = dp[diff] # no change
        if we put it on left:
            dp[diff+l] = max(dp[diff+l], dp_old[diff]+l) # keep copy of dp from previous run (considering a rod)
        if we put it on right:
            dp[diff-l] = max(dp[diff-l], dp_old[diff])

Note:
    1. to avoid negative index when diff goes to -5000, we add offset to dp index
    2. the above transition equation is valid only if the value of dp to be used to transfer from is valid

"""
from functools import lru_cache
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # sort rods
        offset = 5000
        dp = [-1] * (2*offset+1) # height of -1 means this diff is not meaningful (was not achieved)
        dp[0+offset] = 0 # initial condition, using no rods, diff is 0 (+offset)

        for i, l in enumerate(rods):
            # rods[i] has not been used yet, use it to update all dps
            dp_old = dp [:] # keep a copy so that with each rod, we update dp[diff] using dp from previous round of rod
            for diff in range(-offset, offset+1):
                if dp_old[diff+offset] == -1: # previous state is not meaningful
                    continue
                if diff+l+offset < 2*offset+1:
                    dp[diff+l+offset] = max(dp[diff+l+offset], dp_old[diff+offset]+l)
                if diff-l+offset >= 0:
                    dp[diff-l+offset] = max(dp[diff-l+offset], dp_old[diff+offset])

        return dp[0+offset]

def main():
    sol = Solution()
    assert sol.tallestBillboard([1,2,3,6]) == 6, 'fails'

    assert sol.tallestBillboard([1,2,3,6]) == 6, 'fails'

    assert sol.tallestBillboard([1,2]) == 0, 'fails'

if __name__ == '__main__':
   main()