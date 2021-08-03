"""
286. Walls and Gates
Medium

1753

27

Add to List

Share
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.



Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
Example 3:

Input: rooms = [[2147483647]]
Output: [[2147483647]]
Example 4:

Input: rooms = [[0]]
Output: [[0]]


Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 2^31 - 1.
"""
from typing import List

"""
BFS

start from each room, try to reach any gate, fill it with the shortest value of reaching any gate.

TLE

time O(m*n*(m*n)) - m*n to iterate all empty rooms, and m*n for the BFS of each room as start

"""
from collections import deque


class Solution0:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        INF = 2147483647

        m, n = len(rooms), len(rooms[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == INF:
                    q = deque([[[i, j], 0]])  # (cell, distance)
                    visited = set()
                    shortest_dist = INF
                    while q:
                        cur, dist = q.popleft()
                        x, y = cur
                        if rooms[x][y] == 0:
                            shortest_dist = min(shortest_dist, dist)
                            break

                        for nx, ny in [(x + dx, y + dy) for dx, dy in dirs if 0 <= x + dx < m and 0 <= y + dy < n]:
                            # skip walls
                            if rooms[nx][ny] == -1:
                                continue
                            if (nx, ny) not in visited:
                                q.append([[nx, ny], dist + 1])
                                visited.add((nx, ny))

                    rooms[i][j] = shortest_dist


"""
BFS

start from all gates, try to search empty room with shortest path

time O(m*n)

"""


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        EMPTY = 2147483647
        GATE = 0
        WALL = -1

        m, n = len(rooms), len(rooms[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        q = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == GATE:
                    q.append([[i, j], 0])

        while q:
            cur, dist = q.popleft()
            x, y = cur

            for nx, ny in [(x + dx, y + dy) for dx, dy in dirs if 0 <= x + dx < m and 0 <= y + dy < n]:
                # skip walls
                if rooms[nx][ny] != EMPTY:
                    continue
                rooms[nx][ny] = dist + 1
                q.append([[nx, ny], dist + 1])

        return rooms

def main():
    sol = Solution()
    rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    sol.wallsAndGates(rooms = rooms)
    assert rooms == [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]], 'fails'

if __name__ == '__main__':
   main()