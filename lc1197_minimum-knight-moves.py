"""
1197. Minimum Knight Moves
Medium

In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]


Constraints:

|x| + |y| <= 300

"""
from collections import deque
from functools import lru_cache

"""
BFS

time O(XY)
space O(XY)
"""
class Solution0:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0

        dirs = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]

        visited = set((0, 0))

        q = deque([(0, 0, 0)]) # x, y, steps

        while q:
            cx, cy, step = q.popleft()
            for nx, ny in [(cx+dx, cy+dy) for dx, dy in dirs]:
                if (nx, ny) in visited:
                    continue
                if nx == x and ny == y:
                    return step+1
                q.append((nx, ny, step+1))
                visited.add((nx, ny))

"""
BFS

if we observe that the move is symmetric in four quadrants, we can just store the min moves to get to (0,0), (0,1), (1, 0), (1,1),(1, 2) and (2, 1)

time O(XY)
space O(XY)
"""
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0

        @lru_cache(None)
        def dfs(i, j):
            i = abs(i) # symmetric, it takes same number of steps to get to 1,2 of -1,-2
            j = abs(j)
            if i == 0 and j == 0: # starting point
                return 0
            elif (i==0 and j==1) or (i==1 and j==0): # we need minimal 3 steps to get to 0, 1 from 0, 0
                return 3
            elif i == 1 and j == 1:
                return 2
            elif (i==1 and j==2) or (i==2 and j==1):
                return 1
            else:
                return min(dfs(i-1, j-2), dfs(i-2, j-1))+1

        return dfs(x, y)

def main():
    sol = Solution()
    assert sol.minKnightMoves(x = 2, y = 1) == 1, 'fails'

    assert sol.minKnightMoves(x = 5, y = 5) == 4, 'fails'

if __name__ == '__main__':
   main()