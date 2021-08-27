import math
from typing import List
"""
1094. Car Pooling
Medium

You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
 

Constraints:

trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000

"""
"""
Sort / Simulation
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = []
        for trip in trips:
            locations.append((trip[1], trip[0])) # pessenger on
            locations.append((trip[2], -trip[0])) # pesenger off

        locations = sorted(locations, key=lambda x: (x[0], x[1])) # pessenger off first, then on

        pessenger_count = 0
        for loc, pc in locations:
            pessenger_count += pc
            if pessenger_count > capacity:
                return False

        return True

class Solution1:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = []
        for trip in trips:
            locations.append((trip[1], trip[0])) # pessenger on
            locations.append((trip[2], -trip[0])) # pesenger off

        sorted(locations, key=lambda x: (x[0], x[1])) # pessenger off first, then on

        pessenger_count = 0
        for loc, pc in locations:
            pessenger_count += pc
            if pessenger_count > capacity:
                return False

        return True

def main():
    sol = Solution1()

    assert sol.carPooling([[9, 3, 4], [9, 1, 7], [4, 2, 4], [7, 4, 5]], 23) is True, 'fails'

    assert sol.carPooling([[2,1,5],[3,3,7]], 4) is False, 'fails'

    assert sol.carPooling([[2, 1, 5], [3, 3, 7]], 5) is True, 'fails'

    assert sol.carPooling([[2,1,5],[3,5,7]], 3) is True, 'fails'

    # assert sol.carPooling([[3,2,7],[3,7,9],[8,3,9]], 11) is True, 'fails'


if __name__ == '__main__':
   main()