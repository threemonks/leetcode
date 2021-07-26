"""
646. Maximum Length of Pair Chain
Medium

1453

89

Add to List

Share
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.



Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].


Constraints:

n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti < 1000

"""
import math
from typing import List

"""
Greedy

sort by end time, try to use next pair that will end first

mistakes:
1. start time curp should be -math.inf, not 0, since we have negative numbers
"""


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: x[1])

        ans = 0
        curp = -math.inf
        for p0, p1 in pairs:
            # print('curp=%s p0=%s p1=%s' % (curp, p0, p1))
            if p0 > curp:
                ans += 1
                curp = p1
                # print('ans=%s using (%s, %s)' % (ans, p0, p1))

        return ans


def main():
    sol = Solution()
    assert sol.findLongestChain(pairs = [[1,2],[2,3],[3,4]]) == 2, 'fails'

    assert sol.findLongestChain(pairs = [[1,2],[7,8],[4,5]]) == 3, 'fails'


if __name__ == '__main__':
   main()