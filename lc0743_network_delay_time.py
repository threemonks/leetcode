"""
743. Network Delay Time
Medium

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.



Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1


Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

"""
import collections
import math
from typing import List

"""
BFS

BFS traverse graph with weight (traveltime/delay from starting node to current node along this path)
queue里记录的是(node, arrivaltime) - arrivaltime is time to travel to this node from starting node along this path
then we have a global earliest_arrivaltime to record the earliest arrival time for each node from the starting node
Note: we don't use indegree==0 as start node is specified, instead, we loop all nodes until the queue is empty

time O(V+E)
"""


class Solution0:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = collections.defaultdict(list)
        traveltime_list = collections.defaultdict(int)
        for t in times:
            u, v, w = t
            adj_list[u].append(v)
            traveltime_list[(u, v)] = w

        q = collections.deque([(k, 0)])  # node and earliesttime to arrive to this node

        earliest_arrivaltime = dict()  # arrialtime for all nodes (except for starting node) default to inf
        for i in range(1, n + 1):
            earliest_arrivaltime[i] = math.inf
        earliest_arrivaltime[k] = 0

        while q:
            cur, arrivaltime = q.pop()
            for child in adj_list[cur]:
                if child not in arrivaltime or arrivaltime + traveltime_list[(cur, child)] < earliest_arrivaltime[
                    child]:
                    # if quicker path found
                    earliest_arrivaltime[child] = arrivaltime + traveltime_list[(cur, child)]
                    q.append((child, earliest_arrivaltime[child]))

        # print('earliest_arrivaltime=%s' % earliest_arrivaltime)
        # take max earliest_arrivaltime of all nodes (starting from k)
        ret = 0
        for node in earliest_arrivaltime:
            ret = max(ret, earliest_arrivaltime[node])

        if ret == 0 or ret == math.inf:
            return -1
        else:
            return ret


"""
Floyd algorithm (DP) - 求两点之间的最短路径 - can handle graph except for negative cycle
( all-pairs shortest path algorithm)
dp[i][j] represents best travel time from node i to j
基本思路是遍历所有节点k，看从节点i到节点j经过节点k是否对更新dp[i][j]有贡献
  dp[i][j] = min(dp[i][m]+dp[m][j] for all m from 1, ..., n)

time O(V^2E) - V: # of vertices; E: # of edges
"""


class Solution1:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        dp = [[math.inf / 2 for _ in range(n + 1)] for _ in range(n + 1)]

        for t in times:
            u, v, w = t
            dp[u][v] = w

        for i in range(1, n + 1):
            dp[i][i] = 0

        for m in range(1, n + 1):
            for j in range(1, n + 1):
                for i in range(1, n + 1):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m][j])

        ret = 0
        for j in range(1, n + 1):
            ret = max(ret, dp[k][j])

        if ret == 0 or ret == math.inf / 2:
            return -1
        else:
            return ret


import heapq

"""
Dijkstra's Algorithm
distance is traveltime
use heap to keep (traveltime, node), so that each time we pop out node with least distance

steps:
    1. create min heap queue to store (distance, node) of each node
    2. push source vertex into min heap queue
    3. pop the top node of min heap queue (vertex with minimum distance from start node)
    4. update distance of connected vertices (next vertex via adj_list) to the popped vertex in case "current vertex distance + edge weight < recorded next vertex distance", and push the next vertex with new distance into heap queue
    5. if the popped vertex is visited, skip it
    6. repeat until the queue is empty

time O(V+E)
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = collections.defaultdict(list)
        for t in times:
            u, v, w = t
            adj_list[u].append((v, w))

        q = [(0, k)]  # earliesttime to arrive, starting node
        heapq.heapify(q)

        dist = dict()
        while q:
            d, cur = heapq.heappop(q)
            if cur in dist: continue
            dist[cur] = d
            for child, dc in adj_list[cur]:
                if child not in dist:
                    heapq.heappush(q, (d + dc, child))

        # print('dist=%s' % dist)
        return max(dist.values()) if len(dist) == n else -1

def main():
    sol = Solution()
    assert sol.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2) == 2, 'fails'

    assert sol.networkDelayTime([[1,2,1]], n = 2, k = 1) == 1, 'fails'

    assert sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 2) == -1, 'fails'

if __name__ == '__main__':
   main()