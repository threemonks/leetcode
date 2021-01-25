"""
499. The Maze III
Hard

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving the shortest distance. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the hole (included). Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.



Example 1:

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: "lul"

Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.
Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".

Example 2:

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (3, 0)

Output: "impossible"

Explanation: The ball cannot reach the hole.



Note:

There is only one ball and one hole in the maze.
Both the ball and hole exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and the width and the height of the maze won't exceed 30.

"""
from typing import List
import heapq

"""
BFS for shortest path
    minheap queue (steps, x, y, path pattern)
    visited[(x, y)] = (steps to get here, path pattern to get here) # so we can get lexicographically smaller paths
Note: 
    1. to find neighbor in each direction, need to keep move in that direction until hit wall or boundary, or hole
    2. 
"""


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m = len(maze)
        n = len(maze[0])

        dirs = [('d', +1, 0), ('l', 0, -1), ('r', 0, +1), ('u', -1, 0)]

        q = [(0, ball[0], ball[1], '')]
        heapq.heapify(q)
        visited = dict() # remember number of steps of shortest path and the path pattern to get here for given node
        visited[tuple(ball)] = (0, "")

        while q:
            steps, r, c, pattern = heapq.heappop(q)
            if [r, c] == hole:
                return pattern
            for direction, dr, dc in dirs:
                nsteps, nr, nc = steps, r, c
                while 0 <= nr+dr < m and 0 <= nc+dc < n and maze[nr+dr][nc+dc] == 0:
                    nr, nc = nr+dr, nc+dc
                    nsteps += 1
                    if [nr, nc] == hole:
                        break
                if (nr, nc) not in visited or (nsteps, pattern+direction) < visited[(nr, nc)]: # not visited, or shorter (or lexicographically smaller) path found
                    heapq.heappush(q, (nsteps, nr, nc, pattern + direction))
                    visited[(nr, nc)] = (nsteps, pattern+direction)

        return "impossible"


def main():
    sol = Solution()
    assert sol.findShortestWay([[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], ball=[4, 3], hole=[0, 1]) == "lul", 'fails'

    assert sol.findShortestWay([[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], ball=[4, 3], hole=[3, 0]) == "impossible", 'fails'


if __name__ == '__main__':
   main()