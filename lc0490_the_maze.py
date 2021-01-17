"""
490. The Maze
Medium

There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).



Example 1:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
Example 2:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
Example 3:

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: false


Constraints:

1 <= maze.length, maze[i].length <= 100
maze[i][j] is 0 or 1.
start.length == 2
destination.length == 2
0 <= startrow, destinationrow <= maze.length
0 <= startcol, destinationcol <= maze[i].length
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The maze contains at least 2 empty spaces.
"""

from typing import List
import collections

"""
BFS

time O(m*n)
space O(m*n)
"""
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        q = collections.deque()

        q.append(tuple(start))

        visited = set()

        while q:
            cur = q.popleft()

            if cur == tuple(destination):
                return True

            if cur in visited:
                continue
            else:
                visited.add(cur)
            neighbors = []

            # north
            i = cur[0]
            j = cur[1]
            while i >= 0 and maze[i][j] == 0:
                i -= 1
            neighbors.append((i + 1, j))

            # south
            i = cur[0]
            j = cur[1]
            while i < m and maze[i][j] == 0:
                i += 1
            neighbors.append((i - 1, j))

            # west
            i = cur[0]
            j = cur[1]
            while j >= 0 and maze[i][j] == 0:
                j -= 1
            neighbors.append((i, j + 1))

            # east
            i = cur[0]
            j = cur[1]
            while j < n and maze[i][j] == 0:
                j += 1
            neighbors.append((i, j - 1))

            for nei in neighbors:
                q.append(nei)

        return False

def main():
    sol = Solution()
    sol.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]) is True, 'fails'

    sol.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]) is False, 'fails'

    sol.hasPath(maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]) is False, 'fails'

if __name__ == '__main__':
   main()