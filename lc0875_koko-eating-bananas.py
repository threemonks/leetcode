"""
875. Koko Eating Bananas
Medium

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.



Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23


Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109

"""
from typing import List

"""
Binary Search

min of k is 1, largest of k is max(piles) since if he finishes at least one pile per hour, piles.length <=h, he will always be able to finish within h hour

Why binary search?
if he cannot finish at speed k, then he cannot finish with any speed x<k
if he can finish at speed k, then he can finish with any speed x > k
i.e., there's some k such that if he can finish if and only if his speed x >= k
so we can do binary search to find this value k

time O(Nlog(N))

mistakes:
1 calculating hours needed for pile of size p>0 at speed k, it is math.ceil(p/k)=((p-1)//k+1)
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_finish(k):
            # can he finish with speed k per hour
            # for each pile of size p>0, the hours he need would be math.ceil(p/k) = ((p-1)//k)+1 hours
            return sum([((p - 1) // k + 1) for p in piles]) <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            # print('left=%s right=%s mid=%s' % (left, right, mid))
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left

def main():
    sol = Solution()
    assert sol.minEatingSpeed(piles = [3,6,7,11], h = 8) == 4, 'fails'

    assert sol.minEatingSpeed(piles = [30,11,23,4,20], h = 5) == 30, 'fails'

    assert sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6) == 23, 'fails'

    assert sol.minEatingSpeed([312884470], 312884469) == 2, 'fails'



if __name__ == '__main__':
   main()