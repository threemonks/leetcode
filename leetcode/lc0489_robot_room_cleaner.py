"""
489. Robot Room Cleaner
Hard

1310

78

Add to List

Share
Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.

When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.

Design an algorithm to clean the entire room using only the 4 given APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Example:

Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3

Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
Notes:

The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the mentioned 4 APIs, without knowing the room layout and the initial robot's position.
The robot's initial position will always be in an accessible cell.
The initial direction of the robot will be facing up.
All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
Assume all four edges of the grid are all surrounded by wall.
"""
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """
       pass

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       pass

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       pass

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """
       pass

"""
DFS

1. for each new cell, check if it is cleaned, if cleaned, return. else, clean, and mark it as cleaned
   explore all four directions of this cell
2. for each dir, if the next cell is not cleaned and not wall, call dfs on it, after dfs call, backtrack robot to previous position and direction by doing 5 steps: turnRight, turnRight, move, turnRight, turnRight
3. explore next direction by turnRight and repeat 2
4. explore next direction by turnRight and repeat 2
5. explore next direction by turnRight and repeat 2

"""


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()

        def dfs(x, y, d, robot):
            """
            :type x: int
            :type y: int
            :type dir: int (0: east, 1: south, 2: west, 3: north)
            :type robot: Robot
            :rtype: None
            """
            nonlocal visited

            if (x, y) in visited:
                return

            robot.clean()
            visited.add((x, y))

            # currently facing d, we want to iterate and process all four dirs (0 east, 1 south, 2 west, 3 noth)
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for k in range(4):
                newdir = (d + k) % 4
                newx = x + directions[newdir][0]
                newy = y + directions[newdir][1]

                # if this new cell is not cleaned and is not wall, call dfs on it
                if ((newx, newy) not in visited and robot.move()):
                    dfs(newx, newy, newdir, robot)
                    # backtrack/reset to previous location and direction
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()

                # after finish, turn right to process next direction
                robot.turnRight()

        dfs(0, 0, 0, robot)

def main():
    sol = Solution()
    sol.cleanRoom(robot=Robot())

if __name__ == '__main__':
   main()