"""
1499. Max Value of Equation
Hard

246

9

Add to List

Share
Given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length. It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.



Example 1:

Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.
Example 2:

Input: points = [[0,0],[3,0],[9,2]], k = 3
Output: 3
Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.


Constraints:

2 <= points.length <= 10^5
points[i].length == 2
-10^8 <= points[i][0], points[i][1] <= 10^8
0 <= k <= 2 * 10^8
points[i][0] < points[j][0] for all 1 <= i < j <= points.length
xi form a strictly increasing sequence.

"""

from typing import List
import math
import collections

"""
Sliding Window Max

To max yi+yj+|xi-xj| <=> yi+yj-xi+xj for xi<xj when i<j
for a given j, yj+xj is fixed, we look for i that will maximize yi+yj-xi+xj, i.e., maximize yi-xi
so we can use sliding window maximum, and look for max(yi-xi) with constraint |xi-xj|<k
we use deque to store (xi, yi-xi), and the window size would be determined by xj-xi <= k (for i<j)

time O(N)
space O(k)
"""


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        n = len(points)

        dq = collections.deque()
        res = -math.inf
        for x, y in points:
            while dq and x - dq[0][0] > k:
                dq.popleft()
            # yi+yj+abs(xi-xj) <=> yi+yj+xj-xi
            if dq:
                res = max(res, y + x + dq[0][1])
                # print('res=%s' % res)
            # keep a decreasing queue by value of y-x since any existing element in deque with smaller y-x would be useless for future calculation since now we have a newer xi with larger yi-xi, and dq[0] (queue head) would give largest y-x for new incoming element to combine to get better result
            while dq and dq[-1][1] <= y - x:
                dq.pop()
            dq.append((x, y - x))
            # print('x=%s y=%s dq=%s' % (x, y, dq))

        return res


def main():
    sol = Solution()
    assert sol.findMaxValueOfEquation([[1,3],[2,0],[5,10],[6,-10]], 1) == 4, 'fails'

    assert sol.findMaxValueOfEquation([[0,0],[3,0],[9,2]], 3) == 3, 'fails'

    assert sol.findMaxValueOfEquation([[-19,9],[-15,-19],[-5,-8]], 10) == -6, 'fails'


if __name__ == '__main__':
   main()