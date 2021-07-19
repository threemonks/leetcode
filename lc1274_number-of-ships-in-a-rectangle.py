"""
1274. Number of Ships in a Rectangle
Hard

192

29

Add to List

Share
(This problem is an interactive problem.)

Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true If there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.



Example :



Input:
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
Output: 3
Explanation: From [0,0] to [4,4] we can count 3 ships within the range.


Constraints:

On the input ships is only given to initialize the map internally. You must solve this problem "blindfolded". In other words, you must find the answer using the given hasShips API, without knowing the ships position.
0 <= bottomLeft[0] <= topRight[0] <= 1000
0 <= bottomLeft[1] <= topRight[1] <= 1000
topRight != bottomLeft
"""
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        return True

class Point(object):
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

"""
for each such rectangle, divide into four smaller rectangles, and recursively calculate
base case is when it reduces to a single point, then hasShips()==True => ship count = 1

mistakes:
1. points on overlapping edges need to be considered exactly once
2. base case when topRight == bottomLeft: return hasShips()
"""


class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        ans = 0
        x1, y1 = bottomLeft.x, bottomLeft.y
        x2, y2 = topRight.x, topRight.y
        if x1 == x2 and y1 == y2:
            return sea.hasShips(topRight, bottomLeft)
        midx = (x1 + x2) // 2
        midy = (y1 + y2) // 2
        # check box 1
        if sea.hasShips(Point(midx, midy), Point(x1, y1)):
            ans += self.countShips(sea, Point(midx, midy), Point(x1, y1))
        # check box 2
        if midx + 1 <= x2 and sea.hasShips(Point(x2, midy), Point(midx + 1, y1)):
            ans += self.countShips(sea, Point(x2, midy), Point(midx + 1, y1))
        # check box 3
        if midy + 1 <= y2 and sea.hasShips(Point(midx, y2), Point(x1, midy + 1)):
            ans += self.countShips(sea, Point(midx, y2), Point(x1, midy + 1))
        # check box 4
        if midx + 1 <= x2 and midy + 1 <= y2 and sea.hasShips(Point(x2, y2), Point(midx + 1, midy + 1)):
            ans += self.countShips(sea, Point(x2, y2), Point(midx + 1, midy + 1))

        return ans
