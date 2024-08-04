"""
[1, 13, 4]
[5, 23, 2]
[9, 19, 6]

Visualization:
          _________
         |         |
  _______|___      |
 |       |   |     |
 |    ___|___|_____|___
 |   |   |   |     |   |
_|___|___|___|_____|___|__
 1   5   9   13    19  23

 (9-1)*4 + (19-9)*6 + (23-19)*2 = 32+60+8 = 100

 [[1, 4]]
 [[-4, 1, 13], [-2, 5, 23], [-6, 9, 19]]
 1. [-4, 1, 13] => height 4
 5  [[-4, 1, 13], [-2, 5, 23]] => height 4
 9  [[-4, 1, 13], [-2, 5, 23], [-6, 9, 19]] => height 6
 13 [[-4, 1, 13], [-2, 5, 23], [-6, 9, 19]] => height 6
 19 [[-2, 5, 23]]
"""
import heapq


def get_area(buildings):
    buildings = sorted(buildings)

    current = []
    ans = 0
    for building in buildings:
        start, end, height = building
        if len(current) > 0 and current[-1][2] < height:
            ans += (current[-1][1] - current[-1][0]) * current[-1][2]
            current.append([start, end, height])
        elif len(current) > 0 and current[-1][2] > height:  # 2
            ans += (current[-1][1] - current[-1][0]) * current[-1][2]
            current.append([max(start, current[-1][1]), end, height])
        else:
            if len(current):
                current.append([start, end, height])
            else:
                current[-1][1] = max(current[-1][1], end)

    return ans
