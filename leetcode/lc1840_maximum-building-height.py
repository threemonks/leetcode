"""
1840. Maximum Building Height
Hard

23

2

Add to List

Share
You want to build n new buildings in a city. The new buildings will be built in a line and are labeled from 1 to n.

However, there are city restrictions on the heights of the new buildings:

The height of each building must be a non-negative integer.
The height of the first building must be 0.
The height difference between any two adjacent buildings cannot exceed 1.
Additionally, there are city restrictions on the maximum height of specific buildings. These restrictions are given as a 2D integer array restrictions where restrictions[i] = [idi, maxHeighti] indicates that building idi must have a height less than or equal to maxHeighti.

It is guaranteed that each building will appear at most once in restrictions, and building 1 will not be in restrictions.

Return the maximum possible height of the tallest building.



Example 1:


Input: n = 5, restrictions = [[2,1],[4,1]]
Output: 2
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,1,2], and the tallest building has a height of 2.
Example 2:


Input: n = 6, restrictions = []
Output: 5
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,4,5], and the tallest building has a height of 5.
Example 3:


Input: n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
Output: 5
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,3,4,4,5,4,3], and the tallest building has a height of 5.


Constraints:

2 <= n <= 10^9
0 <= restrictions.length <= min(n - 1, 10^5)
2 <= idi <= n
idi is unique.
0 <= maxHeighti <= 10^9
"""
from typing import List

"""
Two Pass

因为相邻两个building高度差不超过1，第一个building高度是0，所以要最大化最大高度，那从最高building往左应该是逐步递减高度，同时每个building A[i][0]高度还必须<=A[i][1]

首先从左往右，building A[i+1] 高度不超过A[i+1][1]，同时和左边building高度差不超过1，所以不超过A[i][1]+A[i][0]-A[i-1][0]，则可以更新A[i+1][1]=min(A[i+1][1], A[i][1]+A[i][0]-A[i-1][0])，即所有building高度限制是在45 Deg斜线以下

    2    2
  2   1   
1 2 3 4  5

同理从右边可以往左边逐步更新A[i][1] = A[i+1][1]+1，这些限制都是一条条-135 Degree 斜线

任何在A[i],A[j]之间building高度不能超过这两条斜线(A[i] y=x+b1 and A[j] y=-x+b2)中的任何一条

left end side restriction is y=x+b1, where when x=A[i][0], y = A[i][1] => b1=A[i][1]-A[i][0] => y = x + A[i][1]-A[i][0]
right end side restriction is y=-x+b2, with X=A[j][0] and y=A[j][1] => b2= A[j][1]+A[j][0] => y = -x+A[j][1]+A[j][0]

the cross of these two lines are:

y = x  + A[i][1]-A[i][0] (y=x+b1)
y = -x + A[j][1]+A[j][0] (y=-x+b2)

=> this two line intersects at x=(b1-b2)/2, and y=(b1+b2)/2
max height between A[i] and A[j] is (A[i][1]-A[i][0] + A[j][1]+A[j][0])/2
also need to make sure x is within A[i] and A[j] (but this is guaranteed once we already updated restriction A from both left and right)

线性规划

mistakes:
1. building is 1 indexed
2. restrictions are not sorted

"""


class Solution:
    def maxBuilding(self, n: int, A: List[List[int]]) -> int:
        # add building 1
        A = [[1, 0]] + A
        # add building n's height restriction (from building 0) if not in already, it should be <= n-1
        if A[-1][0] != n:
            A.append([n, n - 1])

        # sort height restriction by building restriction
        A.sort()

        m = len(A)

        # from left to right, apply restriction to height
        for i in range(1, m):
            distance = A[i][0] - A[i - 1][0]
            A[i][1] = min(A[i][1], A[i - 1][1] + distance)

        # from right to left, apply restriction to height
        for i in range(m - 2, -1, -1):
            distance = A[i + 1][0] - A[i][0]
            A[i][1] = min(A[i][1], A[i + 1][1] + distance)

        # print('A=%s' % A)
        # 3. Take adjacent pairs into height consideration.
        ans = 0
        # any building at between i, j the height should be restricted by two slopes
        # and height is achieved at the intersection of the two restriction slopes
        for i in range(0, m - 1):
            l, h1 = A[i]
            r, h2 = A[i + 1]
            distance = r - l
            # Max possible height is also determined by the distance, achieved as  (h1+h2+distance)//2
            # at the intersection of the two restriction lines (left restriction y=x+A[i][1]-A[i][0], right restriction y=-x+A[i][1]+A[i][0])
            even_height = (h1 + h2 + distance) // 2
            ans = max(ans, even_height)
            # print('i=%s ans=%s' % (i, ans))

        return ans


def main():
    sol = Solution()

    assert sol.maxBuilding(n = 5, A = [[2,1],[4,1]]) == 2, 'fails'

    assert sol.maxBuilding(n = 6, A = []) == 0, 'fails'

    assert sol.maxBuilding(n = 10, A = [[5,3],[2,5],[7,4],[10,3]]) == 5, 'fails'

if __name__ == '__main__':
   main()