"""
505. The Maze II
Medium

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.



Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.



Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

"""
from typing import List

"""
BFS

single source shortest path, weighted => Dijkstra's algorithm
the weight is the number of empty spaces the ball would roll until it stops (hit wall or boundary)
"""
import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        q = [(0, tuple(start))]
        heapq.heapify(q)

        visited = set()

        while q:
            # print('q=%s' % q)
            cost, cur = heapq.heappop(q)
            # print('after heappop q=%s' % q)

            if cur == tuple(destination):
                return cost

            if cur in visited:
                continue
            else:
                visited.add(cur)

            # print('cur=%s cost=%s' % (cur, cost))
            neighbors = []

            # north
            i = cur[0]
            j = cur[1]
            while i >= 0 and maze[i][j] == 0:
                i -= 1
            neighbors.append((cost+cur[0]-(i+1), (i+1, j)))

            # south
            i = cur[0]
            j = cur[1]
            while i < m and maze[i][j] == 0:
                i += 1
            neighbors.append((cost+i-1-cur[0], (i-1, j)))

            # west
            i = cur[0]
            j = cur[1]
            while j >= 0 and maze[i][j] == 0:
                j -= 1
            neighbors.append((cost+cur[1]-(j+1), (i, j+1)))

            # east
            i = cur[0]
            j = cur[1]
            while j < n and maze[i][j] == 0:
                j += 1
            neighbors.append((cost+j-1-cur[1], (i, j-1)))

            for nei in neighbors:
                heapq.heappush(q, nei)

        return -1


def main():
    sol = Solution()
    assert sol.shortestDistance(maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], start=[0, 4], destination=[4,4]) == 12, 'fails'

    assert sol.shortestDistance(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], start=[0, 4], destination=[3,2]) == -1, 'fails'

if __name__ == '__main__':
   main()