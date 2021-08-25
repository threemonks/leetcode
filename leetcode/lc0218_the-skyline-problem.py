"""
218. The Skyline Problem
Hard

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

Example 1:

Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]


Constraints:

1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildings is sorted by lefti in non-decreasing order.

https://leetcode.com/problems/the-skyline-problem/

"""
from typing import List

from sortedcontainers import SortedDict
from collections import defaultdict
from sortedcontainers import SortedDict
from collections import defaultdict

"""
Line Sweep SortedDict {height: count of this height}

iterate through all points, at each point, for start, increase the count of this height in SortedDict (count+=1), for end point, decrease the count of this height in SortedDict, and delete such height if its count reduces to 0, for each such operation, if the tallest height in the dict changes, we have a new skyline

mistakes:
1. points should be stored using dict(list), because we must process all heights at a given point, then update skyline
   we cannot process each (point, height) and update skyline.

time O(N) # N - total number of points
"""

from sortedcontainers import SortedDict
class Solution0:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = defaultdict(list) # [point, start/end flag, height]

        for start, end, height in buildings:
            points[start].append([1, height])
            points[end].append([0, height])

        sd = SortedDict()

        skyline = []
        for x in sorted(points.keys()):
            for is_start, height in points[x]:
                if is_start == 1: # start building height
                    if height in sd:
                        sd[height] += 1
                    else:
                        sd[height] = 1
                elif is_start == 0: # end of building height
                    sd[height] -= 1
                    if sd[height] == 0:
                        del sd[height]

            if not skyline or not sd or skyline[-1][1] != sd.peekitem(-1)[0]: # new tallest height in sd different from output
                skyline.append([x, sd.peekitem(-1)[0] if sd else 0])

        return skyline

"""

Line Sweep / Heap [-height, end]

sort all nodes, for each node, add all building starts before it into priorityqueue, (-height, end)
remove all nodes from priorityqueue whose end point is ealier than this node.

Note that in order to ad all buildings starts before this node, we need to sort buildings, use a pointer to iterate it along with points, so that it does not increase time complexity of the entire program.

if height of node at top of priorityqueue is different from current skyline height, that is a new skyline

note: 

排序所有点，遍历所有点
对每一个点，将所有起点在该点之前的building加入堆 (-height,end)
将堆中终结点(end)早于这点的元素删除
如果堆里面的第一个元素高度不等于当前天际线高度，则用这个新高度延长天际线

注：堆在对应一个点加入新的building point和删除已经结束的building point之后，堆首元素高度就是当前天际线高度
"""
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # buildings = sorted(buildings) # already sorted
        points = [b[0] for b in buildings] + [b[1] for b in buildings]

        points.sort()

        pq = [] # priorityqueue holding (height, end)
        i = 0 # pointer to indicate all buildings up to this index has been pushed into pq
        skyline = []
        for p in points:
            # put heights of all buildings who starting point is before x into pq
            while i < len(buildings) and buildings[i][0] <= p:
                heapq.heappush(pq, [-buildings[i][2], buildings[i][1]])
                i += 1
            # remove any node from top of priorityqueue whose end point is already past
            while pq and pq[0][1] <= p:
                heapq.heappop(pq)
            # now the height in top of pq is the new skyline height, is this a new height?
            h = -pq[0][0] if pq else 0
            if len(skyline) == 0 or h != skyline[-1][1]:
                skyline.append([p, h])

        return skyline


def main():
    sol = Solution()
    assert sol.getSkyline(buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]) == [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]], 'fails'

    assert sol.getSkyline(buildings = [[0,2,3],[2,5,3]]) == [[0,3],[5,0]], 'fails'



if __name__ == '__main__':
   main()