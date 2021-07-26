"""
1878. Get Biggest Three Rhombus Sums in a Grid
Medium

12

60

Add to List

Share
You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:


Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.



Example 1:


Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211
Example 2:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [20,9,8]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)
Example 3:

Input: grid = [[7,7,7]]
Output: [7]
Explanation: All three possible rhombus sums are the same, so return [7].


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
1 <= grid[i][j] <= 10^5
"""
import heapq
from typing import List

"""
Math

1. iterate through each cell for (row, col), use it as center to construct a rhombus of edge length 1, 2, ..., int(sqrt(m**2+n**2))
2. to calculate sum of an edge of rhombus, we can calculate prefixsum along a diagonal line, to reduce the sum from O(N) to O(1)

for rhombus cenetered at (i, j) with radius k, its four vertex are
         (i-k, j)
        /        \
(i, j-k)          (i, j+k)
        \        /
         (i+k, j)

we will need to summarize all nums along its four edges on 45-diagonal and 135 diagonal, and return top 3 uniq sums

"""


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        # print('m=%s n=%s' % (m, n))

        sums = []

        for i in range(m):  # row
            for j in range(n):  # column
                # print('i=%s j=%s grid[i][j]=%s' % (i, j, grid[i][j]))

                # rhombus of radius 0
                heapq.heappush(sums, -grid[i][j])

                # maximum radius of the rhombus
                r = min(i, j, m - 1 - i, n - 1 - j)
                if r <= 0:  # only explore out if there's valid radius range to explore
                    continue

                for k in range(1, r + 1):
                    cursum = 0
                    # now consider rhombus of radius k, centered at (i, j)
                    # its four vertex is (i-k, j), (i+k, j), (i, j-k), (i, j+k)
                    # and we need to sum all numbers between each of the two vertex in 45-diagonal and 135-diagonal
                    # (i, j-k) to (i-k, j)
                    x, y = i, j - k
                    while x >= i - k and y <= j:
                        cursum += grid[x][y]
                        x -= 1
                        y += 1

                    # (i+k, j) to (i, j+k)
                    x, y = i + k, j
                    while x >= i and y <= j + k:
                        cursum += grid[x][y]
                        x -= 1
                        y += 1

                    # (i, j-k) to (i+k, j) # needs to exclude the vertex
                    x, y = i + 1, j - k + 1
                    while x <= i + k - 1 and y <= j - 1:
                        cursum += grid[x][y]
                        x += 1
                        y += 1

                    # (i-k, j) to (i, j+k) # needs to exclude the vertex
                    x, y = i - k + 1, j + 1
                    while x <= i - 1 and y <= j + k - 1:
                        cursum += grid[x][y]
                        x += 1
                        y += 1

                    # print('i=%s j=%s k=%s cursum=%s' % (i, j, k, cursum))

                    heapq.heappush(sums, -cursum)

        # print(sorted(sums))
        ans = set()
        while len(ans) < 3 and len(sums):
            ans.add(-heapq.heappop(sums))

        return sorted(list(ans), reverse=True)

def main():
    sol = Solution()

    assert sol.getBiggestThree(grid = [[20, 17, 9, 13, 5, 2, 9, 1, 5], [14, 9, 9, 9, 16, 18, 3, 4, 12], [18, 15, 10, 20, 19, 20, 15, 12, 11], [19, 16, 19, 18, 8, 13, 15, 14, 11], [4, 19, 5, 2, 19, 17, 7, 2, 2]]) == [107,103,102], 'fails'

    assert sol.getBiggestThree(grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]) == [228,216,211], 'fails'

    assert sol.getBiggestThree(grid = [[1,2,3],[4,5,6],[7,8,9]]) == [20,9,8], 'fails'

    assert sol.getBiggestThree(grid = [[7,7,7]]) == [7], 'fails'

if __name__ == '__main__':
   main()