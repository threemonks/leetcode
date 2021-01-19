"""
778. Swim in Rising Water
Hard

On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].

"""

from typing import List
import heapq
import collections

"""
Dijkstra's algorithm where the distance between two vertices is the maximum of the two vertices' values.

time O(N^2*log(N))
space O(N^2)
"""

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        q = [(grid[0][0], (0, 0))] # node, and elevation of this node
        heapq.heapify(q)
        visited = set()
        visited.add((0, 0))

        res = 0

        while q:
            # print('q=%s' % q)
            t, cur = heapq.heappop(q)
            res = max(res, t)
            if cur == (n-1, n-1):
                return res
            # print('cur=%s t=%s res=%s' % (cur, t, res))
            i, j = cur
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for nei in neighbors:
                ni, nj = nei
                if ni < 0 or ni >= n or nj < 0 or nj >= n or nei in visited:
                    continue
                heapq.heappush(q, (grid[ni][nj], (ni, nj)))
                visited.add(nei)

        return res

"""
use similar idea as 407 trapping rain water ii

we can think this as sea water rises, goes from start node (0, 0) , through the lowest height around its neighbors (we use a minheap to keep all its neighbor barriers, so we can always proceed the lowest point first), and once it gets through this lowest point, we recursively explore all neighbors to see where the water can go to (use deque to keep track of all points that we want to further explore neighbors on), if new point with higher height, it becomes of part of the barrier that water level needs to raise above to pass, we push it into the minheap queue, if new point with lower height, it becomes part of the inner lake where water can flow into, we push it into deque to further explore.

If the end point (n-1, n-1) is encountered, then the current water level is the answer

"""

class Solution1:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        minq = [(grid[0][0], 0, 0)] # store all nodes that together are blocking water from (0, 0) to (n-1, n-1), elevation of this node, node coordinations
        heapq.heapify(minq)
        visited = set()
        visited.add((0, 0))

        t = 0 # sea water level starts at 0

        while minq:
            h, x, y = heapq.heappop(minq) # lowest point the water from outside sea (0, 0) can go through
            t = h
            if x == n-1 and y == n-1: # destination point reaced, return current water level
                return t
            queue = collections.deque()
            queue.append((x, y))
            while queue: # explore all nodes the water from the lowest point can then go into
                xx, yy = queue.popleft()
                neighbors = [(xx-1, yy), (xx+1, yy), (xx, yy-1), (xx, yy+1)]
                for nei in neighbors:
                    nx, ny = nei[0], nei[1]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n: # exceeding boundary
                        continue
                    if nei in visited: # skip visited
                        continue
                    if grid[nx][ny] > t: # higher neighbors, this is part of the barrier that water from start point (0, 0) needs to get through to flow to end point
                        heapq.heappush(minq, (grid[nx][ny], nx, ny))
                        visited.add((nx, ny))
                    else: # lower neighbors, water can flow into
                        if (nx == n-1 and ny == n-1): # destination point reaced, return current water level
                            return t
                        queue.append((nx, ny))
                        visited.add((nx, ny))

        return -1


"""
Minimal Spanning Tree algorithm / Union-Find

- note we are not finding the entire spanning tree, rather only to find spanning that connect starting and ending points

Disjoint-Set (Union Find) using Kruskal's algorithm with some modification
 * consider each cell in the grid as a node in a graph, and the value in the cell represents its weight
 * sort the cells based on their weights, in ascending order
 * iterate through the sorted cells
   i) at each iteration, we add neighbor cells around the current cell to the spanning tree
   ii) at any moment, if we find the starting and ending points are connected thanks to the newly added nodes, we exit the loop. And the weight of the current cell would be the minimal waiting time, before we complete the spanning tree

time O(N^2*log(N^2))
"""
class Solution2:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        size = [[1]*n for _ in range(n)]
        visited = [[0]*n for _ in range(n)]
        root = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                root[i][j] = (i, j)
        positions = sorted([(i, j) for i in range(n) for j in range(n)], key=lambda x:grid[x[0]][x[1]])

        # find parent/representative of the set
        def parent(x, y):
            while root[x][y][0] != x or root[x][y][1] != y:
                root[x][y]= root[root[x][y][0]][root[x][y][1]]
                x, y = root[x][y][0], root[x][y][1]
            return (x, y)

        def union(i, j, x, y):
            pij = parent(i, j)
            pxy = parent(x, y)
            if pij != pxy:
                if size[pij[0]][pij[1]] > size[pxy[0]][pxy[1]]: #
                    pxy, pij = pij, pxy
                size[pxy[0]][pxy[1]] += size[pij[0]][pij[1]]
                root[pij[0]][pij[1]] = list(pxy)

        for i, j in positions:
            visited[i][j] = True
            # explore neighbors to grow the disjoint sets
            print('i=%s j=%s parent=%s' % (i, j, parent(i, j)))
            for x,y in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if 0<=x and x <n and 0<=y and y < n and visited[x][y]:
                    print('x=%s y=%s parent=%s' % (x, y, parent(x, y)))
                    print('i=%s j=%s x=%s y=%s => union' % (i, j, x, y))
                    union(i, j, x, y)
                    print('after union')
                    print('i=%s j=%s x=%s y=%s parent=%s' % (i, j, x, y, parent(i, j)))

            print('i=%s j=%s' % (i, j))

            # the start and end points are joined together, return the weight as answer
            if parent(0,0) == parent(n-1,n-1):
                print('i=%s j=%s answer found' % (i, j))
                return grid[i][j]

"""
Minimal Spanning Tree algorithm / Union-Find using 1-D array for root and parent/union

"""
class Solution3:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        size = [1]*(n*n)
        visited = [[0]*n for _ in range(n)]
        root = list(range(n*n))
        positions = sorted([(i, j) for i in range(n) for j in range(n)], key=lambda x:grid[x[0]][x[1]])

        # find parent/representative of the set
        def parent(x):
            while root[x]!=x:
                root[x] = root[root[x]]
                x=root[x]
            return x

        def union(x, y):
            px = parent(x)
            py = parent(y)
            if px != py:
                if size[px] > size[py]: # union by rank, attach shorter tree to higher tree
                    px, py = py, px
                size[py] += size[px]
                root[px] = py

        for i, j in positions:
            visited[i][j] = True
            # explore neighbors to grow the disjoint sets
            for x,y in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if 0<=x and x <n and 0<=y and y < n and visited[x][y]:
                    union(i*n+j, x*n+y)

            # the start and end points are joined together, return the weight as answer
            if parent(0) == parent(n*n-1):
                return grid[i][j]
def main():
    sol = Solution()
    assert sol.swimInWater([[0,2],[1,3]]) == 3, 'fails'

    assert sol.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]) == 16, 'fails'


if __name__ == '__main__':
   main()