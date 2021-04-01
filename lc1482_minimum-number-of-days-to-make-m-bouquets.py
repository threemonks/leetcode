"""
1482. Minimum Number of Days to Make m Bouquets
Medium

Given an integer array bloomDay, an integer m and an integer k.

We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.



Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let's see what happened in the first three days. x means flower bloomed and _ means flower didn't bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here's the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.
Example 4:

Input: bloomDay = [1000000000,1000000000], m = 1, k = 1
Output: 1000000000
Explanation: You need to wait 1000000000 days to have a flower ready for a bouquet.
Example 5:

Input: bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
Output: 9


Constraints:

bloomDay.length == n
1 <= n <= 10^5
1 <= bloomDay[i] <= 10^9
1 <= m <= 10^6
1 <= k <= n

"""
from typing import List

"""
Binary Search

binary search for minimum number of days between min(bloomDay) and max(bloomDay)

time O(Nlog(N))
mistakes:
1. instead of count bloomDay[i]<=target for every k elements, we keep accumulating flowers that are in blossom (bloomDay[i]<=target)
if accumulated k flowers, increase bouquet count by 1, reduce flower count by k, and continue
   whenever encounter a flower that has yet to bloom, reset flower count t0 0, since we need only adjacent flowers.
"""

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        def possible(target):
            # check how many consecutive k-length subarrays with bloomDay <= target
            nonlocal bloomDay, m, k, n
            f = 0
            count = 0
            for d in bloomDay:
                if d > target:
                    f = 0
                else:
                    f += 1
                    if f >= k:
                        count += 1
                        f -= k  # reset f count after one bouq
                        if count >= m:
                            return True

            return count >= m

        lo, hi = min(bloomDay), max(bloomDay)
        while lo < hi:
            mi = lo + (hi - lo) // 2
            # print('lo=%s hi=%s mi=%s' % (lo, hi, mi))
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo

def main():
    sol = Solution()
    assert sol.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1) == 3, 'fails'

    assert sol.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 2) == -1, 'fails'

    assert sol.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3) == 12, 'fails'

    assert sol.minDays(bloomDay = [1000000000,1000000000], m = 1, k = 1) == 1000000000, 'fails'

    assert sol.minDays(bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2) == 9, 'fails'


if __name__ == '__main__':
   main()