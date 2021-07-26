"""
815. Bus Routes
Hard

1079

33

Add to List

Share
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.



Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1


Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106

"""
from collections import deque
from typing import List

"""
level order BFS - shortest path as all edges have weight 1

Observation:
The problem ask is to take least number of buses, so if we take bus as edge, stop as vertex, then this is a shortest path problem.

consider bus as vertex, a shared station would be an edge between the two buses (vertice)

the ask is to start from any one of the buses that has stop at source, and minimum number of vertices to go through to get to one of buses that stop at target

time O(N^2) - N^2 to build stop2bus and adj_list (N # of buses)
space O(N^2) - adj_list

mistakes:
1. if source and target are same stop, no bus needed
2. return -1 if no route possible
"""


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        n = len(routes)  # bus id

        # find the first bus we will be on, that covers stop source
        dq = deque()  # starting point

        # build a stop to bus map
        stop2bus = collections.defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop2bus[stop].append(bus)

        ending_buses = []
        adj_list = collections.defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop == source:
                    dq.append((bus, 1))  # starting bus
                if stop == target:
                    ending_buses.append(bus)
                reachable_buses = stop2bus[stop]
                for rb in reachable_buses:
                    adj_list[bus].append(rb)

        # convert ending buses to set for quick check
        ending_buses = set(ending_buses)

        visited = set()
        while dq:  # level order BFS guarantees the first time reaching target is the shortest path as all edge has weight 1
            cur, count = dq.popleft()
            if cur in ending_buses:
                return count
            for nxt in adj_list[cur]:
                if nxt not in visited:
                    dq.append((nxt, count + 1))
                    visited.add(nxt)

        return -1


def main():
    sol = Solution()
    assert sol.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6) == 2, 'fails'

    assert sol.numBusesToDestination(routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12) == -1, 'fails'


if __name__ == '__main__':
   main()