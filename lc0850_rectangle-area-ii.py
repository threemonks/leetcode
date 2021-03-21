"""
850. Rectangle Area II
Hard
"""
from typing import List

"""
Line Sweep

Imagine we pass a horizontal line from bottom to top over the shape, then there are some active intervals on the horizontal line, which gets updated twice for each rectangle. There will be a total of @^N events, we can update active horizontal intervals for each update.


for each rectangle (x1, y1, x2, y2), consider it as two events, one event at y1 for adding (x1, x2), then a second event at y2 fo removing (x1, x2)
if we can sort active events, then we can query active events list to find out the total active x length we got on this specific y value, multiple this by the difference of this y value and next, we got area covered between these two y values


time O(N^2*log(N))

"""


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        events = list()
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, 0, x1, x2))  # add this x interval event
            events.append((y2, 1, x1, x2))  # remove this x interval event

        events = sorted(events, key=lambda x: x[0])

        def query():
            # calculate total length covered by all interval (might not be continuous)
            covered = 0
            cur = -1  # we have calculated covered length up to this point
            for x1, x2 in active:
                covered += max(0, x2 - max(cur,
                                           x1))  # cur could be bigger than x2, i.e., a shorter interval start at the same time comes later, but ends sooner
                cur = max(cur, x2)

            return covered

        ans = 0

        active = []  # active interval lists
        prev_y = events[0][0]  # prev y value we were at
        for y, action, x1, x2 in events:
            covered = query()
            ans += covered * (y - prev_y)
            # print('ans+=%s' % covered * (y - prev_y))
            # print('y=%s action=%s x1=%s x2=%s prev_y=%s' % (y, action, x1, x2, prev_y))
            if action == 0:
                active.append((x1, x2))
                active.sort()

            elif action == 1:
                active.remove((x1, x2))

            prev_y = y

        return ans % MOD

def main():
    sol = Solution()
    assert sol.rectangleArea(rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]) == 6, 'fails'

    assert sol.rectangleArea([[0,0,1000000000,1000000000]]) == 49, 'fails'

    assert sol.rectangleArea([[49,40,62,100],[11,83,31,99],[19,39,30,99]]) == 1584, 'fails'

if __name__ == '__main__':
   main()