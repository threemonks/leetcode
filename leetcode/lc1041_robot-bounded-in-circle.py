"""
1041. Robot Bounded In Circle
Medium

1457

395

Add to List

Share
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.



Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...


Constraints:

1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.
"""
"""
bounded in circle only if after all instrucitons, no position move, or change direction
use 0, 1, 2, 3 represents direction North, east, south, west
use modulo % to cycle through directions

accumulate all moves and turns, and we won't go infiintely far as long as moves=0 or turn > 0

"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        dx = 0  # horizontal move steps
        dy = 0  # vertical move steps
        dr = 0  # 0=N, 1=E, 2=S, 3=W

        for c in instructions:
            if c == 'G':
                if dr == 0:
                    dy += 1
                elif dr == 1:
                    dx += 1
                elif dr == 2:
                    dy -= 1
                else:  # dr == 3
                    dx -= 1
            elif c == 'L':
                dr = (dr - 1 + 4) % 4
            else:  # c == 'R'
                dr = (dr + 1) % 4

        return (dx == 0 and dy == 0) or dr != 0


def main():
    sol = Solution()
    assert sol.isRobotBounded(instructions = "GGLLGG") == True, 'fails'

    assert sol.isRobotBounded(instructions = "GG") == False, 'fails'

    assert sol.isRobotBounded(instructions = "GL") == True, 'fails'


if __name__ == '__main__':
   main()