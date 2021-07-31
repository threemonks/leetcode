"""
149. Max Points on a Line
Hard

360

82

Add to List

Share
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.



Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4


Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""
from typing import List

"""
Math

calculate all 300*300 lines, represented by the two points, store in dict, and check if any other points are on these lines by checking same slope (use multiplication instead of division)

notes:
1. special case n<=2

"""
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        points = sorted(points)  # sort to speed up

        lines = dict()

        for i in range(n):
            for j in range(i + 1, n):
                lines[(i, j)] = [i, j]

        line_points = defaultdict(int)
        for line in lines:
            p0, p1 = line[0], line[1]
            for k in range(n):
                if (points[k][0] - points[p0][0]) * (points[k][1] - points[p1][1]) == (points[k][0] - points[p1][0]) * (
                        points[k][1] - points[p0][1]):
                    line_points[line] += 1

        return max(line_points.values())


class Solution1:
    def maxPoints(self, points):
        l = len(points)
        m = 0
        for i in range(l):
            dic = {'i': 1}
            same = 0
            for j in range(i + 1, l):
                tx, ty = points[j][0], points[j][1]
                if tx == points[i][0] and ty == points[i][1]:
                    same += 1
                    continue
                if points[i][0] == tx:
                    slope = 'i'
                else:
                    slope = (points[i][1] - ty) * 1.0 / (points[i][0] - tx)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)
        return m


def main():
    sol = Solution()
    assert sol.maxPoints(points = [[1,1],[2,2],[3,3]]) == 3, 'fails'

    assert sol.maxPoints(points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4, 'fails'

if __name__ == '__main__':
   main()