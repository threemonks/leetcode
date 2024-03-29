"""
134. Gas Station
Medium

3467

458

Add to List

Share
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique



Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.


Constraints:

gas.length == n
cost.length == n
1 <= n <= 10^4
0 <= gas[i], cost[i] <= 10^4

"""
from typing import List

"""
Two Pointers

circular route can be represented as an route of 1...2n

Use two pointer, keep a window size of n, we want to find a start of window where the sum of all diffs within this window > 0

notes:
1. use [stations] + [stations] to simulate circual stations list

time: O(N^2)
"""


class Solution0:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]

        sums = sum(diff)
        if sums < 0:
            return -1

        for i in range(n):
            if diff[i] < 0:
                continue
            tank = diff[i]
            for j in range(1, n + 1):
                k = (i + j) % n  # actual index within gas or cost or diff
                tank += diff[k]
                if tank < 0:
                    break

            # we have checked n stations, with all tank >= 0
            if tank >= 0:
                return i

        return -1


"""
Greedy / Math

1. if total gas > total cost, there must be a solution
2. if start at i, one cannot reach j, then start at any k (i<k<j) will not reach j either, then we should next try j+1 as a new start to explore

if we start at station i, could not reach some other station j, because from i to j, accumulated tank < 0, that means we cannot start from any station between i and j to reach j. So we should next try to start at station j instead.


time O(N)
space O(1)
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        start = 0
        curr_tank, total_tank = 0, 0
        for i in range(n):
            curr_tank += gas[i] - cost[i]
            total_tank += gas[i] - cost[i]
            if curr_tank < 0:
                start = i + 1  # if current station gas < cost, it cannot be start station
                curr_tank = 0

        if total_tank < 0:
            return -1
        else:
            return start

def main():
    sol = Solution()
    assert sol.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]) == 3, 'fails'

    assert sol.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]) == -1, 'fails'

if __name__ == '__main__':
   main()