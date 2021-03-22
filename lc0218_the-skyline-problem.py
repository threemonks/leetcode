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
from sortedcontainers import SortedDict
from collections import defaultdict
from sortedcontainers import SortedDict
from collections import defaultdict

"""
SortedDict

把所有building拆分成左右端点，加入dict，点位置为key，value是list of (起始结束标志,高度)，按key排序。遍历dict，对每个位置点，遇到左端点，高度入栈(count+=1)，遇到右端点，高度出栈(count-=1)，当栈顶高度变化时，新栈顶高度和当前天际线高度比较，如果变化，则天际线添加新节点和新高度。

因为栈需要保存不同building的高度可能相同都需进入，采用SortedDict，计数每个高度的次数
"""


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = defaultdict(list)
        for left, right, height in buildings:
            points[left].append([1, height])  # start, height
            points[right].append([0, height])  # end, height

        skyline = []
        sd = SortedDict()

        for x in sorted(points.keys()):
            for is_start, height in points[x]:
                if is_start:  # start of building, add to heap, and if sd top height changed, add new skyline point
                    if height in sd:
                        sd[height] += 1
                    else:
                        sd[height] = 1
                else:  # end of building, reduce height count by 1 in dict, delete if count drops to 0
                    if height in sd:
                        sd[height] -= 1
                        if sd[height] == 0:
                            del sd[height]
            if not skyline or not sd or sd.peekitem(-1)[0] != skyline[-1][
                1]:  # after the above update with this new building point, check if we have new skyline height
                skyline.append([x, sd.peekitem(-1)[0] if sd else 0])

            # print('x=%s skyline=%s' % (x, skyline))

        return skyline


import heapq

"""
Line Sweep / Heap

排序所有点，遍历所有点
对每一个点，将所有起点在该点之前的building加入堆 (-height,end)
将堆中终结点(end)早于这点的元素删除
如果堆里面的第一个元素高度不等于当前天际线高度，则用这个新高度延长天际线

注：堆在对应一个点加入新的building point和删除已经结束的building point之后，堆首元素高度就是当前天际线高度
"""


class Solution1(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0, 0]]
        q = []  # heap holds (-height, end) for all buildings starts before current point p
        # get all points, and sort
        points = [b[0] for b in buildings] + [b[1] for b in buildings]
        points.sort()
        i = 0
        for p in points:
            print('p=%s' % p)
            # find all buildings who starts before this point, add their (heights*(-1), end) into heap
            while i < len(buildings) and buildings[i][0] == p:
                heapq.heappush(q, (-buildings[i][2], buildings[i][1]))
                print('i=%s buildings[i]=%s' % (i, buildings[i]))
                i += 1
            # remove from queue top all buildings ending before p
            while q and q[0][1] <= p:
                heapq.heappop(q)
            # check queue top for possible new skyline height
            h = -q[0][0] if q else 0
            if h != res[-1][1]:
                res.append([p, h])
        return res[1:]


def main():
    sol = Solution()
    assert sol.getSkyline(buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]) == [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]], 'fails'

    assert sol.getSkyline(buildings = [[0,2,3],[2,5,3]]) == [[0,3],[5,0]], 'fails'



if __name__ == '__main__':
   main()