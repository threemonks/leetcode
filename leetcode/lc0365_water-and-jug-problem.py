"""
365. Water and Jug Problem
Medium

512

946

Add to List

Share
You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.


Example 1:

Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
Output: true
Explanation: The famous Die Hard example
Example 2:

Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
Output: false
Example 3:

Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
Output: true


Constraints:

1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6
"""
"""
Math
"""


class Solution0:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:

        if x + y < z:  # water is finallly in one or both buckets
            return False

        if x == z or y == z or x + y == z:  # x or y = 0 case
            return True

        def gcd(a, b):
            while b != 0:
                b, a = a % b, b

            return a

        return z % gcd(x, y) == 0


"""
DFS

target state
x, y, z
0, y, z
0, 0, z
x, 0, z

can do operations, or BFS traverse methods
fill any of the jugs with water: x, or y
empty any of the jugs with water: -x, or -y
pour water from one jug into another till other jug is completely full or the first jug is empty: 

"""
from collections import deque


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False

        if x == z or y == z or x + y == z:  # nothing to do
            return True

        q = deque()

        q.append((0, 0))  # initial both jugs are empty
        visited = set((0, 0))

        while q:
            a, b = q.popleft()

            if a == z or b == z or a + b == z:
                return True

            states = []  # possible next states via various operation
            states.append([x, b])  # fill up x
            states.append([a, y])  # fill up y
            states.append([x, y])  # fill up both
            states.append([0, b])  # empty x
            states.append([a, 0])  # empty y
            states.append([0, 0])  # empty both
            states.append([0 if a + b < y else a + b - y, min(a + b, y)])  # pour a into b until a is empty or b is full
            states.append([min(a + b, x), 0 if a + b < x else a + b - x])  # pour b into a until b is empty or a is full
            for state in states:
                if tuple(state) not in visited:
                    q.append(state)
                    visited.add(tuple(state))

        return False

def main():
    sol = Solution()
    assert sol.canMeasureWater(x = 3, y = 5, z = 4) == True, 'fails'

    assert sol.canMeasureWater(x = 2, y = 6, z = 5) == False, 'fails'

    assert sol.canMeasureWater(x = 1, y = 2, z = 3) == True, 'fails'

if __name__ == '__main__':
   main()