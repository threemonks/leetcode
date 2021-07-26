"""
452. Minimum Number of Arrows to Burst Balloons
Medium
"""
from collections import deque
from typing import List

"""
Interval Sweepline

1. sort points by end time
2. shoot arrow at end of current interval (greedy), and any intervals/balloon who covers this position will be bursted
3. move arrow to end time of first balloon in remaining lists, and repeat

Note:

Greedy problems usually look like "Find minimum number of something to do something" or "Find maximum number of something to fit in some conditions", and typically propose an unsorted input.

The idea of greedy algorithm is to pick the locally optimal move at each step, that will lead to the globally optimal solution.

"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points = sorted(points, key=lambda x: x[1])
        points = deque(points)

        count = 0
        arrow = points[0][0]  # current arrow position
        while points:
            arrow = points[0][1]
            # print('arrow=%s' % arrow)
            while points and points[0][0] <= arrow <= points[0][1]:
                points.popleft()
            count += 1

        return count


def main():
    sol = Solution()
    assert sol.findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]) == 2, 'fails'

    assert sol.findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]]) == 4, 'fails'

    assert sol.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]]) == 2, 'fails'

    assert sol.findMinArrowShots(points = [[1,2]]) == 1, 'fails'



if __name__ == '__main__':
   main()