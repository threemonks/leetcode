"""
1011. Capacity To Ship Packages Within D Days
Medium

A conveyor belt has packages that must be shipped from one port to another within D days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
Example 2:

Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1


Constraints:

1 <= D <= weights.length <= 5 * 104
1 <= weights[i] <= 500
"""
import math
from typing import List

"""
Binary Search

if a given weight capacity k satisfy (can be shipped in D days), then all larger weight capcity >=k will also satisfy
if a given weight capacity k does not satisfy (cannot be shipped in D days), then all weight capacity less will not satisfy

i.e., the predicate function is monotonic => binary search

weight capacity range 
[max(weights), sum(weigths)]

mistakes:
1. 1 package has to fit on conveyor belt as a whole, so minimal capacity is heaviest package - max(weights)
2. day starts from 1 (since we increase by 1 only after weight won't fit in current day)
"""


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        n = len(weights)
        mn = max(weights)
        sums = sum(weights)

        def can_ship(k):
            # can we ship with D days with weight capacity k?
            nonlocal weights, D
            day = 1
            cur = 0  # weight so far
            for w in weights:
                if cur + w > k:
                    day += 1
                    cur = w
                    if day > D:
                        return False
                else:
                    cur += w

            return day <= D

        left, right = mn, sums
        while left < right:
            mid = left + (right - left) // 2
            # print('left=%s right=%s mid=%s' % (left, right, mid))
            if can_ship(mid):  # can ship, try smaller weight capacity
                right = mid
            else:  # cannot ship, needs to try larger weight capacity
                left = mid + 1

        return left


def main():
    sol = Solution()
    assert sol.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], D = 5) == 15, 'fails'

    assert sol.shipWithinDays(weights = [3,2,2,4,1,4], D = 3) == 6, 'fails'

    assert sol.shipWithinDays(weights = [1,2,3,1,1], D = 4) == 3, 'fails'


if __name__ == '__main__':
   main()