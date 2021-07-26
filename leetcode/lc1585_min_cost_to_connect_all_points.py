"""
1584. Min Cost to Connect All Points
Medium

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
Example 3:

Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4
Example 4:

Input: points = [[-1000000,-1000000],[1000000,1000000]]
Output: 4000000
Example 5:

Input: points = [[0,0]]
Output: 0


Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
"""
import math
from typing import List

"""
MST Prim
connecting each pair of points with weighted edge, the weight is the manhattan distance

MST dense graph using Prim naive implementation (稠密图用Prim naive)

time O(V^2)

"""


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        visited = set()
        distance = [math.inf for _ in range(n)]  # 已知连通分量到未连通点的最小距离
        distance[0] = 0  # 初始连通分量是空，到顶点0的距离是0
        for i in range(n):
            nxt = -1  # next cloest node to visit, start with value -1, loop through all unvisited nodes to find out
            for j in range(n):  # 在剩余点中找到距离i最小的点
                if j not in visited and (nxt == -1 or distance[j] < distance[nxt]):
                    nxt = j
            visited.add(nxt)  # 记录新找到的距离最近的点

            # now relaxing all distances from visited nodes (connected component) to unknown nodes
            for j in range(n):
                if j not in visited:
                    distance[j] = min(distance[j], matrix[nxt][j])

        return sum(distance)


def main():
    sol = Solution()
    assert sol.minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20, 'fails'

    assert sol.minCostConnectPoints(points = [[3,12],[-2,5],[-4,1]]) == 18, 'fails'

    assert sol.minCostConnectPoints(points = [[0,0],[1,1],[1,0],[-1,1]]) == 4, 'fails'

    assert sol.minCostConnectPoints(points = [[-1000000,-1000000],[1000000,1000000]]) == 4000000, 'fails'

    assert sol.minCostConnectPoints(points = [[0,0]]) == 0, 'fails'



if __name__ == '__main__':
   main()