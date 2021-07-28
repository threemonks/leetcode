"""
1648. Sell Diminishing-Valued Colored Balls
Medium

366

106

Add to List

Share
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.



Example 1:


Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.
Example 2:

Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
Example 3:

Input: inventory = [2,8,4,10,6], orders = 20
Output: 110
Example 4:

Input: inventory = [1000000000], orders = 1000000000
Output: 21
Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.


Constraints:

1 <= inventory.length <= 10^5
1 <= inventory[i] <= 10^9
1 <= orders <= min(sum(inventory[i]), 10^9)
"""
from typing import List

"""
Greedy + Heap

naive method: always pick color with most remaining quantity, reduce that color quantity by 1, then push back into heapq
and repeat

time O(N^2)
TLE

"""
import heapq


class Solution0:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 1000000007
        ans = 0

        values = [-i for i in inventory]
        heapq.heapify(values)

        while values and orders:
            num = heapq.heappop(values)
            num = -num
            ans = (ans + num) % MOD
            orders -= 1
            heapq.heappush(values, -(num - 1))

        return ans


"""
Greedy + Heap

better Greedy + Heap

store (# of balls, types of balls with this count) into heap, each time we take the top element (ballcount group) from heap, which is a group of balls of same count, try to fulfill order using this group, layer by layer, if it can fulfill order using just this ball count group, before its ball count drop to same as next ballcount group's ball count at top of heap, we are done (we might use 1 from each ball type for one or more times, then one last time maybe need less than balltypecount of balls from the group)
if not, that means we will use 1 from each type in this group, repeatedly, until the count of each type reduces to be same as the next group at top of heap, at which point we just pop the group from top of heap, merge with remaining items from the group we have been taking orders from, and push the combined group back into heap, and repeat

time O(N*log(N))
"""
import heapq
from collections import Counter


def sumap(a, b):
    # sum of arithmetic sequence a < b
    if a > b:
        return 0
    ans = (a + b) * (b - a + 1) // 2
    # print('sumap a=%s b=%s ans=%s' % (a, b, ans))
    return ans


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 1000000007
        ans = 0

        counter = Counter(inventory)

        balls = []  # prioritqueue, holds ball counts, and # of ball types with this count
        for ballcount, balltypecount in counter.items():
            heapq.heappush(balls, [-ballcount, balltypecount])

        while balls and orders > 0:

            ballcount, balltypecount = heapq.heappop(balls)
            ballcount *= -1
            if balls:  # there are more ball counts
                nxt_ballcount, nxt_balltypecount = heapq.heappop(
                    balls)  # next ball count and ball count type at top of heap
                nxt_ballcount *= -1
            else:
                nxt_ballcount, nxt_balltypecount = 0, 0

            # print('ballcount=%s nxt_ballcount=%s' % (ballcount, nxt_ballcount))
            if (
                    ballcount - nxt_ballcount) * balltypecount > orders:  # can fulfill orders without reducing ballcount to next ballcount in heap top
                # fulfill the order using just from ballcount, balltypecount
                # we will accumulate cost by taking orders//balltypecount from each of the type in this group
                # then take remaining orders%balltypecount from this group
                a = orders // balltypecount  # # of balls we take from each ball type in this group
                b = orders % balltypecount  # remaining # of balls we take from this group to make enough for orders
                # print('fulfill order using just ballcount%s balltypecount=%s a=%s b=%s orders=%s' % (ballcount, balltypecount, a, b, orders))
                if a > 0:  # take a balls from each ball type, then for remaining orders, just take from any type in the group
                    ans = (ans + sumap(ballcount - a + 1, ballcount) * balltypecount + b * (ballcount - a)) % MOD
                else:  # not enough order amount to take one from each type, just take some from any type in the group
                    ans = (ans + b * (ballcount - a)) % MOD
                # print('fulfill order using just ballcount=%s balltypecount=%s balls=%s orders=%s ans=%s' % (ballcount, balltypecount, balls, orders, ans))
                break
            else:
                # after taking a few layers from (ballcount,balltypecount), merge ballcount with nxt_ballcount
                ans = (ans + sumap(nxt_ballcount + 1, ballcount) * balltypecount) % MOD
                orders -= (ballcount - nxt_ballcount) * balltypecount
                nxt_balltypecount += balltypecount
                heapq.heappush(balls, [-nxt_ballcount, nxt_balltypecount])

            # print('balls=%s orders=%s ans=%s' % (balls, orders, ans))

        return ans

def main():
    sol = Solution()
    assert sol.maxProfit(inventory = [2,5], orders = 4) == 14, 'fails'

    assert sol.maxProfit(inventory = [3,5], orders = 6) == 19, 'fails'

    assert sol.maxProfit(inventory = [2,8,4,10,6], orders = 20) == 110, 'fails'

    assert sol.maxProfit(inventory = [1000000000], orders = 1000000000) == 21, 'fails'

if __name__ == '__main__':
   main()