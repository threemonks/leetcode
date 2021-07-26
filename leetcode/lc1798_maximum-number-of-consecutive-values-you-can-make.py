"""
1798. Maximum Number of Consecutive Values You Can Make
Medium

"""
from typing import List

"""
Greedy

Since the ask is to make number of consecutive integers starting from and including 0, if we look at up to first i-1 th element, can already make consecutive integers up to x-1 (that is x integerx), then when checking at i-th element, as long as coins[i] <= x, then we can make any value from 1+coin, 2+coin, to x-1+coin, i.e., using values 0, 1, .., x-1 from previous make, adding current coin, we would be able to make 0+coin, 1+coin, ..., x-1+coin.

Since numbers can only be decomposed to smaller numbers, so integer x would only be composed of coins less than or equal to x, so we can sort the array in ascending order and check smaller coins first, without losing any possible ways of composing x.

time: O(N*log(N))
space: O(1)
"""
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:

        ans = 1
        for coin in sorted(coins):
            if coin > ans:
                break
            else:
                ans = ans + coin

        return ans

def main():
    sol = Solution()
    assert sol.getMaximumConsecutive(coins = [1,3]) == 2, 'fails'

    assert sol.getMaximumConsecutive(coins = [1,1,1,4]) == 8, 'fails'

    assert sol.getMaximumConsecutive(coins = [1,4,10,3,1]) == 20, 'fails'


if __name__ == '__main__':
   main()