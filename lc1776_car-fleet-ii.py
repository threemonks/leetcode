"""
1776. Car Fleet II
Hard

There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.



Example 1:

Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.
Example 2:

Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]


Constraints:

1 <= cars.length <= 105
1 <= positioni, speedi <= 106
positioni < positioni+1

"""
import math
from typing import List

"""
Monotonic Stack

Key observation:
1. The collision time for a car won't be affected by the cars on its left. Thus if going from right to left, we can fix the collision time along the way.
2. The collision time for a car will only be affected by the cars on its right. Again among all the cars on current car's right, there are certain cars that won't affect current car's collision time. Namely, if the car has a higher speed than the current car, or, if the car's collision time is earlier than the current car's collision time with this car, then such cars won't affect current car's collision time, and can be ignored. The mono stack should only kept those cars that can possibly affect the current car.

collision time between c1 and c2 (assuming c1[0] < c2[0], i.e., c2 is in front) is calculated as
    (c2-c1)/(s1-s2)

time O(N)

mistakes:
1. car i collides into i+1, then i's position should be updated to i+1's position after that move
"""

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)

        answer = [-1 for _ in range(n)]

        # stores cars that might collide current car, with their position, speed and collision time with next car
        # init with last car, which has no car to right to collide into
        stack = [(cars[-1][0], cars[-1][1], math.inf)]

        for i in range(n - 2, -1, -1):
            pos, speed = cars[i]
            # any car in stack with faster speed, or with a collision time earlier than the potential collision time between that car and current car
            # will have no impact on current car's collision time, therefore could be popped out from stack
            while stack and (speed <= stack[-1][1] or stack[-1][2] <= (stack[-1][0] - pos) / (speed - stack[-1][1])):
                stack.pop()

            # if stack is empty, current car will never collide to next car in front
            if not stack:
                stack.append((pos, speed, math.inf))
            else:
                # now calculate this car's collision time and put it into stack with the collision time
                collide_time = (stack[-1][0] - pos) / (speed - stack[-1][1])
                stack.append((pos, speed, collide_time))
                answer[i] = collide_time

        return answer


def main():
    sol = Solution()
    assert sol.getCollisionTimes(cars = [[1,2],[2,1],[4,3],[7,2]]) == [1.00000,-1.00000,3.00000,-1.00000], 'fails'

    assert sol.getCollisionTimes(cars = [[3,4],[5,4],[6,3],[9,1]]) == [2.00000,1.00000,1.50000,-1.00000], 'fails'


if __name__ == '__main__':
   main()