"""
391. Perfect Rectangle
Hard

"""
import math
from collections import defaultdict
from typing import List

"""
Math

we basically check the following two conditions to conclude all rectangles together make a perfect rectangle
1. area of all rectangles adds together to total area defined by min x1, max x2, min y1, max y2
2. all corners should appear even number of times (except for four outer most corners, which should appear just once)

"""


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        events = []

        minx, miny, maxx, maxy = math.inf, math.inf, -math.inf, -math.inf

        for x1, y1, x2, y2 in rectangles:
            minx = min(minx, x1)
            maxx = max(maxx, x2)
            miny = min(miny, y1)
            maxy = max(maxy, y2)

        total_area = (maxx - minx) * (maxy - miny)

        corners = defaultdict(int)
        out_corners = set([(minx, miny), (maxx, maxy), (minx, maxy), (maxx, miny)])
        # print(out_corners)

        area = 0
        for x1, y1, x2, y2 in rectangles:
            corners[(x1, y1)] += 1
            corners[(x2, y2)] += 1
            corners[(x1, y2)] += 1
            corners[(x2, y1)] += 1
            area += (x2 - x1) * (y2 - y1)

        for key, val in corners.items():
            if key in out_corners and val != 1:
                print('False due to outcorners key=%s val=%s' % (key, val))
                return False
            elif key not in out_corners and val % 2 != 0:
                print('False due to innercorner key=%s val=%s' % (key, val))
                return False

        return total_area == area


def main():
    sol = Solution()
    assert sol.isRectangleCover(rectangles = [ [1,1,3,3], [3,1,4,2], [3,2,4,4], [1,3,2,4], [2,3,3,4] ]) is True, 'fails'

    assert sol.isRectangleCover(rectangles = [ [1,1,2,3], [1,3,2,4], [3,1,4,2], [3,2,4,4] ]) is False, 'fails'

    assert sol.isRectangleCover(rectangles = [ [1,1,3,3], [3,1,4,2], [1,3,2,4], [3,2,4,4] ]) is False, 'fails'

    assert sol.isRectangleCover(rectangles = [ [1,1,3,3], [3,1,4,2], [1,3,2,4], [2,2,4,4] ]) is False, 'fails'

if __name__ == '__main__':
   main()