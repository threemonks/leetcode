"""
774. Minimize Max Distance to Gas Station
Hard

You are given an integer array stations that represents the positions of the gas stations on the x-axis. You are also given an integer k.

You should add k new gas stations. You can add the stations anywhere on the x-axis, and not necessarily on an integer position.

Let penalty() be the maximum distance between adjacent gas stations after adding the k new stations.

Return the smallest possible value of penalty(). Answers within 10-6 of the actual answer will be accepted.



Example 1:

Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
Output: 0.50000
Example 2:

Input: stations = [23,24,36,39,46,56,57,65,84,98], k = 1
Output: 14.00000


Constraints:

10 <= stations.length <= 2000
0 <= stations[i] <= 108
stations is sorted in a strictly increasing order.
1 <= k <= 10^6
"""
import math
from typing import List

"""
Binary Search

add k gas stations while minimize max distance between adjacent gas stations after adding
new positions are not necessarily on integer
the range is 10^(-6), max(existing distancess)

use binary search to find the smallest possible value of m
initilze left = 0 and right = the distance between the first and the last station
count is the number of gas station we need to make it possible.
if count > K, it means mid is too small to realize using only K more stations.
if count <= K, it means mid is possible and we can continue to find a smaller max gap.
When left + 1e-6 >= right, it means the answer within 10^-6 of the true value and it will be accepted.

mistakes:
1. we only consider adding new stations between stations[0] and stations[n-1], since adding out of this range does not help minimize the max gap after adding
2. because mi can be double, so we use hi-lo < 1e-6 as loop condition, and in each step, we update lo = mi or hi = mi depending on check result, also
  mi = (lo+hi)/2
"""


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        n = len(stations)
        dist = [0 for _ in range(n - 1)]
        maxdist = stations[n - 1] - stations[0]

        lo, hi = 0, maxdist  # [left, right)
        while hi - lo > 10 ** (-6):
            mi = (hi + lo) / 2  # mi is the upper bound of max distance achievable by K new gas stations
            # print('lo=%s hi=%s mi=%s' % (lo, hi, mi))
            if sum([math.ceil((stations[i + 1] - stations[i]) / mi) - 1 for i in range(n - 1)]) <= k:
                # if we can achieve mi with k new stations, lets try if we can achieve smaller max gap
                hi = mi
            else:
                lo = mi

        return lo


def main():
    sol = Solution()
    assert math.isclose(sol.minmaxGasDist(stations = [1,2,3,4,5,6,7,8,9,10], k = 9), 0.5, abs_tol=1e-6), 'fails'

    assert math.isclose(sol.minmaxGasDist(stations = [23,24,36,39,46,56,57,65,84,98], k = 1), 14.0, abs_tol=1e-6), 'fails'

if __name__ == '__main__':
   main()