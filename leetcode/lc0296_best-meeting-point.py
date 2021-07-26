"""
296. Best Meeting Point
Hard

642

51

Add to List

Share
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example 1:

Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 6
Explanation: Given three friends living at (0,0), (0,4), and (2,2).
The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
So return 6.
Example 2:

Input: grid = [[1,1]]
Output: 1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] is either 0 or 1.
There will be at least two friends in the grid.
"""
from typing import List

"""
Brutal Force calculate Manhattan distance

time O(m^2*n^2)
TLE
"""
class Solution0:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        ones = [[i, j] for j in range (n) for i in range(m) if grid[i][j]]

        ans = math.inf

        for i in range(m):
            for j in range(n):
                dist = sum([abs(i-x)+abs(j-y) for x, y in ones])
                if dist < ans:
                    ans = dist
                    print('i=%s j=%s dist=%s' % (i, j, dist))

        return ans

"""
Median / Sort

for 1D, median is the optimal meet point, same is true for 2D, so we find median of two independent 1D arrays, calculate mindistance of each 1D array, and sum the min distances

We can also calculate min distance without knowing the median

time: O(mnlog(mn))
space: O(mn)
"""
class Solution1:
    def min_distance_1d(self, points, origin):
        return sum([abs(p-origin) for p in points])

    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rows, cols = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        cols = sorted(cols)

        row_median = rows[len(rows)//2]
        col_median = cols[len(cols)//2]

        return self.min_distance_1d(rows, row_median) + self.min_distance_1d(cols, col_median)

"""
Collect Coordinates in Sorted Order / Min distance without median
time: O(mn)
space: O(mn)
"""
class Solution:
    def min_distance_1d(self, points):
        # calculate min distances without calculating median
        distance = 0
        n = len(points)
        i, j = 0, n-1
        while i <= j:
            distance += points[j] - points[i]
            i += 1
            j -= 1

        return distance

    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rows= []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)

        cols = []
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    cols.append(j)

        return self.min_distance_1d(rows) + self.min_distance_1d(cols)


def main():
    sol = Solution()
    assert sol.minTotalDistance(grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]) == 6, 'fails'

    assert sol.minTotalDistance(grid = [[1,1]]) == 1, 'fails'


if __name__ == '__main__':
   main()