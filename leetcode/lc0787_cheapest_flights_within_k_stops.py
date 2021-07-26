"""
787. Cheapest Flights Within K Stops
Medium

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.


Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.

"""
import collections
import math
from typing import List

"""
BFS Dijkstra's algorithm
SSSP (single source shortest path) in graph with positive weight => Dijkstra's algorithm

use minheap to store nodes to explore

Note: 1. queue stores (cost, stop, node) for each node
      2. each time we pop out node with smallest cost from queue to process
      3. we return the cost the first time we encounter target
      4. if we didn't encounter target when queue is empty, return -1

"""
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        m = len(flights)
        adj_list = collections.defaultdict(list)

        for f in flights:
            u, v, w = f
            adj_list[u].append((v, w))
        # print('adj_list=%s' % adj_list)

        q = [(0, 0, src)]  # node, and cost to get to this node from src, stops so far
        heapq.heapify(q)

        while q:
            # print('q=%s' % q)
            cost, stops, cur = heapq.heappop(q)
            # print('cur=%s cost=%s stops=%s q=%s' % (cur, cost, stops, q))
            if cur == dst:
                return cost
            if stops > K:  # used too many stops, cannot proceed this path
                continue
            for nxt, nxt_cost in adj_list[cur]:
                heapq.heappush(q, (cost + nxt_cost, stops + 1, nxt))

        return -1


"""
BFS with some modification

use brutal BFS traverse all possible paths, and keep record of path with lowest cost

Note: 1. use standard BFS to traverse all possible paths, and keep record of lowest cost found for each node (from source) in costs
      2. for each node, if lowest cost found, update costs dict
      3. skip exploring this node if
         i) its new cost is higher than its known lowest cost (from source)
         ii) steps to this node exceeds limit K
      4. for standard BFS traverse, we skip a (node, cost) if this (node, cost) has been achieved before (this slighly improve the performance) - not necessary

"""


class Solution1:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        m = len(flights)
        adj_list = collections.defaultdict(list)

        for f in flights:
            u, v, w = f
            adj_list[u].append((v, w))

        costs = [math.inf] * n
        costs[src] = 0

        q = collections.deque()
        q.append((src, 0, 0))  # node, and cost to get to this node from src, stops so far

        seen = set([(src, 0)])  # visited (node, cost)

        while q:
            cur, cost, stops = q.popleft()
            if cost < costs[cur]:
                costs[cur] = cost
            if costs[dst] < math.inf and cost > costs[
                dst]:  # this path is more expensive than known cheaper routes, no need to continue exploring
                continue
            # print('cur=%s cost=%s stops=%s costs=%s' % (cur, cost, stops, costs))
            if stops > K:  # used too many stops
                continue
            for nxt in adj_list[cur]:
                nxt_city, nxt_cost = nxt
                if nxt_city not in seen:
                    q.append((nxt_city, cost + nxt_cost, stops + 1))
                    seen.add(nxt)

        # print(costs)
        return costs[dst] if costs[dst] < math.inf else -1


"""
Bellman-Ford
However, Dijkstra's algorithm uses a priority queue to greedily select the closest vertex that has not yet been processed, and performs this relaxation process on all of its outgoing edges; by contrast, the Bellman-Ford algorithm simply relaxes all the edges and does this {|V|-1}∣V∣−1 times, where |V|∣V∣ is the number of vertices in the graph.

time O(E*K)
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dist = [math.inf] * n
        dist[src] = 0
        for _ in range(K + 1):
            dist2 = dist[:]
            for u, v, w in flights:
                if dist2[v] > dist[u] + w:
                    dist2[v] = dist[u] + w
            dist = dist2[:]
        if dist[dst] < math.inf:
            return dist[dst]
        else:
            return -1

def main():
    sol = Solution()
    assert sol.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 1) == 200, 'fails'

    assert sol.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 0) == 500, 'fails'

if __name__ == '__main__':
   main()