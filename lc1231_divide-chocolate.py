"""
1231. Divide Chocolate
Hard

You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.



Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], K = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]


Constraints:

0 <= K < sweetness.length <= 10^4
1 <= sweetness[i] <= 10^5
"""
import math
from typing import List

"""
Binary Search
maximize the minimum total sum of K+1 groups

We want to split the groups so all subgroup sums >= some value m - then we can binary search this value (min group sum), for each such value m, we check if we can divide the nums such that all subgroups total sweetness >= m

time O(Nlog(10^9)) - sum(sweetness) ~ 10^9
"""


class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        n = len(sweetness)
        sums = sum(sweetness)
        maxx = 1 + sums // (K + 1)  # add 1 to make right end exclusive
        minn = min(sweetness)

        # print('sums=%s maxx=%s minn=%s' % (sums, maxx, minn))

        def can_div(m):
            # given target m, can we divide to make all bars have total sweetness >= m
            nonlocal sweetness
            count = 0
            curr = 0  # current sweetness sum
            for s in sweetness:
                curr += s
                # print('i=%s curr=%s count=%s' % (i, curr, count))
                if curr >= m:
                    count += 1
                    curr = 0  # start a new cut, reset curr sweetness
                    if count >= K + 1:
                        return True

            return count >= K + 1

        ans = -math.inf
        lo, hi = minn, maxx
        while lo < hi:  # [left close (inclusiving), right open (exclusive))
            mi = lo + (hi - lo) // 2
            # print('lo=%s hi=%s mi=%s' % (lo, hi, mi))
            if can_div(mi):
                # print('can div')
                ans = max(ans, mi)
                lo = mi + 1
            else:  # cannot divide, try smaller number
                # print('cannot div')
                hi = mi

        return ans

def main():
    sol = Solution()
    assert sol.maximizeSweetness(sweetness = [1,2,3,4,5,6,7,8,9], K = 5) == 6, 'fails'

    assert sol.maximizeSweetness(sweetness = [5,6,7,8,9,1,2,3,4], K = 8) == 1, 'fails'

    assert sol.maximizeSweetness(sweetness = [1,2,2,1,2,2,1,2,2], K = 2) == 5, 'fails'


if __name__ == '__main__':
   main()