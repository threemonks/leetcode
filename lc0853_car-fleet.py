"""
853. Car Fleet
Medium

N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?



Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Note:

0 <= N <= 10 ^ 4
0 < target <= 10 ^ 6
0 < speed[i] <= 10 ^ 6
0 <= position[i] < target
All initial positions are different.

"""
from typing import List

"""
sort by initial position, start from right most car to left, calculate each car's time to reach target
if the car to left would arrive at target than the one on right, it will catch up and become a fleet, and the arrial time of the fleet will be that of the previous slower car.

steps:
1. sort all cars by initial positions
2. iterate all cars from right to left, 
3. for a given car, calculate its time to arrive at target, a car to left with shorter arrival time will join the one on right and become a fleet
4. the fleet will have the slower front car's arrival time
5. if the car to left has slower (longer) arrival time, it will become a new fleet as it wont catch up with previous car
6. repeat 3 to 5

time O(N)
"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = zip(position, speed)
        cars = sorted(cars, key=lambda x: x[0])

        # current fleet speed, faster car will join it (if time allows before it reachs target)
        # only slower car on left will form new fleet
        arrival_time = 0  # arrival time of fleet in front
        ans = 0
        for i in range(n - 1, -1, -1):
            car, speed = cars[i][0], cars[i][1]
            if i == n - 1:
                arrival_time = (target - cars[i][0]) / cars[i][1]
                ans += 1
            else:
                # this car will join next car if it is faster, and catch up before next car reach target
                if (target - cars[i][0]) / cars[i][1] > arrival_time:
                    arrival_time = (target - cars[i][0]) / cars[i][1]
                    ans += 1
                else:
                    pass

        return ans


def main():
    sol = Solution()
    assert sol.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]) == 3, 'fails'


if __name__ == '__main__':
   main()