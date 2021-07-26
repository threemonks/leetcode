"""
1049. Last Stone Weight II
Medium

"""
from typing import List

"""
DP Knapsack 0/1 variation

observation: assume four rocks, a,b,c,d, we can start with a-b, then add or minus c, say a-b+c, then add or minus d, say a-b+c-d
so we are trying to minimize a+c - (b+d), the order we pick which stone does not matter. So we basically want to split the stones to two group, and try to minimize the difference.

In other words, we want to pick a set of stones whose total weight is maximized, providing the sum of weight of these stones do not exceed half of all stones weights.

dp[i][s] := can we achieve total weight of s, using only first i-th stones

Base case:
dp[i][0] = 0

Transition:
    if s-stones[i-1] > 0:
        dp[i][s] = dp[i-1][s] | dp[i-1][s-stones[i-1]] # use or not use i-th stone stones[i-1]
    else:
        # not enough capacity to consider i-th stone stones[i-1]
        dp[i][s] = dp[i-1][s]

"""


class Solution0:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        sums = sum(stones)
        print(sums)

        dp = [[False for _ in range(sums // 2 + 1)] for _ in range(n + 1)]

        # base case
        for i in range(n + 1):
            dp[i][0] = True  # use no stone to get target sum 0

        s2 = 0  # we want to maximize s2 along with dp, because our goal is to minimize sums-2*s2

        for i in range(1, n + 1):
            for s in range(1, sums // 2 + 1):
                # has enough capacity
                if s >= stones[i - 1]:
                    # not use or use i-th stone (stones[i-1])
                    dp[i][s] = dp[i - 1][s] or dp[i - 1][s - stones[i - 1]]
                else:
                    dp[i][s] = dp[i - 1][s]

                # if this is a valid situation, we want to update max s2
                if dp[i][s]:
                    s2 = max(s2, s)
                # print('i=%s s=%s s2=%s' % (i, s, s2))

        return sums - 2 * s2


class Solution:
    def lastStoneWeightII(self, stones) -> int:

        dp = {0}
        for node in stones:
            newDP = dp
            dp = set()
            for x in newDP:
                # print('node=%s x=%s newDP=%s' % (node, x, newDP))
                dp.add(x + node)
                dp.add(x - node)

        res = float('inf')
        for num in dp:
            if num >= 0 and res > num:
                res = num

        return res
def main():
    sol = Solution()
    assert sol.lastStoneWeightII(stones = [2,7,4,1,8,1]) == 1, 'fails'

    assert sol.lastStoneWeightII(stones = [31,26,33,21,40]) == 5, 'fails'

    assert sol.lastStoneWeightII(stones = [1,2]) == 1, 'fails'


if __name__ == '__main__':
   main()