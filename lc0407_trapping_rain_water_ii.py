"""
407. Trapping Rain Water II
Hard

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.


The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.

After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

Constraints:

1 <= m, n <= 110
0 <= heightMap[i][j] <= 20000
"""
"""
following trapping rain water I, where we find leftmax and rightmax for a given point i, the water this point can hold is min(leftmax, rightmax) - height[i]

we would extend this to a 2D situation,  so the water that can be held by any point i is min(all bounaries of this point) - height[i]

we start with all four borders as the lake borders, store them into a minheap, so each time we proceed with the lowest border point, to explore its neighbor points (and recursively explore their neighbor points to for a connected inner lake if possible):
  1. if the neighbor point is lower than lowest border, it becomes part of the inner lake and can hold water
     we also add this new inner lake point to the queue for inner lake to continue explore their neighbor points to expand the inner lake if possible
  2. if the neighbor point is higher than lowest border, then it becomes part of the border (replacing the previous lowest border height), we add it to the border minheap by popping the existing lowest border height

time O(mn*log(mn)) - every node is pushed into minheap and popped out  exeactly once

"""
import heapq
import collections


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])

        border = []  # minheap queue to hold boundaries
        visited = set()
        for i in range(m):
            border.append((heightMap[i][0], i, 0))
            visited.add((i, 0))
            border.append((heightMap[i][n - 1], i, n - 1))
            visited.add((i, n - 1))

        for j in range(1, n - 1):
            border.append((heightMap[0][j], 0, j))
            visited.add((0, j))
            border.append((heightMap[m - 1][j], m - 1, j))
            visited.add((m - 1, j))

        # print('visited=%s' % visited)
        # print('border=%s' % border)
        heapq.heapify(border)

        ans = 0

        while border:
            lowest, bx, by = heapq.heappop(border)

            # using BFS to recursively explore all neighbors of (i, j) and connected inner lake
            # if higher, add to border heapq
            # if lower, then it will become part of inner lake and hold water, and add to inner lake point queue to further explore its neighbor points
            q = collections.deque([(bx, by)])  # queue to hold points to explore for inner lake

            while q:
                i, j = q.popleft()

                neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for nei in neighbors:
                    nx, ny = nei
                    if nx < 0 or nx > m - 1 or ny < 0 or ny > n - 1 or (nx, ny) in visited:
                        continue
                    # print('nx=%s ny=%s q=%s' % (nx, ny, q))
                    if heightMap[nx][ny] < lowest:
                        # calculate water
                        ans += lowest - heightMap[nx][ny]
                        # print('water=%s' % (lowest - heightMap[nx][ny]))
                        q.append((nx, ny))
                        visited.add((nx, ny))
                    else:  # add this into border queue
                        heapq.heappush(border, (heightMap[nx][ny], nx, ny))
                        visited.add((nx, ny))

        return ans


def main():
    sol = Solution()
    assert sol.trapRainWater([ [1,4,3,1,3,2], [3,2,1,3,2,4], [2,3,3,2,3,1] ]) == 4, 'fails'

if __name__ == '__main__':
   main()