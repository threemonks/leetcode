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
import collections

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

time O(N*M) - N = len(rods), M = min(3^N, sum(rods)<=5000)
  3^N because each rode can be put in left, right, or discarded.
"""


class Solution0:
    def tallestBillboard(self, rods: List[int]) -> int:
        # sort rods
        offset = 5000
        dp = [-1] * (2 * offset + 1)  # height of -1 means this diff is not meaningful (was not achieved)
        dp[0 + offset] = 0  # initial condition, using no rods, diff is 0 (+offset)

        for i, l in enumerate(rods):
            # rods[i] has not been used yet, use it to update all dps
            dp_old = dp[:]  # keep a copy so that with each rod, we update dp[diff] using dp from previous round of rod
            for diff in range(-offset, offset + 1):
                if dp_old[diff + offset] == -1:  # previous state is not meaningful
                    continue
                if diff + l + offset < 2 * offset + 1:
                    dp[diff + l + offset] = max(dp[diff + l + offset], dp_old[diff + offset] + l)
                if diff - l + offset >= 0:
                    dp[diff - l + offset] = max(dp[diff - l + offset], dp_old[diff + offset])

        return dp[0 + offset]


"""
DP
observation, its a knapsack problem, for each rod, we can add its height to left, or right, or not used, so the problem can be considered as:

Given a list of numbers, multiple each number with 1, or 0, or -1, make the sum of all numbers to 0. Find a combination which has largest sum of all positive numbers.

We can consider the sum as the key / index of dp, and the positive number sum as the value of dp, loop through all rods, for each rod, check each dp index (sum) to see if it will be updated by this rod, actually only dp[s+i], dp[s-i] might be updated by this rod, from dp[s], dp[s+i] or dp[s-i] from dp in previous round

base case dp[0] = 0 # uses no rods

"""

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = dict()
        dp[0] = 0

        for i in rods:
            cur = collections.defaultdict(int)
            for s in dp:
                cur[s + i] = max(cur[s + i], dp[s] + i)
                cur[s] = max(cur[s], dp[s])
                cur[s - i] = max(cur[s - i], dp[s] - i)
            dp = cur

        return dp[0]


def main():
    sol = Solution()
    assert sol.tallestBillboard([1,2,3,6]) == 6, 'fails'

    assert sol.tallestBillboard([1,2,3,6]) == 6, 'fails'

    assert sol.tallestBillboard([1,2]) == 0, 'fails'

if __name__ == '__main__':
   main()